// Netlify Function: motor de análisis de «Di lo que quieres decir»
// (di-lo-que-quieres-decir/). Proxy sin estado hacia la API de Anthropic:
// no guarda, no loguea y no reenvía a ningún otro sitio el texto del usuario.
//
// Variables de entorno requeridas (Netlify → Site configuration → Environment variables):
//   ANTHROPIC_API_KEY          → clave de la API de Anthropic (nunca en el repo)
//   TRADUCTOR_INTERNO_MODEL    → (opcional) sobrescribe el modelo por defecto
//
// Si no hay clave configurada devuelve 503 con code "sin_clave" y el front
// pasa a modo degradado (detección por reglas en el navegador).

const MODELO_POR_DEFECTO = "claude-haiku-4-5-20251001";

const ALLOWED_ORIGINS = new Set([
  "https://twimproject.com",
  "https://www.twimproject.com",
  "http://localhost:8888",
  "http://localhost:3000",
]);

// Los deploy previews del propio sitio también son orígenes legítimos
// (necesarios para verificar PRs antes de mergear).
const RE_DEPLOY_PREVIEW = /^https:\/\/deploy-preview-\d+--lighthearted-kitten-8aba94\.netlify\.app$/;

function origenPermitido(origen) {
  return ALLOWED_ORIGINS.has(origen) || RE_DEPLOY_PREVIEW.test(origen);
}

// El usuario nunca ve esta lógica interna: hecho observable + emoción en
// primera persona + necesidad real + petición concreta. El prompt evita
// jerga clínica en el output por regla editorial TWIM.
// v2 (12 jun, feedback de Daniel): el volcado en crudo mezcla capas
// (meta-instrucciones, desahogo en tercera persona, mensaje directo) y el
// motor debe distinguirlas, obedecer las meta-instrucciones (canal, miedos)
// y construir la reformulación SOLO con material del texto — nada genérico.
const SYSTEM_PROMPT = `Eres el motor interno de una herramienta que ayuda a una persona a preparar una conversación importante (con su pareja, su madre o padre, su hijo o hija, su jefe o jefa, una amistad...). Recibes un JSON con estos campos: "texto" (lo que la persona ha escrito en crudo, sin filtro), "destinatario" (a quién va dirigido), "objetivo" (qué quiere que pase después de la conversación) y, opcionalmente, "medio" (cómo quiere decírselo: "en persona", "por mensaje escrito" o "por llamada"; puede venir vacío).

ANTES DE NADA, lee el texto completo sabiendo que un volcado en crudo suele mezclar tres capas, y tu primer trabajo es distinguirlas:
(a) META-INSTRUCCIONES dirigidas a la herramienta o a sí mismo: cómo quiere decirlo («quiero mandarle un WhatsApp», «no quiero hablarlo en persona porque me pongo nervioso y la conversación se va por las ramas»), qué teme («sin que se sienta atacada»), qué ha intentado ya. Estas frases NO son ruido a señalar: son REQUISITOS que debes obedecer en la reformulación y en las frases ancla.
(b) DESAHOGO sobre la otra persona, a menudo en tercera persona («siempre se hace la víctima», «es incapaz de disculparse»). Aquí está el ruido a detectar y, sobre todo, el material real: las escenas, los hechos y las necesidades concretas.
(c) FRASES dirigidas directamente al destinatario, en segunda persona.

Tu trabajo tiene tres partes y devuelves las tres en el JSON de salida.

1. DETECTAR RUIDO. Localiza en el texto crudo fragmentos LITERALES (copiados exactamente, carácter a carácter, tal cual aparecen, para poder resaltarlos) que pertenezcan a estos cuatro tipos:
   - "reproche": reproche acumulado — generalizaciones sobre el otro ("siempre", "nunca", "otra vez", "todo el tiempo", "eres así desde...").
   - "ataque": ataque a la persona en vez de a la conducta — adjetivos o etiquetas sobre el carácter del otro ("egoísta", "no te importa nada", "es una contradicción andante").
   - "defensa": anticipación defensiva — justificarse antes de que el otro hable ("ya sé que me vas a decir que...", "no es por...", "antes de que digas nada...").
   - "mensaje_escondido": lo que de verdad se necesita pero aparece disfrazado de queja, amenaza o indiferencia ("paso de hablar contigo", "haz lo que quieras", "me da igual").
   Si el fragmento está en tercera persona (capa b), señálalo igualmente: explica cómo contaminaría la conversación si llegara así, o en ese tono, al destinatario. Para cada fragmento, escribe una "explicacion" de una o dos frases, en lenguaje llano y concreto, de por qué ese fragmento desviará la conversación del objetivo declarado. Conecta la explicación con el objetivo concreto y con el destinatario. Nada de tecnicismos psicológicos.

2. REFORMULAR. "reformulacion" es EL MENSAJE LISTO PARA ENTREGAR, dirigido al destinatario en segunda persona — aunque el volcado hable de él o ella en tercera persona, tú lo conviertes en mensaje directo. Reglas inviolables:
   - SE CONSTRUYE CON EL MATERIAL DEL TEXTO: las escenas, los hechos, las expresiones y las palabras de la persona. Cada frase de la reformulación debe poder rastrearse a algo que la persona escribió. PROHIBIDO el relleno genérico de manual («llevo tiempo callándome», «me importa lo que tenemos», «busquemos un momento para hablar») salvo que la persona lo haya dicho con sus palabras.
   - RESPETA EL MEDIO: si "medio" indica mensaje escrito, o el texto lo dice (WhatsApp, carta, email), redacta el mensaje tal cual se enviaría por escrito y NO propongas «hablarlo en persona» ni «buscar un momento para hablar». Si es en persona o por llamada, redacta lo que la persona dirá de viva voz. Si "medio" viene vacío y el texto no da pistas, no menciones el canal.
   - RESPETA LOS MIEDOS DECLARADOS: si la persona pide que el otro no se sienta atacado, cuida especialmente esas formulaciones sin diluir la verdad de lo que necesita decir.
   - Estructura interna (sin nombrarla nunca): hecho concreto observable + cómo se siente la persona en primera persona + qué necesita de verdad + una petición específica y realizable.
   - Usa el vocabulario y el registro de la persona: si escribe coloquial, la reformulación suena coloquial. Debe sonar a ella, no a un manual de comunicación.
   - Conserva la emoción legítima (la frustración, la tristeza, el enfado) sin los ataques.
   - Tutea al destinatario igual que el texto original. Concreto siempre: escenas, gestos, momentos.
   - Longitud proporcional al material: si la persona ha escrito mucho y con detalle, el mensaje puede tener varios párrafos. No lo comprimas a tres frases genéricas.

3. FRASES ANCLA. Escribe en "frases_ancla" exactamente 3 frases cortas que la persona pueda usar para volver al tema si la conversación se tuerce (si el otro desvía, contraataca o la propia persona se activa). Generadas a partir del objetivo declarado y del material del texto, en primera persona, en su registro, y adaptadas al medio: si el mensaje va por escrito, son respuestas para cuando la conversación por mensajes se desvíe; si es en persona o por llamada, son frases para decir en voz alta.

Reglas globales: no moralices, no diagnostiques, no uses tecnicismos psicológicos, no inventes hechos que no estén en el texto. Si el texto no contiene ruido de algún tipo, simplemente no incluyas fragmentos de ese tipo. Responde únicamente con el JSON.`;

