# Cierre de sesión · 14 jun 2026 (domingo)

> Sesión larga, con Daniel al portátil ejecutando en paralelo. Foco: dejar la app DLQD lista para difundir + accionar el checklist que solo podía hacer él + cancelar el Directo de hoy por indisposición.

## App «Di lo que quieres decir» — lista para difundir

- **Clave Anthropic rotada y verificada.** Daniel creó clave nueva (termina en `dAAA`), está en Production/Functions; el diag (`/.netlify/functions/traductor-interno?diag=1`) devuelve `clave_configurada:true` con modelo `claude-haiku-4-5-20251001`. **Clave vieja (la expuesta en chat el 12 jun) revocada en console.anthropic.com.** Riesgo de seguridad cerrado.
- **Límite de gasto Anthropic:** 50 (con notificación a 40). Más prepago como techo natural. Guardián de costes resuelto.
- **Entrega del código por email arreglada (PR #356, mergeado):** `subscribe.js` ahora escribe `dlqd_codigo` en el momento del alta (mismo HMAC determinista), para que la carta de bienvenida lo incluya sin carrera de tiempos. **Decisión: NO se monta el proveedor de Netlify Emails** — MailerLite entrega el código en la bienvenida y la app lo muestra en pantalla. Dos vías, cero infraestructura nueva.
- **Carta de bienvenida «Web - Newsletter Home»:** Daniel añadió el bloque del código (`{$dlqd_codigo}`) e idioma español. Activada.
- **Cookies (PR #357, mergeado) — rectificación importante:** el sitio YA cumplía RGPD/LSSI desde mayo con `assets/twim-cookie-consent.js` (banner + Google Consent Mode v2 que bloquea GA4/Meta/Google Ads hasta consentimiento). **NO se quitó GA4** (habría roto el seguimiento de la campaña de Google Ads activa). La única página fuera del patrón era la propia app: se le añadió el mismo banner + consent default. Tema cerrado, sin coste (no se contrató Plausible; el plan Netlify de 9 ya incluye analítica sin cookies).
- **Carrusel IG de lanzamiento v2 (#352, en main):** 7 slides PNG con el arranque por identificación que pidió Daniel («Seguro que te ha pasado…»). Publicar ≥15 jun.
- **Prueba end-to-end (Daniel):** análisis correcto, puerta de suscripción correcta, código en pantalla correcto. El email de bienvenida no le llegó **porque su email ya estaba suscrito** (la automation no se redispara para quien ya está en el grupo) — no es fallo; con email nuevo sí llega.

## Backfill de códigos a suscriptores existentes (#358, #359 — endpoint ya borrado)

- Se creó un endpoint one-off (`dlqd-backfill`) protegido por token para escribir `dlqd_codigo` en los suscriptores que ya existían (la automation de bienvenida no se les redispara). Ejecutado: **todos los suscriptores ACTIVOS quedaron con código** (65; los ~17 restantes eran bajas/rebotes que se omiten). 
- **Limpieza de seguridad hecha al cierre:** env var `DLQD_ADMIN_TOKEN` borrada en Netlify y endpoint `netlify/functions/dlqd-backfill.js` eliminado del repo. El campo `dlqd_codigo` queda escrito para todos los activos (por si en el futuro se quiere una campaña con el código a toda la lista).

## Directo «La voz que te juzga» (14 jun) — CANCELADO por indisposición

- Daniel indispuesto. Instrucción: cancelar, decir que **no hay fecha prevista** (para evitar nuevas cancelaciones de última hora), dar el código de la app y explicar la app en el correo.
- **Cancelada la campaña automática «E4 · en una hora»** (id 189196809348843111) que iba a salir hoy 20:30 — crítico, evitaba el recordatorio de un directo cancelado.
- **Enviada campaña de cancelación** (id 190268255528552136) al grupo «Lead · Directo · La voz que te juzga (14 jun)» (187662493483533365), **17 inscritos, todos activos y con su código** verificado uno a uno. En español (corregido vía API el idioma, que el MCP había puesto en inglés). Incluye: disculpa por indisposición, sin fecha nueva, código personal `{$dlqd_codigo}` + explicación de la app.
- **Autoauditoría que evitó un fallo grave:** al corregir el idioma vía PUT, la API reseteó el destinatario a «todos los suscriptores» (65); se detectó y restauró el filtro al grupo del directo (17) antes de enviar.
- **Aviso de método:** el MCP de MailerLite NO permite fijar idioma al crear campaña (lo pone en inglés por defecto — incidente recurrente). Se corrige con `batch_requests` PUT `language_id:8`, pero **ese PUT borra el filtro de grupos si no se reenvía `groups`** — reenviarlo siempre.

## Pendiente / mañana (15 jun)

- **Foco: la app a full** (Daniel) + **empezar a grabar DDBEO**.
- Backfill: ya no hace falta (campo escrito para activos).
- Opcional, si Daniel lo confirma: campaña con el código a toda la lista de activos (el campo ya está listo).
- App lista para pasar el enlace a su gente y difundir (carrusel ≥15 jun).
- Reprogramar el Directo cuando Daniel pueda asegurar fecha.
- Stripe / Pase: sigue dormido (sin prisa).

## Tarde-noche 14 jun · Directo cancelado + visibilidad app + auditoría insights

**Directo «La voz que te juzga» (14 jun) cancelado por indisposición de Daniel.**
- Campaña automática «E4 · en una hora» (id 189196809348843111) **detenida** antes de su envío de las 20:30.
- **Campaña de cancelación enviada** (id 190268255528552136) al grupo del directo (187662493483533365): 17 inscritos, 100% entregada, en español, con el código personal de cada uno + explicación de la app. Mensaje: indisposición, sin fecha nueva para no repetir cancelaciones de última hora.
- **Aviso de método MailerLite (importante para futuras campañas):** el conector pone el idioma en inglés al crear campaña → corregir con `batch_requests` PUT `language_id:8`; pero ese PUT **borra el filtro de grupos si no se reenvía `groups`** (casi se envía a los 65 en vez de a los 17 — cazado en autoauditoría). Reenviar siempre `name`, `language_id` y `groups` juntos.
- **REGLA DE DANIEL (14 jun, inviolable): en campañas a toda la lista, EXCLUIR a quien ya recibió un envío reciente del mismo contenido.** Hoy los 17 del grupo del directo recibieron el código a las 17:17 y, 2 h después, el «regalo a toda la lista» (64 destinatarios, `all_active_subscribers`) se lo mandó otra vez. Daniel verbatim: «hay que excluir a los que se les envió, las próximas veces.» → Para próximas campañas masivas: usar `excluded_groups`/segmento que filtre a quien ya recibió el mismo contenido en los días previos. Antes de un envío masivo, comprobar qué se ha enviado recientemente y a quién.
- Página `directo-la-voz-que-te-juzga/` convertida en aviso de aplazado con CTA a la app (noindex, fuera del sitemap).

**Visibilidad de la app (PR #361, mergeado) — petición de Daniel «que se vea de primeras y se entienda qué es».**
- Banner superior de la home: fuera el directo, dentro la app con frase clara («te ayuda a escribir lo que sientes para que los nervios no estropeen el mensaje»).
- Botón en «¿Qué te trae aquí?»: «Quiero decir algo difícil sin pelearme».
- Sección de la app en home rediseñada como banner visual con ejemplo **antes/después**, subida sobre el capítulo gratis.
- Landing: **narrativa en 6 escenas** (problema → herramienta → vínculo) + por qué/para qué (origen en consulta) + botón saltar a escribir. Aviso de autoría/derechos en el pie (anti-plagio).
- **Recuadro del directo sustituido por el de la app en 25 insights + 8 landings** (reaprovecha tráfico SEO para captación). Emails históricos de `contenido-rrss/` no tocados.

**Auditoría completa de la sección insights (29 artículos) — deuda técnica vieja descubierta al dirigir tráfico a la app:**
- **Cookies:** los 29 cargaban GA4 sin consentimiento ni banner (mismo incumplimiento RGPD que tenía la app) → añadido Consent Mode v2 + banner a todos.
- Paleta naranja antigua → verde de marca (7). Cabeceras/logos duplicados (3). Schemas JSON-LD rotos que se mostraban como texto (2). Logos inconsistentes normalizados.
- Diagnóstico final verificado: 0 naranjas, 0 duplicados, 0 sin consent, 0 sin banner, HTML balanceado.
- **Pendiente apuntado:** la sección insights tiene varias plantillas distintas; quedó coherente en lo auditado, pero conviene a futuro unificar a una sola plantilla.

**Limpieza de seguridad:** token `DLQD_ADMIN_TOKEN` borrado y endpoint `dlqd-backfill` eliminado del repo (ya cumplieron). Identidad git configurada a noreply@anthropic.com.

PRs de la tarde-noche: #356, #357, #358, #359, #360, #361 — todos mergeados.
