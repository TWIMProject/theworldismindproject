// Netlify Function: entrega del PDF de pago SOLO a quien tiene un token válido.
//
// Flujo: el comprador recibe por email un enlace
//   https://twimproject.com/.netlify/functions/descarga-libro?t=<token>
// El token lo firmó stripe-webhook.js tras el pago (HMAC, caducidad). Aquí se
// verifica y, si es válido, se sirve el PDF desde Netlify Blobs (almacenamiento
// PRIVADO: el PDF nunca está en una ruta pública del sitio).
//
// Env vars requeridas:
//   DOWNLOAD_TOKEN_SECRET  → mismo secreto que usa stripe-webhook.js para firmar.
// Almacenamiento:
//   Netlify Blobs store "productos", clave "engranajes-edicion-digital.pdf".
//   (Subir el PDF con scripts/subir-pdf-a-blobs.mjs · NO va al repo público.)
//
// Seguridad asumida (decisión Daniel, "solo el comprador"): se blinda el ACCESO
// (token firmado caducable + PDF fuera de rutas públicas). El reenvío del archivo
// ya descargado no se impide sin DRM (no compensa a 9,90 €); la marca de agua por
// comprador queda como mejora v2.

const { verifyDownloadToken } = require("./_lib-token");

const PRODUCT_KEY = "engranajes-digital";
const BLOB_STORE = "productos";
const BLOB_KEY = "engranajes-edicion-digital.pdf";
const DOWNLOAD_FILENAME = "Los engranajes de la mente - edicion digital.pdf";

exports.handler = async (event) => {
  if (event.httpMethod !== "GET") {
    return { statusCode: 405, body: "Method not allowed" };
  }

  const secret = process.env.DOWNLOAD_TOKEN_SECRET;
  if (!secret) {
    console.error("DOWNLOAD_TOKEN_SECRET no configurada");
    return { statusCode: 500, body: "config_missing" };
  }

  const token = event.queryStringParameters?.t || "";
  const result = verifyDownloadToken(token, secret);
  if (!result.ok) {
    console.warn("Token rechazado:", result.reason);
    // 403 genérico: no filtramos el motivo al cliente
    return { statusCode: 403, headers: { "Content-Type": "text/plain; charset=utf-8" },
      body: "Este enlace no es válido o ha caducado. Si compraste el libro, escríbeme y te mando uno nuevo." };
  }
  if (result.payload.p !== PRODUCT_KEY) {
    console.warn("Token de otro producto:", result.payload.p);
    return { statusCode: 403, body: "forbidden" };
  }

  // Leer el PDF desde Netlify Blobs (almacenamiento privado)
  let pdfBuffer;
  try {
    const { getStore } = await import("@netlify/blobs");
    const store = getStore(BLOB_STORE);
    const data = await store.get(BLOB_KEY, { type: "arrayBuffer" });
    if (!data) {
      console.error("PDF no encontrado en Blobs:", BLOB_STORE, BLOB_KEY);
      return { statusCode: 404, body: "not_found" };
    }
    pdfBuffer = Buffer.from(data);
  } catch (err) {
    console.error("Error leyendo Blobs:", err.message);
    return { statusCode: 500, body: "storage_error" };
  }

  return {
    statusCode: 200,
    headers: {
      "Content-Type": "application/pdf",
      "Content-Disposition": `attachment; filename="${DOWNLOAD_FILENAME}"`,
      "Cache-Control": "private, no-store, max-age=0",
      "X-Robots-Tag": "noindex, nofollow",
    },
    body: pdfBuffer.toString("base64"),
    isBase64Encoded: true,
  };
};
