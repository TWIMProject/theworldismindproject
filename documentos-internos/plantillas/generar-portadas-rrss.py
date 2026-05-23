#!/usr/bin/env python3
"""
Genera las 3 portadas RRSS principales del proyecto TWIM con copy editorial
actualizado (regla inviolable "claridad de un vistazo en copy público").

- portada-rrss-directo-la-voz-que-te-juzga.png   · sistema A1 verde
- portada-rrss-reto-7-dias-deja-de-buscarte.png  · sistema A2 crema
- portada-rrss-libro-engranajes-mente.png        · pieza de venta del libro
  (aplica criterio dopamina-comercial · paleta TWIM verde · mockup real)

Dimensiones · 1080x1080 (cuadrado RRSS estándar). Paleta TWIM exacta.
Fuentes · Instrument Serif (titulares) + Barlow Condensed (texto/captions).
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

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


# ===== 3 · PORTADA LIBRO LOS ENGRANAJES DE LA MENTE (pieza de venta) =====
# Aplica criterio dopamina-comercial (documentos-internos/marca-twim-criterio-
# dopamina-comercial.md). Mantiene paleta TWIM como marca paraguas + mockup
# real del libro + hook adaptado al canal.
# CTA dual coherente con palancas-venta-libro-engranajes §3.1: Cap III gratis
# preferente + Amazon como segunda opción.
#
# Se generan 2 versiones · v1 X/IG (hook directo «cansado del coaching»)
# v2 LinkedIn (hook profesional sin atacar disciplina · evita choque con
# audiencia coaches/RRHH y no cierra puerta a in-company de /conferencias/).

def build_book_cover(hook_l1, hook_l2, subtitle, output_path):
    canvas = Image.new('RGB', (W, H), GREEN_DARK)
    draw = ImageDraw.Draw(canvas)
    draw.rectangle([(40, 40), (W-40, H-40)], outline=BEIGE, width=2)

    draw_centered(draw, 'TWIM PROJECT · LIBRO', 85,
                  font('BarlowCondensed-Medium.ttf', 24), BEIGE, letter_spacing=4)

    draw_centered(draw, hook_l1, 140,
                  font('InstrumentSerif-Regular.ttf', 56), WHITE)
    draw_centered(draw, hook_l2, 205,
                  font('InstrumentSerif-Italic.ttf', 56), BEIGE)

    draw_centered(draw, subtitle, 285,
                  font('InstrumentSerif-Italic.ttf', 28), CREAM)

    book = Image.open('portadalosengranajes.jpg').convert('RGBA')
    target_w = 300
    target_h = int(book.height * target_w / book.width)
    book = book.resize((target_w, target_h), Image.LANCZOS)

    shadow = Image.new('RGBA', (target_w + 60, target_h + 60), (0,0,0,0))
    sh_draw = ImageDraw.Draw(shadow)
    sh_draw.rectangle([(30, 30), (30 + target_w, 30 + target_h)], fill=(0, 0, 0, 140))
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=18))

    book_x = (W - target_w) // 2
    book_y = 330
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

    canvas.save(output_path, optimize=True)
    print(f'OK · {output_path}')


# v1 · para X / Instagram (hook directo, anti-motivación frontal)
build_book_cover(
    'Para quien ya está cansado',
    'del coaching.',
    'Lo que el «tú puedes» no te cuenta.',
    'portada-rrss-libro-engranajes-mente.png',
)

# v2 · para LinkedIn (hook profesional · evita atacar disciplina · mantiene
# diferenciación clínica sin cerrar puertas con coaches / RRHH · subtítulo
# pulido para descargar culpa y validar la lectura del lector culto)
build_book_cover(
    '¿Por qué entender',
    'no termina de cambiarte?',
    'No es motivación lo que te falta. Son los engranajes entre lo que ya ves.',
    'portada-rrss-libro-engranajes-mente-linkedin.png',
)
