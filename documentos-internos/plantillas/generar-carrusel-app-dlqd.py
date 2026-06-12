#!/usr/bin/env python3
"""Carrusel lanzamiento app «Di lo que quieres decir» · estilo brutalist tipográfico TWIM.

Copy verbatim del kit `contenido-rrss/app-dlqd-lanzamiento-ig.md` (12 jun 2026).
Plantilla derivada de generar-carrusel-mirada-v3-brutalist.py.
"""
import os
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

CREMA = (253, 252, 250)
VERDE_OSCURO = (23, 61, 48)
BEIGE = (194, 167, 139)
W, H = 1080, 1350
MX = 60

FONT_DIRS = [
    os.environ.get("TWIM_FONTS", ""),
    "/tmp/fonts",
    "/root/.fonts",
    os.path.expanduser("~/.fonts"),
    "/mnt/skills/examples/canvas-design/canvas-fonts",
]

FT = {
    "serif": "InstrumentSerif-Regular.ttf",
    "serif_it": "InstrumentSerif-Italic.ttf",
    "sans": "BarlowCondensed-Regular.ttf",
    "sans_md": "BarlowCondensed-Medium.ttf",
}


def font_path(name):
    for d in FONT_DIRS:
        if d and os.path.isfile(os.path.join(d, name)):
            return os.path.join(d, name)
    raise FileNotFoundError(f"fuente {name} no encontrada en {FONT_DIRS}")


def font(k, s):
    return ImageFont.truetype(font_path(FT[k]), s)


def wrap(draw, text, fnt, max_w):
    words, out, line = text.split(), [], ""
    for wd in words:
        test = (line + " " + wd).strip()
        if draw.textlength(test, font=fnt) <= max_w:
            line = test
        else:
            if line:
                out.append(line)
            line = wd
    if line:
        out.append(line)
    return out


def fit_text(draw, text, key, max_w, max_h, start=420, min_size=80):
    size = start
    while size > min_size:
        fnt = font(key, size)
        lines = wrap(draw, text, fnt, max_w)
        lh = int(size * 1.05)
        total_h = len(lines) * lh
        widths = [draw.textlength(ln, font=fnt) for ln in lines]
        if total_h <= max_h and (not widths or max(widths) <= max_w):
            return fnt, lines, lh
        size -= 8
    fnt = font(key, min_size)
    return fnt, wrap(draw, text, fnt, min_size and max_w), int(min_size * 1.05)


OUT = Path("contenido-rrss/app-dlqd-lanzamiento-ig")
OUT.mkdir(exist_ok=True, parents=True)


def slide(idx, kicker, palabra, dark=False, sub_top=None, sub_bot=None, cta=None):
    bg = VERDE_OSCURO if dark else CREMA
    fg = CREMA if dark else VERDE_OSCURO
    sub = BEIGE
    img = Image.new("RGB", (W, H), bg)
    draw = ImageDraw.Draw(img)

    fk = font("sans_md", 23)
    draw.text((MX, 58), kicker.upper(), font=fk, fill=sub)
    pag = f"{idx:02d}/07"
    draw.text((W - MX - draw.textlength(pag, font=fk), 58), pag, font=fk, fill=sub)
    draw.line([(MX, 108), (W - MX, 108)], fill=sub, width=3)

    y = 168
    if sub_top:
        fst = font("sans_md", 46)
        for ln in wrap(draw, sub_top, fst, W - 2 * MX):
            draw.text((MX, y), ln, font=fst, fill=sub)
            y += 56
        y += 34

    fsb = font("serif_it", 52)
    sub_bot_lines = wrap(draw, sub_bot, fsb, W - 2 * MX) if sub_bot else []
    sub_bot_h = (len(sub_bot_lines) * 58 + 30) if sub_bot_lines else 0

    bottom_limit = (H - 210) if cta else (H - 120)
    max_h = bottom_limit - y - sub_bot_h

    fnt, lines, lh = fit_text(draw, palabra.upper(), "sans_md", W - 2 * MX, max_h)
    for ln in lines:
        draw.text((MX, y), ln, font=fnt, fill=fg)
        y += lh

    if sub_bot_lines:
        yy = y + 8
        for ln in sub_bot_lines:
            draw.text((MX, yy), ln, font=fsb, fill=sub)
            yy += 58

    if cta:
        fct = font("sans_md", 40)
        draw.line([(MX, H - 188), (W - MX, H - 188)], fill=sub, width=3)
        draw.text((MX, H - 166), cta.upper(), font=fct, fill=fg)

    ff = font("sans", 22)
    draw.text((MX, H - 58), "@DANIOROZCOPSICOLOGO  ·  TWIMPROJECT.COM", font=ff, fill=sub)

    img.save(OUT / f"slide-{idx:02d}.png", "PNG")
    print(f"OK slide-{idx:02d}")


# ---- 7 slides · copy verbatim del kit (v2 · arranque por identificación, indicación de Daniel 12 jun) ----

slide(1, "Herramienta nueva · gratuita", "Seguro que te ha pasado.", dark=True,
      sub_bot="Quieres explicar algo y no te salen las palabras correctas.")

slide(2, "Lo que sale en su lugar", "Las palabras te salen envueltas de ansiedad, de rabia, de frustración.",
      dark=False,
      sub_bot="O cargadas de una negatividad que no querías poner ahí.")

slide(3, "La escena", "Lo escribes. Lo borras. Lo vuelves a escribir.", dark=True,
      sub_bot="Y al final no envías nada — o envías el reproche entero.")

slide(4, "Por qué no te escucha", "Cuando el otro lee un reproche, se defiende del reproche.",
      dark=False,
      sub_bot="Y lo que necesitabas decir se queda sin escuchar.")

slide(5, "Di lo que quieres decir", "Escribes lo que te sale, sin filtro,", dark=True,
      sub_top="He construido una herramienta gratuita que hace de traductor:",
      sub_bot="y te devuelve el mensaje que sí se puede escuchar.")

slide(6, "El sello · el vínculo", "Sin reproches. Sin atacar.", dark=False,
      sub_bot="Cuidando lo que de verdad importa: el vínculo que tenéis. Nada de lo que escribas se guarda.")

slide(7, "Cierre", "«Di lo que quieres decir»", dark=True,
      cta="Gratis · en el enlace de la bio · twimproject.com")
