# TWIM Project · Vista CEO · fin de semana 30 abr – 4 may 2026

> Documento para leer despacio, no para ejecutar. La operación (Ads Manager, Pixels, suscriptores) seguirá ahí el lunes. Esto es para subir 1.000 metros y ver el mapa entero antes de volver al detalle.

> Autor del documento: tú, ordenado por Claude. Fuentes: repo `theworldismindproject` al 30-04-2026, briefings internos, planes de captación y lanzamiento, catálogo editorial, identidad de marca declarada en CLAUDE.md y README.

---

## Índice

0. Cómo leer este documento
1. Dónde estás hoy (foto del negocio en una página)
2. Cultura TWIM — qué representas y qué no
3. El producto editorial (artículos + cartas + carruseles)
4. Catálogo de ofertas y arquitectura del embudo
5. Mercado, competencia y posicionamiento real
6. La realidad hacia la que tienes que mirar (12 meses)
7. Las 3 decisiones que tienes que tomar este fin de semana
8. Lo que NO debes hacer (lista corta de tentaciones)
9. Riesgos vivos y deuda silenciosa
10. Apéndice — métricas y benchmarks que vale la pena vigilar

---

## 0 · Cómo leer este documento

Este texto está escrito desde el rol que ocupas, no desde el rol en el que sueles operar. Tú operas casi siempre en modo *psicólogo en consulta + creador de contenido + manitas de Ads Manager*. Pero TWIM Project ya no es solo una consulta privada de Daniel Orozco: es una **marca editorial con un producto en construcción y un embudo activo**. Y eso requiere otra mirada.

Léelo en dos pasadas:

1. **Sábado por la mañana, café delante.** Lectura completa, sin tomar notas. Solo dejar que el mapa entre. Marcar mentalmente lo que te incomoda — eso es información.
2. **Domingo por la tarde.** Volver a las secciones 6, 7 y 8. Ahí están las decisiones. El resto es contexto para que esas decisiones no se tomen a ciegas.

No tienes que estar de acuerdo con todo. Algunas cosas están escritas para forzar una postura, no para describir lo que ya piensas.

---

## 1 · Dónde estás hoy (foto del negocio en una página)

Si alguien te preguntara hoy "¿qué es TWIM Project?", la respuesta verdadera tiene tres capas:

- **Capa visible:** una web (`twimproject.com`), 27 artículos publicados en `/insights/`, 7 landings SEO recién desplegadas, una newsletter llamada "Te escribo" a punto de lanzarse formalmente, un libro publicado (*Los engranajes de la mente*, en Amazon), una consulta privada en Valencia y una identidad pública en Instagram (`@daniorozcopsicologo`), LinkedIn y YouTube.
- **Capa operativa:** un embudo Instagram → ManyChat → landing Reto 7 días → MailerLite → secuencia 8 emails → CTA al programa "Deja de Buscarte en Otros". Pixel de Meta activo. Stripe enchufado para los talleres. Netlify functions para suscripción. Un puñado de herramientas saludables y, al fin, conectadas.
- **Capa real (la que importa):** un proyecto que aún no es ni consulta escalada ni infoproducto rentable. Está en la **fase incómoda intermedia** entre "psicólogo con marca personal" y "marca editorial con producto digital". Esa fase tiene un olor reconocible: muchas piezas montadas, números todavía pequeños, dudas legítimas sobre qué crece y qué se puede dejar morir.

### Cifras frías al 30-04-2026

| Indicador | Valor | Lectura honesta |
|---|---|---|
| Suscriptores totales en MailerLite | **30** | Base mínima, todo está por construir |
| Suscriptores activos en Reto 7 días | 5 (en distintos días del reto) | El embudo funciona, falta volumen |
| Open rate emails Reto (D7) | **70 %** | Excepcional. La gente que entra, lee. |
| CTR del email D7 → CTA programa | **20 %** | Excepcional. La promesa convierte. |
| Conversión histórica landing Reto (estimada) | ~0,33 % | Rota por fuera del email. Nuevo formulario+Pixel debería subirla a 5-8 % |
| Artículos publicados en /insights/ | 27 | Volumen sólido, calidad alta, distribución pobre |
| Landings SEO desplegadas (últimas 2 semanas) | 7 | Aún sin tráfico orgánico medible — Google necesita meses |
| Libro publicado | *Los engranajes de la mente* | En Amazon, sin embudo de captación conectado |
| Programas digitales activos | 1 listo (*Deja de Buscarte en Otros*), 2 en preventa (*Rompe el "tengo que"*, *Deja de obligarte*) | El catálogo aún no está al 100% terminado de producir |
| Talleres con landing pública | 2 (TDAH adolescentes + bachillerato motivación) | 0 inscripciones registradas en código todavía |
| Consulta privada (offline) | Operativa, fuente principal de ingresos hoy | No es objeto de este documento, pero financia todo lo demás |

### Lo que esta foto significa

TWIM no tiene problema de **producto** (los emails con 70% open lo dicen). Tampoco tiene problema de **identidad** (la voz editorial está clara). Tiene un único problema real, y vale la pena nombrarlo sin disfrazarlo:

> **Problema central: tráfico cualificado al embudo.** Todo lo demás — la web, los artículos, las landings, el Pixel, la newsletter — son piezas para resolver eso. Si no entran personas nuevas en cantidad suficiente al sistema, el sistema convierte muy bien… pero a casi nadie.

Este documento orbita ese diagnóstico. Cuando dudes en una decisión, pregúntate: ¿esto trae más tráfico cualificado al embudo, o me distrae de eso?

---

## 2 · Cultura TWIM — qué representas y qué no

