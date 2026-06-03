// Netlify Function: Stripe webhook → MailerLite
// 1) Talleres (720 €): mueve al cliente al grupo "Inscritas" del taller pagado.
// 2) Ediciones digitales (libro 9,90 € / cuaderno 8,90 €): mete al comprador en su
//    grupo "Comprador ·", lo que dispara la automation MailerLite que le envía el
//    email con el enlace de descarga (2º canal de entrega; el 1º es el redirect de
//    Stripe a la página de descarga).
//
// Variables de entorno requeridas (Netlify → Site configuration → Environment variables):
//   STRIPE_WEBHOOK_SECRET           → del endpoint creado en https://dashboard.stripe.com/webhooks
//   STRIPE_SECRET_KEY               → REQUERIDA: para expandir line items y leer price_id
//   MAILERLITE_API_KEY              → ya configurada (la usa subscribe.js)
//   MAILERLITE_GROUP_INSCRITAS_TDAH → 186093787887437444
//   MAILERLITE_GROUP_INSCRITAS_BACH → 186093790595909010
//   (los grupos de comprador digital van fijados en código abajo: no son secretos
//    y así el email funciona sin depender de configurar env vars nuevas)
//
// Configuración del endpoint en Stripe:
//   URL:    https://twimproject.com/.netlify/functions/stripe-webhook
//   Evento: checkout.session.completed
//   API ver: 2024-06-20 o superior
//
// Mapping price_id → grupo MailerLite. Cada entrada usa { env } (lee el id de una env
// var) o { groupId } (id fijo en código). label es solo para logs.
const PRICE_TO_GROUP = {
  // Talleres 720 € (sin cambios)
  "price_1TRZ6RFW3OLCwM3HhOLpGNaK": { env: "MAILERLITE_GROUP_INSCRITAS_TDAH", label: "TDAH" },
  "price_1TRZ6UFW3OLCwM3HHbJYZKR0": { env: "MAILERLITE_GROUP_INSCRITAS_BACH", label: "Bachillerato" },
  // Ediciones digitales (entrega por email vía automation al entrar en el grupo)
  "price_1Te9ezFW3OLCwM3Hk5dRzXQd": { groupId: "189245231853471319", label: "Libro digital" },
  "price_1Te9giFW3OLCwM3HTwtYsBEu": { groupId: "189245232345252997", label: "Cuaderno mirada" },
};

// Los deposits (40 €) NO se mueven a Inscritas: el padre solo agendó entrevista.
// Sólo cuando paga el taller 720 € entra a Inscritas (lo que corta la secuencia de captación).

const crypto = require("crypto");

const STRIPE_SIGNATURE_TOLERANCE_SECONDS = 300; // 5 minutes

function verifyStripeSignature(rawBody, signatureHeader, secret) {
  if (!signatureHeader || !secret) return false;

  let timestamp = null;
  const signatures = [];

  for (const entry of signatureHeader.split(",")) {
    const eq = entry.indexOf("=");
    if (eq === -1) continue;
    const key = entry.slice(0, eq).trim();
    const value = entry.slice(eq + 1).trim();
    if (key === "t" && timestamp === null) timestamp = value;
    else if (key === "v1") signatures.push(value);
  }

  if (!timestamp || signatures.length === 0) return false;

  const tsSeconds = Number.parseInt(timestamp, 10);
  if (!Number.isFinite(tsSeconds)) return false;

  const nowSeconds = Math.floor(Date.now() / 1000);
  if (Math.abs(nowSeconds - tsSeconds) > STRIPE_SIGNATURE_TOLERANCE_SECONDS) {
    return false; // replay protection
  }

  const signedPayload = `${timestamp}.${rawBody}`;
  const expected = crypto.createHmac("sha256", secret).update(signedPayload, "utf8").digest("hex");
  const expectedBuf = Buffer.from(expected, "hex");

  for (const sig of signatures) {
    const sigBuf = Buffer.from(sig, "hex");
    if (sigBuf.length !== expectedBuf.length) continue;
    if (crypto.timingSafeEqual(sigBuf, expectedBuf)) return true;
  }
  return false;
}

// Returns { ok: true, items } | { ok: false, retriable: bool, reason }
async function fetchSessionLineItems(sessionId, apiKey) {
  try {
    const res = await fetch(
      `https://api.stripe.com/v1/checkout/sessions/${sessionId}/line_items`,
      { headers: { Authorization: `Bearer ${apiKey}` } }
    );
    if (!res.ok) {
      // 5xx and 429 are retriable — Stripe will redeliver
      const retriable = res.status >= 500 || res.status === 429;
      return { ok: false, retriable, reason: `stripe_api_${res.status}` };
    }
    const data = await res.json();
    return { ok: true, items: data.data || [] };
  } catch (err) {
    return { ok: false, retriable: true, reason: `network: ${err.message}` };
  }
}

