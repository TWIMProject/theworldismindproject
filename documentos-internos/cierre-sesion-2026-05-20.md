# Estado de sesión · 19-20 may 2026

> **Documento de orientación para la próxima sesión de Claude Code.**
>
> Creado el **20 may 2026** al cierre de la sesión `claude/social-media-link-naming-tcIUA` que estuvo activa entre el 19 y el 20 de mayo · 17 PRs abiertos (16 mergeados al cierre, #196 pendiente preview Daniel).
>
> La próxima sesión debe **leer este documento primero** para situarse rápido y operar sobre la verdad real del repo, no sobre intuición.

---

## 1 · Mapa de proyectos vivos (al 20 may, ~14:00)

| Proyecto | Estado | Pendientes inmediatos en Daniel | Pendientes inmediatos en Code |
|---|---|---|---|
| **Sprint editorial · Carta #2 + Carrusel #3 + Cap 3** | Carta #2 enviada 19 may 19:00. Carrusel #3 publicado 19 may 17:07 manualmente (sin programar · invalidó test 19h vs 20h). Cap 3 lead magnet activo desde 13 may pero con **0 completados** · embudo verificado end-to-end por Daniel (smoke test OK · form, MailerLite, email todo bien). Problema = tráfico, no embudo. | (1) Publicar promo Cap 3 del PR #193: hilo X hoy, story IG mañana, Threads pasado · (2) Capturar URLs y anotar en `PLAN-CAPTACION-30D.md` §6 · (3) Verificar deploy preview PR #196 antes de merge | Crear `metricas-carrusel-3-voz-que-te-juzga-19-may-2026.md` el 26 may con métricas a 7 días reales |
| **Directo 8 jun «La voz que te juzga»** | Embudo entero montado y activo. Form de registro con Share URL pública verificada. Automation E1 activa. **Carta promo programada** vía MCP MailerLite (`187974522939377362`) para mié 3 jun 19:00 CEST. Evento creado en Google Calendar. | (1) **Cambiar idioma de la Carta promo a Español en panel MailerLite antes del 3 jun** · (2) Difundir Share URL del form en bio IG/LinkedIn/post FB/YouTube con naming de `documentos-internos/directo-la-voz-que-te-juzga-8-jun-2026.md` §5.5 · (3) Programar campañas E2-E5 en panel cuando haya inscritas · (4) Hacer el directo el 7 jun 19:00 vía Meet | Ninguno hasta post-directo (grabación → evergreen) |
| **Taller «Volver a Mí»** | Análisis recalibrado al 20 may (PR #189). 3 PDFs preparatorios producidos (PR #191). Landing pública en `talleres/volver-a-mi/` (PR #192). KPI Newsletter Fase 1 recalibrado de ≥120 a ≥80 techo / 60-70 realista. | (1) Crear grupo «Pre-venta Volver a Mí» en MailerLite + env var `MAILERLITE_GROUP_PRE_VENTA_VOLVER_A_MI` cuando abra captación (jun-jul) · (2) Lead magnet «5 señales hambre de mirada» se produce en Fase 2 (jun-jul) entre módulos de grabación DDBEO | Producir lead magnet «5 señales hambre de mirada» en Fase 2 (decisión §2.3 del analisis-benchmarks 20-may) |
| **Libro «Tu valor no está en su mirada»** | Manuscrito v 14 may con 3 escenas adicionales ya insertadas por Daniel (escena LABORAL en Cap 6 confirmado, AMISTAD y FAMILIAR en Cap 5/9). Bibliografía pasada (5 autores: Kohut, Winnicott, Freud, Porges, van der Kolk). Índice con Interludio «El cuerpo sabe» + Cierre «Necesitar sin desaparecer». Descripciones breves de Interludio/Cierre pasadas. Daniel maquetando en Word con `brief-word-kdp.md`. **Conteo provisional 228 páginas** (suelo · faltan blanks + saltos · final estimado 245-260). | (1) Terminar maquetación Word · (2) Aplicar saltos de página impar para inicio de Parte/Capítulo · (3) Pegar las páginas preliminares (i-x) · (4) Exportar PDF final y pasar conteo definitivo | Regenerar wraparound KDP con lomo correcto cuando Daniel pase nº páginas final |
| **Programa «Deja de Buscarte en Otros»** | Landing de venta del producto inacabado a 70 € corregida · ahora hay `dejadebuscarteenotros-preventa.html` real con captación lista de espera (PR #196). En grabación 15 jun → 28 jul. | (1) Crear grupo «Lista espera DDBEO» en MailerLite + env var `MAILERLITE_GROUP_LISTA_ESPERA_DDBEO` · (2) Grabar 8 módulos entre 15 jun y 28 jul (tope agosto) | Producción del programa (audios + edición) coordinada con libro y taller |
| **Programa «Deja de Obligarte»** | Sin vídeos, sin Stripe. Convertido a placeholder lista de espera con landing dedicada `dejadeobligarte-preventa.html` (PR #196). Daniel decide más adelante si recupera (opción B · audio+texto) o lo elimina (opción D). | (1) Crear grupo «Lista espera DDO» en MailerLite + env var `MAILERLITE_GROUP_LISTA_ESPERA_DDO` · (2) Decidir A/B/C/D del producto final (mi recomendación firme · A) | Ninguno hasta que Daniel decida |
| **Homepage** | Limpieza completada en PRs #194 + #195 · Cap 3 destacado en sección 2, Volver a Mí prioritario en sección 5, DDBEO + DDO en placeholder, Conferencias fuera con landing dedicada en `/conferencias/`. Nav y GA4 consent arreglados. | Verificar preview del PR #196 antes de merge | Ninguno · home estable hasta nueva orden |
| **X (@DaniOrozcoPsico)** | Bio v2 actualizada (PR #186) · ahora incluye Col. CV11515 + CTA «Te escribo» + sin «conferencias y formaciones». | Pegar la bio nueva en X (si aún no lo hizo) y verificar que el link del perfil apunta a `/newsletter/` con barra final | Ninguno hasta análisis tras primer mes de publicación |
| **4 forms migrados a contacto** | Burnout, Impostora, TDAH adolescentes, Bachillerato motivación → todos pasan a contacto puro vía Formspree (PR #190). Forms estaban operativamente rotos o sin captación. | Verificar que Formspree mpwrqplb está redirigiendo a `equipo@theworldismindproject.com` (panel Formspree) y hacer sumisión de prueba | Ninguno · arreglo concluido |

---

## 2 · PRs mergeados en esta sesión (19-20 may)

| # | Tema | Tipo | Estado |
|---|---|---|---|
| **#180** | Directo 8 jun · fija naming canónico del enlace en canales sociales (§5.5 del doc directo) | docs | ✅ |
| **#181** | Corrige nota errónea de URL · `preview.mailerlite.io/.../share` ES la URL pública para formularios integrados | docs | ✅ |
| **#182** | Portadas RRSS 1080×1080 · Directo «La voz que te juzga» (A1 verde) + Reto 7 días «Deja de Buscarte en Otros» (A2 crema) | rrss | ✅ |
| **#183** | Carrusel #3 «La voz que te juzga» · 7 slides PNG + PDF LinkedIn + log publicación manual IG 19-may | rrss | ✅ |
| **#184** | Story Carta #2 «La voz que te juzga» 1080×1920 con flecha vectorial · sticker link a `/newsletter/` | rrss | ✅ |
| **#185** | Veredicto SaaS «Buzón Emocional Anónimo» · aparcado como futuro candidato (compuerta dura · programa grabado + newsletter >1.000 + asistente) | docs | ✅ |
| **#186** | X bio v2 · CV11515 visible + CTA «Te escribo» + quita conferencias/formaciones (CEO doc §2) | docs | ✅ |
| **#187** | Métricas a ~17 h del Carrusel #3 en log `PLAN-CAPTACION-30D.md` §6 con lectura vs benchmarks del repo | docs | ✅ |
| **#188** | Corrección honesta del desglose de comentarios del Carrusel #3 · engagement orgánico cualificado ≈ 0 (no «4 cualitativos») | docs | ✅ |
| **#189** | Taller Volver a Mí · recalibración 20-may del análisis 13-may + decisiones cerradas (lead magnet, 3 PDFs estructura, alcance forms→contacto) | docs | ✅ |
| **#190** | 4 forms a contacto puro · Burnout/Impostora reemplazaban form roto, TDAH/Bach quitaban duplicación a subscribe.js · subscribe.js endurecido con fail-loud para grupos desconocidos | feat+fix | ✅ |
| **#191** | 3 PDFs preparatorios del taller Volver a Mí · marco clínico + cuaderno auto-observación + encuadre operativo (HTMLs autónomos imprimibles) | rrss/contenido | ✅ |
| **#192** | Landing pública del taller en `talleres/volver-a-mi/` (435 líneas) · hero + 3 conceptos + calendario S1-S8 + cómo entras + precio + FAQ + form lista de espera | feat | ✅ |
| **#193** | Promo orgánica Cap 3 Engranajes · story IG (1080×1920) + hilo X (5 tweets) + versión Threads (2 posts) | rrss | ✅ |
| **#194** | Homepage · limpieza de jerarquía visual (Cap 3 destacado, Volver a Mí prioritario, DDBEO placeholder, Conferencias fuera con landing dedicada) | feat | ✅ |
| **#195** | DDO placeholder + 3 fixes de review Copilot del PR #194 (#keynotes nav roto, footer 404 en conferencias, GA4 consent default) | fix | ✅ |
| **#196** | Fix crítico DDBEO preventa redirecting a venta + DDO preventa landing dedicada + GA4 lead-burnout (Consent Mode v2 RGPD) | fix+feat | 🟡 abierto |

---

## 3 · Decisiones nuevas cerradas en esta sesión

### 3.1 · Estratégicas (CEO doc)

- **Regla meta inviolable nueva:** «Aunque yo te limite en presupuesto o enfoque, debes buscar convencerme de tu visión si claramente me estoy equivocando.» (Daniel, 20-may). Aplicada en esta misma sesión sobre Ads y emails de pacientes.
- **«Toda comunicación con Daniel SIEMPRE en castellano»** (Daniel, 17 may · reafirmada).
- **«Todo cuadro / calendario / dashboard visual para Daniel SIEMPRE en formato HTML autónomo paleta TWIM»** (Daniel, 18 may · reafirmada).
- **Saas «Buzón Emocional Anónimo» aparcado** hasta cumplir compuerta dura (programa DDBEO grabado + newsletter >1.000 + asistente). Documentado en `veredicto-buzon-emocional-saas-19-may-2026.md`.

### 3.2 · Operativas

- **Bio X cambiada a v2** con CV11515 + CTA newsletter.
- **Naming canónico de enlaces del Directo en cada canal** documentado en §5.5 del doc del directo.
- **3 PDFs preparatorios del taller:** estructura cerrada · marco clínico + cuaderno + encuadre.
- **Lead magnet del taller «5 señales hambre de mirada»:** SÍ se produce, en Fase 2 (jun-jul) entre módulos de DDBEO.
- **4 forms (Burnout, Impostora, TDAH, Bachillerato) → contacto puro vía Formspree.** Captación a MailerLite eliminada de esos 4 endpoints.
- **subscribe.js endurecido:** fallback silencioso `MAILERLITE_GROUP_LEAD_MAGNET` sustituido por 400 fail-loud cuando el `group` no existe en el map.
- **Homepage refactor:** Cap 3 destacado (era Reto), Volver a Mí prioritario (era TDAH+Bach), DDBEO + DDO en placeholder, Conferencias fuera con landing dedicada en `/conferencias/`.
- **Email de contacto unificado en `equipo@theworldismindproject.com`** (decisión nueva 20-may tarde · Daniel confirma que `equipo@twimproject.com` NO existe y `equipo@theworldismindproject.com` SÍ está activo). La separación de dominios prevista en P11 del taller queda en suspenso · mientras Daniel sea un solo Daniel revisando bandeja, una sola bandeja. Aplicado find&replace global el 20-may: las 8 landings y email destinos que referenciaban `equipo@twimproject.com` ahora apuntan a `equipo@theworldismindproject.com`. Formspree mpwrqplb sigue manteniendo su panel · Daniel debe verificar que está redirigiendo a `equipo@theworldismindproject.com` (panel Formspree).
- **«Deja de Obligarte» decisión CERRADA DEFINITIVA · opción A · placeholder lista de espera.** Daniel confirma el 20-may tarde · «2. A». Sale del catálogo activo de TWIM Project hasta que Daniel decida explícitamente reactivarlo · no es decisión provisional. La landing `dejadeobligarte-preventa.html` sigue viva con form de captación pasiva (si alguien aparece, queda apuntado al grupo MailerLite, sin esfuerzo activo). El recurso «Deja de Obligarte» en `dejadeobligarte.html` (página de venta legacy del producto inacabado) puede archivarse en un PR futuro si se quiere limpieza · ahora mismo no enlaza desde ningún sitio activo de la home tras PR #196.

---

## 4 · Lo que la siguiente sesión debe priorizar

1. **Verificar el merge del PR #196** y arreglar lo que Daniel reporte en preview.
2. **26 may ~10:00:** crear `metricas-carrusel-3-voz-que-te-juzga-19-may-2026.md` con métricas reales a 7 días + cierre de hipótesis (packaging vs audiencia histórica).
3. **Cuando Daniel publique las piezas del Cap 3 (PR #193):** anotar URLs en `PLAN-CAPTACION-30D.md` §6 (regla simétrica).
4. **Vigilar la métrica del embudo Cap 3** · si a 7 días la automation pasa de 0 a ≥15 completados, validamos para considerar test de Meta Ads (presupuesto a definir por Daniel · ya no hay techo).
5. **Cuando Daniel pase nº páginas final del libro:** regenerar wraparound KDP con lomo correcto.
6. **Fase 2 (15 jun-28 jul):** producir lead magnet «5 señales hambre de mirada» del taller. Sin esto Meta Ads de septiembre no tiene gancho.
7. **Antes del 3 jun:** verificar que Daniel cambió el idioma de la Carta promo del Directo a Español en panel MailerLite.

---

## 5 · Reglas inviolables del repo todavía vigentes (recordatorio)

Estas siguen activas. Cualquier sesión futura las respeta.

- **Repo es la fuente de verdad operativa** (CLAUDE.md preámbulo). Leer antes de proponer.
- **Cambios de infraestructura** (netlify.toml, _redirects, _headers, netlify/functions/*) requieren PR específico, diagnóstico contra config actual, justificación de cada flag, deploy preview verificado, OK explícito de Daniel.
- **Diseño dopamina-comercial** para piezas de venta vs reglas TWIM editoriales para piezas editoriales.
- **Toda comunicación con Daniel en castellano.**
- **Todo cuadro/dashboard visual en HTML autónomo paleta TWIM** (no CSV plano).
- **URLs de directorio siempre con trailing slash** (`/newsletter/`, `/talleres/...`).
- **Regla simétrica** · cada publicación manual se registra el mismo día en el plan correspondiente.
- **Gate Meta Ads condicional** · Ads solo se activa cuando el orgánico demuestra que el registro convierte (CEO doc §7 Decisión 2). Vigente · empuja a Daniel hacia esta gate si quiere quemar dinero antes de validar.
- **Concentración no dispersión** (CEO doc Decisión 1). Mismo principio.
- **Nueva regla meta · convencer a Daniel si veo error grave aunque me limite en enfoque** (Daniel, 20 may).
- **Cualquier producto digital se vende solo cuando es entregable.** Aplicado a DDBEO y DDO en esta sesión.

---

## 6 · Corrección post-autoauditoría (20-may 21:00)

> Regla inviolable nueva declarada por Daniel («Autoauditate cuando te dé libertad de acción»). Aplicada en el cierre del turno · cazó un bug crítico.

**Bug detectado y corregido:** las 3 env vars de Netlify creadas vía MCP (`MAILERLITE_GROUP_PRE_VENTA_VOLVER_A_MI`, `MAILERLITE_GROUP_LISTA_ESPERA_DDBEO`, `MAILERLITE_GROUP_LISTA_ESPERA_DDO`) se crearon con scope `["functions"]` solo, mientras el resto del proyecto las tiene con scope completo `["builds","functions","post_processing","runtime"]`. El connector devolvió `"Environment variable upserted"` 3 veces pero las env vars **no aparecían en `getAllEnvVars`** del Netlify, lo cual implica que **no estaban realmente expuestas al runtime** de las functions. Resultado · los 4 forms (lead magnet 5 señales + lista espera Volver a Mí + DDBEO + DDO) habrían devuelto 500 silenciosamente en producción tras merge.

**Corrección aplicada:** reintento de las 3 env vars con `newVarScopes: ["builds","functions","post_processing","runtime"]`. Verificado en `getAllEnvVars` · las 3 aparecen ahora correctamente expuestas con `updated_at: 2026-05-20T19:47`.

**Aprendizaje para sesiones futuras:** al crear env vars Netlify vía MCP, usar **siempre scope completo** (`["builds","functions","post_processing","runtime"]`) para coincidir con el patrón del proyecto. El default `["all"]` o `["functions"]` solo no funciona como cabe esperar. La diferencia entre el upsert "successful" del MCP y la visibilidad real en `getAllEnvVars` no la detecta la respuesta del propio conector MCP · solo se ve auditando.

**Última actualización:** 20 may 2026 · sesión `claude/social-media-link-naming-tcIUA` · cierre del día con autoauditoría aplicada y bug crítico corregido en el acto.

