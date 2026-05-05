# SEO · Indexación Search Console · 5 mayo 2026

> Documento operativo · 5 mayo 2026
> Diagnóstico de las 24 URLs reportadas como "Descubierta — actualmente sin indexar" en Google Search Console.
> Continúa el análisis estratégico previo: `SEO_ANALISIS_2026-03-20.md` y `GUIA-IMPLEMENTACION-SEO.md`.

---

## TL;DR

- **24 URLs** marcadas como `Descubierta — actualmente sin indexar` con Último rastreo `N/D` en Search Console.
- **Verificado:** las 24 están en `sitemap.xml`, `robots.txt` no las bloquea, el HTML de las páginas auditadas tiene `<meta robots="index, follow">` y canonical correcto.
- **Diagnóstico:** el problema NO es técnico ni de configuración. Es de **autoridad de dominio + crawl budget limitado**, ya identificado en `SEO_ANALISIS_2026-03-20.md` §3.
- **Hallazgo colateral:** 4 archivos con bug HTML del doble `<header>` (corregido en este PR).
- **Hallazgo de interlinking:** 1 URL realmente huérfana (`elegir-es-perder-psicologia-decision`) — añadida al hub `insights/index.html` en este PR.
- **Lo más eficaz a corto plazo:** solicitud manual de indexación en Search Console (acción del lado Daniel, máx. 10 URLs/día).
- **Lo que mueve la aguja a medio plazo:** autoridad externa (backlinks, GBP, menciones) — ya planificado en `SEO_ANALISIS_2026-03-20.md` §5.3 y `PLAN-CAPTACION-30D.md` §4.

---

## 1 · Lista de las 24 URLs no indexadas

Reportadas en Google Search Console, sección "Descubierta: actualmente sin indexar":

### Insights (17)

1. `https://twimproject.com/insights/ansiedad-productiva-presion-creatividad.html`
2. `https://twimproject.com/insights/autoestima-baja-origen-que-nadie-te-explica.html`
3. `https://twimproject.com/insights/deberia-dejar-trabajo-malestar.html`
4. `https://twimproject.com/insights/del-deberia-al-quiero-ejercicios.html`
5. `https://twimproject.com/insights/dependencia-emocional-como-dejar-de-depender.html`
6. `https://twimproject.com/insights/elegir-es-perder-psicologia-decision.html`
7. `https://twimproject.com/insights/hijo-no-es-vago-apatia-bachillerato.html`
8. `https://twimproject.com/insights/idealizacion-devaluacion-pareja.html`
9. `https://twimproject.com/insights/malestar-laboral-trabajas-para-otro-mapa-completo.html`
10. `https://twimproject.com/insights/obediencia-trabajo-casa.html`
11. `https://twimproject.com/insights/por-que-necesitas-que-te-validen.html`
12. `https://twimproject.com/insights/registro-semanal-malestar-activacion.html`
13. `https://twimproject.com/insights/senales-dependencia-emocional-confundes-con-amor.html`
14. `https://twimproject.com/insights/senales-trabajo-te-enferma.html`
15. `https://twimproject.com/insights/sindrome-del-impostor-cuando-mejor-te-va.html`
16. `https://twimproject.com/insights/sobrevivir-jornada-laboral-sin-desconectarte.html`
17. `https://twimproject.com/insights/tecnica-2-minutos-rumiacion.html`

### Landings y otros (7)

18. `https://twimproject.com/newsletter/`
19. `https://twimproject.com/nopuedoparar-taller.html`
20. `https://twimproject.com/psicologo-ansiedad-valencia/`
21. `https://twimproject.com/reto-7-dias.html`
22. `https://twimproject.com/soluciones/`
23. `https://twimproject.com/talleres/bachillerato-motivacion`
24. `https://twimproject.com/talleres/tdah-adolescentes`

---

## 2 · Verificación técnica (lo que NO es el problema)

### 2.1 · Sitemap

Las 24 URLs están todas listadas en `sitemap.xml` (verificado con grep). Google las **conoce**. No es problema de descubrimiento.

### 2.2 · `robots.txt`

