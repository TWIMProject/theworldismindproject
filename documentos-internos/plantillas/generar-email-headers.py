#!/usr/bin/env python3
"""
Genera el banner del email «Te escribo» optimizado para MailerLite y
cualquier cliente de email moderno · ancho retina 1200px, ratio 4:1,
diseño basado en email-header-B-logo-masthead.png pero recalculado para
encajar exacto en el bloque de imagen estándar del editor (600px nominal).

Output: te-escribo-email-banner.png en la raíz del repo.
URL pública resultante tras deploy: https://twimproject.com/te-escribo-email-banner.png
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 300

# Paleta TWIM
GREEN_DARK = (23, 61, 48)      # #173D30
BEIGE      = (194, 167, 139)   # #C2A78B
CREAM      = (245, 239, 227)
WHITE      = (253, 252, 250)   # #FDFCFA

FONT_DIR = '/root/.fonts'
def font(name, size): return ImageFont.truetype(f'{FONT_DIR}/{name}', size)

canvas = Image.new('RGB', (W, H), GREEN_DARK)
draw = ImageDraw.Draw(canvas)

# ---- Logo MIND/WORLD a la izquierda ----
logo = Image.open('/home/user/theworldismindproject/logo-mindworld.png').convert('RGBA')
logo_target_h = 150
logo_target_w = int(logo.width * logo_target_h / logo.height)
logo = logo.resize((logo_target_w, logo_target_h), Image.LANCZOS)
logo_x = 110
logo_y = (H - logo_target_h) // 2
canvas.paste(logo, (logo_x, logo_y), logo)

# ---- Separador vertical fino beige ----
sep_x = logo_x + logo_target_w + 50
draw.line([(sep_x, 75), (sep_x, H - 75)], fill=BEIGE, width=2)

# ---- Bloque tipográfico "Te escribo" + descriptor ----
text_x = sep_x + 60

# Te escribo · Instrument Serif Regular grande
title_font = font('InstrumentSerif-Regular.ttf', 96)
draw.text((text_x, 95), 'Te escribo', fill=CREAM, font=title_font)

# Descriptor pequeño Barlow Condensed con tracking amplio
desc_font = font('BarlowCondensed-Medium.ttf', 24)
descriptor = 'TWIM PROJECT · NEWSLETTER'
# Letter spacing manual
x_cursor = text_x + 4
y_desc = 200
letter_spacing = 4
for ch in descriptor:
    draw.text((x_cursor, y_desc), ch, fill=BEIGE, font=desc_font)
    bbox = draw.textbbox((0, 0), ch, font=desc_font)
    x_cursor += bbox[2] + letter_spacing

canvas.save('/home/user/theworldismindproject/te-escribo-email-banner.png',
            optimize=True)
print('OK · te-escribo-email-banner.png (1200x300, ratio 4:1, retina-ready)')
