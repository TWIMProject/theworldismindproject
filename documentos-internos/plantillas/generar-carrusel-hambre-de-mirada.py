#!/usr/bin/env python3
"""
Genera el Carrusel #4 IG «3 escenas de hambre de mirada» · 8 slides 1080×1080.

Derivado de la Carta #3 «Hambre de mirada» pero con título y enfoque distinto
para no canibalizar la newsletter (regla del plan-captacion-verano-2026.md S21
· carrusel A REDES, carta A NEWSLETTER, dos ángulos del mismo mecanismo).

Sistema visual A1 verde · paleta TWIM exacta · Instrument Serif (titulares)
+ Barlow Condensed (texto). Coherente con generar-portadas-rrss.py.

Outputs en carrusel-hambre-de-mirada/ (raíz del repo)
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1080
OUT = '/home/user/theworldismindproject/carrusel-hambre-de-mirada'
os.makedirs(OUT, exist_ok=True)

GREEN_DARK = (23, 61, 48)
BEIGE      = (194, 167, 139)
CREAM      = (245, 239, 227)
WHITE      = (253, 252, 250)

FONT_DIR = '/root/.fonts'
def font(name, size): return ImageFont.truetype(f'{FONT_DIR}/{name}', size)

def centered(draw, text, y, f, color, ls=0):
    if ls == 0:
        bbox = draw.textbbox((0, 0), text, font=f)
        draw.text(((W - (bbox[2] - bbox[0])) // 2, y), text, fill=color, font=f)
    else:
        total = sum(draw.textbbox((0, 0), ch, font=f)[2] + ls for ch in text) - ls
        x = (W - total) // 2
        for ch in text:
            draw.text((x, y), ch, fill=color, font=f)
            x += draw.textbbox((0, 0), ch, font=f)[2] + ls

def hline(draw, y, color, w=2, half=60):
    cx = W // 2
    draw.line([(cx - half, y), (cx + half, y)], fill=color, width=w)

def base():
    c = Image.new('RGB', (W, H), GREEN_DARK)
    d = ImageDraw.Draw(c)
    d.rectangle([(40, 40), (W - 40, H - 40)], outline=BEIGE, width=2)
    return c, d

def header(d, txt='TWIM PROJECT · CARRUSEL'):
    centered(d, txt, 110, font('BarlowCondensed-Medium.ttf', 26), BEIGE, ls=4)
    hline(d, 165, BEIGE)

def footer(d, idx, total=8):
    hline(d, H - 130, BEIGE)
    label = f'{idx} / {total}  ·  DESLIZA' if idx < total else f'{idx} / {total}'
    centered(d, label, H - 105, font('BarlowCondensed-Medium.ttf', 24), BEIGE, ls=3)
    centered(d, '@daniorozcopsicologo · twimproject.com', H - 65,
             font('BarlowCondensed-Regular.ttf', 19), WHITE, ls=2)


# SLIDE 1 · HOOK
c, d = base()
header(d, 'TWIM PROJECT · CARRUSEL')
centered(d, '3 escenas', 270, font('InstrumentSerif-Regular.ttf', 130), WHITE)
centered(d, 'de hambre', 410, font('InstrumentSerif-Regular.ttf', 130), WHITE)
centered(d, 'de mirada.', 550, font('InstrumentSerif-Regular.ttf', 130), WHITE)
centered(d, 'No las habrás nombrado · pero pasan a diario.', 760,
         font('InstrumentSerif-Italic.ttf', 38), BEIGE)
footer(d, 1)
c.save(f'{OUT}/slide-1-hook.png', optimize=True)
print('OK · slide 1')

# SLIDE 2 · ESCENA 1
c, d = base()
header(d, 'ESCENA 1 · EL MENSAJE')
centered(d, 'Relees', 270, font('InstrumentSerif-Regular.ttf', 130), WHITE)
centered(d, 'el mensaje', 410, font('InstrumentSerif-Regular.ttf', 130), WHITE)
centered(d, 'tres veces', 550, font('InstrumentSerif-Regular.ttf', 130), WHITE)
centered(d, 'antes de enviarlo.', 700, font('InstrumentSerif-Italic.ttf', 56), BEIGE)
centered(d, 'Por si suena raro · por si le sienta mal.', 800,
         font('BarlowCondensed-Medium.ttf', 30), CREAM)
footer(d, 2)
c.save(f'{OUT}/slide-2-mensaje.png', optimize=True)
print('OK · slide 2')

# SLIDE 3 · ESCENA 2
c, d = base()
header(d, 'ESCENA 2 · LA CARA EN CASA')
centered(d, 'Escaneas', 270, font('InstrumentSerif-Regular.ttf', 130), WHITE)
centered(d, 'su cara', 410, font('InstrumentSerif-Regular.ttf', 130), WHITE)
centered(d, 'al entrar.', 550, font('InstrumentSerif-Regular.ttf', 130), WHITE)
centered(d, 'En medio segundo · ¿ha pasado algo?', 720,
         font('InstrumentSerif-Italic.ttf', 42), BEIGE)
centered(d, 'Sin haber preguntado · ya estás respondiendo.', 800,
         font('BarlowCondensed-Medium.ttf', 28), CREAM)
footer(d, 3)
c.save(f'{OUT}/slide-3-cara.png', optimize=True)
print('OK · slide 3')

# SLIDE 4 · ESCENA 3
c, d = base()
header(d, 'ESCENA 3 · EL PERDÓN')
centered(d, 'Pides', 270, font('InstrumentSerif-Regular.ttf', 130), WHITE)
centered(d, 'perdón', 410, font('InstrumentSerif-Regular.ttf', 130), WHITE)
centered(d, 'sin haber', 550, font('InstrumentSerif-Regular.ttf', 130), WHITE)
centered(d, 'hecho nada.', 700, font('InstrumentSerif-Italic.ttf', 70), BEIGE)
centered(d, 'Por adelantarte · por si acaso.', 800,
         font('BarlowCondensed-Medium.ttf', 30), CREAM)
footer(d, 4)
c.save(f'{OUT}/slide-4-perdon.png', optimize=True)
print('OK · slide 4')

# SLIDE 5 · POR QUÉ
c, d = base()
header(d, 'POR QUÉ PASA')
centered(d, 'No es', 250, font('InstrumentSerif-Regular.ttf', 130), WHITE)
centered(d, 'inseguridad.', 390, font('InstrumentSerif-Regular.ttf', 130), WHITE)
centered(d, 'Es un mecanismo', 530, font('InstrumentSerif-Regular.ttf', 70), CREAM)
centered(d, 'que se montó cuando eras niña ·', 615,
         font('InstrumentSerif-Italic.ttf', 38), BEIGE)
centered(d, 'la mirada del adulto era recurso escaso ·', 670,
         font('InstrumentSerif-Italic.ttf', 38), BEIGE)
centered(d, 'aprendiste a hacer lo necesario para no perderla.', 725,
         font('InstrumentSerif-Italic.ttf', 38), BEIGE)
centered(d, 'Hoy sigue funcionando solo.', 810,
         font('BarlowCondensed-Medium.ttf', 30), CREAM)
footer(d, 5)
c.save(f'{OUT}/slide-5-por-que.png', optimize=True)
print('OK · slide 5')

# SLIDE 6 · QUÉ HACER
c, d = base()
header(d, 'UN GESTO PEQUEÑO')
centered(d, 'Esta semana,', 270, font('InstrumentSerif-Regular.ttf', 90), WHITE)
centered(d, 'cuando releas', 380, font('InstrumentSerif-Regular.ttf', 90), WHITE)
centered(d, 'el mensaje varias veces,', 490, font('InstrumentSerif-Regular.ttf', 70), WHITE)
centered(d, 'envíalo como salió a la primera.', 600,
         font('InstrumentSerif-Italic.ttf', 50), BEIGE)
centered(d, 'Y observa qué sientes', 720,
         font('BarlowCondensed-Medium.ttf', 32), CREAM)
centered(d, 'en los siguientes veinte minutos.', 770,
         font('BarlowCondensed-Medium.ttf', 32), CREAM)
centered(d, 'Sin tarea · sin cuaderno. Solo observar.', 830,
         font('InstrumentSerif-Italic.ttf', 30), BEIGE)
footer(d, 6)
c.save(f'{OUT}/slide-6-gesto.png', optimize=True)
print('OK · slide 6')

# SLIDE 7 · LISTA ESPERA VOLVER A MÍ
c, d = base()
header(d, 'EN GRUPO · OTOÑO 2026')
centered(d, 'Volver', 250, font('InstrumentSerif-Regular.ttf', 130), WHITE)
centered(d, 'a Mí.', 390, font('InstrumentSerif-Regular.ttf', 130), WHITE)
centered(d, 'Grupo cerrado de 8 mujeres · 8 miércoles.', 580,
         font('InstrumentSerif-Italic.ttf', 38), BEIGE)
centered(d, '30 sept a 18 nov 2026 · online', 640,
         font('BarlowCondensed-Medium.ttf', 30), CREAM)
centered(d, 'Apúntate a la lista de espera · sin pago, sin compromiso', 750,
         font('BarlowCondensed-Medium.ttf', 28), WHITE)
centered(d, 'twimproject.com/talleres/volver-a-mi/', 800,
         font('BarlowCondensed-Regular.ttf', 24), BEIGE)
footer(d, 7)
c.save(f'{OUT}/slide-7-volver-a-mi.png', optimize=True)
print('OK · slide 7')

# SLIDE 8 · CTA NEWSLETTER TE ESCRIBO
c, d = base()
header(d, 'SI NO PUEDES EL TALLER')
centered(d, 'Te escribo.', 290, font('InstrumentSerif-Regular.ttf', 130), WHITE)
centered(d, 'Cartas sobre la mente, el cansancio', 480,
         font('InstrumentSerif-Italic.ttf', 40), BEIGE)
centered(d, 'y lo que no se dice.', 540,
         font('InstrumentSerif-Italic.ttf', 40), BEIGE)
centered(d, 'Cuando hay algo que merezca tu tiempo.', 660,
         font('BarlowCondensed-Medium.ttf', 30), CREAM)
centered(d, 'Sin spam · sin frecuencia obligada.', 710,
         font('BarlowCondensed-Medium.ttf', 30), CREAM)
centered(d, 'twimproject.com/newsletter/', 800,
         font('BarlowCondensed-Regular.ttf', 26), BEIGE)
footer(d, 8)
c.save(f'{OUT}/slide-8-newsletter.png', optimize=True)
print('OK · slide 8')

print('---')
print(f'Carrusel #4 · 8 slides generados en {OUT}')