La cultura editorial ya está escrita en tres documentos internos (CLAUDE.md, los briefings del programa estrella, los planes de la newsletter "Te escribo"). Pero conviene leerla de un tirón, porque define lo que se puede decir "sí" y lo que hay que aprender a decir "no".

### Identidad declarada (la que ya está en los documentos)

- **Persona:** Daniel Orozco Abia, Psicólogo General Sanitario CV11515, Valencia, en consulta privada desde 2012.
- **Marco teórico:** psicoanálisis aplicado. No "psicoanálisis ortodoxo" ni "psicoanálisis lacaniano puro". Es **psicoanálisis traducido**, que toma conceptos (superyó, juez interno, mecanismo, vínculo temprano) y los pone a trabajar en lenguaje cotidiano.
- **Etiqueta editorial:** "Psicología Profunda y Aplicada". Este es el wording oficial que reemplaza a "orientación psicoanalítica" desde la última actualización del branding global.
- **Estética:** verde oscuro `#173D30`, verde medio `#265C4B`, beige `#C2A78B`, fondo crema `#FDFCFA`, tipografía Barlow Condensed. Sobria, casi monástica. Sin ilustraciones cute, sin emojis, sin íconos motivacionales.
- **Público:** adultos, mayoritariamente mujeres 25-50 años, con cuadros de ansiedad, dependencia emocional, burnout, autoexigencia. Secundariamente: padres y madres de adolescentes (talleres). Terciariamente: equipos profesionales (Método MindShift, in-company).
- **Tuteo siempre.** Nunca usted.

### Lo que TWIM **no** es (y conviene tener escrito)

Esto es más útil que lo que sí es. Los líneas rojas:

- **No** es un proyecto de coaching. Aunque el embudo se parezca, el contenido nunca debe sonar a "tú puedes con esto".
- **No** es un proyecto de "salud mental positiva". Nada de "merece amor", "eres suficiente", "agradece más". Esa estética está prohibida en todos los textos.
- **No** es una marca de psicología pop. Aunque el lenguaje se traduzca, los conceptos psicoanalíticos quedan visibles. La promesa al lector es: *"vas a entender tu mecanismo, no vas a recibir consejos"*.
- **No** es solo Daniel-influencer. Es Daniel-clínico. La autoridad viene del CV11515 y de los años de consulta, no del crecimiento de seguidores.
- **No** es una empresa que use testimonios de pacientes. El briefing del programa "Deja de Buscarte en Otros" lo dice explícito: política firme de no pedir testimonios. Solo casos clínicos anonimizados o citas de investigación.
- **No** es una marca que comprometa el secreto profesional para vender. Esto va a tensionar repetidamente, especialmente cuando entren consultoras de marketing recomendando "vídeo testimonio". La respuesta correcta es siempre no.

### El tono de voz, en una sola frase

> **"Describir el mecanismo, ofrecer una herramienta, no juzgar nunca."**

Y tres ejemplos reales de cómo eso suena (extractos del briefing del programa, no inventados):

1. *"El «tengo que» no es solo una idea: es un modo automático. Aparece un disparador → tu mente lanza una urgencia → tu cuerpo se activa → actúas → algo se calma."*
2. *"Hay una escena que se repite en silencio. Por fuera cumples, entregas, resuelves. Por dentro algo no encaja. No es modestia. Es un desajuste que aprieta."*
3. *"Necesitar validación no es vanidad. Es un sistema interno que aprendiste para regular tu malestar. Y como cualquier sistema, tiene una lógica que se puede entender."*

Esta voz ya existe. No hay que reinventarla. **Hay que protegerla** cuando empieces a contratar redactores externos, asistentes virtuales, agencias o cuando un anuncio de Meta empuje a "hacerlo más comercial".

### Cultura interna (lo que aún no existe pero conviene definir este fin de semana)

TWIM, hoy, eres tú + Claude + algunas herramientas. Pero ya hay decisiones de cultura que se cristalizan en los documentos internos:

- **Sin secretos en el repo.** Las credenciales van a `.env.audit` (gitignored). CLAUDE.md tiene anotado que hay tokens expuestos pendientes de rotar — eso es deuda técnica con riesgo real, no folklore.
- **Documentación viva.** Los briefings (`BRIEFING-*.md`, `PLAN-*.md`) son la memoria del proyecto. Cada cambio importante deja rastro. Esto es lo que permite que mañana otra persona pueda continuar sin sesión-tras-sesión de onboarding.
- **Trabajar por bloques pequeños y commits limpios.** Esto está literalmente en CLAUDE.md como instrucción de generación de archivos. No es manía — es lo que evita que un fallo intermedio destruya horas de trabajo.

---

## 3 · El producto editorial (artículos + cartas + carruseles)

Mucha gente confunde "tener un blog" con "tener un producto editorial". TWIM ya pasó esa línea hace tiempo. Hay 27 artículos publicados con voz consistente, una newsletter en lanzamiento, carruseles de Instagram producidos como pieza editorial (no como reactivos), un libro impreso. Esto **es** un producto editorial.

### 3.1 · Pilares temáticos detectables (los que ya existen)

Mirando los 27 artículos publicados, los temas se agrupan en cuatro racimos. Esto no se decidió en pizarra — emergió. Tu próxima decisión de contenido debería respetar estos racimos o crear deliberadamente uno nuevo.

