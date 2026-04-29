#!/usr/bin/env bash
# Auditoría Netlify + MailerLite — ejecutar en tu máquina local.
#
# Requisitos:
#   - bash, curl, jq (instalar jq con: brew install jq  /  apt install jq)
#   - Tokens en .env.audit (se cargan automáticamente) o exportados:
#       NETLIFY_AUTH_TOKEN  (https://app.netlify.com/user/applications)
#       MAILERLITE_API_KEY  (https://dashboard.mailerlite.com → Integrations → API)
#
# Uso:
#   bash scripts/audit-mailerlite-netlify.sh
#
# El script NO imprime las claves ni los valores de env vars. Solo metadata.

set -u

# -------- Carga de credenciales -----------------------------------------
if [ -f ".env.audit" ]; then
  set -a; . ./.env.audit; set +a
fi

NETLIFY_TOKEN="${NETLIFY_AUTH_TOKEN:-}"
ML_TOKEN="${MAILERLITE_API_KEY:-}"

if ! command -v jq >/dev/null; then
  echo "ERROR: falta jq. Instálalo: brew install jq  (o apt install jq)" >&2
  exit 1
fi

hr() { printf '\n────────────────────────────────────────────────────────\n%s\n────────────────────────────────────────────────────────\n' "$1"; }
ok() { printf '  ✓ %s\n' "$1"; }
warn() { printf '  ⚠ %s\n' "$1"; }
fail() { printf '  ✗ %s\n' "$1"; }

# =========================================================================
# NETLIFY
# =========================================================================
hr "NETLIFY"

if [ -z "$NETLIFY_TOKEN" ]; then
  fail "NETLIFY_AUTH_TOKEN no definido. Saltando Netlify."
