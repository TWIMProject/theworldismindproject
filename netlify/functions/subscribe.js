// Netlify Function: Añadir suscriptor a MailerLite
// Variable de entorno requerida: MAILERLITE_API_KEY (configurar en Netlify Dashboard)

exports.handler = async (event) => {
  const headers = {
    "Access-Control-Allow-Origin": "https://twimproject.com",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Content-Type": "application/json",
  };

  if (event.httpMethod === "OPTIONS") {
    return { statusCode: 204, headers, body: "" };
  }

  if (event.httpMethod !== "POST") {
    return { statusCode: 405, headers, body: JSON.stringify({ error: "Method not allowed" }) };
  }

  const API_KEY = process.env.MAILERLITE_API_KEY;
  if (!API_KEY) {
    return { statusCode: 500, headers, body: JSON.stringify({ error: "API key not configured" }) };
  }

  let data;
  try {
    data = JSON.parse(event.body);
  } catch {
    return { statusCode: 400, headers, body: JSON.stringify({ error: "Invalid JSON" }) };
  }

  const { email, name, whatsapp, group } = data;

  if (!email) {
    return { statusCode: 400, headers, body: JSON.stringify({ error: "Email is required" }) };
  }

  // Determinar el grupo de MailerLite
  // Los IDs de grupo se configuran como variables de entorno en Netlify
  const groupEnvMap = {
    "lead-magnet-dependencia": "MAILERLITE_GROUP_LEAD_MAGNET",
    "reto-7-dias": "MAILERLITE_GROUP_RETO",
    "lista-general": "MAILERLITE_GROUP_GENERAL",
  };

  const groupEnvKey = groupEnvMap[group] || "MAILERLITE_GROUP_LEAD_MAGNET";
  const groupId = process.env[groupEnvKey];

  try {
    // 1. Crear/actualizar suscriptor en MailerLite
    const subscriberResponse = await fetch("https://connect.mailerlite.com/api/subscribers", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": `Bearer ${API_KEY}`,
      },
      body: JSON.stringify({
        email,
        fields: {
          name: name || "",
          last_name: "",
          phone: whatsapp || "",
        },
        groups: groupId ? [groupId] : [],
        status: "active",
      }),
    });

    const result = await subscriberResponse.json();

    if (!subscriberResponse.ok) {
      console.error("MailerLite error:", JSON.stringify(result));
      return {
        statusCode: subscriberResponse.status,
        headers,
        body: JSON.stringify({
          error: result.message || "Error adding subscriber",
        }),
      };
    }

    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({ success: true, message: "Subscriber added successfully" }),
    };
  } catch (error) {
    console.error("Subscribe function error:", error);
    return {
      statusCode: 500,
      headers,
      body: JSON.stringify({ error: "Internal server error" }),
    };
  }
};
