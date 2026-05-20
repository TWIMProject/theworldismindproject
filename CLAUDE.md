# TWIM Project — Instrucciones para Claude Code

## Regla de método inviolable · Leer el repo primero

> Esta regla precede a todas las demás. Nunca, bajo ninguna circunstancia, saltarse este paso.

Antes de proponer contenido, plan, decisión, copy de redes, calendario o cualquier output operativo, **revisar primero los lugares donde el equipo deja la verdad escrita**:

- `documentos-internos/` → todos los planes estratégicos y operativos (CEO, stack audio+vídeo, NotebookLM, reciclaje, sistema visual IG, X/Twitter, MBS checklist, etc.).
- `contenido-rrss/` → planes de redes y material publicado/pendiente (`PLAN-LANZAMIENTO-*.md`, `PLAN-CAPTACION-*.md`, carpetas por carrusel/carta).
- `email-templates/` y `newsletter/` → campañas y material email.
- `documentos-internos/plantillas/` → plantillas reutilizables (podcast, facturación).
- El doc específico del tema si existe — buscarlo con `grep -rli "<palabra clave>"` antes de producir nada nuevo.

**Nunca proponer desde memoria propia ni desde inferencia general** sin haber verificado primero qué dejó escrito otro compañero en el repo. Si el repo dice una cosa y tu memoria dice otra, gana el repo.

El repo es **la fuente de verdad operativa de TWIM Project**. El bienestar del proyecto y de su CEO depende de que cada sesión opere sobre la verdad acumulada por las anteriores, no sobre suposiciones. Este es un proyecto con horizonte generacional — pulcritud y minuciosidad no son opcionales.

**Regla simétrica para escribir en el repo:** cada vez que se publique algo manualmente fuera del calendario documentado, **actualizar el plan correspondiente el mismo día** (basta con dos líneas: `[fecha]: publicado [pieza] en [canal] · URL [link]`). Así la verdad queda y la siguiente sesión no improvisa a ciegas.

---

## Regla inviolable · Cambios de infraestructura y routing

