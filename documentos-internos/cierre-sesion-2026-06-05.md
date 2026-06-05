# Cierre de sesión · 2026-06-05

> Sesión larga (continuación con resumen de contexto previo). Modelo Opus 4.8. Libertad de acción concedida por Daniel en varios puntos («todo lo que puedas ejecutar tú, hazlo»). Día muy productivo · 11 PRs, varias decisiones estratégicas nuevas, 2 reglas inviolables nuevas.

## Hilo principal del día · rediseño del carrusel «5 señales» (4 iteraciones) + giro estratégico Google Ads

### Carrusel «5 señales · la mirada del otro» — recorrido completo
Partió de un carrusel A2 crema estándar y acabó en un sistema brutalist con pensamientos reales. Iteraciones:
- **v1** (PR #299) · 7 slides A2 crema · base teórica del cuaderno «La mirada del otro» (10 señales → 5 curadas).
- **Hashtags** (PR #300) · regla nueva de Daniel · **máximo 5 hashtags en IG, que sirvan de verdad** (no 10). Set: `#dependenciaemocional #psicoanalisisaplicado #ansiedad #autoestima #psicologavalencia`.
- **v2 Expediente+Mirada** (PR #301) · fondo verde con grano/viñeta + número gigante + ojo en hook/cierre. Daniel: «me gusta pero quiero un giro radical».
- **v3 BRUTALIST** (PR #303) · se le mostraron 2 conceptos radicales (Cuaderno clínico / Brutalist), eligió **Brutalist al 100%** («me maxiencanta»). Una palabra descomunal por slide.
- **v4 pensamientos reales** (PR #304) · Daniel: las palabras-bomba clínicas («VIVES EN SU MIRADA») son demasiado abstractas, nadie las piensa así. Sustituidas por el pensamiento literal en primera persona.
- **v4.1** (PR #304) · tras review de Copilot + feedback · arregla conteo 5↔6, reformula slides 03 y 05. Arco final: hook «Eso me pasa.» / «¿Estás enfadada?» / «Tienes razón.» / «¿Me va a dejar?» / «Tú no eras así.» / «¿Quién soy?» / cierre «Míralo.».
- **slide 01 claridad** (PR #307) · sub_top reformulado a «5 frases que dices o piensas sin nombrarlas.» (el anterior era pronombre colgado).

Generador reproducible · `documentos-internos/plantillas/generar-carrusel-mirada-v3-brutalist.py` (resolución de fuentes portable vía `TWIM_FONTS`).

### Giro estratégico · Google Ads → red supervisada → liberar tardes
Daniel articula el objetivo personal con más fuerza que nunca · **liberarse de las tardes entre semana desde septiembre 2026 sin perder ingresos**. Camino:
1. Captar pacientes (Google Ads, además de Unió y embudo editorial).
2. Derivarlos a una red de psicólogos junior supervisados (modelo ya escrito hoy en sesión previa · `modelo-captacion-supervisada-union-periodistas.md`).
3. Él cobra margen de supervisión por sesión · sigue atendiendo siempre su franja premium de mañana.
4. Si funciona · S.L. + red de colaboradores TWIM. (S.L. solo cuando haya volumen sostenido 6+ meses · mantener Opción B «cada uno factura su parte» hasta entonces.)

Estado Google Ads (captura de Daniel) · **cuenta ACTIVA, no suspendida**. Esto invalida la premisa del doc antiguo `google-ads-cumplimiento-y-reactivacion.md` (que asumía cuenta pausada). Campaña previa tipo INTELIGENTE «Tu Mente Merece Bienestar» (5 clics/832 impr/0 conv) · recomendado pausar.

**Entregado:**
- Doc `google-ads-campana-captacion-pacientes-2026-06.md` (PR #308) · build operativo completo (Búsqueda manual, geo, presupuesto, keywords, negativas, RSA copy, conversiones, umbrales CPL).
- **PDF paso a paso** estilo TWIM enviado al móvil de Daniel (lo crea él mañana con calma).
- **Encuadre del equipo** en home + 2 landings (PR #309, SIN MERGEAR · Daniel revisa preview) · prerrequisito deontológico + política Google.

## Reglas inviolables NUEVAS declaradas hoy (la #1 ya en CLAUDE.md; la #2 aún no)
1. **Concreción para empatizar** (PR #302) · toda pieza de TWIM Project y TWIM Podcast se escribe desde lo concreto, nunca lo abstracto · la concreción es el motor de la identificación («esa soy yo»). Verbatim Daniel: «siempre hay que ser más concreto porque sino a la gente le cuesta más empatizar. Es inviolable esa premisa».
2. **Máximo 5 hashtags en IG** (en la regla de carrusel) · que sirvan de verdad, no relleno. (Declarada al pasar el caption; persistida en `captions.md`, no en CLAUDE.md aún · candidata a subir a regla formal si se repite.)

## Otros entregables del día
- **Guion teleprompter YouTube «La voz que te juzga»** · `contenido-rrss/youtube-la-voz-que-te-juzga/guion.md` (rama `claude/youtube-guion-voz-que-te-juzga`, sin PR · evergreen, Daniel grabará cuando pueda · hoy no pudo, le vino un paciente).

## Directo del domingo 7 jun · estado de recordatorios MailerLite (cerrado)
Daniel autorizó enviar el **Recado 04 «aunque salga en inglés como excepción»** (el `language_id` queda en `en-US`, solo afecta al pie legal automático · el HTML va en español). Cancelados E2 y E4 (estaban en inglés sin entrar en la excepción y/o duplicaban). PRs #305 + #306.

**Calendario final de envíos a los 11 inscritos:**
- sáb 6 jun 10:00 · Recado 04 (víspera) · `ready`.
- dom 7 jun 10:00 · E3 día D · `ready` · ES.
- lun 9 jun ~10:00 · E5 post-directo · `draft` · ES · **programar manual con URL de la grabación**.
- (E4 «en una hora» dom 18:00 · `draft`/stopped · opcional reactivar cambiando idioma a ES en panel.)

## PRs del día
| PR | Tema | Estado |
|---|---|---|
| #299 | Carrusel 5 señales v1 | merged |
| #300 | Hashtags IG 8→5 | merged |
| #301 | Carrusel v2 Expediente+Mirada | merged |
| #302 | Regla concreción para empatizar (CLAUDE.md) | merged |
| #303 | Carrusel v3 Brutalist | merged |
| #304 | Carrusel v4/v4.1 pensamientos reales | merged |
| #305 | Directo · cancelar E2 + excepción idioma | merged |
| #306 | Directo · cancelar E4 + tabla §8.1 | merged |
| #307 | Slide 01 claridad sub_top | merged |
| #308 | Google Ads · build campaña | merged |
| #309 | Equipo TWIM en home+landings | **abierto · Daniel revisa preview** |

## Pendientes para la próxima sesión / para Daniel
- **Daniel mañana (6 jun):** crear el anuncio de Google Ads con el PDF · revisar y mergear el preview del PR #309.
- **Daniel domingo (7 jun):** el Directo a las 19h. Opcional · reactivar E4 en ES.
- **Daniel lunes (9 jun):** programar E5 post-directo con la URL de la grabación.
- **Sesión futura:** si Google Ads convierte, actualizar `modelo-captacion-supervisada-union-periodistas.md` añadiendo Google Ads como canal formal + orden estratégico de los 3 canales (Sergio → Unió → Ads). Vigilar que el éxito no convierta a Daniel en «empresario de psicólogos» y ahueque la marca clínico-editorial.

## Estado emocional / foco del CEO al cierre
Daniel está en modo expansión estratégica · ilusionado con la idea de la red supervisada como vía rápida para liberar tardes («sería una gran idea», «es lo que busco, liberarme desde septiembre ya, de tardes»). Mantiene firme que **él siempre va a atender pacientes** (no quiere dejar la clínica, solo soltar las tardes). Decisión del 5 jun se mantiene · foco H2 en newsletter + artículos + libro + RRSS + venta libros, ahora con la capa de captación-derivación como motor de ingresos pasivos. Día sin fricción · iteró el carrusel con criterio fino y agradeció el trabajo.