```
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /private/
Disallow: /rompetengoquepreventa.html
Disallow: /anti-test-ddbeo.html
Sitemap: https://twimproject.com/sitemap.xml
```

Solo bloquea 2 URLs muy específicas (preventas) que no están en la lista de N/D. Allow global. No es bloqueo.

### 2.3 · Meta robots y canonical en páginas auditadas

Auditados manualmente: `del-deberia-al-quiero-ejercicios.html`, `senales-vivir-en-obligacion.html`, `juez-interno-como-desactivar.html`.

Los tres tienen:

- `<meta name="robots" content="index, follow">` ✓
- `<link rel="canonical" href="...">` correcto y autoreferenciado ✓
- Schema.org Article + BreadcrumbList ✓
- Open Graph + Twitter Card ✓

No hay `noindex` accidental, no hay canonical apuntando a otra URL, no hay redirect 301/302 raro.

### 2.4 · Discrepancia con/sin slash en talleres

URLs en GSC:
- `/talleres/bachillerato-motivacion` (sin slash final)
- `/talleres/tdah-adolescentes` (sin slash final)

URLs en sitemap:
- `/talleres/bachillerato-motivacion/` (con slash final)
- `/talleres/tdah-adolescentes/` (con slash final)

**Acción recomendada:** verificar en producción que ambas formas (con/sin slash) cargan o redirigen a la misma URL canónica. Si no, configurar redirect 301 desde la versión sin slash a la versión con slash en `netlify.toml`.

---

## 3 · Diagnóstico del problema real

El estado `Descubierta — actualmente sin indexar` con `Último rastreo: N/D` significa que **Google conoce las URLs pero ha decidido no priorizarlas para crawl**. Tres causas concretas (todas ya identificadas en `SEO_ANALISIS_2026-03-20.md` §3):

### 3.1 · Autoridad de dominio baja

El sitio es relativamente joven y tiene pocas señales externas (backlinks, citas, prensa). Sin autoridad acumulada, Google asigna **crawl budget bajo**. El crawler rastrea X páginas por sesión proporcional a la autoridad y va dejando atrás las URLs menos prioritarias.

Ya documentado en `SEO_ANALISIS_2026-03-20.md` §3.1: *"Para subir arriba del todo por tu nombre en Google, Google necesita señales claras de que eres una persona real y reconocible en tu categoría profesional [...] hay fuentes externas que te mencionan [...] tu web es el nodo principal de esa identidad digital"*.

### 3.2 · Crawl budget limitado en sitios pequeños

Con 44 URLs en sitemap y baja autoridad, Google rastrea 5-10 URLs por sesión y deja el resto pendiente. Es normal en sitios que están construyendo autoridad. **Tarda semanas o meses absorber todas las URLs nuevas**.

### 3.3 · Falta de señales de uso

Páginas sin tráfico, sin clics desde SERP, sin tiempo de permanencia, no envían señales positivas a Google. El crawler las despriorisa progresivamente.

---

## 4 · Auditoría adicional ejecutada en este PR

### 4.1 · Bug HTML del doble `<header>` (corregido)

Detectado en 4 archivos:

| Archivo | Estado tras este PR |
|---|---|
| `insights/del-deberia-al-quiero-ejercicios.html` | ✅ corregido |
| `insights/elegir-es-perder-psicologia-decision.html` | ✅ corregido |
| `insights/tecnica-2-minutos-rumiacion.html` | ✅ corregido |
| `insights/senales-vivir-en-obligacion.html` (no estaba en N/D pero tenía el bug) | ✅ corregido |

**El bug NO es la causa principal de la no-indexación** — hay URLs con bug que están indexadas (`senales-vivir-en-obligacion`) y URLs sin bug que no lo están. Pero es higiene técnica que mejora calidad percibida.

### 4.2 · Interlinking de las 24 URLs N/D

Auditoría con `grep -rl` en todos los HTML del repo:

