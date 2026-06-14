// Netlify Function · ONE-OFF de mantenimiento (borrar tras usar)
// Rellena el campo `dlqd_codigo` en TODOS los suscriptores que aún no lo tengan,
// para poder enviarles por email su código personal de la app DLQD.
//
// El código es determinista (mismo HMAC que subscribe.js / traductor-interno.js),
// así que el proceso es idempotente: se puede repetir sin efectos raros.
//
// Uso (desde el navegador, una vez):
//   1. DRY-RUN (no escribe nada, solo cuenta):
//      /.netlify/functions/dlqd-backfill?token=XXXX
//   2. APLICAR (escribe los códigos que falten):
//      /.netlify/functions/dlqd-backfill?token=XXXX&apply=1
//
// Variables de entorno:
//   DLQD_ADMIN_TOKEN   → token de autorización (temporal, crear y borrar tras usar)
//   DLQD_CODE_SECRET   → secreto del HMAC del código (ya existe)
//   MAILERLITE_API_KEY → token de MailerLite (ya existe)
//
// No devuelve datos personales: solo un resumen de conteos.

const crypto = require("node:crypto");

function codigoParaEmail(email) {
  const secreto = process.env.DLQD_CODE_SECRET;
  if (!secreto) return null;
  return crypto
    .createHmac("sha256", secreto)
    .update(email.trim().toLowerCase())
    .digest("hex")
    .slice(0, 8)
    .toUpperCase();
}

function tokenOk(dado) {
  const esperado = process.env.DLQD_ADMIN_TOKEN || "";
  if (!esperado || !dado) return false;
  const a = Buffer.from(String(dado));
  const b = Buffer.from(esperado);
  if (a.length !== b.length) return false;
  return crypto.timingSafeEqual(a, b);
}

function json(statusCode, payload) {
  return {
    statusCode,
    headers: { "Content-Type": "application/json", "Cache-Control": "no-store" },
    body: JSON.stringify(payload),
  };
}

exports.handler = async (event) => {
  const q = event.queryStringParameters || {};
  if (!tokenOk(q.token)) {
    return json(401, { ok: false, error: "no autorizado" });
  }

  const API = process.env.MAILERLITE_API_KEY;
  if (!API) {
    return json(500, { ok: false, error: "falta MAILERLITE_API_KEY" });
  }
  if (!process.env.DLQD_CODE_SECRET) {
    return json(500, { ok: false, error: "falta DLQD_CODE_SECRET" });
  }

  const apply = q.apply === "1";

  let total = 0;
  let yaTenian = 0;
  let escritos = 0;
  let errores = 0;
  let omitidosInactivos = 0;
  const erroresMuestra = [];
  let cursor = null;

  function enmascara(email) {
    const s = String(email || "");
    const i = s.indexOf("@");
    if (i <= 1) return "***";
    return s[0] + "***" + s.slice(i);
  }

  try {
    do {
      const url = new URL("https://connect.mailerlite.com/api/subscribers");
      url.searchParams.set("limit", "100");
      if (cursor) url.searchParams.set("cursor", cursor);

      const r = await fetch(url, {
        headers: { Authorization: "Bearer " + API, Accept: "application/json" },
      });
      if (!r.ok) {
        return json(502, { ok: false, error: "MailerLite listó error", status: r.status });
      }
      const data = await r.json();
      const subs = Array.isArray(data.data) ? data.data : [];

      const pendientes = [];
      for (const s of subs) {
        total++;
        if (s.fields && s.fields.dlqd_codigo) {
          yaTenian++;
          continue;
        }
        // No tocar suscriptores que no están activos (baja/rebote/no confirmado):
        // ni se les puede enviar la campaña ni MailerLite deja actualizarlos limpio.
        if (s.status && s.status !== "active") {
          omitidosInactivos++;
          continue;
        }
        pendientes.push(s);
      }

      // Lotes paralelos para no agotar el tiempo de la función ni el rate limit.
      const LOTE = 5;
      for (let i = 0; i < pendientes.length; i += LOTE) {
        const trozo = pendientes.slice(i, i + LOTE);
        const resultados = await Promise.allSettled(
          trozo.map(async (s) => {
            const cod = codigoParaEmail(s.email);
            if (!cod) throw new Error("sin codigo");
            if (!apply) return "dry";
            const up = await fetch("https://connect.mailerlite.com/api/subscribers", {
              method: "POST",
              headers: { Authorization: "Bearer " + API, "Content-Type": "application/json" },
              body: JSON.stringify({ email: s.email, fields: { dlqd_codigo: cod } }),
            });
            if (!up.ok) {
              let detalle = "";
              try { detalle = (await up.text()).slice(0, 160); } catch {}
              const err = new Error("HTTP " + up.status);
              err.status = up.status;
              err.email = s.email;
              err.detalle = detalle;
              throw err;
            }
            return "ok";
          })
        );
        for (const res of resultados) {
          if (res.status === "fulfilled") {
            if (apply) escritos++;
          } else {
            errores++;
            if (erroresMuestra.length < 5) {
              const e = res.reason || {};
              erroresMuestra.push({
                status: e.status || null,
                email: enmascara(e.email),
                detalle: e.detalle || String(e.message || e),
              });
            }
          }
        }
      }

      cursor = data.meta && data.meta.next_cursor ? data.meta.next_cursor : null;
    } while (cursor);
  } catch (e) {
    return json(500, { ok: false, error: String(e && e.message ? e.message : e), total, escritos, errores });
  }

  return json(200, {
    ok: true,
    modo: apply ? "aplicado" : "dry-run (no se ha escrito nada)",
    total_suscriptores: total,
    ya_tenian_codigo: yaTenian,
    omitidos_inactivos: omitidosInactivos,
    pendientes_activos: apply ? 0 : (total - yaTenian - omitidosInactivos),
    escritos: apply ? escritos : 0,
    errores,
    errores_muestra: erroresMuestra,
  });
};
