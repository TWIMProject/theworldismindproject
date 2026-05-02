# TWIM Project · Vista CEO · v2 consolidada · 1 mayo 2026

> Documento para leer despacio, no para ejecutar. Consolidación del informe del 30 abril + actualizaciones del 1 mayo.
>
> **Cambios respecto a la v1:**
> - Stack de producción audio + vídeo (YouTube + Podcast + NotebookLM + ElevenLabs) integrado como cuarta palanca de captación y nueva sección §5.
> - TWIM Clinic (modelo de derivación supervisada con Sergio) integrado como sección §11.
> - Rectificación de §9 (antes §8): la regla "no YouTube" queda anulada (válida para canal a cero, NO para 10,1K subs ya existentes).
> - Decisiones a cerrar pasan de 3 a 6.
> - Branding: "Psicología Profunda y Aplicada" como etiqueta editorial oficial (en lugar de "psicoanalítico"/"orientación psicoanalítica" que aparecía en algunos sitios).
> - Identidad de Instagram con sistema visual definido y plan de transición (PR #94 mergeado).
>
> Autor: Daniel Orozco Abia, ordenado por Claude. Fuentes: repo `theworldismindproject` al 1-05-2026, conversaciones de las sesiones 30-abr y 1-may, briefings internos.

---

## Índice

0. Cómo leer este documento
1. Dónde estás hoy (foto del negocio en una página)
2. Cultura TWIM — qué representas y qué no
3. El producto editorial (artículos + cartas + carruseles + podcast + YouTube)
4. Catálogo de ofertas y arquitectura del embudo
5. Stack de producción de marca — NotebookLM + ElevenLabs + reciclaje cruzado
6. Mercado, competencia y posicionamiento real
7. La realidad hacia la que tienes que mirar (12 meses)
8. Las 6 decisiones que tienes que tomar este mes
9. Lo que NO debes hacer (rectificada)
10. Riesgos vivos y deuda silenciosa
11. TWIM Clinic — modelo de derivación supervisada
12. Apéndice — métricas y benchmarks que vale la pena vigilar

---

## 0 · Cómo leer este documento

Este texto está escrito desde el rol que ocupas, no desde el rol en el que sueles operar. Tú operas casi siempre en modo *psicólogo en consulta + creador de contenido + manitas de Ads Manager*. Pero TWIM Project ya no es solo una consulta privada de Daniel Orozco: es una **marca editorial con un producto en construcción, un embudo activo, un canal de YouTube con tracción y una red clínica que empieza a montarse**. Y eso requiere otra mirada.

Léelo en dos pasadas:

1. **Hoy, café delante.** Lectura completa, sin tomar notas. Solo dejar que el mapa entre. Marcar mentalmente lo que te incomoda — eso es información.
2. **Mañana o pasado.** Volver a las secciones 7, 8 y 9. Ahí están las decisiones. El resto es contexto para que esas decisiones no se tomen a ciegas.

No tienes que estar de acuerdo con todo. Algunas cosas están escritas para forzar una postura, no para describir lo que ya piensas.

---

## 1 · Dónde estás hoy (foto del negocio en una página)

Si alguien te preguntara hoy "¿qué es TWIM Project?", la respuesta verdadera tiene tres capas:

- **Capa visible:** una web (`twimproject.com`), 27 artículos publicados en `/insights/`, 7 landings SEO recién desplegadas, una newsletter llamada "Te escribo" a punto de lanzarse formalmente, un libro publicado (*Los engranajes de la mente*, en Amazon), una consulta privada en Valencia, un canal de YouTube con 10,1K suscriptores, dos podcasts (TWIM Podcast · Psicología Aplicada con 4 episodios + Los Invitados con 15 episodios) en Spotify y YouTube, y una identidad pública en Instagram (`@daniorozcopsicologo`) y LinkedIn.
- **Capa operativa:** un embudo Instagram → ManyChat → landing Reto 7 días → MailerLite → secuencia 8 emails → CTA al programa "Deja de Buscarte en Otros". Pixel de Meta activo. Stripe enchufado para los talleres. Netlify functions para suscripción. NotebookLM como organizador de fuentes editoriales. Stack de producción audio en marcha (NotebookLM + ElevenLabs pendiente de configurar). Un puñado de herramientas saludables y, al fin, conectadas.
- **Capa real (la que importa):** un proyecto que aún no es ni consulta escalada ni infoproducto rentable, pero que **dejó de ser solo "psicólogo con marca personal"** y empezó a ser una **marca editorial-clínica con producto digital, canal de audio + vídeo, y red clínica supervisada en construcción**. Sigue siendo fase incómoda intermedia, pero el mapa es más rico que hace una semana.

### Cifras frías al 1-05-2026

| Indicador | Valor | Lectura honesta |
|---|---|---|
| Suscriptores totales en MailerLite | **30** | Base mínima, todo está por construir |
| Suscriptores activos en Reto 7 días | 5 (en distintos días del reto) | El embudo funciona, falta volumen |
| Open rate emails Reto (D7) | **70 %** | Excepcional. La gente que entra, lee. |
| CTR del email D7 → CTA programa | **20 %** | Excepcional. La promesa convierte. |
| Conversión histórica landing Reto (estimada) | ~0,33 % | Rota por fuera del email. Nuevo formulario+Pixel debería subirla a 5-8 % |
| Artículos publicados en /insights/ | 27 | Volumen sólido, calidad alta, distribución pobre |
| Landings SEO desplegadas (últimas 2 semanas) | 7 | Aún sin tráfico orgánico medible — Google necesita meses |
| **Suscriptores YouTube @daniorozcopsicologo** | **10.100** | Tracción real. Cumple criterios de monetización (1.000 subs + 4.000h watch). |
| **TWIM Podcast · Psicología Aplicada** | 4 episodios | Generados con NotebookLM Audio Overview hoy; migrar a voz Daniel clonada con ElevenLabs (decisión 1-may). |
| **Los Invitados · TWIM Podcast** | 15 episodios | Formato entrevistas con figuras (Bisila Bokoko, Loreto Crespo, Frank Cuesta…). |
| Libro publicado | *Los engranajes de la mente* | En Amazon, sin embudo de captación inverso conectado |
| Programas digitales activos | 1 listo (*Deja de Buscarte en Otros*), 2 en preventa (*Rompe el "tengo que"*, *Deja de obligarte*) | El catálogo aún no está al 100% terminado de producir |
| Talleres con landing pública | 2 (TDAH adolescentes + bachillerato motivación) | 0 inscripciones registradas en código. Posible pivote: Sergio como psicólogo principal. |
| Consulta privada (offline) | Operativa, fuente principal de ingresos hoy | La pieza que financia todo lo demás |
| **Red clínica TWIM Clinic** | 1 asociado en setup (Sergio) | Modelo de derivación supervisada. Detalle en §11. |

### Lo que esta foto significa

TWIM no tiene problema de **producto** (los emails con 70% open lo dicen). Tampoco tiene problema de **identidad** (la voz editorial está clara). Tiene un único problema real, y vale la pena nombrarlo sin disfrazarlo:

> **Problema central: tráfico cualificado al embudo.** Todo lo demás — la web, los artículos, las landings, el Pixel, la newsletter, el podcast, YouTube — son piezas para resolver eso. Si no entran personas nuevas en cantidad suficiente al sistema, el sistema convierte muy bien… pero a casi nadie.

Este documento orbita ese diagnóstico. Cuando dudes en una decisión, pregúntate: ¿esto trae más tráfico cualificado al embudo, o me distrae de eso?

---

## 2 · Cultura TWIM — qué representas y qué no

### Identidad declarada

- **Persona:** Daniel Orozco Abia, Psicólogo General Sanitario CV11515, Valencia, en consulta privada desde 2012.
- **Marco teórico:** Psicología Profunda y Aplicada. Integra orientación psicoanalítica + psicología del self + psicología aplicada. Es **psicoanálisis traducido**, que toma conceptos (superyó, juez interno, mecanismo, vínculo temprano) y los pone a trabajar en lenguaje cotidiano.
- **Etiqueta editorial oficial:** **"Psicología Profunda y Aplicada"**. Reemplaza definitivamente a "psicólogo psicoanalítico" o "orientación psicoanalítica" como label público.
- **Estética:** verde oscuro `#173D30`, verde medio `#265C4B`, beige `#C2A78B`, fondo crema `#FDFCFA`, tipografía Barlow Condensed. Sobria, casi monástica. Sin ilustraciones cute, sin emojis, sin íconos motivacionales.
- **Público:** adultos, mayoritariamente mujeres 25-50 años, con cuadros de ansiedad, dependencia emocional, burnout, autoexigencia. Secundariamente: padres y madres de adolescentes (talleres). Terciariamente: equipos profesionales (Método MindShift, in-company).
- **Tuteo siempre.** Nunca usted.

### Lo que TWIM **no** es (y conviene tener escrito)

- **No** es un proyecto de coaching.
- **No** es un proyecto de "salud mental positiva". Nada de "merece amor", "eres suficiente", "agradece más".
- **No** es una marca de psicología pop. Aunque el lenguaje se traduzca, los conceptos psicoanalíticos quedan visibles.
- **No** es solo Daniel-influencer. Es **Daniel-clínico**. La autoridad viene del CV11515 y de los años de consulta, no del crecimiento de seguidores.
- **No** es una empresa que use testimonios de pacientes.
- **No** es una marca que comprometa el secreto profesional para vender.

### El tono de voz, en una sola frase

> **"Describir el mecanismo, ofrecer una herramienta, no juzgar nunca."**

Y tres ejemplos reales del propio repo:

1. *"El «tengo que» no es solo una idea: es un modo automático. Aparece un disparador → tu mente lanza una urgencia → tu cuerpo se activa → actúas → algo se calma."*
2. *"Hay una escena que se repite en silencio. Por fuera cumples, entregas, resuelves. Por dentro algo no encaja. No es modestia. Es un desajuste que aprieta."*
3. *"Necesitar validación no es vanidad. Es un sistema interno que aprendiste para regular tu malestar. Y como cualquier sistema, tiene una lógica que se puede entender."*

Esta voz ya existe. No hay que reinventarla. **Hay que protegerla** cuando empieces a contratar redactores externos, asistentes virtuales, agencias o cuando un anuncio de Meta empuje a "hacerlo más comercial". Cuando uses ElevenLabs para clonar tu voz para el podcast, esta voz editorial es lo que tiene que sonar.

### Cultura interna

- **Sin secretos en el repo.** Las credenciales van a `.env.audit` (gitignored). CLAUDE.md tiene anotado token Netlify pendiente de rotar — deuda técnica con riesgo real.
- **Documentación viva.** Los briefings (`BRIEFING-*.md`, `PLAN-*.md`, `documentos-internos/*.md`) son la memoria del proyecto. Cada cambio importante deja rastro.
- **Trabajar por bloques pequeños y commits limpios.** CLAUDE.md como instrucción de generación de archivos.
- **Política con pacientes:** NUNCA en NotebookLM, NUNCA en ElevenLabs, NUNCA como prueba social. Solo casos clínicos anonimizados al máximo cuando aplique.

---

## 3 · El producto editorial (artículos + cartas + carruseles + podcast + YouTube)

TWIM ya tiene un **producto editorial multicanal** real: 27 artículos publicados con voz consistente, una newsletter en lanzamiento, carruseles de Instagram producidos como pieza editorial, un libro impreso, un canal de YouTube con 10K subs, y dos podcasts con 19 episodios entre los dos.

### 3.1 · Pilares temáticos detectables

Mirando los 27 artículos publicados, los temas se agrupan en cuatro racimos:

| Racimo | Estado | Producto digital asociado |
|---|---|---|
| **Dependencia emocional / validación externa** | Maduro (5+ artículos, programa cerrado) | "Deja de Buscarte en Otros" (lanzado, 49 € lanzamiento / 79 € core) |
| **Autoexigencia / juez interno / urgencia mental** | Maduro (6+ artículos, lead magnet activo) | "Reto 7 Días" (lead magnet) + "Rompe el TENGO QUE" (en preventa) |
| **Malestar laboral / burnout / sentido del trabajo** | Sólido (6+ artículos, landing SEO, carrusel "cansancio psíquico") | Falta producto digital propio. Oportunidad clara para 2026. |
| **Adolescencia / TDAH / crianza** | Pobre (solo 2 artículos) | 2 talleres con landing pública pero sin tracción. Pieza más débil del ecosistema. |

### 3.2 · La pregunta editorial

El catálogo está repartido en cuatro racimos pero **el embudo activo trabaja sobre todo el de autoexigencia/dependencia**. La decisión cocida en el documento original sigue válida: **camino A — concentración**. Doblar la apuesta en autoexigencia/dependencia los próximos 6 meses, mantener burnout y adolescencia en SEO pasivo. Cuando la newsletter cruce 1.000 suscriptores y haya asistente, abrir el segundo embudo.

### 3.3 · La newsletter "Te escribo" como columna vertebral

- Carta #1 "esto es lo que vas a recibir" → programada para **martes 5 mayo 19:00 CET**, audiencia ~24 personas.
- Carta #2 "La voz que te juzga" → programada para **martes 19 mayo 19:00 CEST**.
- Cross-sell "Te escribo" añadido a las 7 landings SEO.
- Exit-intent modal en las mismas 7 landings.
- GA4 events `newsletter_signup` y `newsletter_modal_shown` cableados.
- Objetivo declarado: **200 suscriptoras netas en mes 1**.
- Gate Meta Ads condicional (semana 4): si a 21 mayo hay <150 suscriptoras, se activa con 25-35 € de test.

> "Te escribo" no es 'un boletín más'. Es el activo de marca que te separa de los 50.000 psicólogos que tienen Instagram. Las cartas son el producto. Los emails secundarios son distribución. El podcast multiplica audiencia. Pero la newsletter es el lugar donde construyes audiencia que dura años.

### 3.4 · El podcast como nuevo motor — TWIM Podcast + Los Invitados

- **TWIM Podcast · Psicología Aplicada** — formato monólogo editorial, 4 episodios (Ep.1 "El cansancio que no se cura durmiendo", Ep.4 "La paz mental es una ilusión biológica", entre otros). Hoy generados con NotebookLM Audio Overview. **Decisión 1-may:** migrar a voz Daniel clonada vía ElevenLabs + disclosure transparente.
- **Los Invitados · TWIM Podcast** — formato entrevistas, 15 episodios con figuras como Bisila Bokoko, Loreto Crespo, Frank Cuesta, Jenny Barry. Mantener formato actual.
- **Distribución cruzada:** Spotify + YouTube (vídeo del podcast con cover estático). Esto es lo que enchufa el podcast con el canal YouTube de 10K subs.

### 3.5 · YouTube como activo dormido **que ya tiene tracción**

Con 10,1K suscriptores en YouTube, ya hay base para que el algoritmo empuje los próximos episodios y los Shorts derivados. La regla del doc original "no YouTube" queda **anulada** (era válida para canal a cero, no para esto).

Plan razonable:
- 1 episodio cada 2 semanas mayo-agosto. Subir a 1/semana desde septiembre cuando entre VA.
- 3-5 Shorts derivados de cada episodio (recortes de 30-60 s con caption + cover branded).
- Monetización (AdSense + Members + Super Thanks): activable casi inmediato, ingresos pasivos crecientes durante 12 meses.

### 3.6 · El libro como activo dormido (sigue dormido)

*Los engranajes de la mente* está publicado en Amazon. **No hay embudo desde el libro a la newsletter** todavía. Tarea pendiente y de alto ROI: landing rica del libro en `twimproject.com/libro` con índice + capítulo gratuito a cambio de email + reseñas + link a Amazon. Trabajo de 2 semanas, multiplica utilidad del libro durante años.

---

## 4 · Catálogo de ofertas y arquitectura del embudo

### 4.1 · Lo que vendes hoy (o estás a punto de vender)

Inventario real al 1-05-2026:

| Oferta | Tipo | Estado | Precio | Motor de captación |
|---|---|---|---|---|
| **Consulta privada** (Valencia + online) | 1:1 clínico | Operativo desde 2012 | ~70-90 €/sesión | Boca-oreja + SEO local + landings SEO |
| **Consulta supervisada (Sergio)** | 1:1 clínico derivado | Setup en mayo 2026 | 70 € (subir a 80 € recomendado) — 50 € Sergio + 20 €/30 € Daniel | Capacity adicional para leads que excedan agenda Daniel |
| **Deja de Buscarte en Otros** | Programa digital autoguiado | Listo | 79 € (lanzamiento 49 €) | Reto 7 días → secuencia 8 emails → CTA email D7 |
| **Rompe el TENGO QUE** | Programa digital autoguiado | Preventa | 39 € | Pendiente de embudo dedicado |
| **Deja de obligarte** | Programa digital autoguiado | Landing pública | Pendiente | Pendiente |
| **Taller TDAH adolescentes** | Grupal | Landing pública | Pendiente publicar | Cero captación activa hoy. Posible pivote: Sergio como principal. |
| **Taller bachillerato motivación** | Grupal | Landing pública | Pendiente publicar | Cero captación activa hoy. Mismo pivote. |
| **Taller "No puedo parar"** | Grupal | Landing setup | Pendiente | Pendiente |
| **Método MindShift / In-Company** | B2B corporativo | Mencionado en home + PDF | A medida | Cero pipeline declarado |
| **Libro "Engranajes de la mente"** | Físico/Kindle | Publicado en Amazon | Precio Amazon | Cero captación inversa |
| **Newsletter "Te escribo"** | Gratuito (activo de audiencia) | Lanzamiento formal 5 mayo | Gratis | Cross-sell SEO + exit-intent + carruseles + email + podcast |
| **TWIM Podcast + Los Invitados** | Audio editorial | Activo (4 + 15 episodios) | Gratis (futura monetización YouTube) | Spotify + YouTube |

### 4.2 · Mapa del embudo activo

```
       Instagram orgánico  ──┐
                              │
       Instagram Ads (en      │
       configuración) ────────┤
                              │
       YouTube + Podcast ─────┤      (NUEVO motor, 10K subs base)
                              │
       SEO landings ──────────┤      (7 nuevas, indexación 6-12 m)
                              ▼
                      Landing Reto 7 días / Newsletter
                              │
                       (Pixel activo, evento Lead disparando)
                              │
                              ▼
                      MailerLite · Newsletter "Te escribo"
                              │
                              ▼
                  Secuencia de 8 emails (D0–D7)
                              │
                              ▼
                  Email D7 · CTA programa "Deja de Buscarte en Otros"
                              │
                              ▼
                       Compra (Stripe)
                              │
                  ┌───────────┴───────────┐
                  ▼                       ▼
             Cliente Stripe          Si pide consulta:
             (programa digital)      → Daniel (si hay agenda)
                                     → Sergio (si Daniel lleno)
                                       supervisado
```

Esto **funciona**. El cuello de botella **no está dentro del embudo**: está en el grifo de arriba. La pregunta no es "¿cómo mejoro el embudo?" sino "¿cómo le abro más la llave?". Y la respuesta principal a 12 meses es: **YouTube + Podcast + Newsletter + SEO + Meta Ads en gate condicional**.

### 4.3 · Arquitectura ideal a 6 meses

```
                      ┌─── consulta privada Daniel (cash flow base)
                      │
                      ├─── consulta derivada Sergio (capacity adicional)
                      │
   Tráfico orgánico ──┤
   (SEO + IG + LK +   │
    YouTube + Podcast)│─── newsletter "Te escribo" (audiencia)
                      │         │
                      │         ├──→ programa #1 (Deja de Buscarte)
                      │         ├──→ programa #2 (Rompe el TENGO QUE)
                      │         └──→ taller en directo (1-2 al año)
                      │
   Tráfico pagado ────┘
   (Meta Ads cuando
    el orgánico ya
    cualifica)
                      │
                      └─── monetización directa YouTube AdSense (~100-400 €/mes a fin de 2026)
```

El cambio respecto al hoy: **dejar de tener "muchas ofertas con embudos rotos"** y pasar a "infraestructura única donde todo se alimenta de la newsletter + el podcast". El podcast y la newsletter son los dos ejes; todo lo demás se conecta a ellos.

---

## 5 · Stack de producción de marca · NotebookLM + ElevenLabs + reciclaje

> Sección nueva del 1-may-2026. Resuelve el cuello de botella estructural identificado en §6 del doc original: "el tiempo es el recurso escaso, no el dinero".

### 5.1 · La idea central

Cada episodio de podcast se convierte en **7 piezas derivadas** sin esfuerzo extra de producción:

1. 1 audio Spotify.
2. 1 vídeo YouTube (audio + cover estático + waveform animado).
3. 3-5 Shorts/Reels de YouTube + Instagram (recortes 30-60 s).
4. 1 carrusel Instagram sistema A1 (idea principal en 5-7 slides).
5. 1 cita visual sistema A2 (frase memorable).
6. 1 fragmento newsletter "Te escribo".
7. 1 post LinkedIn (versión más profesional del fragmento).

**Un trabajo de producción alimenta el ecosistema completo durante una semana.**

### 5.2 · Los 4 elementos del stack

| Herramienta | Rol | Coste |
|---|---|---|
| **NotebookLM** (Google) | Organiza fuentes (artículos, libro, notas editoriales — NUNCA pacientes), genera resúmenes, esquemas, guion de partida. | Gratis al 1-may-2026 |
| **ElevenLabs** | Clona la voz de Daniel (30-60 min audio fuente). Genera el audio del podcast a partir del guion. Disclosure obligatorio. | ~22 €/mes plan Creator |
| **YouTube** | Distribución de vídeo + Shorts derivados + monetización AdSense. | Gratis (e ingresos) |
| **Spotify** | Distribución de audio. | Gratis |

### 5.3 · Workflow de producción (de tema a publicación)

```
PASO 1 · Curaduría editorial Daniel · 30-45 min
  Elegir tema. Reunir fuentes propias (artículos, libro, notas).
  NUNCA fuentes clínicas de pacientes.

PASO 2 · NotebookLM · 30 min
  Subir fuentes a notebook. Pedir esquema 5-7 puntos. Output: estructura.

PASO 3 · Redacción guion · Daniel · 60-90 min
  A partir del esquema, redactar guion en voz tuya editorial.
  2.500-5.000 palabras ≈ 15-30 min hablados.

PASO 4 · ElevenLabs · ~10 min
  Pegar guion. Voz clonada Daniel. Generar audio.

PASO 5 · Edición rápida · ~15 min
  Audacity. Intro/outro + disclosure + normalizar volumen.

PASO 6 · Publicación cruzada · ~30 min
  Spotify + YouTube + descripciones + cover + tags.

TOTAL POR EPISODIO: ~3-4 h Daniel
(con VA: baja a 1.5-2 h Daniel + asistente lo demás)
```

### 5.4 · Disclosure obligatorio (deontológico + plataformas)

En **bio del podcast** y en **descripción de cada episodio**:

> *Audio generado con clonación de voz vía ElevenLabs a partir del material editorial de Daniel Orozco Abia · CV11515. La voz es la suya, sintetizada para optimizar tiempo de producción.*

En el **primer minuto del audio**:

> *Esto es TWIM Podcast. La voz que escuchas es la de Daniel Orozco, sintetizada con clonación para liberar tiempo de producción. El contenido editorial es 100 % suyo.*

Razones: (1) deontológica — el oyente debe saber qué escucha; (2) Spotify/Apple/YouTube exigen etiquetar contenido AI-asistido; (3) reputacional — cuando se descubra (y se descubre), el daño es proporcional al ocultamiento.

### 5.5 · Política de uso

- **NUNCA NotebookLM ni ElevenLabs con material clínico de pacientes.** Política deontológica firme. Solo material editorial propio.
- **NotebookLM como organizador y generador de estructura, no como autor final.** El guion siempre lo escribe Daniel a partir del esquema.
- **ElevenLabs para uso comercial requiere plan Creator (22 €/mes).** Plan free no permite.
- **Backup obligatorio** del audio fuente (30-60 min de entrenamiento) en local + Drive cifrado + disco externo. Si ElevenLabs cambia ToS o cierra, recreas el modelo.

### 5.6 · Por qué este stack es la cuarta palanca de captación TWIM

Tres razones estructurales:

1. **Es el único motor de captación que monetiza directamente.** SEO trae tráfico → embudo → ventas. Newsletter construye audiencia → ventas. Meta Ads compra atención → ventas. **YouTube monetiza el propio acto de consumir el contenido**, además de alimentar todo lo demás. Doble pago.
2. **Reciclaje cruzado.** 1 episodio = 7 piezas. La eficiencia más alta del mapa.
3. **Construye autoridad sostenida.** YouTube con 10K-100K subs te posiciona en buscadores, te citan en medios, te invitan a podcasts. Activo permanente, no atención efímera.

---

## 6 · Mercado, competencia y posicionamiento real

> Mercado de psicología online en español al 1-may-2026. Datos de Ahrefs no disponibles esta sesión por límite de plan; cifras son aproximaciones del sector.

### 6.1 · El mercado

Cuatro tipos de actores:

1. **Plataformas tipo marketplace** (Mundopsicologos, ifeel, TherapyChat). SEO de cabeza, presupuesto Ads. No te peleas en su terreno.
2. **Coaches con marca personal grande** (Marian Rojas, Patricia Ramírez). "Salud mental positiva". Antítesis de TWIM — y eso es ventaja.
3. **Psicólogos con consulta + presencia digital media** (cientos por ciudad). Genérico. Es el lugar del que sales.
4. **El espacio raro: clínico-editorial-profundo** (poca gente, mucha demanda). Recalcati en Italia, Lori Gottlieb en EEUU, Anabel González (psiquiatra) en España. **Aquí TWIM se está construyendo.**

### 6.2 · Tu posicionamiento real

> *"Es un psicólogo de Valencia que escribe en serio y no dice tonterías motivacionales."*

El trabajo de los próximos 12 meses no es cambiar este posicionamiento — es **amplificarlo sin diluirlo** cuando el embudo escale. Y ahora con el podcast y YouTube, también: *"y el que trae el psicoanálisis aplicado a lo cotidiano sin ridiculizarlo"*.

### 6.3 · Referentes de la categoría

Sin afán exhaustivo, son el mapa para entender la categoría:

- **Anabel González** (psiquiatra, libros sobre dependencia emocional / EMDR).
- **Borja Vilaseca** (modelo de negocio editorial-formativo de referencia, tono distinto).
- **Miguel Silveira** (psiquiatra, contenido TDAH adolescente).
- **Gabriel Rolón** (psicoanalista argentino, marca editorial muy potente).
- **Massimo Recalcati** (psicoanalista italiano, "techo" del posicionamiento clínico-editorial-mainstream).

No es competir con ellos. Es **estudiar cómo construyen autoridad** — libros, cursos, columnas regulares, conferencias, formación, podcast.

### 6.4 · Donde sí compites cabeza con cabeza

SEO local: "psicólogo dependencia emocional Valencia", "psicólogo burnout Valencia". Pelea con 20-40 consultas privadas en Valencia. Las landings SEO son tu artillería. SEO local en psicología tarda **6-12 meses** en estabilizarse — no esperes ranking visible antes de septiembre 2026.

### 6.5 · Demandas no atendidas que tu público pide

- **Padres y madres con hijos adolescentes en Valencia** que buscan ayuda y no encuentran nada que no sea publicidad de academias. **Pivote nuevo (1-may):** Sergio como psicólogo principal de los talleres TDAH + bachillerato. Desbloquea esto.
- **Mujeres profesionales 30-45 con burnout que no saben que es burnout.** Falta producto digital propio que cierre el embudo.
- **Hispanohablantes en LatAm y EEUU** que buscan psicólogos con autoridad clínica online. La landing `psicologo-online.html` apunta ahí. Cuando "Te escribo" cruce 1.000 suscriptores, abrir nicho LatAm con producto propio en pesos / dólares.

---

## 7 · La realidad hacia la que tienes que mirar (12 meses)

### 7.1 · El supuesto base — qué pasaría si no cambias nada

- 200-400 suscriptores en MailerLite.
- 7-15 ventas del programa "Deja de Buscarte en Otros".
- 3-6 talleres llenos.
- Consulta privada estable.
- YouTube creciendo lentamente sin foco.
- Marca creciendo lentamente.

**Buen año personal, mal año de negocio.**

### 7.2 · El supuesto ambicioso — TWIM como marca editorial-clínica-multimedia real

A 30 abril 2027:

- **Newsletter "Te escribo"**: 2.500-4.000 suscriptoras activas. Open rate >40 %.
- **Catálogo digital**: 3 programas vivos. 50-150 ventas anuales acumuladas → 4.000-12.000 €.
- **Talleres**: 3-4 ediciones llenas con Sergio como principal.
- **In-Company / MindShift**: 1-3 contratos. Ticket 3.000-8.000 €.
- **SEO local Valencia**: top 5 dependencia emocional + burnout.
- **Libro**: segunda obra en preparación, idealmente con editorial reconocida.
- **YouTube**: 25.000-40.000 subs. Monetización AdSense 100-400 €/mes a fin de año.
- **Podcast**: 50-80 episodios totales acumulados. Posicionamiento "podcast clínico de referencia en español".
- **TWIM Clinic**: 2-3 asociados (Sergio + especialista parejas + posiblemente trauma).
- **Equipo**: 1 VA a tiempo parcial + posible diseñadora freelance puntual.

### 7.3 · Las 6 palancas que mueven todo (actualizadas)

1. **Volumen de la newsletter.** Cada suscriptor cualificado vale 5-50 € de LTV. Llegar a 2.000 suscriptores es la palanca #1.
2. **Cierre del segundo programa monetizable** (probablemente burnout, dado el racimo editorial maduro).
3. **Activar libro como puerta inversa al ecosistema.** Landing del libro + capítulo gratuito → newsletter.
4. **Stack de producción audio + vídeo (NUEVA palanca).** YouTube + Podcast + NotebookLM + ElevenLabs. Reciclaje cruzado 1 episodio → 7 piezas. Es la palanca con mejor ROI/coste-en-tiempo del mapa.
5. **TWIM Clinic — modelo de derivación supervisada (NUEVA palanca).** Sergio como primer asociado, talleres adolescencia con él como principal, escalado a 3-5 asociados a 12-18 meses. Detalle en §11.
6. **Delegar ejecución, blindar la voz.** VA en junio. La voz se preserva con ElevenLabs (sin gastar tiempo grabando) y la VA absorbe operación.

### 7.4 · Lo que ya no es posible negar

- **Instagram orgánico solo no escala.** Lo demás sí (SEO + newsletter + YouTube + podcast + Meta Ads).
- **Sin pago hay límites duros** en algunos canales. Newsletter y podcast crecen orgánico; SEO y Meta Ads requieren paciencia o presupuesto.
- **El tiempo es el recurso escaso, no el dinero.** Cualquier inversión que libere tiempo de Daniel tiene ROI mucho mayor que cualquier herramienta o curso. ElevenLabs es exactamente eso. La VA también.

---

## 8 · Las 6 decisiones que tienes que tomar este mes

> El doc original de 30 abril listaba 3 decisiones. Hoy son 6. El resto sigue válido.

### Decisión 1 — Concentración o expansión de embudos

**Recomendado: Camino A — Concentración.** Doblar apuesta autoexigencia/dependencia los próximos 6 meses. Burnout y adolescencia en SEO pasivo. Cuando newsletter cruce 1.000 suscriptores y haya VA, abrir camino B.

### Decisión 2 — Presupuesto Meta Ads próximos 6 meses

**Recomendado: empezar 6 €/día (180 €/mes), subir a 15 €/día si en 14 días hay ≥10 leads y CPL ≤ 4 €, subir a 30 €/día si en 60 días los números aguantan.**

### Decisión 3 — Cuándo contratas la primera VA

**Recomendado: Junio 2026.** 200-400 €/mes, 10-15 h/semana. Las 3 tareas que delegas primero: programar carruseles + reposting + atención mensajes. Las 3 que NO delegas: escribir, atender pacientes, supervisión clínica.

### Decisión 4 — Estructura jurídica de TWIM Clinic con Sergio (NUEVA)

**Recomendado: Opción B — cada uno factura su parte.** Sergio factura al paciente sus 70 € (o 80 € si subes precio). Sergio te paga 20 €/30 € de supervisión. Más limpio jurídicamente, evita riesgo de falso autónomo. Cita con gestor antes del 15 mayo. Detalle en doc `twim-clinic-modelo-derivacion.md` §3.

### Decisión 5 — Ritmo de publicación del podcast (NUEVA)

**Recomendado: 1 episodio cada 2 semanas mayo-agosto, subir a 1/semana desde septiembre cuando entre VA.** Esto significa 12-15 episodios totales en 2026 con la palanca de reciclaje cruzado funcionando.

### Decisión 6 — Migración del podcast actual a voz Daniel clonada (NUEVA)

**Recomendado: Opción 2 — mantener con disclosure transparente + migrar progresivamente a ElevenLabs con voz Daniel.**

- Setup ElevenLabs Creator (~22 €/mes).
- Grabar 30-60 min de audio fuente.
- Entrenar modelo "Daniel Orozco · TWIM Podcast".
- Test calidad con alguien que conozca la voz.
- Disclosure en bio + descripción de cada episodio + intro audio.
- Republicar (o editar descripción de) los 4 episodios actuales con disclosure.
- Detalle en doc `elevenlabs-clonacion-voz-podcast.md`.

---

## 9 · Lo que NO debes hacer (rectificada)

- **No abras un segundo embudo (burnout / adolescencia / consulta) hasta que el primero esté saturado.** Saturación = el Reto 7 días recibe ≥50 leads/mes orgánicos sin necesidad de Ads.
- **~~No grabes vídeos largos para YouTube.~~** **Rectificación 1-may:** la regla original era válida con canal a cero. **Con 10,1K subs ya existentes la regla cambia:** sí alimenta el canal con el stack NotebookLM + ElevenLabs (no grabas, generas). La regla actualizada es: *"No grabes vídeos largos cara-a-cámara durante horas; sí alimenta el canal con el stack de producción del §5"*.
- **No aceptes entrevistas en podcasts pequeños solo por aparecer.** Audiencia ≥10× tu newsletter o no lo hagas.
- **No contrates "agencia de marketing" todavía.** Tu producto y embudo están — los datos no. Las agencias funcionan cuando hay datos. Ahorra esos 1.000-2.000 €/mes.
- **No compres cursos de "cómo escalar tu consulta".** Lo que enseñan ya lo sabes (o está en este documento).
- **No aceptes pedidos del público para hacer un grupo terapéutico online ahora.** Atrae demanda pero te ata a horarios fijos. Postergar a 2027 cuando haya 1.000+ suscriptores.
- **No publiques en LinkedIn por publicar.** O activas LinkedIn como canal real para B2B / In-Company (1 post largo/semana sostenido), o lo dejas dormido. Lo intermedio es ruido.
- **No cambies la voz editorial al recibir crítica.** Habrá quien diga "muy serio", "poca calidez", "demasiado psicoanalítico". No es tu público. Tu público siente que **por fin alguien le habla en serio**.
- **No publiques Audio Overviews de NotebookLM directamente como podcast (NUEVA).** Las dos voces sintéticas norteamericanas no son tu marca. Para podcast publicado, voz Daniel clonada vía ElevenLabs con disclosure. NotebookLM se usa internamente como organizador/generador de estructura.
- **No subas material clínico de pacientes a NotebookLM ni ElevenLabs (NUEVA, deontológico).** Política firme. Solo material editorial propio.
- **No copies a Sergio en cosas de marca pública sin que esté alineado con la voz TWIM (NUEVA).** Su voz pública dentro del proyecto debe pasar por la sesión 0 de marco editorial (doc TWIM Clinic §7).

---

## 10 · Riesgos vivos y deuda silenciosa

### 10.1 · Riesgo de seguridad / cumplimiento

- **Token Netlify expuesto pendiente de rotar.** En CLAUDE.md está marcado el token literal (no se repite aquí por seguridad). Acción: revocarlo en `https://app.netlify.com/user/applications`, generar nuevo, actualizar `.env.audit` y eliminar el literal de CLAUDE.md una vez rotado. 5 minutos. Hacerlo esta semana.
- **MFA (2FA) en Netlify desactivado.** 5 minutos.
- **No hay copia de seguridad declarada de la lista de MailerLite.** Buena práctica: exportar CSV mensual + cifrar + Drive.
- **Política de privacidad** (`privacy.html`) — revisar anualmente con texto actualizado para Pixel Meta + GA4 + ElevenLabs (cuando se active).
- **Backup obligatorio del audio fuente de ElevenLabs** (NUEVO). Local + Drive cifrado + disco externo. Si ElevenLabs cambia ToS o cierra, recreas el modelo.

### 10.2 · Riesgo operativo

- **Solo Daniel sabe el sistema entero.** Si te caes 2 semanas, embudo sigue corriendo (automatizado), pero no se publica nada nuevo. Mitigación: VA + documentación viva (los `BRIEFING-*.md`, `documentos-internos/*.md`).
- **MailerLite es proveedor único.** Lock-in moderado. Documentar qué hace cada automation.
- **Netlify es proveedor único.** Lock-in bajo (HTML estático), migración fácil. Bajo riesgo.
- **NotebookLM es producto Google que puede cambiar (NUEVO).** Histórico Google: Bard, Project IDX, etc. Los notebooks son recreables si hay que migrar a otra herramienta similar.

### 10.3 · Riesgo de marca

- **Mezcla de etiquetas viejas y nuevas en el repo.** Hoy 1-may aplicado lote de limpieza ("psicoanalítico"/"orientación psicoanalítica" → "Psicología Profunda y Aplicada"). Auditar trimestralmente.
- **README desactualizado.** 30 minutos para corregir.
- **Mezcla de identidades visuales en Instagram resuelta** con sistema visual del PR #94 (mergeado). Implementación: cero publicación fuera del sistema desde mañana.
- **Disclosure ElevenLabs (NUEVO).** Sin disclosure, riesgo deontológico + reputacional + plataformas. Con disclosure desde día 1, blindado.

### 10.4 · Deuda editorial

- **Cluster adolescencia casi vacío.** 2 artículos de 27. Atacar cuando se decida pivote Sergio en talleres.
- **Sin caso clínico anonimizado publicado todavía.** Única forma legítima de prueba social. Vale la pena 3-4 publicados antes de fin de año.
- **Sin página rica del libro.** El libro merece landing en `twimproject.com/libro` con índice + capítulo gratuito + reseñas + Amazon. Trabajo de 2 semanas, ROI altísimo a años.

---

## 11 · TWIM Clinic — modelo de derivación supervisada

> Sección nueva del 30-abr-2026. Detalle completo en doc `twim-clinic-modelo-derivacion.md`. Aquí lo esencial.

### 11.1 · Qué es

TWIM deja de ser "consulta privada de Daniel Orozco" y empieza a ser **red clínica supervisada con marca propia**. Sergio (psicólogo amigo) entra como primer asociado. Modelo:

- Sergio atiende pacientes derivados (adolescentes y adultos).
- Tarifa actual: 70 €/sesión paciente. Sergio cobra 50 €. Daniel margen 20 €.
- **Recomendación: subir tarifa a 80 €/sesión.** Sergio sigue cobrando 50 €, Daniel pasa a 30 € (+50 % margen). El mercado Valencia lo aguanta.
- Daniel **supervisa clínicamente** el caso.

### 11.2 · Lo que esto cambia estructuralmente

- **Techo del negocio clínico:** ahora es supervisar bien (5-8 asociados a tiempo parcial), no las horas de Daniel.
- **Modelo de ingresos:** aparece componente de margen estructural (20-30 € por cada sesión que atiende un asociado, escalable).
- **Identidad de marca:** TWIM deja de ser "un psicólogo con voz editorial" y empieza a ser "una escuela clínica con voz editorial".

### 11.3 · La estructura jurídica recomendada

**Opción B: cada uno factura su parte.** Sergio factura al paciente. Sergio te paga supervisión por factura mensual. Limpio jurídicamente. Evita riesgo de falso autónomo (que es el riesgo más caro si se materializa). Cita con gestor antes del 15 mayo para validar.

### 11.4 · La oportunidad inmediata

**Septiembre 2026: lanzar la primera edición del taller TDAH adolescentes con Sergio como psicólogo principal y tú como supervisor + co-firmante.**

Esto cierra cuatro frentes a la vez: (1) llena los talleres que hoy están vacíos, (2) le da volumen a Sergio rápido, (3) valida el modelo de derivación supervisada, (4) genera contenido (caso clínico anonimizado del taller, primer artículo del racimo adolescencia).

### 11.5 · KPIs y horizonte

- Mes 3: Sergio ~30 sesiones/mes, margen Daniel ~600 €/mes.
- Mes 6: ~60 sesiones/mes, margen Daniel ~1.200 €/mes + primera edición taller TDAH.
- Mes 12: ~80-100 sesiones/mes con Sergio, margen Daniel ~2.500 €/mes + 2ª-3ª edición talleres + posible 2º asociado en Q4.

A 24 meses con 5 asociados a régimen estable: **margen Daniel 100.000-150.000 €/año solo de la parte clínica**, sin tocar más pacientes propios. Eso es lo que separa una consulta de una clínica.

### 11.6 · 5 decisiones a cerrar este mes (subset de §8)

- [ ] Cita con gestor para validar Opción B (antes del 15 mayo).
- [ ] Pricing definitivo (recomendado: 80 €).
- [ ] Talleres adolescencia con Sergio como responsable principal: sí/no.
- [ ] SLA de supervisión (frecuencia, formato, día y hora fijos).
- [ ] Sesión 0 de marco TWIM con Sergio (2-3 horas, antes del 31 mayo).

---

## 12 · Apéndice — métricas y benchmarks

Una pestaña, una vez por semana lunes (15 min). Si dedicas más, estás procrastinando.

### 12.1 · Métricas semanales (cada lunes)

| Métrica | Fuente | Cota saludable mes 1-3 | Cota objetivo mes 6 |
|---|---|---|---|
| Suscriptores netos nuevos en MailerLite | ML dashboard | +30/semana | +100/semana |
| Open rate Carta semanal "Te escribo" | ML | ≥40 % | ≥45 % |
| Click rate Carta → web | ML | ≥5 % | ≥8 % |
| Visitas únicas a `/reto-7-dias` | GA4 | ≥150/semana | ≥500/semana |
| Conversión visitante → lead Reto | GA4 | ≥5 % | ≥8 % |
| Visitas a las 7 landings SEO | GA4 | aún 0 (Google indexa lento) | ≥800/semana en agregado |
| Ventas Stripe del programa | Stripe | 0-2/semana | ≥5/semana |
| Suscriptores nuevos YouTube semanales | YouTube Studio | +50/semana | +200/semana |

### 12.2 · Métricas mensuales (primer lunes de mes)

- **CPL Meta Ads** (gasto / leads). Cota mes 1: ≤4 €. Cota mes 6: ≤2 €.
- **LTV estimado por suscriptor** (ingresos del mes / suscriptores totales).
- **Ingresos por canal**: consulta privada / programa digital / talleres / in-company / clínica derivada Sergio / AdSense YouTube.
- **Watch time medio episodio podcast** (YouTube Studio): cota mes 6 ≥40 % retención.
- **Ingresos AdSense YouTube** mensuales: cota mes 6 30-100 €, cota mes 12 100-400 €.
- **Sesiones supervisadas a Sergio** (TWIM Clinic): cota mes 6 ≥60, cota mes 12 ≥80.

### 12.3 · Benchmarks de referencia

> Aproximaciones, no datos auditados.

- Open rate medio newsletter de psicólogos con voz fuerte: 35-45 % (TWIM hoy: 51-70 % en grupo Reto, excepcional).
- Conversión visitante → lead landing lead magnet psicólogo: 2-5 %.
- CPL Meta Ads para lead magnet psicológico España: 2-6 €.
- Conversión email → compra programa bajo ticket (≤100 €): 2-5 %.
- Ratio suscriptores newsletter / compradores anuales programa estrella: 5-10 %.
- AdSense YouTube nicho psicología español: 1-3 € por 1.000 vistas (CPM real, no inflado).
- Retención podcast: episodios <20 min ≥45 % retención es excelente; 20-40 min ≥35 % es bueno.

### 12.4 · Cómo leer estos números sin enloquecer

1. **Mide cada lunes, no cada día.** Las métricas diarias son ruido. Las semanales son señal.
2. **Compara contigo mismo, no con benchmarks.** El benchmark sirve para situarse, no para juzgarse.
3. **Si una métrica empeora 2 semanas seguidas, investiga. Si mejora 2 semanas seguidas, no toques nada.** El instinto de "optimizar" cuando algo funciona es la forma más común de romperlo.
4. **El test de los 5 segundos** (perfil IG, perfil YouTube, web). Una vez al mes, abrir tus propios canales en incógnito sin estar logueado. ¿Qué entiende un desconocido en 5 segundos? Si la respuesta es ambigua, el sistema no se está aplicando.

---

## Cierre

TWIM Project no es lo que era hace 6 meses. Tampoco es lo que va a ser dentro de 12. Estás en un punto raro y poco glamuroso: el que hay entre "esto funciona técnicamente" y "esto funciona económicamente". La mayoría de proyectos editoriales se rompen aquí, no por falta de talento sino por dispersión.

Lo que tienes a fecha 1 de mayo es un mapa **mucho más rico** que hace una semana:

- Un embudo editorial activo (Reto 7 días → Newsletter → Programa).
- 7 landings SEO desplegadas (indexación 6-12 meses).
- Un canal YouTube con 10K subs (motor de captación + monetización directa).
- Dos podcasts con 19 episodios entre los dos (a migrar a voz Daniel clonada con disclosure).
- Un stack de producción (NotebookLM + ElevenLabs) que multiplica output sin multiplicar tiempo.
- Una red clínica empezando (TWIM Clinic con Sergio como primer asociado).
- Un sistema visual definido para Instagram (cero clickbait, cero reposts virales, cero fotos familiares en grid público).

Lo único que te separa de ser un negocio editorial-clínico-multimedia de referencia en español es **disciplina sostenida durante 12-18 meses** sobre las 6 palancas de §7.3 y las 6 decisiones de §8.

Y, sobre todo, recuerda lo que ya sabes en consulta y a veces se te olvida cuando estás operando el embudo:

> **No es urgencia. Es repetición.**

Buena lectura.

— Notas técnicas: documento generado el 1-05-2026 a las 10:30 (consolidación del informe del 30-abr + actualizaciones del 1-may). Sustituye al doc `ceo-vista-fin-de-semana.md` como referencia estratégica de trabajo. El original se mantiene como histórico. Cuando aparezca dato nuevo importante (Ahrefs disponible, primera medición real KPIs YouTube post-consolidación, primer mes de Sergio operativo, etc.), generar v3.

