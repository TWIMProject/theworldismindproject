# Taller «Volver a Mí» · carpeta operativa interna

> Carpeta creada el **13 may 2026** en sesión `claude/improve-proposal-quality-pq3d9` a partir del dossier que Daniel pegó en chat el mismo día. Su función es **dejar la verdad operativa del taller en el repo** según la regla inviolable del CLAUDE.md, para que ninguna sesión futura (humana o IA) opere desde memoria de chat.
>
> Estado del taller: producción avanzada · lanzamiento **miércoles 30 sep 2026** (reprogramado desde 17 jun el 13 may tras análisis científico — verano era mala fecha por caída industria coaching premium 30-50%, vacaciones del target, incompatibilidad clínica con modo vacacional, y «Volver a Mí» encaja con narrativa de rentrée) · precio **697 €** · decisiones operativas cerradas en `decisiones-cerradas.md`.

---

## 1 · Mapa de archivos

| Archivo | Contenido | Estado |
|---|---|---|
| `README.md` | Este índice | ✅ |
| `dossier-completo.md` | Dossier verbatim que Daniel pegó en chat (identificación, marco conceptual, posicionamiento, audiencia, producción, identidad visual, normas) | ✅ |
| `guion-sesion-01.md` | Guion narrativo verbatim de la primera sesión (75-90 min) generado por ChatGPT con base en Kernberg, con anexos sobre manejo de situaciones, honestidades, investigación de contexto | ✅ |
| `marco-conceptual.md` | Los tres conceptos propios (hambre de mirada, self hambriento, Juez Interno) con cruce a libro `Tu valor no está en su mirada` y a manuscrito del libro `Los Engranajes de la Mente` | ✅ |
| `normas-inviolables.md` | Reglas profesionales y editoriales que cualquier entregable del taller debe cumplir | ✅ |
| `piezas-pendientes.md` | Las 14 preguntas operativas + decisiones — **respuestas de Daniel mergeadas en PR #151 el 13 may** | ✅ cerrado (ver `decisiones-cerradas.md`) |
| `decisiones-cerradas.md` | Tabla maestra consolidada con las 18 decisiones tomadas (Daniel + Code) + argumentaciones detalladas | ✅ |
| `mailerlite-api-incidencia.md` | Documentación del problema técnico que bloquea la captación vía formularios web | ⚠️ esperando que Daniel ejecute paso 2 (curl al endpoint diag desde navegador — sandbox no permite a Code hacerlo) |
| `plan-captacion-verano-2026.md` | Cronograma operativo de las 20 semanas entre 13 may 2026 y S1 (30 sep 2026) en 5 fases: sprint editorial + lista de espera · grabación Deja de Buscarte · vacaciones Daniel · pre-venta dura + Meta Ads · sesiones individuales previas. Incluye KPIs, decisiones por escenarios al 22 sep, riesgos + mitigación, operativa día D. | ✅ |

---

## 2 · Lo que NO está aquí todavía (se sube cuando Daniel lo pase)

> **Actualización 18-may 2026 (reparto cerrado con Daniel):**
> - **Logo / identidad:** NO se crea nada nuevo. Se usa la identidad TWIM ya en el repo (`logo-mindworld.png`, `assets/logo-mindworld-transparent.png`, paleta `#173D30 / #265C4B / #C2A78B / #FDFCFA`, Instrument Serif + Barlow Condensed). Crear sub-marca propia sería dispersión (sistema visual §4 «Consolidación TWIM»). Suficiente para producir landing y PDFs sin assets de Daniel.
> - **3 PDFs preparatorios:** los redacta Code desde `marco-conceptual.md` + `guion-sesion-01.md` + `dossier-completo.md`.
> - **Análisis comparativo / benchmarks de precio / proyecciones de conversión:** los redacta Code desde el repo (`decisiones-cerradas.md`, `plan-captacion-verano-2026.md`), marcando qué es dato documentado y qué estimación. **No se delegan a ChatGPT**: hay dos precedentes en el repo de dossiers de ChatGPT con cifras/decisiones erróneas que hubo que corregir (veredicto §5; este README §5). ChatGPT inventaría números.
> - **Informe técnico incidencia MailerLite:** ya resuelto el 13 may (era hipótesis falsada), documentado en `mailerlite-api-incidencia.md`. No es un artefacto pendiente.
> - **Landing HTML:** la produce Code (§3 ya cerrado + dominio/lead magnet/cobertura agosto confirmados 18-may). Desbloqueada.

Lista original (estado previo al 18-may). Estos artefactos los tiene Daniel pero aún no están en el repo:

