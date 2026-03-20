# Análisis SEO y posicionamiento orgánico — TWIM Project / Daniel Orozco Abia

**Fecha:** 20 de marzo de 2026  
**Objetivo:** aumentar la visibilidad orgánica en Google de la web y de la marca personal de Daniel Orozco Abia sin depender todavía de publicidad pagada.

## 1. Resumen ejecutivo

### Fortalezas actuales
- La home ya está orientada a intención local y transaccional con términos como “Psicólogo en Valencia”, “ansiedad”, “estrés”, “depresión”, “dependencia emocional” y modalidades presencial/online.
- La web ya incluye señales técnicas importantes: `canonical`, `author`, metadescripción, Open Graph, Twitter Cards, `robots.txt`, `sitemap.xml` y varios bloques `JSON-LD`.
- Existe una base de contenidos “Insights” con múltiples artículos indexables y bastante alineados con búsquedas informacionales de alto valor.
- La marca personal está bien conectada con perfiles externos (Instagram, YouTube, LinkedIn) y con activos editoriales como libros/programas.

### Debilidades principales
- La autoridad externa de marca todavía parece baja: en búsquedas de nombre/marca apenas aparecen resultados sólidos de terceros en las comprobaciones rápidas realizadas.
- La home intenta atacar demasiadas intenciones a la vez; esto puede diluir el foco semántico para consultas de alta competencia como “psicólogo Valencia”.
- Faltan páginas de servicio específicas y profundas para cada línea con intención local clara (`/psicologo-ansiedad-valencia/`, `/psicologo-dependencia-emocional-valencia/`, etc.).
- La estrategia de reseñas necesita una vía ética compatible con el encuadre terapéutico.

### Prioridades estratégicas
1. **Consolidar SEO local y de marca personal** (Google Business Profile, citas locales, consistencia NAP, páginas locales/servicio).
2. **Convertir la autoridad temática de Insights en captación** con clusters más cerrados y enlazado interno más agresivo hacia servicios.
3. **Construir prueba social ética** sin pedir reseñas a pacientes actuales ni vulnerar el encuadre.
4. **Generar autoridad de terceros** con entrevistas, podcasts, prensa local, colegios profesionales y colaboraciones expertas.

---

## 2. Qué se ha revisado

### Revisión técnica local del proyecto
Se revisaron:
- `index.html`
- `insights/index.html`
- artículos de `insights/`
- `robots.txt`
- `sitemap.xml`
- el documento previo `seo_analysis.md`

### Comprobaciones externas rápidas
Se realizaron búsquedas web sobre:
- `site:twimproject.com`
- `"Daniel Orozco Abia" psicólogo Valencia`
- `"TWIM Project"`
- `"daniorozcopsicologo"`

**Limitación:** las herramientas de búsqueda devolvieron pocos resultados útiles y la comprobación HTTP directa contra `https://twimproject.com/` desde terminal quedó bloqueada por red/proxy, así que las conclusiones sobre SERP reales deben tomarse como orientación inicial y validarse después en Google Search Console y en búsquedas manuales desde navegador real.

---

## 3. Diagnóstico SEO actual

## 3.1. Marca personal: “Daniel Orozco Abia”

### Lectura estratégica
Ahora mismo el reto no parece ser solo “SEO de web”, sino **SEO de entidad/persona**. Para subir arriba del todo por tu nombre en Google, Google necesita señales claras de que:
- eres una persona real y reconocible en tu categoría profesional,
- hay fuentes externas que te mencionan,
- tu web es el nodo principal de esa identidad digital,
- tus perfiles sociales y profesionales están coherentemente conectados.

### Qué faltaría reforzar
- Más resultados de terceros controlables: entrevistas, perfiles profesionales, colaboraciones, artículos invitados, apariciones en medios, podcasts, directorios profesionales serios.
- Más consistencia exacta del nombre: usar siempre **Daniel Orozco Abia** o la variante elegida como estándar principal.
- Más menciones externas enlazadas apuntando a la web principal.
- Una página dedicada tipo `/daniel-orozco-abia/` o equivalente con biografía extensa, credenciales, enfoque, medios, libros, talleres y enlaces a perfiles.

---

## 3.2. SEO local: “psicólogo Valencia” y variantes

