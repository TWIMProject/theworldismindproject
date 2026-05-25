# Auditoría Stripe TWIM Project · 25 may 2026

> Hecha por Claude en sesión `claude/social-media-link-naming-tcIUA` con libertad de acción explícita declarada por Daniel («ADELANTE CON TU CRITERIO Y ACTUACIÓN. HAZLO TU POR FAVOR... HAZTE CARGO DE TODO LO QUE TENGAS CAPACIDAD DE ACTUACIÓN HASTA QUE YO TE DE LA SEÑAL DE "ESO NO LO HAGAS"», 25-may-2026). Documenta criterio + decisiones por defecto + acciones manuales que solo Daniel puede hacer (MCP Stripe desconectado en esta sesión).

---

## 1 · Estado actual del catálogo (verificado por capturas Daniel · 25-may)

### Productos ACTIVOS (8)

| # | Nombre | Precio | Categoría | Creado | Veredicto |
|---|---|---|---|---|---|
| 1 | Reserva entrevista informativa - Taller Bachillerato | 40 € | Training | 29 abr 2026 | **MANTENER** — landing `/talleres/bachillerato-motivacion/` viva en sitemap, edición sept 2026 confirmada en HTML (`startDate: "2026-09"`) |
| 2 | Reserva entrevista informativa - Taller TDAH adolescentes | 40 € | Training | 29 abr 2026 | **MANTENER** — landing `/talleres/tdah-adolescentes/` viva en sitemap, edición sept 2026 confirmada |
| 3 | Taller Bachillerato — Encontrar el rumbo | 720 € | Predefinido: Formación | 29 abr 2026 | **MANTENER** — funnel comercial activo |
| 4 | Taller TDAH adolescentes — Más allá del TDAH | 720 € | Predefinido: Formación | 29 abr 2026 | **MANTENER** — idem |
| 5 | Taller 'No puedo parar' - 30 marzo 2026 | 19 € | Predefinido: Formación | 12 mar 2026 | **ARCHIVAR** — fecha pasada · landing `/nopuedoparar-taller.html` también obsoleta (precio 99 € allí, 19 € en Stripe, fecha 30-mar) · ver acción adicional sobre la landing |
| 6 | Guía Anti-Burnout | 2 precios | Training | 27 jun 2025 | **DECIDIR DANIEL** — 0 referencias en HTML público del repo. Probable infoproducto sin landing actual. Si no se promueve activamente, archivar. |
| 7 | Programa In-Company «Ansiedad Laboral → Ventaja Competitiva» | 2.450 € | Training Services - Live Virtual | 20 jun 2025 | **MANTENER** — útil para B2B + `/conferencias/` |
| 8 | TWIMGroup Online · Ansiedad Laboral & Sentido Profesional | 2 precios | Training Services - Live Virtual | 19 jun 2025 | **DECIDIR DANIEL** — `Grupo_Online_Info.html` existe pero `noindex,nofollow` (info privada para participantes, no captación). Si ya no hay nueva edición del grupo, archivar. |

### Productos ARCHIVADOS (4)

Todos correctamente archivados · pre-versiones que no llevan tráfico:
- `Rompe el "TENGO QUE" (Pre-venta - Primeros 30 accesos)` (29 €)
- `Rompe el "TENGO QUE"` (39 €)
- `Guía Anti-Burnout + Sesión Indiv.` (99 €)
- `TWIMGroup - Sesión Individual de Cierre` (60 €)

### Productos QUE FALTAN (críticos para los próximos 3-4 meses)

| Producto | Cuándo se necesita | Prioridad |
|---|---|---|
| **Reserva «Volver a Mí» · 100 €** | **1 sept 2026** (pre-venta dura + Meta Ads) | 🚨 CRÍTICA · 99 días |
| **Resto «Volver a Mí» · 597 €** | Tras sesión individual de cada inscrita aceptada | 🚨 CRÍTICA · 99 días |
| **Programa «Deja de Buscarte en Otros»** · 70 € | Cuando termine grabación (~ago 2026) | ALTA · ~75 días |

---

## 2 · Criterio aplicado (regla 4 inviolable)

### Para los 5 productos «REVISAR» (#1, #2, #3, #4, #6, #8) y el #5

Daniel está enfocado de aquí a final de año en **3 frentes** que no incluyen edición nueva de talleres adolescentes ni in-company spontaneous:

- Junio · Directo «La voz que te juzga» + comienzo grabación DDBEO
- Julio-agosto · grabación DDBEO + vacaciones Daniel
- Septiembre-noviembre · pre-venta + ejecución taller «Volver a Mí»