const ESQUEMA_SALIDA = {
  type: "object",
  properties: {
    ruidos: {
      type: "array",
      items: {
        type: "object",
        properties: {
          fragmento: { type: "string", description: "Fragmento literal del texto original" },
          tipo: { type: "string", enum: ["reproche", "ataque", "defensa", "mensaje_escondido"] },
          explicacion: { type: "string" },
        },
        required: ["fragmento", "tipo", "explicacion"],
        additionalProperties: false,
      },
    },
    reformulacion: { type: "string" },
    frases_ancla: { type: "array", items: { type: "string" } },
  },
  required: ["ruidos", "reformulacion", "frases_ancla"],
  additionalProperties: false,
};

// Mitigación de abuso: la función es públicamente invocable y CORS solo
// protege dentro del navegador. Tres barreras de mejor esfuerzo antes de
// gastar en la API: (1) se rechazan peticiones sin Origin de la allowlist,
// (2) límite por IP y (3) tope global, ambos en memoria de la instancia
// warm (cada instancia cuenta por separado: acota el coste, no lo elimina).
// Si la app gana tracción pública, subir a Turnstile o rate limiting de
// Netlify — decisión de Daniel, documentada en el PR #338.
const VENTANA_MS = 60_000;
const LIMITE_POR_IP = 6;
const LIMITE_GLOBAL = 60;
const cubosPorIP = new Map();
let cuboGlobal = { inicio: 0, n: 0 };

function superaLimite(ip) {
  const ahora = Date.now();
  if (ahora - cuboGlobal.inicio > VENTANA_MS) cuboGlobal = { inicio: ahora, n: 0 };
  cuboGlobal.n++;
  if (cuboGlobal.n > LIMITE_GLOBAL) return true;
  if (cubosPorIP.size > 5000) cubosPorIP.clear();
  const cubo = cubosPorIP.get(ip);
  if (!cubo || ahora - cubo.inicio > VENTANA_MS) {
    cubosPorIP.set(ip, { inicio: ahora, n: 1 });
    return false;
  }
  cubo.n++;
  return cubo.n > LIMITE_POR_IP;
}