### Situación
La home ya intenta posicionar consultas locales potentes, pero “psicólogo Valencia” es una keyword muy competida. Sin un perfil local potente y sin señales externas suficientes, es difícil dominar esa SERP solo con una home generalista.

### Qué falta para competir mejor
- **Google Business Profile** muy trabajado.
- **Categoría principal y secundarias** bien afinadas.
- **NAP consistente** (nombre, dirección, teléfono si procede) en web + perfiles + directorios.
- **Landing pages por problema + ciudad**.
- **Más autoridad externa local**: prensa local, directorios del sector, colaboraciones en Valencia, asociaciones, universidades, charlas.

---

## 3.3. SEO temático / contenidos

### Lo positivo
La carpeta `insights/` ya cubre temas con buen potencial de descubrimiento orgánico:
- dependencia emocional,
- ansiedad productiva,
- rumiación,
- obligación/debería,
- burnout/malestar laboral,
- autoestima,
- validación,
- síndrome del impostor.

### Lo que falta para convertir ese tráfico en ranking + negocio
- Cada artículo debería empujar con claridad hacia una página de servicio o programa muy alineado.
- Faltan clusters cerrados con intención clara:
  - **Ansiedad en adultos en Valencia**
  - **Dependencia emocional**
  - **Burnout / malestar laboral**
  - **Adolescentes / TDAH / motivación escolar**
  - **Terapia de pareja**
- Faltan piezas BOFU/MOFU más transaccionales, por ejemplo:
  - “Cómo elegir psicólogo en Valencia para ansiedad”
  - “Terapia para dependencia emocional en Valencia: cuándo sí ayuda”
  - “Psicólogo online vs presencial: cuál te conviene según tu caso”
  - “Cuándo el burnout necesita terapia y no solo descanso”

---

## 4. Auditoría técnica y on-page del sitio

## 4.1. Señales buenas ya implementadas
- `index.html` contiene `title`, metadescripción, `author`, canonical, Open Graph y Twitter Cards.
- La home incluye `JSON-LD` para `Organization`/`ProfessionalService`, `Person`, `Book`, `FAQPage`, `BreadcrumbList` y un `Product`.
- `robots.txt` permite rastreo e informa del sitemap.
- `sitemap.xml` ya incluye home, landings principales e índice/artículos de `insights`.
- Los artículos revisados de `insights` tienen en general `title`, `h1`, canonical y schema de `Article`.

## 4.2. Huecos detectados

### A. Exceso de ambición semántica en la home
La home intenta atacar muchas keywords a la vez: ansiedad, depresión, estrés, dependencia emocional, burnout, adolescentes, deportistas, pareja, Valencia, online, etc. Eso puede funcionar como carta de presentación, pero no es lo ideal para dominar búsquedas concretas de alta competencia.

**Recomendación:** dejar la home como página de marca + consulta general y crear páginas satélite mucho más específicas.

### B. Falta de landings de servicio altamente específicas
Ahora mismo la home concentra gran parte de la intención transaccional. Para SEO real en servicios sanitarios necesitas URLs independientes con:
- H1 exacto y específico,
- copy más profundo,
- preguntas frecuentes del problema,
- pruebas de autoridad,
- casos típicos / señales / cuándo pedir ayuda,
- CTA claros.

### C. Falta de una página fuerte de marca personal
Aunque ya hay schema de `Person`, conviene una página propia de autor/profesional que sea la referencia semántica principal de tu entidad.

### D. Entidad local mejorable
Si el objetivo es “estar arriba del todo”, no basta con metadatos. Hace falta reforzar la **entidad local** fuera de la web.

### E. E-E-A-T mejorable en superficie visible
Aunque se mencionan credenciales y experiencia, conviene mostrarlas de forma más explícita y repetida en páginas clave:
- número de colegiado / registro sanitario,
- años de experiencia,
- áreas exactas de trabajo,
- medios / entrevistas / publicaciones,
- libros / talleres / formaciones,
- página de política editorial y enfoque profesional.

---

## 5. Qué haría para subir posiciones sin anuncios

