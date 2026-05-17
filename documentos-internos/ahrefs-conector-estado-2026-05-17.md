# Ahrefs · Estado del conector · 17 may 2026

> Documento operativo · 17 may 2026 · sesión `claude/improve-proposal-quality-pq3d9`.
> Daniel pidió lanzar la primera pasada de Ahrefs (rank tracking keywords Valencia + estado de backlinks + Brand Radar de visibilidad en IA) y dejar un baseline escrito para disparar la v3 del doc CEO.
> Este documento deja escrito **por qué ese baseline no se pudo generar hoy**, para que ninguna sesión futura vuelva a quemar turnos intentándolo a ciegas.
> **Actualización 17-may (ver §0): la decisión final es NO invertir en Ahrefs.** El baseline ya **no** es un objetivo activo; todo lo de abajo queda archivado como referencia por si Daniel reabre el tema explícitamente.

---

## 0 · DECISIÓN FINAL · 17 may 2026 · NO se invierte en Ahrefs

> Decisión declarada por Daniel el 17 may 2026, en la misma sesión.

**Daniel decidió NO invertir en el acceso de pago a Ahrefs.** El tema queda **cerrado**, no «pendiente de decidir». Consecuencias operativas, vinculantes para toda sesión futura:

- ❌ Ninguna sesión debe proponer activar/contratar Ahrefs, ni reintentar la pasada, ni tratar «Ahrefs disponible» como trigger para la v3 del doc CEO. Ese trigger queda **anulado por decisión** (el caveat del doc CEO §6 se asume permanente, no transitorio).
- ❌ No re-litigar la conveniencia de Ahrefs en cada sesión. La decisión está tomada y razonada (abajo). Solo se reabre si **Daniel lo pide explícitamente**.
- ✅ Fuente primaria de SEO / indexación / posición: **Google Search Console** (gratis, ya en uso — plan §5.1 del `seo-indexacion-search-console-2026-05-05.md`). El proyecto opera sin Ahrefs.
- ✅ El resto de este documento (diagnóstico técnico §1-§2, mapa de ejecución §3, requisitos §4) queda **archivado como referencia** por si Daniel reabre el tema; no es una invitación a reabrirlo.

**Razonamiento (resumen, fundamentado en el repo):** Ahrefs mide, no genera tráfico; el diagnóstico SEO ya está hecho y su ejecución (autoridad externa, §5.3 del doc SEO) no está bloqueada por falta de datos Ahrefs; GSC cubre gratis lo accionable en esta fase; el tier API es caro; y la prioridad real es la del `veredicto-analisis-oportunidades-negocio-15-may-2026.md` (terminar/grabar el programa + motor newsletter/libro). El crecimiento orgánico de la newsletter (30 → 63 total en ~16 días, ver `metricas-newsletter-baseline-17-may-2026.md`) confirma que el dinero rinde más en ejecución que en analítica de pago.

---

## TL;DR

- El conector Ahrefs (MCP API v3) está **disponible como herramienta pero bloqueado por plan**. Toda llamada de datos sobre `twimproject.com` devuelve `MCP error -32001: { "error": "Insufficient plan" }`.
- Verificado hoy con **tres endpoints independientes**, incluido el que la propia API documenta como gratuito y sin consumo de unidades:
  - `subscription-info-limits-and-usage` (gratuito, sin unidades) → **Insufficient plan**.
  - `site-explorer-domain-rating` (`twimproject.com`, 2026-05-17) → **Insufficient plan**.
  - `site-explorer-backlinks-stats` (`twimproject.com`, mode=subdomains, 2026-05-17) → **Insufficient plan**.