| URL N/D | Enlaces internos entrantes |
|---|---|
| `elegir-es-perder-psicologia-decision` | **1 (huérfano)** |
| `ansiedad-productiva-presion-creatividad` | 2 |
| `sobrevivir-jornada-laboral-sin-desconectarte` | 2 |
| `idealizacion-devaluacion-pareja` | 3 |
| `registro-semanal-malestar-activacion` | 3 |
| `hijo-no-es-vago-apatia-bachillerato` | 4 |
| `obediencia-trabajo-casa` | 4 |
| `del-deberia-al-quiero-ejercicios` | 5 |
| `tecnica-2-minutos-rumiacion` | 5 |
| `deberia-dejar-trabajo-malestar` | 5 |
| `autoestima-baja-origen-que-nadie-te-explica` | 6 |
| `por-que-necesitas-que-te-validen` | 6 |
| `senales-dependencia-emocional-confundes-con-amor` | 6 |
| `senales-trabajo-te-enferma` | 6 |
| `sindrome-del-impostor-cuando-mejor-te-va` | 6 |
| `dependencia-emocional-como-dejar-de-depender` | 7 |
| `malestar-laboral-trabajas-para-otro-mapa-completo` | 8 |
| `nopuedoparar-taller` | 7 |
| `reto-7-dias` | 9 |
| `newsletter/` | 7 |
| `psicologo-ansiedad-valencia/` | 9 |
| `soluciones/` | 13 |
| `talleres/bachillerato-motivacion` | 9 |
| `talleres/tdah-adolescentes` | 10 |

**Conclusión:** la mayoría tiene interlinking razonable. **Solo 1 huérfano real** (`elegir-es-perder`) y 2-3 con interlinking débil. Confirma que **el problema NO es interlinking** — hay URLs con 8-13 enlaces que tampoco indexan.

### 4.3 · Acción ejecutada · refuerzo de interlinking

`elegir-es-perder-psicologia-decision.html` añadido al hub `insights/index.html` como séptima tarjeta del cluster "Autoexigencia / obligación". Pasa de 1 a 2 enlaces entrantes desde páginas reales.

---

## 5 · Plan de acción

### 5.1 · Acción inmediata · DANIEL (lado Search Console, máx. 10/día)

Solicitar indexación manual desde Google Search Console en este orden de prioridad:

**Día 1 (hoy o mañana, 10 URLs):**

1. `https://twimproject.com/newsletter/` — captación principal
2. `https://twimproject.com/psicologo-ansiedad-valencia/` — landing servicio prioritario
3. `https://twimproject.com/soluciones/` — hub conversión
4. `https://twimproject.com/reto-7-dias.html` — lead magnet
5. `https://twimproject.com/insights/del-deberia-al-quiero-ejercicios.html` — cluster autoexigencia
6. `https://twimproject.com/insights/juez-interno-como-desactivar.html` — referenciada en E5 podcast
7. `https://twimproject.com/insights/dependencia-emocional-como-dejar-de-depender.html` — pilar dependencia
8. `https://twimproject.com/insights/sindrome-del-impostor-cuando-mejor-te-va.html` — alta intención
9. `https://twimproject.com/insights/malestar-laboral-trabajas-para-otro-mapa-completo.html` — pilar burnout
10. `https://twimproject.com/insights/senales-trabajo-te-enferma.html` — alta intención

**Día 2 (10 URLs más):**

11-20. Las 10 URLs restantes del listado, priorizando insights con interlinking >5.

**Día 3 (4 URLs restantes + verificación):**

21-24. Las 4 finales + verificar Search Console para ver si las del Día 1 ya están rastreadas.

**Procedimiento por URL:**
- Search Console → Inspeccionar URL → pegar URL → "Solicitar indexación".
- Esperar 1-3 días para que Google rastree.
- Verificar el cambio de estado en GSC.

### 5.2 · Acción en curso · ESTE PR

Aplicado en commit asociado a este documento:

- ✅ Bug doble `<header>` corregido en 4 archivos.
- ✅ `elegir-es-perder-psicologia-decision` añadido al hub `insights/index.html`.
- ✅ Diagnóstico documentado (este archivo).

### 5.3 · Acción a 2-4 semanas · DANIEL + posible apoyo Claude

Construir autoridad externa según `SEO_ANALISIS_2026-03-20.md` §5.3 y §8:

