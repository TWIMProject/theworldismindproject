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

1. **Automations de listas de espera DDBEO/DDO** (188015669577516322 / 188015675634091134): siguen en borrador desde el 20-may, pendientes de diseñar+activar en panel. Mitigado porque las cartas llegan a todos, pero sigue abierto.
2. **«Sin secuencia agresiva» fuera de la web**: la frase sigue en los emails de las automations de MailerLite (documentadas en `email-templates/automations-listas-lead-21-may/README.md`) y en posts ya publicados de X/LinkedIn (archivo en `contenido-rrss/perfil-x/`). Lo publicado no se toca; los emails de automation se pueden actualizar vía MCP si Daniel da OK (ventana de veto habitual).
3. **Validación visual de la home**: el cambio respeta paleta y sobriedad, pero Daniel no lo ha visto renderizado. Si algo no le encaja al verlo, se revierte la sección `#orientacion` con un solo commit (es un bloque autocontenido).

## Estado emocional CEO al cierre

Sin señal directa en esta sesión (instrucción operativa breve, en mayúsculas parciales — modo ejecutivo habitual). Sin cambios para el perfil handoff: el patrón «trae análisis externo → pide validación contra criterio propio → pide ejecución» ya está documentado (4 jun).
