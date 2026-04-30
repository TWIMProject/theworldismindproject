// Netlify Function: Añadir suscriptor a MailerLite
// Variables de entorno requeridas (Netlify → Site configuration → Environment variables):
//   MAILERLITE_API_KEY              → token Bearer del MailerLite nuevo (connect.mailerlite.com)
//   MAILERLITE_GROUP_RETO           → ID del grupo "Reto 7 Días - Inscritas"
//   MAILERLITE_GROUP_LEAD_MAGNET    → ID del grupo "Lead Magnet - Dependencia Emocional"
//   MAILERLITE_GROUP_GENERAL        → ID del grupo "Lista General TWIM"
//   MAILERLITE_GROUP_PADRES_TDAH    → ID del grupo "Padres TDAH ESO"
//   MAILERLITE_GROUP_PADRES_BACH    → ID del grupo "Padres Bachillerato"
//   MAILERLITE_GROUP_PADRES_TALLERES→ ID del grupo "Padres Talleres Adolescentes"
//   MAILERLITE_GROUP_NEWSLETTER_HOME→ ID del grupo "Web - Newsletter Home"
//   MAILERLITE_GROUP_INSCRITAS_TDAH → ID del grupo "Taller TDAH - Inscritas" (186093787887437444)
//   MAILERLITE_GROUP_INSCRITAS_BACH → ID del grupo "Taller Bachillerato - Inscritas" (186093790595909010)
//
// Diagnóstico: GET /.netlify/functions/subscribe?diag=1 devuelve qué env vars están
// configuradas (sin exponer valores) y la versión de Node del runtime.

const ALLOWED_ORIGINS = new Set([
  "https://twimproject.com",
  "https://www.twimproject.com",
  "http://localhost:8888",
  "http://localhost:3000",
]);

const groupEnvMap = {
  "lead-magnet-dependencia": "MAILERLITE_GROUP_LEAD_MAGNET",
  "reto-7-dias": "MAILERLITE_GROUP_RETO",
  "lista-general": "MAILERLITE_GROUP_GENERAL",
  "padres-talleres-tdah": "MAILERLITE_GROUP_PADRES_TDAH",
  "padres-talleres-bachillerato": "MAILERLITE_GROUP_PADRES_BACH",
  "padres-talleres-adolescentes": "MAILERLITE_GROUP_PADRES_TALLERES",
  "newsletter-home": "MAILERLITE_GROUP_NEWSLETTER_HOME",
  "inscritas-tdah": "MAILERLITE_GROUP_INSCRITAS_TDAH",
  "inscritas-bachillerato": "MAILERLITE_GROUP_INSCRITAS_BACH",
};

function buildHeaders(event) {
  const origin = event.headers?.origin || event.headers?.Origin || "";
  const allowOrigin = ALLOWED_ORIGINS.has(origin) ? origin : "https://twimproject.com";
  return {
    "Access-Control-Allow-Origin": allowOrigin,
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
    "Vary": "Origin",
    "Content-Type": "application/json",
  };
}

function json(statusCode, headers, payload) {
  return { statusCode, headers, body: JSON.stringify(payload) };
}

exports.handler = async (event) => {
  const headers = buildHeaders(event);

  try {
    if (event.httpMethod === "OPTIONS") {
      return { statusCode: 204, headers, body: "" };
    }

    // Diagnóstico: GET con ?diag=1 devuelve estado de configuración sin exponer secretos.
    if (event.httpMethod === "GET") {
      const diag = event.queryStringParameters?.diag === "1";
      if (!diag) {
        return json(405, headers, { error: "Method not allowed" });
      }
      const envStatus = {};
      envStatus.MAILERLITE_API_KEY = Boolean(process.env.MAILERLITE_API_KEY);
      for (const envKey of new Set(Object.values(groupEnvMap))) {
        envStatus[envKey] = Boolean(process.env[envKey]);
      }
      return json(200, headers, {
        ok: true,
        node: process.version,
        fetchAvailable: typeof fetch === "function",
        env: envStatus,
      });
    }

    if (event.httpMethod !== "POST") {
      return json(405, headers, { error: "Method not allowed" });
    }

    if (typeof fetch !== "function") {
      console.error("Runtime sin fetch nativo. Node:", process.version);
      return json(500, headers, {
        error: "Runtime incompatible (fetch no disponible). Actualizar Node a 18+ en Netlify.",
      });
    }

    const API_KEY = process.env.MAILERLITE_API_KEY;
    if (!API_KEY) {
      return json(500, headers, { error: "MAILERLITE_API_KEY no configurada en Netlify" });
    }

    let data;
    try {
      data = JSON.parse(event.body || "{}");
    } catch {
      return json(400, headers, { error: "JSON inválido" });
    }

    const { email, name, whatsapp, group } = data;

    if (!email || typeof email !== "string" || !email.includes("@")) {
      return json(400, headers, { error: "Email inválido o ausente" });
    }

    const groupEnvKey = groupEnvMap[group] || "MAILERLITE_GROUP_LEAD_MAGNET";
    const groupId = process.env[groupEnvKey];

    if (!groupId) {
      console.error(`Env var ${groupEnvKey} no configurada (grupo solicitado: ${group})`);
      return json(500, headers, {
        error: `Grupo MailerLite no configurado (${groupEnvKey} ausente en Netlify)`,
      });
    }

    const mlPayload = {
      email,
      fields: {
        name: name || "",
        last_name: "",
        phone: whatsapp || "",
      },
      groups: [groupId],
      status: "active",
    };

    let subscriberResponse;
    try {
      subscriberResponse = await fetch("https://connect.mailerlite.com/api/subscribers", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json",
          "Authorization": `Bearer ${API_KEY}`,
        },
        body: JSON.stringify(mlPayload),
      });
    } catch (networkErr) {
      console.error("Fallo de red contra MailerLite:", networkErr);
      return json(502, headers, {
        error: "No se pudo contactar con MailerLite",
        detail: String(networkErr?.message || networkErr),
      });
    }

    const rawBody = await subscriberResponse.text();
    let result;
    try {
      result = rawBody ? JSON.parse(rawBody) : {};
    } catch {
      result = { raw: rawBody };
    }

    if (!subscriberResponse.ok) {
      console.error("MailerLite respondió error:", subscriberResponse.status, rawBody);
      return json(subscriberResponse.status, headers, {
        error: result.message || `MailerLite devolvió ${subscriberResponse.status}`,
        mailerliteStatus: subscriberResponse.status,
        mailerliteBody: result,
      });
    }

    return json(200, headers, { success: true, message: "Suscriptor añadido" });
  } catch (error) {
    console.error("Subscribe function crash:", error);
    return json(500, headers, {
      error: "Internal server error",
      detail: String(error?.message || error),
    });
  }
};
