# Análisis SEO - TWIM Project
## Última actualización: 9 marzo 2026

---

## SCORE ACTUAL ESTIMADO: 88/100

| Métrica | Score | Estado |
|---------|-------|--------|
| Technical SEO | 90/100 | Excelente |
| On-Page SEO | 88/100 | Muy bueno |
| Schema/Structured Data | 95/100 | Excelente |
| Content Quality | 85/100 | Bueno |
| Mobile-First | 90/100 | Excelente |

---

### PUNTOS FUERTES ACTUALES

1. **Schema.org muy completo**: Organization, Person, Book, FAQPage, BreadcrumbList, Product, WebSite, VideoObject, Article (con datePublished/dateModified en todos)
2. **Meta Tags optimizados**: Title, description, keywords, author, geo tags, robots directives en todas las páginas
3. **Open Graph + Twitter Cards**: Configuración social completa en homepage y artículos
4. **Jerarquía HTML correcta**: H1 en hero, estructura H1→H2→H3 coherente
5. **Imágenes optimizadas**: ALT descriptivos, WebP con fallback, lazy loading, width/height para CLS
6. **Performance**: Preconnect, preload, dns-prefetch, font-display:swap, lazy loading en iframes
7. **Accesibilidad**: Aria-labels, autocomplete en forms, honeypot anti-spam
8. **Contenido de calidad**: 10 artículos bien estructurados con pillar + cluster strategy
9. **Links internos**: Sección "Sigue leyendo" con artículos relacionados en todos los artículos
10. **BreadcrumbList schema**: Implementado en homepage y en todos los artículos

---

### MEJORAS IMPLEMENTADAS (9 marzo 2026)

#### 1. VideoObject Schema en homepage
- Schema completo para el vídeo de YouTube embebido
- Incluye thumbnailUrl, embedUrl, contentUrl, author y publisher
- **Impacto**: Rich snippets de vídeo en SERPs

#### 2. dateModified en todos los artículos
- Añadido `dateModified` al Article schema de los 9 artículos
- Google usa dateModified para freshness signals
- **Impacto**: Mejor señal de actualización para crawlers

#### 3. BreadcrumbList schema en artículos
- Schema de breadcrumbs añadido a los 9 artículos de insights
- Estructura: Inicio → Insights → [Título del artículo]
- **Impacto**: Breadcrumbs visibles en SERPs, mejor navegación para crawlers

#### 4. robots.txt corregido
- Eliminada la regla `Disallow: /*.pdf$` que bloqueaba PDFs educativos
- Añadidas reglas para páginas que no deben indexarse (preventa)
- **Impacto**: PDFs ahora indexables, páginas transaccionales protegidas

#### 5. sitemap.xml mejorado
- Añadido namespace `xmlns:image` para image sitemap
- Incluidas imágenes principales de la homepage (daniel-orozco-consulta, portadas de libros)
- Actualizado lastmod del insights/index.html a fecha actual
- **Impacto**: Mejor indexación de imágenes, señal de freshness

#### 6. Related articles en elegir-es-perder
- Era el único artículo sin sección "Sigue leyendo"
- Añadidos 3 artículos relacionados (pillar article, juez interno, síndrome del impostor)
- **Impacto**: Mejor internal linking, reduce bounce rate

---

### OPORTUNIDADES PENDIENTES (Prioridad alta → baja)

#### ALTA PRIORIDAD

1. **Crear landing pages de servicios independientes**
   - `/terapia-adultos/` con schema Service
   - `/psicologia-deportistas/` con schema Service
   - `/terapia-de-pareja/` con schema Service
   - Impacto: Cada servicio puede rankear por sus propias keywords

2. **Implementar Google Business Profile**
   - Optimizar ficha con fotos, horarios, categorías
   - Pedir reseñas de pacientes
   - Añadir LocalBusiness schema al sitio
   - Impacto: Visibilidad en Google Maps, Local Pack

3. **Ampliar artículos del blog**
   - Crear contenido sobre: narcisismo, dependencia emocional, apego, ansiedad
   - Formato: "Psicólogo explica: [tema con volumen de búsqueda]"
   - Frecuencia mínima: 2 artículos/mes
   - Impacto: Tráfico orgánico long-tail

#### MEDIA PRIORIDAD

4. **Integrar transcripciones de YouTube como artículos**
   - Cada vídeo popular → artículo con transcript optimizado
   - Schema VideoObject en cada artículo con vídeo
   - Impacto: Doble indexación (YouTube + Web)

5. **Añadir AggregateRating/Review schema**
   - Recopilar testimonios de pacientes
   - Implementar schema Review
   - Impacto: Estrellas en SERPs, mayor CTR

6. **Mejorar imágenes OG por artículo**
   - Crear imagen OG específica para cada artículo (no reusar preview.jpg)
   - 1200x630px con título del artículo y foto de Daniel
   - Impacto: Mayor CTR en redes sociales

#### BAJA PRIORIDAD

7. **Implementar hreflang** (si se traduce contenido)
8. **Añadir tabla de contenidos** a artículos largos (>8 min lectura)
9. **Crear RSS feed** para el blog
10. **Implementar AMP** para artículos

---

### KEYWORDS OBJETIVO

| Keyword | Volumen (ES) | Dificultad | Estado |
|---------|-------------|------------|--------|
| psicólogo Valencia | 2.4K/mes | Alta | Optimizado |
| Daniel Orozco psicólogo | 200/mes | Baja | Posición 1 |
| síndrome del impostor | 12K/mes | Media | Artículo publicado |
| autoexigencia psicología | 1.2K/mes | Media | Contenido presente |
| terapia de pareja Valencia | 1.5K/mes | Alta | Necesita landing page |
| psicólogo deportista | 800/mes | Media | Servicio listado |
| narcisismo psicología | 8K/mes | Media | Sin contenido aún |
| dependencia emocional | 15K/mes | Media | Sin contenido aún |
| apego ansioso | 10K/mes | Media | Sin contenido aún |

---

### MÉTRICAS A MONITORIZAR

- **Search Console**: Impresiones, clicks, CTR, posición media
- **GA4**: Tráfico orgánico, páginas/sesión, tiempo en página
- **Conversiones**: Envíos de formulario, clicks en Stripe, compras libro
- **Indexación**: Páginas indexadas vs enviadas en sitemap
