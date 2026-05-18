"""Genera el Carrusel #3 «La voz que te juzga» para Instagram/LinkedIn.

7 slides 1080x1350 (4:5), sistema visual A1 verde dominante. Copy verbatim
del BRIEFING.md §2. Mismo pipeline que `te-escribo-fragmento-carta1/
generar-carrusel.py` (loader de fuentes, logo MIND WORLD extraído de
podcast-cover.png y pasado a blanco sólido, paleta TWIM).

USO (en tu ordenador, una vez tengas las 4 TTF):
    pip install pillow
    # descarga gratis de Google Fonts: Instrument Serif y Barlow Condensed
    # mete las 4 .ttf en una carpeta y apúntala con TWIM_FONTS_DIR:
    TWIM_FONTS_DIR="~/Descargas/fuentes-twim" python generar-carrusel-voz-que-te-juzga.py
Salida: slide-01.png … slide-07.png en esta misma carpeta.
"""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

REPO = Path(__file__).resolve().parent.parent.parent
DESTINO = REPO / "contenido-rrss" / "te-escribo-voz-que-te-juzga"


def _resolver_fuentes():
    candidatos = []
    if env := os.environ.get("TWIM_FONTS_DIR"):
        candidatos.append(Path(env).expanduser())
    candidatos += [
        Path.home() / ".local" / "share" / "fonts",
        Path.home() / "Library" / "Fonts",
        Path("/usr/local/share/fonts"),
        Path("/Library/Fonts"),
        Path("C:/Windows/Fonts"),
    ]
    requeridas = [
        "BarlowCondensed-Regular.ttf", "BarlowCondensed-Bold.ttf",
        "InstrumentSerif-Regular.ttf", "InstrumentSerif-Italic.ttf",
    ]
    for c in candidatos:
        if c.is_dir() and all((c / f).exists() for f in requeridas):
            return c
    rutas = "\n  · ".join(str(c) for c in candidatos)
    raise FileNotFoundError(
        "Faltan las TTF de marca.\n"
        f"Necesarias: {', '.join(requeridas)}.\n"
        "Descárgalas gratis: fonts.google.com/specimen/Instrument+Serif y "
        "fonts.google.com/specimen/Barlow+Condensed (botón «Download family»).\n"
        "Renombra a los nombres de arriba si hiciera falta y define "
        "TWIM_FONTS_DIR, o colócalas en una de:\n  · " + rutas)


FUENTES = _resolver_fuentes()

VERDE = (23, 61, 48)
BEIGE = (194, 167, 139)
CREMA = (253, 252, 250)
W, H, MARGEN, TOTAL = 1080, 1350, 80, 7


def sans(weight, size):
    return ImageFont.truetype(str(FUENTES / f"BarlowCondensed-{weight}.ttf"), size)


def serif(size, italic=False):
    a = "InstrumentSerif-Italic.ttf" if italic else "InstrumentSerif-Regular.ttf"
    return ImageFont.truetype(str(FUENTES / a), size)


def medir(t, f):
    b = f.getbbox(t)
    return b[2] - b[0], b[3] - b[1]


