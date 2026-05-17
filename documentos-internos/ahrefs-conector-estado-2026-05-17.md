# Ahrefs · Estado del conector · 17 may 2026

> Documento operativo · 17 may 2026 · sesión `claude/improve-proposal-quality-pq3d9`.
> Daniel pidió lanzar la primera pasada de Ahrefs (rank tracking keywords Valencia + estado de backlinks + Brand Radar de visibilidad en IA) y dejar un baseline escrito para disparar la v3 del doc CEO.
> Este documento deja escrito **por qué ese baseline no se pudo generar hoy y qué hace falta exactamente para que sea posible**, para que ninguna sesión futura vuelva a quemar turnos intentándolo a ciegas.

---

## TL;DR

- El conector Ahrefs (MCP API v3) está **disponible como herramienta pero bloqueado por plan**. Toda llamada de datos sobre `twimproject.com` devuelve `MCP error -32001: { "error": "Insufficient plan" }`.
- Verificado hoy con **tres endpoints independientes**, incluido el que la propia API documenta como gratuito y sin consumo de unidades:
  - `subscription-info-limits-and-usage` (gratuito, sin unidades) → **Insufficient plan**.
  - `site-explorer-domain-rating` (`twimproject.com`, 2026-05-17) → **Insufficient plan**.
  - `site-explorer-backlinks-stats` (`twimproject.com`, mode=subdomains, 2026-05-17) → **Insufficient plan**.
- El esquema de las herramientas (`doc`) **sí** responde: el bloqueo es de **nivel de plan/suscripción**, no de cuota de unidades agotada ni de credencial caída ni de fallo transitorio. Reintentar no lo resuelve.
- **No se ha fabricado ningún baseline.** Inventar números de DR/backlinks/keywords sin dato real es exactamente el patrón que `veredicto-analisis-oportunidades-negocio-15-may-2026.md` §2.1 prohíbe ("la tabla cuelga de un número inventado").
- **Impacto en el doc CEO:** el `ceo-vista-completa-v2-1-mayo-2026.md` cierre línea 638 pone "Ahrefs disponible" como uno de los triggers para generar la v3. **Ese trigger NO está cumplido.** El caveat de §6 ("Datos de Ahrefs no disponibles esta sesión por límite de plan; cifras son aproximaciones del sector") **sigue vigente** — no es un problema de esa sesión concreta, es el estado estructural del plan.

---

## 1 · Qué se intentó exactamente (trazabilidad)

| Llamada | Parámetros | Resultado |
|---|---|---|
| `subscription-info-limits-and-usage` | (sin parámetros) | `-32001 Insufficient plan` |
| `site-explorer-domain-rating` | `target=twimproject.com`, `date=2026-05-17` | `-32001 Insufficient plan` |
| `site-explorer-backlinks-stats` | `target=twimproject.com`, `mode=subdomains`, `date=2026-05-17` | `-32001 Insufficient plan` |
| `doc` (esquemas de varias tools) | varias | OK (la documentación responde sin plan) |

Diagnóstico: el endpoint de suscripción está descrito por la propia API como *"free and does not consume any API units"*. Que **ese** endpoint también devuelva `Insufficient plan` confirma que el bloqueo es de **tier de plan** (la API key asociada no tiene un plan con acceso a API v3 / MCP), no una cuota mensual agotada que se recupere sola ni un corte temporal.

---

## 2 · Lo que esta pasada SÍ resuelve (valor del hallazgo negativo)

No es una pasada fallida: cierra una suposición que llevaba colgando desde el 1-may.

1. **Desbloquea la duda del doc CEO.** Hasta hoy quedaba la lectura ambigua de "Ahrefs no disponible *esta sesión*" (sonaba a problema puntual). Queda escrito que es **estructural de plan**. La v3 del CEO doc **no debe** generarse esperando que Ahrefs aparezca solo.
2. **Protege el rigor.** El posicionamiento competitivo del CEO doc §6 está construido sobre aproximaciones del sector declaradas como tales. Esto confirma que **deben seguir marcadas como aproximaciones** hasta que haya plan. Nadie debe "rellenar" esa tabla con datos Ahrefs sin que el plan exista.
3. **Evita quemar sesiones futuras.** Sin esta nota, cada sesión que reciba "haz la pasada de Ahrefs" repetiría las mismas 3 llamadas, mismo error, mismos turnos perdidos.

---

## 3 · Qué entregaría Ahrefs el día que haya plan (mapa de ejecución listo)

Cuando el plan se active, esta es la pasada exacta a ejecutar (mapeada a necesidades ya documentadas en el repo, no genéricas). Dejar esto escrito convierte una sesión futura de exploración en una de ejecución directa.