- El esquema de las herramientas (`doc`) **sí** responde: el bloqueo es de **nivel de plan/suscripción**, no de cuota de unidades agotada ni de credencial caída ni de fallo transitorio. Reintentar no lo resuelve.
- **No se ha fabricado ningún baseline.** Inventar números de DR/backlinks/keywords sin dato real es exactamente el patrón que `veredicto-analisis-oportunidades-negocio-15-may-2026.md` §2.1 prohíbe ("la tabla cuelga de un número inventado").
- **Impacto en el doc CEO:** el `ceo-vista-completa-v2-1-mayo-2026.md`, en su sección **«Cierre»** (nota técnica final), lista *«Cuando aparezca dato nuevo importante (Ahrefs disponible…), generar v3»* como uno de los triggers para generar la v3. **Ese trigger NO está cumplido — y además queda anulado por la decisión de Daniel del 17-may (ver §0): no se invierte.** El caveat de §6 ("Datos de Ahrefs no disponibles esta sesión por límite de plan; cifras son aproximaciones del sector") **sigue vigente** — no es un problema de esa sesión concreta, es el estado estructural del plan.

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

## 4 · (Archivado) Qué requeriría desbloquear Ahrefs — NO aplicable

> Sección **archivada**. Daniel decidió el 17-may **no invertir** (ver §0). Se conserva solo por si el tema se reabre explícitamente; no es una acción pendiente.

El sandbox no puede subir el plan. Lo que requeriría (si algún día Daniel reabre):

1. Verificar en la cuenta Ahrefs qué plan tiene la API key conectada al MCP. El acceso a **API v3** requiere plan con add-on de API (los planes estándar Lite/Standard **no** incluyen acceso API por defecto; suele requerir Advanced/Enterprise + unidades API, o el add-on API explícito).
2. Decidir si el coste del acceso API justifica el lever. Según el filtro del CEO doc (§1, §7.4): Ahrefs sirve al problema #1 (tráfico cualificado) y a un cuello ya documentado (autoridad/indexación) → es de los pocos gastos de herramienta alineados, no dispersión. Pero el coste real del tier API de Ahrefs no es trivial; es decisión de Daniel, no automática.
3. Alternativa de coste cero mientras no haya plan API: **Google Search Console** sigue siendo la fuente primaria para indexación/posición (ya en uso, plan §5.1 del doc SEO del 5-may), y es lo que el doc SEO §6.3 ya cita junto a Ahrefs. Ahrefs añade backlinks de terceros y Brand Radar, que GSC no da — ese es su valor diferencial real, no el ranking propio.

---

## 5 · Inoculación para futuras sesiones

- ❌ "Genera el baseline Ahrefs / dispara la v3 del CEO doc porque Ahrefs ya está" → **NO. Decisión cerrada (§0): no se invierte en Ahrefs.** No reintentar la pasada, no proponer Ahrefs, no sondear el conector — salvo que **Daniel reabra el tema explícitamente**.
- ✅ Solo si Daniel reabre explícitamente: antes de cualquier pasada, hacer **una** llamada barata de sondeo (`site-explorer-domain-rating` sobre `twimproject.com`). Si devuelve `Insufficient plan`, **parar** y no encadenar más llamadas. Si devuelve datos, ejecutar el mapa del §3.
- Regla operativa confirmada (coherente con `veredicto-analisis-oportunidades-negocio-15-may-2026.md` §5): ante "haz la pasada de la herramienta X", **verificar disponibilidad real antes de prometer output**; un hallazgo negativo bien escrito vale más que un baseline inventado.

---

## 6 · Refs

- `ceo-vista-completa-v2-1-mayo-2026.md` §6 (caveat Ahrefs) y cierre (trigger v3).
- `seo-indexacion-search-console-2026-05-05.md` §3 (diagnóstico autoridad/crawl), §5.3 (plan autoridad externa), §6.3 (meta backlinks, cita Ahrefs).
- `veredicto-analisis-oportunidades-negocio-15-may-2026.md` §2.1 y §5 (prohibición de números inventados, patrón de inoculación).
- `CLAUDE.md` (regla de método: verificar el repo y la realidad antes de producir output).

---

— Nota de trazabilidad: generado el 17-05-2026 en sesión `claude/improve-proposal-quality-pq3d9`. Trigger: petición de Daniel de lanzar la pasada Ahrefs. **Decisión cerrada el 17-05-2026 (§0): NO se invierte en Ahrefs.** No hay próxima revisión salvo reapertura explícita de Daniel.
