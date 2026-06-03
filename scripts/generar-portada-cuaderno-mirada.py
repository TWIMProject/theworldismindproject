#!/usr/bin/env python3
"""
Portada de venta del cuaderno «La mirada del otro».

Pedida por Daniel el 3 jun 2026: la primera versión (render de la página 1 del PDF)
salía "pálida" y vacía. Esta es una portada de venta, premium y con gancho, que hace
PAREJA con la del libro digital (misma familia TWIM, contraste de color):

  - Fondo verde TWIM profundo (no pálido), marco doble beige.
  - Motivo line-art de un OJO (el tema literal: "la mirada del otro"), en beige.
  - Tipografía de marca (Instrument Serif), título en crema.
  - Logo MIND WORLD recoloreado a crema + autor y colegiado.

Salida: portada-cuaderno-la-mirada.jpg (raíz, asset público de marketing).
Reproducir: python3 scripts/generar-portada-cuaderno-mirada.py
"""
import math, os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "portada-cuaderno-la-mirada.jpg"

FONT_DIR = Path(os.environ.get("TWIM_FONTS_DIR", "/mnt/skills/examples/canvas-design/canvas-fonts")).expanduser()
FR = str(FONT_DIR / "InstrumentSerif-Regular.ttf")
FI = str(FONT_DIR / "InstrumentSerif-Italic.ttf")

GREEN = (23, 61, 48)      # #173D30 fondo
GREEN2 = (38, 92, 75)     # #265C4B
CREAM = (253, 252, 250)   # #FDFCFA
BEIGE = (194, 167, 139)   # #C2A78B
BEIGE_S = (167, 142, 116) # beige más apagado

W, H = 1000, 1500
img = Image.new("RGB", (W, H), GREEN)
d = ImageDraw.Draw(img)

# Marco doble editorial (beige sobre verde)
d.rectangle([38, 38, W - 38, H - 38], outline=BEIGE, width=4)
d.rectangle([52, 52, W - 52, H - 52], outline=GREEN2, width=2)

def ctext(y, txt, f, col):
    w = d.textlength(txt, font=f)
    d.text(((W - w) // 2, y), txt, font=f, fill=col)

def spaced(txt, n=1):
    return (" " * n).join(list(txt))

# Eyebrow
ctext(150, spaced("CUADERNO PARA ESCRIBIR", 1), ImageFont.truetype(FR, 30), BEIGE)

# Título
ctext(212, "La mirada", ImageFont.truetype(FR, 104), CREAM)
ctext(322, "del otro", ImageFont.truetype(FR, 104), CREAM)

# Filete
d.line([(W * 0.34, 470), (W * 0.66, 470)], fill=BEIGE, width=2)

# Subtítulo (italic)
ctext(498, "Dejar de necesitar que te validen", ImageFont.truetype(FI, 34), BEIGE)
ctext(544, "para sentir que vales.", ImageFont.truetype(FI, 34), BEIGE)

# --- Motivo: un OJO en line-art (la mirada) ---
cx, cy = W // 2, 880
aw, ah_up, ah_lo = 200, 116, 104

def lid(ah, sign, steps=120):
    pts = []
    for i in range(steps + 1):
        x = cx - aw + (2 * aw) * i / steps
        t = (x - cx) / aw
        y = cy + sign * ah * (1 - t * t)
        pts.append((x, y))
    return pts

d.line(lid(ah_up, -1), fill=BEIGE, width=6, joint="curve")
d.line(lid(ah_lo, 1), fill=BEIGE, width=6, joint="curve")

# Iris + pupila + brillo
ir = 78
d.ellipse([cx - ir, cy - ir, cx + ir, cy + ir], outline=CREAM, width=6)
d.ellipse([cx - ir * 0.5, cy - ir * 0.5, cx + ir * 0.5, cy + ir * 0.5], fill=BEIGE)
pr = 26
d.ellipse([cx - pr, cy - pr, cx + pr, cy + pr], fill=CREAM)
d.ellipse([cx + 4, cy - 14, cx + 16, cy - 2], fill=GREEN)

# Pestañas / rayos de mirada (sutiles) sobre el párpado superior
for k in (-1.0, -0.6, -0.2, 0.2, 0.6, 1.0):
    bx = cx + aw * k * 0.62
    t = (bx - cx) / aw
    by = cy - ah_up * (1 - t * t)
    ang = math.atan2(-(-2 * ah_up * t / aw), 1) - math.pi / 2
    ex = bx + 34 * math.cos(math.radians(-90) + k * 0.5)
    ey = by - 34
    d.line([(bx, by), (ex, ey)], fill=BEIGE_S, width=4)

# Logo recoloreado a crema (el original es oscuro; no se vería sobre verde)
try:
    logo = Image.open(ROOT / "assets" / "logo-mindworld-transparent.png").convert("RGBA")
    lw = int(W * 0.20); lh = int(lw * logo.height / logo.width)
    logo = logo.resize((lw, lh))
    alpha = logo.split()[3]
    cream_layer = Image.new("RGBA", logo.size, CREAM + (255,))
    cream_layer.putalpha(alpha)
    ly = int(H * 0.79)
    img.paste(cream_layer, ((W - lw) // 2, ly), cream_layer)
    autor_y = ly + lh + 26
except Exception as e:
    print("logo skip:", e); autor_y = int(H * 0.84)

ctext(autor_y, "Daniel Orozco Abia", ImageFont.truetype(FR, 46), CREAM)
ctext(autor_y + 60, "Psicólogo General Sanitario · CV11515", ImageFont.truetype(FR, 26), BEIGE)

img.save(OUT, quality=93)
print("Portada cuaderno generada:", OUT, img.size)
