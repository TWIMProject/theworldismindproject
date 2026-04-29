# Talleres · Stripe Payment Links

> Documento interno. **No publicar estos enlaces en ninguna landing pública** mientras estés en Opción A (privado): se mandan por WhatsApp/email solo a padres que ya hayan pasado la reunión informativa y encajen en el grupo.

---

## Talleres Septiembre 2026

| Taller | Precio | Plazas | Payment Link |
|---|---|---|---|
| **TDAH adolescentes — Más allá del TDAH** | 720 € | 6 | https://buy.stripe.com/28E5kD5T45SZasP8jm2sM08 |
| **Bachillerato — Encontrar el rumbo** | 720 € | 6 | https://buy.stripe.com/3cI7sL2GS81758vgPS2sM09 |

Stripe IDs (referencia técnica para webhook futuro):

| Taller | Product ID | Price ID | Payment Link ID |
|---|---|---|---|
| TDAH | `prod_UQPvWiUSDThMzy` | `price_1TRZ6RFW3OLCwM3HhOLpGNaK` | `plink_1TRZ6hFW3OLCwM3H26cHJiy5` |
| Bachillerato | `prod_UQPvQMyWlvVCmm` | `price_1TRZ6UFW3OLCwM3HHbJYZKR0` | `plink_1TRZ6kFW3OLCwM3HgSGrmmfF` |

---

## Plantilla mensaje post-reunión (WhatsApp / email)

> Hola [NOMBRE],
>
> Gracias por la reunión de [DÍA]. Como hemos hablado, creo que [NOMBRE_HIJO] puede encajar bien en el grupo de [TDAH / Bachillerato] que arranca en septiembre 2026.
>
> Aquí tienes el enlace para reservar la plaza:
>
> 👉 [PAYMENT_LINK]
>
> Son 720 € (pago único). Una vez recibas la confirmación de Stripe, te llega de mi parte un email con los detalles logísticos del primer mes (fechas exactas, lugar, qué llevar).
>
> Si tienes cualquier duda antes de pagar, escríbeme aquí mismo.
>
> Un abrazo,
> Daniel

---

## Configuración usada

- **Modelo:** Pago único en EUR
- **Cantidad ajustable por cliente:** No
- **Datos del cliente recopilados:** Email + nombre (Stripe los pide automáticamente)
- **Códigos promocionales:** No configurados (puedes activarlos desde el dashboard de Stripe si quieres ofrecer alguno puntual)
- **Límite de pagos:** ⚠️ **Por configurar manualmente en el dashboard.** La API no permite establecer "Limit number of payments". Ve a cada Payment Link en https://dashboard.stripe.com/payment-links → Avanzado → "Limit the number of payments" → 6.

---

## Cuando alguien pague (proceso semi-manual hasta webhook)

1. Te llega notificación de Stripe.
2. **Manualmente** en MailerLite añades su email al grupo correspondiente:
   - `Taller TDAH - Inscritas` (ID `186093787887437444`)
   - `Taller Bachillerato - Inscritas` (ID `186093790595909010`)
3. Eso lo saca automáticamente de la secuencia activa de captación.
4. Le mandas el email de bienvenida con detalles logísticos (plantilla aún por crear).

---

## Webhook automático (fase 2, cuando hayas validado 1-2 inscripciones reales)

Plan técnico:
1. Configurar webhook en Stripe: evento `checkout.session.completed` → endpoint Netlify Function `/.netlify/functions/stripe-webhook`
2. La function:
   - Verifica la firma del webhook con `STRIPE_WEBHOOK_SECRET`
   - Identifica qué taller compró (por Price ID — ya están en este doc)
   - Llama a la API de MailerLite para añadir al cliente al grupo `Taller TDAH - Inscritas` o `Taller Bachillerato - Inscritas`
   - Dispara email de confirmación con detalles logísticos del taller

Cuando me digas "ya tengo 1-2 inscripciones, monta el webhook", lo conecto.

---

## Tax / IVA

⚠️ Pendiente de revisar con tu gestor:
- Algunos talleres psicoeducativos pueden estar **exentos de IVA** por ser servicios sanitarios prestados por psicólogo colegiado.
- Si aplica exención: actualiza el `tax_code` del producto en Stripe a `txcd_20030000` (servicios educativos / formación) con `tax_behavior: exclusive`.
- Activa Stripe Tax solo cuando lo confirmes con tu gestor.