- **Google Business Profile** completo y optimizado (paso prioritario semana 1 según SEO_ANALISIS §8).
- **Directorios profesionales** del sector psicología (Top Doctors, Psicología y Mente directorio, Colegio de Psicólogos de la Comunidad Valenciana).
- **Apariciones como invitado** en podcasts ajenos (psicología, divulgación, salud mental).
- **Guest posts / colaboraciones** en blogs de empresa, RRHH o salud.
- **Mantener presencia LinkedIn / X** (ya en marcha tras Carta #1) para que cuando alguien busque "Daniel Orozco psicólogo" haya señal.

### 5.4 · Acción a 1-3 meses · DANIEL

- Crear página dedicada `/daniel-orozco-abia/` ya identificada como prioridad en `SEO_ANALISIS_2026-03-20.md` §5.1 (existe `daniel-orozco-abia.html` — verificar que está optimizada con bio extensa, credenciales, medios, libros, etc.).
- Contenido nuevo: 6-9 piezas en clusters cerrados (`SEO_ANALISIS_2026-03-20.md` §5.2).
- Evaluar Cloudflare CDN si los Core Web Vitals lo requieren (`GUIA-IMPLEMENTACION-SEO.md` §FASE 4).

---

## 6 · Métricas a vigilar

### 6.1 · A 1 semana

- ¿Google Search Console muestra las URLs solicitadas como "Indexadas" o "Rastreada — actualmente sin indexar"? El segundo estado ya es progreso (Google las ha rastreado, falta decidir indexar).
- ¿Aparece tráfico orgánico en GA4 hacia las URLs forzadas?

### 6.2 · A 1 mes

- **Cobertura GSC:** ¿el número de URLs en estado N/D ha bajado?
- **Impresiones GSC:** ¿alguna de las 24 URLs aparece ya en SERPs?
- **Tráfico orgánico GA4:** ¿hay sesiones nuevas desde búsqueda orgánica hacia estas URLs?

### 6.3 · A 3 meses

- **CTR > 1%** en al menos las 5 URLs principales del listado.
- **Posicionamiento medio** de las keywords objetivo (`SEO_ANALISIS_2026-03-20.md` §5.2).
- **Backlinks externos:** mínimo 3-5 dominios distintos enlazando al sitio (Ahrefs, Search Console).

### 6.4 · Si en 3 meses siguen N/D

Entonces revisar:

- Posibles penalizaciones manuales en Search Console → Acciones manuales.
- Calidad real del contenido vs estándares E-E-A-T (puede que algunas páginas requieran reescritura más profunda).
- Si el sitemap necesita troceado (sitemap por subdirectorio).
- Solicitar revisión específica a Google si hay algún error técnico de servidor.

---

## 7 · Lo que NO conviene hacer

- ❌ Borrar y volver a crear las URLs.
- ❌ Modificar URLs (cambia el canonical y rompe enlaces externos si ya existen).
- ❌ Hacer ping al sitemap manualmente — Google ya no respeta este protocolo desde 2023.
- ❌ Usar "SEO indexer services" que prometen indexación rápida pagando — alta probabilidad de penalización.
- ❌ Saturar de enlaces internos para forzar PageRank — Google detecta el patrón y penaliza.
- ❌ Esperar pasivamente sin ejecutar §5.1 manual.

---

## 8 · Trazabilidad

- **Generado:** 5 mayo 2026.
- **Trigger:** capturas de Google Search Console enviadas por Daniel mostrando 24 URLs en estado N/D.
- **Aplicado en mismo PR:** correcciones de bug `<header>` + interlinking de `elegir-es-perder` + este documento.
- **Próxima revisión:** lunes 12 mayo 2026 (a 1 semana de las solicitudes manuales del Día 1).

## 9 · Refs

- `SEO_ANALISIS_2026-03-20.md` (análisis estratégico previo, 323 líneas).
- `GUIA-IMPLEMENTACION-SEO.md` (guía técnica previa, 367 líneas).
- `contenido-rrss/te-escribo-newsletters/PLAN-CAPTACION-30D.md` §4 (brief Meta Ads condicional, no relacionado pero relevante para conversión).
- `sitemap.xml` (44 URLs).
- `robots.txt`.
- Identidad editorial: `CLAUDE.md`.
