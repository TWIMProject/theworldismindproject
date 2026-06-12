# App «Di lo que quieres decir» · Legal y marca · 12 jun 2026

> Encargo de Daniel (verbatim): «ten bien atado todo el tema legal pertinente para protegernos, avisa de aspectos que podríamos atar también para que no se nos pase nada con respecto a la marca y a la app». Nota: esto es un análisis operativo de un asistente, no asesoramiento jurídico colegiado — para el registro de marca y la revisión final de textos legales, conviene una pasada de un abogado (1-2 h de un especialista en TIC/propiedad industrial).

## 1 · Hecho hoy (Claude)

- **`di-lo-que-quieres-decir/legal.html`**: página de privacidad y condiciones específica de la app, en lenguaje claro: tránsito del texto por Anthropic como encargado (sin almacenamiento ni entrenamiento), localStorage con botón de borrado, newsletter (MailerLite, baja en un clic), GA4 sin texto, descargo «no es terapia» + **línea 024**, condiciones del Pase con renuncia al desistimiento en contenido digital de ejecución inmediata (art. 103.m LGDCU), derechos RGPD y AEPD. Enlazada desde el pie de la app, que ahora incluye también el aviso 024.
- Añadida a sitemap.

## 2 · Pendientes que solo puede atar Daniel (por prioridad)

1. **DPA con Anthropic** (10 min): verificar en console.anthropic.com → aceptar/descargar el Data Processing Addendum de los Commercial Terms (Anthropic como encargado, SCCs para transferencia a EE. UU.). Guardar copia en el repo o en el archivo legal. Sin esto, la afirmación de la página legal queda sin papel detrás.
2. **Consentimiento de cookies (riesgo de TODO el sitio, no solo de la app)**: GA4 corre en twimproject.com sin banner de consentimiento previo visible. Criterio AEPD: la analítica requiere consentimiento. Opciones: (a) instalar un gestor de consentimiento (p. ej. CookieYes/Cookiebot gratis para un dominio, o banner propio + Consent Mode v2), o (b) sustituir GA4 por analítica sin cookies exenta de consentimiento. Decisión de Daniel; Claude implementa cualquiera de las dos.
3. **Marca** (OEPM ~150 € por clase, o EUIPO ~850 € una clase):
   - «**Di lo que quieres decir**» como marca denominativa es **débil/difícil** (frase descriptiva del servicio). Estrategia recomendada: registrar la **marca mixta** (nombre + logo/grafía propia) o un nombre distintivo acompañante («DLQD», «Traductor del Vínculo»...), y sobre todo **registrar «The World Is Mind Project» / «TWIM»** si aún no está — es el activo de marca real del proyecto.
   - Clases Niza sugeridas: **9** (software/apps), **41** (formación/educación), **44** (servicios de psicología). Mínimo defendible: 9 + 44.
   - Antes de pagar: búsqueda de anterioridades en OEPM (localizador) y EUIPO (eSearch). Claude puede preparar el borrador de solicitud.
4. **Condiciones del Pase en el checkout** (cuando se encienda Stripe): en el Payment Link, activar la casilla de aceptación de condiciones con enlace a `legal.html` y el texto de consentimiento de ejecución inmediata. 2 min en el panel de Stripe al crear el link.
5. **Facturación e IVA del Pase**: el Pase es servicio digital B2C (IVA español 21 % a clientes en España; si hubiera ventas UE transfronterizas relevantes, valorar régimen OSS más adelante — irrelevante a volumen actual). Stripe Tax puede automatizarlo si algún día hace falta.
6. **Seguro RC profesional**: confirmar con la correduría que la actividad «herramienta digital de apoyo a la comunicación» queda dentro de la cobertura actual de psicólogo sanitario (suele requerir una mención). Una llamada.
7. **Los dos pendientes de seguridad ya conocidos**: rotar `ANTHROPIC_API_KEY` (expuesta en chat 12 jun) y el token de Netlify de mayo.

## 3 · Riesgos evaluados y descartados/aceptados

- **Edad**: fijada en 16+ con autorización parental para menores (alineado con LOPDGDD art. 7 para consentimiento de menores: 14+; se fija 16 por prudencia clínica).
- **Datos de terceros en los volcados** (el usuario escribe sobre su pareja): tratados como datos del propio relato del usuario, no almacenados; la página legal pide no identificar a terceros innecesariamente. Riesgo residual bajo por no-almacenamiento.
- **Contenido generado por IA**: descargo de imprecisiones incluido; el usuario revisa y decide. El motor no diagnostica ni promete resultados (regla de no prometer resultados terapéuticos, cumplida).
- **Crisis**: la app no es un servicio de crisis; aviso 024 visible en el pie y destacado en legal.html.

*Registro: [2026-06-12]: legal.html publicada con la app · checklist entregado a Daniel en informe.*