| Racimo | Artículos representativos | Lectura clínica del racimo |
|---|---|---|
| **Dependencia emocional / validación externa** | dependencia-emocional-como-dejar-de-depender, idealizacion-devaluacion-pareja, por-que-necesitas-que-te-validen, senales-dependencia-emocional, articulo-vacio-idealizacion | Es el racimo con producto digital ya construido (programa "Deja de Buscarte en Otros"). El embudo y los textos están alineados. |
| **Autoexigencia / juez interno / urgencia mental** | juez-interno-como-desactivar, urgencia-mental-frenarla-120-segundos, tecnica-2-minutos-rumiacion, sindrome-del-impostor, del-deberia-al-quiero-ejercicios, como-dejar-de-hacer-las-cosas-por-obligacion | Es el racimo más visitado y compartido. Aquí está el "Reto 7 días" como lead magnet y el programa "Rompe el TENGO QUE" en preventa. |
| **Malestar laboral / burnout / sentido del trabajo** | senales-trabajo-te-enferma, malestar-laboral-trabajas-para-otro-mapa-completo, sobrevivir-jornada-laboral-sin-desconectarte, ansiedad-productiva-presion-creatividad, deberia-dejar-trabajo-malestar, obediencia-trabajo-casa | Tiene landing SEO (`psicologo-burnout-valencia.html`) y carrusel ("cansancio psíquico"). Falta cerrar producto digital propio — es la siguiente oportunidad clara. |
| **Adolescencia / TDAH / crianza** | hijo-no-es-vago-apatia-bachillerato, tdah-adolescentes-autoestima-lo-que-las-notas-no-dicen | Solo dos artículos. Hay dos talleres con landing pero **el blog está casi vacío** para este público. El propio briefing PLAN-TALLERES-ADOLESCENCIA.md detectó esto como debilidad crítica. |

### 3.2 · La pregunta editorial que hay que responder

El catálogo está repartido en cuatro racimos pero **el embudo activo solo trabaja uno** (autoexigencia → reto 7 días → programa dependencia). Esto crea dos posibles caminos:

- **Camino A (concentración):** doblar la apuesta en el racimo de autoexigencia/dependencia. Cerrar el programa "Rompe el TENGO QUE", construir embudo paralelo al del Reto 7 días, dejar burnout y adolescencia en modo SEO pasivo durante 6 meses.
- **Camino B (expansión):** abrir un segundo embudo de burnout (lead magnet propio, secuencia email propia, producto propio) en paralelo al de autoexigencia. Ganarías diversificación de tráfico pero duplicarías la complejidad operativa.

Ninguno es objetivamente mejor. Pero la decisión es **tuya y de este fin de semana**. Está apuntada en la sección 7.

### 3.3 · La newsletter "Te escribo" como columna vertebral

Lo que ya está montado (extraído de PLAN-LANZAMIENTO-5-MAYO.md y PLAN-CAPTACION-30D.md):

- Carta #1 "esto es lo que vas a recibir" → programada para martes **5 mayo 19:00 CET**, audiencia ~24 personas (Reto + Lead Magnet + Lista General).
- Carta #2 "La voz que te juzga" → programada para martes **19 mayo 19:00 CEST**.
- Carrusel #1 "cansancio psíquico" → programado IG/LinkedIn mismo día Carta #1.
- Carrusel #2 "saberlo no te lo quita" → producido, pendiente publicar semana 2.
- Cross-sell "Te escribo" añadido a las 7 landings SEO con copy específico por síntoma de la página.
- Exit-intent modal en las mismas 7 landings.
- GA4 events `newsletter_signup` y `newsletter_modal_shown` cableados.
- Objetivo declarado: **200 suscriptoras netas en mes 1** al grupo `Web - Newsletter Home`.
- Gate Meta Ads condicional (semana 4): si a 21 mayo hay <150, se activa con 25-35 € de test. Si hay ≥150, se queda en orgánico puro.

Lo que esto significa en lenguaje de CEO:

> **"Te escribo" no es 'un boletín más'. Es el activo de marca que te separa de los 50.000 psicólogos que tienen Instagram.** Las cartas son el producto. Los emails secundarios son distribución. El embudo del Reto 7 días es captación. La consulta paga las facturas. El programa digital es el primer escalón monetizable. La newsletter es el lugar donde construyes audiencia que dura años, no clicks que duran días.

Si en algún momento te toca priorizar entre escribir una carta y configurar un anuncio, prioriza la carta. Los anuncios se delegan; la voz no.

### 3.4 · El libro como activo dormido

*Los engranajes de la mente* está publicado en Amazon. En el repo hay un directorio `libro-engranajes-mente/` con un `index.html` (mínimo). En el README se enlaza al ASIN. Pero:

- No hay embudo desde el libro a la newsletter (lectores que terminan el libro no entran en "Te escribo").
- No hay landing rica del libro en `twimproject.com/libro` con extracto, índice, reseñas, capítulo gratuito.
- No hay automatización post-compra (Amazon no entrega el email del comprador, pero sí puedes usar QR en últimas páginas / dedicatoria que lleve a una landing).

**Acción recomendada:** este es uno de los activos con mayor ROI/esfuerzo. Convertirlo de "libro publicado" a "puerta de entrada al ecosistema TWIM" es trabajo de 2 semanas y multiplica la utilidad del libro durante años.

---

## 4 · Catálogo de ofertas y arquitectura del embudo

### 4.1 · Lo que vendes hoy (o estás a punto de vender)

Inventario real al 30-04-2026, con su estado de producción y monetización:

