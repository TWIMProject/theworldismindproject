# Embudo Directo 7 jun · estado y pendientes (al 2 jun 2026, noche)

> Auditoría + intervención del embudo. **Leer el «aprendizaje crítico» antes de tocar campañas.**

## ✅ Hecho y verificado (campañas recordatorio, todas al grupo Directo `187662493483533365`, 9 inscritos)
- **E2** víspera (nueva `189196741644388190`): **sáb 6 jun 19:00 CEST** (`2026-06-06 17:00 UTC`). Texto «Domingo **7**» corregido, enlace Meet OK. (La vieja `187809525929084347`, rota por `update_campaign`, fue borrada.)
- **E3** día D (`187809536941229345`): **dom 7 jun 10:00 CEST** (`08:00 UTC`). Enlace Meet OK.
- **E4** «en 1 hora» (nueva `189196809348843111`): **dom 7 jun 18:00 CEST** (`16:00 UTC`). Enlace Meet OK. (La vieja `187809546704520781` fue borrada.)
- **Carta promo** (`187974522939377362`): 3 jun 19:00 CEST, español, todos los activos.

## ⏳ PENDIENTE
1. **E5** post-directo (`187809557833058027`) — DRAFT. **No programar** hasta tener el enlace de la grabación (lunes). Programar **lun 8 jun ~10:00** con Cap III + grabación. Si hay que editar texto, **recrear con `create_campaign`** (no `update`). Verificar que no diga «8 jun».
2. **Automation de confirmación «Estás dentro»** (`187662509833979144`) — **NO existe** en la cuenta (solo hay 2 automations, de talleres, deshabilitadas). Los inscritos no reciben confirmación. → **Daniel: verificar/recrear/activar en el panel** (activar no es vía API).
3. **Inscritos: 9** (objetivo 30-60). → **Daniel: difundir el Share URL del formulario** (redes/reels) esta semana. Es lo que más decide que el directo «salga bien».

## ⚠️ APRENDIZAJE CRÍTICO (confirmado en vivo 2 jun)
`update_campaign` sobre una campaña con grupo **resetea el destinatario a `all_active_subscribers` (59)** y cambia `language_id` a en-US, y no aplica el `content` de forma fiable. **Nunca** para editar contenido de campaña con grupo. Vía correcta: `create_campaign(content, groups)` + `schedule_campaign` + borrar la vieja. (`create_campaign` no acepta `language`: nace en en-US; el pie legal sale en inglés pero el HTML lleva footer propio en español — aceptable.)

## Calibración zona horaria (verificada)
`schedule_campaign` interpreta `date/hours/minutes` en **hora local CEST**; almacena en UTC (19:00 CEST → 17:00 UTC). Verificar siempre `scheduled_for`.
