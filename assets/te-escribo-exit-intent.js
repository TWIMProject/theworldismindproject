/* Te escribo · exit-intent modal
 * Carga en cada landing SEO. Una sola muestra por sesión.
 * Triggers: mouse leaves top of viewport (desktop) · 35s on page (touch)
 * POST → /.netlify/functions/subscribe { email, group:'newsletter-home' }
 */
(function () {
  // sessionStorage puede fallar (modo incógnito, storage bloqueado).
  // Fallback in-memory para que la función no se rompa.
  var seenInMemory = false;
  function alreadyShown() {
    try { return sessionStorage.getItem('twim_te_seen') === '1'; }
    catch (_) { return seenInMemory; }
  }
  function markShown() {
    seenInMemory = true;
    try { sessionStorage.setItem('twim_te_seen', '1'); } catch (_) {}
  }

  if (alreadyShown()) return;
  if (location.pathname.indexOf('/newsletter') === 0) return; // no en /newsletter/
  if (location.pathname === '/' || location.pathname === '/index.html') return; // home ya tiene su form

  var armed = false;
  var fired = false;
  var isTouch = ('ontouchstart' in window) || (navigator.maxTouchPoints > 0);

  function arm() {
    if (armed) return;
    armed = true;
    if (isTouch) {
      setTimeout(function () { if (!fired) trigger('time'); }, 35000);
    } else {
      document.addEventListener('mouseout', function (e) {
        if (fired) return;
        if (e.relatedTarget) return;
        if (e.clientY > 0) return;
        trigger('mouseleave');
      });
    }
  }

  function trigger(reason) {
    if (fired) return;
    fired = true;
    markShown();
    mount(reason);
  }

  function mount(reason) {
    var css = '\
.twim-te-overlay{position:fixed;inset:0;background:rgba(23,61,48,.86);backdrop-filter:blur(4px);z-index:99998;display:flex;align-items:center;justify-content:center;padding:1rem;animation:twimTeFade .25s ease-out;}\
@keyframes twimTeFade{from{opacity:0}to{opacity:1}}\
.twim-te-card{background:#FDFCFA;color:#2B2420;max-width:480px;width:100%;border-radius:10px;padding:2.4rem 1.8rem 1.8rem;font-family:"Barlow Condensed",sans-serif;font-weight:300;line-height:1.6;position:relative;box-shadow:0 24px 60px rgba(0,0,0,.35);animation:twimTeRise .3s ease-out;}\
@keyframes twimTeRise{from{transform:translateY(20px);opacity:0}to{transform:translateY(0);opacity:1}}\
.twim-te-close{position:absolute;top:.7rem;right:.9rem;background:none;border:none;font-size:1.6rem;color:rgba(43,36,32,.4);cursor:pointer;line-height:1;font-family:inherit;}\
.twim-te-close:hover{color:#173D30;}\
.twim-te-kicker{font-size:.74rem;letter-spacing:3px;text-transform:uppercase;color:#C2A78B;margin:0 0 .7rem;font-weight:400;}\
.twim-te-card h2{font-size:1.55rem;line-height:1.2;color:#173D30;font-weight:600;margin:0 0 1rem;letter-spacing:.3px;}\
.twim-te-sub{font-size:1rem;color:#3a322d;margin:0 0 1.4rem;}\
.twim-te-form{display:flex;flex-direction:column;gap:.55rem;}\
.twim-te-form input[type=email]{background:#fff;border:1px solid rgba(23,61,48,.2);color:#2B2420;padding:.85rem 1rem;border-radius:6px;font-family:inherit;font-size:1rem;}\
.twim-te-form input[type=email]:focus{outline:none;border-color:#173D30;}\
.twim-te-form button{background:#173D30;color:#fff;border:none;padding:.95rem 1rem;border-radius:6px;font-family:inherit;font-size:1rem;font-weight:500;cursor:pointer;transition:background .15s;}\
.twim-te-form button:hover{background:#0d2a20;}\
.twim-te-form button:disabled{opacity:.5;cursor:not-allowed;}\
.twim-te-fine{font-size:.78rem;color:rgba(43,36,32,.5);margin-top:.8rem;}\
.twim-te-skip{margin-top:.9rem;background:none;border:none;color:rgba(43,36,32,.5);font-size:.85rem;cursor:pointer;font-family:inherit;text-decoration:underline;}\
.twim-te-skip:hover{color:#173D30;}\
.twim-te-ok{display:none;background:rgba(23,61,48,.06);border:1px solid rgba(23,61,48,.15);padding:1.1rem;border-radius:6px;color:#173D30;}\
.twim-te-err{color:#a3261c;font-size:.9rem;margin-top:.5rem;display:none;}';

    var style = document.createElement('style');
    style.textContent = css;
    document.head.appendChild(style);

    var ov = document.createElement('div');
    ov.className = 'twim-te-overlay';
    ov.setAttribute('role', 'dialog');
    ov.setAttribute('aria-modal', 'true');
    ov.setAttribute('aria-labelledby', 'twim-te-title');
    ov.innerHTML =
      '<div class="twim-te-card">' +
        '<button class="twim-te-close" aria-label="Cerrar" data-twim-close>&times;</button>' +
        '<p class="twim-te-kicker">Te escribo</p>' +
        '<h2 id="twim-te-title">Antes de irte: lo que has venido a buscar a lo mejor está aquí.</h2>' +
        '<p class="twim-te-sub">Una carta cada tanto, escrita por mí. Sobre la mente, el cansancio y lo que no se dice. No es coaching. No es positividad. Es leer la propia historia, despacio.</p>' +
        '<form class="twim-te-form" data-twim-form novalidate>' +
          '<input type="email" name="email" placeholder="Tu email" aria-label="Tu email" required autocomplete="email">' +
          '<button type="submit">Quiero recibirlas</button>' +
          '<p class="twim-te-fine">Sin spam. Te puedes dar de baja cuando quieras.</p>' +
          '<p class="twim-te-err" data-twim-err></p>' +
        '</form>' +
        '<div class="twim-te-ok" data-twim-ok><strong>Hecho.</strong> Te he escrito al correo. Mira tu bandeja.</div>' +
        '<button class="twim-te-skip" data-twim-close>Ahora no</button>' +
      '</div>';
    document.body.appendChild(ov);

    var lastFocus = document.activeElement;
    var firstField = ov.querySelector('input[name="email"]');
    if (firstField) firstField.focus();

    function onEsc(e) { if (e.key === 'Escape') close(); }

    function close() {
      document.removeEventListener('keydown', onEsc);
      ov.remove();
      try { if (lastFocus && typeof lastFocus.focus === 'function') lastFocus.focus(); } catch (_) {}
    }

    ov.addEventListener('click', function (e) {
      if (e.target === ov) close();
    });
    ov.querySelectorAll('[data-twim-close]').forEach(function (b) {
      b.addEventListener('click', close);
    });
    document.addEventListener('keydown', onEsc);

    var form = ov.querySelector('[data-twim-form]');
    var ok = ov.querySelector('[data-twim-ok]');
    var err = ov.querySelector('[data-twim-err]');
    form.addEventListener('submit', async function (e) {
      e.preventDefault();
      var btn = form.querySelector('button');
      var email = form.querySelector('input[name="email"]').value.trim();
      if (!email || email.indexOf('@') === -1) {
        err.textContent = 'Introduce un email válido.';
        err.style.display = 'block';
        return;
      }
      btn.disabled = true;
      var label = btn.textContent;
      btn.textContent = 'Enviando...';
      err.style.display = 'none';
      try {
        var res = await fetch('/.netlify/functions/subscribe', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email: email, group: 'newsletter-home' })
        });
        if (!res.ok) throw new Error('req_failed');
        form.style.display = 'none';
        ok.style.display = 'block';
        if (window.gtag) gtag('event', 'newsletter_signup', { source: 'exit_intent', reason: reason, landing: location.pathname });
      } catch (ex) {
        btn.disabled = false;
        btn.textContent = label;
        err.textContent = 'No se pudo completar. Inténtalo en un momento.';
        err.style.display = 'block';
      }
    });

    if (window.gtag) gtag('event', 'newsletter_modal_shown', { source: 'exit_intent', reason: reason, landing: location.pathname });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', arm);
  } else {
    arm();
  }
})();
