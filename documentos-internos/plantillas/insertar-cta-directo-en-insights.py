#!/usr/bin/env python3
"""
Inserta o reemplaza el bloque CTA al Directo + Newsletter en cada insight HTML.

Versión actual del bloque (v2) · ofrece DOS pasos:
  · CTA primario · Directo «La voz que te juzga» (domingo 7 junio)
  · CTA secundario · Newsletter Te escribo (evergreen)

Estrategia post-7-jun (para futuro · NO automático):
Ejecutar este mismo script con `MODE = 'newsletter_only'` para reemplazar
el bloque por una versión solo Newsletter (sin el Directo, que ya habrá pasado).

Idempotente · si existe `id="cta-directo-7-jun"` (v1 o v2), lo reemplaza
con la versión actual. Si NO existe, lo inserta antes de `</article>` o
`<footer>` (lo que aparezca primero).

Anclas conocidas que necesitan insertion alternativa:
- 24 insights cierran con `</article>` → insertion estándar
- 1 insight (`elegir-es-perder-psicologia-decision.html`) cierra con `</div>`
  antes de `<footer>` → insertion antes de `<footer>`
"""
import os
import re
import sys

INSIGHTS_DIR = '/home/user/theworldismindproject/insights'
CTA_ID = 'cta-directo-7-jun'

# Bloque actual (v2) · Directo + Newsletter
CTA_HTML = '''<aside id="cta-directo-7-jun" style="margin:2.5rem auto 1.5rem;padding:1.6rem 1.8rem;background:#173D30;color:#FDFCFA;border-radius:8px;max-width:720px;font-family:'Barlow Condensed',system-ui,sans-serif;">
  <p style="margin:0 0 .4rem;font-size:.8rem;text-transform:uppercase;letter-spacing:3px;color:#C2A78B;font-weight:500;">Directo gratuito · domingo 7 junio · 19:00 (España)</p>
  <h3 style="margin:0 0 .7rem;font-family:'Instrument Serif',Georgia,serif;font-size:1.7rem;font-weight:400;color:#FDFCFA;letter-spacing:.3px;">La voz que te juzga</h3>
  <p style="margin:0 0 1.2rem;font-size:1rem;color:#FDFCFA;opacity:.92;line-height:1.55;">Una hora en directo sobre la voz interior que siempre te pone un pero · de dónde sale, por qué no se calla con razones, y qué empieza a aflojarla. Sin coaching, sin venta, sin embudo raro.</p>
  <a href="/directo-la-voz-que-te-juzga/" style="display:inline-block;padding:.75rem 1.5rem;background:#C2A78B;color:#173D30;text-decoration:none;border-radius:5px;font-weight:600;font-size:.95rem;letter-spacing:.3px;">Reservar plaza gratuita →</a>
  <p style="margin:1.2rem 0 0;padding-top:1rem;border-top:1px solid rgba(194,167,139,.25);font-size:.9rem;color:#FDFCFA;opacity:.75;line-height:1.55;">¿No te encaja el directo? Suscríbete a <a href="/newsletter/" style="color:#C2A78B;text-decoration:underline;text-decoration-color:rgba(194,167,139,.5);text-underline-offset:3px;">Te escribo</a> · cartas editoriales sobre la mente, el cansancio y lo que no se dice. Sin frecuencia obligada · sin spam.</p>
</aside>'''


def process(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Si ya tiene el bloque (cualquier versión) · REEMPLAZAR
    if CTA_ID in content:
        # Match el aside entero por su id
        pattern = re.compile(
            r'\s*<aside id="cta-directo-7-jun"[^>]*>.*?</aside>',
            re.DOTALL
        )
        new_content = pattern.sub(f'\n    {CTA_HTML}', content, count=1)
        if new_content == content:
            return 'skip-no-match'
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return 'replaced'

    # Si NO tiene · insertar antes de </article> (preferente) o <footer>
    if '</article>' in content:
        new_content = content.replace(
            '</article>',
            f'    {CTA_HTML}\n  </article>',
            1
        )
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return 'inserted-article'
    if '<footer>' in content:
        new_content = content.replace(
            '<footer>',
            f'    {CTA_HTML}\n\n<footer>',
            1
        )
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return 'inserted-footer'

    return 'skip-no-anchor'


def main():
    if not os.path.isdir(INSIGHTS_DIR):
        print(f'ERROR · directorio no existe: {INSIGHTS_DIR}')
        sys.exit(1)

    results = {'replaced': [], 'inserted-article': [], 'inserted-footer': [],
               'skip-no-anchor': [], 'skip-no-match': []}

    for fname in sorted(os.listdir(INSIGHTS_DIR)):
        if not fname.endswith('.html'):
            continue
        if fname.startswith('_template') or fname == 'index.html':
            continue
        path = os.path.join(INSIGHTS_DIR, fname)
        status = process(path)
        results[status].append(fname)

    print('== Resumen ==')
    for key, items in results.items():
        if items:
            print(f'{key} ({len(items)}):')
            for f in items[:3]:
                print(f'  - {f}')
            if len(items) > 3:
                print(f'  ... +{len(items) - 3} más')


if __name__ == '__main__':
    main()
