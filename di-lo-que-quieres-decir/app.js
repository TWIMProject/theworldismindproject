/* Di lo que quieres decir · The World Is Mind Project
   Todo el estado vive en memoria. Nada se guarda en servidor ni en el navegador. */
(function () {
  "use strict";

  var NOMBRE_APP = "Di lo que quieres decir";
  var URL_MOTOR = "/.netlify/functions/traductor-interno";

  var ETIQUETAS_RUIDO = {
    reproche: "Reproche acumulado",
    ataque: "Ataque a la persona",
    defensa: "Anticipación defensiva",
    mensaje_escondido: "Mensaje escondido",
  };

  // Estado de sesión, solo en memoria.
  var estado = {
    texto: "",
    destinatario: "",
    objetivo: "",
    medio: "",           // opcional: en persona / por mensaje escrito / por llamada
    analisis: null,      // { ruidos, reformulacion, frases_ancla }
    modoBasico: false,
    analizado: false,    // evita repetir la llamada si no cambió la entrada
    claveAnalisis: "",
  };

  function $(id) { return document.getElementById(id); }

  // Medición anónima de uso (GA4). Jamás se envía el texto del usuario.
  function evento(nombre, params) {
    if (typeof window.gtag === "function") {
      window.gtag("event", nombre, params || {});
    }
  }

  /* ---------- Acceso: 1 análisis de regalo, después código de suscriptor ----------
     Lo único que se guarda en este navegador es el contador de usos y, si la
     persona se suscribe, su email y su código. El texto jamás. Botón de borrado
     total en el pie. */

  var USOS_GRATIS = 1;
  // Freemium (Motor B, orden de Daniel 12 jun): los suscriptores tienen
  // LIMITE_SUSCRIPTOR_MES análisis gratis al mes; el Pase (pago único,
  // 12 meses) quita el límite. El cobro se enciende rellenando URL_PASE
  // con el Payment Link de Stripe; mientras esté vacío, no hay límite mensual.
  var URL_PASE = "";
  var LIMITE_SUSCRIPTOR_MES = 3;
  // Plus de seguimiento (función de pago adicional al Pase). Mientras
  // PLUS_ACTIVO sea false, su apartado no se muestra (precio por decidir).
  var PLUS_ACTIVO = false;

  function plusGuardado() {
    try {
      var em = localStorage.getItem("dlqd_email");
      var p = localStorage.getItem("dlqd_plus");
      return em && p ? { email: em, plus: p } : null;
    } catch (e) { return null; }
  }
  function guardarPlus(email, plus) {
    try {
      localStorage.setItem("dlqd_email", email);
      localStorage.setItem("dlqd_plus", plus);
    } catch (e) { /* sin storage */ }
  }

  function mesActual() {
    var d = new Date();
    return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0");
  }
  function usosEsteMes() {
    try {
      var raw = JSON.parse(localStorage.getItem("dlqd_usos_mes") || "{}");
      return raw.mes === mesActual() ? (Number(raw.n) || 0) : 0;
    } catch (e) { return 0; }
  }
  function sumarUsoMes() {
    try {
      localStorage.setItem("dlqd_usos_mes", JSON.stringify({ mes: mesActual(), n: usosEsteMes() + 1 }));
    } catch (e) { /* sin storage */ }
  }
  function paseGuardado() {
    try {
      var em = localStorage.getItem("dlqd_email");
      var p = localStorage.getItem("dlqd_pase");
      return em && p ? { email: em, pase: p } : null;
    } catch (e) { return null; }
  }
  function guardarPase(email, pase) {
    try {
      localStorage.setItem("dlqd_email", email);
      localStorage.setItem("dlqd_pase", pase);
    } catch (e) { /* sin storage */ }
  }

  function usosHechos() {
    try { return Number(localStorage.getItem("dlqd_usos") || "0") || 0; } catch (e) { return 0; }
  }
  function sumarUso() {
    try { localStorage.setItem("dlqd_usos", String(usosHechos() + 1)); } catch (e) { /* sin storage: gratis */ }
  }
  function accesoGuardado() {
    try {
      var em = localStorage.getItem("dlqd_email");
      var cod = localStorage.getItem("dlqd_codigo");
      return em && cod ? { email: em, codigo: cod } : null;
    } catch (e) { return null; }
  }
  function guardarAcceso(email, codigo) {
    try {
      localStorage.setItem("dlqd_email", email);
      localStorage.setItem("dlqd_codigo", codigo);
    } catch (e) { /* sin storage: la puerta volverá a salir */ }
  }

  function pedirCodigo(email) {
    return fetch(URL_MOTOR, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ accion: "codigo", email: email }),
    }).then(function (res) { return res.json(); });
  }

  function suscribir(email) {
    return fetch("/.netlify/functions/subscribe", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: email, group: "newsletter-home" }),
    });
  }

  function escaparHTML(s) {
    return s.replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  /* ---------- Navegación entre pasos ---------- */

  function irAPaso(n) {
    for (var i = 1; i <= 5; i++) {
      var seccion = $("paso-" + i);
      seccion.hidden = i !== n;
    }
    var items = document.querySelectorAll("#indicador-lista li");
    items.forEach(function (li) {
      var p = Number(li.getAttribute("data-paso"));
      li.classList.toggle("activo", p === n);
      li.classList.toggle("hecho", p < n);
    });
    window.scrollTo(0, 0);
    var titulo = $("titulo-paso-" + n);
    if (titulo) {
      titulo.setAttribute("tabindex", "-1");
      titulo.focus({ preventScroll: true });
    }
  }

  document.querySelectorAll("[data-volver]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      irAPaso(Number(btn.getAttribute("data-volver")));
    });
  });

  /* ---------- Paso 1 ---------- */

  $("btn-seguir-1").addEventListener("click", function () {
    var texto = $("texto-crudo").value.trim();
    var error = $("error-paso-1");
    if (!texto) {
      error.hidden = false;
      $("texto-crudo").focus();
      return;
    }
    error.hidden = true;
    estado.texto = texto;
    irAPaso(2);
  });

  /* ---------- Paso 2 ---------- */

  function enlazarOtro(selectId, inputId) {
    $(selectId).addEventListener("change", function () {
      var esOtro = this.value === "otro";
      $(inputId).hidden = !esOtro;
      if (esOtro) $(inputId).focus();
    });
  }
  enlazarOtro("destinatario", "destinatario-otro");
  enlazarOtro("objetivo", "objetivo-otro");

  function leerCampo(selectId, inputId) {
    var v = $(selectId).value;
    if (v === "otro") v = $(inputId).value.trim();
    return v || "";
  }

  $("btn-analizar").addEventListener("click", function () {
    var destinatario = leerCampo("destinatario", "destinatario-otro");
    var objetivo = leerCampo("objetivo", "objetivo-otro");
    var error = $("error-paso-2");
    if (!destinatario || !objetivo) {
      error.hidden = false;
      return;
    }
    error.hidden = true;
    estado.destinatario = destinatario;
    estado.objetivo = objetivo;
    estado.medio = $("medio").value;
    if (!paseGuardado()) {
      if (!accesoGuardado() && usosHechos() >= USOS_GRATIS) {
        $("puerta").hidden = false;
        evento("dlqd_puerta_vista", {});
        $("puerta-email").focus();
        return;
      }
      if (accesoGuardado() && URL_PASE && usosEsteMes() >= LIMITE_SUSCRIPTOR_MES) {
        $("panel-pase").hidden = false;
        evento("dlqd_pase_visto", {});
        return;
      }
    }
    irAPaso(3);
    analizar();
  });

  /* ---------- Puerta de suscriptor ---------- */

  function continuarTrasPuerta() {
    $("puerta").hidden = true;
    irAPaso(3);
    analizar();
  }

  function errorPuerta(msg) {
    $("puerta-error").textContent = msg;
    $("puerta-error").hidden = false;
  }

  $("btn-puerta-continuar").addEventListener("click", continuarTrasPuerta);

  $("puerta-alternar").addEventListener("click", function () {
    var verCodigo = $("puerta-codigo").hidden;
    $("puerta-codigo").hidden = !verCodigo;
    $("puerta-alta").hidden = verCodigo;
    this.textContent = verCodigo ? "Quiero un código nuevo" : "Ya tengo mi código";
    $("puerta-error").hidden = true;
  });

  $("btn-puerta").addEventListener("click", function () {
    var email = $("puerta-email").value.trim();
    if (!email || email.indexOf("@") === -1) { errorPuerta("Escribe tu email para conseguir tu código."); return; }
    var btn = this;
    btn.disabled = true;
    $("puerta-error").hidden = true;
    suscribir(email)
      .then(function (res) {
        if (!res.ok) throw new Error("subscribe " + res.status);
        return pedirCodigo(email);
      })
      .then(function (r) {
        if (r && r.ok && r.codigo) {
          guardarAcceso(email, r.codigo);
          evento("dlqd_alta_newsletter", { via: "puerta" });
          evento("generate_lead", { origen: "app-dlqd-puerta" });
          // Enseñar el código antes de continuar (para otros dispositivos).
          $("puerta-alta").hidden = true;
          $("puerta-codigo").hidden = true;
          $("puerta-alternar").hidden = true;
          $("codigo-dado-valor").textContent = r.codigo;
          $("puerta-exito").hidden = false;
        } else if (r && r.code === "no_suscrito") {
          errorPuerta("Tu alta está en camino. Espera unos segundos y vuelve a pulsar el botón.");
          btn.disabled = false;
        } else {
          throw new Error("codigo");
        }
      })
      .catch(function () {
        errorPuerta("No se ha podido completar. Inténtalo de nuevo en un momento.");
        btn.disabled = false;
      });
  });

  $("btn-puerta-entrar").addEventListener("click", function () {
    var email = $("puerta-email-2").value.trim();
    var cod = $("puerta-cod").value.trim().toUpperCase();
    if (!email || !cod) { errorPuerta("Escribe el email y el código."); return; }
    var btn = this;
    btn.disabled = true;
    $("puerta-error").hidden = true;
    fetch(URL_MOTOR, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ accion: "validar", email: email, codigo: cod }),
    })
      .then(function (res) { return res.json(); })
      .then(function (r) {
        if (r && r.ok && r.valido) {
          if (r.tipo === "plus") {
            guardarPase(email, cod);
            guardarPlus(email, cod);
          } else if (r.tipo === "pase") {
            guardarPase(email, cod);
          } else {
            guardarAcceso(email, cod);
          }
          continuarTrasPuerta();
        } else {
          errorPuerta("Ese código no coincide con ese email. Revísalos o pide un código nuevo.");
          btn.disabled = false;
        }
      })
      .catch(function () {
        errorPuerta("No se ha podido comprobar. Inténtalo de nuevo en un momento.");
        btn.disabled = false;
      });
  });

  /* ---------- Pase de pago (freemium) ---------- */

  if (URL_PASE) {
    $("enlace-pase").href = URL_PASE;
  }

  $("btn-pase-tengo").addEventListener("click", function () {
    // Reutiliza la puerta en modo «ya tengo mi código»: valida también pases.
    $("panel-pase").hidden = true;
    $("puerta").hidden = false;
    if ($("puerta-codigo").hidden) $("puerta-alternar").click();
    $("puerta-email-2").focus();
  });

  // Vuelta de Stripe: canjear la sesión de pago por el Pase.
  (function canjearPaseSiVuelveDeStripe() {
    var params = new URLSearchParams(window.location.search);
    var sesion = params.get("pase_sesion");
    if (!sesion) return;
    history.replaceState(null, "", window.location.pathname);
    fetch(URL_MOTOR, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ accion: "pase", session_id: sesion }),
    })
      .then(function (res) { return res.json(); })
      .then(function (r) {
        if (r && r.ok && r.pase && r.email) {
          guardarPase(r.email, r.pase);
          evento("dlqd_pase_canjeado", {});
          $("aviso-pase-ok").hidden = false;
        }
      })
      .catch(function () { /* podrá canjearlo con «ya tengo mi código» */ });
  })();

  $("btn-borrar-datos").addEventListener("click", function () {
    try {
      localStorage.removeItem("dlqd_usos");
      localStorage.removeItem("dlqd_usos_mes");
      localStorage.removeItem("dlqd_email");
      localStorage.removeItem("dlqd_codigo");
      localStorage.removeItem("dlqd_pase");
      localStorage.removeItem("dlqd_plus");
    } catch (e) { /* nada que borrar */ }
    var btn = this;
    btn.textContent = "Datos borrados de este navegador";
    setTimeout(function () {
      btn.textContent = "Borrar mis datos de este navegador";
    }, 2500);
  });

  /* ---------- Paso 3 · análisis ---------- */

  $("btn-reintentar").addEventListener("click", analizar);

  function claveDeEntrada() {
    return [estado.texto, estado.destinatario, estado.objetivo, estado.medio].join(" | ");
  }

  function analizar() {
    var clave = claveDeEntrada();
    if (estado.analizado && estado.claveAnalisis === clave) {
      pintarAnalisis();
      return;
    }
    $("cargando").hidden = false;
    $("error-analisis").hidden = true;
    $("aviso-modo-basico").hidden = true;
    $("resultado-analisis").hidden = true;
    $("btn-seguir-3").hidden = true;

    fetch(URL_MOTOR, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        texto: estado.texto,
        destinatario: estado.destinatario,
        objetivo: estado.objetivo,
        medio: estado.medio,
      }),
    })
      .then(function (res) {
        return res.json().then(function (datos) { return { status: res.status, datos: datos }; });
      })
      .then(function (r) {
        if (r.datos && r.datos.ok && r.datos.resultado) {
          aceptarAnalisis(r.datos.resultado, false, clave);
        } else if (r.datos && r.datos.code === "sin_clave") {
          // Sin clave configurada: modo degradado por reglas, avisando con honestidad.
          aceptarAnalisis(analisisPorReglas(), true, clave);
        } else if (r.datos && r.datos.reintentable) {
          // Resiliencia ante picos: también en sobrecarga se ofrece el modo básico.
          mostrarErrorAnalisis("Ahora mismo hay mucha gente usando la herramienta y no hemos podido leer tu texto. Espera unos segundos y reinténtalo, o sigue con el análisis básico.", true);
        } else {
          mostrarErrorAnalisis("No hemos podido hacer el análisis completo. Puedes reintentarlo o seguir con el análisis básico.", true);
        }
      })
      .catch(function () {
        mostrarErrorAnalisis("Parece que no hay conexión. Comprueba tu red y reinténtalo, o sigue con el análisis básico.", true);
      });
  }

  function aceptarAnalisis(resultado, esBasico, clave) {
    estado.analisis = normalizarResultado(resultado);
    estado.modoBasico = esBasico;
    estado.analizado = true;
    estado.claveAnalisis = clave;
    if (!esBasico) { sumarUso(); sumarUsoMes(); }
    evento("dlqd_analisis", { modo: esBasico ? "basico" : "ia", destinatario: estado.destinatario, objetivo: estado.objetivo });
    pintarAnalisis();
  }

  function mostrarErrorAnalisis(mensaje, ofrecerBasico) {
    $("cargando").hidden = true;
    $("error-analisis-texto").textContent = mensaje;
    $("error-analisis").hidden = false;
    if (ofrecerBasico && !$("btn-basico")) {
      var btn = document.createElement("button");
      btn.type = "button";
      btn.id = "btn-basico";
      btn.className = "btn btn-secundario";
      btn.textContent = "Usar análisis básico";
      btn.addEventListener("click", function () {
        aceptarAnalisis(analisisPorReglas(), true, claveDeEntrada());
      });
      $("error-analisis").appendChild(btn);
    }
  }

  function normalizarResultado(r) {
    var ruidos = Array.isArray(r.ruidos) ? r.ruidos.filter(function (x) {
      return x && typeof x.fragmento === "string" && x.fragmento &&
        ETIQUETAS_RUIDO[x.tipo] && typeof x.explicacion === "string";
    }) : [];
    return {
      ruidos: ruidos,
      reformulacion: typeof r.reformulacion === "string" && r.reformulacion.trim()
        ? r.reformulacion.trim()
        : reformulacionPorReglas(),
      frases_ancla: Array.isArray(r.frases_ancla) && r.frases_ancla.length
        ? r.frases_ancla.slice(0, 3)
        : frasesAnclaPorReglas(),
    };
  }

  /* ---------- Modo degradado: detección por reglas en español ---------- */

  var REGLAS = [
    { tipo: "reproche", re: /\b(?:siempre|nunca|jam[áa]s|otra vez|todo el (?:d[íi]a|tiempo)|cada vez que|como siempre|de siempre)\b/gi,
      exp: "Las palabras totales («siempre», «nunca», «otra vez») hacen que el otro se defienda del «siempre» en vez de escuchar lo que necesitas." },
    { tipo: "ataque", re: /\beres (?:un[a]? |tan )?(?:ego[íi]sta|in[úu]til|desastre|mentiros[oa]|fr[íi][oa]|borde|imb[ée]cil|incapaz|injust[oa]|cobarde|vag[oa])\w*/gi,
      exp: "Esto habla del carácter de la otra persona, no de lo que hace. Quien se siente atacado deja de escuchar y empieza a defenderse." },
    { tipo: "ataque", re: /\bno te (?:importa|importo|entera[s]?|enteras de nada)\b[^,.!?]*/gi,
      exp: "Afirmar lo que el otro siente o le importa suena a sentencia. Es muy probable que conteste a eso y no a lo que le pides." },
    { tipo: "defensa", re: /\bya s[ée] que (?:me vas a decir|vas a decir|piensas|dir[áa]s)[^,.!?]*/gi,
      exp: "Contestar antes de que el otro hable convierte la conversación en una discusión imaginaria. Deja que responda de verdad." },
    { tipo: "defensa", re: /\b(?:antes de que (?:me )?digas|no es por|seguro que (?:piensas|crees|me dices))[^,.!?]*/gi,
      exp: "Justificarte por adelantado desvía el foco de lo que quieres pedir hacia tu defensa." },
    { tipo: "mensaje_escondido", re: /\b(?:paso de [^,.!?]+|me da igual|haz lo que quieras|no me importa|olv[íi]dalo|d[ée]jalo|para qu[ée] te lo digo)\b/gi,
      exp: "Esto suena a indiferencia, pero debajo hay algo que necesitas y no está dicho. Si lo dejas así, el otro se quedará con la indiferencia." },
  ];

  function analisisPorReglas() {
    var ruidos = [];
    REGLAS.forEach(function (regla) {
      regla.re.lastIndex = 0;
      var m;
      while ((m = regla.re.exec(estado.texto)) !== null) {
        ruidos.push({ fragmento: m[0], tipo: regla.tipo, explicacion: regla.exp });
        if (m.index === regla.re.lastIndex) regla.re.lastIndex++;
      }
    });
    return {
      ruidos: ruidos,
      reformulacion: reformulacionPorReglas(),
      frases_ancla: frasesAnclaPorReglas(),
    };
  }

  function emocionInferida() {
    // Devuelve una frase completa que funciona tras "cuando pasa, ".
    var t = estado.texto.toLowerCase();
    if (/hart[oa]|no puedo m[áa]s|al l[íi]mite|agotad[oa]|cansad[oa]/.test(t)) return "me siento al límite";
    if (/triste|duele|dolid[oa]|llorar|pena\b/.test(t)) return "me duele de verdad";
    if (/sol[oa]\b|ignorad[oa]|invisible/.test(t)) return "siento que no cuento para ti";
    if (/rabia|cabread[oa]|enfadad[oa]|furios[oa]/.test(t)) return "se me llena el cuerpo de rabia";
    return "siento que no me tienes en cuenta";
  }

  // Peticiones con enfoque vínculo (sello de la herramienta): el sujeto que
  // importa es el «nosotros». Regla de concordancia: la frase del vínculo se
  // mantiene en plural de principio a fin; la primera persona va en frase aparte.
  var PETICIONES = {
    "que me entienda": "Para lo que tenemos, importa que nos entendamos de verdad. Escúchame un momento, aunque no estés de acuerdo.",
    "que cambie algo concreto": "Para cuidar lo que tenemos, necesitamos que algo cambie. ¿Acordamos una cosa concreta y la probamos esta semana?",
    "que nos reconciliemos": "Lo que tenemos importa más que esta pelea. ¿Lo hablamos con calma, sin guardarnos nada?",
    "poner un límite": "Esto que pasa daña lo que tenemos. Necesito que no se repita; te lo digo en serio y con respeto.",
    "pedir algo": "Para cuidar lo que tenemos, te pido una cosa concreta. Piénsala de verdad antes de contestar.",
  };

  // Variantes para mensaje escrito: sin verbos que empujen a verse o hablar en voz alta.
  var PETICIONES_ESCRITO = {
    "que me entienda": "Para lo que tenemos, importa que nos entendamos de verdad. Léeme entero antes de contestar, aunque no estés de acuerdo.",
    "que nos reconciliemos": "Lo que tenemos importa más que esta pelea. Contéstame cuando puedas hacerlo con calma, sin guardarte nada.",
  };

  function reformulacionPorReglas() {
    // Plantilla del modo básico: sin IA no puede leer el contenido, así que
    // es deliberadamente general y la interfaz lo avisa en los pasos 3, 4 y 5.
    var peticion =
      (estado.medio === "por mensaje escrito" && PETICIONES_ESCRITO[estado.objetivo]) ||
      PETICIONES[estado.objetivo] ||
      "Necesito que esto lo tratemos con calma, sin que se nos vaya a otra cosa.";
    var apertura;
    if (estado.medio === "por mensaje escrito") {
      apertura = "Te escribo esto porque dicho a la cara me cuesta que salga como quiero. ";
    } else if (estado.medio === "por llamada") {
      apertura = "Quiero llamarte para contarte algo que me importa. ";
    } else {
      apertura = "Quiero contarte algo que me importa. ";
    }
    return apertura +
      "Hay una cosa que se me repite por dentro y, cuando pasa, " + emocionInferida() + ". " +
      "No te lo digo para atacarte: te lo digo porque me importa lo que tenemos. " +
      peticion;
  }

  var ANCLA_POR_OBJETIVO = {
    "que me entienda": "No busco tener razón: busco que entiendas cómo lo vivo yo.",
    "que cambie algo concreto": "Te pido un cambio concreto por nosotros. No te estoy juzgando como persona.",
    "que nos reconciliemos": "Te estoy diciendo esto porque quiero que estemos bien, no para reabrir la herida.",
    "poner un límite": "Esto es un límite para mí y necesito que lo respetes.",
    "pedir algo": "Te lo estoy pidiendo a ti porque confío en ti.",
  };

  function frasesAnclaPorReglas() {
    return [
      "No te estoy atacando: te estoy pidiendo algo concreto.",
      "Esto no va de quién tiene razón: va de cuidar lo que tenemos.",
      ANCLA_POR_OBJETIVO[estado.objetivo] ||
        "Volvamos a lo que te estaba diciendo: " + estado.objetivo + ".",
    ];
  }

  /* ---------- Pintado del análisis (paso 3) ---------- */

  function localizarFragmentos() {
    // Devuelve tramos no solapados {ini, fin, tipo, explicacion}, ordenados.
    var tramos = [];
    estado.analisis.ruidos.forEach(function (r) {
      var ini = estado.texto.indexOf(r.fragmento);
      while (ini !== -1) {
        var fin = ini + r.fragmento.length;
        var solapa = tramos.some(function (t) { return ini < t.fin && fin > t.ini; });
        if (!solapa) { tramos.push({ ini: ini, fin: fin, tipo: r.tipo, explicacion: r.explicacion }); break; }
        ini = estado.texto.indexOf(r.fragmento, fin);
      }
    });
    return tramos.sort(function (a, b) { return a.ini - b.ini; });
  }

  function pintarAnalisis() {
    $("cargando").hidden = true;
    $("error-analisis").hidden = true;
    $("aviso-modo-basico").hidden = !estado.modoBasico;

    var tramos = localizarFragmentos();
    var resumen = $("resumen-ruido");
    if (tramos.length === 0) {
      resumen.textContent = "No hemos encontrado ruido claro en tu texto. Aun así, mira la versión depurada del siguiente paso: a veces ordena lo que ya estaba bien.";
    } else {
      resumen.textContent = "Hemos encontrado " + tramos.length +
        (tramos.length === 1 ? " fragmento que puede desviar" : " fragmentos que pueden desviar") +
        " la conversación de lo que quieres: " + estado.objetivo + ".";
    }

    // Texto con resaltados
    var html = "";
    var cursor = 0;
    tramos.forEach(function (t) {
      html += escaparHTML(estado.texto.slice(cursor, t.ini));
      html += '<mark class="ruido-' + t.tipo + '">' + escaparHTML(estado.texto.slice(t.ini, t.fin)) + "</mark>";
      cursor = t.fin;
    });
    html += escaparHTML(estado.texto.slice(cursor));
    $("texto-resaltado").innerHTML = html;

    // Explicaciones
    var lista = $("lista-explicaciones");
    lista.innerHTML = "";
    tramos.forEach(function (t) {
      var li = document.createElement("li");
      li.innerHTML =
        '<span class="tipo-etiqueta ruido-' + t.tipo + '">' + ETIQUETAS_RUIDO[t.tipo] + "</span>" +
        '<span class="fragmento-cita">«' + escaparHTML(estado.texto.slice(t.ini, t.fin)) + "»</span>" +
        escaparHTML(t.explicacion);
      lista.appendChild(li);
    });

    $("resultado-analisis").hidden = false;
    $("btn-seguir-3").hidden = false;
  }

  /* ---------- Paso 4 ---------- */

  $("btn-seguir-3").addEventListener("click", function () {
    $("texto-antes").textContent = estado.texto;
    $("aviso-basico-4").hidden = !estado.modoBasico;
    if (!$("texto-despues").value.trim() || $("texto-despues").dataset.origen !== estado.claveAnalisis) {
      $("texto-despues").value = estado.analisis.reformulacion;
      $("texto-despues").dataset.origen = estado.claveAnalisis;
    }
    irAPaso(4);
  });

  /* ---------- Paso 5 ---------- */

  $("btn-seguir-4").addEventListener("click", function () {
    var mensaje = $("texto-despues").value.trim() || estado.analisis.reformulacion;
    $("aviso-basico-5").hidden = !estado.modoBasico;
    // Si ya tiene código o Pase (= ya está suscrita), el bloque de newsletter sobra.
    $("titulo-newsletter").parentElement.hidden = Boolean(accesoGuardado() || paseGuardado());
    // El seguimiento solo se muestra cuando el Plus esté a la venta y la persona lo tenga.
    $("seccion-seguimiento").hidden = !(PLUS_ACTIVO && plusGuardado());
    $("mensaje-final").textContent = mensaje;
    var lista = $("frases-ancla");
    lista.innerHTML = "";
    estado.analisis.frases_ancla.forEach(function (f) {
      var li = document.createElement("li");
      li.textContent = f;
      lista.appendChild(li);
    });
    irAPaso(5);
  });

  $("btn-copiar").addEventListener("click", function () {
    var texto = $("mensaje-final").textContent;
    function avisar() {
      $("copiado-ok").hidden = false;
      setTimeout(function () { $("copiado-ok").hidden = true; }, 2500);
    }
    evento("dlqd_mensaje_copiado", { modo: estado.modoBasico ? "basico" : "ia" });
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(texto).then(avisar, function () { copiarFallback(texto, avisar); });
    } else {
      copiarFallback(texto, avisar);
    }
  });

  /* ---------- Captación newsletter (paso 5, opcional) ---------- */

  $("form-newsletter").addEventListener("submit", function (e) {
    e.preventDefault();
    var email = $("email-newsletter").value.trim();
    if (!email) return;
    var btn = $("btn-newsletter");
    btn.disabled = true;
    $("newsletter-error").hidden = true;
    suscribir(email)
      .then(function (res) {
        if (!res.ok) throw new Error("subscribe " + res.status);
        $("form-newsletter").hidden = true;
        $("newsletter-ok").hidden = false;
        evento("dlqd_alta_newsletter", { via: "paso5" });
        evento("generate_lead", { origen: "app-dlqd" });
        // Le dejamos también su código guardado y se lo enseñamos.
        return pedirCodigo(email).then(function (r) {
          if (r && r.ok && r.codigo) {
            guardarAcceso(email, r.codigo);
            $("newsletter-ok").textContent = "Hecho. Tu código personal para usar la app donde quieras: " + r.codigo + " — apúntalo. Te escribiré cuando algo merezca tu tiempo.";
          }
        }).catch(function () { /* el código podrá pedirlo en la puerta */ });
      })
      .catch(function () {
        $("newsletter-error").hidden = false;
        btn.disabled = false;
      });
  });

  function copiarFallback(texto, listo) {
    var ta = document.createElement("textarea");
    ta.value = texto;
    ta.setAttribute("readonly", "");
    ta.style.position = "absolute";
    ta.style.left = "-9999px";
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand("copy"); listo(); } catch (e) { /* sin permiso: el usuario puede seleccionar a mano */ }
    document.body.removeChild(ta);
  }

  $("btn-empezar").addEventListener("click", function () {
    estado = { texto: "", destinatario: "", objetivo: "", medio: "", analisis: null, modoBasico: false, analizado: false, claveAnalisis: "" };
    $("texto-crudo").value = "";
    $("destinatario").selectedIndex = 0;
    $("objetivo").selectedIndex = 0;
    $("medio").selectedIndex = 0;
    $("destinatario-otro").value = ""; $("destinatario-otro").hidden = true;
    $("objetivo-otro").value = ""; $("objetivo-otro").hidden = true;
    $("texto-despues").value = ""; delete $("texto-despues").dataset.origen;
    irAPaso(1);
  });

  /* ---------- Seguimiento de conversación (Plus) ---------- */

  $("btn-seguimiento").addEventListener("click", function () {
    var contestacion = $("texto-respuesta").value.trim();
    var plus = plusGuardado();
    if (!contestacion) {
      $("seguimiento-error").textContent = "Pega primero lo que te ha respondido.";
      $("seguimiento-error").hidden = false;
      return;
    }
    if (!plus) return;
    var btn = this;
    btn.disabled = true;
    $("seguimiento-error").hidden = true;
    fetch(URL_MOTOR, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        accion: "seguimiento",
        email: plus.email,
        plus: plus.plus,
        mensaje_enviado: $("mensaje-final").textContent,
        respuesta: contestacion,
        destinatario: estado.destinatario,
        objetivo: estado.objetivo,
        medio: estado.medio,
      }),
    })
      .then(function (res) { return res.json(); })
      .then(function (r) {
        btn.disabled = false;
        if (r && r.ok && r.resultado) {
          $("seguimiento-lectura").textContent = r.resultado.lectura || "";
          $("seguimiento-mensaje").textContent = r.resultado.siguiente_mensaje || "";
          var lista = $("seguimiento-anclas");
          lista.innerHTML = "";
          (r.resultado.frases_ancla || []).forEach(function (f) {
            var li = document.createElement("li");
            li.textContent = f;
            lista.appendChild(li);
          });
          $("seguimiento-resultado").hidden = false;
          evento("dlqd_seguimiento", {});
        } else {
          $("seguimiento-error").textContent = "No se ha podido preparar el mensaje. Inténtalo de nuevo en un momento.";
          $("seguimiento-error").hidden = false;
        }
      })
      .catch(function () {
        btn.disabled = false;
        $("seguimiento-error").textContent = "No se ha podido conectar. Inténtalo de nuevo en un momento.";
        $("seguimiento-error").hidden = false;
      });
  });

  // Aviso interno en consola, sin datos del usuario.
  if (window.console) console.info(NOMBRE_APP + " · sin almacenamiento: todo vive en memoria de esta pestaña.");
})();