## 5.1. Prioridad 1 — SEO local y de conversión
Crear en los próximos 30 días estas páginas:
- `/psicologo-ansiedad-valencia/`
- `/psicologo-dependencia-emocional-valencia/`
- `/psicologo-burnout-valencia/`
- `/terapia-pareja-valencia/`
- `/psicologo-adolescentes-valencia/`
- `/psicologo-online/`
- `/daniel-orozco-abia/`

Cada página debería incluir:
- título y H1 específicos,
- introducción enfocada en la intención de búsqueda,
- síntomas/problemas típicos,
- cómo trabajas ese problema,
- para quién sí / para quién no,
- FAQs,
- CTA a contacto,
- enlaces a 3–5 artículos relacionados de Insights,
- schema de `MedicalBusiness` o `ProfessionalService` / `Person` / `FAQPage` según corresponda.

## 5.2. Prioridad 2 — Arquitectura de contenidos
Organizar el blog en clusters con pilares y supporting content.

### Cluster 1: Dependencia emocional
- Pilar: “Terapia para dependencia emocional en Valencia”
- Apoyos:
  - señales de dependencia emocional,
  - necesidad de validación,
  - autoestima baja,
  - relaciones intermitentes,
  - apego ansioso.

### Cluster 2: Ansiedad / urgencia / rumiación
- Pilar: “Psicólogo ansiedad Valencia”
- Apoyos:
  - urgencia mental,
  - rumiación,
  - autoexigencia,
  - ansiedad productiva,
  - síntomas de ansiedad funcional.

### Cluster 3: Burnout / trabajo / obligación
- Pilar: “Psicólogo burnout Valencia”
- Apoyos:
  - trabajo que te enferma,
  - malestar laboral,
  - obediencia en el trabajo,
  - vivir en obligación,
  - desconexión al acabar la jornada.

## 5.3. Prioridad 3 — Autoridad externa
Sin autoridad externa será muy difícil ser top en consultas competidas.

### Acciones recomendadas
- Perfil completo y activo en Google Business Profile.
- Ficha potente en directorios profesionales serios y selectivos.
- Entrevistas en podcasts o canales afines sobre ansiedad, dependencia emocional, burnout o adolescencia.
- Colaboraciones con medios locales de Valencia.
- Apariciones como experto invitado en blogs, newsletters o medios de salud/empresa/deporte.
- Publicar o republicar extractos del libro y enlazarlos desde perfiles externos.
- Conseguir enlaces desde asociaciones, colegios, formaciones, centros colaboradores o eventos donde participes.

---

## 6. Sobre reseñas: cómo abordarlo sin romper el encuadre

Tu preocupación tiene sentido. En salud mental, pedir reseñas a pacientes puede ser problemático por encuadre, asimetría y presión implícita. Yo **no basaría tu estrategia principal en pedir reseñas a pacientes** si eso choca con tu práctica clínica.

## 6.1. Qué NO haría
- No pedir reseñas de forma insistente a pacientes actuales.
- No pedir reseñas “de favor” a amistades si no conocen tu trabajo profesional real.
- No inflar artificialmente Google Business Profile con opiniones poco genuinas.
- No publicar testimonios ambiguos que puedan comprometer confidencialidad o parecer fabricados.

## 6.2. Qué sí puedes hacer de forma ética

### Opción A — Reseñas de homólogos con contexto real
Sí puede tener sentido pedir reseñas a colegas **solo si** pueden hablar de algo verdadero y verificable:
- tu rigor profesional,
- tu capacidad docente,
- tu claridad clínica,
- colaboraciones reales,
- supervisiones, formación o trabajo conjunto,
- charlas o talleres que hayan visto.

**Importante:** que la reseña deje claro el contexto (“he compartido formación / colaboración profesional / he visto su trabajo divulgativo”) y no simule haber sido paciente.

### Opción B — Testimonios de alumnos / asistentes / lectores / empresas
Esta es probablemente tu mejor vía ahora mismo.
Puedes recoger testimonios de:
- asistentes a talleres,
- personas que hayan hecho programas formativos,
- lectores de tus libros/guías,
- empresas o equipos donde hayas impartido formación,
- padres/madres o centros educativos en actividades no clínicas,
- deportistas o profesionales con quienes hayas trabajado en contexto formativo o de rendimiento, si procede y es adecuado.

Eso genera prueba social válida **sin invadir la relación terapéutica**.

