#!/usr/bin/env bash
# TWIM Project · hook SessionStart
# Imprime los hitos del calendario operativo con su estado de urgencia
# y los devuelve como additionalContext para que Claude los lea al iniciar sesión.
#
# Patrón Consent Mode v2 del Claude Code: hook stdin recibe JSON (no se usa aquí),
# stdout debe ser JSON con hookSpecificOutput.additionalContext para inyectar
# texto al contexto del modelo.
#
# Portable Mac+Linux · usa Python 3.

python3 - <<'PY'
import datetime, json

today = datetime.date.today()
items = [
    ("2026-05-26", "crear doc métricas Carrusel #3 a 7 días"),
    ("2026-06-03", "carta promo Directo · verificar idioma a Español en panel MailerLite antes del envío 19:00 CEST"),
    ("2026-06-08", "Directo «La voz que te juzga» 19:00 CEST vía Meet"),
    ("2026-06-15", "inicio ventana grabación «Deja de Buscarte en Otros»"),
    ("2026-07-28", "cierre ventana grabación DDBEO (tope agosto)"),
    ("2026-09-01", "apertura pre-venta dura del taller «Volver a Mí» + Meta Ads"),
    ("2026-09-30", "S1 del taller «Volver a Mí» · 20:00 CEST"),
]

lines = [f"[recordatorio hitos calendario TWIM al {today.isoformat()}]"]
for fecha, desc in items:
    d = datetime.date.fromisoformat(fecha)
    diff = (d - today).days
    if diff < 0:
        estado = f"[vencido · hace {-diff}d]"
    elif diff == 0:
        estado = "[HOY]"
    elif diff <= 7:
        estado = f"[próximo · en {diff}d]"
    elif diff <= 30:
        estado = f"[<30d · en {diff}d]"
    else:
        estado = f"[futuro · en {diff}d]"
    lines.append(f"  {estado} {fecha} · {desc}")

output = "\n".join(lines)
print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": output}}, ensure_ascii=False))
PY