> Esta regla nace de un incidente real (PR #133, 7 may 2026): un redirect con `force = true` en `netlify.toml` causó `ERR_TOO_MANY_REDIRECTS` en producción y rompió la web entera en un momento crítico del proyecto. No puede repetirse.

Cualquier cambio que toque alguno de estos ficheros se considera **cambio de infraestructura**:

- `netlify.toml`
- `_redirects`
- `_headers`
- `robots.txt`, `sitemap.xml` (cuando afecten a indexación o canónicas)
- `netlify/functions/*`
- Cualquier fichero que controle routing, redirects, headers HTTP, CSP, CORS, edge functions o build.

### Antes de mergear un cambio de infraestructura

1. **Reproducir el síntoma exacto antes de proponer fix.** Si Daniel reporta un bug de URL/cache/navegador, primero entender qué URL falla, en qué navegador, con qué status HTTP. Nunca proponer fix por intuición.
2. **Diagnosticar contra la config actual.** Leer `netlify.toml` completo, mirar qué hace Netlify por defecto (Pretty URLs, asset optimization, trailing slash policy), entender por qué falla antes de añadir reglas.
3. **Justificar cada flag explícitamente.** Si una redirect lleva `force = true`, articular por qué es necesario y por qué no causa loops según las reglas de matching de Netlify. Si no se puede articular, no se usa.
4. **Verificar el deploy preview en navegador antes de pedir merge.** Esperar al check verde de Netlify, abrir el preview URL (`https://deploy-preview-N--lighthearted-kitten-8aba94.netlify.app`) y probar como mínimo: la URL afectada por el cambio, la home, una URL de directorio (`/newsletter/`), una URL de archivo (`/insights/<slug>.html`).
5. **Si no se puede verificar el preview**, decirlo explícitamente en el PR y **no recomendar merge** — Daniel decide.
6. **Doble verificación en momentos críticos.** En lanzamientos, ventanas de tráfico o fechas señaladas, Daniel da el OK explícito antes del merge. Sin OK, no se mergea aunque los checks estén verdes.

### Patrones prohibidos sin justificación documentada

- `force = true` sobre paths que coinciden con un directorio existente (riesgo de loop).
- Redirects circulares (A → B → A o A → A).
- Catch-all (`/*`) sin ruta de escape para assets estáticos.
- Cambios silenciosos al header CSP, CORS o cookies.
- Subir secretos al repo (siempre `.env.audit` gitignored).

### Si el incidente vuelve a ocurrir

Revertir inmediatamente al `netlify.toml` previo (no parchear), abrir PR de revert con etiqueta urgente, comunicar a Daniel y solo después analizar la causa.

---

## Regla inviolable · Diseño de piezas visuales de venta · criterio dopamina-comercial

> Regla declarada por Daniel el 14 may 2026. Detalle operativo completo en `documentos-internos/marca-twim-criterio-dopamina-comercial.md`.

Toda pieza visual de venta del proyecto TWIM (portadas de libros, landings comerciales, anuncios Meta Ads, miniaturas YouTube, lead magnets cuando se diseñan para captar) debe estar orientada a **maximizar la respuesta dopaminérgica del público objetivo concreto** del producto. La marca atrae para que el cliente compre, reciba la ayuda real del producto y se cuide.

**Distinción inviolable: seducir con la verdad, no con la mentira.** La regla dopamina-comercial no autoriza clickbait, falsa escasez, promesas imposibles, testimonios falsos ni estética que ridiculice al cliente. Sí autoriza estética premium contemporánea, promesa visible del beneficio real, imágenes que disparen identificación, paletas y tipografías propias del producto (más allá de la paleta TWIM editorial).

**Convivencia con el resto de reglas TWIM:**

- En activos editoriales puros (newsletter «Te escribo», cartas, carruseles editoriales A1/A2, podcast, libro Engranajes ya publicado) prevalecen las reglas previas (paleta TWIM `#173D30 / #265C4B / #C2A78B / #FDFCFA`, Instrument Serif + Barlow Condensed, anti-coaching, sin emojis, sin frases motivacionales).
- En activos comerciales nuevos (portadas de libros nuevos, landings de venta, anuncios, miniaturas YouTube) prevalece el criterio dopamina-comercial con los límites éticos del §2 del doc operativo. Cada producto puede tener su propio mapa visual orientado a SU cliente objetivo.

**Antes de producir cualquier pieza de venta nueva:** seguir el protocolo de 3 preguntas + benchmark obligatorio + test de validación documentados en el §3 del doc operativo.

---

## Regla inviolable · Idioma de comunicación con Daniel

> Regla declarada por Daniel el 17 may 2026.

**Toda comunicación con Daniel —respuestas de chat, resúmenes, preguntas, explicaciones, avisos— va SIEMPRE en castellano.** Sin excepción y sin que haga falta pedirlo cada sesión. Aunque la petición, un log, un error de herramienta o un documento llegue en otro idioma, la respuesta a Daniel es en castellano. Esto no cambia el idioma de artefactos técnicos que ya tienen su convención (nombres de fichero, identificadores de código); afecta a lo que Daniel lee de vuelta.

---

## Regla inviolable · Formato de entregables visuales para Daniel

> Regla declarada por Daniel el 18 may 2026.

**Todo cuadro, calendario, dashboard, resumen visual o panel operativo que se le pase a Daniel para visualizar va SIEMPRE en este formato.** Sin excepción y sin que haga falta pedirlo. Nada de CSV crudo ni tablas planas abrumadoras como entregable visual (el CSV solo vale como dato secundario si además se entrega la versión visual).

Especificación reproducible:

- **Soporte:** un archivo **HTML autónomo** (abre en navegador, imprimible a PDF con `@media print` sin cortar tarjetas). Descargable; **no se versiona en el repo** salvo que Daniel lo pida.
- **Paleta TWIM exacta:** fondo crema `#FDFCFA`, texto verde oscuro `#173D30`, verde medio `#265C4B`, beige `#C2A78B`. Ningún color ajeno.
- **Tipografía:** Instrument Serif (titulares) + Barlow Condensed (texto), vía Google Fonts.
- **Estructura:** organizado por **bloques temáticos/temporales**, cada ítem en **tarjeta** con jerarquía clara (fecha/etiqueta destacada · título en serif · una línea de «qué falta» · pasos en gris pequeño y discreto). **Código de color por estado** con leyenda (borde/píldora: verde oscuro = urgente/clave, beige = pendiente, contorno tenue = automático, verde medio = espera OK).
- **Sin emojis.** Sobrio, premium, editorial. La claridad y el escaneo rápido priman sobre la densidad.

**Convivencia:** esta regla rige los entregables **internos/operativos para Daniel**. No sustituye el criterio dopamina-comercial (piezas de venta) ni las reglas editoriales públicas; las refuerza aplicando la estética TWIM a las herramientas internas. Plantilla de referencia: el calendario operativo entregado el 18 may 2026.

---

## Regla inviolable · Autoauditoría tras libertad de acción

> Regla declarada por Daniel el 20 may 2026.

**Siempre que Daniel haya dado «libertad de acción» (frases tipo «sigue», «empuja todo lo que veas necesario», «hazlo tú», «como tus otros compañeros», «si me equivoco insiste»), al cerrar la tarea hay que ejecutar una autoauditoría antes de pasar la pelota al usuario.** La autoauditoría se hace en el mismo turno en que se entrega el trabajo (no en un turno futuro) y se reporta lo encontrado · lo que está bien queda confirmado, lo que está mal o incompleto se arregla en el acto si es trivial o se reporta explícitamente si requiere decisión.

**Qué cubre la autoauditoría:**

- **Find & replaces** · verificar que no quedan referencias residuales en docs, captions, txt, scripts.
- **Archivos nuevos creados** · verificar que están enlazados desde algún sitio (no son archivos huérfanos), que el sitemap los incluye si son públicos, y que su sintaxis es válida.
- **APIs externas (MailerLite, Netlify, Stripe, etc.)** · verificar que la operación ejecutada realmente se completó (ej. env var creada existe en el panel; grupo aparece en list_resources; automation tiene los IDs correctos).
- **Cambios de copy en piezas con CTAs** · verificar coherencia con el resto del copy de la pieza (no contradicciones internas tipo «exclusivo para X» mientras se dice «general para Y»).
- **Documentos cierre-sesion y log** · verificar que reflejan la verdad real al cierre del turno (no la del inicio).
- **PRs abiertos vs cambios en branch** · si hay commits posteriores al último PR abierto, abrir nuevo PR o mencionar explícitamente.

**Por qué importa:** la libertad de acción de Daniel implica que él NO está revisando paso a paso. Sin autoauditoría, los errores caen en producción sin que nadie los vea. La autoauditoría es la forma de honrar la confianza sin pedirle a Daniel que verifique cada cosa.

**Formato del reporte de autoauditoría:** lista breve · qué se verificó, qué resultado dio, qué quedó arreglado en el acto, qué se reporta como pendiente. Sobrio, sin inflación, fiel a lo que realmente se ejecutó.

---

## Reglas al compartir URLs del proyecto

- **Siempre con trailing slash en URLs de directorio.** Las páginas servidas desde un directorio con `index.html` (`/newsletter/`, `/insights/`, `/talleres/`, `/soluciones/`, `/libro-engranajes-mente/`, `/psicologo-ansiedad-valencia/`) deben compartirse **siempre** con la barra final. La versión sin slash puede dar problemas según el navegador y la caché. Convención canónica: terminar siempre en `/`.
- **Formato canónico esperado para newsletter:** `https://twimproject.com/newsletter/`. Nunca pasar la versión sin barra ni en chat ni en copy publicado.
- Las URLs a archivos `.html` concretos (`/insights/tdah-depresion-invisible-detras-diagnostico.html`, etc.) van **sin** barra final — solo aplica a directorios.

---

## Reglas de generación de archivos HTML

- **NUNCA crear un archivo HTML completo de una sola vez con `Write`** si supera ~150 líneas.
- **SIEMPRE construir por bloques** usando `Write` para el esqueleto inicial y `Edit` para añadir secciones sucesivas: head → header → hero → secciones de contenido → FAQ → CTA → footer.
- Esto evita el error `Stream idle timeout - partial response received` que corta la respuesta a mitad.

## Stack técnico

- **Web:** Netlify (site: twimproject, rama main)
- **Email marketing:** MailerLite (API v3, `connect.mailerlite.com`)
- **Automatizaciones Instagram:** ManyChat
- **Analytics:** GA4 `G-VMMZ1TKWZ0`
- **Rama de trabajo:** `claude/check-manychat-instagram-EQalY`

## APIs bloqueadas en el sandbox

- `api.netlify.com` → `host_not_allowed` (usar MCP server netlify si está activo)
- `connect.mailerlite.com` → `host_not_allowed` (auditar con script local PowerShell)

## Identidad editorial

- **Autor:** Daniel Orozco Abia · Psicólogo General Sanitario CV11515 · Valencia
- **Tono:** psicoanalítico aplicado, descriptivo, sin positivismo tóxico, sin emojis, tuteo
- **Público:** adultos (mujeres 25-50 principalmente) con ansiedad, dependencia emocional, burnout, autoexigencia
- **Paleta:** verde oscuro `#173D30`, verde medio `#265C4B`, beige `#C2A78B`, fondo `#FDFCFA`
- **Fuente:** Barlow Condensed (Google Fonts)

## Credenciales y variables de entorno

- Las credenciales sensibles van en `.env.audit` (gitignored, nunca se sube)
- **No pegar tokens en el chat** — quedaron expuestos en sesión anterior y deben rotarse:
  - Netlify token `nfp_***REDACTED***` (literal eliminado del repo el 1-may-2026) → pendiente de revocar — acción inmediata en https://app.netlify.com/user/applications