### 3.1 · SEO local Valencia — el problema #1 (tráfico cualificado)
- `serp-overview` + `site-explorer-organic-keywords` para las keywords del CEO doc §6.4:
  - `psicólogo dependencia emocional Valencia`
  - `psicólogo burnout Valencia`
  - `psicologo ansiedad valencia` (landing ya desplegada)
- Objetivo: posición real de `twimproject.com` vs las 20-40 consultas privadas de Valencia con las que compite (CEO §6.4).

### 3.2 · Autoridad de dominio y backlinks — el cuello SEO documentado
- `site-explorer-domain-rating` + `site-explorer-backlinks-stats` + `site-explorer-referring-domains`.
- Objetivo: medir contra la meta de `seo-indexacion-search-console-2026-05-05.md` §6.3 ("mínimo 3-5 dominios distintos enlazando") y verificar si el plan de autoridad externa de ese doc §5.3 (GBP, directorios, guest posts, podcasts ajenos) está moviendo la aguja. Diagnóstico raíz de las 24 URLs no indexadas (autoridad baja + crawl budget), no técnico.

### 3.3 · Brand Radar — visibilidad en respuestas de IA (lever nuevo, alineado)
- `brand-radar-mentions-overview` / `brand-radar-sov-overview` / `brand-radar-cited-domains`.
- Objetivo: si ChatGPT/Perplexity citan a TWIM / Daniel Orozco cuando el público 25-50 pregunta por dependencia emocional, ansiedad o autoexigencia. **No abre canal nuevo** (no es dispersión vs Camino A): sirve al único problema documentado — tráfico cualificado al embudo.

### 3.4 · Web Analytics Ahrefs
- Complementa GA4 (`G-VMMZ1TKWZ0`) en fuentes/canales. Secundario respecto a 3.1–3.3.

---

## 4 · Acción de desbloqueo (lado Daniel — fuera del sandbox)

El sandbox no puede subir el plan. Acción manual de Daniel:

1. Verificar en la cuenta Ahrefs qué plan tiene la API key conectada al MCP. El acceso a **API v3** requiere plan con add-on de API (los planes estándar Lite/Standard **no** incluyen acceso API por defecto; suele requerir Advanced/Enterprise + unidades API, o el add-on API explícito).
2. Decidir si el coste del acceso API justifica el lever. Según el filtro del CEO doc (§1, §7.4): Ahrefs sirve al problema #1 (tráfico cualificado) y a un cuello ya documentado (autoridad/indexación) → es de los pocos gastos de herramienta alineados, no dispersión. Pero el coste real del tier API de Ahrefs no es trivial; es decisión de Daniel, no automática.
3. Alternativa de coste cero mientras no haya plan API: **Google Search Console** sigue siendo la fuente primaria para indexación/posición (ya en uso, plan §5.1 del doc SEO del 5-may), y es lo que el doc SEO §6.3 ya cita junto a Ahrefs. Ahrefs añade backlinks de terceros y Brand Radar, que GSC no da — ese es su valor diferencial real, no el ranking propio.

---

## 5 · Inoculación para futuras sesiones

- ❌ "Genera el baseline Ahrefs / dispara la v3 del CEO doc porque Ahrefs ya está" → **falso mientras este documento no se haya actualizado con una verificación OK**. El gate es de plan, no transitorio.
- ✅ Antes de reintentar la pasada Ahrefs, hacer **una** llamada barata de sondeo (`site-explorer-domain-rating` sobre `twimproject.com`). Si devuelve `Insufficient plan`, **parar**, no encadenar más llamadas, y solo actualizar la fecha de este doc. Si devuelve datos, ejecutar el mapa del §3 y entonces sí generar el baseline + disparar v3 del CEO doc.
- Regla operativa confirmada (coherente con `veredicto-…-15-may-2026.md` §5): ante "haz la pasada de la herramienta X", **verificar disponibilidad real antes de prometer output**; un hallazgo negativo bien escrito vale más que un baseline inventado.

---

## 6 · Refs

- `ceo-vista-completa-v2-1-mayo-2026.md` §6 (caveat Ahrefs) y cierre (trigger v3).
- `seo-indexacion-search-console-2026-05-05.md` §3 (diagnóstico autoridad/crawl), §5.3 (plan autoridad externa), §6.3 (meta backlinks, cita Ahrefs).
- `veredicto-analisis-oportunidades-negocio-15-may-2026.md` §2.1 y §5 (prohibición de números inventados, patrón de inoculación).
- `CLAUDE.md` (regla de método: verificar el repo y la realidad antes de producir output).

---

— Nota de trazabilidad: generado el 17-05-2026 en sesión `claude/improve-proposal-quality-pq3d9`. Trigger: petición de Daniel de lanzar la pasada Ahrefs. Próxima revisión: cuando Daniel confirme cambio de plan API Ahrefs; entonces re-sondear según §5 y, si OK, ejecutar §3.