| Oferta | Tipo | Estado | Precio | Motor de captación |
|---|---|---|---|---|
| **Consulta privada** (Valencia + online) | 1:1 clínico | Operativo desde 2012 | ~70-90 €/sesión (estándar mercado VLC) | Boca-oreja + SEO local + landings SEO recién publicadas |
| **Deja de Buscarte en Otros** | Programa digital autoguiado | Listo (briefing + materiales) | 79 € (lanzamiento 49 €) | Reto 7 días → secuencia 8 emails → CTA en email D7 |
| **Rompe el TENGO QUE** | Programa digital autoguiado | Preventa (`rompetengoquepreventa.html`) | Pendiente | Pendiente |
| **Deja de obligarte** | Programa digital autoguiado | Landing pública (`dejadeobligarte.html`) | Pendiente | Pendiente |
| **Taller TDAH adolescentes** | Grupal presencial / híbrido | Landing pública | Pendiente publicar precio | Cero captación activa hoy |
| **Taller bachillerato motivación** | Grupal presencial / híbrido | Landing pública | Pendiente publicar precio | Cero captación activa hoy |
| **Taller "No puedo parar"** | Grupal | Landing setup en marcha | Pendiente | Pendiente |
| **Método MindShift / In-Company** | B2B corporativo | Mencionado en home + PDF (`Programa_In-Company_Info.pdf`) | A medida | Cero pipeline declarado |
| **Libro "Engranajes de la mente"** | Físico/Kindle | Publicado en Amazon | Precio Amazon | Cero captación inversa hacia web |
| **Newsletter "Te escribo"** | Gratuito (activo de audiencia) | Lanzamiento formal 5 mayo | Gratis | Cross-sell SEO + exit-intent + carruseles + email |

### 4.2 · Mapa del embudo activo (lo único que está medible y vivo hoy)

```
       Instagram orgánico  ──┐
                              │
       Instagram Ads (en      │
       configuración hoy) ────┤
                              ▼
                      Carrusel "El sobrepensar"
                              │
                              ▼
              twimproject.com/reto-7-dias.html
                              │
                       (form sin WhatsApp, Pixel activo,
                        evento Lead disparando)
                              │
                              ▼
                      MailerLite · Grupo "Reto 7 Días"
                              │
                              ▼
                  Secuencia de 8 emails (D0–D7)
                              │
                              ▼
                  Email D7 · CTA programa "Deja de Buscarte en Otros"
                              │
                              ▼
                       Compra (Stripe)
```

Esto **funciona**. La conversión email → CTA es del 20%, lo que en infoproducto es altísimo. El cuello de botella **no está dentro del embudo**: está en el grifo de arriba. La pregunta no es "¿cómo mejoro el embudo?" sino "¿cómo le abro más la llave?".

### 4.3 · Lo que está construido pero aún no enchufado

- Landing del programa "Rompe el TENGO QUE" en preventa, sin embudo de captación dedicado.
- 2 talleres adolescencia con landings pero **sin formulario propio** (solo mailto), sin lead magnet para padres, sin cluster editorial dirigido a padres. El briefing PLAN-TALLERES-ADOLESCENCIA.md detectó esto explícitamente como funnel roto.
- Programa "Deja de obligarte" con landing pública sin embudo.
- 2 automations talleres (TDAH y bachillerato) creadas en MailerLite pero **pendientes de activar** (en el `PLAN-CAPTACION-30D.md` aparece como tarea manual pendiente para Daniel).

### 4.4 · La arquitectura ideal a 6 meses (propuesta)

```
                      ┌─── consulta privada (cash flow base)
                      │
   Tráfico orgánico ──┼─── newsletter "Te escribo" (audiencia)
   (SEO + IG + LK)    │         │
                      │         ├──→ programa autoguiado #1 (dependencia)
                      │         ├──→ programa autoguiado #2 (autoexigencia)
                      │         └──→ taller en directo (1-2 al año, alto ticket)
                      │
   Tráfico pagado ────┘
   (Meta Ads cuando
    el orgánico ya
    cualifica)
```

El cambio clave respecto al hoy: **dejar de tener "muchas ofertas con embudos rotos"** y pasar a "una infraestructura única donde todo se alimenta de la newsletter". La newsletter pasa de ser una pieza más a ser el **eje del modelo**.

---

## 5 · Mercado, competencia y posicionamiento real

> Nota honesta: no he podido sacar datos de Ahrefs en esta sesión (plan limitado). Los benchmarks de mercado de abajo vienen de conocimiento general del sector psicología digital en España al 2025-26 y de cómo se posicionan los referentes públicos. Cuando recuperes acceso a Ahrefs/SEMrush, vale la pena auditarlos con número en mano.

### 5.1 · El mercado en el que juegas

El mercado "psicología online en español" está saturado y, a la vez, mal cubierto. Conviven cuatro grandes tipos de actores:

1. **Plataformas tipo marketplace** (Mundopsicologos, ifeel, TherapyChat). Compiten por SEO de cabeza ("psicólogo online", "ansiedad"). Tienen presupuesto de Ads. No te puedes pelear contra ellos en su terreno.
2. **Coaches con marca personal grande** (figuras tipo Marian Rojas, Patricia Ramírez). Colonizan el espacio "salud mental positiva". Audiencia masiva pero poco profundidad. Es la antítesis estética de TWIM — y eso es una ventaja, no un problema.
3. **Psicólogos con consulta + presencia digital media** (cientos en cada ciudad). Hacen lo que hace todo el mundo: web informativa, Instagram con frases motivacionales, captación por boca-oreja y SEO local. Es el lugar del que quieres salir, no en el que quieres quedarte.
4. **El espacio raro: clínico-editorial-profundo** (poca gente, mucha demanda no atendida). Aquí caben perfiles tipo Massimo Recalcati en Italia, Lori Gottlieb en EEUU, Jorge Bucay (otra época, otro registro), o cuentas como Aitor Sánchez García en nutrición — referentes de "rigor profesional + voz editorial fuerte". **Este es el sitio donde TWIM Project se está construyendo.**

### 5.2 · Tu posicionamiento real (no el aspiracional)

A día de hoy, si alguien te describe en una frase sin marketing por medio, dice:

