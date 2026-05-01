# TODO pendiente · sesión 30 abril 2026

> Cuando Daniel vuelva mañana o cualquier otro día, decirle a Claude:
> **"Ejecuta el TODO pendiente"**
> Claude lee este archivo y genera los 3 docs faltantes con la decisión ya cocida.

---

## Contexto de la sesión 30-04-2026

Decisiones cerradas durante la sesión:

1. **Stack de producción audio + vídeo TWIM** = NotebookLM (organización + estructura) + ElevenLabs (clonación de voz) + YouTube + Spotify.
2. **NotebookLM nunca con material clínico de pacientes.** Solo material editorial propio (artículos, libro, notas, briefings).
3. **ElevenLabs con voz clonada de Daniel + disclosure transparente** ("Opción 2"). Audio Briefings con voz Daniel sintetizada, no voces sintéticas norteamericanas de NotebookLM Audio Overview.
4. **Ritmo objetivo:** 1 episodio/2 semanas mayo-agosto, subir a 1/semana desde septiembre cuando entre VA.
5. **Reciclaje cruzado:** 1 episodio podcast → 1 vídeo YouTube + 1 audio Spotify + 3-5 Shorts/Reels + 1 carrusel IG + 1 fragmento newsletter + 1 cita visual.

Docs ya generados hoy:

