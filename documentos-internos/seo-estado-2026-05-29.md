# SEO · Estado y mejoras on-page · 29 mayo 2026

> Documento operativo · 29 may 2026 · sesión `claude/confident-ptolemy-e6Kpx`.
> Trigger: Daniel pregunta «¿cómo está el posicionamiento SEO de TWIM Project?» y da libertad de acción para aplicar mejoras que vayan en línea con el proyecto.
> Continúa la línea de: `SEO_ANALISIS_2026-03-20.md`, `GUIA-IMPLEMENTACION-SEO.md`, `seo-indexacion-search-console-2026-05-05.md`.

---

## 0 · Encuadre de método (qué SÍ y qué NO se ha tocado)

- **Fuente primaria de posición/indexación: Google Search Console** (gratis, lado Daniel). **No se ha usado ni sondeado el conector Ahrefs** — decisión cerrada de Daniel el 17-may (`ahrefs-conector-estado-2026-05-17.md` §0): no se invierte, no se reabre salvo que él lo pida explícitamente. Esta pregunta no reabre Ahrefs.
- Por eso este documento **no trae cifras de posición/keywords/backlinks** (no hay fuente de dato sin GSC delante). Es una auditoría **on-page y técnica** del repo (lo que sí es verificable y accionable desde aquí) + plan de lo que mueve la aguja, que sigue siendo del lado Daniel.
- Cambios aplicados: solo **aditivos on-page** (meta tags, schema, copy) sobre páginas concretas. **Cero cambios de routing** (`netlify.toml`, `_redirects`, `_headers` intactos). Únicos toques en `sitemap.xml`: 3 `lastmod` de las páginas editadas (señal de re-rastreo, sin riesgo).

---

## 1 · Cómo está el SEO hoy (lectura honesta)

### 1.1 · Lo que está muy bien (base técnica sólida)

Auditoría on-page de las ~40 páginas públicas indexables (matriz completa generada en sesión). La salud técnica es **alta** y muy por encima de la media de webs de psicólogo:

- **Casi todas las páginas indexables tienen:** `<title>` y meta description trabajados, `canonical` autorreferenciado, `og:*` completo, Twitter Card, JSON-LD (Article / FAQPage / BreadcrumbList / Person / MedicalBusiness-ProfessionalService según corresponde), un único `<h1>`, `lang="es"`, e imágenes con `alt`.
- **Home:** schema `Organization`+`ProfessionalService`+`Person`, NAP, `sameAs` a todas las redes, `geo.region`, verificación GSC. Impecable.
- **Las 7 landings de servicio prioritarias** que el análisis de marzo pedía (§5.1) **ya existen y están bien montadas**: `psicologo-ansiedad-valencia/`, `psicologo-dependencia-emocional-valencia.html`, `psicologo-burnout-valencia.html`, `psicologo-adolescentes-valencia.html`, `terapia-pareja-valencia.html`, `psicologo-online.html`, `daniel-orozco-abia.html`. **La Prioridad 1 de marzo está ejecutada.**
- **25 insights** indexables, todos con schema Article, y con CTA al Directo/Newsletter (trabajo del 26-may). Cluster temático fuerte.
- Las 24 URLs «Descubierta — sin indexar» del 5-may eran problema de **autoridad de dominio + crawl budget**, NO técnico (diagnóstico ya cerrado en `seo-indexacion-search-console-2026-05-05.md`).

**Conclusión:** el techo de TWIM hoy **no es on-page**. Lo on-page está bien. El techo es **autoridad externa + entidad** (backlinks, GBP, menciones, reseñas éticas) — exactamente lo que marcan los docs previos y que es del lado Daniel.

### 1.2 · Huecos on-page detectados (los he arreglado · §2)

A pesar de la base sólida, había excepciones concretas:

| Página | Hueco detectado |
|---|---|
| `reto-7-dias.html` | **Sin `canonical`** (pese a estar en sitemap, prioridad 0.9). OG incompleto (sin `og:image`/`og:url`). Sin Twitter Card. **Y «confirmen» en el H1 del hero** → viola regla inviolable «claridad de un vistazo». |
| `libros-firmados.html` | **Canonical incoherente:** apuntaba a `/libros-firmados` (sin `.html`) mientras sitemap + enlaces internos usan `/libros-firmados.html`. Señal partida. Sin OG/Twitter. |
| `insights/index.html` | Hub de contenidos **sin JSON-LD**. |

### 1.3 · Huecos que NO he tocado (requieren decisión o diseño · §4)

- `talleres/volver-a-mi/index.html` (landing del taller insignia de otoño) **sin OG/Twitter** → al compartirla no genera preview. Necesita una tarjeta social propia (tarea de diseño, criterio dopamina-comercial).
- `lead-volver-a-mi-5-senales.html` sin `og:image` → no hay tarjeta social 1200×630 limpia de «hambre de mirada» (solo slides verticales del carrusel). No le fuerzo una imagen mal recortada.
- **Directorios fuente servidos en público:** como `netlify.toml` publica `.` (raíz), `email-templates/`, `documentos-internos/`, `contenido-rrss/` y los `pdfs/` de talleres son técnicamente accesibles por URL. Hoy están **huérfanos** (ningún enlace público apunta a ellos) y fuera del sitemap, así que el riesgo de indexación es bajo, pero no es cero. Bloquearlos limpio sería con `robots.txt`/`_headers` → **cambio de infraestructura (regla §2)**: lo dejo como recomendación, no lo toco sin tu OK.