> *"Es un psicólogo de Valencia que escribe en serio y no dice tonterías motivacionales."*

Eso es **enorme**. Es exactamente la promesa que la mayoría no puede cumplir. Tres palabras importan ahí: *"escribe en serio"* (autoridad editorial), *"no dice tonterías"* (anti-coaching), *"de Valencia"* (cuerpo, lugar, persona real, no un avatar de Instagram).

El trabajo de los próximos 12 meses no es cambiar ese posicionamiento. Es **amplificarlo** sin diluirlo cuando el embudo empiece a escalar.

### 5.3 · Quién más respira aire similar

Sin orden particular y sin afán exhaustivo, son referentes del mismo aire (no son enemigos — son el mapa de la categoría):

- **Anabel González** (psiquiatra, libros sobre dependencia emocional / EMDR). Voz clínica seria, con audiencia construida por libros más que por redes.
- **Borja Vilaseca** (no es psicólogo pero tiene un público adyacente). Modelo de negocio editorial-formativo de referencia, aunque su tono no encaja con el tuyo.
- **Miguel Silveira** (psiquiatra, contenido de TDAH adolescente). Más cercano al pilar de adolescencia que tienes flojo.
- **Gabriel Rolón** (psicoanalista argentino). Marca editorial muy potente, libros de referencia, aire psicoanalítico aplicado parecido al tuyo.
- **Massimo Recalcati** (psicoanalista italiano). El "techo" del posicionamiento clínico-editorial-mainstream. Probablemente inalcanzable a corto, pero es buena coordenada.

Lo importante no es competir con ellos. Es **estudiar cómo construyen autoridad** y qué piezas usan: libros, cursos, columnas regulares, conferencias, formación.

### 5.4 · Donde sí compites cabeza con cabeza

Cuando alguien busca en Google "psicólogo dependencia emocional Valencia" o "psicólogo burnout Valencia", **sí** estás en una pelea local con 20-40 consultas privadas. Ahí las landings SEO recién publicadas son tu artillería. Pero ojo: el SEO local en psicología tarda **6-12 meses** en estabilizarse. No esperes ranking visible antes de septiembre 2026.

### 5.5 · Lo que el mercado te pide y aún no le das

Tres demandas claras del público objetivo, observables sin hacer un estudio formal:

- **Padres y madres con hijos adolescentes en Valencia** que buscan ayuda y no encuentran nada que no sea publicidad de academias. Los dos talleres están listos. Falta el racimo editorial (3-6 artículos sobre adolescencia/TDAH/motivación) y el lead magnet para padres.
- **Mujeres profesionales 30-45 con burnout que no saben que es burnout.** Esta gente busca "estoy cansada todo el tiempo", "no tengo ganas de nada", "me cuesta mucho ir a trabajar". El racimo editorial existe. Falta producto digital propio (un programa "Burnout: leer el cansancio" o similar) que cierre el embudo como hace "Deja de Buscarte en Otros" con dependencia.
- **Hispanohablantes en LatAm y EEUU** que buscan psicólogos con autoridad clínica y consulta online. La landing `psicologo-online.html` apunta ahí. Si la newsletter "Te escribo" arranca bien, el siguiente paso natural es abrir un nicho LatAm con producto propio en pesos / dólares.

---

## 6 · La realidad hacia la que tienes que mirar (12 meses)

Este es el bloque más importante. Léelo dos veces.

### 6.1 · El supuesto base — qué pasaría si no cambias nada

Si los próximos 12 meses son una continuación lineal del mes pasado, llegarás a:

- 200-400 suscriptores en MailerLite (sumando newsletter + lead magnets).
- 7-15 ventas del programa "Deja de Buscarte en Otros" (~500-1.000 € de ingresos del programa).
- 3-6 talleres adolescencia llenos (~2.000-4.000 € si cobras 300-400 €/plaza × 6-12 plazas).
- Consulta privada estable — fuente principal de ingresos.
- Marca creciendo lentamente, sin tracción notable en redes ni en búsqueda.

Esto es **un buen año personal** pero **un mal año de negocio**. Mantiene la consulta llena pero no construye un activo escalable. El TWIM de 2027 sería casi indistinguible del TWIM de 2026.

### 6.2 · El supuesto ambicioso — qué pasaría si en 12 meses TWIM se convierte en marca editorial real

Hipótesis: te ordenas para que la newsletter sea el centro y todo lo demás la alimente. Cuál sería la foto a 30 abril 2027:

- **Newsletter "Te escribo"**: 2.500-4.000 suscriptoras activas. Open rate sostenido >40%. Carta cada 2-3 semanas, sin saltarse el ritmo. **Esto es la base de todo lo demás.**
- **Catálogo digital**: 3 programas vivos (*Deja de Buscarte en Otros*, *Rompe el TENGO QUE*, un programa de burnout/cansancio psíquico). 50-150 ventas anuales acumuladas → 4.000-12.000 € de programas.
- **Talleres**: 3-4 ediciones de talleres adolescencia (TDAH + bachillerato), llenos (12 plazas cada uno). + posiblemente 1-2 talleres en directo para adultos vinculados a programas (formato "carta + sesión Zoom + PDF").
- **In-Company / Método MindShift**: 1-3 contratos al año. Ticket medio 3.000-8.000 €. Esto se construye con LinkedIn, no con Instagram.
- **SEO local Valencia**: top 5 para "psicólogo dependencia emocional Valencia", "psicólogo burnout Valencia". Esto trae 2-5 primeras consultas/mes adicionales.
- **Libro**: segunda obra en preparación o publicada. Idealmente con editorial conocida (Paidós, Anagrama, Plataforma) en lugar de autopublicación, porque la editorial **es** una herramienta de distribución y autoridad.
- **Equipo**: ya no eres tú solo. Tienes (mínimo) una asistente virtual a tiempo parcial gestionando publicación de carruseles, programación de emails, atención al cliente del programa, agenda de Calendly. **5-10 horas/semana liberadas para hacer lo único que solo tú puedes hacer: escribir y atender pacientes.**

