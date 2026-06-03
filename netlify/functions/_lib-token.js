// Token de descarga firmado (HMAC-SHA256) para entrega de productos digitales.
// Compartido por stripe-webhook.js (firma al comprar) y descarga-libro.js (verifica).
//
// Formato del token: base64url(payloadJSON) + "." + base64url(hmac)
// payload = { e: email, p: productKey, exp: epochSeconds }
//
// Requiere env var DOWNLOAD_TOKEN_SECRET (string aleatorio largo, NO commitear).
// El token NO es secreto en sí: va al email del comprador. Su seguridad está en
// la firma HMAC (no se puede falsificar sin el secret) y en la caducidad (exp).

const crypto = require("crypto");

function b64url(buf) {
  return Buffer.from(buf).toString("base64").replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}
function b64urlDecode(str) {
  str = str.replace(/-/g, "+").replace(/_/g, "/");
  while (str.length % 4) str += "=";
  return Buffer.from(str, "base64");
}

function signDownloadToken({ email, productKey, ttlSeconds, secret }) {
  const payload = { e: email, p: productKey, exp: Math.floor(Date.now() / 1000) + ttlSeconds };
  const body = b64url(JSON.stringify(payload));
  const mac = crypto.createHmac("sha256", secret).update(body).digest();
  return `${body}.${b64url(mac)}`;
}

// Devuelve { ok:true, payload } | { ok:false, reason }
function verifyDownloadToken(token, secret) {
  if (!token || typeof token !== "string") {
    return { ok: false, reason: "malformed" };
  }
  const parts = token.split(".");
  if (parts.length !== 2 || !parts[0] || !parts[1]) {
    return { ok: false, reason: "malformed" }; // exactamente 2 segmentos no vacíos
  }
  const [body, sig] = parts;
  const expected = crypto.createHmac("sha256", secret).update(body).digest();
  const given = b64urlDecode(sig || "");
  if (given.length !== expected.length || !crypto.timingSafeEqual(given, expected)) {
    return { ok: false, reason: "bad_signature" };
  }
  let payload;
  try {
    payload = JSON.parse(b64urlDecode(body).toString("utf8"));
  } catch {
    return { ok: false, reason: "bad_payload" };
  }
  if (!payload.exp || Math.floor(Date.now() / 1000) > payload.exp) {
    return { ok: false, reason: "expired" };
  }
  return { ok: true, payload };
}

module.exports = { signDownloadToken, verifyDownloadToken };
