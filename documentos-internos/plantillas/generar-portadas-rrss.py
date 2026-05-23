#!/usr/bin/env python3
"""
Genera las 2 portadas RRSS principales del proyecto TWIM con copy editorial
actualizado (regla inviolable "claridad de un vistazo en copy público").

- portada-rrss-directo-la-voz-que-te-juzga.png · sistema A1 verde
- portada-rrss-reto-7-dias-deja-de-buscarte.png · sistema A2 crema

Dimensiones · 1080x1080 (cuadrado RRSS estándar). Paleta TWIM exacta.
Fuentes · Instrument Serif (titulares) + Barlow Condensed (texto/captions).
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1080

# ---- Paleta TWIM ----
GREEN_DARK = (23, 61, 48)      # #173D30
GREEN      = (38, 92, 75)      # #265C4B
BEIGE      = (194, 167, 139)   # #C2A78B
CREAM      = (245, 239, 227)   # crema suave (fondo del Reto)
WHITE      = (253, 252, 250)   # #FDFCFA

# ---- Fuentes ----
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


# ===== 1 · PORTADA DIRECTO (sistema A1 verde) =====
canvas = Image.new('RGB', (W, H), GREEN_DARK)
draw = ImageDraw.Draw(canvas)
draw.rectangle([(40, 40), (W-40, H-40)], outline=BEIGE, width=2)

draw_centered(draw, 'TE ESCRIBO · DIRECTO', 178,
              font('BarlowCondensed-Medium.ttf', 28), BEIGE, letter_spacing=4)
hline(draw, 240, BEIGE)

# Título · "La voz que" / "te juzga"
draw_centered(draw, 'La voz que', 320,
              font('InstrumentSerif-Regular.ttf', 130), WHITE)
draw_centered(draw, 'te juzga', 470,
              font('InstrumentSerif-Regular.ttf', 130), WHITE)

# Subtítulo italic (FRASE NUEVA pulida por Daniel · «pone un pero»)
draw_centered(draw, 'La voz interior que siempre te pone un pero.', 670,
              font('InstrumentSerif-Italic.ttf', 38), BEIGE)

# Fecha
draw_centered(draw, 'Domingo 8 de junio · 19:00 (España)', 780,
              font('BarlowCondensed-Medium.ttf', 36), WHITE)

# Caption
draw_centered(draw, 'EN DIRECTO · GRATUITO · CON REGISTRO', 840,
              font('BarlowCondensed-Medium.ttf', 26), BEIGE, letter_spacing=4)

hline(draw, 920, BEIGE)
draw_centered(draw, '@daniorozcopsicologo · twimproject.com', 960,
              font('BarlowCondensed-Regular.ttf', 20), WHITE, letter_spacing=2)

canvas.save('portada-rrss-directo-la-voz-que-te-juzga.png', optimize=True)
print('OK · portada-rrss-directo-la-voz-que-te-juzga.png')


# ===== 2 · PORTADA RETO (sistema A2 crema) =====
canvas = Image.new('RGB', (W, H), CREAM)
draw = ImageDraw.Draw(canvas)
draw.rectangle([(40, 40), (W-40, H-40)], outline=BEIGE, width=2)

draw_centered(draw, 'TWIM PROJECT · RETO GRATUITO', 178,
              font('BarlowCondensed-Medium.ttf', 28), GREEN_DARK, letter_spacing=4)
hline(draw, 240, BEIGE)

draw_centered(draw, 'Deja de buscarte', 330,
              font('InstrumentSerif-Regular.ttf', 110), GREEN_DARK)
draw_centered(draw, 'en otros', 470,
              font('InstrumentSerif-Regular.ttf', 110), GREEN_DARK)

# Subtítulo italic (FRASE NUEVA opción B · imagen mental concreta)
draw_centered(draw, 'Por qué escaneas su cara cuando llegas a casa.', 660,
              font('InstrumentSerif-Italic.ttf', 38), BEIGE)

draw_centered(draw, 'Reto de 7 días · observación guiada', 770,
              font('BarlowCondensed-Medium.ttf', 32), GREEN_DARK)
draw_centered(draw, 'GRATIS · POR EMAIL', 830,
              font('BarlowCondensed-Medium.ttf', 26), BEIGE, letter_spacing=4)

hline(draw, 920, BEIGE)
draw_centered(draw, '@daniorozcopsicologo · twimproject.com', 960,
              font('BarlowCondensed-Regular.ttf', 20), GREEN_DARK, letter_spacing=2)

canvas.save('portada-rrss-reto-7-dias-deja-de-buscarte.png', optimize=True)
print('OK · portada-rrss-reto-7-dias-deja-de-buscarte.png')
