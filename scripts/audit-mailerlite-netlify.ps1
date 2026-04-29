# Auditoría Netlify + MailerLite - versión PowerShell para Windows 11.
#
# Uso:
#   1. Crea un fichero .env.audit en la raíz del repo con:
#        NETLIFY_AUTH_TOKEN=nfp_xxxx
#        MAILERLITE_API_KEY=xxxx
#   2. Abre PowerShell en la carpeta del repo y ejecuta:
#        powershell -ExecutionPolicy Bypass -File scripts/audit-mailerlite-netlify.ps1
#
# El output NO contiene tokens ni valores de env vars: solo metadata.

$ErrorActionPreference = 'Continue'

# -------- Carga de credenciales desde .env.audit --------
if (Test-Path ".env.audit") {
  Get-Content ".env.audit" | ForEach-Object {
    if ($_ -match '^\s*([A-Z_][A-Z0-9_]*)\s*=\s*(.+?)\s*$') {
      [Environment]::SetEnvironmentVariable($matches[1], $matches[2], 'Process')
    }
  }
}

$NETLIFY_TOKEN = $env:NETLIFY_AUTH_TOKEN
$ML_TOKEN      = $env:MAILERLITE_API_KEY

function Hr([string]$t) { Write-Host ""; Write-Host ("─" * 60); Write-Host $t; Write-Host ("─" * 60) }
function Ok([string]$t)   { Write-Host "  [OK]   $t" -ForegroundColor Green }
function Warn([string]$t) { Write-Host "  [WARN] $t" -ForegroundColor Yellow }
function Fail([string]$t) { Write-Host "  [FAIL] $t" -ForegroundColor Red }

function Invoke-Api {
  param([string]$Url, [hashtable]$Headers)
  try {
    return Invoke-RestMethod -Uri $Url -Headers $Headers -Method Get -ErrorAction Stop
  } catch {
    return @{ __error = $_.Exception.Message }
  }
}

# =========================================================================
# NETLIFY
# =========================================================================
Hr "NETLIFY"

if (-not $NETLIFY_TOKEN) {
  Fail "NETLIFY_AUTH_TOKEN no definido. Saltando Netlify."
} else {
  $nh = @{ Authorization = "Bearer $NETLIFY_TOKEN" }

  $user = Invoke-Api "https://api.netlify.com/api/v1/user" $nh
  if ($user.__error) {
    Fail "Token Netlify rechazado: $($user.__error)"
  } else {
    Ok "Autenticado como: $($user.email)"

    $sites = Invoke-Api "https://api.netlify.com/api/v1/sites?filter=all&per_page=200" $nh
    $site = $sites | Where-Object { $_.url -match 'twimproject' } | Select-Object -First 1

    if (-not $site) {
      Warn "No se encontró un site con 'twimproject' en la URL. Sites disponibles:"
      $sites | ForEach-Object { Write-Host "    - $($_.name) [$($_.url)]" }
    } else {
      Ok "Site: $($site.name) ($($site.url)) id=$($site.id)"

      Hr "Netlify · Variables de entorno (solo nombres)"
      $envs = Invoke-Api "https://api.netlify.com/api/v1/accounts/$($site.account_slug)/env?site_id=$($site.id)" $nh
      if ($envs -is [array]) {
        $keys = $envs | ForEach-Object { $_.key } | Sort-Object
        $keys | ForEach-Object { Write-Host "  · $_" }

        $expected = @(
          "MAILERLITE_API_KEY",
          "MAILERLITE_GROUP_RETO",
          "MAILERLITE_GROUP_GENERAL",
          "MAILERLITE_GROUP_LEAD_MAGNET",
          "MAILERLITE_GROUP_PADRES_TDAH",
          "MAILERLITE_GROUP_PADRES_BACH",
          "MAILERLITE_GROUP_PADRES_TALLERES"
        )
        Write-Host ""
        foreach ($k in $expected) {
          if ($keys -contains $k) { Ok "$k presente" } else { Warn "$k FALTANTE" }
        }
      } else {
        Fail "No pude leer env vars (¿token sin permiso?): $($envs | ConvertTo-Json -Compress -Depth 3)"
      }

      Hr "Netlify · Functions"
      $fns = Invoke-Api "https://api.netlify.com/api/v1/sites/$($site.id)/functions" $nh
      if ($fns.functions) { $fns.functions | ForEach-Object { Write-Host "  · $($_.name)" } }
      elseif ($fns -is [array]) { $fns | ForEach-Object { Write-Host "  · $($_.name)" } }
      else { Warn "No se pudieron listar functions: $($fns | ConvertTo-Json -Compress -Depth 3)" }

      Hr "Netlify · Últimos 5 deploys"
      $deploys = Invoke-Api "https://api.netlify.com/api/v1/sites/$($site.id)/deploys?per_page=5" $nh
      $deploys | ForEach-Object {
        $title = if ($_.title) { $_.title } elseif ($_.commit_ref) { $_.commit_ref } else { "-" }
        Write-Host "  · $($_.created_at) [$($_.state)] $title (branch: $($_.branch))"
      }
    }
  }
}

