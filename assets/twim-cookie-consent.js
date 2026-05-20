/**
 * TWIM Project · Cookie Consent Banner
 * v1.0 · 1 mayo 2026 · doc actualizada 20 may 2026 a Consent Mode v2
 *
 * Banner GDPR/LSSI-CE-compliant. Bloquea las cookies analíticas (GA4) y
 * publicitarias (Meta Pixel, Google Ads) hasta que el usuario otorga
 * consentimiento explícito.
 *
 * Uso en cada landing (patrón Google Consent Mode v2):
 *   1. Cargar el script gtag.js de Google + inicializar dataLayer.
 *   2. Llamar a gtag('consent','default',{ ad_storage:'denied',
 *      analytics_storage:'denied', ad_user_data:'denied',
 *      ad_personalization:'denied', wait_for_update:500 }) ANTES de
 *      cualquier gtag('config', ...).
 *   3. Cargar este script con defer:
 *        <script src="/assets/twim-cookie-consent.js" defer></script>
 *
 * Comportamiento: el script gtag se carga al render (1 request a Google
 * sin cookies, permitido bajo Consent Mode v2). NO se graban cookies ni
 * se envían eventos de tracking hasta que este banner llama a
 * gtag('consent','update',{ analytics_storage:'granted', ... }) tras el
 * clic del usuario. Si rechaza, las cookies analíticas/publicitarias
 * quedan denegadas y solo se almacenan cookies técnicas del propio
 * banner (consentimiento persistido 12 meses).
 *
 * NOTA HISTÓRICA: la doc previa decía «No carga ni GA ni Pixel hasta
 * que el usuario acepta» (patrón v1 anterior a Consent Mode v2). Eso
 * implicaba inyectar gtag dinámicamente, lo cual no se llegó a
 * implementar; el contrato real desde v1 es el patrón Consent Mode v2
 * descrito arriba, que sí cumple LSSI-CE y RGPD.
 *
 * window.twimReopenCookies() reabre el modal para reconfigurar.
 */
