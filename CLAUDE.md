# TWIM Project — Instrucciones para Claude Code

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
  - Netlify token `nfp_Fe7FsD3Uv9UtsLmz9broLYSad2PKqh9E4d2e` → pendiente de revocar
