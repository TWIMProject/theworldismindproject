#!/usr/bin/env python3
"""
Genera el Carrusel #4 IG «3 escenas de hambre de mirada» · 8 slides 1080×1350.

VERSIÓN A2 CREMA + FOTO IA (slide 1) · reemplaza la versión A1 verde 1080×1080
previa (decisión Daniel · 26 may 2026 tras métricas del Carrusel #3 a 7 d).
Razón · romper expectativa del algoritmo (94,3 % seguidores en el #3 indica
distribución cerrada, hipótesis B dominante en el doc de métricas).

Sistema visual A2 crema (`documentos-internos/instagram-sistema-visual-marca.md`
§3.4 · plantilla A2): fondo crema #FDFCFA, texto verde oscuro #173D30,
kicker verde medio #265C4B. Italics aforísticas en beige #C2A78B.

Formato 1080×1350 (4:5) · spec correcto del sistema visual (no 1080×1080
del intento previo, que era cuadrado).

Foto IA generada externamente por Daniel (DALL-E / ChatGPT image). Pega
el archivo en carrusel-hambre-de-mirada/foto-hook.jpg (o .png) y vuelve
a ejecutar el script · slide 1 la incorpora. Si no existe, se dibuja un
placeholder gris claro.

Prompt DALL-E sugerido en carrusel-hambre-de-mirada/README.md.

Outputs en carrusel-hambre-de-mirada/ (raíz del repo)
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1350
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'carrusel-hambre-de-mirada')
os.makedirs(OUT, exist_ok=True)

# Paleta A2 (sistema visual §3.4) · texto sobre crema
BG_CREAM     = (253, 252, 250)
TEXT_DARK    = (23, 61, 48)
KICKER_GREEN = (38, 92, 75)
BEIGE        = (194, 167, 139)
PLACEHOLDER  = (228, 222, 210)

FONT_DIRS = [
    os.environ.get('TWIM_FONTS', ''),
    '/tmp/fonts',
    '/root/.fonts',
    os.path.expanduser('~/.fonts'),
    '/mnt/skills/examples/canvas-design/canvas-fonts',
]

def font_path(name):
    for d in FONT_DIRS:
        if d:
            p = os.path.join(d, name)
            if os.path.exists(p):
                return p
    raise FileNotFoundError(f'fuente {name} no encontrada en {FONT_DIRS}')

def font(name, size):
    return ImageFont.truetype(font_path(name), size)

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
    c = Image.new('RGB', (W, H), BG_CREAM)
    d = ImageDraw.Draw(c)
    d.rectangle([(40, 40), (W - 40, H - 40)], outline=BEIGE, width=2)
    return c, d

def header(d, txt='TWIM PROJECT · CARRUSEL'):
    centered(d, txt, 110, font('BarlowCondensed-Medium.ttf', 26), KICKER_GREEN, ls=4)
    hline(d, 165, BEIGE)

def footer(d, idx, total=8):
    hline(d, H - 130, BEIGE)
    label = f'{idx} / {total}  ·  DESLIZA' if idx < total else f'{idx} / {total}'
    centered(d, label, H - 105, font('BarlowCondensed-Medium.ttf', 24), KICKER_GREEN, ls=3)
    centered(d, '@daniorozcopsicologo · twimproject.com', H - 65,
             font('BarlowCondensed-Regular.ttf', 19), TEXT_DARK, ls=2)

# ─────────────────────────────────────────────────────────────────
# SLIDE 1 · HOOK con FOTO IA + tipografía
# ─────────────────────────────────────────────────────────────────
c = Image.new('RGB', (W, H), BG_CREAM)
d = ImageDraw.Draw(c)

# Zona de foto: 1080×700 desde y=0 a y=700
FOTO_BOX = (0, 0, W, 720)
foto_paths = [
    os.path.join(OUT, 'foto-hook.jpg'),
    os.path.join(OUT, 'foto-hook.jpeg'),
    os.path.join(OUT, 'foto-hook.png'),
    os.path.join(OUT, 'foto-hook.webp'),
]
foto_path = next((p for p in foto_paths if os.path.exists(p)), None)

if foto_path:
    foto = Image.open(foto_path).convert('RGB')
    # Recorte tipo cover · mantener proporción y centrar
    target_w, target_h = W, 720
    src_ratio = foto.width / foto.height
    tgt_ratio = target_w / target_h
    if src_ratio > tgt_ratio:
        new_h = target_h
        new_w = int(new_h * src_ratio)
    else:
        new_w = target_w
        new_h = int(new_w / src_ratio)
    foto = foto.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    foto = foto.crop((left, top, left + target_w, top + target_h))
    c.paste(foto, (0, 0))
    print(f'OK · foto IA cargada desde {os.path.basename(foto_path)}')
else:
    # Placeholder: gradiente cálido apagado
    placeholder = Image.new('RGB', (W, 720), PLACEHOLDER)
    pdraw = ImageDraw.Draw(placeholder)
    pdraw.text((W // 2 - 220, 320), '[ foto IA · slide 1 ]',
               fill=TEXT_DARK, font=font('BarlowCondensed-Medium.ttf', 32))
    pdraw.text((W // 2 - 280, 365), 'ver README.md para prompt DALL-E',
               fill=KICKER_GREEN, font=font('BarlowCondensed-Regular.ttf', 22))
    c.paste(placeholder, (0, 0))
    print('OK · placeholder (foto IA pendiente)')

# Banda separadora sutil entre foto y zona tipográfica
d.rectangle([(0, 720), (W, 723)], fill=BEIGE)

# Kicker sobre crema
centered(d, 'TWIM PROJECT · CARRUSEL', 770,
         font('BarlowCondensed-Medium.ttf', 26), KICKER_GREEN, ls=4)
hline(d, 815, BEIGE)

# Título principal · 3 líneas en Instrument Serif
centered(d, '3 escenas', 860, font('InstrumentSerif-Regular.ttf', 110), TEXT_DARK)
centered(d, 'de hambre', 980, font('InstrumentSerif-Regular.ttf', 110), TEXT_DARK)
centered(d, 'de mirada.', 1100, font('InstrumentSerif-Regular.ttf', 110), TEXT_DARK)

# Cierre aforístico italic beige
centered(d, 'No las habrás nombrado · pero pasan a diario.', 1245,
         font('InstrumentSerif-Italic.ttf', 36), BEIGE)

# Footer minimal (sin paginación, slide 1 es portada)
centered(d, '01 / 08  ·  DESLIZA', 1295,
         font('BarlowCondensed-Medium.ttf', 22), KICKER_GREEN, ls=3)
c.save(f'{OUT}/slide-1-hook.png', optimize=True)
print('OK · slide 1')

# ─────────────────────────────────────────────────────────────────
# SLIDE 2 · ESCENA 1 · EL MENSAJE
# ─────────────────────────────────────────────────────────────────
c, d = base()
header(d, 'ESCENA 1 · EL MENSAJE')
centered(d, 'Relees',     360, font('InstrumentSerif-Regular.ttf', 130), TEXT_DARK)
centered(d, 'el mensaje', 500, font('InstrumentSerif-Regular.ttf', 130), TEXT_DARK)
centered(d, 'tres veces', 640, font('InstrumentSerif-Regular.ttf', 130), TEXT_DARK)
centered(d, 'antes de enviarlo.', 820,
         font('InstrumentSerif-Italic.ttf', 56), BEIGE)
centered(d, 'Por si suena raro · por si le sienta mal.', 930,
         font('BarlowCondensed-Medium.ttf', 32), KICKER_GREEN)
footer(d, 2)
c.save(f'{OUT}/slide-2-mensaje.png', optimize=True)
print('OK · slide 2')

# ─────────────────────────────────────────────────────────────────
# SLIDE 3 · ESCENA 2 · LA CARA EN CASA
# ─────────────────────────────────────────────────────────────────
c, d = base()
header(d, 'ESCENA 2 · LA CARA EN CASA')
centered(d, 'Escaneas',   360, font('InstrumentSerif-Regular.ttf', 130), TEXT_DARK)
centered(d, 'su cara',    500, font('InstrumentSerif-Regular.ttf', 130), TEXT_DARK)
centered(d, 'al entrar.', 640, font('InstrumentSerif-Regular.ttf', 130), TEXT_DARK)
centered(d, 'En medio segundo · ¿ha pasado algo?', 830,
         font('InstrumentSerif-Italic.ttf', 42), BEIGE)
centered(d, 'Sin haber preguntado · ya estás respondiendo.', 920,
         font('BarlowCondensed-Medium.ttf', 30), KICKER_GREEN)
footer(d, 3)
c.save(f'{OUT}/slide-3-cara.png', optimize=True)
print('OK · slide 3')

# ─────────────────────────────────────────────────────────────────
# SLIDE 4 · ESCENA 3 · EL PERDÓN
# ─────────────────────────────────────────────────────────────────
c, d = base()
header(d, 'ESCENA 3 · EL PERDÓN')
centered(d, 'Pides',        360, font('InstrumentSerif-Regular.ttf', 130), TEXT_DARK)
centered(d, 'perdón',       500, font('InstrumentSerif-Regular.ttf', 130), TEXT_DARK)
centered(d, 'sin haber',    640, font('InstrumentSerif-Regular.ttf', 130), TEXT_DARK)
centered(d, 'hecho nada.',  820, font('InstrumentSerif-Italic.ttf', 70), BEIGE)
centered(d, 'Por adelantarte · por si acaso.', 940,
         font('BarlowCondensed-Medium.ttf', 32), KICKER_GREEN)
footer(d, 4)
c.save(f'{OUT}/slide-4-perdon.png', optimize=True)
print('OK · slide 4')

# ─────────────────────────────────────────────────────────────────
# SLIDE 5 · POR QUÉ
# ─────────────────────────────────────────────────────────────────
c, d = base()
header(d, 'POR QUÉ PASA')
centered(d, 'No es',       340, font('InstrumentSerif-Regular.ttf', 130), TEXT_DARK)
centered(d, 'inseguridad.', 480, font('InstrumentSerif-Regular.ttf', 130), TEXT_DARK)
centered(d, 'Es un mecanismo', 640,
         font('InstrumentSerif-Regular.ttf', 70), KICKER_GREEN)
centered(d, 'que se montó cuando eras niña ·', 760,
         font('InstrumentSerif-Italic.ttf', 38), BEIGE)
centered(d, 'la mirada del adulto era recurso escaso ·', 815,
         font('InstrumentSerif-Italic.ttf', 38), BEIGE)
centered(d, 'aprendiste a hacer lo necesario para no perderla.', 870,
         font('InstrumentSerif-Italic.ttf', 38), BEIGE)
centered(d, 'Hoy sigue funcionando solo.', 990,
         font('BarlowCondensed-Medium.ttf', 32), KICKER_GREEN)
footer(d, 5)
c.save(f'{OUT}/slide-5-por-que.png', optimize=True)
print('OK · slide 5')

# ─────────────────────────────────────────────────────────────────
# SLIDE 6 · UN GESTO PEQUEÑO
# ─────────────────────────────────────────────────────────────────
c, d = base()
header(d, 'UN GESTO PEQUEÑO')
centered(d, 'Esta semana,',           360, font('InstrumentSerif-Regular.ttf', 90), TEXT_DARK)
centered(d, 'cuando releas',          470, font('InstrumentSerif-Regular.ttf', 90), TEXT_DARK)
centered(d, 'el mensaje varias veces,', 580,
         font('InstrumentSerif-Regular.ttf', 70), TEXT_DARK)
centered(d, 'envíalo como salió a la primera.', 720,
         font('InstrumentSerif-Italic.ttf', 50), BEIGE)
centered(d, 'Y observa qué sientes', 870,
         font('BarlowCondensed-Medium.ttf', 32), KICKER_GREEN)
centered(d, 'en los siguientes veinte minutos.', 920,
         font('BarlowCondensed-Medium.ttf', 32), KICKER_GREEN)
centered(d, 'Sin tarea · sin cuaderno. Solo observar.', 990,
         font('InstrumentSerif-Italic.ttf', 30), BEIGE)
footer(d, 6)
c.save(f'{OUT}/slide-6-gesto.png', optimize=True)
print('OK · slide 6')

# ─────────────────────────────────────────────────────────────────
# SLIDE 7 · LISTA DE ESPERA VOLVER A MÍ
# ─────────────────────────────────────────────────────────────────
c, d = base()
header(d, 'EN GRUPO · OTOÑO 2026')
centered(d, 'Volver',  340, font('InstrumentSerif-Regular.ttf', 130), TEXT_DARK)
centered(d, 'a Mí.',   480, font('InstrumentSerif-Regular.ttf', 130), TEXT_DARK)
centered(d, 'Grupo cerrado de 8 mujeres · 8 miércoles.', 700,
         font('InstrumentSerif-Italic.ttf', 38), BEIGE)
centered(d, '30 sept a 18 nov 2026 · online', 760,
         font('BarlowCondensed-Medium.ttf', 30), KICKER_GREEN)
centered(d, 'Apúntate a la lista de espera · sin pago, sin compromiso', 880,
         font('BarlowCondensed-Medium.ttf', 28), TEXT_DARK)
centered(d, 'twimproject.com/talleres/volver-a-mi/', 930,
         font('BarlowCondensed-Regular.ttf', 24), BEIGE)
footer(d, 7)
c.save(f'{OUT}/slide-7-volver-a-mi.png', optimize=True)
print('OK · slide 7')

# ─────────────────────────────────────────────────────────────────
# SLIDE 8 · CTA NEWSLETTER TE ESCRIBO
# ─────────────────────────────────────────────────────────────────
c, d = base()
header(d, 'SI NO PUEDES EL TALLER')
centered(d, 'Te escribo.', 380, font('InstrumentSerif-Regular.ttf', 130), TEXT_DARK)
centered(d, 'Cartas sobre la mente, el cansancio', 600,
         font('InstrumentSerif-Italic.ttf', 40), BEIGE)
centered(d, 'y lo que no se dice.', 660,
         font('InstrumentSerif-Italic.ttf', 40), BEIGE)
centered(d, 'Cuando hay algo que merezca tu tiempo.', 820,
         font('BarlowCondensed-Medium.ttf', 30), KICKER_GREEN)
centered(d, 'Sin spam · sin frecuencia obligada.', 870,
         font('BarlowCondensed-Medium.ttf', 30), KICKER_GREEN)
centered(d, 'twimproject.com/newsletter/', 980,
         font('BarlowCondensed-Regular.ttf', 26), BEIGE)
footer(d, 8)
c.save(f'{OUT}/slide-8-newsletter.png', optimize=True)
print('OK · slide 8')

print('---')
print(f'Carrusel #4 A2 crema · 8 slides 1080×1350 generados en {OUT}')
print(f'Foto IA: {"detectada y aplicada" if foto_path else "PENDIENTE (placeholder en slide 1)"}')