- `documentos-internos/ceo-anexo-stack-produccion-audio-video.md` (rectifica doc CEO §8 + añade palanca #4).
- `documentos-internos/elevenlabs-clonacion-voz-podcast.md` (referencia técnica completa).

---

## Docs pendientes — generar mañana

### Doc #3 · YouTube + Podcast · Estrategia de canal

**Archivo:** `documentos-internos/youtube-podcast-estrategia-canal.md`

**Estructura recomendada:**

1. TL;DR — qué es el canal, qué publica, qué objetivos.
2. Estado actual (10,1K subs YouTube, TWIM Podcast 4 episodios, Los Invitados 15 episodios, Spotify activo).
3. Posicionamiento del canal — Daniel-clínico no Daniel-influencer (igual que doc CEO §2). Sin clickbait, sin frases motivacionales.
4. Diferenciación TWIM Podcast vs Los Invitados — formato, audiencia, objetivo.
5. Calendario editorial (1 cada 2 semanas mayo-agosto, alineado con calendario IG del PR #94 §11.3 — los pilares se rotan).
6. Pilares temáticos (mismos 4 racimos del doc CEO §3.1: autoexigencia, dependencia, burnout, adolescencia).
7. Reciclaje cruzado — mencionar que se desarrolla en doc separado #5.
8. Monetización YouTube — umbrales, estimación de ingresos a 10K/25K/50K subs (referenciar números del anexo §6 KPIs).
9. SEO de YouTube — títulos, descripciones, tags, thumbnails consistentes con sistema visual IG.
10. Shorts derivados — política (1 episodio = 3-5 Shorts), formato, cadencia.
11. KPIs del canal (mismos del anexo CEO §6 más detalle).
12. Riesgos y mitigación (cambio algoritmo, demonetización por contenido AI sin disclosure, saturación, etc.).
13. Decisiones a cerrar este mes.

**Tono:** mismo que doc CEO. Honesto, específico, sin hype.

**Referencias internas:** anexo CEO, doc ElevenLabs, sistema visual IG (PR #94), automatización IG (PR #95).

### Doc #4 · NotebookLM · Infraestructura interna de TWIM

**Archivo:** `documentos-internos/notebooklm-infraestructura-interna.md`

**Estructura recomendada:**

1. TL;DR — qué hace NotebookLM en TWIM, política de uso.
2. **Política estricta de privacidad clínica** (NUNCA pacientes, ni anonimizados parciales — solo si la anonimización es total y no permite re-identificación).
3. Notebooks recomendados — listado de notebooks específicos a crear:
   - **Marco editorial TWIM** (CLAUDE.md + doc CEO + briefings + 5-7 artículos representativos). Para onboarding Sergio + VA + cualquier colaborador futuro.
   - **Pilar autoexigencia** (todos los artículos del racimo + carta #2).
   - **Pilar dependencia** (todos los artículos + briefing programa Deja de Buscarte en Otros).
   - **Pilar burnout** (todos los artículos + carrusel cansancio psíquico + Te escribo carta #1).
   - **Pilar adolescencia** (artículos + plan talleres + briefing).
   - **Libro Engranajes** (manuscrito completo) — para citar y reciclar.
   - **Por episodio de podcast** (notebook efímero por episodio, archivable post-publicación).
4. Workflows operativos:
   - Generar estructura de episodio podcast.
   - Generar borrador de carrusel IG.
   - Generar borrador de carta "Te escribo".
   - Onboarding rápido de Sergio o VA.
   - Investigación cruzada de un concepto.
5. Lo que NotebookLM SÍ hace bien — organizar, resumir, conectar fuentes, generar estructura.
6. Lo que NotebookLM NO hace bien — escribir con voz TWIM auténtica (siempre requiere edición editorial humana), resolver conceptos clínicos delicados, sustituir lectura humana del material original.
7. Política de Audio Overviews — **NO publicar Audio Overviews de NotebookLM directamente como podcast.** Para podcast se usa ElevenLabs sobre guion editorial Daniel (ver doc #2).
8. Riesgos y mitigación (Google cierra producto, cambio de funcionalidades, fugas accidentales de info).
9. Coste — gratis (al 30-04-2026). Si Google introduce planes de pago, evaluar.
10. Decisiones a cerrar este mes.

**Tono:** referencia operativa, similar al doc de automatización IG.

**Referencias internas:** anexo CEO, doc ElevenLabs, doc TWIM Clinic (para onboarding Sergio).

### Doc #5 · Reciclaje de contenido · 1 episodio → 7 piezas

**Archivo:** `documentos-internos/reciclaje-contenido-pipeline.md`

**Estructura recomendada:**

1. TL;DR — cada episodio del podcast genera 7 piezas derivadas. Workflow descrito.
2. Por qué importa — un esfuerzo de producción alimenta el ecosistema completo durante una semana sin esfuerzo extra.
3. Las 7 piezas derivadas de cada episodio:
   - 1 vídeo YouTube (audio + cover estático + waveform).
   - 1 audio Spotify (mismo audio).
   - 3-5 Shorts/Reels (recortes de 30-60 s con caption + cover branded).
   - 1 carrusel IG sistema A1 (idea principal del episodio en 5-7 slides).
   - 1 cita visual sistema A2 (frase memorable del episodio).
   - 1 fragmento newsletter "Te escribo" (extracto de 200-400 palabras + audio integrado).
   - 1 post LinkedIn (versión más profesional del fragmento).
4. Workflow paso a paso (con tiempos estimados):
   - Días 1-2: producción episodio (3-4 h).
   - Día 3: generación de derivados (2-3 h).
   - Días 4-7: distribución programada según calendario.
5. Plantillas reutilizables — específicas para cada formato derivado.
6. Cómo se integra con el calendario IG del PR #94 §11.3 — sustituir parte del calendario por piezas derivadas de podcast (más eficiente que producir cada pieza desde cero).
7. Cuándo entra la VA — qué tareas se delegan, qué tareas Daniel mantiene (curaduría editorial siempre).
8. Métricas — cuánto multiplica el output por hora invertida vs producción aislada.
9. Riesgos — mensaje repetitivo si todas las piezas son demasiado similares; mitigación: cada formato tiene framing distinto.
10. Decisiones a cerrar este mes.

**Tono:** operativo y muy práctico. Esto es el manual de producción.

**Referencias internas:** todos los docs anteriores (es la pieza que cierra el sistema).

---

## Orden de generación recomendado

Mañana, generar en este orden:

1. **#3 YouTube + Podcast estrategia** primero — pone el "qué" y el "porqué" del canal.
2. **#4 NotebookLM infraestructura** segundo — pone el "cómo" del input.
3. **#5 Reciclaje pipeline** tercero — pone el "cómo" del output, integrando todo.

Cada uno con su PR independiente. Como hicimos con los 5 PRs anteriores.

---

## Reglas de generación (recordatorios para Claude mañana)

- **Construir por bloques.** Empezar con `Write` esqueleto, luego ir añadiendo con `Edit`. Igual que se hizo con los docs de hoy. Evita timeout.
- **Tono:** honesto, sin hype, con criterio de Daniel-CEO mirando al negocio. Igual que doc CEO + anexo + ElevenLabs.
- **Decisiones cocidas:** las decisiones ya están tomadas en este TODO. NO volver a abrir debate sobre Opción 2 (ElevenLabs con disclosure), ritmo (1 cada 2 semanas), Audio Overviews directos (NO publicar). Documentar la decisión, no relitigar.
- **Tras cada doc:** commit + push + crear PR. Reutilizar la rama de trabajo actual si sigue siendo la adecuada; si no, crear una nueva siguiendo la convención de ramas del repo.
- **Borrar este archivo TODO-PENDIENTE.md después** de generar los 3 docs (para que no quede residual).

---

## Cierre

Si Daniel olvida pedirlo y este archivo queda dormido más de una semana, **Claude debe proactivamente preguntarle si quiere que ejecute el TODO** la primera vez que detecte el archivo en una sesión nueva sobre el repo.

— Generado en sesión 30-04-2026 como mecanismo de continuidad entre sesiones.