(function () {
  'use strict';

  const CONSENT_KEY = 'twim_cookie_consent';
  const CONSENT_VERSION = '1';
  const EXPIRY_DAYS = 365;

  function getConsent() {
    try {
      const raw = localStorage.getItem(CONSENT_KEY);
      if (!raw) return null;
      const parsed = JSON.parse(raw);
      if (parsed.version !== CONSENT_VERSION) return null;
      if (parsed.expires && Date.now() > parsed.expires) return null;
      return parsed;
    } catch (e) {
      return null;
    }
  }

  function setConsent(analytics, ads) {
    const data = {
      version: CONSENT_VERSION,
      analytics: !!analytics,
      ads: !!ads,
      timestamp: Date.now(),
      expires: Date.now() + EXPIRY_DAYS * 24 * 60 * 60 * 1000
    };
    try {
      localStorage.setItem(CONSENT_KEY, JSON.stringify(data));
    } catch (e) {}
    applyConsent(data);
  }

  function applyConsent(consent) {
    if (!consent) return;

    if (window.gtag) {
      window.gtag('consent', 'update', {
        'analytics_storage': consent.analytics ? 'granted' : 'denied',
        'ad_storage': consent.ads ? 'granted' : 'denied',
        'ad_user_data': consent.ads ? 'granted' : 'denied',
        'ad_personalization': consent.ads ? 'granted' : 'denied'
      });
    }

    if (consent.ads && typeof window.fbq === 'function') {
      window.fbq('consent', 'grant');
    } else if (typeof window.fbq === 'function') {
      window.fbq('consent', 'revoke');
    }

    document.dispatchEvent(new CustomEvent('twim:consent', { detail: consent }));
  }

  function buildBanner() {
    const wrapper = document.createElement('div');
    wrapper.id = 'twim-cookie-banner';
    wrapper.setAttribute('role', 'dialog');
    wrapper.setAttribute('aria-labelledby', 'twim-cookie-title');
    wrapper.style.cssText = [
      'position:fixed', 'left:1rem', 'right:1rem', 'bottom:1rem',
      'max-width:560px', 'margin:0 auto',
      'background:#173D30', 'color:#FDFCFA',
      'padding:1.4rem 1.5rem', 'border-radius:6px',
      'box-shadow:0 8px 30px rgba(0,0,0,0.25)',
      'font-family:Barlow Condensed,-apple-system,sans-serif',
      'font-size:16px', 'line-height:1.5',
      'z-index:99999'
    ].join(';');

    wrapper.innerHTML =
      '<h2 id="twim-cookie-title" style="margin:0 0 0.6rem;font-size:1.05rem;color:#C2A78B;font-weight:700;letter-spacing:0.5px;text-transform:uppercase">Cookies en TWIM Project</h2>' +
      '<p style="margin:0 0 1rem;color:#FDFCFA">Usamos cookies técnicas (necesarias) y, con tu permiso, analíticas y publicitarias para mejorar la web y medir campañas. Puedes aceptarlas, rechazarlas o configurarlas. Detalle en la <a href="/cookies.html" style="color:#C2A78B;text-decoration:underline">Política de Cookies</a>.</p>' +
      '<div id="twim-cookie-config" style="display:none;margin:0 0 1rem;padding:0.8rem;background:rgba(255,255,255,0.05);border-radius:4px">' +
        '<label style="display:block;margin-bottom:0.5rem"><input type="checkbox" checked disabled> Técnicas <span style="opacity:0.7">(necesarias, no se pueden desactivar)</span></label>' +
        '<label style="display:block;margin-bottom:0.5rem"><input type="checkbox" id="twim-consent-analytics"> Analíticas (Google Analytics anonimizado)</label>' +
        '<label style="display:block"><input type="checkbox" id="twim-consent-ads"> Publicitarias (Meta Pixel, Google Ads)</label>' +
      '</div>' +
      '<div style="display:flex;flex-wrap:wrap;gap:0.5rem">' +
        '<button id="twim-cookie-accept-all" style="flex:1;min-width:120px;background:#C2A78B;color:#173D30;border:0;padding:0.7rem 1rem;border-radius:4px;font-weight:700;cursor:pointer;font-family:inherit">Aceptar todas</button>' +
        '<button id="twim-cookie-reject-all" style="flex:1;min-width:120px;background:transparent;color:#FDFCFA;border:1px solid #C2A78B;padding:0.7rem 1rem;border-radius:4px;font-weight:600;cursor:pointer;font-family:inherit">Solo necesarias</button>' +
        '<button id="twim-cookie-config-toggle" style="flex:1;min-width:120px;background:transparent;color:#C2A78B;border:1px solid #C2A78B;padding:0.7rem 1rem;border-radius:4px;font-weight:600;cursor:pointer;font-family:inherit">Configurar</button>' +
      '</div>' +
      '<button id="twim-cookie-save" style="display:none;width:100%;margin-top:0.6rem;background:#C2A78B;color:#173D30;border:0;padding:0.7rem 1rem;border-radius:4px;font-weight:700;cursor:pointer;font-family:inherit">Guardar mi configuración</button>';

    document.body.appendChild(wrapper);

    document.getElementById('twim-cookie-accept-all').addEventListener('click', function () {
      setConsent(true, true);
      wrapper.remove();
    });
    document.getElementById('twim-cookie-reject-all').addEventListener('click', function () {
      setConsent(false, false);
      wrapper.remove();
    });
    document.getElementById('twim-cookie-config-toggle').addEventListener('click', function () {
      const config = document.getElementById('twim-cookie-config');
      const save = document.getElementById('twim-cookie-save');
      config.style.display = 'block';
      save.style.display = 'block';
    });
    document.getElementById('twim-cookie-save').addEventListener('click', function () {
      const analytics = document.getElementById('twim-consent-analytics').checked;
      const ads = document.getElementById('twim-consent-ads').checked;
      setConsent(analytics, ads);
      wrapper.remove();
    });
  }

  function setDefaultsBeforeConsent() {
    if (typeof window.gtag === 'function') {
      window.gtag('consent', 'default', {
        'analytics_storage': 'denied',
        'ad_storage': 'denied',
        'ad_user_data': 'denied',
        'ad_personalization': 'denied',
        'wait_for_update': 500
      });
    }
  }

  setDefaultsBeforeConsent();

  window.twimReopenCookies = function () {
    if (document.getElementById('twim-cookie-banner')) return;
    buildBanner();
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  function init() {
    const consent = getConsent();
    if (consent) {
      applyConsent(consent);
    } else {
      buildBanner();
    }
  }
})();
