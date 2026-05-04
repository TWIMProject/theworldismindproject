# NotebookLM · Infraestructura interna de TWIM

> Documento interno · 4 mayo 2026
> Doc #4 de la serie de stack de producción audio + vídeo.
> Complementa: anexo CEO stack audio+vídeo (doc #1), ElevenLabs clonación de voz (doc #2), YouTube + Podcast estrategia de canal (doc #3), reciclaje pipeline (doc #5 pendiente).
> Cuando Daniel pregunte sobre NotebookLM, organización de fuentes editoriales, o onboarding de Sergio/VA, abrir este documento.

---

## TL;DR

- **Qué es NotebookLM en TWIM:** herramienta de Google (gratis al 4-may-2026) para organizar fuentes editoriales propias y generar estructura de partida (esquemas, FAQ, párrafos de transición) para podcast, carruseles, cartas y onboarding de colaboradores.
- **Política dura inviolable:** NUNCA material clínico de pacientes en NotebookLM, ni siquiera anonimizado parcial. Solo material editorial propio (artículos del repo, libro, briefings, notas).
- **Notebooks a montar:** Marco editorial TWIM (onboarding Sergio + VA), uno por pilar (autoexigencia, dependencia, burnout, adolescencia), Libro Engranajes, y un notebook efímero por episodio de podcast.
- **Lo que SÍ hace:** organizar, resumir, conectar fuentes, generar estructura. Es un asistente de redacción, no un autor.
- **Lo que NO hace:** escribir con voz TWIM auténtica (siempre necesita edición editorial humana de Daniel), resolver dudas clínicas delicadas, sustituir lectura del material original.
- **Audio Overviews directos:** **NO se publican como podcast.** Para audio del podcast se usa el workflow del doc #2 (guion editorial Daniel + voz humana T1, ElevenLabs T2).
- **Coste:** 0 € hoy. Si Google introduce planes de pago, evaluar mantener Free vs subir a Pro.

---

## 1 · Política dura de privacidad clínica

Esta es la sección más importante del documento. Si una sola regla se rompe, el resto del sistema deja de ser defendible deontológica y legalmente.

### 1.1 · Regla absoluta

> **Nunca subir a NotebookLM (ni a ningún sistema cloud externo) material clínico de pacientes, ni anonimizado parcialmente.**

"Anonimización parcial" incluye:

- Cambiar el nombre pero mantener edad, profesión, ciudad, situación familiar.
- Redactar el caso "como si fuera otra persona" pero con detalles que permiten re-identificación a alguien del entorno cercano.
- Combinar elementos de un paciente real con elementos genéricos (mosaico identificable).
- Cualquier transcripción de sesión, aunque sea de una sola frase.

### 1.2 · Lo único que sí se permite

- **Casos compuestos** completamente sintéticos, construidos a partir de patrones clínicos genéricos descritos en literatura, sin referencia a ningún paciente real concreto.
- **Material editorial publicado o publicable**: artículos del propio repo, libro, briefings de programa, cartas "Te escribo", carruseles, notas editoriales propias.
- **Literatura de terceros con derechos correctos**: papers académicos, capítulos de libros con licencia adecuada, transcripciones de conferencias públicas.
- **Notas internas del equipo TWIM** sobre flujos operativos, calendarios, briefings — no clínico.

### 1.3 · Por qué la regla es tan dura

Tres razones:

- **Deontológica.** El secreto profesional del psicólogo (LOPS, código deontológico del COP) cubre cualquier contenido clínico, incluso anonimizado, si el paciente no ha dado consentimiento explícito por escrito para ese uso concreto. NotebookLM no es ese uso concreto.
- **Legal (RGPD).** Subir datos de salud (categoría especial, art. 9 RGPD) a un sistema cloud externo requiere base jurídica explícita. NotebookLM no la tiene como herramienta de Google general.
- **Práctica.** Aunque deontológica y legalmente fuera defendible (que no lo es), basta con que **el paciente se entere por su cuenta** para que se rompa la relación clínica y, peor, para que sea pasto de denuncia colegial.

### 1.4 · Regla operativa de chequeo

Antes de subir cualquier fuente a NotebookLM, Daniel se hace tres preguntas:

1. ¿Esta fuente está publicada en algún sitio (web, libro, newsletter) o sería publicable sin más permisos?
2. Si una persona del entorno cercano de cualquier paciente leyera esto, ¿podría identificar a un paciente concreto?
3. ¿Esto es material editorial mío (o de terceros con derechos correctos), o es material clínico?

Si la respuesta a (1) es no, o a (2) es sí, o a (3) es "clínico" — la fuente no entra a NotebookLM. Punto.

### 1.5 · Misma regla aplica a ElevenLabs

La regla 1.1 se extiende a ElevenLabs: el guion del podcast nunca contiene material clínico identificable. Esto ya se documenta en el doc #2 §1 (TL;DR) y §3 (workflow). Aquí se cierra el bucle: ni input editorial (NotebookLM) ni output audio (ElevenLabs) tocan material clínico.

---

## 2 · Notebooks recomendados

NotebookLM organiza el conocimiento por "notebooks" (proyectos) y cada notebook contiene "fuentes" (hasta 50 al 4-may-2026 en plan Free, ampliable en Pro). La estructura recomendada para TWIM:

### 2.1 · Notebook · Marco editorial TWIM

**Propósito:** onboarding de Sergio, futura VA, o cualquier colaborador editorial que entre al proyecto. Permite que en 1-2 horas alguien externo entienda quién es Daniel-clínico, qué publica TWIM, qué tono editorial se usa.

**Fuentes (5-10 documentos):**

- `CLAUDE.md` (reglas de generación + identidad editorial).
- `documentos-internos/ceo-vista-completa-v2-1-mayo-2026.md` (visión del negocio).
- `documentos-internos/ceo-anexo-stack-produccion-audio-video.md`.
- `documentos-internos/twim-clinic-modelo-derivacion.md`.
- `BRIEFING-ESTADO-ACTUAL.md`.
- 5-7 artículos representativos del repo (uno por pilar más alguno transversal).

**Output esperado:**
- Resúmenes para onboarding rápido.
- FAQ tipo "¿qué es TWIM?", "¿qué tono debe usarse?", "¿qué NO se hace?".
- Referencias cruzadas cuando un colaborador pregunta por un concepto y NotebookLM le indica en qué fuente está.

### 2.2 · Notebook · Pilar autoexigencia

**Propósito:** redacción y reciclaje de cualquier pieza editorial sobre autoexigencia.

**Fuentes:**
- Artículos del repo: `reto-7-dias.html`, `dejadeobligarte.html`, secciones relevantes de `index.html`, `psicologo-burnout-valencia.html` (intersección).
- Carrusel autoexigencia (`contenido-rrss/`).
- "Te escribo" carta #2 (autoexigencia).
- Capítulos del libro Los engranajes que tratan ideal yoico, mandato, culpa.
- Briefings internos relacionados.

**Output esperado:**
- Esquema de un nuevo episodio de podcast sobre autoexigencia.
- Borrador de un nuevo carrusel.
- FAQ sobre autoexigencia (útil también para SEO de las landings).

### 2.3 · Notebook · Pilar dependencia emocional

**Fuentes:** `dejadebuscarteenotros.html`, `BRIEFING-PROGRAMA-DEJADEBUSCARTE.md`, capítulos del libro sobre elección de objeto y repetición, cartas "Te escribo" relacionadas, carruseles relacionados.

### 2.4 · Notebook · Pilar burnout y ansiedad

**Fuentes:** `psicologo-burnout-valencia.html`, `psicologo-ansiedad-valencia/`, `nopuedoparar-taller.html`, carrusel cansancio psíquico, "Te escribo" carta #1, capítulos del libro sobre somatización y angustia.

### 2.5 · Notebook · Pilar adolescencia

**Fuentes:** `psicologo-adolescentes-valencia.html`, `PLAN-TALLERES-ADOLESCENCIA.md`, briefings de talleres adolescencia, capítulos del libro relevantes.

### 2.6 · Notebook · Libro Engranajes

**Propósito:** notebook dedicado al manuscrito completo del libro Los engranajes de la mente, accesible de forma transversal cuando se quiere citar el libro o reciclar fragmentos.

**Fuentes:** manuscrito completo (1 fuente o segmentado en capítulos según peso).

**Output esperado:** localización rápida de citas, reciclaje de fragmentos para podcast, carrusel o newsletter.

### 2.7 · Notebook efímero · por episodio de podcast

**Propósito:** organizar fuentes específicas de un episodio concreto. Vida útil: hasta que el episodio se publica + 1 mes (por si hay que actualizar derivados). Después se archiva o se borra.

**Fuentes (3-5 por notebook):**
- 1-2 artículos del pilar correspondiente.
- 1 fragmento del libro (cuando aplique).
- 1 briefing o carta relacionada.
- Referencias externas (papers, libros de terceros con derechos OK).

**Output esperado:** esquema de 5-7 puntos del episodio, FAQ, párrafos de transición. **Nunca redacción final del guion** — eso lo hace Daniel a partir del esquema.

### 2.8 · Política de notebooks

- **Máximo 7 notebooks "permanentes"** (1.1 a 1.6 + 1 transversal de marketing si hace falta). Más es ruido organizativo.
- **Los efímeros se archivan o eliminan** cuando el episodio publicado lleva 1 mes en distribución.
- **Una fuente puede estar en varios notebooks** (no hay limitación, NotebookLM no copia, indexa).
- **Cuando un artículo se actualiza en el repo, se reemplaza la fuente en el notebook**, no se añade duplicada.

---

## 3 · Workflows operativos

Los workflows son recetas reproducibles. Cada uno indica qué notebook usar, qué pedir a NotebookLM y qué hacer después con el output.

### 3.1 · Workflow A — Generar estructura de un episodio del podcast

1. Crear notebook efímero para el episodio (§2.7).
2. Subir 3-5 fuentes (artículo principal + briefing + fragmento libro + 1-2 fuentes externas con derechos).
3. Pedir a NotebookLM:
   - "Genera un esquema de 5-7 puntos para un episodio de podcast de 20 minutos sobre [tema], basado en estas fuentes."
   - "Identifica 5 preguntas frecuentes que un oyente podría tener sobre este tema, con la respuesta basada en las fuentes."
   - "Sugiere 3-4 párrafos de transición entre los puntos del esquema."
4. Revisión editorial Daniel (≈30 min): reescribir el esquema con voz TWIM, descartar lo que no cuadra, reordenar.
5. Output: esquema definitivo listo para redactar guion (paso 3 del workflow del doc #2 §3).

### 3.2 · Workflow B — Generar borrador de carrusel IG

1. Usar notebook del pilar correspondiente (§2.2-2.5).
2. Pedir a NotebookLM:
   - "Resume en 5-7 ideas concretas el concepto [X] basándote en las fuentes."
   - "Para cada idea, genera una frase de 8-12 palabras que pudiera ir en una slide de carrusel."
3. Revisión editorial Daniel: reescribir con voz TWIM, ajustar tono, validar que no hay positivismo tóxico ni clickbait.
4. Output: 5-7 frases candidatas para slides del carrusel (las slides finales se diseñan según sistema visual del PR #94).

### 3.3 · Workflow C — Generar borrador de carta "Te escribo" del newsletter

1. Usar notebook del pilar correspondiente.
2. Pedir a NotebookLM:
   - "Identifica un mecanismo psíquico concreto descrito en estas fuentes que tenga peso emocional para una lectora con [perfil de pilar]."
   - "Genera 3-4 párrafos descriptivos del mecanismo, sin coaching ni frases motivacionales."
3. Revisión editorial intensiva Daniel (1-2 h): la carta "Te escribo" exige voz humana auténtica. NotebookLM aporta arquitectura conceptual, no redacción final.
4. Output: carta lista para enviar por MailerLite (ver `documentos-internos/mailerlite-*` cuando se actualicen).

### 3.4 · Workflow D — Onboarding rápido de Sergio o futura VA

1. Dar acceso al notebook "Marco editorial TWIM" (§2.1).
2. Pedir al colaborador que haga 5-7 preguntas a NotebookLM sobre TWIM (qué es, tono, pilares, diferencias entre programas).
3. Daniel revisa las respuestas con el colaborador en 1 sesión de 60 min: dónde acertó NotebookLM, dónde se queda corto, qué matices añadir.
4. Output: colaborador con base mínima para empezar a operar sin necesidad de que Daniel le explique todo desde cero.

### 3.5 · Workflow E — Investigación cruzada de un concepto

Cuando Daniel quiere preparar un episodio o artículo sobre un concepto que aparece en varios pilares (ej. "transferencia", "introyección", "ideal yoico").

1. Crear notebook temporal con fuentes de varios pilares + literatura externa relevante.
2. Pedir a NotebookLM:
   - "Cómo aparece el concepto [X] en cada una de estas fuentes. ¿Qué matices distintos hay?"
   - "Genera un mapa conceptual de [X] basado en estas fuentes."
3. Output: visión panorámica del concepto en TWIM, útil para escribir piezas que cruzan pilares.

### 3.6 · Lo que NO se hace en ningún workflow

- Pedirle a NotebookLM que **redacte el output final** (guion, carrusel, carta) sin pasar por edición editorial Daniel.
- Subir como fuente **transcripciones de sesión clínica**, ni siquiera "anonimizadas".
- Compartir notebooks fuera del equipo TWIM (Daniel + Sergio + VA cuando entre).
- Confiar ciegamente en una **referencia o cita** que NotebookLM dé sin verificarla en la fuente original.

---

## 4 · Lo que NotebookLM SÍ hace bien

- **Organizar fuentes** en colecciones consultables. Es básicamente un repositorio indexado que entiende el contenido, no solo el nombre del archivo.
- **Resumir** documentos largos manteniendo la estructura del original. El resumen tiende a ser razonablemente fiel.
- **Generar esquemas** de partida para piezas nuevas a partir de fuentes existentes. Útil como "primer borrador conceptual".
- **Localizar fragmentos** dentro de fuentes largas (libro, briefings de programa). Si Daniel busca "qué decía el libro sobre culpa", NotebookLM lo encuentra rápido.
- **Conectar conceptos entre fuentes**. Útil cuando un mismo concepto aparece en varios artículos y Daniel quiere ver cómo se ha tratado en cada uno.
- **Generar FAQ** para landings, descripciones de podcast, etc. Las preguntas que sugiere suelen ser las que realmente se hacen los lectores.
- **Mantener trazabilidad de citas** — cuando responde a una pregunta, indica qué fuente del notebook está usando. Esto es lo que diferencia a NotebookLM de un chatbot genérico.

---

## 5 · Lo que NotebookLM NO hace bien

- **Escribir con voz TWIM auténtica.** El output es siempre tonalmente neutro o ligeramente positivista. Reescribir con voz Daniel es obligatorio en cualquier pieza pública.
- **Resolver dudas clínicas delicadas.** Una pregunta tipo "¿este caso compuesto cuadra como ejemplo de dependencia o de duelo?" la resuelve Daniel, no NotebookLM. La herramienta no tiene criterio clínico.
- **Sustituir la lectura humana del material.** NotebookLM puede resumir un capítulo del libro, pero el resumen no equivale a haberlo leído. Un colaborador que solo se base en lo que NotebookLM le dice del libro no tiene base suficiente para escribir como TWIM.
- **Garantizar que el output es 100 % fiel al original.** Hay alucinaciones (poco frecuentes en NotebookLM por su diseño basado en fuentes, pero existen). Verificar siempre las citas concretas en la fuente original.
- **Adaptar tono a perfil de audiencia.** Si se le pide "escribe esto para mujeres 25-35 con burnout", el resultado es genérico. La adaptación a perfil real la hace Daniel.
- **Conectar con material que no esté en sus fuentes.** NotebookLM solo razona sobre lo que tiene en el notebook. Esto es feature (anti-alucinación) pero también limitación: si falta una fuente clave, no la inventa.
- **Sustituir conversación clínica con un paciente.** Esto va en §1 pero conviene repetirlo: NotebookLM es herramienta editorial, no clínica.

---

## 6 · Política de Audio Overviews

NotebookLM ofrece una función "Audio Overview" que genera automáticamente un audio tipo conversación entre dos voces sintéticas norteamericanas resumiendo las fuentes del notebook.

### 6.1 · Decisión cocida (sesión 30-abr)

> **NO se publican Audio Overviews de NotebookLM como contenido del podcast TWIM.** Para podcast se usa exclusivamente el workflow del doc #2 (guion editorial Daniel + voz humana T1, ElevenLabs T2 con disclosure).

### 6.2 · Por qué

- **Voz no es la de Daniel.** Audio Overview usa dos voces sintéticas norteamericanas predefinidas. Publicar eso bajo la marca TWIM Podcast rompe la promesa "voz de Daniel" de raíz.
- **Tono no es TWIM.** El estilo Audio Overview es entusiasta, dialogado, ligeramente positivista. Es el opuesto del tono editorial TWIM (descriptivo, sin coaching).
- **Sin disclosure adecuado.** Aunque NotebookLM marque que es generado, las plataformas (Spotify, YouTube) no tienen vías limpias para etiquetar este contenido como tal de forma defendible deontológicamente.
- **No aporta valor diferencial.** Un Audio Overview es básicamente un resumen automático de las fuentes. Lo que TWIM Podcast aporta es la **lectura editorial Daniel** del material — eso es lo que tiene valor de marca.

### 6.3 · Cuándo SÍ se puede usar Audio Overview (uso interno)

- **Como ayuda para Daniel** al preparar un episodio: escuchar el Audio Overview de las fuentes mientras conduce o pasea le permite "remasticar" el material desde otra perspectiva.
- **Como onboarding de un colaborador** que prefiere escuchar a leer un primer resumen del notebook "Marco editorial TWIM".
- **Para uso 1:1** dentro del equipo (Daniel ↔ Sergio ↔ VA), no publicado.

En todos estos usos, el Audio Overview se queda dentro del equipo. Nunca sale a feed público bajo marca TWIM.

---

## 7 · Riesgos y mitigación

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Filtración accidental de material clínico de paciente a NotebookLM | Muy baja con la política, catastrófica sin ella | Catastrófico (deontológico + RGPD + reputacional) | §1 política dura. Chequeo de 3 preguntas (§1.4) antes de cualquier subida. Auditoría trimestral del contenido de notebooks. |
| Google cierra NotebookLM o lo convierte en producto de pago restringido | Media a 24 meses | Medio | Mantener fuentes originales en repo TWIM (todas las fuentes ya están en el repo o en almacenamiento propio). Si NotebookLM cierra, migrar a herramienta equivalente (Anthropic Projects, ChatGPT Projects, Claude Projects, etc.) sin pérdida del contenido fuente. |
| Cambio de funcionalidades (ej. retirada de citaciones por fuente, cambio de límite de fuentes) | Media | Bajo | El valor diferencial es la trazabilidad de citas; si Google la quita, el valor cae y conviene migrar. |
| Output de NotebookLM con alucinación citada como fuente real | Baja | Medio | Verificar manualmente toda cita concreta en fuente original antes de publicarla. No publicar nunca "directamente" un output de NotebookLM. |
| Colaborador (Sergio, VA) sube fuente sin pedir permiso a Daniel | Media a 12 meses | Variable según fuente | Política de control: solo Daniel sube fuentes a notebooks compartidos. Colaboradores piden subida vía mensaje. |
| Sobre-dependencia editorial de NotebookLM (Daniel pierde el músculo de escribir desde cero) | Media a 12 meses | Medio (pérdida de voz auténtica con el tiempo) | Regla operativa: cada N piezas, hacer una sin NotebookLM, totalmente desde cero. Mantener el músculo. |
| Compartición accidental de notebook con persona ajena al equipo | Baja con configuración correcta | Variable según notebook | Notebook nunca compartido públicamente. Lista cerrada de cuentas con acceso. Revisar permisos cada 3 meses. |
| Publicación errónea de Audio Overview sintético como episodio del podcast | Baja con la regla §6 clara | Alto reputacional | Regla §6 explícita y formación a colaboradores. Checklist pre-publicación de podcast incluye "¿el audio es voz Daniel humana o ElevenLabs con disclosure?". |
| Dependencia de cuenta Google personal de Daniel para todo el sistema | Media | Alto si Daniel pierde acceso | Migrar a cuenta TWIM corporativa cuando se formalice. Tener acceso de emergencia compartido con persona de confianza (legal, no técnica). |

---

## 8 · Coste y plan

### 8.1 · Estado al 4-may-2026

| Plan | Coste | Límites | Recomendación |
|---|---|---|---|
| NotebookLM (general) | 0 € | Hasta 100 notebooks, 50 fuentes/notebook, ~500.000 palabras totales por notebook | Suficiente para TWIM hoy |
| NotebookLM Plus (vía Google One AI Premium) | ~22 €/mes | 5x los límites del free, modelos más recientes, audio overviews ilimitados | Solo si se llega al techo del Free |

### 8.2 · Cuándo evaluar subir a Plus

- Cuando un notebook se acerque al techo de 50 fuentes y haya que partirlo de forma poco natural.
- Si Google introduce features Plus-only que sean operativamente relevantes (ejemplo hipotético: edición colaborativa con varios usuarios).
- Si el equipo crece a 3+ personas usando NotebookLM activamente.

### 8.3 · Si Google introduce planes de pago obligatorio

Probabilidad media a 24 meses: Google migra NotebookLM a Google One AI Premium o lo separa como producto de pago independiente.

Plan B en ese escenario:

- Si el coste es < 30 €/mes para Daniel solo, subir.
- Si el coste es > 30 €/mes o si pasa a tarificarse por uso, evaluar alternativas: Anthropic Projects, ChatGPT Projects con archivos. Migración estimada: 1-2 días de trabajo si las fuentes están bien organizadas en el repo.

---

## 9 · Decisiones a cerrar este mes

- [ ] **Crear cuenta TWIM en Google** (si no existe ya como cuenta corporativa) y montar NotebookLM ahí, no en cuenta personal de Daniel.
- [ ] **Crear notebook "Marco editorial TWIM"** (§2.1) con las 5-10 fuentes recomendadas.
- [ ] **Crear notebooks por pilar** (§2.2 a §2.5) con las fuentes de cada uno.
- [ ] **Crear notebook "Libro Engranajes"** (§2.6) con manuscrito completo.
- [ ] **Probar workflow A** (§3.1) con un episodio piloto y validar que el output ahorra tiempo real frente a redactar el esquema desde cero.
- [ ] **Documentar la política §1** en una nota visible cuando se cree cada notebook (en la descripción del propio notebook).
- [ ] **Configurar permisos** de cada notebook con lista cerrada de cuentas. Revisar que ningún notebook tenga "anyone with the link" activado.
- [ ] **Hacer una sesión de onboarding** con Sergio (cuando aplique) usando el notebook "Marco editorial TWIM" como base, validando que el workflow D (§3.4) funciona en la práctica.
- [ ] **Programar auditoría trimestral** de fuentes en notebooks (próxima: julio 2026) para validar que se respeta la política §1.

---

## Cierre

NotebookLM es la pieza menos visible de la cadena del stack audio + vídeo (el oyente del podcast nunca lo va a notar) pero es la que multiplica la productividad editorial de Daniel. Bien usado ahorra 30-60 min de organización de fuentes por episodio y 1-2 h por carrusel o carta.

Mal usado — y el modo de mal uso más fácil es cruzar la línea de §1 y subir material clínico — destruye la base deontológica de TWIM. Por eso la sección §1 es la más larga del documento y la primera del orden lógico.

El orden de implementación es:

1. Política §1 documentada y interiorizada por todo el que toque NotebookLM (Daniel ahora, Sergio y VA cuando entren).
2. Notebooks permanentes §2.1-§2.6 montados.
3. Workflow A (§3.1) probado con un episodio piloto.
4. Resto de workflows según se necesite.

— Notas técnicas: documento generado el 04-05-2026 a partir del TODO-PENDIENTE.md de la sesión 30-abr. Si Google cambia plan de precios o features clave, actualizar §8 y §6. Si aparece alternativa con mejor trazabilidad de citas (Anthropic Projects con citas, por ejemplo), evaluar migración.
