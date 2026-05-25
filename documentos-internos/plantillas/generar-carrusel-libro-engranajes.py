#!/usr/bin/env python3
"""
Genera el carrusel IG (4 slides 1080x1080) del libro
«Los Engranajes de la Mente» · paleta TWIM verde · sistema A1
+ portada real del libro en slide final + CTA dual Cap III + Amazon.

Coherente con `documentos-internos/plantillas/generar-portadas-rrss.py`,
`palancas-venta-libro-engranajes-15-may-2026.md` §3.1 y
`marca-twim-criterio-dopamina-comercial.md`.

Pieza de venta · aplica criterio dopamina-comercial sin atacar
disciplinas hermanas (regla decidida para IG el 24-may).
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1080
OUT = '/home/user/theworldismindproject'

# ---- Paleta TWIM ----
GREEN_DARK = (23, 61, 48)      # #173D30
GREEN      = (38, 92, 75)      # #265C4B
BEIGE      = (194, 167, 139)   # #C2A78B
CREAM      = (245, 239, 227)
WHITE      = (253, 252, 250)   # #FDFCFA

FONT_DIR = '/root/.fonts'
def font(name, size): return ImageFont.truetype(f'{FONT_DIR}/{name}', size)

def draw_centered(draw, text, y, f, color, letter_spacing=0):
    if letter_spacing == 0:
        bbox = draw.textbbox((0,0), text, font=f)
        w = bbox[2] - bbox[0]
        draw.text(((W - w) // 2, y), text, fill=color, font=f)
    else:
        total = sum((draw.textbbox((0,0), ch, font=f)[2] + letter_spacing) for ch in text) - letter_spacing
        x = (W - total) // 2
        for ch in text:
            draw.text((x, y), ch, fill=color, font=f)
            x += draw.textbbox((0,0), ch, font=f)[2] + letter_spacing

def hline(draw, y, color, width=2, half_length=60):
    cx = W // 2
    draw.line([(cx - half_length, y), (cx + half_length, y)], fill=color, width=width)

def base_canvas():
    canvas = Image.new('RGB', (W, H), GREEN_DARK)
    draw = ImageDraw.Draw(canvas)
    draw.rectangle([(40, 40), (W-40, H-40)], outline=BEIGE, width=2)
    return canvas, draw

def header_kicker(draw, text='LIBRO · LOS ENGRANAJES DE LA MENTE'):
    draw_centered(draw, text, 110,
                  font('BarlowCondensed-Medium.ttf', 26), BEIGE, letter_spacing=4)
    hline(draw, 165, BEIGE)

def footer_indicator(draw, idx, total=4):
    hline(draw, H - 130, BEIGE)
    draw_centered(draw, f'{idx} / {total}  ·  DESLIZA' if idx < total else f'{idx} / {total}',
                  H - 105,
                  font('BarlowCondensed-Medium.ttf', 24), BEIGE, letter_spacing=3)
    draw_centered(draw, '@daniorozcopsicologo · twimproject.com', H - 65,
                  font('BarlowCondensed-Regular.ttf', 19), WHITE, letter_spacing=2)


# ===== SLIDE 1 · HOOK · imagen mental concreta =====
canvas, draw = base_canvas()
header_kicker(draw)

draw_centered(draw, 'Sabes', 290,
              font('InstrumentSerif-Regular.ttf', 130), WHITE)
draw_centered(draw, 'lo que tendrías', 430,
              font('InstrumentSerif-Regular.ttf', 130), WHITE)
draw_centered(draw, 'que hacer.', 570,
              font('InstrumentSerif-Regular.ttf', 130), WHITE)

draw_centered(draw, 'Y no lo haces.', 760,
              font('InstrumentSerif-Italic.ttf', 56), BEIGE)

footer_indicator(draw, 1)
canvas.save(f'{OUT}/carrusel-libro-engranajes-slide-1.png', optimize=True)
print('OK · slide 1')


# ===== SLIDE 2 · CONSTATAR · qué NO es =====
canvas, draw = base_canvas()
header_kicker(draw)

draw_centered(draw, 'No es falta', 290,
              font('InstrumentSerif-Regular.ttf', 130), WHITE)
draw_centered(draw, 'de información.', 430,
              font('InstrumentSerif-Regular.ttf', 130), WHITE)
draw_centered(draw, 'No es falta de fuerza.', 590,
              font('InstrumentSerif-Italic.ttf', 70), BEIGE)

draw_centered(draw, 'Es otra cosa.', 740,
              font('InstrumentSerif-Italic.ttf', 56), CREAM)

footer_indicator(draw, 2)
canvas.save(f'{OUT}/carrusel-libro-engranajes-slide-2.png', optimize=True)
print('OK · slide 2')


# ===== SLIDE 3 · NOMBRAR · diferenciación clínica =====
canvas, draw = base_canvas()
header_kicker(draw)

draw_centered(draw, 'Faltan', 270,
              font('InstrumentSerif-Regular.ttf', 130), WHITE)
draw_centered(draw, 'los engranajes', 410,
              font('InstrumentSerif-Regular.ttf', 130), WHITE)
draw_centered(draw, 'entre entender', 550,
              font('InstrumentSerif-Regular.ttf', 90), WHITE)
draw_centered(draw, 'y cambiar.', 660,
              font('InstrumentSerif-Regular.ttf', 90), WHITE)

draw_centered(draw, 'Las piezas pequeñas que la cabeza salta', 800,
              font('InstrumentSerif-Italic.ttf', 36), BEIGE)
draw_centered(draw, 'y el cuerpo nota.', 845,
              font('InstrumentSerif-Italic.ttf', 36), BEIGE)

footer_indicator(draw, 3)
canvas.save(f'{OUT}/carrusel-libro-engranajes-slide-3.png', optimize=True)
print('OK · slide 3')


# ===== SLIDE 4 · CTA · portada real del libro + dual Cap III + Amazon =====
canvas, draw = base_canvas()
draw_centered(draw, 'TWIM PROJECT · LIBRO', 90,
              font('BarlowCondensed-Medium.ttf', 24), BEIGE, letter_spacing=4)

draw_centered(draw, 'Los Engranajes', 150,
              font('InstrumentSerif-Regular.ttf', 56), WHITE)
draw_centered(draw, 'de la Mente', 215,
              font('InstrumentSerif-Italic.ttf', 56), BEIGE)

book = Image.open(f'{OUT}/portadalosengranajes.jpg').convert('RGBA')
target_w = 300
target_h = int(book.height * target_w / book.width)
book = book.resize((target_w, target_h), Image.LANCZOS)

shadow = Image.new('RGBA', (target_w + 60, target_h + 60), (0,0,0,0))
sh_draw = ImageDraw.Draw(shadow)
sh_draw.rectangle([(30, 30), (30 + target_w, 30 + target_h)], fill=(0, 0, 0, 140))
shadow = shadow.filter(ImageFilter.GaussianBlur(radius=18))

book_x = (W - target_w) // 2
book_y = 305
canvas.paste(shadow, (book_x - 30, book_y - 15), shadow)
canvas.paste(book, (book_x, book_y), book)

cta_y = book_y + target_h + 25
draw_centered(draw, 'Capítulo III gratis · sin spam, sin embudo raro', cta_y,
              font('BarlowCondensed-Medium.ttf', 24), WHITE)
draw_centered(draw, 'twimproject.com/libro/capitulo-3/', cta_y + 32,
              font('BarlowCondensed-Regular.ttf', 20), BEIGE)
draw_centered(draw, 'Libro completo · disponible en Amazon', cta_y + 75,
              font('BarlowCondensed-Medium.ttf', 24), WHITE)

hline(draw, H - 95, BEIGE)
draw_centered(draw, 'Daniel Orozco Abia · Psicólogo CV11515 · @daniorozcopsicologo', H - 72,
              font('BarlowCondensed-Regular.ttf', 17), WHITE, letter_spacing=1)

canvas.save(f'{OUT}/carrusel-libro-engranajes-slide-4.png', optimize=True)
print('OK · slide 4')
print('---')
print('Carrusel libro Engranajes · 4 slides generados.')
