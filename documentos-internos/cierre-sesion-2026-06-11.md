# Cierre de sesión · 11 junio 2026

## Qué pidió Daniel

Capturas de un análisis externo (otra IA) sobre la web con 4 «errores» de arquitectura de la información/conversión. Instrucción verbatim: «oBJETIVO, LEE LAS CAPTURAS, ANALIZA, VALIDA SI ES LO QUE PIENSAS Y EJECUTA PARA MEJORARLO/IMPLEMENTARLO». Libertad de acción → autoauditoría obligatoria al cierre (regla 20-may).

## Validación del análisis externo (método: repo primero)

Antes de tocar nada se leyó: `index.html` completo, `plan-x10-lista-email-2026-06-10.md`, `newsletter-sistema-constancia-2026-06-10.md`, `captacion-email-doc-externo-comparacion-2026-06-04.md`, `ceo-vista-completa-v2-1-mayo-2026.md`, `perfil-daniel-handoff-sesiones.md`, `netlify/functions/subscribe.js`, y se verificó MailerLite vía MCP (solo lectura).

| Error externo | Veredicto | Qué se hizo |
|---|---|---|
| 1 · Exceso de CTAs, home «escaparate» | Diagnóstico parcialmente cierto. El rediseño total como «enrutador» choca con el foco editorial (2 ejes, ceo-vista §3.2) y con el SEO de la home. | Versión ligera: sección `#orientacion` «¿Qué te trae aquí?» tras el hero con 3 rutas (terapia para mí → #especialidades · hijo/a → psicologo-adolescentes-valencia.html · libros → #libros). No se quitó contenido. |
| 2 · FAQs duplicadas | CIERTO. 2 parejas duplicadas en lista visible y en schema FAQPage. La etiqueta «keyword cannibalization» es exagerada (eso es entre páginas), pero el duplicado en schema es real y malo. | Fusionadas: 13 → 11 preguntas, schema alineado con texto visible. About reescrito para no repetir verbatim la lista de patologías (sigue en tarjeta adultos + bloque SEO + meta). |
| 3 · «Sin secuencia agresiva» = choque de tonos | CIERTO con matiz: no es marketing agresivo, es jerga de embudo que rompe la regla de claridad de un vistazo (quien no sabe qué es una «secuencia» no lo entiende). | Sustituido en home («El PDF te llega al instante · después, solo mis cartas · te das de baja en un clic») y en `lead-volver-a-mi-5-senales.html` («Sin spam · solo mis cartas y los avisos del taller»). Copy honesto: el lector del Cap 3 SÍ recibe la automation de 5 emails + cartas, y ahora se le dice. |
| 4 · «Síndrome de la lista de espera» | Diagnóstico cierto (los 3 grupos de lista de espera están a 0 suscriptores en MailerLite, verificado), PERO la solución que propone ya existe: lista unificada + cartas «Te escribo» a todos los suscriptores activos (Carta 3 → `all_active_subscribers: true`, verificado) + automations de nurturing activas. | Copy de las 2 tarjetas de programas ya no enfría: «Mientras llega, te van llegando mis cartas» + salida caliente «si lo estás pasando mal ahora… pide cita» → #contacto. |

## Hallazgo propio (no estaba en el análisis externo)

**Bug de contraste en producción**: las 2 tarjetas de programas (`Deja de Obligarte`, `Deja de Buscarte en Otros`) usaban `.prog-featured` (texto blanco) con fondo crema inline → títulos y bullets prácticamente ilegibles desde ~2 jun. Arreglado con clase nueva `.prog-soon` (texto oscuro, mismo fondo claro con borde beige discontinuo).

## PRs

- **PR #334** · `index.html` + `lead-volver-a-mi-5-senales.html` · todo lo anterior. Deploy preview Netlify ✅ (Lighthouse: SEO 100, Best Practices 100, A11y 97, Perf 62). Mergeado según regla auto-merge 23-may tras CI verde y review atendida.
- **PR de este cierre** · solo documentos internos.

## Verificaciones MailerLite (solo lectura, vía MCP)

- Carta 3 «Necesitas que te miren para saber que vales» programada 16 jun 19:00 CEST a todos los suscriptores activos → **regla de constancia cumplida** (hay carta en <15 días).
- E2 (13 jun) y E4 (14 jun) del directo: programadas y filtradas al grupo del directo (13 suscriptores). Correcto.
- Grupos lista de espera DDBEO / DDO / Pre-venta Volver a Mí: **0 suscriptores** los tres. `subscribe.js` está bien (fail-loud, slugs correctos) → no es bug, es que nadie se apunta todavía. Dato para la estrategia de captación.

## Pendientes que requieren decisión o acción de Daniel

1. ~~Automations DDBEO/DDO en borrador~~ **CORREGIDO mismo día (segunda pasada, tras OK de Daniel):** verificado contra API que las automations DDBEO/DDO **ya están activas** (`enabled: true`, con envíos de prueba) y que la del lead magnet 5 señales fue sustituida el 26-may por «Secuencia · Lista espera Volver a Mí · 3 emails» (`188524234377528522`, activa). El dato «en borrador» venía del README del 21-may, que quedó desfasado y se actualizó hoy.
2. **«Sin secuencia agresiva» en emails — auditado por capturas del builder (11 jun):** el único email VIVO con la frase es el de la automation DDBEO. Es builder HTML y el conector MCP no puede editarlo → **pendiente manual de Daniel (1 línea, ~2 min)**: <https://dashboard.mailerlite.com/automations/188015669577516322> → step de email → «Te lo regalo en PDF, sin secuencia agresiva:» pasa a «Te lo regalo en PDF · solo el capítulo:». DDO y los 3 emails de Volver a Mí están limpios (verificado en captura). El README fuente (`email-templates/automations-listas-lead-21-may/README.md`) ya está corregido con el criterio nuevo. Posts ya publicados de X/LinkedIn no se tocan (archivo histórico).
3. **Validación visual de la home**: el cambio respeta paleta y sobriedad, pero Daniel no lo ha visto renderizado. Si algo no le encaja al verlo, se revierte la sección `#orientacion` con un solo commit (es un bloque autocontenido).

## Tercera pasada (tarde) · OK a la home + empuje del directo + diapositivas

Instrucciones verbatim de Daniel (tarde): «Adelante con la Home nueva.» · «Alimentar alcance para captar para el directo del domingo porque además no sabemos si la gente se conectará o se a apuntado para recibir la grabación.» · «También necesito estructurada una secuencia de "diapositivas" que me acompañen mientras hablo en el directo».

- **Home nueva: VALIDADA por Daniel.** El pendiente de validación visual de los PRs #334 queda cerrado.
- **Hallazgo de captación:** la promo del 3 jun fue a toda la lista anunciando el 7 jun; el aviso del cambio al 14 solo llegó a las 13 inscritas → la lista general no conocía la fecha nueva. Corregido con campaña `189996292943906778` programada vie 12 jun 19:00 CEST a los 64 activos (⚠️ Daniel: idioma → Español en panel). Copy doble-válido (inscritas/no inscritas) y con el argumento de estar en vivo (preguntar por chat sin cámara).
- **Kit RRSS última semana** en `contenido-rrss/directo-14-jun-kit-ultima-semana.md` (captions jue–dom + checklist canales + quote-tweet X pendiente).
- **Diapositivas del directo** en `documentos-internos/directo-14-jun-2026-diapositivas.html` (17 slides, navegación por flechas, mapeadas a la planilla de bloques). Daniel comparte la ventana en Meet: mitad él, mitad slides.
- **Sobre la duda asistencia vs. grabación:** no se encuesta; se argumenta el vivo en todo el copy de la semana y el domingo se mide asistentes reales vs. registrados (queda para el post-mortem del directo).

## Estado emocional CEO al cierre

Sin señal directa en esta sesión (instrucción operativa breve, en mayúsculas parciales — modo ejecutivo habitual). Sin cambios para el perfil handoff: el patrón «trae análisis externo → pide validación contra criterio propio → pide ejecución» ya está documentado (4 jun).
