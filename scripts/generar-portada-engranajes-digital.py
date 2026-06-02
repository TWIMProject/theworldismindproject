#!/usr/bin/env python3
"""
Genera la portada de la EDICIÓN DIGITAL TWIM de «Los engranajes de la mente».

Decidido el 2 jun 2026 (sesión claude/blissful-lovelace-VPbaj). Daniel pidió una
portada "más marca TWIM y con novedad" para la venta directa digital, distinta de
la de Amazon. En vez de rediseñar de cero (sin ilustración quedaría sosa), se parte
de la portada existente y se le da sello TWIM:

  1. Duotono cálido sobre `portadalosengranajes.jpg` para igualar los tonos a la
     contraportada elegida (`contraportadaretro.jpg`) y eliminar el verde original.
  2. Banda inferior verde TWIM (#173D30) con el logo MIND WORLD PROJECT, el nombre
     del autor y el colegiado correctos (se elimina el alias "Psicólogo Random").

Salida: documentos-internos/producto-engranajes-digital/portada-edicion-digital-twim.jpg
Reproducir: python3 scripts/generar-portada-engranajes-digital.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "documentos-internos" / "producto-engranajes-digital"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT = OUT_DIR / "portada-edicion-digital-twim.jpg"

GREEN = "#173D30"; BEIGE = "#C2A78B"; CREAM = "#FDFCFA"
# Fuente de marca (Instrument Serif). Ruta del entorno; ajustar si se ejecuta en otro.
FONT_DIR = Path("/mnt/skills/examples/canvas-design/canvas-fonts")
F_REG = str(FONT_DIR / "InstrumentSerif-Regular.ttf")
F_ITA = str(FONT_DIR / "InstrumentSerif-Italic.ttf")

# 1 · DUOTONO: igualar tonos a la contraportada retro
base = Image.open(ROOT / "portadalosengranajes.jpg").convert("RGB")
ref = Image.open(ROOT / "contraportadaretro.jpg").convert("RGB")
cream = ref.getpixel((15, 15))
mid = ref.getpixel((ref.size[0] // 2, int(ref.size[1] * 0.45)))
dark = (52, 40, 28)
g = ImageEnhance.Contrast(base.convert("L")).enhance(1.08)
img = ImageOps.colorize(g, black=dark, mid=mid, white=cream)

# 2 · BANDA TWIM con logo + autor
W, H = img.size
d = ImageDraw.Draw(img)
band_top = int(H * 0.78)
d.rectangle([0, band_top, W, H], fill=GREEN)
d.rectangle([0, band_top, W, band_top + 4], fill=BEIGE)
band_h = H - band_top

logo = Image.open(ROOT / "assets" / "logo-mindworld-on-dark.png").convert("RGBA")
lw = int(W * 0.21); lh = int(lw * logo.height / logo.width)
logo = logo.resize((lw, lh))

f_name = ImageFont.truetype(F_REG, 52)
f_role = ImageFont.truetype(F_ITA, 28)
name = "Daniel Orozco Abia"
role = "Psicólogo General Sanitario · CV11515"
na = f_name.getbbox(name); nh = na[3] - na[1]
ra = f_role.getbbox(role); rh = ra[3] - ra[1]
gap1 = int(band_h * 0.10); gap2 = int(band_h * 0.13)
block = lh + gap1 + nh + gap2 + rh
start = band_top + (band_h - block) // 2
img.paste(logo, ((W - lw) // 2, start), logo)
tw = d.textlength(name, font=f_name)
d.text(((W - tw) // 2, start + lh + gap1 - na[1]), name, font=f_name, fill=CREAM)
rw = d.textlength(role, font=f_role)
d.text(((W - rw) // 2, start + lh + gap1 + nh + gap2 - ra[1]), role, font=f_role, fill=BEIGE)

img.save(OUT, quality=93)
print("Portada generada:", OUT, img.size)