else
  N_HDR=(-H "Authorization: Bearer $NETLIFY_TOKEN")

  # User
  USER_JSON=$(curl -s "${N_HDR[@]}" https://api.netlify.com/api/v1/user)
  USER_EMAIL=$(echo "$USER_JSON" | jq -r '.email // "ERROR"')
  if [ "$USER_EMAIL" = "ERROR" ]; then
    fail "Token Netlify rechazado. Respuesta: $(echo "$USER_JSON" | jq -c '.')"
  else
    ok "Autenticado como: $USER_EMAIL"
  fi

  # Buscar el site twimproject
  SITES_JSON=$(curl -s "${N_HDR[@]}" "https://api.netlify.com/api/v1/sites?filter=all&per_page=200")
  SITE_ID=$(echo "$SITES_JSON" | jq -r '.[] | select(.url | test("twimproject"; "i")) | .id' | head -1)
  SITE_NAME=$(echo "$SITES_JSON" | jq -r '.[] | select(.url | test("twimproject"; "i")) | .name' | head -1)
  SITE_URL=$(echo "$SITES_JSON" | jq -r '.[] | select(.url | test("twimproject"; "i")) | .url' | head -1)

  if [ -z "$SITE_ID" ]; then
    warn "No se encontró un site con 'twimproject' en la URL. Sites disponibles:"
    echo "$SITES_JSON" | jq -r '.[] | "    - \(.name) [\(.url)]"'
  else
    ok "Site: $SITE_NAME ($SITE_URL) id=$SITE_ID"

    # Env vars (solo claves, no valores)
    hr "Netlify · Variables de entorno (solo nombres)"
    ACCOUNT_SLUG=$(echo "$SITES_JSON" | jq -r --arg id "$SITE_ID" '.[] | select(.id==$id) | .account_slug')
    ENV_JSON=$(curl -s "${N_HDR[@]}" "https://api.netlify.com/api/v1/accounts/$ACCOUNT_SLUG/env?site_id=$SITE_ID")
    if echo "$ENV_JSON" | jq -e 'type == "array"' >/dev/null 2>&1; then
      KEYS=$(echo "$ENV_JSON" | jq -r '.[].key' | sort)
      echo "$KEYS" | sed 's/^/  · /'
      echo
      # Comprobar las críticas
      EXPECTED=("MAILERLITE_API_KEY" "MAILERLITE_GROUP_RETO" "MAILERLITE_GROUP_GENERAL" "MAILERLITE_GROUP_LEAD_MAGNET" "MAILERLITE_GROUP_PADRES_TDAH" "MAILERLITE_GROUP_PADRES_BACH" "MAILERLITE_GROUP_PADRES_TALLERES")
      for k in "${EXPECTED[@]}"; do
        if echo "$KEYS" | grep -qx "$k"; then ok "$k presente"; else warn "$k FALTANTE"; fi
      done
    else
      fail "No pude leer env vars (puede que el token no tenga ese permiso): $(echo "$ENV_JSON" | jq -c '.')"
    fi

    # Functions
    hr "Netlify · Functions"
    FN_JSON=$(curl -s "${N_HDR[@]}" "https://api.netlify.com/api/v1/sites/$SITE_ID/functions")
    if echo "$FN_JSON" | jq -e 'type == "array" or .functions' >/dev/null 2>&1; then
      echo "$FN_JSON" | jq -r '(.functions // .) | .[].name? // .' | sed 's/^/  · /'
    else
      warn "No se pudieron listar las functions: $(echo "$FN_JSON" | jq -c '.' 2>/dev/null | head -c 200)"
    fi

    # Últimos 5 deploys
    hr "Netlify · Últimos 5 deploys"
    DEPLOYS=$(curl -s "${N_HDR[@]}" "https://api.netlify.com/api/v1/sites/$SITE_ID/deploys?per_page=5")
    echo "$DEPLOYS" | jq -r '.[] | "  · \(.created_at) [\(.state)] \(.title // .commit_ref // "-") (branch: \(.branch))"'
  fi
fi

# =========================================================================
# MAILERLITE
# =========================================================================
hr "MAILERLITE"

if [ -z "$ML_TOKEN" ]; then
  warn "MAILERLITE_API_KEY no definido. Saltando MailerLite."
  warn "Para auditarlo: añade MAILERLITE_API_KEY=xxxx a .env.audit y vuelve a lanzar."
else
  ML_HDR=(-H "Authorization: Bearer $ML_TOKEN" -H "Accept: application/json")

  # Account info
  ACC_JSON=$(curl -s "${ML_HDR[@]}" "https://connect.mailerlite.com/api/account")
  ACC_NAME=$(echo "$ACC_JSON" | jq -r '.data.account_name // .data.company // "ERROR"' 2>/dev/null)
  if [ "$ACC_NAME" = "ERROR" ] || [ -z "$ACC_NAME" ]; then
    # API alternativa
    ACC_JSON=$(curl -s "${ML_HDR[@]}" "https://connect.mailerlite.com/api/me")
    ACC_NAME=$(echo "$ACC_JSON" | jq -r '.data.account.name // .data.email // "?"')
  fi
  ok "Cuenta MailerLite: $ACC_NAME"

  # Groups
  hr "MailerLite · Grupos"
  GROUPS_JSON=$(curl -s "${ML_HDR[@]}" "https://connect.mailerlite.com/api/groups?limit=100")
  if echo "$GROUPS_JSON" | jq -e '.data' >/dev/null 2>&1; then
    echo "$GROUPS_JSON" | jq -r '.data[] | "  · [\(.id)] \(.name)  → \(.active_count) activos / \(.total // .total_count // 0) totales"'
    echo
    # Verificar grupo del Reto
    RETO=$(echo "$GROUPS_JSON" | jq -r '.data[] | select(.name | test("reto"; "i")) | .id' | head -1)
    if [ -n "$RETO" ]; then
      ok "Grupo del Reto encontrado: id=$RETO"
    else
      warn "No se encontró grupo con 'Reto' en el nombre"
    fi
  else
    fail "Error leyendo grupos: $(echo "$GROUPS_JSON" | jq -c '.')"
  fi

  # Automations
  hr "MailerLite · Automatizaciones"
  AUTOS=$(curl -s "${ML_HDR[@]}" "https://connect.mailerlite.com/api/automations?limit=50")
  if echo "$AUTOS" | jq -e '.data' >/dev/null 2>&1; then
    echo "$AUTOS" | jq -r '.data[] | "  · [\(.id)] \(.name)
      Estado: \(.enabled // .status)  · Activos: \(.stats.subscribers_in_queue_count // 0)  · Completados: \(.stats.completed_subscribers_count // 0)"'
    echo
    # Buscar la del Reto
    RETO_AUTO=$(echo "$AUTOS" | jq -r '.data[] | select(.name | test("reto"; "i")) | .id' | head -1)
    if [ -n "$RETO_AUTO" ]; then
      ok "Automatización del Reto encontrada: id=$RETO_AUTO"
      # Detalle de la automatización
      hr "MailerLite · Detalle automatización Reto"
      DETAIL=$(curl -s "${ML_HDR[@]}" "https://connect.mailerlite.com/api/automations/$RETO_AUTO")
      echo "$DETAIL" | jq '{name: .data.name, enabled: .data.enabled, status: .data.status, trigger: .data.triggers, steps: (.data.steps | length // .data.flow | length // 0)}'
    else
      warn "No se encontró automatización con 'Reto' en el nombre"
    fi
  else
    fail "Error leyendo automatizaciones: $(echo "$AUTOS" | jq -c '.')"
  fi

  # Campañas recientes (últimas 10)
  hr "MailerLite · Últimas 10 campañas/envíos"
  CAMPS=$(curl -s "${ML_HDR[@]}" "https://connect.mailerlite.com/api/campaigns?limit=10")
  echo "$CAMPS" | jq -r '.data[]? | "  · [\(.status)] \(.name)  · enviados: \(.stats.sent // 0)  · open rate: \(.stats.open_rate.float // 0)"' 2>/dev/null || warn "No se pudieron leer campañas"

  # Dominios
  hr "MailerLite · Dominios"
  DOMS=$(curl -s "${ML_HDR[@]}" "https://connect.mailerlite.com/api/domains")
  echo "$DOMS" | jq -r '.data[]? | "  · \(.name)  · SPF: \(.dns.spf.is_verified // "?")  · DKIM: \(.dns.dkim.is_verified // "?")"' 2>/dev/null || echo "  (endpoint no disponible o sin dominios)"
fi

hr "FIN"
echo "Pega este output en el chat (es seguro: no contiene tokens ni valores de env vars)."