- **Landing HTML completa** del taller (mencionada en el dossier §6).
- **3 PDFs preparatorios** con diseño de marca, organizados por bloques temáticos.
- **Logo Mind World Project procesado** para fondos claros y oscuros (.svg).
- **Análisis comparativo asíncrono vs sincrónico** para dependencia emocional.
- **Benchmarks de precio** en mercado español.
- **Proyecciones de conversión** para el lanzamiento.
- **Informe técnico** sobre la incidencia MailerLite API (Daniel dice que existe).

Cuando Daniel los pase (o los vuelque desde otro espacio), van a:

```
documentos-internos/taller-volver-a-mi/
  ├── analisis-comparativo-asincronico-sincronico.md
  ├── benchmark-precios-mercado-espanol.md
  ├── proyecciones-conversion.md
  └── mailerlite-api-incidencia.md  ← se completa con datos del informe técnico

talleres/volver-a-mi/                ← landing pública (no se crea hasta tener §3 cerrado)
  ├── index.html
  └── assets/
      ├── logos/
      └── pdfs-preparatorios/
```

La landing pública en `/talleres/volver-a-mi/` **no se crea hasta que Daniel confirme las 12 piezas pendientes del §3**, para evitar publicar una landing con placeholders falsos (plazas, fechas, modalidad indeterminada — eso sería peor que no tener landing).

---

## 3 · Decisiones del taller (todas cerradas tras PR #151)

Daniel contestó las 14 piezas pendientes en el PR #151 (mergeado el 13 may) y delegó a Code las que requerían argumentación técnica. La tabla maestra con valores cerrados, autor de cada decisión y argumentación está en **`decisiones-cerradas.md`**.

Resumen ejecutivo:

- **8 plazas** (mínimo viable 5) · **8 sesiones** semanales de **90 min** · **miércoles 20:00-21:30 hora de Madrid** (S1-S4 en CEST UTC+2 · S5-S8 en CET UTC+1, cambio horario el último domingo de octubre 25 oct 2026) · **online (Zoom) por defecto, presencial Valencia opcional si hay demanda local**.
- **Calendario 1ª edición:** S1 = **miércoles 30 sep 2026** → S2 = 7 oct → S3 = 14 oct → S4 = 21 oct → S5 = 28 oct → S6 = 4 nov → S7 = 11 nov → S8 = **18 nov 2026**.
- **Precio 697 €** dividido en **reserva 100 € + restantes 597 € antes de S1**.
- **Sesión individual previa con Daniel** (30 min) incluida en el precio — sirve como filtro de entrada y commitment.
- **Material post:** PDFs adicionales + comunidad cerrada. **No grabaciones**.
- **Devolución total** durante 14 días desde el pago de reserva si S1 no ha empezado.
- **2ª edición** anunciada para **Q1 2027** (enero, momento «nueva versión de mí» post-Reyes).
- **Métricas:** éxito 8 plazas · mínimo 5 · corte **22 sep 2026 23:59 CEST**. Plan B si <5 al 22 sep: posponer S1 a **miércoles 14 oct** (calendario corrido S1-S8 hasta 2 dic) + 50 € extra de descuento. Si al 5 oct siguen <5 → cancelar y devolver. Si 0-2 al 22 sep → cancelar inmediatamente.
- **Canales:** Newsletter «Te escribo» + IG orgánico + Meta Ads. Pre-pre-venta julio (lista de espera, 0 €) → pre-venta dura 1-22 sep (**330 € en Ads = 15 €/día × 22 días**, escalable a 660 € si CPL primera semana < 50 €).
- **Tipografía:** Instrument Serif + Barlow Condensed (sistema visual vigente del repo).
- **Email contacto:** `equipo@theworldismindproject.com` — **confirmado por Daniel el 18-may** (sustituye al fallback `equipo@twimproject.com`).
- **Cronograma completo 13 may → 30 sep** en `plan-captacion-verano-2026.md`.

---

## 4 · Relación con otros activos del repo

