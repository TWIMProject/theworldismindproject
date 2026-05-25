#!/usr/bin/env python3
"""
Añade un bloque CTA al Directo «La voz que te juzga» (7 jun 2026 19:00)
al final de cada insight HTML, justo antes del cierre `</article>`.

Idempotente · si el insight ya contiene el bloque (detectado por el ID
`cta-directo-7-jun`), lo salta. Si tiene un `article-cta` obsoleto que
menciona la Carta #2 del 19 mayo (fecha pasada), lo reemplaza por uno
limpio + el nuevo CTA al Directo.

Conservador: solo modifica si encuentra exactamente un `</article>`.
"""
import os
import re
import sys

INSIGHTS_DIR = '/home/user/theworldismindproject/insights'
CTA_MARKER = 'id="cta-directo-7-jun"'

CTA_HTML = '''<aside id="cta-directo-7-jun" style="margin:2.5rem auto 1.5rem;padding:1.6rem 1.8rem;background:#173D30;color:#FDFCFA;border-radius:8px;max-width:720px;font-family:'Barlow Condensed',system-ui,sans-serif;">
  <p style="margin:0 0 .4rem;font-size:.8rem;text-transform:uppercase;letter-spacing:3px;color:#C2A78B;font-weight:500;">Directo gratuito · domingo 7 junio · 19:00 (España)</p>
  <h3 style="margin:0 0 .7rem;font-family:'Instrument Serif',Georgia,serif;font-size:1.7rem;font-weight:400;color:#FDFCFA;letter-spacing:.3px;">La voz que te juzga</h3>
  <p style="margin:0 0 1.2rem;font-size:1rem;color:#FDFCFA;opacity:.92;line-height:1.55;">Una hora en directo sobre la voz interior que siempre te pone un pero · de dónde sale, por qué no se calla con razones, y qué empieza a aflojarla. Sin coaching, sin venta, sin embudo raro.</p>
  <a href="/directo-la-voz-que-te-juzga/" style="display:inline-block;padding:.75rem 1.5rem;background:#C2A78B;color:#173D30;text-decoration:none;border-radius:5px;font-weight:600;font-size:.95rem;letter-spacing:.3px;">Reservar plaza gratuita →</a>
</aside>'''


def process(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Idempotencia: si ya tiene el bloque, skip
    if CTA_MARKER in content:
        return 'skip-idempotent'

    # Detectar y limpiar bloque article-cta obsoleto (Carta #2 19 mayo)
    article_cta_obsolete = re.compile(
        r'<div class="article-cta">.*?</div>\s*',
        re.DOTALL
    )
    if 'Carta #2' in content or '19 de mayo' in content:
        # Hay copy obsoleto · reemplazar bloque article-cta entero
        # SOLO si es el bloque exacto del article-cta
        if '<div class="article-cta">' in content:
            content = article_cta_obsolete.sub('', content, count=1)

    # Insertar el CTA antes del primer </article>
    if content.count('</article>') != 1:
        return 'skip-no-article'

    new_content = content.replace(
        '</article>',
        f'    {CTA_HTML}\n  </article>',
        1
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return 'ok'


def main():
    if not os.path.isdir(INSIGHTS_DIR):
        print(f'ERROR · directorio no existe: {INSIGHTS_DIR}')
        sys.exit(1)

    results = {'ok': [], 'skip-idempotent': [], 'skip-no-article': []}

    for fname in sorted(os.listdir(INSIGHTS_DIR)):
        if not fname.endswith('.html'):
            continue
        if fname.startswith('_template') or fname == 'index.html':
            continue
        path = os.path.join(INSIGHTS_DIR, fname)
        status = process(path)
        results[status].append(fname)

    print(f'== Resumen ==')
    print(f'OK procesados ............ {len(results["ok"])}')
    print(f'Skip idempotente (ya tienen) {len(results["skip-idempotent"])}')
    print(f'Skip sin </article> ........ {len(results["skip-no-article"])}')
    if results['skip-no-article']:
        print('Avisar Daniel · sin </article>:')
        for f in results['skip-no-article']:
            print(f'  - {f}')


if __name__ == '__main__':
    main()