// Returns { ok: true } | { ok: false, retriable: bool, status, message }
async function addToMailerLiteGroupSafe({ email, name, phone, groupId, apiKey }) {
  const payload = {
    email,
    fields: { name: name || "", last_name: "", phone: phone || "" },
    groups: [groupId],
    status: "active",
  };
  let res;
  try {
    res = await fetch("https://connect.mailerlite.com/api/subscribers", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
        Authorization: `Bearer ${apiKey}`,
      },
      body: JSON.stringify(payload),
    });
  } catch (err) {
    return { ok: false, retriable: true, status: 0, message: `network: ${err.message}` };
  }
  if (res.ok) return { ok: true };
  const text = await res.text().catch(() => "");
  // 5xx and 429 → retriable; let Stripe redeliver. 4xx (validation/conflict) → not retriable.
  const retriable = res.status >= 500 || res.status === 429;
  return { ok: false, retriable, status: res.status, message: text };
}

function jsonResponse(statusCode, payload) {
  return {
    statusCode,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  };
}

exports.handler = async (event) => {
  // Solo POST con body
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, body: "Method not allowed" };
  }

  // Validar TODAS las env vars críticas antes de hacer nada
  const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;
  const stripeSecretKey = process.env.STRIPE_SECRET_KEY;
  const mailerLiteKey = process.env.MAILERLITE_API_KEY;
  const missing = [];
  if (!webhookSecret) missing.push("STRIPE_WEBHOOK_SECRET");
  if (!stripeSecretKey) missing.push("STRIPE_SECRET_KEY");
  if (!mailerLiteKey) missing.push("MAILERLITE_API_KEY");
  if (missing.length) {
    console.error("Env vars missing:", missing);
    return jsonResponse(500, { error: "config_missing", missing_env_vars: missing });
  }

  // Soporte body base64-encoded (Netlify Functions a veces lo envía así)
  const rawBody = event.isBase64Encoded
    ? Buffer.from(event.body || "", "base64").toString("utf8")
    : event.body || "";

  // Verificar firma Stripe (replay-safe con tolerancia de timestamp)
  const signature = event.headers?.["stripe-signature"] || event.headers?.["Stripe-Signature"];
  if (!verifyStripeSignature(rawBody, signature, webhookSecret)) {
    console.error("Firma Stripe inválida o fuera de tolerancia");
    return jsonResponse(400, { error: "invalid_signature" });
  }

  let stripeEvent;
  try {
    stripeEvent = JSON.parse(rawBody);
  } catch {
    return jsonResponse(400, { error: "bad_json" });
  }

  // Sólo nos interesa checkout.session.completed
  if (stripeEvent.type !== "checkout.session.completed") {
    return jsonResponse(200, { received: true, ignored: stripeEvent.type });
  }

  const session = stripeEvent.data?.object || {};
  const customerEmail = session.customer_details?.email || session.customer_email;
  const customerName = session.customer_details?.name || "";
  const customerPhone = session.customer_details?.phone || "";
  const sessionId = session.id;

  if (!customerEmail) {
    console.error("Sin customer email en session", sessionId);
    return jsonResponse(200, { received: true, error: "no_email" });
  }

  // Resolver line items para identificar qué producto se compró
  const lineItemsResult = await fetchSessionLineItems(sessionId, stripeSecretKey);
  if (!lineItemsResult.ok) {
    console.error("No pude obtener line items", { sessionId, reason: lineItemsResult.reason });
    if (lineItemsResult.retriable) {
      // 500 → Stripe reintentará (no perdemos el evento)
      return jsonResponse(500, { error: "line_items_unavailable", reason: lineItemsResult.reason });
    }
    // 4xx (auth, etc) → no tiene sentido reintentar. Loggeamos y dejamos pasar.
    return jsonResponse(200, { received: true, ignored: "line_items_unavailable", reason: lineItemsResult.reason });
  }

  let mapping = null;
  for (const item of lineItemsResult.items) {
    const priceId = item.price?.id;
    if (priceId && PRICE_TO_GROUP[priceId]) {
      mapping = PRICE_TO_GROUP[priceId];
      break;
    }
  }

  if (!mapping) {
    // Producto no mapeado (deposit 40 € u otro producto). Ignored.
    console.log("Session ignored (no price match)", { sessionId, amount: session.amount_total });
    return jsonResponse(200, { received: true, ignored: "no_price_match" });
  }

  const mappedLabel = mapping.label;
  // groupId fijo en código (digital) o leído de env var (talleres)
  const groupId = mapping.groupId || process.env[mapping.env];
  if (!groupId) {
    console.error(`Grupo no resuelto para ${mappedLabel} (env ${mapping.env})`);
    return jsonResponse(500, { error: "group_unresolved", label: mappedLabel });
  }

  const mlResult = await addToMailerLiteGroupSafe({
    email: customerEmail,
    name: customerName,
    phone: customerPhone,
    groupId,
    apiKey: mailerLiteKey,
  });

  if (mlResult.ok) {
    console.log(`Added ${customerEmail} to group [${mappedLabel}]`);
    return jsonResponse(200, { received: true, moved_to: mappedLabel, email: customerEmail });
  }

  console.error("MailerLite error", { status: mlResult.status, message: mlResult.message, retriable: mlResult.retriable });
  if (mlResult.retriable) {
    // 500 → Stripe reintenta. Evita perder el alta por un timeout/rate-limit transitorio.
    return jsonResponse(500, { error: "mailerlite_retriable", status: mlResult.status });
  }
  // No retriable (validación, conflicto): 200 para no entrar en retry storms.
  // El evento queda registrado en logs para reproceso manual si hace falta.
  return jsonResponse(200, { received: true, mailerlite_error: mlResult.status, message: mlResult.message });
};
