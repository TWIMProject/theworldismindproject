#!/usr/bin/env python3
"""
Genera las portadas Stripe de los 5 productos activos del catálogo TWIM Project
(1080×1080, paleta exacta, sistema visual A1 verde oscuro). Coherente con las
portadas RRSS de `generar-portadas-rrss.py` y con la regla inviolable de naming
Stripe persistida en CLAUDE.md.

Outputs (todos en assets/stripe-portadas/):
- 01-reserva-bachillerato.png
- 02-reserva-tdah.png
- 03-taller-bachillerato.png
- 04-taller-tdah.png
- 05-programa-in-company.png
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1080

# Paleta TWIM
GREEN_DARK = (23, 61, 48)      # #173D30
BEIGE      = (194, 167, 139)   # #C2A78B
CREAM      = (245, 239, 227)
WHITE      = (253, 252, 250)   # #FDFCFA

FONT_DIR = '/root/.fonts'
def font(name, size): return ImageFont.truetype(f'{FONT_DIR}/{name}', size)

OUT = '/home/user/theworldismindproject/assets/stripe-portadas'
os.makedirs(OUT, exist_ok=True)


def draw_centered(draw, text, y, f, color, letter_spacing=0):
    if letter_spacing == 0:
        bbox = draw.textbbox((0, 0), text, font=f)
        w = bbox[2] - bbox[0]
        draw.text(((W - w) // 2, y), text, fill=color, font=f)
    else:
        total = sum((draw.textbbox((0, 0), ch, font=f)[2] + letter_spacing) for ch in text) - letter_spacing
        x = (W - total) // 2
        for ch in text:
            draw.text((x, y), ch, fill=color, font=f)
            x += draw.textbbox((0, 0), ch, font=f)[2] + letter_spacing


def hline(draw, y, color, width=2, half_length=60):
    cx = W // 2
    draw.line([(cx - half_length, y), (cx + half_length, y)], fill=color, width=width)


def base_canvas():
    canvas = Image.new('RGB', (W, H), GREEN_DARK)
    draw = ImageDraw.Draw(canvas)
    draw.rectangle([(40, 40), (W - 40, H - 40)], outline=BEIGE, width=2)
    return canvas, draw


def build(filename, kicker, title_l1, title_l2, subtitle_italic, footer_meta):
    canvas, draw = base_canvas()
    # Kicker arriba con tracking amplio
    draw_centered(draw, kicker, 180,
                  font('BarlowCondensed-Medium.ttf', 28), BEIGE, letter_spacing=4)
    hline(draw, 245, BEIGE)

    # Título serif grande · 2 líneas
    draw_centered(draw, title_l1, 340,
                  font('InstrumentSerif-Regular.ttf', 110), WHITE)
    draw_centered(draw, title_l2, 480,
                  font('InstrumentSerif-Regular.ttf', 110), WHITE)

    # Subtítulo italic en beige · 1-2 líneas centradas
    draw_centered(draw, subtitle_italic, 680,
                  font('InstrumentSerif-Italic.ttf', 40), BEIGE)

    # Footer meta · BarlowCondensed con tracking
    draw_centered(draw, footer_meta, 820,
                  font('BarlowCondensed-Medium.ttf', 32), WHITE)

    hline(draw, 920, BEIGE)
    draw_centered(draw, 'TWIM PROJECT · DANIEL OROZCO ABIA · CV11515', 955,
                  font('BarlowCondensed-Regular.ttf', 20), CREAM, letter_spacing=3)

    out_path = f'{OUT}/{filename}'
    canvas.save(out_path, optimize=True)
    print(f'OK · {filename}')


# 1 · Reserva entrevista Bachillerato (40 €)
build(
    filename='01-reserva-bachillerato.png',
    kicker='TWIM PROJECT · RESERVA',
    title_l1='Entrevista',
    title_l2='informativa',
    subtitle_italic='Antes de inscribir a tu hijo · 90 min contigo.',
    footer_meta='Taller Bachillerato · Encontrar el rumbo',
)

# 2 · Reserva entrevista TDAH adolescentes (40 €)
build(
    filename='02-reserva-tdah.png',
    kicker='TWIM PROJECT · RESERVA',
    title_l1='Entrevista',
    title_l2='informativa',
    subtitle_italic='Antes de inscribir a tu hijo · 90 min contigo.',
    footer_meta='Taller TDAH adolescentes · Más allá del TDAH',
)

# 3 · Taller Bachillerato (720 €)
build(
    filename='03-taller-bachillerato.png',
    kicker='TWIM PROJECT · TALLER',
    title_l1='Encontrar',
    title_l2='el rumbo',
    subtitle_italic='Cuando tu hijo dice «no sé qué quiero».',
    footer_meta='Bachillerato · 16 sesiones · Valencia · sept 2026',
)

# 4 · Taller TDAH adolescentes (720 €)
build(
    filename='04-taller-tdah.png',
    kicker='TWIM PROJECT · TALLER',
    title_l1='Más allá',
    title_l2='del TDAH',
    subtitle_italic='Lo que el diagnóstico nombra · y lo que no.',
    footer_meta='TDAH adolescentes · 16 sesiones · Valencia · sept 2026',
)

# 5 · Programa In-Company «Ansiedad Laboral · Ventaja Competitiva» (2.450 €)
build(
    filename='05-programa-in-company.png',
    kicker='TWIM PROJECT · PROGRAMA IN-COMPANY',
    title_l1='Ansiedad',
    title_l2='laboral.',
    subtitle_italic='Lo que el equipo aguanta · y lo que paga por callárselo.',
    footer_meta='Formación para equipos · 6 sesiones · presencial u online',
)

print('---')
print(f'5 portadas Stripe generadas en {OUT}')
