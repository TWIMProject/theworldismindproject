#!/usr/bin/env python3
"""
Genera el banner header para emails «Te escribo» con logo TWIM + kicker
de la serie a la que pertenezca el email.

Formato email standard: 600px ancho · alto proporcional (~150px).
Fondo verde TWIM oscuro. Logo crema sobre verde. Kicker en beige.

Outputs en assets/email-headers/
- te-escribo-volver-a-mi.png
- te-escribo-directo.png
- te-escribo.png (generico)
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = '/home/user/theworldismindproject/assets/email-headers'
os.makedirs(OUT, exist_ok=True)

W, H = 1200, 280  # @2x para retina · MailerLite lo escala a 600×140

GREEN_DARK = (23, 61, 48)
BEIGE      = (194, 167, 139)
CREAM      = (245, 239, 227)
WHITE      = (253, 252, 250)

FONT_DIR = '/root/.fonts'
def font(name, size): return ImageFont.truetype(f'{FONT_DIR}/{name}', size)

LOGO = Image.open('/home/user/theworldismindproject/assets/logo-mindworld-on-dark.png').convert('RGBA')


def make_header(kicker_text, out_filename):
    c = Image.new('RGB', (W, H), GREEN_DARK)
    d = ImageDraw.Draw(c)

    # Logo a la izquierda · proporcional
    logo_h = 160
    ratio = LOGO.size[0] / LOGO.size[1]
    logo_w = int(logo_h * ratio)
    logo = LOGO.resize((logo_w, logo_h), Image.LANCZOS)
    logo_x = 90
    logo_y = (H - logo_h) // 2
    c.paste(logo, (logo_x, logo_y), logo)

    # Separador vertical sutil entre logo y kicker
    sep_x = logo_x + logo_w + 50
    d.line([(sep_x, H // 2 - 50), (sep_x, H // 2 + 50)], fill=BEIGE, width=2)

    # Kicker a la derecha del logo (con tracking)
    kicker_x = sep_x + 40
    kicker_y = H // 2
    f_kicker = font('BarlowCondensed-Medium.ttf', 38)
    ls = 5

    # calcular ancho con letter-spacing para centrar verticalmente
    bbox = d.textbbox((0, 0), kicker_text, font=f_kicker)
    text_h = bbox[3] - bbox[1]
    ty = kicker_y - text_h // 2 - 4
    x = kicker_x
    for ch in kicker_text:
        d.text((x, ty), ch, fill=BEIGE, font=f_kicker)
        x += d.textbbox((0, 0), ch, font=f_kicker)[2] + ls

    c.save(f'{OUT}/{out_filename}', optimize=True)
    print(f'OK · {out_filename}')


make_header('TE ESCRIBO  ·  VOLVER A MÍ', 'te-escribo-volver-a-mi.png')
make_header('TE ESCRIBO  ·  DIRECTO',     'te-escribo-directo.png')
make_header('TE ESCRIBO',                 'te-escribo.png')

print('---')
print(f'3 headers generados en {OUT}')
