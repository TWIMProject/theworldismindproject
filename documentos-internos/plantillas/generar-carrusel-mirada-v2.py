#!/usr/bin/env python3
"""Carrusel «5 senales» v2 · mezcla Expediente+Mirada · paleta TWIM · 1080x1350."""
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import math
from pathlib import Path

CREMA = (253, 252, 250)
VERDE_OSCURO = (23, 61, 48)
VERDE_MEDIO = (38, 92, 75)
BEIGE = (194, 167, 139)
W, H = 1080, 1350
MX = 90

FT = {
    "serif": "/tmp/fonts/InstrumentSerif-Regular.ttf",
    "serif_it": "/tmp/fonts/InstrumentSerif-Italic.ttf",
    "sans": "/tmp/fonts/BarlowCondensed-Regular.ttf",
    "sans_md": "/tmp/fonts/BarlowCondensed-Medium.ttf",
}


def font(k, s):
    return ImageFont.truetype(FT[k], s)


def add_grain(img, intensity):
    arr = np.asarray(img).astype(np.int16)
    noise = np.random.normal(0, intensity, arr.shape[:2])
    noise = np.stack([noise] * 3, axis=-1)
    return Image.fromarray(np.clip(arr + noise, 0, 255).astype(np.uint8))


def add_vignette(img, strength):
    w, h = img.size
    yy, xx = np.mgrid[0:h, 0:w]
    d = np.sqrt(((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2)
    mask = np.clip(1 - (d - 0.55) * strength, 0, 1)
    arr = np.asarray(img).astype(np.float32) * mask[..., None]
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))


def vgradient(top, bot):
    yy = np.linspace(0, 1, H)[:, None]
    arr = np.zeros((H, W, 3), np.float32)
    for i in range(3):
        arr[..., i] = top[i] + (bot[i] - top[i]) * yy
    return Image.fromarray(arr.astype(np.uint8))


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


def draw_eye(draw, cx, cy, rx, ry, color, lw, iris_r, iris_color):
    draw.arc([cx - rx, cy - ry, cx + rx, cy + ry], 200, 340, fill=color, width=lw)
    draw.arc([cx - rx, cy - ry, cx + rx, cy + ry], 20, 160, fill=color, width=lw)
    draw.ellipse([cx - iris_r, cy - iris_r, cx + iris_r, cy + iris_r], outline=color, width=lw)
    draw.ellipse([cx - iris_r * 0.62, cy - iris_r * 0.62, cx + iris_r * 0.62, cy + iris_r * 0.62],
                 outline=iris_color, width=max(2, lw - 1))
    pr = iris_r * 0.26
    draw.ellipse([cx - pr, cy - pr, cx + pr, cy + pr], fill=color)
    for ang in range(0, 360, 30):
        a = math.radians(ang)
        x1, y1 = cx + math.cos(a) * (rx + 30), cy + math.sin(a) * (ry + 30)
        x2, y2 = cx + math.cos(a) * (rx + 70), cy + math.sin(a) * (ry + 55)
        draw.line([(x1, y1), (x2, y2)], fill=color, width=2)


OUT = Path("contenido-rrss/carrusel-5-senales-mirada-del-otro")
OUT.mkdir(exist_ok=True, parents=True)


def header(draw, kicker, pag, accent):
    fk = font("sans_md", 27)
    draw.text((MX, 96), kicker.upper(), font=fk, fill=accent)
    pg = f"{pag} / 07"
    draw.text((W - MX - draw.textlength(pg, font=fk), 96), pg, font=fk, fill=accent)


def footer(draw, sub):
    ff = font("sans", 24)
    foot = "@daniorozcopsicologo · twimproject.com"
    draw.text((MX, H - 92), foot, font=ff, fill=sub)