- **Libro en desarrollo**: `documentos-internos/libro-tu-valor-no-esta-en-su-mirada/` (manuscrito limpio del 11 may + revisión temario) trabaja exactamente el mismo cuadro psíquico que el taller. Pueden venderse juntos o cross-sellearse.
- **Programa «Deja de Buscarte en Otros»**: `documentos-internos/programa-deja-de-buscarte-en-otros/` está estructurado (briefing, currículo, módulos, workbook, protocolo 21 días, stripe, email confirmación). Es el producto digital asíncrono del mismo eje. Decisión estratégica de Daniel del 13 may: priorizar Volver a Mí ahora, grabar Deja de Buscarte como tope agosto.
- **Lead magnet activo del libro Engranajes**: `libro/capitulo-3/` + automation MailerLite «Lectores · Engranajes Cap3» (PR #149 mergeado el 13 may). Su Cap III es sobre el Juez Interno = mismo concepto central del taller. **El lead magnet del libro es el primer escalón natural del embudo del taller.**
- **Sprint editorial activo semana 19 may**: Carta #2 «La voz que te juzga» (`contenido-rrss/te-escribo-newsletters/carta-02-la-voz-que-te-juzga.html`) + Carrusel #3 «5 frases del juez interno» (`contenido-rrss/te-escribo-voz-que-te-juzga/`). **Toda esa publicación es ya regado del terreno para el taller.**

---

## 5 · Inconsistencias dossier vs repo — TODAS RESUELTAS

Las dos discrepancias bloqueantes quedaron resueltas el 13 may con la confirmación de Daniel en PR #151:

| Dossier ChatGPT dice | Verdad operativa cerrada | Estado |
|---|---|---|
| Newsletter «Cartas desde el diván» | **«Te escribo»** | ✅ resuelto el 13 may |
| Tipografía DM Serif Display + DM Sans | **Instrument Serif + Barlow Condensed** | ✅ resuelto el 13 may |
| Daniel «especialista en psicoanálisis…» | Mismo en CLAUDE.md + landing libro | ✅ consistente desde el principio |
| Logo «Mind World Project» | Logo `logo-mindworld.png` en root del repo | ✅ consistente desde el principio |
| Paleta cromática «exacta de twimproject.com» | `#173D30 / #265C4B / #C2A78B / #FDFCFA` | ✅ consistente desde el principio |

---

## 6 · Próximos pasos · estado actualizado 13 may

**Cerrado (✅):**

1. Daniel contestó las 14 preguntas operativas (PR #151 mergeado).
2. Code argumentó y cerró las decisiones delegadas (`decisiones-cerradas.md`).
3. Discrepancia tipografía resuelta (Instrument Serif + Barlow Condensed).
4. Discrepancia newsletter resuelta («Te escribo»).
5. Calendario reprogramado a otoño: **S1 = miércoles 30 sep → S8 = 18 nov 2026** (tras pregunta de Daniel del 13 may sobre si verano era buena fecha → análisis científico → confirmación de reprogramación).
6. Plan B si <5 plazas al 22 sep (posponer a 14 oct con calendario corrido hasta 2 dic; si <5 al 5 oct, cancelar; si 0-2 al 22 sep, cancelar inmediatamente).
7. **Beneficio operativo colateral:** agosto de Daniel queda íntegro como vacaciones. Junio-julio se libera para grabar el programa «Deja de Buscarte en Otros» asíncrono. En Q4 2026 hay dos productos vivos simultáneamente.

**Pendiente (⚠️):**

1. ~~**MailerLite API**~~ ✅ **RESUELTO el 13 may ~14:30 CEST**. Daniel ejecutó paso 2 (diag endpoint), Code confirmó que la API key NO está revocada (hipótesis original falsada). Estado real: 4 env vars secundarias ausentes (`INSCRITAS_TDAH`, `INSCRITAS_BACH`, `LEAD_IMPOSTORA`, `LEAD_BURNOUT`) — **no bloquean el taller Volver a Mí ni la captación newsletter actual**. Detalle en `mailerlite-api-incidencia.md` §4.3-§4.4. Pendiente menor opcional: Daniel decide si activa los 4 forms secundarios o desactiva las landings asociadas (decisión no urgente).
2. **Artefactos** — reparto cerrado el 18-may (ver §2): los produce Code (PDFs, análisis, benchmarks, proyecciones, landing); identidad = la existente del repo; informe técnico MailerLite ya resuelto. Ya no se espera que Daniel los pase.
3. ~~**Confirmar dominio email**~~ ✅ **RESUELTO 18-may**: `equipo@theworldismindproject.com` confirmado por Daniel.
4. ~~**Decisión lead magnet del taller**~~ ✅ **RESUELTO 18-may**: Daniel da OK al lead magnet «5 señales de hambre de mirada». Desbloquea su producción.
5. ~~**Colega de cobertura clínica agosto**~~ ✅ **RESUELTO 18-may**: NO hay colega. **Decisión de Daniel:** en agosto él NO abre consulta, así que tendrá hueco y **responde personalmente los emails** (las respuestas pueden tardar algo más, sin escalada a tercero). El autoresponder de agosto refleja esto, no deriva a nadie. Actualizar en consecuencia `plan-captacion-verano-2026.md` §4 fase 3.

**Cuando 1-4 estén resueltos**, el siguiente PR construye:

- Landing pública en `talleres/volver-a-mi/index.html` con todos los datos cerrados.
- Grupo `pre-venta-volver-a-mi` en `subscribe.js` + env var.
- Lead magnet específico del taller (si Daniel da OK).
- Automation MailerLite del taller con copy de 3-4 emails de pre-venta.
- Brief operativo Meta Ads con copy + audiencias + UTMs.
- Actualización `sitemap.xml`.

---

**Última actualización:** 13 may 2026 · sesión `claude/improve-proposal-quality-pq3d9` · pendiente de input de Daniel para completar §2 y §3.
