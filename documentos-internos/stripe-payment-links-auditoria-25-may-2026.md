# Stripe Payment Links · auditoría 25 may 2026

> Auditoría completa de los 4 Payment Links activos en producción, con sus IDs, productos vinculados, URLs y configuración. Hecha bajo libertad de acción al cierre del día (Daniel saturado). Las mejoras aplicables vía API ya se ejecutaron · las que requieren UI/decisión están listadas.

---

## 1 · Inventario verificado (4 Payment Links activos)

| Producto | Payment Link ID | URL pública | Estado |
|---|---|---|---|
| Reserva entrevista Bachillerato (40 €) | `plink_1TRapuFW3OLCwM3H7CVk5y89` | `https://buy.stripe.com/28E7sLchsgxD58varu2sM0b` | ✅ Live, CTA primario en landings |
| Reserva entrevista TDAH (40 €) | `plink_1TRaXJFW3OLCwM3HTufzolAL` | `https://buy.stripe.com/9B6dR9bdo95bfN99nq2sM0a` | ✅ Live, CTA primario en landings |
| Taller Bachillerato 720 € | `plink_1TRZ6kFW3OLCwM3HgSGrmmfF` | `https://buy.stripe.com/3cI7sL2GS81758vgPS2sM09` | ✅ Live, uso post-entrevista |
| Taller TDAH 720 € | `plink_1TRZ6hFW3OLCwM3H26cHJiy5` | `https://buy.stripe.com/28E5kD5T45SZasP8jm2sM08` | ✅ Live, uso post-entrevista |

NO existen Payment Links para:
- Programa In-Company 2.450 € · gestionado ad-hoc (coherente, contacto previo obligatorio)
- Volver a Mí Reserva 100 € · producto archivado, payment link se crea al activar (julio)
- Volver a Mí Resto 597 € · idem

---

## 2 · Mejoras aplicadas vía API (25-may-2026)

### Aplicado a los 2 Payment Links de 720 € (Bachillerato + TDAH)

| Cambio | Antes | Después | Por qué |
|---|---|---|---|
| `automatic_tax.enabled` | `false` | **`true`** | Necesario para que Stripe Tax calcule IVA automático cuando Daniel lo active. Sin esto, aunque active Stripe Tax, estos checkouts saldrían sin IVA. |
| `allow_promotion_codes` | `false` | **`true`** | Alinear con los Payment Links de 40 €. Permite ofrecer códigos promocionales («EARLY», «AMIGOS», etc.) si quiere para captación inicial. |

Los 2 de 40 € ya tenían ambos activos · no requirieron cambios.

---

## 3 · Gaps pendientes (no aplicados, requieren decisión)

### Gap A · Redirect personalizado tras pago en los 720 €

Los 2 Payment Links de 720 € usan `hosted_confirmation` (página genérica de Stripe). Los 2 de 40 € redirigen a `https://twimproject.com/talleres/gracias-reserva.html?utm_source=stripe&utm_taller=bach|tdah`.

**Por qué importa:** página propia post-pago permite:
- Tracking GA4 / Meta del evento conversión
- Mensaje editorial alineado con la voz Te escribo
- Cross-sell / next step (qué pasa ahora, cuándo le llega info de la sesión 1)

**Por qué no lo aplico ahora:** requiere crear página HTML nueva `gracias-inscripcion.html` (texto distinto al de gracias-reserva, ya que aquí ya cobré, no es reserva). Trabajo de 15 min cuando Daniel pueda confirmar el copy editorial post-pago.

### Gap B · Limit number of payments (max 6 por edición)

El campo `restrictions.completed_sessions.limit` NO se expone vía API según los endpoints disponibles · es config UI-only. Daniel lo gestiona desde el dashboard de cada Payment Link.

Estado actual desconocido (no se ve vía API). **Pendiente Daniel verificar manualmente** y poner `6` en cada uno antes de campañas de captación serias (talleres adolescentes están limitados a 6 plazas por edición).

### Gap C · Bizum nativo en checkout

Los 4 Payment Links tienen `payment_method_types: null`, lo que significa que aceptan TODOS los métodos del PMC `Default · Tu cuenta` (Tarjetas, Apple Pay, Google Pay, Link, Klarna actualmente).

**Cuando Daniel active Bizum nativo** en el PMC, automáticamente aparecerá en estos checkouts sin necesidad de actualizar nada vía API. ✅ Sin acción técnica requerida.

---

## 4 · Acciones manuales Daniel · resumen Stripe Payment Links

1. **Verificar `Limit number of payments = 6`** en cada uno de los 4 Payment Links (UI · dashboard de cada plink). Sin esto, en el mejor de los casos puedes acabar con 7-8 inscritos a un grupo de 6.
2. **Activar Bizum nativo** (decisión global de cuenta) · ya documentado en `cierre-sesion-2026-05-25.md`. Una vez activo, los 4 Payment Links lo ofrecerán automáticamente.
3. **Cuando quieras, decide sobre el Gap A** · si crear `gracias-inscripcion.html` propia para los 720 € o aceptar la página genérica de Stripe. Sin urgencia.

---

**Última actualización:** 25 may 2026 · sesión `claude/social-media-link-naming-tcIUA`.