def render_eye(idx, n, kicker, setup, punch, punch_it, cta=None):
    """Slides hook y cierre · ojo centrado, fondo crema o verde."""
    dark = (idx == 1)
    bg = VERDE_OSCURO if dark else CREMA
    fg = CREMA if dark else VERDE_OSCURO
    sub = (196, 206, 196) if dark else VERDE_MEDIO
    img = vgradient((28, 70, 56), (16, 44, 34)) if dark else Image.new("RGB", (W, H), bg)
    draw = ImageDraw.Draw(img)

    draw_eye(draw, W // 2, 348, 300, 152, BEIGE, 6, 100, fg)
    header(draw, kicker, n, BEIGE if dark else VERDE_MEDIO)

    y = 650
    if setup:
        fs = font("sans", 42)
        for ln in wrap(draw, setup, fs, W - 2 * MX):
            tw = draw.textlength(ln, font=fs)
            draw.text(((W - tw) / 2, y), ln, font=fs, fill=sub)
            y += 54
        y += 26
    fp = font("serif", 134)
    for ln in wrap(draw, punch, fp, W - 2 * MX):
        tw = draw.textlength(ln, font=fp)
        draw.text(((W - tw) / 2, y), ln, font=fp, fill=fg)
        y += 126
    fpi = font("serif_it", 134)
    for ln in wrap(draw, punch_it, fpi, W - 2 * MX):
        tw = draw.textlength(ln, font=fpi)
        draw.text(((W - tw) / 2, y), ln, font=fpi, fill=BEIGE)
        y += 126
    if cta:
        fc = font("sans_md", 44)
        tw = draw.textlength(cta, font=fc)
        draw.text(((W - tw) / 2, H - 250), cta, font=fc, fill=BEIGE if dark else VERDE_MEDIO)
    footer(draw, sub)
    img = add_grain(img, 6)
    if dark:
        img = add_vignette(img, 0.45)
    img.save(OUT / f"slide-{idx:02d}.png", "PNG")
    print(f"OK slide-{idx:02d} (ojo)")


def render_num(idx, n, num, kicker, setup, punch, punch_it, closer=None):
    """Slides de senal · numero gigante al fondo, composicion asimetrica."""
    dark = (idx % 2 == 0)
    if dark:
        img = vgradient((28, 70, 56), (16, 44, 34))
        fg, sub, accent = CREMA, (210, 218, 210), BEIGE
        num_alpha = 30
    else:
        img = Image.new("RGB", (W, H), CREMA)
        fg, sub, accent = VERDE_OSCURO, VERDE_MEDIO, VERDE_MEDIO
        num_alpha = 46
    draw = ImageDraw.Draw(img)

    # numero gigante marca de agua, esquina inferior derecha
    fbig = font("serif", 720)
    tw = draw.textlength(num, font=fbig)
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    ld.text((W - tw + 50, H - 860), num, font=fbig, fill=BEIGE + (num_alpha,))
    img = Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB")
    draw = ImageDraw.Draw(img)

    header(draw, kicker, n, accent)
    draw.line([(MX, 152), (W - MX, 152)], fill=(accent if not dark else (120, 112, 96)), width=2)

    y = 330
    if setup:
        fs = font("sans", 44)
        for ln in wrap(draw, setup, fs, W - 2 * MX):
            draw.text((MX, y), ln, font=fs, fill=sub)
            y += 56
        y += 38
    fp = font("serif", 132)
    for ln in wrap(draw, punch, fp, W - 2 * MX):
        draw.text((MX, y), ln, font=fp, fill=fg)
        y += 122
    fpi = font("serif_it", 132)
    for ln in wrap(draw, punch_it, fpi, W - 2 * MX):
        draw.text((MX, y), ln, font=fpi, fill=BEIGE if dark else VERDE_MEDIO)
        y += 122
    draw.line([(MX, y + 22), (MX + 120, y + 22)], fill=BEIGE, width=4)
    if closer:
        fcl = font("sans", 38)
        draw.text((MX, y + 60), closer, font=fcl, fill=sub)
    footer(draw, sub)
    img = add_grain(img, 6)
    if dark:
        img = add_vignette(img, 0.45)
    img.save(OUT / f"slide-{idx:02d}.png", "PNG")
    print(f"OK slide-{idx:02d} (num {num})")


# ---- slides ----
render_eye(1, "01", "La mirada del otro",
           "Las que cuesta ver, porque hace años que las haces.",
           "5 señales", "de que vives en su mirada")

render_num(2, "02", "1", "Señal 01 · hipervigilancia",
           "Varias veces al día, sin darte cuenta.",
           "Necesitas que te diga", "que está todo bien",
           closer="entre vosotros, para sentirte en paz.")

render_num(3, "03", "2", "Señal 02 · identidad espejo",
           "En la misma semana defiendes una cosa y la contraria.",
           "Tu opinión cambia", "según quién te escucha")

render_num(4, "04", "3", "Señal 03 · pánico al conflicto",
           "Alguien no está de acuerdo contigo.",
           "Y lo vives", "como si fueras a perderle")

render_num(5, "05", "4", "Señal 04 · idealizar y reñir",
           "Al principio es perfecto para ti.",
           "Cuando deja de serlo,", "le castigas por ello")

render_num(6, "06", "5", "Señal 05 · disolución",
           "No es la tristeza normal de una ruptura.",
           "Cuando te dejan,", "sientes que desapareces")

render_eye(7, "07", "No se apaga queriéndote más",
           "El domingo lo miramos de frente. Una hora, en directo, gratis.",
           "Se afloja", "viéndolo",
           cta="Directo dom 7 jun · 19h · enlace en bio")
