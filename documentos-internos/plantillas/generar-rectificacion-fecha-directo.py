#!/usr/bin/env python3
"""
Genera la imagen de RECTIFICACIÓN de fecha del Directo «La voz que te juzga».

Pieza social urgente · 1080×1080 (feed) + 1080×1920 (story).
El error es que se anunció 8 junio cuando en realidad es DOMINGO 7 junio.
Visual: «8 JUNIO» tachado en rojo · «7 JUNIO» limpio y grande encima/debajo.

Sistema visual TWIM A1 verde · paleta exacta · Instrument Serif + Barlow Condensed.
Rojo de rectificación = único color ajeno permitido (códice editorial: rojo solo
para señalar error corregido · convención periodística clásica).

Output en rectificacion-directo-7-jun/ (raíz del repo)
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = '/home/user/theworldismindproject/rectificacion-directo-7-jun'
os.makedirs(OUT, exist_ok=True)

GREEN_DARK = (23, 61, 48)
BEIGE      = (194, 167, 139)
CREAM      = (245, 239, 227)
WHITE      = (253, 252, 250)
RED        = (200, 50, 45)        # rojo rectificación · contundente sin chillón
RED_SOFT   = (220, 90, 80)

FONT_DIR = '/root/.fonts'
def font(name, size): return ImageFont.truetype(f'{FONT_DIR}/{name}', size)


def centered(draw, text, y, f, color, W, ls=0):
    if ls == 0:
        bbox = draw.textbbox((0, 0), text, font=f)
        draw.text(((W - (bbox[2] - bbox[0])) // 2, y), text, fill=color, font=f)
    else:
        total = sum(draw.textbbox((0, 0), ch, font=f)[2] + ls for ch in text) - ls
        x = (W - total) // 2
        for ch in text:
            draw.text((x, y), ch, fill=color, font=f)
            x += draw.textbbox((0, 0), ch, font=f)[2] + ls


def text_width(draw, text, f):
    bbox = draw.textbbox((0, 0), text, font=f)
    return bbox[2] - bbox[0]


def hline(draw, y, color, W, w=2, half=60):
    cx = W // 2
    draw.line([(cx - half, y), (cx + half, y)], fill=color, width=w)


def draw_strike_text(draw, text, x, y, f, text_color, strike_color, strike_w=8, tilt=False):
    """Dibuja texto con un tachón en rojo encima · simula corrección manual."""
    draw.text((x, y), text, fill=text_color, font=f)
    bbox = draw.textbbox((x, y), text, font=f)
    # tachón horizontal (un poco por encima del centro · queda más natural)
    cy = (bbox[1] + bbox[3]) // 2
    pad = 8
    if tilt:
        draw.line([(bbox[0] - pad, cy + 6), (bbox[2] + pad, cy - 6)],
                  fill=strike_color, width=strike_w)
    else:
        draw.line([(bbox[0] - pad, cy), (bbox[2] + pad, cy)],
                  fill=strike_color, width=strike_w)


def base(W, H):
    c = Image.new('RGB', (W, H), GREEN_DARK)
    d = ImageDraw.Draw(c)
    d.rectangle([(40, 40), (W - 40, H - 40)], outline=BEIGE, width=2)
    return c, d


# ─────────────────────────────────────────────────────────────
# VERSIÓN 1 · FEED 1080×1080
# ─────────────────────────────────────────────────────────────
W, H = 1080, 1080
c, d = base(W, H)

# Header pequeño · etiqueta «RECTIFICACIÓN»
centered(d, 'RECTIFICACIÓN', 115,
         font('BarlowCondensed-Medium.ttf', 30), RED_SOFT, W, ls=6)
hline(d, 170, BEIGE, W)

# Bloque tachado: «8 JUNIO» grande, tachado en rojo
f_strike = font('InstrumentSerif-Regular.ttf', 150)
strike_txt = '8 JUNIO'
sw = text_width(d, strike_txt, f_strike)
sx = (W - sw) // 2
draw_strike_text(d, strike_txt, sx, 240, f_strike,
                 text_color=BEIGE, strike_color=RED, strike_w=10)

# Subtexto pequeño «era»
centered(d, 'era', 425,
         font('InstrumentSerif-Italic.ttf', 38), CREAM, W)

# Bloque correcto · MUCHO más grande, en blanco
centered(d, 'DOMINGO', 490,
         font('BarlowCondensed-Medium.ttf', 60), CREAM, W, ls=8)
centered(d, '7 JUNIO', 560,
         font('InstrumentSerif-Regular.ttf', 200), WHITE, W)

hline(d, 800, BEIGE, W, half=80)

# Datos del directo
centered(d, 'LA VOZ QUE TE JUZGA',  840,
         font('BarlowCondensed-Medium.ttf', 34), BEIGE, W, ls=5)
centered(d, 'Directo gratuito · 19:00 hora Madrid',  885,
         font('InstrumentSerif-Italic.ttf', 32), CREAM, W)

# Footer URL
centered(d, 'twimproject.com/directo-la-voz-que-te-juzga/', 985,
         font('BarlowCondensed-Regular.ttf', 26), BEIGE, W, ls=2)
centered(d, '@daniorozcopsicologo', 1025,
         font('BarlowCondensed-Regular.ttf', 22), WHITE, W, ls=2)

c.save(f'{OUT}/rectificacion-feed-1080.png', optimize=True)
print('OK · feed 1080×1080')


# ─────────────────────────────────────────────────────────────
# VERSIÓN 2 · STORY 1080×1920
# ─────────────────────────────────────────────────────────────
W, H = 1080, 1920
c, d = base(W, H)

centered(d, 'RECTIFICACIÓN', 230,
         font('BarlowCondensed-Medium.ttf', 38), RED_SOFT, W, ls=8)
hline(d, 300, BEIGE, W)

# «8 JUNIO» tachado
f_strike = font('InstrumentSerif-Regular.ttf', 170)
strike_txt = '8 JUNIO'
sw = text_width(d, strike_txt, f_strike)
sx = (W - sw) // 2
draw_strike_text(d, strike_txt, sx, 430, f_strike,
                 text_color=BEIGE, strike_color=RED, strike_w=12)

centered(d, 'era', 650,
         font('InstrumentSerif-Italic.ttf', 46), CREAM, W)

centered(d, 'DOMINGO', 760,
         font('BarlowCondensed-Medium.ttf', 72), CREAM, W, ls=10)
centered(d, '7 JUNIO', 850,
         font('InstrumentSerif-Regular.ttf', 240), WHITE, W)

hline(d, 1180, BEIGE, W, half=100)

centered(d, 'LA VOZ QUE TE JUZGA',  1240,
         font('BarlowCondensed-Medium.ttf', 42), BEIGE, W, ls=6)
centered(d, 'Directo gratuito · 19:00 hora Madrid',  1310,
         font('InstrumentSerif-Italic.ttf', 38), CREAM, W)
centered(d, 'Una hora · sobre la voz que te juzga por dentro.',  1370,
         font('BarlowCondensed-Regular.ttf', 30), CREAM, W)

hline(d, 1500, BEIGE, W, half=80)

centered(d, 'RESERVAR PLAZA', 1560,
         font('BarlowCondensed-Medium.ttf', 36), WHITE, W, ls=6)
centered(d, 'twimproject.com/directo-la-voz-que-te-juzga/', 1620,
         font('BarlowCondensed-Regular.ttf', 30), BEIGE, W, ls=2)

centered(d, '@daniorozcopsicologo · twimproject.com', 1810,
         font('BarlowCondensed-Regular.ttf', 24), WHITE, W, ls=2)

c.save(f'{OUT}/rectificacion-story-1080x1920.png', optimize=True)
print('OK · story 1080×1920')


print('---')
print(f'Rectificación · 2 piezas generadas en {OUT}')