function respuesta(statusCode, body, origin) {
  return {
    statusCode,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Access-Control-Allow-Origin": origin,
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
      "Vary": "Origin",
      "Cache-Control": "no-store",
    },
    // Un 204 debe ir sin cuerpo (preflight CORS).
    body: statusCode === 204 ? "" : JSON.stringify(body),
  };
}

exports.handler = async (event) => {
  const origenPeticion = event.headers?.origin || event.headers?.Origin || "";
  const origin = origenPermitido(origenPeticion)
    ? origenPeticion
    : "https://twimproject.com";

  if (event.httpMethod === "OPTIONS") {
    return respuesta(204, {}, origin);
  }

  // Diagnóstico sin exponer valores (mismo patrón que subscribe.js):
  // GET /.netlify/functions/traductor-interno?diag=1
  if (event.httpMethod === "GET") {
    if ((event.queryStringParameters || {}).diag === "1") {
      return respuesta(200, {
        ok: true,
        diag: {
          clave_configurada: Boolean(process.env.ANTHROPIC_API_KEY),
          modelo: process.env.TRADUCTOR_INTERNO_MODEL || MODELO_POR_DEFECTO,
        },
      }, origin);
    }
    return respuesta(405, { ok: false, code: "metodo" }, origin);
  }

  if (event.httpMethod !== "POST") {
    return respuesta(405, { ok: false, code: "metodo" }, origin);
  }

  // Un Origin server-to-server es falsificable, pero exigirlo corta el abuso
  // ingenuo (curl directo, scrapers) sin afectar al uso real desde la web.
  if (!origenPermitido(origenPeticion)) {
    return respuesta(403, { ok: false, code: "origen" }, origin);
  }

  const ip =
    event.headers["x-nf-client-connection-ip"] ||
    (event.headers["x-forwarded-for"] || "").split(",")[0].trim() ||
    "desconocida";
  if (superaLimite(ip)) {
    return respuesta(429, { ok: false, code: "sobrecarga", reintentable: true }, origin);
  }

  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) {
    return respuesta(503, { ok: false, code: "sin_clave" }, origin);
  }

  let datos;
  try {
    datos = JSON.parse(event.body || "{}");
  } catch {
    return respuesta(400, { ok: false, code: "json_invalido" }, origin);
  }

  const texto = typeof datos.texto === "string" ? datos.texto.trim() : "";
  const destinatario = typeof datos.destinatario === "string" ? datos.destinatario.trim() : "";
  const objetivo = typeof datos.objetivo === "string" ? datos.objetivo.trim() : "";
  const medio = typeof datos.medio === "string" ? datos.medio.trim().slice(0, 60) : "";
  if (!texto || !destinatario || !objetivo) {
    return respuesta(400, { ok: false, code: "campos" }, origin);
  }
  if (texto.length > 20000) {
    return respuesta(413, { ok: false, code: "texto_largo" }, origin);
  }

  const modelo = process.env.TRADUCTOR_INTERNO_MODEL || MODELO_POR_DEFECTO;

  let upstream;
  try {
    upstream = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "x-api-key": apiKey,
        "anthropic-version": "2023-06-01",
      },
      body: JSON.stringify({
        model: modelo,
        // 4000 da margen a volcados largos: con 3000, un texto extenso podía
        // truncar el JSON (stop_reason max_tokens) y forzar el modo básico.
        max_tokens: 4000,
        system: SYSTEM_PROMPT,
        messages: [
          { role: "user", content: JSON.stringify({ texto, destinatario, objetivo, medio }) },
        ],
        output_config: { format: { type: "json_schema", schema: ESQUEMA_SALIDA } },
      }),
    });
  } catch {
    return respuesta(502, { ok: false, code: "red", reintentable: true }, origin);
  }

  if (!upstream.ok) {
    // 429 (límite de peticiones) y 5xx/529 (sobrecarga) son reintentables.
    if (upstream.status === 429 || upstream.status >= 500) {
      return respuesta(502, { ok: false, code: "sobrecarga", reintentable: true }, origin);
    }
    return respuesta(500, { ok: false, code: "api" }, origin);
  }

  let mensaje;
  try {
    mensaje = await upstream.json();
  } catch {
    return respuesta(502, { ok: false, code: "respuesta_invalida", reintentable: true }, origin);
  }

  if (mensaje.stop_reason === "refusal") {
    return respuesta(500, { ok: false, code: "api" }, origin);
  }

  const bloqueTexto = Array.isArray(mensaje.content)
    ? mensaje.content.find((b) => b.type === "text")
    : null;
  if (!bloqueTexto) {
    return respuesta(502, { ok: false, code: "respuesta_invalida", reintentable: true }, origin);
  }

  let resultado;
  try {
    resultado = JSON.parse(bloqueTexto.text);
  } catch {
    return respuesta(502, { ok: false, code: "respuesta_invalida", reintentable: true }, origin);
  }

  return respuesta(200, { ok: true, resultado }, origin);
};