### 6.3 · Las 5 palancas que mueven todo

De todo lo que podrías hacer, son cinco las que mueven la aguja de verdad. El resto es ruido (o efecto secundario de estas).

1. **Volumen de la newsletter.** Cada suscriptor cualificado vale 5-50 € de LTV en este modelo. Llegar a 2.000 suscriptores antes de fin de año es la palanca #1. Todo el resto (más artículos, más Ads, más carruseles) es subordinado a eso.
2. **Cierre del segundo programa monetizable** (probablemente el de burnout / cansancio psíquico, dado que ya tienes el racimo editorial maduro). Hoy tienes UN producto digital que se vende — eso te hace dependiente de un solo embudo.
3. **Activar el activo dormido del libro.** Embudo desde Amazon a la newsletter (QR + landing dedicada del libro + capítulo gratuito a cambio de email). Es una conversión barata: gente que ya pagó por leerte es la mejor candidata para "Te escribo".
4. **Construir el racimo editorial de adolescencia/padres.** Sin esto, los dos talleres no se van a llenar nunca de forma orgánica. Y los talleres son ingresos altos (300-500 €/plaza × 6-12 plazas) cuando funcionan.
5. **Delegar ejecución, blindar la voz.** Antes de fin de año tienes que dejar de ser tú quien sube los carruseles, programa los emails, configura los Pixels. Esto no es "lujo" — es lo único que evita el burnout del propio Daniel y libera el tiempo que necesita para escribir y consultar.

### 6.4 · Lo que ya no es posible negar

- **Instagram orgánico solo no escala.** Llevas tiempo publicando y los suscriptores siguen siendo 30. Instagram cumple un papel (presencia, prueba social, atención inicial) pero no es el motor de captación. El motor tiene que ser, en orden de prioridad: SEO + newsletter + Meta Ads + LinkedIn (para B2B / In-Company).
- **Sin pago hay límites duros.** Hay un mito en el mundo psicología-creator de que "si haces buen contenido, el tráfico llega". Es verdad solo a 3-5 años vista y con suerte. Si quieres ver tracción en 12 meses, **necesitas presupuesto de Meta Ads sostenido**, no solo el test de 6 €/día de esta semana.
- **El tiempo es el recurso escaso, no el dinero.** El cuello de botella no es presupuestario — es que tú haces todo. Cualquier inversión que libere tu tiempo (asistente, agencia para el SEO técnico, alguien que diseñe los carruseles) tiene ROI mucho mayor que cualquier inversión en herramientas o cursos.

---

## 7 · Las 3 decisiones que tienes que tomar este fin de semana

No son las únicas decisiones pendientes. Son las tres que **bloquean** el resto del trabajo. Si las dejas abiertas, lunes por la mañana volvemos al modo "operador de Ads Manager" y nada se mueve realmente.

### Decisión 1 — ¿Concentración o expansión de embudos?

**Pregunta:** ¿Vas a doblar la apuesta en el embudo de autoexigencia/dependencia (camino A) o vas a abrir un segundo embudo de burnout en paralelo (camino B)?

- Camino A — Concentración. Próximos 6 meses: Reto 7 días + programa "Deja de Buscarte en Otros" + cerrar y lanzar "Rompe el TENGO QUE" como segundo producto del mismo embudo. Burnout y adolescencia quedan en SEO pasivo. Pro: foco brutal, una sola promesa que aprender a vender. Contra: dependencia de un solo público.
- Camino B — Expansión. Próximos 6 meses: mantener el embudo actual + abrir un embudo paralelo de burnout (lead magnet propio + secuencia + producto digital). Pro: diversificación. Contra: duplicas la operación con la misma persona haciendo todo.

**Recomendación honesta:** camino A. Estás en una fase donde **la disciplina vale más que la diversificación**. Cuando la newsletter pase de 1.000 suscriptores y haya un asistente liberándote 5h/semana, abres camino B sin sufrir.

### Decisión 2 — ¿Cuánto presupuesto mensual para Meta Ads en los próximos 6 meses?

**Pregunta:** ¿6 €/día (180 €/mes), 15 €/día (450 €/mes) o 30 €/día (900 €/mes)?

- 6 €/día. Es lo que estás a punto de configurar. Sirve para validar que el embudo convierte con tráfico pagado. **No sirve para escalar.** Es un cinturón de seguridad, no un motor.
- 15 €/día. El nivel donde empiezas a ver datos suficientes para optimizar (>50 conversiones/mes). Te permite probar 2-3 audiencias y 2-3 creatividades en paralelo. Probablemente el nivel correcto para mes 2-3.
- 30 €/día. Aquí ya estás escalando de verdad. Tiene sentido si la newsletter cruza 500 suscriptores y validas que CPL ≤ 2 €.

**Recomendación honesta:** empezar en 6 €/día durante 2 semanas (lo que estás haciendo). Si en 14 días tienes ≥10 leads y CPL ≤ 4 €, subir a 15 €/día. Si los números aguantan, en 60 días subir a 30 €/día.

> Esta decisión no se cierra del todo este fin de semana — depende de los datos del primer test. Pero **sí** tienes que cerrar este fin de semana el principio: *"voy a financiar Meta Ads hasta X €/mes durante 6 meses como inversión de marca, no como gasto de marketing"*.

### Decisión 3 — ¿Cuándo contratas la primera asistente virtual?

