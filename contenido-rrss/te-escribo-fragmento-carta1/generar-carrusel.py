"""Genera el carrusel feed Instagram del fragmento de la Carta #1 de
"Te escribo". 7 slides 1080x1350 (4:5) en sistema visual A1 verde
dominante, idéntico al carrusel "Tu cansancio no es físico" publicado
el 25 abril 2026.

Estructura editorial (manifesto Carta #1 condensado, sin diluirlo):
01 Hook — anti-promesa
02 Diagnóstico — el ruido como etiquetas
03 Problema — te dan un nombre y te quedas igual
04 Daño — sabes el nombre pero no qué hacer
05 Promesa — el fragmento literal (climax)
06 Sentido — para qué sirve la newsletter
07 CTA — suscríbete + fecha Carta #2

Tipografías:
- Barlow Condensed (kickers, setup, footer) — ya en sistema.
- Instrument Serif Regular + Italic (titulares y citas) — descargada.

Paleta:
- #173D30 fondo · #FDFCFA texto · #C2A78B kicker/cita · cita italica.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# --- Paths -------------------------------------------------------------------

REPO = Path(__file__).resolve().parent.parent.parent
DESTINO = REPO / "contenido-rrss" / "te-escribo-fragmento-carta1"


def _resolver_fuentes():
    """Devuelve el primer directorio existente que contenga las TTF
    necesarias. Permite override via env var TWIM_FONTS_DIR; si no,
    busca en ubicaciones convencionales por SO."""
    import os
    candidatos = []
    if env := os.environ.get("TWIM_FONTS_DIR"):
        candidatos.append(Path(env))
    candidatos += [
        Path.home() / ".local" / "share" / "fonts",            # Linux user
        Path.home() / "Library" / "Fonts",                      # macOS user
        Path("/usr/local/share/fonts"),                         # Linux system
        Path("/Library/Fonts"),                                 # macOS system
        Path("C:/Windows/Fonts"),                               # Windows
    ]
    requeridas = [
        "BarlowCondensed-Regular.ttf", "BarlowCondensed-Bold.ttf",
        "InstrumentSerif-Regular.ttf", "InstrumentSerif-Italic.ttf",
    ]
    for c in candidatos:
        if c.is_dir() and all((c / f).exists() for f in requeridas):
            return c
    raise FileNotFoundError(
        "No se han encontrado las fuentes requeridas en ninguna ruta. "
        f"Necesarias: {', '.join(requeridas)}. "
        f"Define TWIM_FONTS_DIR o instala en ~/.local/share/fonts. "
        f"Probadas: {[str(c) for c in candidatos]}"
    )


FUENTES = _resolver_fuentes()

# --- Paleta TWIM (sistema visual IG) -----------------------------------------

VERDE_OSCURO = (23, 61, 48)        # #173D30
BEIGE = (194, 167, 139)            # #C2A78B
CREMA = (253, 252, 250)            # #FDFCFA

# --- Canvas ------------------------------------------------------------------

W, H = 1080, 1350
MARGEN = 80
TOTAL_SLIDES = 7

# --- Fuentes -----------------------------------------------------------------

def sans(weight, size):
    return ImageFont.truetype(str(FUENTES / f"BarlowCondensed-{weight}.ttf"), size)


def serif(size, italic=False):
    archivo = "InstrumentSerif-Italic.ttf" if italic else "InstrumentSerif-Regular.ttf"
    return ImageFont.truetype(str(FUENTES / archivo), size)


# --- Helpers de texto --------------------------------------------------------

def medir(texto, fuente):
    bbox = fuente.getbbox(texto)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def medir_tracked(texto, fuente, tracking):
    total = 0
    for ch in texto:
        w, _ = medir(ch, fuente)
        total += w + tracking
    return total - tracking


def dibujar_tracked(draw, texto, fuente, color, x, y, tracking):
    cursor = x
    for ch in texto:
        draw.text((cursor, y), ch, font=fuente, fill=color)
        w, _ = medir(ch, fuente)
        cursor += w + tracking


def dibujar_centrado(draw, texto, fuente, color, y, w_canvas=W):
    w, _ = medir(texto, fuente)
    draw.text(((w_canvas - w) // 2, y), texto, font=fuente, fill=color)


def dibujar_lineas_centradas(draw, lineas, fuente, color, y_inicio, gap):
    """Dibuja varias lineas centradas, devuelve y final tras la ultima."""
    alto_linea = medir("Hg", fuente)[1] + gap
    for i, linea in enumerate(lineas):
        dibujar_centrado(draw, linea, fuente, color, y_inicio + i * alto_linea)
    return y_inicio + len(lineas) * alto_linea - gap


# --- Logo MIND WORLD blanco solido (extraido del cover canal) ----------------

def cargar_logo_mindworld_blanco(ancho):
    cover = Image.open(REPO / "podcast-cover.png").convert("RGB")
    logo_rgb = cover.crop((2200, 2380, 2880, 2880))
    h = int(ancho * logo_rgb.height / logo_rgb.width)
    logo = logo_rgb.resize((ancho, h), Image.LANCZOS).convert("RGBA")
    px = logo.load()
    vr, vg, vb = 23, 61, 48
    dist_max = 215.0
    for y in range(h):
        for x in range(ancho):
            r, g, b, _ = px[x, y]
            dist = ((r - vr) ** 2 + (g - vg) ** 2 + (b - vb) ** 2) ** 0.5
            t = min(1.0, dist / dist_max)
            # Logo blanco solido (no translucido como en covers podcast):
            # alpha alto proporcional a distancia al verde.
            px[x, y] = (255, 255, 255, int(t * 255))
    return logo


# --- Layout base (header + footer comun a todas las slides) ------------------

def slide_base(numero, total, logo):
    """Devuelve un lienzo con kicker top-left, paginacion top-right,
    logo MIND WORLD centrado abajo y footer @daniorozcopsicologo."""
    img = Image.new("RGB", (W, H), VERDE_OSCURO)
    d = ImageDraw.Draw(img)

    # Kicker top-left
    f_kicker = sans("Bold", 26)
    dibujar_tracked(d, "TE ESCRIBO · CARTA #1", f_kicker, BEIGE,
                    MARGEN, MARGEN + 6, 4)

    # Paginacion top-right
    f_pag = sans("Regular", 26)
    pag = f"{numero:02d} / {total:02d}"
    pw, _ = medir(pag, f_pag)
    d.text((W - MARGEN - pw, MARGEN + 6), pag, font=f_pag,
           fill=(BEIGE[0], BEIGE[1], BEIGE[2]))

    # Logo MIND WORLD centrado abajo
    img_rgba = img.convert("RGBA")
    img_rgba.paste(logo, ((W - logo.width) // 2, H - 200), logo)
    img = img_rgba.convert("RGB")
    d = ImageDraw.Draw(img)

    # Footer @daniorozcopsicologo · twimproject.com
    f_footer = sans("Regular", 24)
    dibujar_centrado(d, "@daniorozcopsicologo  ·  twimproject.com",
                     f_footer, CREMA, H - MARGEN - 10)

    return img, d


# --- Slides individuales -----------------------------------------------------

def slide_01(logo):
    """HOOK · Anti-promesa.

    Aquí no vas a recibir
    diagnósticos en quince segundos.

    Vas a recibir mecanismo.
    """
    img, d = slide_base(1, TOTAL_SLIDES, logo)
    f_titulo = serif(108)
    dibujar_lineas_centradas(d, [
        "Aquí no vas a recibir",
        "diagnósticos",
        "en quince segundos."
    ], f_titulo, CREMA, 320, 18)
    f_sub = sans("Regular", 44)
    dibujar_centrado(d, "Vas a recibir mecanismo.", f_sub, BEIGE, 830)
    img.save(DESTINO / "slide-01.png", "PNG", optimize=True)


def slide_02(logo):
    """DIAGNÓSTICO · Las redes sociales convierten la psicologia en…

    Llevo años viendo cómo las redes sociales
    convierten la psicología en

    un juego de etiquetas.
    """
    img, d = slide_base(2, TOTAL_SLIDES, logo)
    f_setup = sans("Regular", 42)
    dibujar_lineas_centradas(d, [
        "Llevo años viendo cómo",
        "las redes sociales convierten",
        "la psicología en"
    ], f_setup, CREMA, 350, 14)
    f_punch = serif(120)
    dibujar_lineas_centradas(d, [
        "un juego",
        "de etiquetas."
    ], f_punch, CREMA, 670, 16)
    img.save(DESTINO / "slide-02.png", "PNG", optimize=True)


def slide_03(logo):
    """PROBLEMA · 3 etiquetas + verdict.

    Apego ansioso.
    Narcisismo encubierto.
    Niño herido.

    Te dan un nombre
    y te quedas igual.
    """
    img, d = slide_base(3, TOTAL_SLIDES, logo)
    f_setup = sans("Regular", 44)
    dibujar_lineas_centradas(d, [
        "Apego ansioso.",
        "Narcisismo encubierto.",
        "Niño herido.",
    ], f_setup, BEIGE, 340, 14)
    f_punch = serif(110)
    dibujar_lineas_centradas(d, [
        "Te dan un nombre",
        "y te quedas igual."
    ], f_punch, CREMA, 680, 16)
    img.save(DESTINO / "slide-03.png", "PNG", optimize=True)


def slide_04(logo):
    """DAÑO · sabes el nombre pero no qué hacer.

    Sabes cómo se llama
    lo que te pasa,

    pero no por qué te pasa,

    ni qué hacer con ello.
    """
    img, d = slide_base(4, TOTAL_SLIDES, logo)
    f_body = serif(92)
    y = dibujar_lineas_centradas(d, [
        "Sabes cómo se llama",
        "lo que te pasa,"
    ], f_body, CREMA, 330, 12)
    f_body2 = serif(82)
    y2 = dibujar_lineas_centradas(d, [
        "pero no por qué te pasa,"
    ], f_body2, CREMA, y + 60, 12)
    f_italica = serif(80, italic=True)
    dibujar_lineas_centradas(d, [
        "ni qué hacer con ello."
    ], f_italica, BEIGE, y2 + 60, 12)
    img.save(DESTINO / "slide-04.png", "PNG", optimize=True)


def slide_05(logo):
    """CLIMAX · La promesa entera (el fragmento de la story crema, ampliado).

    Aquí vas a recibir mecanismo:

    Cómo funciona algo
    por dentro,
    de dónde viene,
    y qué puedes hacer
    para que deje de operar
    en automático.
    """
    img, d = slide_base(5, TOTAL_SLIDES, logo)
    f_lead = sans("Regular", 42)
    dibujar_centrado(d, "Aquí vas a recibir mecanismo:",
                     f_lead, BEIGE, 295)
    f_quote = serif(78)
    dibujar_lineas_centradas(d, [
        "Cómo funciona algo",
        "por dentro,",
        "de dónde viene,",
        "y qué puedes hacer",
        "para que deje de operar",
        "en automático.",
    ], f_quote, CREMA, 410, 6)
    img.save(DESTINO / "slide-05.png", "PNG", optimize=True)


def slide_06(logo):
    """SENTIDO · Para qué sirve la newsletter.

    Para que pares diez minutos
    a mirar algo de tu funcionamiento
    que normalmente no miras.

    A veces solo entender
    ya mueve cosas.
    """
    img, d = slide_base(6, TOTAL_SLIDES, logo)
    f_setup = sans("Regular", 44)
    y = dibujar_lineas_centradas(d, [
        "Para que pares diez minutos",
        "a mirar algo de tu funcionamiento",
        "que normalmente no miras."
    ], f_setup, CREMA, 360, 16)
    f_italica = serif(96, italic=True)
    dibujar_lineas_centradas(d, [
        "A veces solo entender",
        "ya mueve cosas.",
    ], f_italica, BEIGE, y + 90, 14)
    img.save(DESTINO / "slide-06.png", "PNG", optimize=True)


def slide_07(logo):
    """CTA · Suscríbete + fecha Carta #2.

    Una carta cada dos semanas.

    Sobre la mente, el cansancio,
    y lo que no se dice.

    twimproject.com/newsletter

    La próxima sale el martes 19 de mayo.
    """
    img, d = slide_base(7, TOTAL_SLIDES, logo)
    f_titulo = serif(110)
    dibujar_lineas_centradas(d, [
        "Una carta",
        "cada dos semanas."
    ], f_titulo, CREMA, 290, 16)
    f_sub = sans("Regular", 42)
    y = dibujar_lineas_centradas(d, [
        "Sobre la mente, el cansancio,",
        "y lo que no se dice."
    ], f_sub, CREMA, 580, 12)
    f_url = sans("Bold", 48)
    dibujar_centrado(d, "twimproject.com/newsletter",
                     f_url, BEIGE, y + 80)
    f_italica = serif(48, italic=True)
    dibujar_centrado(d, "La próxima sale el martes 19 de mayo.",
                     f_italica, BEIGE, y + 200)
    img.save(DESTINO / "slide-07.png", "PNG", optimize=True)


# --- Main --------------------------------------------------------------------

def main():
    DESTINO.mkdir(parents=True, exist_ok=True)
    logo = cargar_logo_mindworld_blanco(140)
    print(f"Logo MIND WORLD blanco preparado: {logo.size}")
    print(f"Fuentes: {FUENTES}")
    funciones = [slide_01, slide_02, slide_03, slide_04,
                 slide_05, slide_06, slide_07]
    for i, fn in enumerate(funciones, start=1):
        fn(logo)
        print(f"  OK slide-{i:02d}.png")
    print(f"Listo. {len(funciones)} slides en {DESTINO.relative_to(REPO)}")


if __name__ == "__main__":
    main()