---

## 2 · Mejoras aplicadas esta sesión (on-page, en línea TWIM)

Todas aditivas, sin riesgo de routing. CI/deploy preview de Netlify debe quedar verde.

1. **`reto-7-dias.html`**
   - Añadido `canonical` autorreferenciado (`/reto-7-dias.html`), `author`, `robots`.
   - OG completo: `og:url`, `og:image` (`portada-rrss-reto-7-dias-deja-de-buscarte.png`, tarjeta ya existente), `og:image:alt`, `og:site_name`, `og:locale`.
   - Twitter Card `summary_large_image` con título/descr/imagen.
   - **Copy (regla inviolable «claridad de un vistazo»):** H1 «por qué necesitas que te **confirmen** para sentirte bien» → «por qué **dependes** de la mirada de los demás para estar en paz» (redacción elegida por Daniel el 29-may entre 3 opciones; usa la imagen concreta «la mirada del otro» de la propia regla). `og:description` y `twitter:description` alineados a la misma imagen. (La meta description mantiene «necesidad de validación» — término clínico válido en SEO según la propia regla.)

2. **`libros-firmados.html`**
   - Canonical corregido a `/libros-firmados.html` (coherente con sitemap + enlaces internos + convención `.html` del resto del sitio).
   - Añadido OG completo + Twitter Card (imagen `portada-rrss-libro-engranajes-mente.png`) + `author`.

3. **`insights/index.html`**
   - Añadido JSON-LD `Blog` (con author Person → `daniel-orozco-abia.html`, publisher Organization) + `BreadcrumbList` (Inicio → Artículos). Ayuda a Google a clasificar el hub.

4. **`sitemap.xml`** · `lastmod` → 2026-05-29 en las 3 páginas editadas (re-rastreo).

---

## 3 · Diagnóstico estratégico: dónde está el verdadero techo

Reafirma lo ya escrito (marzo §3 + 5-may §3). El on-page no es el cuello. El cuello es:

1. **Autoridad de dominio baja** → crawl budget limitado → URLs que tardan en indexar.
2. **Entidad «Daniel Orozco Abia» poco reforzada fuera de la web** (pocas menciones de terceros).
3. **SEO local Valencia** muy competido sin GBP fuerte + señales locales.

Ninguno se resuelve con código. Se resuelven con las acciones del §5.3 de marzo y del 5-may.

---

## 4 · Acciones pendientes (lado Daniel · orden de impacto)

### 4.1 · GSC — gratis, alto impacto, ya documentado
- Solicitud manual de indexación de las URLs aún en «Descubierta — sin indexar» (plan §5.1 de `seo-indexacion-search-console-2026-05-05.md`, máx. 10/día). Revisar si las del Día 1 del 5-may ya pasaron a «Indexada».
- Tras este push: re-inspeccionar `reto-7-dias.html`, `libros-firmados.html` e `insights/` en GSC para que recoja los cambios.

### 4.2 · Autoridad externa — lo que mueve la aguja (medio plazo)
- Google Business Profile completo + optimizado (Prioridad 1 de marzo, aún la palanca #1 local).
- Directorios profesionales serios (Colegio Oficial de Psicología CV, Top Doctors, etc.).
- Apariciones en podcasts ajenos / guest posts / prensa local (entidad + backlinks).
- Reseñas éticas (no de pacientes): talleres, libros, homólogos — protocolo en `SEO_ANALISIS_2026-03-20.md` §6-7.

### 4.3 · On-page que requiere diseño/decisión
- Tarjeta social (OG 1200×630) para `talleres/volver-a-mi/` y para `lead-volver-a-mi-5-senales.html` → luego añadir `og:image`/Twitter (criterio dopamina-comercial).
- **Decisión infra (§2):** ¿bloquear con `robots.txt`/`X-Robots-Tag` los directorios fuente servidos en público (`email-templates/`, `documentos-internos/`, `contenido-rrss/`, `talleres/**/pdfs/`)? Bajo riesgo actual (huérfanos), pero higiene. Requiere tu OK por ser cambio de routing/headers.

---

## 5 · Métricas a vigilar (GSC, sin Ahrefs)
- Nº de URLs en «Descubierta/Rastreada sin indexar» → debe bajar.
- Impresiones/clics de `reto-7-dias`, `libros-firmados`, insights tras el re-rastreo.
- Aparición en SERP de keywords de servicio Valencia (las landings ya existen; falta autoridad).

---

## 6 · Trazabilidad
- Generado: 29 may 2026, sesión `claude/confident-ptolemy-e6Kpx`.
- Aplicado en el mismo PR: ediciones on-page §2 + este documento.
- No se tocó: `netlify.toml`, `_redirects`, `_headers`, conector Ahrefs.
- Refs: `SEO_ANALISIS_2026-03-20.md`, `seo-indexacion-search-console-2026-05-05.md`, `ahrefs-conector-estado-2026-05-17.md`, `CLAUDE.md` (reglas §método, §infra, §claridad de un vistazo).
