#!/usr/bin/env python3
"""Carrusel «5 señales» · DISEÑO FINAL · Concepto D Brutalist tipográfico · paleta TWIM."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

CREMA = (253, 252, 250)
VERDE_OSCURO = (23, 61, 48)
VERDE_MEDIO = (38, 92, 75)
BEIGE = (194, 167, 139)
W, H = 1080, 1350
MX = 60

FT = {
    "serif": "/tmp/fonts/InstrumentSerif-Regular.ttf",
    "serif_it": "/tmp/fonts/InstrumentSerif-Italic.ttf",
    "sans": "/tmp/fonts/BarlowCondensed-Regular.ttf",
    "sans_md": "/tmp/fonts/BarlowCondensed-Medium.ttf",
}


def font(k, s):
    return ImageFont.truetype(FT[k], s)


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


# ---- 7 slides · arco brutalist ----
slide(1, "5 señales · la mirada del otro", "Vives en su mirada.", dark=False,
      sub_bot="Las que cuesta ver, porque hace años que las haces.")

slide(2, "Señal 01 · hipervigilancia", "Todo bien.", dark=True,
      sub_top="Necesitas que te diga, varias veces al día,",
      sub_bot="entre vosotros, para sentirte en paz.")

slide(3, "Señal 02 · identidad espejo", "Según quién.", dark=False,
      sub_top="Tu opinión cambia",
      sub_bot="En la misma semana defiendes una cosa y la contraria.")

slide(4, "Señal 03 · pánico al conflicto", "Vas a perderle.", dark=True,
      sub_top="Alguien no está de acuerdo contigo y lo vives",
      sub_bot="como si te fueras a quedar sin él.")

slide(5, "Señal 04 · idealizar y reñir", "Le castigas.", dark=False,
      sub_top="Al principio es perfecto para ti.",
      sub_bot="Cuando deja de serlo, le castigas por ello.")

slide(6, "Señal 05 · disolución", "Desapareces.", dark=True,
      sub_top="No es la tristeza normal de una ruptura.",
      sub_bot="Cuando te dejan, sientes que desapareces.")

slide(7, "Cierre · directo gratuito", "Míralo.", dark=False,
      sub_top="No se afloja queriéndote más.",
      sub_bot="Se afloja viéndolo.",
      cta="Domingo 7 jun · 19h · enlace en bio")
