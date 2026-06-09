/* TWIM · medición de conversión para Google Ads
   Dispara un evento GA4 "generate_lead" cuando alguien hace clic en un CTA de
   contacto (WhatsApp, email o teléfono) desde una landing de captación.
   Pasivo: no altera el enlace, el comportamiento ni el diseño. Usa el gtag (GA4)
   que ya está cargado en la página. Luego en GA4 se marca "generate_lead" como
   evento clave y se importa a Google Ads como conversión. */
(function () {
  function fire(method) {
    if (typeof window.gtag === 'function') {
      window.gtag('event', 'generate_lead', { method: method, source: 'landing' });
    }
  }
  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest ? e.target.closest('a') : null;
    if (!a) return;
    var href = (a.getAttribute('href') || '').toLowerCase();
    if (href.indexOf('wa.me') !== -1 || href.indexOf('api.whatsapp') !== -1) {
      fire('whatsapp');
    } else if (href.indexOf('mailto:') === 0) {
      fire('email');
    } else if (href.indexOf('tel:') === 0) {
      fire('phone');
    }
  }, true);
})();
