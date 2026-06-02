#!/usr/bin/env python3
"""
Portada de la EDICIÓN DIGITAL TWIM de «Los engranajes de la mente».

Decidida el 2 jun 2026 (sesión claude/blissful-lovelace-VPbaj). Daniel descartó el
recoloreo de la portada de Amazon ("combinación horrenda") y pidió una de cero, más
marca TWIM, que hiciera familia con la contraportada elegida (`contraportadaretro.jpg`,
line-art sepia sobre crema). Resultado aprobado por Daniel ("así genial"):

  - Fondo crema muestreado de la contraportada (para que casen exactos).
  - Engranajes a trazo (dientes trapezoidales reales, no estrellas), sepia.
  - Tipografía de marca (Instrument Serif), título en verde TWIM.
  - Doble filete (marco) verde + sepia: estructura y rompe el plano beige.
  - Logo MIND WORLD PROJECT + autor y colegiado correctos (sin "Psicólogo Random").

Salida: documentos-internos/producto-engranajes-digital/portada-edicion-digital-twim.jpg
Reproducir: python3 scripts/generar-portada-engranajes-digital.py
"""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "documentos-internos" / "producto-engranajes-digital"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT = OUT_DIR / "portada-edicion-digital-twim.jpg"

FONT_DIR = Path("/mnt/skills/examples/canvas-design/canvas-fonts")
FR = str(FONT_DIR / "InstrumentSerif-Regular.ttf")
FI = str(FONT_DIR / "InstrumentSerif-Italic.ttf")

ref = Image.open(ROOT / "contraportadaretro.jpg").convert("RGB")
CREAM = ref.getpixel((15, 15))
SEPIA = (120, 92, 56); GREEN = (23, 61, 48); BEIGE = (150, 120, 80)

W, H = 1000, 1500
img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)

# marco doble editorial
d.rectangle([38, 38, W - 38, H - 38], outline=GREEN, width=4)
d.rectangle([52, 52, W - 52, H - 52], outline=SEPIA, width=2)

def gear(cx, cy, r_out, r_in, teeth, width, col):
    pts = []; step = 2 * math.pi / teeth
    frac = [(0.00, r_in), (0.28, r_in), (0.36, r_out), (0.64, r_out), (0.72, r_in)]
    for i in range(teeth):
        base = step * i
        for f, r in frac:
            a = base + step * f
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    pts.append(pts[0])
    d.line(pts, fill=col, width=width, joint="curve")
    d.ellipse([cx - r_in * 0.34, cy - r_in * 0.34, cx + r_in * 0.34, cy + r_in * 0.34],
              outline=col, width=width)

cx, cy = W // 2, int(H * 0.50)
gear(cx - 92, cy - 52, 152, 120, 13, 6, SEPIA)
gear(cx + 120, cy + 80, 110, 86, 11, 6, SEPIA)

def ctext(y, txt, f, col):
    w = d.textlength(txt, font=f); d.text(((W - w) // 2, y), txt, font=f, fill=col)

ctext(165, "Los engranajes", ImageFont.truetype(FR, 96), GREEN)
ctext(260, "de la mente", ImageFont.truetype(FR, 96), GREEN)
d.line([(W * 0.32, 388), (W * 0.68, 388)], fill=BEIGE, width=2)
ctext(408, "Comprendiendo el Yo, el Ello y el Superyó", ImageFont.truetype(FR, 40), SEPIA)
ctext(458, "Un viaje psicoanalítico hacia el conocimiento del ser", ImageFont.truetype(FI, 30), BEIGE)

logo = Image.open(ROOT / "assets" / "logo-mindworld-transparent.png").convert("RGBA")
lw = int(W * 0.205); lh = int(lw * logo.height / logo.width); logo = logo.resize((lw, lh))
ly = int(H * 0.785); img.paste(logo, ((W - lw) // 2, ly), logo)
ctext(ly + lh + 28, "Daniel Orozco Abia", ImageFont.truetype(FR, 46), GREEN)
ctext(ly + lh + 90, "Psicólogo General Sanitario · CV11515", ImageFont.truetype(FR, 26), SEPIA)

img.save(OUT, quality=93)
print("Portada generada:", OUT, img.size)
