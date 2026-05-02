# Política de seguridad · TWIM Project

> Última actualización: 1 de mayo de 2026

## Reportar una vulnerabilidad

Si encuentras una vulnerabilidad de seguridad en este proyecto, **no abras un issue público**. Envía un email a:

**equipo@theworldismindproject.com**

con asunto **"Reporte de seguridad — TWIM Project"** y el mayor detalle posible:

- Descripción del problema.
- Pasos para reproducirlo.
- Impacto potencial.
- (Opcional) Sugerencia de mitigación.

Te responderemos en un plazo máximo de **5 días naturales**, evaluaremos el alcance y aplicaremos la corrección. Si lo deseas, te daremos crédito público una vez resuelta.

## Versiones soportadas

Este es un sitio web estático. Solo `main` recibe correcciones de seguridad. Las ramas de trabajo (`claude/*`, `feature/*`, etc.) no están protegidas y no deben usarse en producción.

## Buenas prácticas seguidas

- **Secretos:** nunca se commitean al repositorio. Las credenciales sensibles van en `.env.audit` (ignorado por git) o en variables de entorno de Netlify.
- **HTTPS obligatorio** en producción (configurado en Netlify).
- **Política de privacidad** publicada en `/privacy.html` con cumplimiento RGPD/LOPDGDD.
- **Banner de consentimiento de cookies** con Google Consent Mode v2 (`/assets/twim-cookie-consent.js`).
- **Rotación de credenciales** ante cualquier sospecha de exposición.
- **Acceso al repositorio** restringido a la organización TWIMProject; recomendable 2FA obligatorio para todos los miembros.

## Qué hacer si has filtrado un secreto por accidente

1. **Rotar inmediatamente** la credencial expuesta (revocar + generar nueva).
2. **Redactar el literal** del repositorio en un commit explícito (`security: redactar [tipo de credencial] expuesta`).
3. **Considerar purgar el historial** con `git filter-repo` o BFG si el repositorio es público o tiene colaboradores externos.
4. Notificar al equipo si aplica.

Nunca confíes en "ya no aparece en el último commit" — los secretos en el historial siguen siendo accesibles.

## Contacto

- Email seguridad: equipo@theworldismindproject.com
- Responsable: Daniel Orozco Abia (CV11515)
