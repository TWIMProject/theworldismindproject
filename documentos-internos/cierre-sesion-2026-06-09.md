# Cierre de sesión · 2026-06-09

> Sesión muy larga (8-9 jun, cruzó el cambio de día). Modelo Opus 4.8. Libertad de acción de Daniel en varios tramos («adecua la web si falta algo», «sigue con lo pendiente», «haz lo que mejor vaya»). Día de mucho output operativo + 6 PRs + 1 regla nueva + corrección importante de un doc.

## Hilo 1 · Nuevo formato YouTube «prescripción del síntoma» (anti-tutorial)

Daniel pasó una transcripción de un vídeo de **Claudia Nicolasa Psicología** («Guía definitiva para arruinar tu autoestima»). Pidió dos cosas: planilla de orden de temas para su directo + estilo de narrativa para grabar en YouTube.

- **Doc de formato** · `documentos-internos/youtube-narrativa-prescripcion-sintoma.md` · destila el recurso (prescripción del síntoma / anti-tutorial), lo reconcilia con §2 del doc de canal (anti-clickbait) y la regla dopamina-comercial, mapa de titulares por tema, esqueleto de guion.
- **Regla nueva persistida (§3.1 de ese doc) · ANTI-CALCO**, declarada por Daniel verbatim: **«es un calco de Claudia Nicolasa, no seamos descarados, por favor.»** Tabla muletilla→alternativa TWIM + «prueba de las dos columnas». Tomar la técnica (dominio público), nunca la ejecución/muletillas del creador de referencia.
- **Decisión Daniel · grabar el formato A** (irónico TWIM-seguro). Empezar por **ansiedad**.
- **Guion ansiedad** · `contenido-rrss/youtube-ansiedad-como-vivir-con-ansiedad/guion.md`. Recorrido v1 (7 pasos) → v2 (10 pasos, «lo veo corto») → **v3 anti-calco** (reescrito sin las muletillas de Claudia, apertura con 3 escenas propias, coste contado distinto en cada paso) → restaurada longitud con concreción (~2.800 palabras, 15-18 min). Título recomendado: «10 pasos para no soltar nunca tu ansiedad (que ya estás dando sin saberlo)».
- PRs #313, #314, #315, #316.

## Hilo 2 · Planilla de orden de temas del directo

- `documentos-internos/directo-planilla-orden-temas.md` (método reutilizable + rellena) + `directo-14-jun-2026-planilla-orden-temas.html` (panel visual TWIM, regla §5). Para el Directo **«La voz que te juzga» · dom 14 jun 21:30 CEST** (Meet `fsu-scrz-res`, gratuito, CTA Cap III + newsletter, sin venta). PR #313.

## Hilo 3 · Campaña Google Ads · LANZADA + corrección importante

- **Acompañé a Daniel clic a clic** montando la campaña (él desde el ordenador, Windows). Resultado: **campaña «Búsqueda · Captación pacientes · Valencia + Online» PUBLICADA** (9 jun). Config: Búsqueda manual (no inteligente), redes solo Búsqueda, geo Valencia+radio (presencia), ES, **8,5 €/día**, Maximizar clics CPC máx 1,80 €, **horario lun-vie 8-22 · sáb 8-14 · dom 19-00** (domingo noche lo decidió Daniel · pico de ansiedad anticipatoria), grupo Ansiedad 9 keywords frase+exacta, RSA «Buena», 6 sitelinks + callouts, nombre TWIM Project, IA Max OFF. Resultado = **llamadas + visitas web** (las dos).
- **CORRECCIÓN CLAVE (verificada contra política oficial de Google):** un psicólogo que da terapia en España **NO necesita certificación Healthcare** (esa es para farmacias/telemedicina con receta/adicciones/medicamentos). El doc `google-ads-cumplimiento-y-reactivacion.md` (1 may) decía lo contrario · **estaba mal** · corregido con banner al inicio. El aviso «Health in personalized advertising» es informativo · solo limita Display/remarketing, no Búsqueda. (Daniel se fue por error a la página de Google CLOUD Healthcare API · le paré.)
- **Web de conversión** · `assets/twim-ads-conversion.js` dispara evento GA4 `generate_lead` en clics de WhatsApp/email de las **5 landings** de captación. Aviso de embudo registrado: la conversión de llamada no captura WhatsApp (vía real de la landing) → por eso el evento. PR #318.
- **Pendiente de Daniel** (él decidió dejarlo para luego): marcar `generate_lead` como evento clave en GA4 + importar a Ads. Verificar en GA4 «Tiempo real» que salta al pulsar WhatsApp.

## Hilo 4 · Roadmap libros (audiolibro + tapa dura)

- `documentos-internos/roadmap-libros-audiolibro-y-tapa-2026.md`. Audiolibros con voz clonada ElevenLabs (Engranajes ahora, libro nuevo en septiembre) + Amazon tapa blanda/dura de Engranajes.
- **Decisión del extra · A (provisional)** · el extra «De los engranajes a tu día» sigue exclusivo de la edición web; en Amazon solo la base. Pendiente confirmación explícita A/B.
- **Flags de socio:** Audible/ACX no admite narración IA → audiolibro va a Google Play/Spotify/Apple/web, no Audible. La grabación de voz (30-60 min) desbloquea audiolibro **y** podcast T2 → hacerla una vez (agosto). KDP tapa blanda/dura reutiliza el `brief-word-kdp.md` del otro libro.
- **Timing:** DDBEO grabación 15 jun-28 jul → agosto (audiolibro Engranajes + tapas + grabar voz) → septiembre cargado (libro nuevo + Volver a Mí + ElevenLabs T2). No solapar.

## PRs del día
| PR | Tema | Estado |
|---|---|---|
| #313 | Planilla directo + narrativa YouTube prescripción del síntoma | merged |
| #314 | Guion ansiedad v1 (formato A) | merged |
| #315 | Guion ansiedad v2 (10 pasos) | merged |
| #316 | Guion ansiedad v3 (anti-calco) | merged |
| #318 | Web conversión Ads + corrección cert salud + roadmap libros | merged |

## Pendientes para Daniel / próxima sesión
- **Daniel:** grabar el vídeo de ansiedad (formato A) cuando pueda → entonces preparar Shorts + copy descripción YouTube. Marcar `generate_lead` evento clave GA4 + importar a Ads. Confirmar A/B del extra. Pasar texto base de Engranajes en Word para maquetar tapa.
- **Directo 14 jun:** pendientes manuales (idioma E4 a ES, programar E5 con URL grabación, verificar Cap III accesible, mover evento Google Calendar a 14 jun 21:30, story/quote-tweet del cambio de fecha).
- **Próxima sesión:** vigilar CPL de la campaña Ads a ~2 semanas (objetivo ≤15-20 €). Si convierte, ampliar ad groups (dependencia, burnout, online).

## Estado emocional / foco del CEO al cierre
Daniel en modo ejecución intensa · montó la campaña entera desde el ordenador entre tareas, con buen ánimo y criterio fino (la decisión del domingo noche, el ojo para el calco). Sigue delegando con confianza («adecua la web», «sigue con lo pendiente»). Foco del momento · liberar tardes desde septiembre vía captación Ads + red supervisada, sin soltar la clínica de mañana.
