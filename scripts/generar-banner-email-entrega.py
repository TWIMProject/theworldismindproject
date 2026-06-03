#!/usr/bin/env python3
"""
Banner de cabecera para los emails de ENTREGA de compra (libro digital y cuaderno).

Pedido por Daniel el 3 jun 2026: no reutilizar los banners de «Te escribo / Volver
a mí / Directo» (son editoriales / de productos concretos y confunden en un email
de entrega). Banner sobrio y reutilizable: fondo verde TWIM + logo MIND WORLD en
crema + filete beige.

Salida: assets/email-banner-twim-entrega.png (1200×300, se ve a 600px en email).
Reproducir: python3 scripts/generar-banner-email-entrega.py
"""
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
GREEN = (23, 61, 48); CREAM = (253, 252, 250); BEIGE = (194, 167, 139)
W, H = 1200, 300
img = Image.new('RGB', (W, H), GREEN)
d = ImageDraw.Draw(img)

logo = Image.open(ROOT / 'assets' / 'logo-mindworld-transparent.png').convert('RGBA')
lw = int(W * 0.20); lh = int(lw * logo.height / logo.width); logo = logo.resize((lw, lh))
alpha = logo.split()[3]
cream = Image.new('RGBA', logo.size, CREAM + (255,)); cream.putalpha(alpha)
ly = (H - lh) // 2 - 6
img.paste(cream, ((W - lw) // 2, ly), cream)
d.line([(W * 0.42, ly + lh + 22), (W * 0.58, ly + lh + 22)], fill=BEIGE, width=3)

out = ROOT / 'assets' / 'email-banner-twim-entrega.png'
img.save(out)
print('banner:', out, img.size)