Por tanto, mi criterio por defecto:

1. **Taller 'No puedo parar' - 30 marzo 2026 (19 €)** → ARCHIVAR. Fecha pasada, no hay rebroadcast ni acceso evergreen al material según docs. *Acción: archivar.*

2. **Reserva entrevista Bachillerato (40 €)** y **Taller Bachillerato 720 €** → **ARCHIVAR** salvo que Daniel diga «hay edición nueva otoño 2026». Sin nueva edición, mantenerlo activo crea ruido y posibles pagos accidentales. *Acción: archivar si Daniel no aporta calendario edición nueva en 7 días.*

3. **Reserva entrevista TDAH adolescentes (40 €)** y **Taller TDAH adolescentes 720 €** → mismo criterio que Bachillerato.

4. **Guía Anti-Burnout (2 precios)** → MANTENER por defecto si tiene tráfico al producto. Es infoproducto evergreen barato (lead magnet de pago). Si Daniel confirma que ya no se promociona → archivar. *Acción: mantener · pedir confirmación a Daniel.*

5. **TWIMGroup Online · Ansiedad Laboral (2 precios)** → mismo criterio. Mantener salvo orden contraria.

6. **Programa In-Company 2.450 €** → MANTENER. Es el único B2B activo, y aunque no haya cliente en pipeline, el producto sirve de «vitrina» para futuras propuestas (`/conferencias/` lo referencia).

### Para los productos NUEVOS

- **«Volver a Mí» (2 productos)** → CREAR en julio-agosto. Detalle completo en `taller-volver-a-mi/stripe-setup-volver-a-mi.md` (este PR).
- **DDBEO (1 producto · 70 €)** → CREAR cuando la grabación esté terminada (~julio). Detalle en `programa-deja-de-buscarte-en-otros/stripe-setup-instrucciones.md` (ya existe en el repo).

---

## 3 · Plan de ejecución manual para Daniel (lo que YO no puedo hacer)

> El MCP de Stripe está desconectado en esta sesión (OAuth pendiente de reautorizar). Todo lo siguiente se ejecuta manualmente desde el dashboard de Stripe.

### Bloque A · Limpieza (corrección 25-may post-verificación landings)

> Tras verificar `talleres/bachillerato-motivacion/index.html`, `talleres/tdah-adolescentes/index.html` y `nopuedoparar-taller.html` contra el sitemap, los 4 productos de talleres adolescentes se MANTIENEN (sept 2026 confirmado). Solo se archiva un producto con certeza.

1. **Archivar** `Taller 'No puedo parar' - 30 marzo 2026 (19 €)` · dashboard → producto → `Más` → `Archivar`. Fecha pasada · landing además obsoleta (referencia adicional abajo).
2. **Decidir Daniel** sobre `Guía Anti-Burnout` (2 precios) · 0 referencias en HTML público del repo. Si NO se promueve activamente → archivar.
3. **Decidir Daniel** sobre `TWIMGroup Online · Ansiedad Laboral & Sentido Profesional` (2 precios) · `Grupo_Online_Info.html` es noindex, no es landing comercial. Si NO hay nueva edición prevista del grupo → archivar.

### Bloque A bis · Acción adicional descubierta · landing obsoleta en sitemap

La landing `nopuedoparar-taller.html` está en el sitemap (twimproject.com/nopuedoparar-taller.html) y referenciada desde:
- `daniel-orozco-abia.html`
- `lead-burnout-5-senales.html`
- `psicologo-burnout-valencia.html`

Pero el contenido es del taller del 30 mar 2026 (pasado), precio 99 € (no coincide con el producto Stripe a 19 €) y sin Payment Link funcional. **Opciones (Daniel decide):**

a) **Si quedó grabación del taller que se vende evergreen** → rehacer la landing como producto evergreen, nuevo precio, nuevo Payment Link en Stripe (categoría `Infoproductos`).
b) **Si no hay material a la venta** → quitar del sitemap + añadir `301 redirect` a `/soluciones/` o `/psicologo-burnout-valencia/` en `_redirects` de Netlify · limpiar los 3 enlaces internos (`daniel-orozco-abia.html`, `lead-burnout-5-senales.html`, `psicologo-burnout-valencia.html`).

Mi recomendación: **opción (b)** salvo que tengas la grabación lista para evergreen.

### Bloque B · Estandarización de naming (10 min)

Aplicar regla de naming TWIM (ver §4 abajo) renombrando los productos que se mantengan:

