# Embudo Directo 7 jun · estado y pendientes (al 2 jun 2026, noche)

> Auditoría + intervención parcial del embudo. Quedan tareas de envío real que hay que hacer con cabeza fresca antes del 6-7 jun. **Leer el «aprendizaje crítico» antes de tocar campañas.**

## ✅ Hecho y verificado
- **E3** (`187809536941229345`, día D): programada **domingo 7 jun 10:00 CEST** (`scheduled_for 2026-06-07 08:00:00` UTC). Enlace Meet `https://meet.google.com/fsu-scrz-res` OK, español, solo grupo Directo (`187662493483533365`, 9 inscritos). Correcta.
- **Carta promo** (`187974522939377362`): 3 jun 19:00 CEST, español, todos los activos. Correcta.

## ⏳ PENDIENTE (antes del sáb 6 / dom 7)
1. **E2** (`187809525929084347`, víspera) — **EN DRAFT, ROTA.** Tenía error «Domingo 8» (debe ser **7**). Al intentar corregir con `update_campaign` se rompió: grupo reseteado a **all_active (59)** + idioma a **en-US** + el texto NO se corrigió. **No se envía (draft).** → **Recrear con `create_campaign`** pasando juntos: content con «Domingo **7**, 19:00», `groups:["187662493483533365"]`, `language` español. Borrar la rota. Programar **sáb 6 jun 19:00**.
2. **E4** (`187809546704520781`, «en 1 hora») — DRAFT. **Verificar subtítulo** (probable «Domingo 8» → 7). Programar **dom 7 jun 18:00**.
3. **E5** (`187809557833058027`, post) — DRAFT. **No programar** hasta tener el enlace de la grabación. Programar **lun 8 jun ~10:00** (Cap III + grabación).
4. **Automation de confirmación «Estás dentro»** (`187662509833979144`) — **NO aparece** en la cuenta (solo hay 2 automations, de talleres, ambas deshabilitadas). Los inscritos NO reciben confirmación al registrarse. → Recrear la automation de bienvenida del grupo Directo.
5. **Inscritos: 9** (objetivo 30-60). Difundir el Share URL del formulario (redes/reels) esta semana.

## ⚠️ APRENDIZAJE CRÍTICO (no repetir)
`update_campaign` sobre una campaña dirigida a un grupo **resetea el destinatario a `all_active_subscribers` y cambia `language_id` a en-US**, y no aplica el `content` de forma fiable. **Nunca** usarlo para editar el contenido de una campaña con grupo. En su lugar: `create_campaign(content, groups, language)` + borrar la vieja. Confirmado en vivo el 2 jun (ya estaba avisado en `directo-la-voz-que-te-juzga-8-jun-2026.md` §9.2).

## Calibración zona horaria (verificada)
`schedule_campaign` interpreta `date/hours/minutes` en **hora local de la cuenta (CEST)** y almacena en UTC (19:00 CEST → 17:00 UTC). Pasar la hora CEST directamente. **Verificar siempre `scheduled_for`** tras programar.
