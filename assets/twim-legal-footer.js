/**
 * TWIM Project · Legal Footer Injector
 * v1.0 · 1 mayo 2026
 *
 * Inyecta automáticamente un mini-footer con enlaces legales al final del body
 * SI la página todavía no tiene esos enlaces. Detecta presencia mediante
 * búsqueda de href a /privacy.html o /aviso-legal.html.
 *
 * Uso en cada landing:
 *   <script src="/assets/twim-legal-footer.js" defer></script>
 *
 * No reemplaza footers existentes. Solo añade un bloque mínimo al final del body
 * cuando faltan los links legales obligatorios.
 */
(function () {
  'use strict';

  function hasLegalLinks() {
    const links = document.querySelectorAll('a[href]');
    let foundPrivacy = false;
    let foundLegal = false;
    let foundCookies = false;
    for (let i = 0; i < links.length; i++) {
      const href = links[i].getAttribute('href') || '';
      if (/privacy\.html/i.test(href) || /privacidad/i.test(href)) foundPrivacy = true;
      if (/aviso-legal\.html/i.test(href)) foundLegal = true;
      if (/cookies\.html/i.test(href)) foundCookies = true;
    }
    return foundPrivacy && foundLegal && foundCookies;
  }

  function injectFooter() {
    if (hasLegalLinks()) return;
    if (document.getElementById('twim-legal-footer-injected')) return;

    const footer = document.createElement('div');
    footer.id = 'twim-legal-footer-injected';
    footer.style.cssText = [
      'background:#173D30',
      'color:#FDFCFA',
      'padding:1.2rem 1rem',
      'text-align:center',
      'font-family:Barlow Condensed,-apple-system,sans-serif',
      'font-size:14px',
      'line-height:1.5',
      'margin-top:3rem'
    ].join(';');

    footer.innerHTML =
      '<div style="max-width:820px;margin:0 auto">' +
        '<p style="margin:0 0 0.4rem;font-weight:600;letter-spacing:0.5px">Daniel Orozco Abia · Psicólogo General Sanitario · CV11515</p>' +
        '<p style="margin:0;color:#C2A78B">' +
          '<a href="/" style="color:#C2A78B;text-decoration:none;margin:0 0.5rem">Inicio</a>·' +
          '<a href="/privacy.html" style="color:#C2A78B;text-decoration:none;margin:0 0.5rem">Privacidad</a>·' +
          '<a href="/cookies.html" style="color:#C2A78B;text-decoration:none;margin:0 0.5rem">Cookies</a>·' +
          '<a href="/aviso-legal.html" style="color:#C2A78B;text-decoration:none;margin:0 0.5rem">Aviso legal</a>' +
        '</p>' +
      '</div>';

    document.body.appendChild(footer);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectFooter);
  } else {
    injectFooter();
  }
})();