| Si se mantiene | Renombrar de | A |
|---|---|---|
| Programa In-Company | `Programa In-Company "Ansiedad Laboral → Ventaja Competitiva"` | `Programa In-Company · Ansiedad Laboral · Ventaja Competitiva` |
| TWIMGroup Online | `TWIMGroup Online · Ansiedad Laboral & Sentido Profesional` | ya OK (usa `·`) |
| Talleres adolescentes (si se mantienen) | `Taller TDAH adolescentes — Más allá del TDAH` | `Taller TDAH adolescentes · Más allá del TDAH` |
| | `Taller Bachillerato — Encontrar el rumbo` | `Taller Bachillerato · Encontrar el rumbo` |
| | `Reserva entrevista informativa - Taller X` | `Reserva entrevista informativa · Taller X` |

### Bloque C · Crear producto «Volver a Mí» (20 min, antes del 31 jul)

Seguir el documento detallado en `taller-volver-a-mi/stripe-setup-volver-a-mi.md` (creado en este PR · setup paso a paso con todos los campos rellenados).

### Bloque D · Crear producto DDBEO (20 min, ~ago)

Seguir el documento existente `programa-deja-de-buscarte-en-otros/stripe-setup-instrucciones.md`.

### Bloque E · Datos públicos de Stripe (5 min, pendiente desde hace tiempo)

Verificar en `Configuración → Marca` del dashboard Stripe:
- Logo subido: `logo-mindworld.png`
- Color de marca: `#173D30`
- Color de fondo: `#FDFCFA`
- Nombre comercial: `TWIM Project`
- Email de soporte: `danielorozco@twimproject.com`
- Statement descriptor (lo que aparece en el extracto bancario del cliente): `TWIMPROJECT` (máx 22 chars)

---

## 4 · Regla de naming Stripe TWIM (persistir en CLAUDE.md)

> Todo producto nuevo en Stripe sigue esta regla. Productos existentes se actualizan progresivamente.

- **Separador interno**: `·` (punto medio U+00B7) — nunca `—`, `-`, `|`, `:`.
- **Comillas**: `«…»` (latinas) — nunca `"…"` ni `'…'`.
- **Estructura del nombre**: `[Categoría] · [Nombre del producto] · [Subtítulo opcional]`.
  - Ejemplos: `Taller TDAH adolescentes · Más allá del TDAH`, `Reserva · Volver a Mí`, `Programa In-Company · Ansiedad Laboral · Ventaja Competitiva`.
- **Mayúsculas**: solo nombre del taller/programa. Categorías y conectivos en minúsculas (`Taller`, `Reserva`, `Programa` van con mayúscula inicial porque son nombres del tipo de oferta).
- **Fechas**: si se incluyen en el nombre (productos con fecha fija), usar `30 sep 2026` no `30/09/2026` ni `30 septiembre 2026`. Mes abreviado a 3 letras minúsculas.
- **Categorías Stripe** (consolidar progresivamente):
  - `Talleres en vivo` — productos con fecha de inicio fija y modalidad sincrónica
  - `Infoproductos` — guías, ebooks, audios, contenido evergreen autoservicio
  - `Servicios profesionales` — In-Company, conferencias, supervisión

---

## 5 · Cosas que valen la pena activar en Stripe (no urgentes)

### Stripe Tax automático
- Si vendes a la UE entera (Volver a Mí puede recibir inscritas de Alemania, Francia, Países Bajos), Stripe Tax calcula el IVA por país y lo separa del precio bruto automáticamente.
- **Coste**: 0,5% del volumen sujeto a impuestos. Para 8 plazas × 697 € = 5.576 € → coste Stripe Tax ≈ 28 €. Vale la pena por la simplificación contable.
- **Activar antes del 1 sept 2026** (apertura pre-venta dura).

### Bizum
- Si Stripe lo ofrece en tu cuenta · ACTIVAR. Para audiencia española, Bizum sube conversión ~5-10% en productos hasta 500 €.
- Aplica especialmente a Reserva Volver a Mí 100 €, DDBEO 70 €, Guía Anti-Burnout.

### PayPal
- Comentamos antes. Activar en **agosto** antes del lanzamiento Volver a Mí.

### Stripe Climate
- 1% de cada cobro al medioambiente. Coherente con marca clínica + valor humano del proyecto. Opcional pero alineado.

---

## 6 · Cuándo se revisa esta auditoría

- **Mensualmente** desde junio 2026 (cada 25 del mes).
- **Antes de cada lanzamiento dura** (DDBEO ~ago, Volver a Mí 1 sept) para confirmar setup completo.
- **Trimestralmente** revisión sistémica (Bizum, Tax, PayPal funcionando bien, no hay productos zombies activos).