def centrado(d, t, f, c, y):
    w, _ = medir(t, f)
    d.text(((W - w) // 2, y), t, font=f, fill=c)


def fit(lineas, hacer, size, max_w=W - 2 * MARGEN - 40):
    """Reduce el tamaño hasta que la línea más ancha quepa."""
    f = hacer(size)
    while size > 24 and max(medir(l, f)[0] for l in lineas) > max_w:
        size -= 3
        f = hacer(size)
    return f


def cargar_logo(ancho):
    cover = Image.open(REPO / "podcast-cover.png").convert("RGB")
    logo_rgb = cover.crop((2200, 2380, 2880, 2880))
    h = int(ancho * logo_rgb.height / logo_rgb.width)
    logo = logo_rgb.resize((ancho, h), Image.LANCZOS).convert("RGBA")
    px = logo.load()
    for y in range(h):
        for x in range(ancho):
            r, g, b, _ = px[x, y]
            dist = ((r - 23) ** 2 + (g - 61) ** 2 + (b - 48) ** 2) ** 0.5
            px[x, y] = (255, 255, 255, int(min(1.0, dist / 215.0) * 255))
    return logo


def base(numero, kicker, logo):
    img = Image.new("RGB", (W, H), VERDE)
    d = ImageDraw.Draw(img)
    fk = sans("Bold", 26)
    cur = MARGEN
    for ch in kicker:
        d.text((cur, MARGEN + 6), ch, font=fk, fill=BEIGE)
        cur += medir(ch, fk)[0] + 4
    fp = sans("Regular", 26)
    pag = f"{numero:02d} / {TOTAL:02d}"
    pw, _ = medir(pag, fp)
    d.text((W - MARGEN - pw, MARGEN + 6), pag, font=fp, fill=BEIGE)
    rgba = img.convert("RGBA")
    rgba.paste(logo, ((W - logo.width) // 2, H - 210), logo)
    img = rgba.convert("RGB")
    d = ImageDraw.Draw(img)
    centrado(d, "@daniorozcopsicologo  ·  twimproject.com",
             sans("Regular", 24), CREMA, H - MARGEN - 6)
    return img, d


def render(numero, kicker, bloques, logo):
    """bloques: lista de (lineas, fuente, color, gap_interlinea).
    Se centran verticalmente en la banda entre header y footer."""
    img, d = base(numero, kicker, logo)
    GAP_BLOQUE = 54
    alturas = []
    for lineas, f, _c, gap in bloques:
        lh = medir("Hg", f)[1] + gap
        alturas.append(lh * len(lineas) - gap)
    total = sum(alturas) + GAP_BLOQUE * (len(bloques) - 1)
    y = (300 + (H - 320)) // 2 - total // 2
    for (lineas, f, c, gap), alto in zip(bloques, alturas):
        lh = medir("Hg", f)[1] + gap
        for i, ln in enumerate(lineas):
            centrado(d, ln, f, c, y + i * lh)
        y += alto + GAP_BLOQUE
    img.save(DESTINO / f"slide-{numero:02d}.png", "PNG", optimize=True)
    print(f"  OK slide-{numero:02d}.png")


def main():
    DESTINO.mkdir(parents=True, exist_ok=True)
    logo = cargar_logo(150)
    print(f"Logo: {logo.size} · Fuentes: {FUENTES}")

    render(1, "TWIM PROJECT", [
        (["5 frases del juez interno", "que confundes con", "tu propio criterio."],
         fit(["5 frases del juez interno"], lambda s: serif(s), 92), CREMA, 14),
    ], logo)

    render(2, "TWIM PROJECT", [
        (["Ya por la noche, lavándote", "los dientes, te oyes decir:"], sans("Regular", 42), CREMA, 12),
        (["«No has hecho nada", "que valga la pena hoy.»"], serif(82), CREMA, 12),
        (["no es tu criterio.", "es una grabación."], serif(70, italic=True), BEIGE, 10),
    ], logo)

    render(3, "TWIM PROJECT", [
        (["Mientras escribes un email,", "una voz baja:"], sans("Regular", 42), CREMA, 12),
        (["«Esto te ha", "quedado regular.»"], serif(88), CREMA, 12),
        (["tampoco eres tú."], serif(72, italic=True), BEIGE, 10),
    ], logo)

    render(4, "TWIM PROJECT", [
        (["En medio de una", "conversación con un amigo:"], sans("Regular", 42), CREMA, 12),
        (["«Otros lo habrían", "hecho mejor.»"], serif(88), CREMA, 12),
        (["tampoco."], serif(72, italic=True), BEIGE, 10),
    ], logo)

    render(5, "TWIM PROJECT", [
        (["Y las dos últimas, casi a la vez:"], sans("Regular", 42), CREMA, 12),
        (["«No estás siendo bastante.»", "«¿Y eso es todo lo que", "vas a hacer hoy?»"], serif(64), CREMA, 12),
        (["ninguna es tu voz.", "todas las aprendiste."], serif(60, italic=True), BEIGE, 10),
    ], logo)

    render(6, "TWIM PROJECT", [
        (["El cambio no es decir", "«soy suficiente»."], sans("Regular", 42), CREMA, 12),
        (["Es notar quién está", "hablando antes", "de creérselo."], serif(80), CREMA, 12),
        (["La frase no se discute.", "Se le pone autor."], serif(64, italic=True), BEIGE, 10),
    ], logo)

    render(7, "TE ESCRIBO", [
        (["Cómo se monta esa voz", "y qué la debilita."], serif(84), CREMA, 14),
        (["Te lo cuento en la carta", "de esta semana. Despacio."], sans("Regular", 42), CREMA, 12),
        (["twimproject.com/newsletter/"], sans("Bold", 48), BEIGE, 10),
        (["Carta nueva esta semana."], serif(46, italic=True), BEIGE, 10),
    ], logo)

    print(f"Listo. 7 slides en {DESTINO.relative_to(REPO)}")


if __name__ == "__main__":
    main()
