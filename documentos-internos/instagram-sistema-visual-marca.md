# TWIM Project · Sistema visual Instagram + plan de transición

> **⚠️ EVOLUCIÓN 10-jun-2026 · leer antes de producir posts/carruseles.** Los datos de mayo-junio (Carruseles #2-#4 · 94,3 % alcance solo a seguidores · save 0,24 % · confirmación de Daniel con capturas: «los peores en años») refutaron el formato **lámina tipográfica como portada** — en ambas paletas A1 y A2, con y sin foto de fondo. El sistema de este doc sigue vigente en paleta, tipografía, principios y políticas, pero el **empaquetado de portada y la arquitectura del carrusel** se rigen ahora por `instagram-rearme-posts-carruseles-2026-06-10.md` (portada = escena humana en foto + hook concreto en segunda persona · lámina verde en interiores · carrusel mixto de 7). Patrón de evolución de reglas: se persiste, no se borra.

> Documento interno · v1 · 30 abril 2026
> Autor: Daniel Orozco Abia · Borrador estructurado por Claude
> Estado: borrador para discusión. Algunas decisiones (§4) dependen de confirmación de Daniel sobre la arquitectura de marcas — marcadas como "PENDIENTE CONFIRMAR".

---

## Resumen ejecutivo

El feed actual de @daniorozcopsicologo tiene **al menos 6 estéticas conviviendo sin sistema**, mezcla contenido propio con reposts de otras cuentas (@unpsicologorandom, @psicologo_random) sin curaduría, incluye contenido personal (familia, bebé) sin política definida, y publica formato clickbait estilo YouTuber ("Dosis de Realidad", "V0yeur1sm0 del Poder", banderas rojas tipo Impact) que es la **antítesis** del posicionamiento "Psicología Profunda y Aplicada · anti-coaching · Daniel-clínico no Daniel-influencer" declarado en CLAUDE.md y desarrollado en el doc CEO §2.

Este documento define el sistema visual único, las reglas editoriales, el plan de transición del feed actual y la decisión estratégica sobre la arquitectura de marcas (consolidación vs portafolio).

## Índice

1. Diagnóstico ampliado
2. Principios editoriales (lo que sí, lo que no)
3. Sistema visual único — paleta, tipografías, plantillas
4. Arquitectura de marcas — decisión estratégica pendiente
5. Política sobre contenido personal
6. Política sobre reposts de otros perfiles
7. Cover de reels (la pieza que más rompe el feed)
8. Stories destacadas — limpieza obligatoria
9. Pinned posts — reorganización
10. Plan de transición (qué hacer con los ~500 posts ya publicados)
11. Calendario editorial 30 días alineado
12. Checklist editorial pre-publicación
13. KPIs y métricas
14. Decisiones a cerrar este mes

---

## 1 · Diagnóstico ampliado

Analizadas 13 capturas del feed @daniorozcopsicologo el 30-04-2026 (~120 posts visibles), el feed presenta **6 estéticas conviviendo** y **3 marcas de origen** mezcladas (propia + dos reposteadas regularmente):

### 1.1 · Las 6 estéticas detectadas

| # | Sistema | En marca | Ejemplos |
|---|---|---|---|
| 1 | **Carrusel editorial TWIM** verde oscuro #173D30, serif elegante, kicker minimal | ✅ **Sí. Es el sistema correcto.** | "Tu cansancio no es físico" · "5 señales de que buscas validación" · "Si alguna vez has sentido un vacío" |
| 2 | Crema con highlight amarillo, ilustraciones flat estilo educativo | ⚠️ Coherente entre sí pero ≠ sistema #1. Mezcla paletas. | Pinneado "Familias decir la verdad" · carrusel "AUTOESTIMA" · "La autoestima no nace de decirte quiérete más" |
| 3 | Reels selfie con caption blanca tipo Instagram default, sin cover branded | ⚠️ Genérico. Sin identidad. | La mayoría de reels hablando |
| 4 | **Reels clickbait tipo YouTuber** — banderas rojas, font Impact, mayúsculas agresivas | ❌ **Antítesis de la marca.** | "Dosis de Realidad" · "¡Stop Bullying!" · "El V0yeur1sm0 del Poder" · "Cuando un NO se vuelve delito" |
| 5 | Reposts virales sin curaduría (frames de pelis, memes, captura email Epstein, fotos personales) | ❌ Rompe la curaduría editorial. | "La lista Invisible" · captura email Epstein · "Majo, la mujer que Hackeo" · selfie con bebé |
| 6 | TWIM PODCAST — verde oscuro pero tipografía bold sans diferente | ⚠️ Sub-sistema casi en marca, falta unificar tipografía. | Cover "EPISODIO 1 · El cansancio que no se cura durmiendo" |

### 1.2 · Las firmas/nicks históricos presentes en el feed

> **Aclaración del 30-04-2026:** las firmas @unpsicologorandom y @psicologo_random NO son cuentas externas. Son nicks ANTERIORES de Daniel — etapas previas de la marca antes de consolidarse como @daniorozcopsicologo + TWIM Project. El contenido firmado con esos nombres es propio, solo de otra fase.

| Firma | Frecuencia visible | Estilo | Naturaleza |
|---|---|---|---|
| **TWIM Project / @daniorozcopsicologo** | Mayoritaria | Sistemas 1, 2, 3, 4 (mezclado) | Marca actual |
| **@unpsicologorandom + "The World Is Mind Project"** | Frecuente | Crema/beige con sans serif bold negro | **Etapa anterior** de Daniel. Contenido propio antiguo con branding distinto. |
| **@psicologo_random** | Ocasional | Serif crema con decoración de ramas | **Etapa anterior** de Daniel. Contenido propio antiguo con branding distinto. |
| Otros (@danyblazquez, etc.) | Esporádica | Diversos | Reposts/menciones de otros perfiles. Cortar o reformular como cita propia. |

Esto cambia el problema: no es "mezcla de cuentas externas en mi feed", es **arrastre histórico** de tres etapas de evolución de marca cohabitando en el mismo grid sin transición visible.

### 1.3 · Los 4 problemas estructurales

1. **Mezcla de identidades visuales.** Para el seguidor casual, el feed parece de 3-4 perfiles distintos cosidos juntos. La cuadrícula visual es caótica.
2. **Contraste con el posicionamiento declarado.** El doc CEO §2 dice literalmente: *"No es Daniel-influencer. Es Daniel-clínico. La autoridad viene del CV11515 y de los años de consulta, no del crecimiento de seguidores."* El sistema #4 (clickbait) y el #5 (reposts virales sin curaduría) dicen lo contrario.
3. **Energía mal asignada.** Los reels clickbait (sistema #4) promedian 5K–30K views (alta visibilidad, baja conversión a embudo TWIM). Los carruseles editoriales (sistema #1) promedian 2K–5K (baja visibilidad pero alta conversión a embudo). Estás dedicando esfuerzo al formato que **no** alimenta el negocio editorial.
4. **Personal mezclado sin política.** Bebé, pareja, paseos por Asturias, foto de pueblo, momentos familiares — todo aparece sin política definida sobre qué pertenece a TWIM Project y qué no.

---

## 2 · Principios editoriales (lo que sí, lo que no)

Antes del sistema visual, los principios. Sin estos, cualquier sistema visual se erosiona en 3 meses.

### 2.1 · Lo que sí

- **Cada post debe responder a "qué le aporta esto al lector como adulto pensante"**, no "qué hace que más gente le dé like".
- **Tono descriptivo del mecanismo**, no prescriptivo. "Esto es lo que pasa en tu mente cuando…" no "Tú puedes con esto si…".
- **Lenguaje de adulto inteligente.** Nada de simplificaciones infantilizadas.
- **Imagen sobria.** Verde oscuro #173D30, beige #C2A78B, crema #FDFCFA, blanco roto. Tipografía Barlow Condensed o serif clásica. Foto siempre con tratamiento de color.
- **Si algo se publica, queda.** No se publica para borrar tres días después por "no funcionó". Eso destruye autoridad.

### 2.2 · Lo que no

- **No clickbait.** Nada de banderas rojas, font Impact en mayúsculas agresivas, "DOSIS DE REALIDAD", "¡PELIGRO!", "V0YEUR1SMO", titulares con tildes invertidas o números reemplazando letras.
- **No frases motivacionales descontextualizadas.** "Eres suficiente", "merece amor", "agradece más" — están prohibidas. CLAUDE.md y el doc CEO lo dicen explícito.
- **No reposts virales sin curaduría.** Los memes, frames de pelis, capturas de Twitter de actualidad — fuera. Si hay algo viral que merece comentario, se reformula en post propio.
- **No emojis.** Ni en captions ni en imágenes. CLAUDE.md lo dice como regla absoluta.
- **No posts personales accidentales.** Familia, bebé, paseos, fotos casuales — solo bajo política definida (ver §5). El feed no es Stories.
- **No tres mensajes a la vez.** Un post = una idea. Si la idea no cabe en 1-2 frases de hook, no es post, es artículo.

---

## 3 · Sistema visual único — paleta, tipografías, plantillas

### 3.1 · Paleta de marca (la única permitida)

```
Verde TWIM oscuro     #173D30   ← fondo dominante de carruseles tipo A
Verde TWIM medio      #265C4B   ← acentos, links, kicker
Beige TWIM            #C2A78B   ← kickers, tipografía secundaria
Crema TWIM            #FDFCFA   ← fondo dominante de carruseles tipo B
Texto sobre verde     #FDFCFA   ← cream sobre fondo oscuro
Texto sobre crema     #173D30   ← verde oscuro sobre fondo crema
```

**Esto es lo único.** No naranjas, no rojos, no amarillos highlight, no azules, no resaltadores. Si una idea necesita resalte, se hace con peso tipográfico (bold) o con kicker beige sobre fondo verde.

### 3.2 · Tipografía de marca

> **Actualización 6-may-2026 · alineamiento con verdad operativa.** El carrusel "Tu cansancio no es físico" publicado el 25 abril (referencia visual del feed) y el SVG de la story crema `contenido-rrss/te-escribo-newsletters/imagenes-stories/story-01-fragmento-carta1.svg` usan **Instrument Serif** para titulares editoriales — incluyendo cursiva para cierres aforísticos como *"callándose"* o *"Y eso empieza por nombrarlo"*. El doc anterior prohibía cursiva por arrastre, pero la práctica establecida es otra. Esta sección refleja la práctica real.

- **Kickers (etiquetas pequeñas):** Barlow Condensed Bold mayúsculas, letter-spacing 3-4 px, color beige.
- **Setup / body en sans:** Barlow Condensed Regular para frases de transición y subtítulos.
- **Display / títulos editoriales:** **Instrument Serif Regular** (Google Fonts) — serif transitional con personalidad editorial alta. Tamaños 78-130 px en carruseles 1080×1350.
- **Closer aforístico / cita íntima:** **Instrument Serif Italic** sobre beige `#C2A78B`. Reservada para frases-resumen de slide o cierres ("ni qué hacer con ello", "A veces solo entender ya mueve cosas"). NO se usa para cuerpo continuo, solo para el remate de un slide o pieza.
- **Cuerpo largo en piezas que lo requieran:** Lora Regular como alternativa serif. En la práctica se usa muy poco — la mayor parte del cuerpo va en Instrument Serif Regular o Barlow Condensed.
- **Prohibidas:** font Impact, Bebas Neue agresiva, Poppins, Montserrat, cualquier sans serif decorativa, cualquier serif distinta a Instrument Serif/Lora. La cursiva se usa SOLO en Instrument Serif Italic como acento aforístico, nunca en sans, nunca en cuerpo continuo.

### 3.3 · Las 3 categorías de contenido permitidas

**Solo tres.** Si una pieza no encaja en ninguna, no se publica.

#### A. Carrusel editorial TWIM

- Formato: 1080×1350 (4:5).
- 5-9 slides por carrusel.
- Slide 1 (hook): kicker beige + título corto + footer "@daniorozcopsicologo · twimproject.com".
- Slides 2-N: idea desarrollada, una frase por slide.
- Slide final (CTA): kicker beige + frase de cierre + URL "twimproject.com" o CTA específico.
- Dos paletas posibles:
  - **A1 verde dominante** (#173D30 fondo, cream texto, beige kicker). Es el sistema #1 actual del feed que sí está bien.
  - **A2 crema dominante** (#FDFCFA fondo, verde oscuro texto, beige kicker). Para variar el ritmo del feed sin romper marca.

Referencia interna ya existente en el feed: "Tu cansancio no es físico", "5 señales de que buscas validación", "Si alguna vez has sentido un vacío".

#### B. Reel original con cover branded

- Formato: 1080×1920 (9:16).
- **Cover obligatorio** generado a posteriori desde plantilla (specs §7), no el frame inicial del vídeo.
- Vídeo: Daniel hablando a cámara, fondo neutro (estantería, despacho), buena iluminación, audio nítido.
- Caption en vídeo (subtítulos): tipografía Barlow Condensed Bold blanco con borde verde oscuro fino. NO la caption blanca default de Instagram. NO highlights amarillos/morados/cyan agresivos.
- Duración: 30-90 s. Si necesita más de 90 s, hazlo artículo.

#### C. Cita visual / micropost

- Formato: 1080×1350 (4:5).
- Pieza única (no carrusel).
- Una frase corta de la newsletter, del libro, o un concepto clínico nombrado. Tipografía display Barlow Condensed o Lora.
- Footer: "@daniorozcopsicologo · twimproject.com" o "Los engranajes de la mente · libro" según origen.
- Misma paleta A1 o A2.

### 3.4 · Plantillas — specs detallados para diseñador o asistente

**Plantilla A1 · Carrusel verde dominante** (alineada con verdad operativa del 25 abril 2026):

- Canvas 1080×1350.
- Fondo: sólido #173D30.
- Margen interior: 80 px en todos los lados.

- **Header (todas las slides):**
  - Kicker top-left: Barlow Condensed Bold 26-28 px, mayúsculas, letter-spacing 4 px, color #C2A78B. Texto: nombre del carrusel/serie ("TWIM PROJECT", "TE ESCRIBO · CARTA #1", etc.).
  - Paginación top-right: Barlow Condensed Regular 26 px, color #C2A78B, formato `0X / 0N`.

- **Slide hook (slide 1):**
  - Título principal en Instrument Serif Regular 90-130 px (según largo), color #FDFCFA, centrado horizontalmente, vertical en tercio superior-medio.
  - Subtítulo opcional: Barlow Condensed Regular 40-50 px, color #C2A78B, centrado debajo del título principal.

- **Slides cuerpo (2 a N-1):** patrón setup + punchline:
  - Setup en Barlow Condensed Regular 40-46 px crema o beige, varias líneas centradas en tercio superior.
  - Punchline en Instrument Serif Regular 90-130 px crema, centrado en tercio medio.
  - Closer opcional en Instrument Serif Italic 80-100 px sobre beige `#C2A78B`, centrado en tercio inferior antes del footer (para cierres aforísticos).

- **Slide CTA (slide final):**
  - Título en Instrument Serif Regular 100-130 px crema.
  - Subtítulo en Barlow Condensed Regular 40-44 px crema.
  - URL destacada en Barlow Condensed Bold 44-52 px, color #C2A78B (sin caja).
  - Pie en Instrument Serif Italic 44-52 px sobre beige (opcional, fecha o promesa concreta).

- **Footer (todas las slides):** logo MIND WORLD PROJECT blanco sólido ~120-150 px de altura, centrado horizontalmente con base a ~200 px del borde inferior. Debajo, "@daniorozcopsicologo · twimproject.com" en Barlow Condensed Regular 24 px crema 100% opacidad, centrado a ~80 px del borde inferior.

> **Nota:** la verdad operativa del 25 abril usa footer **centrado** (no bottom-left) con el logo MIND WORLD encima del handle. Esto sustituye la indicación previa de "bottom-left opacity 70%" que era desactualizada.

**Plantilla A2 · Carrusel crema dominante:**
- Canvas 1080×1350.
- Fondo sólido #FDFCFA.
- Mismo layout que A1 pero invirtiendo colores (texto #173D30, kicker #265C4B).

**Plantilla C · Cita visual:**
- Canvas 1080×1350.
- Fondo A1 o A2.
- Frase central: Lora Regular 56 px o Barlow Condensed Bold 72 px, según largo. Vertical centrado.
- Atribución bottom: Barlow Condensed Regular 22 px, "— Daniel Orozco Abia · TWIM Project" o "— de 'Los engranajes de la mente'".

### 3.5 · Lo que se elimina del repertorio actual

| Elemento actual | Sustituir por |
|---|---|
| Banderas rojas tipo "Dosis de Realidad" | Kicker beige minimal sobre verde, mayúsculas sin font Impact |
| Highlights amarillos chillones | Bold tipográfico o kicker beige |
| Highlights cyan/morados estilo cap subtitle | Subtítulos Barlow Condensed bold blanco con borde fino verde oscuro |
| Font Impact / Bebas Neue agresivas | Barlow Condensed Bold |
| Reposts de memes virales | Eliminados o reformulados como cita visual con comentario propio |
| Selfies casuales con bebé en feed | Reservados para Stories (ver §5) |
| Títulos con números reemplazando letras (V0yeur1sm0, M*3rt3) | Prohibidos absolutamente |

---

## 4 · Arquitectura de marcas — decisión confirmada

> **Confirmado por Daniel (30-04-2026):** @unpsicologorandom y @psicologo_random son NICKS ANTERIORES suyos, no cuentas distintas. "The World Is Mind" es proyecto matriz vivo. La decisión queda fijada en **Opción 1 — Consolidación TWIM Project**, con un matiz: hay un legado histórico de contenido propio bajo branding antiguo que hay que gestionar (no eliminar).

### 4.1 · Las tres opciones realistas

#### Opción 1 — Consolidación TWIM Project (recomendada si solo @daniorozcopsicologo es tuya)

- **Una sola cuenta:** @daniorozcopsicologo, marca TWIM Project.
- "The World Is Mind" como proyecto matriz solo aparece en el libro y la web (twimproject.com), no como cuenta IG separada.
- Los reposts de @unpsicologorandom y @psicologo_random se cortan. Si una cita es muy buena se reformula como cita visual propia con atribución (§6).
- Foco editorial absoluto.

#### Opción 2 — Portafolio diferenciado (solo si las tres cuentas son tuyas y hay equipo)

- **3 cuentas con identidades visuales completamente distintas y propósitos no solapados:**
  - **@daniorozcopsicologo · TWIM Project** — clínico/editorial profundo, sistema visual definido en §3.
  - **@unpsicologorandom · The World Is Mind Project** — divulgación más amplia, formato podcast/entrevistas. Sistema visual propio, distinto.
  - **@psicologo_random** — experimentos rápidos, formato prueba. Sistema propio.
- Requiere asistente o equipo. Imposible sostener tres voces consistentes con una sola persona escribiendo.
- Objetivo: cada cuenta captura una audiencia distinta y todas convergen en el embudo de pago de TWIM Project.

#### Opción 3 — Migración (si las cuentas son tuyas pero quieres consolidar)

- Mantener @daniorozcopsicologo como cuenta principal.
- Anuncio explícito en @unpsicologorandom y @psicologo_random: "este contenido se traslada a @daniorozcopsicologo".
- Pin en cada una con CTA "→ síguenos en @daniorozcopsicologo".
- Las dos cuentas se quedan dormidas (no se borran, por SEO inverso y por si alguien las busca).

### 4.2 · Decisión fijada: Opción 1 con gestión de legado

**Acciones derivadas:**

- **Toda publicación nueva** sigue el sistema visual §3 al 100 %, firmado solo "@daniorozcopsicologo · TWIM Project".
- **No volver a publicar piezas firmadas como @unpsicologorandom o @psicologo_random.** Aunque ese contenido sea bueno, la firma vieja es ruido para la marca actual.
- **Las mejores piezas de las etapas anteriores se rescatan y republican** con maquetación nueva (sistema A1 o A2) y firma actualizada. Lo demás se archiva o se deja (ver §10).
- **"The World Is Mind"** se posiciona como **proyecto matriz** visible en bio del perfil (web + libro), no como cuenta IG separada. La bio puede decir algo como: *"TWIM Project · Psicología Profunda y Aplicada · The World Is Mind"*.

### 4.3 · Lo que NO conviene (las trampas)

- **Mantener tres cuentas activas haciéndolo todo tú mismo "porque cuesta cerrar".** Esto es la situación actual. La energía dispersada en tres voces nunca construye una marca fuerte.
- **Repostar de cuentas externas como si fueran propias** cuando esas cuentas tienen estética conflictiva con la tuya. Confunde a tu audiencia sobre quién eres realmente.
- **"Probar formatos nuevos" en la cuenta principal sin sistema.** Cada experimento sin sistema desgasta el patrón. Los experimentos van en una cuenta secundaria o no se hacen.

---

## 5 · Política sobre contenido personal

> **Aclaración del 30-04-2026:** Las fotos familiares con icono de estrella ⭐ que aparecen en el feed son **publicaciones de Close Friends** (visibles solo para amigos cercanos en Instagram, no público general). Esto significa que para el seguidor regular de @daniorozcopsicologo, esas fotos **no aparecen**. Es una política de privacidad ya implementada que conviene formalizar y mantener.

La regla actual funciona. Vamos a documentarla y profundizarla.

### 5.1 · Política actual (a mantener y formalizar)

**Nivel mixto controlado · vía Close Friends.**

- **Feed público:** cero contenido familiar visible para audiencia general.
- **Close Friends (icono ⭐):** las fotos del bebé, pareja, paseos, fotos en pueblo, etc. van a este círculo restringido. Ya está siendo así, solo formalizar y mantener.
- **Stories generales (no Close Friends):** evitar familia. Si aparece, que sea muy ocasional y sin texto editorial encima.
- **Reels y carruseles:** nunca usar al bebé como gancho. "Mi hijo me enseñó X" — no.

### 5.2 · Cómo refinar la política

- **Auditar grupo Close Friends una vez al año.** El círculo crece y se mete gente que ya no es íntima. Vale la pena revisarlo en enero y junio.
- **Si una persona profesional (paciente, colaborador, periodista) entra al grupo Close Friends por error, sale.** No es por desconfianza — es por separación de roles.
- **Decisión sobre el bebé en posts profesionales (no Close Friends):** no aparecer. Ni siquiera en imágenes "anodinas" tipo "paseo familiar". El feed público es 100 % TWIM.
- **Si en algún momento decides hacer contenido sobre paternidad o crianza desde tu marco profesional**, que sea desde la teoría/clínica (no desde "mira lo que hace mi hijo"). Eso entra en TWIM Project legítimamente.

### 5.3 · Por qué importa

Tu marca crece porque alguien te lee y piensa "este tío sabe de lo que habla, no es un creador de contenido más". Cada foto del bebé en grid resta unos puntos a esa percepción. Sumado a 50 fotos en 2 años, la percepción cambia: pasa de "Daniel Orozco es un psicólogo serio" a "Daniel Orozco es un psicólogo simpático que comparte su vida". El segundo está saturado en Instagram. El primero es escaso y vale más.

---

## 6 · Política sobre reposts de otros perfiles

> Recordatorio: @unpsicologorandom y @psicologo_random eran nicks tuyos anteriores. La política sobre ellos se trata en §4 y §10 (gestión de legado). Esta sección habla solo de cuentas externas.

### 6.1 · Regla general

**No se repostea contenido visual de cuentas externas en el feed.** Ni de cuentas grandes (Recalcati, Anabel González), ni de virales del momento, ni de cuentas afines.

### 6.2 · Si un contenido externo es muy bueno

Dos opciones permitidas:

1. **Reformular como cita visual propia** (formato C de §3.3) atribuyendo claramente al autor. Ejemplo: "— Massimo Recalcati, *El complejo de Telémaco*" en footer.
2. **Compartir en Stories** con atribución y comentario propio. NO en feed.

### 6.3 · Por qué

Cada repost de cuenta externa hace tres cosas:

- Manda audiencia a otro creador en lugar de fortalecer tu autoridad.
- Mezcla estéticas en tu grid, rompe el sistema visual.
- Confunde sobre cuál es tu voz real (la del repost o la tuya).

Las cuentas con autoridad clínica más sólida (Anabel González, Recalcati en sus formatos digitales, Lori Gottlieb) **casi no repostean**. Su feed es 100 % producción propia. No es casualidad.

---

## 7 · Cover de reels — la pieza que más rompe el feed hoy

Hoy los reels van sin cover diseñado. Cada uno se queda con el frame inicial del vídeo, lo que produce una cuadrícula de selfies aleatorios. Es lo que más visualmente desarma el grid.

### 7.1 · Plantilla de cover de reel

- Canvas: 1080×1920 (la dimensión completa del reel) **PERO** Instagram solo muestra el cuadrado central 1080×1080 en el grid de perfil. Diseñar pensando en ambos.
- **Zona "feed grid" (centro 1080×1080):** debe ser legible y branded.
- Composición:
  - 60 % superior: foto de Daniel con tratamiento de color verde (overlay sutil verde oscuro a 15-20% de opacidad sobre la foto).
  - 40 % inferior: rectángulo verde oscuro #173D30 con kicker beige + título.
- Tipografía título: Barlow Condensed Bold 72 px mayúsculas, color #FDFCFA.
- Kicker arriba del título: Barlow Condensed Bold 24 px, mayúsculas, letter-spacing 4 px, color #C2A78B (ej: "TWIM REELS · Nº23" o "MICROCLASES · Ansiedad").
- Footer: Barlow Condensed Regular 22 px "@daniorozcopsicologo · twimproject.com" en color #FDFCFA opacity 70 %.

### 7.2 · Workflow recomendado

- Plantilla en Canva (o Figma) con capas editables: foto, título, kicker.
- Cada reel publicado pasa por la plantilla antes de subirse: 30 segundos de trabajo.
- Subir el cover en Instagram al publicar (Instagram permite "Cover photo" → "Add from gallery"). NO dejar el frame default.

### 7.3 · Categorías de reel = categorías de cover

Diferenciar covers por kicker para crear sub-series visuales:

- **TWIM REELS · Nº[X]** — reel general semanal.
- **MICROCLASES · [Tema]** — reel didáctico de 60-90 s sobre concepto clínico.
- **CARTAS · [Título]** — reel donde lees fragmento de la newsletter.
- **CASOS · [Pseudónimo]** — viñeta clínica anonimizada.
- **CONSULTA · [Pregunta]** — respuesta a pregunta de seguidor (filtrada).

---

## 8 · Stories destacadas — limpieza obligatoria

### 8.1 · Estado actual

Las capturas muestran al menos 5 destacadas mezclando dos brandings:
- **TWIMProject** — sello negro con foto Daniel.
- **Articulos T...** y **Shop Online** — sello blanco "MIND WORLD PROJECT".
- **Ponencias** — sello negro con foto Daniel.

Mezcla "TWIM Project" con "MIND WORLD PROJECT" sin lógica visible. Confunde al visitante nuevo sobre cuál es la marca.

### 8.2 · Propuesta — un solo sistema de portadas

Todas las portadas de destacadas siguen el mismo template:

- Canvas circular Instagram 161×161 px de visualización (subir a 1080×1080 para resolución).
- Fondo verde oscuro #173D30.
- Texto centrado: Barlow Condensed Bold mayúsculas color #C2A78B (beige), 1-2 palabras max.
- NO foto, NO logo encima del texto. Limpio.

### 8.3 · Reorganización de destacadas (orden recomendado)

1. **EMPIEZA** — qué es TWIM, qué tipo de contenido vas a encontrar, hacia dónde va si quiere más.
2. **NEWSLETTER** — qué es Te escribo, link al formulario.
3. **LIBRO** — Engranajes de la mente, link a Amazon + landing.
4. **PROGRAMAS** — Deja de Buscarte en Otros + futuros.
5. **TALLERES** — TDAH adolescentes + bachillerato.
6. **CONSULTA** — info de cómo trabajar contigo (1:1 o derivación supervisada Sergio).
7. **PRENSA / PONENCIAS** — apariciones en medios, charlas.
8. **PREGUNTAS** — FAQs frecuentes.

Eliminar destacadas sueltas que no encajen en este orden.

---

## 9 · Pinned posts — reorganización

### 9.1 · Estado actual

3 pinned: "Familias decir la verdad" (sistema 2 crema/amarillo), libro lifestyle, "Compromiso Sano" (clickbait).

Es lo primero que ve quien entra a tu perfil. Hoy comunica caos visual.

### 9.2 · Recomendación

Los 3 pinned deberían ser tus 3 mejores carruseles editoriales del **sistema A1 (verde dominante)** o **A2 (crema dominante)**, eligiendo:

1. **Una pieza de identidad** — algo que diga "esto es lo que vas a encontrar aquí". Ej: la pieza más clara del manifesto editorial.
2. **Una pieza de resultados** — algo que demuestre la calidad clínica del trabajo. Ej: el carrusel "Si alguna vez has sentido un vacío" si está performing bien.
3. **Una pieza con CTA al lead magnet más alto** — algo que termine en "→ Reto 7 días" o "→ Newsletter Te escribo".

Los 3 pinned son tu landing page de Instagram. Diseñarlos como tales, no dejarlos al azar.

---

## 10 · Plan de transición — qué hacer con los ~500 posts ya publicados

> No se borran. Borrar destruye señales de algoritmo y se nota en alcance durante meses. La estrategia es **archivar selectivamente + rescatar lo mejor**.

### 10.1 · Las 4 capas del legado

El feed actual contiene piezas de cuatro etapas. Cada una se trata distinto:

| Capa | Qué es | Acción |
|---|---|---|
| **A. Etapa actual TWIM (sistema #1)** | Carruseles verdes editoriales firmados @daniorozcopsicologo | **Mantener.** Son el patrón a multiplicar. |
| **B. Etapa @unpsicologorandom + The World Is Mind** | Crema/beige con sans serif bold, frases tipo "MADRES NARCISISTAS HIJOS ROTOS", "DISFRAZAS LO QUE DESEAS" | **Auditar y decidir pieza por pieza:** las que tengan buen alcance y se puedan republicar bajo nueva maquetación TWIM, rescatar. El resto, archivar. |
| **C. Etapa @psicologo_random** | Serif crema con ramas, tono editorial elegante | **Auditar y decidir pieza por pieza** igual que B. |
| **D. Reels clickbait + reposts virales sin curaduría** | "Dosis de Realidad", "V0yeur1sm0", capturas de Twitter, frames de pelis | **Archivar todo lo que pueda archivarse sin perder views útiles.** El contenido contradice la marca actual. |

### 10.2 · Lo que sí se hace

| Acción | Cuándo |
|---|---|
| **Cortar nuevas publicaciones que rompan el sistema desde mañana.** | Inmediato |
| **Reorganizar pinned posts** (§9). | Esta semana |
| **Limpiar stories destacadas** (§8). | Esta semana |
| **Crear plantilla cover de reels** (§7) en Canva/Figma. | Próximas 2 semanas |
| **Auditar el grid completo** marcando cada post como Capa A, B, C o D. | Junio 2026 |
| **Archivar capa D al completo** salvo los reels con más de 10K views (esos se quedan, son señal de algoritmo aprovechable). | Junio 2026 |
| **Identificar las 10-15 mejores piezas de capas B y C** y republicarlas re-maquetadas en sistema A1/A2 con firma TWIM. Captions reescritas. | Julio-Agosto 2026 |
| **Archivar las piezas B y C que no se republiquen.** | Agosto 2026 |

### 10.2 · Lo que NO se hace

- **NO borrar posts** masivamente.
- **NO publicar tanda de "limpieza" anunciando "vamos a profesionalizar el feed".** Es ruido y da explicaciones que nadie pidió.
- **NO eliminar reels con muchas views** aunque rompan el sistema. Esos reels tienen alcance prestado al algoritmo. Archivar solo los que no aportaron alcance.

### 10.3 · El nuevo grid — 6 meses

A los 6 meses de aplicar el sistema, el grid debería verse así:

- Filas alternando carruseles A1 (verde) y A2 (crema), creando ritmo visual de 2-3 posts.
- Reels intercalados con cover branded coherente (no rompen el patrón).
- Citas visuales puntuales como "respiro" entre carruseles.
- Cero clickbait, cero reposts, cero familia.

A los 12 meses: el visitante nuevo entiende qué es TWIM en 5 segundos solo viendo el grid.

---

## 11 · Calendario editorial 30 días alineado

> Plantilla de ritmo sostenible para 1 sola persona (Daniel) sin asistente. Cuando contrates VA, este calendario se duplica fácil.

### 11.1 · Ritmo semanal recomendado

| Día | Categoría | Formato | Tiempo de producción |
|---|---|---|---|
| Lunes | Carrusel A1 (verde) | 5-7 slides editoriales | 60-90 min |
| Miércoles | Reel original | 60-90 s + cover | 45-60 min |
| Viernes | Cita visual A2 (crema) | Pieza única | 15-20 min |

**3 publicaciones/semana = 12 al mes.** Es el suelo sostenible. Más que esto sin asistente lleva a publicar peor.

### 11.2 · Pilares temáticos por semana

Para que el feed tenga ritmo de pilares (no aleatorio), rotar pilares por semana:

| Semana | Pilar |
|---|---|
| Semana 1 | Autoexigencia / juez interno / urgencia mental |
| Semana 2 | Dependencia emocional / validación |
| Semana 3 | Burnout / cansancio psíquico |
| Semana 4 | Manifesto editorial / método / posicionamiento (frases del libro, citas de la newsletter) |

Adolescencia entra cuando el racimo editorial esté lanzado (§ doc CEO).

### 11.3 · Mes 1 piloto (mayo 2026)

| Fecha | Día | Categoría | Pilar | Tema sugerido |
|---|---|---|---|---|
| 4 mayo | Lunes | Carrusel A1 | Autoexigencia | "El TENGO QUE no es una idea, es un modo automático" |
| 6 mayo | Miércoles | Reel + cover | Autoexigencia | Microclase 60s "Qué pasa en tu mente cuando no puedes parar" |
| 8 mayo | Viernes | Cita A2 | Manifesto | Cita de Carta #1 "Te escribo" |
| 11 mayo | Lunes | Carrusel A1 | Dependencia | "Necesitar validación no es vanidad: es un sistema interno" |
| 13 mayo | Miércoles | Reel + cover | Dependencia | Microclase 60s "Cómo aprendiste a buscarte en otros" |
| 15 mayo | Viernes | Cita A2 | Manifesto | Cita del libro Engranajes |
| 18 mayo | Lunes | Carrusel A1 | Burnout | "El cuerpo se recupera con horas, la psique se recupera con honestidad" |
| 20 mayo | Miércoles | Reel + cover | Burnout | Microclase 60s "Tu cansancio no es físico" (recicla del carrusel cansancio psíquico) |
| 22 mayo | Viernes | Cita A2 | Manifesto | Cita de Carta #2 "La voz que te juzga" |
| 25 mayo | Lunes | Carrusel A1 | Posicionamiento | Manifesto: "Esto NO es coaching, esto es leer la propia historia" |
| 27 mayo | Miércoles | Reel + cover | Posicionamiento | Microclase 60s "Por qué la psicología no es motivación" |
| 29 mayo | Viernes | Cita A2 | Cierre mes | Frase de Recalcati o de la propia obra |

12 publicaciones, 4 horas semanales de producción, sistema visual coherente desde el día 1.

---

## 12 · Checklist editorial pre-publicación

Imprimir, tener al lado del ordenador. Antes de pulsar "Compartir":

```
[ ] La pieza encaja en una de las 3 categorías (A carrusel, B reel, C cita).
[ ] Usa solo paleta de marca (#173D30, #265C4B, #C2A78B, #FDFCFA).
[ ] Tipografía es Barlow Condensed o Lora (cero Impact, cero Bebas).
[ ] Sin emojis en imagen ni en caption.
[ ] Sin frases motivacionales tipo "tú puedes", "mereces amor", "agradece".
[ ] Sin clickbait (banderas rojas, V0Yeur1sm0, signos de exclamación múltiples).
[ ] Sin familia visible (excepto Close Friends ⭐).
[ ] Si es reel, tiene cover branded subido (no frame default).
[ ] Firma "@daniorozcopsicologo · twimproject.com" presente en footer del slide (la marca "TWIM Project" se nombra en otras zonas del doc — el footer concreto de carrusel siempre es handle + URL).
[ ] Caption: 1 frase de hook + cuerpo + CTA opcional. Sin hashtags spam.
[ ] Ningún concepto importante queda solo en imagen — también en caption (accesibilidad + SEO interno).
[ ] Si la pieza viene de la newsletter o el libro, tiene atribución correcta.

Si alguna casilla no se marca → no se publica. Se revisa o se descarta.
```

---

## 13 · KPIs y métricas

> Revisar mensualmente. Las métricas semanales en Instagram son ruido.

### 13.1 · Métricas que importan

| Métrica | Hoy | Objetivo mes 3 | Objetivo mes 12 |
|---|---|---|---|
| Tasa de save por post (saves / impresiones) | desconocida | >2 % en carruseles A | >4 % |
| Tasa de share por post | desconocida | >1 % | >2 % |
| Conversión visitante perfil → click bio link | desconocida | >5 % | >10 % |
| Suscriptores netos a newsletter atribuibles a IG (vía UTM en bio link) | desconocida | +20/mes | +100/mes |
| % de contenido publicado en marca (capas A1/A2/Reel branded) | <30 % | >90 % | 100 % |

### 13.2 · Métricas que NO importan

- **Likes totales.** Vanidad. Un post con 1.000 likes y 0 saves vale menos que uno con 100 likes y 30 saves.
- **Followers totales.** Importa la calidad, no el número. 5.000 followers cualificados convierten más que 50.000 dispersos.
- **Reach individual de un reel.** Un reel viral aislado no construye marca. La consistencia sí.

### 13.3 · El test de los 5 segundos

Una vez al mes, abrir tu propio perfil en una ventana de incógnito (sin estar logueado). Mirar el grid 5 segundos. Hacer estas preguntas:

- ¿Qué entiende un desconocido sobre lo que ofrezco?
- ¿Lo asociaría con "psicólogo serio" o con "creador de contenido"?
- ¿Encajaría con el lector de Te escribo?

Si la respuesta a cualquiera de las tres es ambigua, el sistema no se está aplicando bien.

---

## 14 · Decisiones a cerrar este mes

- [ ] **Cortar publicación de cualquier pieza fuera del sistema** desde mañana 1 mayo.
- [ ] **Reorganizar pinned posts** con 3 carruseles del sistema A1/A2 esta semana.
- [ ] **Limpiar stories destacadas**: rediseñar portadas con un solo template (§8.2). Esta semana.
- [ ] **Crear plantillas A1, A2, Cover de reel y Cita visual** en Canva o Figma. 2 semanas.
- [ ] **Decidir herramienta de producción**: ¿Canva, Figma, ambas? Una sola. (Recomendado: Canva por velocidad y porque una asistente futura la maneja sin formación.)
- [ ] **Auditar grid completo** marcando capas A/B/C/D en una hoja simple. Junio.
- [ ] **Republicar 10-15 mejores piezas legado** re-maquetadas. Julio-Agosto.
- [ ] **Definir bio del perfil**: línea actualizada del estilo *"Daniel Orozco Abia · Psicólogo CV11515 · TWIM Project · The World Is Mind · Newsletter Te escribo · Libro Engranajes ↓"*.
- [ ] **Auditar grupo Close Friends** — limpiar lista, dejar solo amistad real.
- [ ] **Imprimir checklist editorial §12** y pegarla cerca del ordenador donde produces.

---

## Cierre

El feed actual de @daniorozcopsicologo tiene contenido valioso disperso entre tres etapas de marca y demasiado ruido (clickbait, reposts, mezcla de identidades). El problema no es que falte talento — los carruseles editoriales del sistema #1 lo demuestran. El problema es que **falta sistema** y el feed lleva años acumulando capas sin transición visible.

Aplicar este sistema hace dos cosas simultáneamente:

1. **Limpia el grid** para que el visitante nuevo entienda qué eres en 5 segundos.
2. **Reduce el coste cognitivo de producir contenido** — 3 categorías, 2 paletas, 1 tipografía, 1 plantilla por categoría. Esto te libera tiempo para escribir, que es lo único que solo tú puedes hacer.

A 12 meses, el feed debería ser indistinguible — en limpieza, no en estilo — del de un autor referencial del nicho clínico-editorial. Esa distancia es lo que separa una cuenta personal de psicólogo de una marca editorial.

— Notas técnicas: documento generado el 30-04-2026. Specs de plantillas (§3.4 y §7.1) son aproximaciones de partida — al diseñador real conviene darle libertad de ajustar pesos y tamaños manteniendo paleta y tipografía. Cuando contrates asistente, este documento es lo primero que debe leer (junto con CLAUDE.md y el doc CEO).
