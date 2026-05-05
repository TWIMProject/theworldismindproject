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
