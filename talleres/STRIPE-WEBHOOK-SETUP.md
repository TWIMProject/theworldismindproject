# Stripe Webhook · Setup

> **Para qué sirve:** cuando un padre pague el taller (720 €), automáticamente se añade al grupo `Inscritas` correspondiente en MailerLite. Eso corta la secuencia de captación de 4 emails y deja al cliente listo para recibir comunicación post-inscripción. Sin esto, lo haces a mano cada vez.

> **Tiempo de activación:** ~10 min cuando hayas validado el funnel manual con 1-2 ventas reales.

---

## 1 · Estado del código

✅ Archivo creado: `netlify/functions/stripe-webhook.js`
✅ Sin dependencias npm (usa `crypto` y `fetch` built-in de Node 18+)
✅ Verifica firma Stripe (HMAC-SHA256, comparación timing-safe)
✅ Solo procesa `checkout.session.completed`
✅ Mapeo hardcoded:
  - `price_1TRZ6RFW3OLCwM3HhOLpGNaK` (TDAH 720 €) → grupo `Inscritas TDAH` (`186093787887437444`)
  - `price_1TRZ6UFW3OLCwM3HHbJYZKR0` (Bach 720 €) → grupo `Inscritas Bach` (`186093790595909010`)
  - Deposits 40 € y otros productos → ignored (log only)

---

## 2 · Pasos para activarlo (~10 min)

### 2.1 · Añadir env vars en Netlify (3 min)

Site configuration → Environment variables → **Add variable**:

| Variable | Valor | De dónde |
|---|---|---|
| `STRIPE_WEBHOOK_SECRET` | `whsec_...` | Lo da Stripe al crear el endpoint (paso 2.2) |
| `STRIPE_SECRET_KEY` | `sk_live_...` | https://dashboard.stripe.com/apikeys → "Secret key" |
| `MAILERLITE_GROUP_INSCRITAS_TDAH` | `186093787887437444` | Ya documentado |
| `MAILERLITE_GROUP_INSCRITAS_BACH` | `186093790595909010` | Ya documentado |

`MAILERLITE_API_KEY` ya existe (la usa `subscribe.js`).

### 2.2 · Crear el endpoint en Stripe (5 min)

1. https://dashboard.stripe.com/webhooks → **Add endpoint**
2. **Endpoint URL**: `https://twimproject.com/.netlify/functions/stripe-webhook`
3. **Description**: `MailerLite sync taller inscripciones`
4. **API version**: 2024-06-20 o superior (deja la default)
5. **Events to send**: solo selecciona `checkout.session.completed`
6. → **Add endpoint**
7. En la página del endpoint recién creado → **Signing secret** → click "Reveal" → **copia el valor `whsec_...`** y pégalo en el env var `STRIPE_WEBHOOK_SECRET` de Netlify

### 2.3 · Re-deploy en Netlify (2 min)

Las env vars no se aplican hasta el próximo deploy. Trigger un deploy manual:
- Netlify dashboard → Deploys → **Trigger deploy** → "Deploy site"

O hacer un commit cualquiera al main (incluso vacío con `--allow-empty`).

---

## 3 · Test antes de poner en producción

### 3.1 · Test desde Stripe Dashboard

1. https://dashboard.stripe.com/webhooks → tu endpoint → **Send test webhook**
2. Selecciona evento `checkout.session.completed`
3. Click **Send test webhook**
4. Stripe te muestra la respuesta:
   - `200` con `{"received":true,"ignored":"no_taller_match"}` = correcto (el evento de prueba no tiene los price IDs reales)
   - `400` con "Invalid signature" = `STRIPE_WEBHOOK_SECRET` mal configurada
   - `500` con error = ver logs Netlify

### 3.2 · Test real con tarjeta

1. Crea un código de descuento del 100 % en Stripe (te queda gratis para ti la prueba) y aplícalo a uno de los 2 Payment Links de 720 €
2. Compra desde una cuenta nueva con tu propio email de prueba
3. Verifica:
   - Stripe: pago `succeeded`
   - Netlify Functions logs: 1 entrada con `Added <email> to Inscritas-TDAH` (o Bach)
   - MailerLite Suscriptores: ese email aparece en el grupo `Inscritas` correspondiente
   - Si la automation de captación está activa: el email se sale de la secuencia automáticamente (porque el bloque condicional detecta el grupo Inscritas → exit)

---

## 4 · Logs y debugging

### 4.1 · Ver logs en Netlify

Netlify dashboard → Site → Logs → Functions → busca `stripe-webhook`. Verás cada invocación con su entrada/salida.

### 4.2 · Ver logs en Stripe

Dashboard Stripe → Webhooks → tu endpoint → tab "Events". Cada evento muestra el código de respuesta y el body recibido.

### 4.3 · Errores comunes

| Error | Causa probable | Solución |
|---|---|---|
| `400 Invalid signature` | `STRIPE_WEBHOOK_SECRET` mal configurada o usaste el de modo test en producción | Re-copia el secret desde Stripe Dashboard |
| `500 Webhook not configured` | Falta env var `STRIPE_WEBHOOK_SECRET` | Añadir en Netlify y re-deploy |
| `200 ignored: no_taller_match` | Compraste algo que NO es uno de los 2 talleres 720 € (deposit, otro producto). **Esperado.** | Ninguna, es la respuesta correcta |
| `200 mailerlite_error: ...` | El email ya estaba en MailerLite con conflicto, o API key caducada | Ver mensaje exacto en log |

---

## 5 · Qué pasa cuando alguien paga 720 €

```
Padre paga 720 € en Stripe Payment Link (el que tú le pasaste post-reunión)
→ Stripe genera evento checkout.session.completed
→ Stripe POST a https://twimproject.com/.netlify/functions/stripe-webhook
→ Netlify Function:
   1. Verifica firma con STRIPE_WEBHOOK_SECRET ✓
   2. Lee el price_id de la línea de pago (TDAH 720 € o Bach 720 €)
   3. Identifica grupo MailerLite Inscritas correspondiente
   4. POST a connect.mailerlite.com/api/subscribers añadiendo al cliente al grupo Inscritas
   5. MailerLite detecta que el cliente ahora está en "Inscritas" 
      → la automation de captación tiene un bloque condicional 
      → exit del flujo
   6. Función devuelve 200 OK a Stripe
```

**Tu único trabajo manual restante:** mandarle email/WhatsApp de bienvenida con detalles logísticos del taller (eso no se automatiza porque varía por grupo y momento).

---

## 6 · Pendiente para cuando lo actives

- [ ] Añadir las 4 env vars en Netlify (§2.1)
- [ ] Crear el endpoint en Stripe Dashboard (§2.2)
- [ ] Pegar `whsec_...` como `STRIPE_WEBHOOK_SECRET` en Netlify
- [ ] Trigger re-deploy
- [ ] Test desde Stripe Dashboard "Send test webhook"
- [ ] (Opcional) Test real con código 100 % off
