#!/usr/bin/env python3
"""Carrusel «5 señales» · DISEÑO FINAL · Concepto D Brutalist tipográfico · paleta TWIM."""
import os
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

CREMA = (253, 252, 250)
VERDE_OSCURO = (23, 61, 48)
BEIGE = (194, 167, 139)
W, H = 1080, 1350
MX = 60

# Resolución de fuentes · convención del repo (env TWIM_FONTS + ubicaciones
# habituales), para que el script no dependa del entorno exacto de quien lo generó.
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


def fit_text(draw, text, key, max_w, max_h, start=540, min_size=90):
    """Tamaño máximo de la palabra-bomba que cabe en el bloque.
    lh con factor 1.05 reserva descendentes y acentos en mayúscula."""
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
    return fnt, wrap(draw, text, fnt, max_w), int(min_size * 1.05)


OUT = Path("contenido-rrss/carrusel-5-senales-mirada-del-otro")
OUT.mkdir(exist_ok=True, parents=True)


def slide(idx, kicker, palabra, dark=False, sub_top=None, sub_bot=None, cta=None):
    bg = VERDE_OSCURO if dark else CREMA
    fg = CREMA if dark else VERDE_OSCURO
    sub = BEIGE
    img = Image.new("RGB", (W, H), bg)
    draw = ImageDraw.Draw(img)

    # micro-kicker + paginacion + filete fuerte
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

    # pre-calcular alto real del sub_bot (cursiva 52) para reservar
    fsb = font("serif_it", 52)
    sub_bot_lines = wrap(draw, sub_bot, fsb, W - 2 * MX) if sub_bot else []
    sub_bot_h = (len(sub_bot_lines) * 58 + 30) if sub_bot_lines else 0

    bottom_limit = (H - 210) if cta else (H - 120)
    max_h = bottom_limit - y - sub_bot_h

    fnt, lines, lh = fit_text(draw, palabra.upper(), "sans_md", W - 2 * MX, max_h, start=540)
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


# ---- 7 slides · arco brutalist v4 · pensamientos del día a día ----
# Cambio 5 jun 2026 · las palabras-bomba pasan de sentencias clínicas
# abstractas a pensamientos literales que la persona se oye a diario.
# Aplica regla de concreción CLAUDE.md.

slide(1, "5 señales · la mirada del otro", "«Eso me pasa.»", dark=False,
      sub_top="Las que llevas años haciendo. No las llamabas señales.",
      sub_bot="Vas a pensarlo en cada slide. Cuenta cuántas.")

slide(2, "Señal 01 · hipervigilancia", "«¿Estás enfadada?»", dark=True,
      sub_bot="Lo preguntas varias veces al día, aunque acabe de decirte que no.")

slide(3, "Señal 02 · identidad espejo", "«Tienes razón.»", dark=False,
      sub_bot="Aunque la semana pasada defendías exactamente lo contrario.")

slide(4, "Señal 03 · pánico al conflicto", "«¿Me va a dejar?»", dark=True,
      sub_bot="Por una opinión distinta, ya estás haciendo cuentas.")

slide(5, "Señal 04 · idealizar y reñir", "«Tú no eras así.»", dark=False,
      sub_bot="Comete un fallo humano normal y deja de encajar con el referente que era para ti.")

slide(6, "Señal 05 · disolución", "«¿Quién soy?»", dark=True,
      sub_bot="El día que te dejan, como si te hubieras quedado en blanco.")

slide(7, "Cierre · directo gratuito", "Míralo.", dark=False,
      sub_top="Si te has reconocido en dos o tres, no estás peor que nadie.",
      sub_bot="Llevas tiempo oyéndolo sin nombrarlo.",
      cta="Domingo 7 jun · 19h · enlace en bio")