### Opción C — Testimonios anónimos y consentidos fuera de Google
Si alguna persona, de forma espontánea y libre, quiere dejar feedback, puedes usar un sistema más controlado:
- consentimiento explícito por escrito,
- anonimización real,
- sin detalles clínicos sensibles,
- publicados en la web como “experiencias con talleres/programas/contenido”, no necesariamente como reseñas públicas en Google.

### Opción D — Sustituir reseñas por otras señales de confianza
Si decides no empujar reseñas, entonces necesitas redoblar otras pruebas de confianza:
- credenciales visibles,
- años de experiencia,
- número de registro/colegiación,
- entrevistas y apariciones,
- publicaciones y libros,
- colaboraciones institucionales,
- FAQs muy trabajadas,
- páginas de enfoque y método,
- contenido experto constante.

---

## 7. Mi recomendación específica sobre reseñas para tu caso

### Estrategia más limpia
1. **No pedir reseñas a pacientes dentro del proceso terapéutico.**
2. **Sí pedirlas a contextos no clínicos reales:** talleres, programas, libros, charlas, empresas, colaboraciones profesionales.
3. **Sí pedir 3–8 reseñas cualificadas a homólogos**, pero en formato honesto (“como colega/profesional, destaco…”).
4. **Crear una página de testimonios de contexto formativo/divulgativo** en tu web, separada claramente de la clínica.
5. **Usar Google Business Profile con prudencia**, aceptando que crecerá más lento pero con mayor coherencia ética.

### Plantilla de petición ética para homólogos
> Hola, [Nombre]. Estoy reforzando la presencia digital de mi proyecto y me ayudaría mucho una reseña honesta sobre mi trabajo desde el contexto en el que tú lo conoces (colaboración, formación, supervisión, divulgación, etc.). La idea es que sea totalmente fiel a tu experiencia real, sin aparentar en ningún caso experiencia clínica como paciente. Si te encaja, te paso el enlace. Gracias.

### Plantilla de petición ética para talleres / programas
> Hola, [Nombre]. Estoy mejorando la visibilidad del proyecto y me ayudaría mucho una reseña honesta sobre tu experiencia con el taller/programa/libro. Si te apetece, puedes comentar qué te resultó útil, claro o transformador, sin compartir nada íntimo que no quieras hacer público. Gracias de corazón.

---

## 8. Acciones concretas recomendadas en orden

## Próximos 7 días
- Configurar o optimizar al máximo Google Business Profile.
- Definir nombre profesional estándar y repetirlo igual en todos los activos.
- Crear página propia de marca personal (`/daniel-orozco-abia/`).
- Diseñar 3 landings de servicio prioritarias: ansiedad, dependencia emocional y burnout en Valencia.
- Añadir módulos de “sobre el profesional” y “credenciales” en páginas clave.

## Próximos 30 días
- Publicar 6–9 contenidos nuevos orientados a clusters con intención clara.
- Conseguir 5–10 menciones externas de calidad (directorios, entrevistas, colaboraciones, medios, perfiles profesionales).
- Conseguir 5–12 reseñas éticas de talleres, programas, libro, empresas u homólogos.
- Mejorar enlazado interno entre Insights → servicios → contacto.

## Próximos 90 días
- Medir en Search Console qué consultas ya activan impresiones.
- Doblar contenido sobre las keywords donde ya apareces entre posiciones 8–25.
- Construir una página de prensa/medios/colaboraciones.
- Crear una estrategia editorial estable para marca personal + talleres.

---

## 9. Conclusión clara

Sí hay base para crecer orgánicamente sin pagar anuncios todavía. La web ya tiene una estructura técnica bastante mejor que la de muchas webs pequeñas, pero para estar “arriba del todo” te falta sobre todo lo que Google interpreta como **autoridad real y entidad confiable**: páginas de servicio específicas, mayor fuerza local, más señales externas y una estrategia ética de prueba social.

La parte más importante de tu caso es esta: **si no quieres apoyar el crecimiento en reseñas de pacientes, necesitas compensarlo con autoridad de terceros, reseñas de contextos no clínicos, contenido excelente y una presencia local impecable**.

Eso es totalmente viable. Solo exige jugar una partida un poco más lenta, pero también más sólida y coherente con tu práctica.