**Pregunta:** ¿Junio, septiembre o "cuando los ingresos lo justifiquen"?

- Junio (ya). Costaría 200-400 €/mes (10-15h/semana, perfil VA hispanohablante). Liberaría inmediatamente: programación de carruseles, reposting, atención de mensajes IG/email, gestión de calendario, primera línea de soporte de programas.
- Septiembre (post-verano). Tiene la ventaja de esperar a tener los datos del primer trimestre del lanzamiento serio.
- "Cuando los ingresos lo justifiquen". Trampa clásica del solopreneur. Los ingresos **nunca** lo justifican antes de tiempo, porque no hay tiempo libre para producir más.

**Recomendación honesta:** junio. La inversión es baja, el ROI inmediato es alto (no en dinero — en tu tiempo y tu cabeza). El criterio no es "tengo dinero para pagarla" sino "qué dejaría de hacer yo si tuviera 10h libres a la semana". Si la respuesta es *"escribir la newsletter y atender pacientes"*, entonces la asistente vale la pena ya.

---

## 8 · Lo que NO debes hacer (lista corta de tentaciones)

Tan importante como decidir qué hacer es decidir qué **rechazar** activamente. Lista de tentaciones que van a aparecer en los próximos meses y que conviene tener vacunadas:

- **No abras un segundo embudo (burnout / adolescencia / consulta) hasta que el primero esté saturado.** Saturado significa: el Reto 7 días recibe ≥50 leads/mes orgánicos sin necesidad de Ads. Hoy no.
- **No grabes vídeos largos para YouTube.** Es el peor ROI/hora del mercado para un psicólogo individual. YouTube como canal funciona con 2-3 vídeos/semana sostenidos durante 18 meses. No tienes ese tiempo. Si quieres video, formato corto (Shorts/Reels) reciclando carruseles.
- **No aceptes entrevistas en podcasts pequeños solo por aparecer.** Cada entrevista cuesta 2-4 horas (preparación + grabación + repromoción). Acéptalas solo si la audiencia del podcast es ≥10× tu newsletter o si el host es alguien con quien quieres construir relación a largo plazo.
- **No contrates "agencia de marketing" todavía.** Mes 6.000-2.000 € que se evaporan haciendo lo que ya estás haciendo tú con Claude. Las agencias funcionan cuando ya tienes producto, embudo y datos. Tú tienes lo dos primeros, no el tercero.
- **No compres cursos de "cómo escalar tu consulta".** Has visto y vas a ver muchos. Lo que enseñan tú ya lo sabes (o está en este documento).
- **No aceptes pedidos del público para hacer un grupo terapéutico online ahora.** Es atractivo, parece "fácil" porque ya hay demanda, pero te ata a horarios fijos y te roba el tiempo de escribir. Postergar a 2027 mínimo, cuando haya 1.000+ suscriptores que justifiquen un grupo selectivo.
- **No publiques en LinkedIn por publicar.** O activas LinkedIn como canal real para B2B / In-Company (1 post largo/semana sostenido), o lo dejas dormido. Lo intermedio es ruido.
- **No cambies la voz editorial al recibir crítica.** Habrá gente que te diga "es muy serio", "no eres lo suficientemente cercano", "te falta calidez". Esa gente no es tu público. Tu público es la persona que siente que **por fin alguien le habla en serio**.

---

## 9 · Riesgos vivos y deuda silenciosa

No son urgentes esta semana, pero conviene no perderlos de vista.

### 9.1 · Riesgo de seguridad / cumplimiento

- **Token Netlify expuesto pendiente de rotar.** En CLAUDE.md está marcado: `nfp_Fe7FsD3Uv9UtsLmz9broLYSad2PKqh9E4d2e`. Cualquiera con ese token podría desplegar en tu site. Tarea de 5 minutos: ir a `https://app.netlify.com/user/applications`, revocar, generar uno nuevo, actualizar `.env.audit`.
- **MFA (2FA) en Netlify desactivado.** Mismo nivel de prioridad. 5 minutos.
- **No hay copia de seguridad declarada de la lista de MailerLite.** 30 suscriptores hoy; pronto serán 2.000. Cuando seas dependiente de esa lista, si pierdes acceso a la cuenta o ML cierra una funcionalidad, te quedas en cero. Buena práctica: exportar la lista a CSV una vez al mes y guardarla cifrada en una carpeta local + cloud.
- **Posibles cuestiones LOPD/GDPR del Pixel + email marketing**. Tu política de privacidad existe (`privacy.html`) — vale la pena revisarla anualmente con un texto actualizado para Pixel de Meta + Google Analytics. No es urgente, pero pasa de "no urgente" a "muy urgente" el día que recibes una reclamación.

### 9.2 · Riesgo operativo

- **Solo Daniel sabe el sistema entero.** Si te caes 2 semanas, el embudo sigue corriendo (porque está automatizado), pero no se publica nada nuevo en redes ni en blog ni en newsletter. Esto se resuelve con una asistente y con la documentación viva (los `BRIEFING-*.md`, `PLAN-*.md`).
- **MailerLite es proveedor único.** Lock-in moderado. Si hubiera un problema, migrar la automation de 8 emails + plantillas + segmentaciones puede llevar semanas. Mitigación: documentación de qué hace cada automation (algo de eso ya existe).
- **Netlify es proveedor único.** Lock-in bajo (es HTML estático), migración relativamente fácil. No prioridad.

### 9.3 · Riesgo de marca

