# Talleres · Stripe — Modelo deposit + taller

> Documento interno. Define el flujo de cobro de los talleres TDAH y Bachillerato adolescentes.
>
> **Decisión de Daniel (29 abril 2026):** nadie paga 720 € sin haber pasado primero la entrevista informativa. La entrevista sigue siendo gratuita en concepto, pero hay un **deposit de 40 € como reserva** para garantizar que los padres se presentan.

---

## 1 · El flujo en 3 escenarios

| Escenario | Qué cobra Daniel | Reembolso | Por qué |
|---|---|---|---|
| Padre **paga deposit** y **NO se presenta** a la reunión | 40 € retenidos | ❌ no reembolsable | Compensa el tiempo perdido |
| Padre **paga deposit** y **SE PRESENTA** | 40 € reembolsados al instante | ✅ íntegro | La entrevista es gratuita en concepto — sólo era reserva |
| Padre se presenta + se inscribe al taller | 720 € cobro adicional (más el reembolso del deposit) | ✅ deposit reembolsado · cobra 720 € por el taller | Limpio y sin liosos cálculos. Entrevista gratis + taller a precio íntegro. |

**Importante:** no se aplica el deposit "a cuenta del taller". Si se aplicara, el padre con interés legítimo terminaría pagando 720 (= 40 deposit + 680 taller) cuando podría pagar 720 directos. El modelo "reembolso íntegro al presentarse" mantiene la promesa original de "entrevista gratuita" intacta.

---

## 2 · Productos en Stripe

### 2.1 · Productos deposit (40 €) — ✅ LIVE

| Taller | Payment Link | Estado |
|---|---|---|
| Reserva entrevista TDAH 40 € | https://buy.stripe.com/9B6dR9bdo95bfN99nq2sM0a | ✅ live · CTA primario en landings |
| Reserva entrevista Bach 40 € | https://buy.stripe.com/28E7sLchsgxD58varu2sM0b | ✅ live · CTA primario en landings |

Configuración aplicada (29 abril 2026):
- Tipo: Puntual (no recurrente)
- Importe: 40 € · EUR · IVA incluido en el precio
- Categoría fiscal: Formación
- Datos recopilados: Email · Nombre · Teléfono · Dirección
- Limit number of payments: NO (queremos máxima entrada al funnel; el filtro lo hace Daniel en la entrevista)

> Copia original (referencia histórica) usada para crearlos:

#### Producto 1: Reserva entrevista TDAH

| Campo | Valor |
|---|---|
| **Nombre** | `Reserva entrevista informativa - Taller TDAH adolescentes` |
| **Descripción** | `Reserva de la primera reunión informativa de hora y media (presencial Valencia o videollamada) con Daniel Orozco Abia, Psicólogo General Sanitario CV11515. La reunión es gratuita: si te presentas se devuelve íntegra. Si no te presentas, no es reembolsable. Si tras la reunión inscribes a tu hijo/a en el taller TDAH adolescentes (720 €), se cobra el taller por separado.` |
| **Imagen** | (opcional) `portadalosengranajes.webp` o foto Daniel |
| **Modelo de precio** | Estándar / pago único |
| **Importe** | `40,00 €` |
| **Moneda** | EUR |
| **Datos a recopilar** | Email ✅ · Nombre ✅ · Teléfono ✅ |
| **Tras el pago** | Mostrar página de confirmación (luego conectaremos con Cal.com) |
| **Limit number of payments** | **No establecer** (queremos tantas reservas de entrevista como se pueda; el filtro lo haces tú en la reunión) |

#### Producto 2: Reserva entrevista Bachillerato

Idéntico al anterior cambiando "TDAH adolescentes" por "Bachillerato".

### 2.2 · Productos taller (720 €) — YA EXISTEN

| Taller | Payment Link | Estado |
|---|---|---|
| TDAH 720 € | https://buy.stripe.com/28E5kD5T45SZasP8jm2sM08 | ✅ live · uso post-entrevista |
| Bachillerato 720 € | https://buy.stripe.com/3cI7sL2GS81758vgPS2sM09 | ✅ live · uso post-entrevista |

> ⚠️ **Limit number of payments = 6** sigue pendiente en estos 2 (la API no lo expone). Daniel lo configura desde el dashboard de cada Payment Link.

Stripe IDs ya creados (referencia técnica):

| Taller | Product ID | Price ID | Payment Link ID |
|---|---|---|---|
| TDAH | `prod_UQPvWiUSDThMzy` | `price_1TRZ6RFW3OLCwM3HhOLpGNaK` | `plink_1TRZ6hFW3OLCwM3H26cHJiy5` |
| Bachillerato | `prod_UQPvQMyWlvVCmm` | `price_1TRZ6UFW3OLCwM3HHbJYZKR0` | `plink_1TRZ6kFW3OLCwM3HgSGrmmfF` |

---

## 3 · Cuando Daniel cree los 2 deposits, me pasa las URLs así:

```
Deposit TDAH:    https://buy.stripe.com/xxxxxxxx
Deposit Bach:    https://buy.stripe.com/yyyyyyyy
```

