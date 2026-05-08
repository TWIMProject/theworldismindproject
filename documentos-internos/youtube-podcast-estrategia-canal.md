# YouTube + Podcast · Estrategia de canal TWIM

> Documento interno · 4 mayo 2026
> Doc #3 de la serie de stack de producción audio + vídeo.
> Complementa: anexo CEO stack audio+vídeo (doc #1), ElevenLabs clonación de voz (doc #2), NotebookLM infraestructura (doc #4 pendiente), reciclaje pipeline (doc #5 pendiente).
> Decisiones cocidas en sesión 30-abr-2026 + ajuste 4-may-2026 (opción B grabación humana en T1).

---

## TL;DR

- **Canal:** YouTube `@daniorozcopsicologo` con 10,1K suscriptores. Dos podcasts ya vivos: TWIM Podcast (4 episodios) y Los Invitados (15 episodios), ambos también en Spotify.
- **Posicionamiento:** Daniel-clínico que produce contenido editorial, no Daniel-influencer. Sin clickbait, sin frases motivacionales, sin promesas de transformación. La voz del libro y de los artículos llevada a audio.
- **Cadencia mayo-agosto 2026:** 1 episodio cada 2 semanas. **Grabación humana de Daniel leyendo guion** (decisión 4-may, opción B). ElevenLabs queda configurado en paralelo como palanca de escalado para cuando se suba a 1/semana en septiembre o cuando un episodio concreto no admita grabación humana.
- **Reciclaje:** cada episodio alimenta 7 piezas (vídeo YouTube, audio Spotify, 3-5 Shorts, carrusel IG, cita visual, fragmento newsletter, post LinkedIn). Detalle en doc #5.
- **Distribución gratuita derivados:** Meta Business Suite para IG + FB; Metricool a evaluar más adelante si hace falta agregación multi-canal.
- **Monetización YouTube:** ya cumplido umbral de Partner Program. Estimación honesta de AdSense a 12 meses: 100-400 €/mes en ritmo sostenido. Es ingreso pasivo creciente, no negocio.
- **Disclosure obligatorio** cuando entre ElevenLabs (texto base en doc #2 §4). Mientras la fase sea humana, no aplica disclosure de IA.
- **Política dura:** nunca material clínico de pacientes ni en NotebookLM ni en guion del podcast (ver doc #4).

---

## 1 · Estado actual del canal

A 4 de mayo de 2026, los activos audio + vídeo de TWIM son:

| Activo | Volumen | Estado | Plataforma |
|---|---|---|---|
| Canal YouTube `@daniorozcopsicologo` | 10.100 subs | Vivo, monetización elegible | YouTube |
| TWIM Podcast · Psicología Aplicada | 4 episodios | Vivo, baja cadencia hasta hoy | YouTube + Spotify |
| Los Invitados · TWIM Podcast | 15 episodios | Vivo, formato entrevistas | YouTube + Spotify |
| Cover de podcast unificado | Sí, alineado al sistema visual del PR #94 | Listo para producción | n/a |
| Cuenta ElevenLabs Creator | Pendiente de contratar | Setup tras decisión opción B | ElevenLabs |
| Modelo voz clonada Daniel | No entrenado todavía | Diferido a fase 2 (sept+) | ElevenLabs |
| NotebookLM | Disponible, sin notebooks específicos por pilar todavía | Setup pendiente (doc #4) | Google |

Lo que esto implica:

- **El canal ya pasa el umbral de Partner Program** (1.000 subs + 4.000 h watch o 10M Shorts views). Falta confirmar las 4.000 h y solicitar monetización.
- **Hay tracción algorítmica acumulada.** Un canal con 10K subs no es un canal "desde cero". El coste/oportunidad de producir es mucho menor que el de un creador empezando.
- **Hay dos formatos vivos a la vez** (TWIM Podcast monólogo + Los Invitados entrevistas). Esto es bueno editorialmente pero exige separar líneas para que la audiencia entienda qué consume. Detalle en §3.
- **El cuello de botella hoy no es plataforma ni equipo, es ritmo de publicación.** 4 episodios de TWIM Podcast en lo que va de proyecto es bajo. Subir a 1 cada 2 semanas mayo-agosto es el cambio operativo principal.

---

## 2 · Posicionamiento — Daniel-clínico, no Daniel-influencer

Misma regla que el doc CEO §2 y que el sistema visual de IG (PR #94). El canal de YouTube + el podcast **no se reposicionan** para optimizar tasa de clic. Mantienen tono editorial.

Lo que sí se hace:

- Títulos descriptivos del mecanismo psíquico que se va a explicar.
- Descripciones que citan el material original (artículo del repo, capítulo del libro, briefing de programa).
- Thumbnails con sistema visual TWIM — paleta verde oscuro `#173D30`, verde medio `#265C4B`, beige `#C2A78B`, fondo `#FDFCFA`, fuente Barlow Condensed.
- Bio de canal que deja claro que Daniel es psicólogo general sanitario CV11515, no creador de contenido.

Lo que NO se hace:

- **Títulos clickbait** tipo *"Lo que NUNCA te dirá tu pareja"*, *"5 señales de que eres tóxica"*, *"Cómo dejar de sufrir en 30 días"*. Esto rompe la promesa del producto.
- **Thumbnails con caras gritando**, flechas rojas, círculos amarillos, reacciones exageradas. Es el código visual de la creación de contenido masiva, no de TWIM.
- **Frases motivacionales** ni positivismo tóxico. La identidad editorial (CLAUDE.md) lo prohíbe explícitamente.
- **Promesas de transformación rápida.** No "te cambiaré la vida en 5 minutos". Sí "vamos a describir cómo funciona X mecanismo".
- **Reaccionar a otros creadores** (debate, dueto, "respondiendo a..."). No es el formato de TWIM.

El criterio de decisión cuando aparezca duda sobre un título o thumbnail es: *¿esto cabe en la voz del libro Los engranajes de la mente?* Si no cabe, fuera.

---

## 3 · TWIM Podcast vs Los Invitados — diferenciación

Los dos formatos comparten marca y canal pero apuntan a usos distintos. Que la audiencia lo entienda evita canibalización y mejora retención por playlist.

| Eje | TWIM Podcast · Psicología Aplicada | Los Invitados |
|---|---|---|
| Formato | Monólogo editorial de Daniel | Conversación con un invitado |
| Voz | Solo Daniel (humana T1, ElevenLabs T2) | Daniel + invitado, ambos humanos |
| Duración objetivo | 15-30 min | 45-90 min |
| Audiencia primaria | Mujeres adultas 25-50 con autoexigencia, dependencia, burnout, ansiedad | Mixta, lectores del libro y profesionales del entorno |
| Objetivo editorial | Describir un mecanismo psíquico concreto por episodio | Conversar sobre un cruce temático con alguien que aporta otra mirada |
| Relación con embudo TWIM | Alimenta directamente programas digitales (autoexigencia, dependencia, burnout) | Construye autoridad de marca y red profesional |
| Cadencia objetivo | 1 cada 2 semanas mayo-agosto, 1/semana desde sept | Sin cadencia fija, oportunista cuando hay invitado relevante |
| Reciclaje cruzado | Sí, plenamente — origen del pipeline 1→7 (doc #5) | Parcial — Shorts y citas, pero no necesariamente carrusel ni newsletter |
| Producción | NotebookLM + guion + voz Daniel humana o ElevenLabs | Grabación humana directa, edición clásica |

Decisión editorial:

- **Cuando hay duda de formato, gana TWIM Podcast.** Los Invitados se reserva para cuando el invitado aporta valor genuino (no relleno).
- **No mezclar dentro del mismo episodio.** Si Daniel quiere comentar una entrevista, lo hace en un episodio aparte de TWIM Podcast referenciando el episodio de Los Invitados.
- **Playlists separadas en YouTube.** Una para TWIM Podcast, otra para Los Invitados. La gente que viene por monólogo no quiere encontrarse con entrevistas, y al revés.

---

## 4 · Pilares temáticos

Mismos cuatro racimos que el doc CEO §3.1 y que el calendario de IG (PR #94 §11.3). El canal no abre temas nuevos: **profundiza los que ya existen** en artículos, libro y briefings de programa.

### 4.1 · Pilar autoexigencia

- **Núcleo:** mandato interno, ideal yoico hipertrofiado, imposibilidad de descansar sin culpa.
- **Material editorial disponible:** artículos del repo (`reto-7-dias.html`, `dejadeobligarte.html`), carrusel autoexigencia, carta #2 newsletter.
- **Tipo de episodio:** descripción de mecanismos (introyección del mandato, transferencia parental al trabajo). Lectura de fragmentos del libro.

### 4.2 · Pilar dependencia emocional

- **Núcleo:** elección de objeto de pareja como repetición, espera, asimetría.
- **Material editorial disponible:** `dejadebuscarteenotros.html`, briefing del programa Deja de Buscarte en Otros.
- **Tipo de episodio:** lectura del briefing del programa con comentario clínico, casos compuestos (no pacientes reales) que ilustran patrones.

### 4.3 · Pilar burnout y ansiedad

- **Núcleo:** agotamiento psíquico crónico, somatización, pérdida de deseo, ansiedad estructural.
- **Material editorial disponible:** `psicologo-burnout-valencia.html`, `psicologo-ansiedad-valencia/`, `nopuedoparar-taller.html`, carrusel cansancio psíquico, "Te escribo" carta #1.
- **Tipo de episodio:** distinción entre cansancio y burnout, lectura de la carta "Te escribo cuando no puedes parar", marcos clínicos sobre ansiedad.

### 4.4 · Pilar adolescencia

- **Núcleo:** angustia adolescente, conflictos familiares, formación del yo en la era de redes.
- **Material editorial disponible:** `psicologo-adolescentes-valencia.html`, `PLAN-TALLERES-ADOLESCENCIA.md`, briefings de talleres.
- **Tipo de episodio:** dirigido a padres y a profesionales que trabajan con adolescentes. Marco clínico, no manuales de "qué hacer con tu hijo".

### 4.5 · Rotación entre pilares

- **Mayo-agosto (8 episodios planificados):** 2 por pilar, alternando para que ningún pilar quede más de 2 publicaciones sin tocar.
- **Septiembre+ (cadencia semanal):** misma rotación, comprimida.
- **Excepciones puntuales:** lanzamiento de un programa nuevo o de un taller justifica concentrar 2-3 episodios consecutivos en su pilar. Eso pasa, por ejemplo, en torno al lanzamiento de talleres de adolescencia o del programa Deja de Buscarte en Otros.

---

## 5 · Calendario editorial — fase 1 humana, fase 2 ElevenLabs

### 5.1 · Decisión cocida 4-may-2026 (opción B)

El doc #2 (ElevenLabs) describía un workflow basado en voz clonada. La decisión revisada por Daniel el 4-may-2026 desdobla la implementación en dos fases:

| Fase | Periodo | Cadencia | Voz | Justificación |
|---|---|---|---|---|
| **T1 humana** | Mayo-agosto 2026 | 1 episodio cada 2 semanas | Daniel graba leyendo guion preparado | Cadencia compatible con grabación humana. No requiere disclosure de IA. Perfecciona el guion editorial antes de pasar a clonación. |
| **T2 ElevenLabs** | Septiembre 2026+ | 1 episodio/semana | Voz Daniel clonada (con disclosure) | Cadencia semanal incompatible con grabación humana sostenida. ElevenLabs entra como palanca de escalado. |

**Por qué se graba humano en T1 aunque ElevenLabs ya esté disponible:**

- A 1 cada 2 semanas, grabar leyendo guion **es viable** sin que se note que se está leyendo (Daniel no aparece en cámara, sale cover estático + waveform).
- Da margen para refinar el formato del guion (longitud, transiciones, ritmo) antes de pasar a clonación, donde corregir errores tiene más fricción.
- Evita activar el disclosure de IA antes de tiempo, lo que mantiene la promesa "voz humana real" durante T1.
- Permite acumular 30-60 min de audio editorial reciente con el formato definitivo del podcast — material directamente reutilizable como fuente de entrenamiento del modelo ElevenLabs en septiembre.

**Cuándo ElevenLabs se adelanta a T2:**

- Si Daniel está enfermo o de viaje y no puede grabar.
- Si un episodio requiere lectura larga de fragmentos del libro y la voz humana se cansa.
- Si llega una semana en T1 sin slot para grabar.

En todos esos casos, el episodio sale con disclosure de IA igualmente (el disclosure no es ocasional, es por episodio).

### 5.2 · Calendario mayo-agosto 2026 (T1)

8 episodios de TWIM Podcast en 4 meses, alternando pilares.

| Semana | Episodio | Pilar | Material editorial base |
|---|---|---|---|
| 12-18 mayo | E5 | Autoexigencia | Carrusel autoexigencia + carta #2 |
| 26 may-1 jun | E6 | Dependencia emocional | Briefing programa Deja de Buscarte en Otros |
| 9-15 junio | E7 | Burnout / ansiedad | Carta "Te escribo cuando no puedes parar" |
| 23-29 junio | E8 | Adolescencia | Plan talleres adolescencia |
| 7-13 julio | E9 | Autoexigencia | Lectura fragmento Los engranajes (capítulo a definir) |
| 21-27 julio | E10 | Dependencia emocional | Casos compuestos (no pacientes reales) |
| 4-10 agosto | E11 | Burnout / ansiedad | Mecanismo de la somatización |
| 18-24 agosto | E12 | Adolescencia | Marco clínico para profesionales que trabajan con adolescentes |

Las fechas son ventana, no día fijo. Día concreto de publicación se cierra al inicio de cada mes.

### 5.3 · Alineación con calendario IG (PR #94 §11.3)

Los pilares del podcast siguen el mismo orden de rotación que el calendario de IG. Cuando un episodio sale, las piezas derivadas (carrusel, cita, Reels) **se incrustan en el calendario IG sustituyendo lo que tocaba esa semana**, no se añaden encima. Esto es lo que hace que el reciclaje no genere saturación. Detalle en doc #5.

### 5.4 · Cadencia Los Invitados

Los Invitados sigue ritmo oportunista, no calendarizado:

- 1 episodio/mes como máximo.
- Solo cuando hay un invitado con cruce temático real con un pilar TWIM.
- No se fuerzan invitados para "rellenar".
- Los episodios pendientes en cola se publican distribuidos para que ningún mes quede vacío.

---

## 6 · Reciclaje cruzado — el episodio como hub

El detalle operativo va en doc #5 (`reciclaje-contenido-pipeline.md`). Aquí solo el principio aplicado al canal:

- **El episodio no es el destino, es el origen.** Un episodio de 20 min se produce una vez y luego alimenta IG, newsletter, LinkedIn y Shorts durante una semana. Si se trata como pieza única de YouTube, se desperdicia.
- **El cover unificado** (ya alineado al sistema visual TWIM) sirve también como base visual de las piezas derivadas. Esto da consistencia gratis: la audiencia reconoce de qué episodio viene cada Short, cada carrusel, cada cita.
- **La distribución programada de los derivados va por Meta Business Suite** (gratis, nativo Meta) para IG + FB durante T1. Si el volumen exige agregación con LinkedIn, X o YouTube Shorts en una sola consola, **se evalúa Metricool** más adelante. Hoy no es necesario.
- **El episodio en YouTube y Spotify se publica primero**, y los derivados salen en los días posteriores siguiendo el calendario IG. Esto evita spoilear el contenido principal con un Short del mismo día.

---

## 7 · Monetización YouTube — umbrales y proyección

### 7.1 · Estado de elegibilidad

YouTube Partner Program (YPP) requiere:

- 1.000 suscriptores (cumplido: 10.100).
- 4.000 horas de visionado público válidas en los últimos 12 meses **o** 10M Shorts views en los últimos 90 días.
- Cuenta sin strikes activos por copyright o monetización.
- AdSense vinculado con titular fiscal correcto.

Acción inmediata:

1. Confirmar en YouTube Studio si las 4.000 h de los últimos 12 meses están cumplidas. Si no, calcular cuánto falta y plan de Shorts derivados para acelerar.
2. Solicitar entrada a YPP en cuanto esté el umbral confirmado.
3. Validar que la cuenta de AdSense tiene los datos fiscales correctos (autónomo o sociedad de Daniel, según se cierre tema gestor).

### 7.2 · Estimación honesta de ingresos AdSense

Datos del nicho psicología España al 2026, conservadores:

- RPM (revenue per mille) en España, nicho psicología, formato podcast en YouTube: 1,5-3 €/1.000 views válidas.
- Shorts: RPM mucho más bajo (0,03-0,10 €/1.000 views) — los Shorts no son la fuente de ingresos directa, son captación.
- Conversión views → suscripción: 0,5-2 % en canales con tracción consolidada.

| Hito | Subs | Views/mes estimadas | RPM medio | AdSense/mes estimado |
|---|---|---|---|---|
| Hoy (10K) | 10.100 | 30.000-60.000 (mixto vídeo + Shorts) | 1,2 € | 35-70 € |
| Mes 6 | 14.000 | 80.000-150.000 | 1,5 € | 120-225 € |
| Mes 12 | 25.000-40.000 | 200.000-400.000 | 1,8 € | 360-720 € |

**Cifras de la fila "mes 12" optimistas pero alcanzables si la cadencia 1/semana se sostiene desde septiembre.** Para mantener honestidad: si solo se sostiene 1 cada 2 semanas todo el año, el rango realista para mes 12 baja a 100-300 €/mes.

### 7.3 · Otras vías de monetización del canal

| Vía | Activable cuándo | Estimación |
|---|---|---|
| AdSense (vídeos largos + Shorts) | Inmediato tras YPP aprobado | Ver §7.2 |
| Super Thanks (donaciones de 1 vídeo) | Tras YPP aprobado | 0-50 €/mes — anecdótico, no relevante |
| Members del canal (suscripción de pago) | A 25K subs y con criterio editorial claro | Diferido a 2027 |
| Patrocinios directos | A 25K subs + episodio promedio >3K views | 100-500 €/mención, diferido |
| Tráfico al embudo TWIM (libro, programas, newsletter) | Inmediato | **Esto es lo más valioso** y no se mide en AdSense — se mide en altas a newsletter y leads a programas |

La regla: **el canal monetiza directamente lo que puede (AdSense), pero su mayor valor sigue siendo alimentar el embudo TWIM**. No optimizar el contenido para maximizar AdSense si eso erosiona la conversión a newsletter.

---

## 8 · SEO de YouTube — títulos, descripciones, tags, thumbnails

### 8.1 · Títulos

- **Patrón base:** `{tema descriptivo} | TWIM Podcast E{n}`
- Ejemplo válido: `El mandato de no parar — autoexigencia y culpa de descansar | TWIM Podcast E5`
- Ejemplo inválido: `5 SEÑALES de que NO PUEDES PARAR (te va a sorprender) 😱`
- Longitud objetivo: 55-65 caracteres antes del separador `|`. YouTube corta visualmente sobre 70.
- Palabras clave naturales del pilar (autoexigencia, dependencia emocional, burnout, ansiedad, adolescencia) integradas sin forzar. Misma lógica que el SEO de las landings (`SEO_ANALISIS_2026-03-20.md`).

### 8.2 · Descripciones

Estructura fija:

```
[Resumen editorial 2-3 párrafos describiendo el mecanismo del episodio]

— Material original referenciado en este episodio:
· Artículo: [link al artículo del repo]
· Capítulo del libro Los engranajes de la mente: [referencia]
· Carta "Te escribo": [link si aplica]

— Recursos:
· Suscríbete a "Te escribo": https://twimproject.com/newsletter
· Web de la consulta: https://twimproject.com
· Programa relacionado: [link cuando aplique]

— Sobre TWIM:
Daniel Orozco Abia · Psicólogo General Sanitario CV11515 · Valencia.
TWIM Podcast es contenido editorial sobre psicología aplicada, sin coaching, sin promesas, sin clickbait.

[Cuando aplique fase 2: bloque de disclosure ElevenLabs según doc #2 §4.2]

#TWIMPodcast #PsicologíaAplicada #DanielOrozcoAbia #{pilar}
```

### 8.3 · Tags

- 5-10 tags por vídeo, mezclando:
  - Tag de marca: `TWIM Podcast`, `Daniel Orozco Abia`, `psicología aplicada`.
  - Tag de pilar: `autoexigencia`, `dependencia emocional`, `burnout`, `adolescencia`.
  - Tag de búsqueda larga: `por qué no puedo parar de trabajar`, `dependencia emocional pareja`, `psicólogo Valencia`, etc.
- Tags ya no pesan tanto en YouTube como en 2018, pero siguen ayudando para aparición en sugeridos. No obsesionarse.

### 8.4 · Thumbnails

- **Sistema visual TWIM** (paleta + fuente Barlow Condensed).
- Plantilla recomendada: cover del episodio + título corto (3-5 palabras) sobreimpreso en beige `#C2A78B` sobre fondo verde oscuro `#173D30`.
- Sin foto de Daniel reaccionando.
- Sin emojis, sin flechas, sin tachones.
- Versión móvil legible: probar el thumbnail al 30% del tamaño antes de subir. Si el título no se lee, reescribir más corto.

### 8.5 · Capítulos

- Activar capítulos en cada episodio. Marcas de tiempo en la descripción con formato `00:00 Introducción`, `02:30 Tema 1`, etc.
- 4-7 capítulos por episodio. Más es ruido, menos no aprovecha la función.
- Beneficio doble: SEO interno de YouTube + retención (los espectadores saltan en lugar de abandonar).

### 8.6 · Playlists

- Una playlist por pilar (autoexigencia, dependencia, burnout, adolescencia) que mezcla TWIM Podcast + Los Invitados + vídeos antiguos del canal cuando aplique.
- Una playlist `TWIM Podcast · Psicología Aplicada` con todos los episodios del formato monólogo.
- Una playlist `Los Invitados` con todas las entrevistas.
- Las playlists son la herramienta de SEO interno más infravalorada de YouTube. Mejoran watch time y posicionan en sugeridos.

---

## 9 · Shorts derivados — política, formato, cadencia

### 9.1 · Política

- **3-5 Shorts por episodio.** No más, no menos. 3 es mínimo viable para alimentar IG Reels + YouTube Shorts; 5 es máximo antes de canibalizar el episodio largo.
- **Cada Short es un mecanismo psíquico contenido en sí mismo**, no un teaser que diga "ve a YouTube para ver el episodio completo". El espectador de Shorts no salta a long-form en la mayoría de los casos; tratar cada Short como pieza autónoma que aporta valor por sí sola.
- **Reciclaje cruzado:** el mismo Short se publica como YouTube Short, IG Reel y, si aplica, TikTok (cuando se decida abrir TikTok según anexo CEO §5).

### 9.2 · Formato

| Atributo | Valor |
|---|---|
| Duración | 30-60 s. 45 s es el punto óptimo. |
| Aspect ratio | 9:16 vertical |
| Subtítulos | Obligatorios, quemados sobre el vídeo (no como CC opcional). Mayoría del consumo es sin sonido. |
| Cover frame | Frame inicial con título visible 1-2 s antes de que arranque el audio |
| Audio | Voz Daniel (humana T1, ElevenLabs T2 con disclosure) sin música de fondo o con música muy suave |
| Cierre | Frase de cierre con la mano editorial TWIM, sin CTA del tipo "sígueme" |
| Hashtags | 3-5 por Short, mezclando pilar + marca |

### 9.3 · Cadencia

- **3-5 Shorts por episodio**, distribuidos en los 5-7 días posteriores a la publicación del episodio largo.
- En T1 (1 cada 2 semanas), eso son 6-10 Shorts/mes. Cubre la cadencia de Reels recomendada por el sistema visual de IG (PR #94 §11.3) sin necesidad de producir Reels desde cero.
- En T2 (1/semana), 12-20 Shorts/mes. Aquí ya hay riesgo de saturar el feed de un mismo seguidor; conviene espaciar publicación entre canales (un Short en YouTube hoy, mismo Short en IG Reel +3 días).

### 9.4 · Lo que un Short de TWIM no hace

- No empieza con "Hola, soy Daniel".
- No termina con "dale like y suscríbete".
- No usa el código visual de Shorts genéricos (zoom dramático, palabras parpadeando, transiciones bruscas).
- No reacciona a tendencias virales.
- No promete transformación ni resuelve un problema en 30 segundos.

Lo que sí hace: describe un mecanismo psíquico en lenguaje claro, con voz editorial, en tiempo corto. La diferencia con un Short genérico es la misma que entre un párrafo del libro y un meme: ambos pueden ser cortos; solo uno es TWIM.

---

## 10 · KPIs del canal

Mismo bloque base que el anexo CEO §6, ampliado con métricas operativas del propio canal.

### 10.1 · KPIs de crecimiento (revisión mensual)

| Métrica | Hoy | Mes 6 | Mes 12 |
|---|---|---|---|
| Suscriptores YouTube | 10.100 | 14.000 | 25.000-40.000 |
| Episodios totales TWIM Podcast | 4 | 12-15 | 26-30 |
| Episodios totales Los Invitados | 15 | 18-22 | 24-30 |
| Watch time medio por vídeo | desconocido | >40 % retención | >50 % |
| Ingresos AdSense YouTube/mes | 0 (YPP no activado) | 120-225 € | 360-720 € |
| Conversión YouTube → newsletter | desconocida | >2 % | >5 % |
| Shorts >50K views/mes | 0 | 1 | 2-3 |

### 10.2 · KPIs operativos (revisión semanal mientras se asienta el ritmo)

| Métrica | Umbral mínimo | Acción si no se cumple |
|---|---|---|
| Tiempo de producción por episodio | < 4 h Daniel en T1, < 2 h en T2 | Revisar guion, plantilla, herramienta |
| Cumplimiento de fecha planificada (8 episodios mayo-agosto) | 100 % | Si se salta uno, mover el siguiente; si se saltan dos, revisar viabilidad de la cadencia |
| Shorts derivados publicados por episodio | ≥ 3 | Si bajan a 1-2, revisar pipeline en doc #5 |
| Distribución cruzada en IG (carrusel + cita + Reels) por episodio | ≥ 2 piezas IG por episodio | Reasignar al calendario de IG según PR #94 |

### 10.3 · Lo que NO se mide como KPI principal

- **Likes y comentarios** del vídeo. Indicadores secundarios, sí, pero no objetivo.
- **Velocidad de crecimiento de suscriptores día a día.** Volátil, no aporta señal de gestión.
- **Compararse con creadores del mismo nicho.** Son canales con propuestas distintas. Compararse es ruido.

El criterio único de éxito del canal es: **¿está alimentando el embudo TWIM (newsletter + libro + programas) de forma sostenida?** Si la respuesta es sí, el canal funciona, independientemente de la velocidad bruta de subs.

---

## 11 · Riesgos y mitigación

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Cambio de algoritmo YouTube que penalice Shorts derivados o vídeos con audio TTS | Media a 18 meses | Medio | Diversificar formato (algunos Shorts grabados humano, no todos derivados). Mantener parte de la audiencia sobre newsletter, no sobre canal. |
| Demonetización por contenido AI sin disclosure | Baja con disclosure correcto, alta sin él | Alto | Disclosure desde el primer episodio T2 (doc #2 §4). Etiqueta "AI-generated content" en metadata YouTube. |
| Caída de cadencia (saltarse episodios planificados) | Alta los 2 primeros meses | Medio | Tener 1-2 episodios de buffer producidos por adelantado. Si se cae el ritmo dos meses seguidos, bajar a 1/mes formalmente antes que improvisar. |
| Saturación cruzada IG + YouTube + newsletter | Media | Medio | Coordinar calendarios (doc #5). El derivado sustituye al original en cada canal, no se acumula. |
| Daniel-clínico erosionado por presión del algoritmo a hacer clickbait | Media en mes 2-6 | Alto | Revisión editorial mensual: ¿este título cabe en la voz del libro? Si no, fuera. |
| Pérdida del activo "voz Daniel" si ElevenLabs sube precios o cambia ToS | Media a 24 meses | Alto cuando entre T2 | Backup audio fuente (doc #2 §5). Evaluar Resemble.ai o alternativa cada 12 meses. |
| Comentarios tóxicos o trolls en vídeos sobre dependencia o adolescencia | Alta | Bajo si hay política de moderación | Configurar moderación automática + palabras prohibidas. Bloqueo manual rápido. No responder a trolls. |
| Filtración de material clínico de pacientes a NotebookLM o ElevenLabs | Muy baja con la política, alta sin ella | Catastrófico (deontológico + legal) | Política dura: NUNCA pacientes en NotebookLM ni ElevenLabs. Doc #4 desarrolla el protocolo. |
| Plagio de fragmentos del libro o artículos por terceros que recortan Shorts y los republican | Media | Bajo | Marca de agua sutil en thumbnails Shorts. Estrategia de no perseguir judicialmente, sí reportar a YouTube/IG vía herramientas de copyright. |
| Cambio de proveedor de hosting de podcast (Spotify for Podcasters, Buzzsprout, etc.) | Media a 24 meses | Bajo | Mantener archivos MP3 originales en almacenamiento propio. La migración entre hosts es trivial si los archivos están a mano. |

---

## 12 · Decisiones a cerrar este mes

- [ ] **Confirmar elegibilidad YPP** en YouTube Studio (4.000 h watch acumuladas).
- [ ] **Solicitar entrada a YouTube Partner Program** y vinculación AdSense con datos fiscales correctos (esperar a cierre de tema gestor si afecta).
- [ ] **Cerrar slot de grabación humano semanal** en agenda Daniel (bloque de 90 min reservado para grabar guion del próximo episodio).
- [ ] **Definir intro + outro de marca** del podcast (jingle + frase de bienvenida + bloque de disclosure cuando entre T2).
- [ ] **Configurar moderación automática** del canal con palabras prohibidas y bloqueo automático de comentarios con enlaces.
- [ ] **Crear playlists** por pilar (autoexigencia, dependencia, burnout, adolescencia) y por formato (TWIM Podcast, Los Invitados).
- [ ] **Plantilla de descripción** del episodio en formato fijo (§8.2) guardada como bloque reutilizable.
- [ ] **Plantilla de thumbnail** en Canva o herramienta equivalente, alineada al sistema visual TWIM.
- [ ] **Cuenta Meta Business Suite** lista para programar derivados de IG + FB. Revisar permisos de la página de FB y validar que el calendario de IG del PR #94 se puede importar/programar desde ahí.
- [ ] **Producir y publicar E5** (autoexigencia, ventana 12-18 mayo) como episodio piloto del nuevo formato T1.
- [ ] **Revisar el episodio piloto** con dos lectores beta (uno cercano, uno externo) antes de publicar el siguiente para ajustar duración, ritmo y estructura.
- [ ] **Setup ElevenLabs Creator** en paralelo (no urgente, pero conviene tener el modelo entrenado en julio para poder activarlo en septiembre sin fricción). Tareas operativas en doc #2 §10.

---

## 13 · Apéndice 8 mayo 2026 · Formato vídeo-ensayo con b-roll editado

> Decisión cerrada con Daniel el 8 mayo 2026. No reescribe el plan principal: lo extiende con una variante de formato visual para los episodios de TWIM Podcast monólogo.

### 13.1 · Decisión

A partir del E5 (o del primer episodio donde sea operativamente posible), TWIM Podcast monólogo adopta el formato **vídeo-ensayo**: voz en off de Daniel sobre secuencias visuales construidas (Daniel en consulta leyendo, eligiendo un libro, recolocando objetos, escribiendo, de pie pensativo, etc.). El **talking head desaparece como recurso central**: aparece como mucho en cabecera o cierre breve, no como columna del episodio.

El referente visual no es un canal de psicología hablada. Es el registro de **The School of Life**, **Like Stories of Old** o un Lex Fridman cuando edita ensayo: composición de plano cuidada, b-roll editorial, voz en off como conductor.

### 13.2 · Por qué encaja con el plan existente

- Duración objetivo TWIM Podcast monólogo (§3): **15-30 min**. La propuesta de 15 min cae dentro del rango.
- Voz humana en T1 (§5 + §6 decisión 4-may opción B): la voz en off de Daniel cumple con T1 sin reescribir nada.
- Posicionamiento Daniel-clínico (§2): el b-roll de consulta refuerza el registro clínico **mejor** que un talking head genérico, que es indistinguible de cualquier creator de psicología.
- Reciclaje (§9 + doc #5): el b-roll genera material casi gratuito para Shorts (cualquier corte de 8 s sobre frase corta funciona como pieza autónoma).

### 13.3 · Reglas duras del formato

1. **Cada toma compuesta, no improvisada.** Encuadre pensado, iluminación pensada, sin cámara temblona ni zoom dramático. Si una toma no tendría sentido en un libro de fotografía editorial, fuera.
2. **El guion sigue siendo la pieza central.** El b-roll es soporte, nunca protagonista. Si la voz en off cae 30 segundos sin frase, el b-roll no rescata el episodio.
3. **El 70 % o más del tiempo de producción debe ir al guion.** Si Daniel se descubre dedicando más tiempo a editar plano que a pulir frase, hay que parar y revisar.
4. **Vídeo-ensayo ≠ vlog.** Nunca «autenticidad casual», nunca cámara en mano improvisando, nunca «detrás de las cámaras de mi día». Eso desliza a registro influencer y rompe la promesa.

### 13.4 · Sesión única de b-roll genérico (ahorro de cadencia)

Filmar nuevo b-roll cada episodio a ritmo de uno cada dos semanas no es sostenible. Solución acordada:

- **Una sesión única de 2-3 horas** que produce **30-50 clips reutilizables**. Esa librería cubre **5-10 episodios** sin volver a filmar.
- Cada toma debe filmarse durante **15-20 s mínimo** para permitir cortes y loops en edición.
- Reposición: cuando la librería se haya usado en más del 70 % en episodios publicados, agendar nueva sesión.

#### Tipologías mínimas a cubrir en la sesión

| Tipología | Variantes a registrar |
|---|---|
| Daniel sentado leyendo un libro | 2-3 libros distintos, 2-3 ángulos por libro |
| Daniel eligiendo un libro de la estantería | Frontal y perfil, mano alcanzando estante |
| Daniel recolocando objetos / libros | Movimiento lento, distintos rincones de la consulta |
| Daniel de pie pensativo | Junto a ventana mirando fuera, en el centro de la consulta, apoyado en estante |
| Daniel escribiendo a mano | Cuaderno abierto, primer plano y plano medio |
| Daniel escribiendo en ordenador | De espaldas, perfil, detalle de teclado |
| Detalle de manos | Pasando páginas, escribiendo, sosteniendo gafas |
| Detalle de objetos | Gafas sobre libro abierto, cuaderno, pluma, taza |
| Plano general de la consulta vacía | Distintas horas, distintas luces |
| Plano de luz / textura / sombras | Sin Daniel, para usar como respiro entre frases |
| Caminar por la consulta | Paso lento, paso pensativo, atravesando habitación |

Equipo: la cámara que Daniel ya use + luz natural cuando sea posible. **No comprar equipo nuevo** para esto. Si en la sesión de rodaje aparece una limitación recurrente, evaluarla en un anexo posterior y no en caliente.

### 13.5 · B-roll específico por episodio

Si el tema del episodio pide una toma concreta (p. ej. un libro citado, un objeto que aparece como ejemplo en el guion), filmar **1-2 tomas dedicadas** durante la propia sesión de grabación de voz. **Tope:** 30 minutos de rodaje específico por episodio. Más que eso rompe la cadencia.

### 13.6 · Workflow integrado (encaja con doc #5 §3.1)

Orden de producción por episodio:

1. **Guion editorial** (~3.000-3.500 palabras = ~15 min de voz en off). Vive en `contenido-rrss/podcast-eN-tema/guion.md`.
2. **Grabación voz en off limpia.** Audio sin música ni ambiente, en bloque cerrado de 90 min ya reservado en agenda Daniel (§12).
3. **Edición visual.** Montar b-roll de la librería sobre la voz, añadir 1-2 tomas específicas si aplica, intercalar plano de respiro entre bloques temáticos. Sin transiciones bruscas.
4. **Master final.** 4-7 capítulos (§8.5), thumbnail según sistema visual TWIM (§8.4), descripción según plantilla (§8.2).

Tiempo total estimado por episodio (revisar contra cronómetro real en doc `cronometraje-episodio-piloto-e5.md`): **5-7 h Daniel** en T1, igual que la estimación previa del workflow §3.1 del doc #5. La edición visual añade tiempo, pero la sesión única de b-roll evita filmar cada vez, así que el balance neto se mantiene.

### 13.7 · Ubicación canónica de los guiones (acceso operativo)

Para que «necesito el guion del episodio X» sea siempre una operación trivial:

- Cada episodio tiene su propia carpeta: **`contenido-rrss/podcast-eN-tema/`** (patrón ya establecido por E5: `contenido-rrss/podcast-e5-autoexigencia/`).
- El guion vive en: **`contenido-rrss/podcast-eN-tema/guion.md`**.
- Junto al guion, en la misma carpeta, viven: thumbnail/cover del episodio, caption de YouTube, caption de Spotify, specs y portada.
- Cuando se planifique un episodio nuevo, **el primer paso del workflow es crear esa carpeta + un `guion.md` vacío con la plantilla del repo**. Sin esa carpeta no hay episodio; con ella, todas las piezas (guion, captions, portadas, derivados) van al mismo sitio.

### 13.8 · Tradeoffs aceptados

| Tradeoff | Aceptado porque |
|---|---|
| Producción más compleja por episodio frente a talking head | Daniel disfruta editar — energía sostenible. El upgrade visual diferencia frente a competencia genérica. |
| Riesgo de saturación visual (siempre la consulta) | Mitigado por variedad de tipologías en la sesión + b-roll específico ocasional + planos de luz/textura como respiro. |
| Riesgo de que Daniel se desvíe a editar y descuide el guion | Mitigado por la regla 13.3.3 (70 %+ del tiempo de producción al guion). Revisar mensualmente en el cronometraje. |
| Riesgo de que la sesión única no rinda 30-50 clips | Mitigado por planificar lista cerrada de tomas antes de la sesión y filmar 15-20 s por toma como mínimo. |

### 13.9 · Pendientes operativos derivados de este apéndice

- [ ] **Agendar la sesión única de b-roll** (2-3 h, consulta de Daniel) antes de la grabación del E5.
- [ ] **Lista cerrada de tomas** para esa sesión, basada en §13.4. Imprimible, marcable durante el rodaje.
- [ ] **Estructura de almacenamiento** del b-roll: carpeta `contenido-rrss/b-roll-libreria/` con subcarpetas por tipología. Confirmar con Daniel si esta ubicación encaja o conviene otra (p. ej. fuera del repo si los archivos son pesados).
- [ ] **Plantilla `guion.md`** estandarizada (encabezado, marcadores de pausa, cierre con disclaimer educativo). Crear como `contenido-rrss/_plantilla-guion.md` para que sirva de copia base.
- [ ] **Revisar cronometraje del E5** con este formato y comparar contra la estimación 5-7 h. Si la edición visual desborda, ajustar §13.6 antes del E6.

---

## Cierre

YouTube + Podcast es la cuarta palanca del mapa TWIM (anexo CEO §2). Tiene la particularidad de ser la única que monetiza directamente el acto de consumir contenido — todas las demás (SEO, Newsletter, Meta Ads) monetizan al final del embudo. Eso no la convierte en la más importante, pero sí en la más eficiente por hora de producción una vez el sistema está montado.

La decisión 4-may-2026 (opción B) es deliberadamente conservadora: empezar con voz humana mayo-agosto reduce velocidad pero aumenta calidad del formato, y cuando ElevenLabs entre en septiembre, el guion editorial ya estará pulido. Lo contrario (lanzar con voz clonada antes de tener el formato definitivo) habría obligado a corregir errores en una capa que tiene más fricción.

El éxito del canal a 12 meses se mide por una sola pregunta: **¿está alimentando el embudo TWIM?** No por subs brutos, no por AdSense, no por Shorts virales. Si la respuesta es sí, los KPIs derivados ya cuadran solos.

— Notas técnicas: documento generado el 04-05-2026 a partir del TODO-PENDIENTE.md de la sesión 30-abr. Cuando entre T2 (septiembre 2026), revisar §5 para confirmar que la transición a ElevenLabs es estable y actualizar §7.2 con datos reales de AdSense. Si Meta Business Suite resulta insuficiente para el volumen, evaluar Metricool en mes 4-5.