- **Mezcla de etiquetas viejas y nuevas en el repo.** El propio README dice "GitHub Pages" cuando ya estás en Netlify. Y aún hay textos sueltos con "más de una década" en lugar de "desde 2012", o con "orientación psicoanalítica" en lugar de "Psicología Profunda y Aplicada" si te toca revisar HTML antiguo. No es urgente individualmente; sí es un goteo que conviene auditar trimestralmente.
- **README desactualizado.** Si alguien (un colaborador, un asistente, otro psicólogo que quiera referirte) entra al repo, lo primero que lee es texto antiguo. 30 minutos de actualización lo corrigen.

### 9.4 · Deuda editorial

- **Cluster adolescencia casi vacío.** 2 artículos de 27. Si quieres llenar talleres, esto se ataca primero.
- **Sin caso clínico anonimizado publicado todavía.** Es la única forma legítima de prueba social en tu marco. Vale la pena tener al menos 3-4 casos anonimizados publicados antes de fin de año, distribuidos por los racimos editoriales.
- **Sin página rica del libro.** El libro merece su propia landing en `twimproject.com/libro` con índice, capítulo gratuito a cambio de email, reseñas, link a Amazon. Hoy no existe.

---

## 10 · Apéndice — métricas y benchmarks que vale la pena vigilar

Una sola pestaña, una vez por semana (lunes por la mañana, 15 minutos). Si dedicas más de eso a mirar métricas, estás procrastinando.

### Métricas semanales (cada lunes)

| Métrica | Fuente | Cota saludable mes 1-3 | Cota objetivo mes 6 |
|---|---|---|---|
| Suscriptores netos nuevos en MailerLite | ML dashboard | +30/semana | +100/semana |
| Open rate Carta semanal "Te escribo" | ML | ≥40 % | ≥45 % |
| Click rate Carta → web | ML | ≥5 % | ≥8 % |
| Unsubscribe rate Carta | ML | <1 % | <0,5 % |
| Visitas únicas a `/reto-7-dias` | GA4 | ≥150/semana | ≥500/semana |
| Conversión visitante → lead Reto | GA4 | ≥5 % | ≥8 % |
| Visitas a las 7 landings SEO | GA4 | aún 0 (Google indexa lento) | ≥800/semana en agregado |
| Ventas Stripe del programa | Stripe dashboard | 0-2/semana | ≥5/semana |

### Métricas mensuales (primer lunes de cada mes)

- **CPL Meta Ads** (gasto / leads). Cota mes 1: ≤4 €. Cota mes 6: ≤2 €.
- **LTV estimado por suscriptor** (ingresos del mes / suscriptores totales). Empieza calculándolo aunque sean 5 €. Es la única forma de justificar inversión en captación.
- **Ingresos por canal**: consulta privada / programa digital / talleres / in-company. Saber de dónde viene cada euro es lo que permite tomar decisiones de dónde invertir en el siguiente trimestre.

### Benchmarks de referencia (psicología digital española / hispanohablante)

> Aproximaciones, no datos auditados. Sirven como suelo para no asustarse y techo para no celebrar de más.

- Open rate medio newsletter de psicólogos con voz fuerte: 35-45 % (TWIM hoy: 51-70 % en grupo Reto, lo que indica una promesa muy bien cumplida).
- Conversión visitante → lead en landing de lead magnet de psicólogo: 2-5 % (TWIM histórico: 0,33 % — muy bajo, esperable que suba a 5-8 % con el rediseño y Pixel).
- CPL Meta Ads para lead magnet psicológico en España: 2-6 €. Lo que esté por debajo de 2 € es excelente; por encima de 6 € hay que rotar creativo o audiencia.
- Conversión email → compra de programa de bajo ticket (≤100 €): 2-5 % (TWIM: el 20 % de CTR en email D7 sugiere que la conversión a venta podría rondar 3-8 %, todavía por validar con volumen).
- Ratio entre suscriptores de newsletter y compradores anuales del programa estrella: 5-10 %. Es decir, 1.000 suscriptores → 50-100 ventas/año.

### Cómo leer estos números sin enloquecer

Tres reglas:

1. **Mide cada lunes, no cada día.** Las métricas diarias son ruido. Las semanales son señal.
2. **Compara contigo mismo, no con benchmarks.** El benchmark sirve para situarse, no para juzgarse. Si la semana 12 está mejor que la 11, va bien — independientemente de lo que haga la industria.
3. **Si una métrica empeora 2 semanas seguidas, investiga. Si mejora 2 semanas seguidas, no toques nada.** El instinto de "optimizar" cuando algo funciona es una de las formas más comunes de romperlo.

---

## Cierre

TWIM Project no es lo que era hace 6 meses. Tampoco es lo que va a ser dentro de 12. Estás en un punto raro y poco glamuroso: el que hay entre "esto funciona técnicamente" y "esto funciona económicamente". La mayoría de proyectos editoriales se rompen en este punto exacto, no por falta de talento sino por dispersión.

Lo único que te separa de un negocio editorial-clínico de referencia en español es **disciplina sostenida durante 12-18 meses** sobre las cinco palancas de la sección 6.3 y las tres decisiones de la sección 7. Si los próximos 12 meses los dedicas a hacer lo correcto en lugar de a hacer mucho, el TWIM de 2027 va a ser irreconocible.

Y, sobre todo, recuerda lo que ya sabes en consulta y a veces se te olvida cuando estás operando el embudo:

> **No es urgencia. Es repetición.**

Buen fin de semana.

— Notas técnicas para Daniel: este documento se generó el 30-04-2026 a partir del estado del repo `theworldismindproject` en la rama `claude/seo-lead-funnel-AerVG`. Ahrefs no respondió por límite de plan, así que las cifras de mercado son aproximaciones del sector. Cuando vuelvas a tener acceso a Ahrefs/SEMrush vale la pena auditar las secciones 5 y 10. Para discusión, las preguntas concretas están en las decisiones de la sección 7.

