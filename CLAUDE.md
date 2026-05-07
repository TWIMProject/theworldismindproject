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