Y entonces yo conecto:
- Hero CTA primario en `/talleres/tdah-adolescentes/` y `/talleres/bachillerato-motivacion/` → "Reservar entrevista · 40 €"
- Hero CTA primario en `/talleres/` (página índice) → mismos links
- Email 4 de cada automation MailerLite (`186094472462862106` TDAH y `186094552519541764` Bach) → CTA "Reservar entrevista · 40 €"
- Doc operativo de qué hacer cuando alguien paga el deposit (notificación → agendar Cal.com → marcar en MailerLite grupo "Entrevista pagada")

---

## 4 · Plantilla mensajes

### 4.1 · Tras el pago del deposit (automático Stripe envía recibo + Daniel manda este email manual)

> Hola [NOMBRE],
>
> Gracias por reservar la entrevista. Te confirmo que he recibido los 40 € de reserva.
>
> El siguiente paso es agendar la fecha. Tienes dos opciones:
>
> 1. Reservar tú mismo en mi calendario: [CAL_COM_URL]
> 2. Decirme aquí 2-3 huecos que te vengan bien y agendamos por WhatsApp/email.
>
> La reunión dura **1 hora y media**. Recuérdalo: si te presentas, te devuelvo los 40 € íntegros. Si fallas, no son reembolsables.
>
> Cualquier cosa, escríbeme aquí mismo.
>
> Un abrazo,
> Daniel

### 4.2 · Tras la reunión, si encaja (ofreciendo el taller)

> Hola [NOMBRE],
>
> Gracias por la reunión de [DÍA]. Como hemos hablado, creo que [NOMBRE_HIJO] puede encajar bien en el grupo de [TDAH / Bachillerato] que arranca en septiembre 2026.
>
> Aquí tienes el enlace para reservar la plaza:
>
> 👉 [PAYMENT_LINK_720]
>
> Son 720 € (pago único). Como te has presentado a la reunión, ya te he reembolsado los 40 € de la reserva (puedes verlo en tu cuenta o tarjeta).
>
> Una vez recibas la confirmación del taller, te llega de mi parte un email con los detalles logísticos del primer mes.
>
> Si tienes cualquier duda antes de pagar, escríbeme aquí mismo.
>
> Un abrazo,
> Daniel

### 4.3 · Tras la reunión, si no encaja (devolución y honestidad)

> Hola [NOMBRE],
>
> Gracias por confiarme la conversación. Como hablamos, creo que el formato de este taller no es lo que [NOMBRE_HIJO] necesita ahora mismo. Lo que sí creo que le ayudaría es [TERAPIA INDIVIDUAL / ORIENTACIÓN PSICOPEDAGÓGICA / OTRO RECURSO].
>
> He procesado el reembolso de los 40 € de la reserva. Te llega en 2-5 días laborales.
>
> Si más adelante quieres explorar otra vía, aquí estoy.
>
> Un abrazo,
> Daniel

---

## 5 · Operativa del reembolso (manual hasta webhook)

Cuando un padre paga el deposit y SE PRESENTA a la reunión:

1. Voy al dashboard de Stripe → Payments → busco la transacción del deposit
2. Click "Refund" → confirmar 40 € íntegros
3. Stripe envía el recibo del reembolso al padre automáticamente
4. (Opcional) marco al padre en MailerLite con tag "entrevista_realizada" para reporting

Si **no se presenta**: no toco nada. Stripe ya cobró, los 40 € se quedan, el padre puede ver en su cuenta el cargo. Recomendación: enviarle un email amable: "Te esperaba el [día] y no apareciste. Sigo aquí si quieres reagendarlo, pero los 40 € ya no son reembolsables." (no obligatorio).

---

## 6 · Webhook futuro (cuando se valide el funnel manual)

Cuando 2-3 deposits hayan pasado por todo el flujo (pagar → presentarse → reembolso → inscribir o no), monto:

- Webhook Stripe `checkout.session.completed` → Netlify Function `/.netlify/functions/stripe-webhook`
- La function distingue por Price ID:
  - Si es deposit → añade al grupo MailerLite `Entrevista reservada - TDAH/Bach` y dispara email 4.1
  - Si es taller (720 €) → añade al grupo `Inscritas - TDAH/Bach` (corta secuencia de captación + dispara bienvenida con detalles logísticos)

---

## 7 · Estado actual (29 abril 2026)

✅ Decisión estratégica tomada (deposit 40 €)
✅ Productos taller 720 € creados en Stripe (live)
✅ **Productos deposit 40 € creados en Stripe (live)**
✅ **Deposits cableados como CTA primario en `/talleres/`, `/talleres/tdah-adolescentes/` y `/talleres/bachillerato-motivacion/`**
✅ Grupos MailerLite "Inscritas" creados
✅ 2 automations TDAH/Bach creadas (draft) · email 4 actualizado con CTA deposit
⏳ Limit number of payments = 6 en los 2 Payment Links de 720 €
⏳ Activar las 2 automations en MailerLite (pegar HTML rich + condicionales + acciones + sender + switch enabled)
⏳ Actualizar bio Author Central de Amazon (quitar "Un Psicólogo Random")
⏳ Subir sitemap.xml a Search Console
⏳ Cuenta Cal.com para automatizar agendado post-deposit