# =========================================================================
# MAILERLITE
# =========================================================================
Hr "MAILERLITE"

if (-not $ML_TOKEN) {
  Warn "MAILERLITE_API_KEY no definido. Saltando MailerLite."
  Warn "Para auditarlo: añade MAILERLITE_API_KEY=xxxx a .env.audit y vuelve a lanzar."
} else {
  $mh = @{ Authorization = "Bearer $ML_TOKEN"; Accept = "application/json" }

  $me = Invoke-Api "https://connect.mailerlite.com/api/me" $mh
  if ($me.__error) { Fail "Error MailerLite: $($me.__error)" }
  else { Ok "Cuenta MailerLite: $($me.data.account.name) ($($me.data.email))" }

  Hr "MailerLite · Grupos"
  $groups = Invoke-Api "https://connect.mailerlite.com/api/groups?limit=100" $mh
  if ($groups.data) {
    $groups.data | ForEach-Object {
      Write-Host "  · [$($_.id)] $($_.name)  → $($_.active_count) activos / $($_.total_count) totales"
    }
    Write-Host ""
    $reto = $groups.data | Where-Object { $_.name -match '(?i)reto' } | Select-Object -First 1
    if ($reto) { Ok "Grupo del Reto encontrado: id=$($reto.id) nombre='$($reto.name)' activos=$($reto.active_count)" }
    else { Warn "No se encontró grupo con 'Reto' en el nombre" }
  } else { Fail "Error leyendo grupos: $($groups | ConvertTo-Json -Compress -Depth 3)" }

  Hr "MailerLite · Automatizaciones"
  $autos = Invoke-Api "https://connect.mailerlite.com/api/automations?limit=50" $mh
  if ($autos.data) {
    $autos.data | ForEach-Object {
      $estado = if ($_.enabled -ne $null) { if ($_.enabled) { "ACTIVA" } else { "PAUSADA" } } else { $_.status }
      Write-Host "  · [$($_.id)] $($_.name)  · Estado: $estado"
      if ($_.stats) { Write-Host "      en queue: $($_.stats.subscribers_in_queue_count)  · completados: $($_.stats.completed_subscribers_count)" }
    }
    Write-Host ""
    $retoAuto = $autos.data | Where-Object { $_.name -match '(?i)reto' } | Select-Object -First 1
    if ($retoAuto) {
      Ok "Automatización del Reto encontrada: id=$($retoAuto.id)"
      Hr "MailerLite · Detalle automatización Reto"
      $detail = Invoke-Api "https://connect.mailerlite.com/api/automations/$($retoAuto.id)" $mh
      $detail.data | Select-Object name, enabled, status, triggers | Format-List
      if ($detail.data.steps)      { Write-Host "  Pasos: $($detail.data.steps.Count)" }
      elseif ($detail.data.flow)   { Write-Host "  Pasos: $($detail.data.flow.Count)" }
    } else { Warn "No se encontró automatización con 'Reto' en el nombre" }
  } else { Fail "Error leyendo automatizaciones: $($autos | ConvertTo-Json -Compress -Depth 3)" }

  Hr "MailerLite · Últimas 10 campañas"
  $camps = Invoke-Api "https://connect.mailerlite.com/api/campaigns?limit=10" $mh
  if ($camps.data) {
    $camps.data | ForEach-Object {
      $sent = if ($_.stats.sent) { $_.stats.sent } else { 0 }
      $opens = if ($_.stats.opens_count) { $_.stats.opens_count } else { 0 }
      Write-Host "  · [$($_.status)] $($_.name)  · enviados: $sent  · aperturas: $opens"
    }
  }

  Hr "MailerLite · Dominios autenticados"
  $doms = Invoke-Api "https://connect.mailerlite.com/api/domains" $mh
  if ($doms.data) {
    $doms.data | ForEach-Object {
      $spf = $_.dns.spf.is_verified
      $dkim = $_.dns.dkim.is_verified
      Write-Host "  · $($_.name)  · SPF: $spf  · DKIM: $dkim"
    }
  } else { Write-Host "  (sin dominios o endpoint no disponible)" }
}

Hr "FIN"
Write-Host "Pega este output en el chat. Es seguro: no contiene tokens ni valores de env vars."
