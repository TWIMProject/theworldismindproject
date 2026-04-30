# Probe: ¿la API pública de MailerLite v3 expone algún endpoint para activar
# (enabled=true) una automation? La doc oficial no lo menciona, pero a veces hay
# rutas no documentadas. Este script intenta 3 variantes contra los 2 talleres
# en draft y registra el status HTTP + body de cada intento.
#
# Uso:
#   1. .env.audit en raíz con MAILERLITE_API_KEY=xxxx (mismo patrón que audit)
#   2. powershell -ExecutionPolicy Bypass -File scripts/probe-mailerlite-enable-automation.ps1
#
# El script NO modifica nada si los endpoints no existen — sólo registra qué
# devuelve la API. Si alguno responde 200/201/204, entonces la automation
# quedaría activada (verificable después con GET).

$ErrorActionPreference = 'Continue'

if (Test-Path ".env.audit") {
  Get-Content ".env.audit" | ForEach-Object {
    if ($_ -match '^\s*([A-Z_][A-Z0-9_]*)\s*=\s*(.+?)\s*$') {
      [Environment]::SetEnvironmentVariable($matches[1], $matches[2], 'Process')
    }
  }
}

$ML_TOKEN = $env:MAILERLITE_API_KEY
if (-not $ML_TOKEN) {
  Write-Host "[FAIL] MAILERLITE_API_KEY no definido en .env.audit" -ForegroundColor Red
  exit 1
}

$automations = @(
  @{ id = "186094472462862106"; label = "TDAH" },
  @{ id = "186094552519541764"; label = "Bachillerato" }
)

# Variantes a probar. Formato: METHOD path body
$variants = @(
  @{ method = "PUT";  path = "/api/automations/{id}";         body = '{"enabled":true}' },
  @{ method = "POST"; path = "/api/automations/{id}/enable";  body = '' },
  @{ method = "POST"; path = "/api/automations/{id}/start";   body = '' },
  @{ method = "POST"; path = "/api/automations/{id}/activate";body = '' }
)

$headers = @{
  Authorization = "Bearer $ML_TOKEN"
  "Content-Type" = "application/json"
  Accept = "application/json"
}

foreach ($auto in $automations) {
  Write-Host ""
  Write-Host ("═" * 70)
  Write-Host "Automation $($auto.label) · id=$($auto.id)"
  Write-Host ("═" * 70)

  foreach ($v in $variants) {
    $url = "https://connect.mailerlite.com" + ($v.path -replace '\{id\}', $auto.id)
    Write-Host ""
    Write-Host "→ $($v.method) $url"

    try {
      if ($v.body) {
        $resp = Invoke-WebRequest -Uri $url -Method $v.method -Headers $headers -Body $v.body -SkipHttpErrorCheck
      } else {
        $resp = Invoke-WebRequest -Uri $url -Method $v.method -Headers $headers -SkipHttpErrorCheck
      }
      Write-Host "   status: $($resp.StatusCode) $($resp.StatusDescription)"
      if ($resp.Content) {
        $snippet = $resp.Content
        if ($snippet.Length -gt 400) { $snippet = $snippet.Substring(0,400) + "…" }
        Write-Host "   body  : $snippet"
      }
    } catch {
      Write-Host "   ERR   : $($_.Exception.Message)" -ForegroundColor Yellow
    }
  }

  # Verificación final: ¿quedó enabled?
  Write-Host ""
  Write-Host "→ Verificación GET /api/automations/$($auto.id)"
  try {
    $get = Invoke-RestMethod -Uri "https://connect.mailerlite.com/api/automations/$($auto.id)" -Headers $headers -Method Get
    Write-Host "   enabled = $($get.data.enabled)"
  } catch {
    Write-Host "   ERR: $($_.Exception.Message)" -ForegroundColor Yellow
  }
}

Write-Host ""
Write-Host ("═" * 70)
Write-Host "Pega el output entero en el chat. Si todas las variantes devuelven"
Write-Host "404/405, queda confirmado que el toggle es dashboard-only."
Write-Host ("═" * 70)
