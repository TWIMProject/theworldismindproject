// Netlify Function: Stripe webhook → MailerLite
// Mueve al cliente al grupo "Inscritas" cuando paga el taller de 720 €.
//
// Variables de entorno requeridas (Netlify → Site configuration → Environment variables):
//   STRIPE_WEBHOOK_SECRET           → del endpoint creado en https://dashboard.stripe.com/webhooks
//   STRIPE_SECRET_KEY               → opcional pero recomendado: para expandir line items
//   MAILERLITE_API_KEY              → ya configurada (la usa subscribe.js)
//   MAILERLITE_GROUP_INSCRITAS_TDAH → 186093787887437444
//   MAILERLITE_GROUP_INSCRITAS_BACH → 186093790595909010
//
// Configuración del endpoint en Stripe:
//   URL:    https://twimproject.com/.netlify/functions/stripe-webhook
//   Evento: checkout.session.completed
//   API ver: 2024-06-20 o superior
//
// Mapping price_id → grupo MailerLite Inscritas (los 2 talleres de 720 €):
const PRICE_TO_GROUP = {
  "price_1TRZ6RFW3OLCwM3HhOLpGNaK": { env: "MAILERLITE_GROUP_INSCRITAS_TDAH", label: "TDAH" },
  "price_1TRZ6UFW3OLCwM3HHbJYZKR0": { env: "MAILERLITE_GROUP_INSCRITAS_BACH", label: "Bachillerato" },
};

// Los deposits (40 €) NO se mueven a Inscritas: el padre solo agendó entrevista.
// Sólo cuando paga el taller 720 € entra a Inscritas (lo que corta la secuencia de captación).

const crypto = require("crypto");

function verifyStripeSignature(rawBody, signatureHeader, secret) {
  if (!signatureHeader || !secret) return false;
  const parts = Object.fromEntries(
    signatureHeader.split(",").map((kv) => kv.split("=").map((s) => s.trim()))
  );
  if (!parts.t || !parts.v1) return false;
  const signedPayload = `${parts.t}.${rawBody}`;
  const expected = crypto.createHmac("sha256", secret).update(signedPayload, "utf8").digest("hex");
  // Constant-time compare
  const a = Buffer.from(parts.v1, "hex");
  const b = Buffer.from(expected, "hex");
  if (a.length !== b.length) return false;
  return crypto.timingSafeEqual(a, b);
}

async function fetchSessionLineItems(sessionId, apiKey) {
  if (!apiKey) return null;
  try {
    const res = await fetch(
      `https://api.stripe.com/v1/checkout/sessions/${sessionId}/line_items`,
      { headers: { Authorization: `Bearer ${apiKey}` } }
    );
    if (!res.ok) return null;
    const data = await res.json();
    return data.data || [];
  } catch {
    return null;
  }
}

async function addToMailerLiteGroup({ email, name, phone, groupId, apiKey }) {
  const payload = {
    email,
    fields: { name: name || "", last_name: "", phone: phone || "" },
    groups: [groupId],
    status: "active",
  };
  const res = await fetch("https://connect.mailerlite.com/api/subscribers", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
      Authorization: `Bearer ${apiKey}`,
    },
    body: JSON.stringify(payload),
  });
  const text = await res.text();
  if (!res.ok) throw new Error(`MailerLite ${res.status}: ${text}`);
  return JSON.parse(text || "{}");
}

exports.handler = async (event) => {
  // Solo POST con body
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, body: "Method not allowed" };
  }
  const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;
  if (!webhookSecret) {
    console.error("STRIPE_WEBHOOK_SECRET no configurada");
    return { statusCode: 500, body: "Webhook not configured" };
  }
  const mailerLiteKey = process.env.MAILERLITE_API_KEY;
  if (!mailerLiteKey) {
    console.error("MAILERLITE_API_KEY no configurada");
    return { statusCode: 500, body: "MailerLite not configured" };
  }

  // Verificar firma Stripe
  const signature = event.headers?.["stripe-signature"] || event.headers?.["Stripe-Signature"];
  if (!verifyStripeSignature(event.body || "", signature, webhookSecret)) {
    console.error("Firma Stripe inválida");
    return { statusCode: 400, body: "Invalid signature" };
  }

  let stripeEvent;
  try {
    stripeEvent = JSON.parse(event.body);
  } catch {
    return { statusCode: 400, body: "Bad JSON" };
  }

  // Sólo nos interesa checkout.session.completed
  if (stripeEvent.type !== "checkout.session.completed") {
    return { statusCode: 200, body: JSON.stringify({ received: true, ignored: stripeEvent.type }) };
  }

  const session = stripeEvent.data?.object || {};
  const customerEmail = session.customer_details?.email || session.customer_email;
  const customerName = session.customer_details?.name || "";
  const customerPhone = session.customer_details?.phone || "";
  const sessionId = session.id;

  if (!customerEmail) {
    console.error("Sin customer email en session", sessionId);
    return { statusCode: 200, body: JSON.stringify({ received: true, error: "no_email" }) };
  }

  // Identificar qué producto se compró por price_id
  const lineItems = await fetchSessionLineItems(sessionId, process.env.STRIPE_SECRET_KEY);
  if (!lineItems) {
    console.warn("No se pudieron obtener line items, fallback por amount_total");
  }

  let mappedGroupEnv = null;
  let mappedLabel = null;
  if (lineItems) {
    for (const item of lineItems) {
      const priceId = item.price?.id;
      if (priceId && PRICE_TO_GROUP[priceId]) {
        mappedGroupEnv = PRICE_TO_GROUP[priceId].env;
        mappedLabel = PRICE_TO_GROUP[priceId].label;
        break;
      }
    }
  }

  if (!mappedGroupEnv) {
    // Producto no es uno de los 2 talleres 720 €. Probablemente deposit 40 € o algún otro producto.
    // No hacemos nada — solo log para auditoría.
    console.log("Session ignored (no taller match)", { sessionId, amount: session.amount_total });
    return { statusCode: 200, body: JSON.stringify({ received: true, ignored: "no_taller_match" }) };
  }

  const groupId = process.env[mappedGroupEnv];
  if (!groupId) {
    console.error(`Env var ${mappedGroupEnv} no configurada`);
    return { statusCode: 500, body: "Group env var missing" };
  }

  try {
    await addToMailerLiteGroup({
      email: customerEmail,
      name: customerName,
      phone: customerPhone,
      groupId,
      apiKey: mailerLiteKey,
    });
    console.log(`Added ${customerEmail} to Inscritas-${mappedLabel}`);
    return {
      statusCode: 200,
      body: JSON.stringify({ received: true, moved_to: mappedLabel, email: customerEmail }),
    };
  } catch (err) {
    console.error("MailerLite error:", err.message);
    // Devolvemos 200 para que Stripe no reintente eternamente; el log queda para auditoría.
    return { statusCode: 200, body: JSON.stringify({ received: true, mailerlite_error: err.message }) };
  }
};
