/* Te escribo · cross-sell submit handler (shared)
 * Recorre todos los <section class="te-escribo-cta"> y engancha el form
 * → POST /.netlify/functions/subscribe { email, group: 'newsletter-home' }
 */
(function () {
  function init() {
    var blocks = document.querySelectorAll('.te-escribo-cta');
    if (!blocks.length) return;
    blocks.forEach(function (root) {
      var form = root.querySelector('[data-te-form]');
      var ok = root.querySelector('[data-te-ok]');
      var err = root.querySelector('[data-te-err]');
      if (!form || form.dataset.teBound === '1') return;
      form.dataset.teBound = '1';
      form.addEventListener('submit', async function (e) {
        e.preventDefault();
        var btn = form.querySelector('button');
        var emailInput = form.querySelector('input[name="email"]');
        var email = emailInput ? emailInput.value.trim() : '';
        if (!email || email.indexOf('@') === -1) {
          if (err) { err.textContent = 'Introduce un email válido.'; err.style.display = 'block'; }
          return;
        }
        btn.disabled = true;
        var label = btn.textContent;
        btn.textContent = 'Enviando...';
        if (err) err.style.display = 'none';
        try {
          var res = await fetch('/.netlify/functions/subscribe', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email: email, group: 'newsletter-home' })
          });
          if (!res.ok) throw new Error('req_failed');
          form.style.display = 'none';
          if (ok) ok.style.display = 'block';
          if (window.gtag) gtag('event', 'newsletter_signup', { source: 'cross_sell_seo', landing: location.pathname });
        } catch (ex) {
          btn.disabled = false;
          btn.textContent = label;
          if (err) {
            err.textContent = 'No se pudo completar. Inténtalo en un momento.';
            err.style.display = 'block';
          }
        }
      });
    });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
