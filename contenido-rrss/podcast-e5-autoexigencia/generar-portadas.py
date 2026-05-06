"""Genera las 3 portadas del E5 reutilizando los elementos visuales del cover canal.

Reusa `podcast-cover.png` (raíz repo) como banco de elementos icónicos:
los sillones y el logo MIND WORLD PROJECT. Compone tres lienzos nuevos
(Spotify cuadrado, YouTube horizontal, video-fondo 16:9) con la jerarquía
editorial que define `specs-portada.md`.

Uso: `python3 generar-portadas.py` desde la raíz del repo o desde la
carpeta del episodio. Sobrescribe `cover-spotify.png`, `cover-youtube.png`
y `video-fondo.png` en `contenido-rrss/podcast-e5-autoexigencia/`.

Para episodios siguientes: copiar este script a la carpeta del nuevo
episodio y cambiar el bloque CONTENIDO_EPISODIO de abajo.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# --- Configuración del episodio ----------------------------------------------

CONTENIDO_EPISODIO = {
    "numero": "E5",
    "titulo_l1": "EL MANDATO",
    "titulo_l2": "DE NO PARAR",
    "subtitulo": "Autoexigencia y culpa de descansar",
    "pie_corto": "Daniel Orozco Abia · CV11515",
    "pie_largo": "Daniel Orozco Abia · Psicólogo CV11515 · Valencia",
}

# --- Paleta TWIM (CLAUDE.md) -------------------------------------------------

VERDE_OSCURO = (23, 61, 48)
VERDE_MEDIO = (38, 92, 75)
BEIGE = (194, 167, 139)
CREMA = (253, 252, 250)
BLANCO_HUMO = (245, 242, 236)

# --- Paths -------------------------------------------------------------------

REPO = Path(__file__).resolve().parent.parent.parent
COVER_CANAL = REPO / "podcast-cover.png"
DESTINO = REPO / "contenido-rrss" / "podcast-e5-autoexigencia"
FUENTES = Path("/root/.local/share/fonts")

# --- Carga de fuentes --------------------------------------------------------

def font(weight, size):
    archivo = FUENTES / f"BarlowCondensed-{weight}.ttf"
    return ImageFont.truetype(str(archivo), size)


# --- Recorte de elementos del cover canal ------------------------------------

def cargar_elementos_canal():
    """Recorta sillon y logo del cover canal 3000x3000."""
    cover = Image.open(COVER_CANAL).convert("RGB")
    # Coordenadas medidas sobre cover 3000x3000 (verde solido + dibujo a linea):
    # sillon ocupa franja vertical aprox y=1180..2230, x=360..2640.
    sillon = cover.crop((360, 1180, 2640, 2230))
    # Logo MIND WORLD esquina inferior derecha aprox y=2380..2880, x=2200..2880.
    logo = cover.crop((2200, 2380, 2880, 2880))
    return sillon, logo


# --- Helpers de texto --------------------------------------------------------

def medir(texto, fuente):
    bbox = fuente.getbbox(texto)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def dibujar_centrado(draw, texto, fuente, color, y, ancho_lienzo):
    w, _ = medir(texto, fuente)
    draw.text(((ancho_lienzo - w) // 2, y), texto, font=fuente, fill=color)


def dibujar_tracked(draw, texto, fuente, color, x, y, tracking_px):
    """Dibuja con letter-spacing manual (Pillow no lo trae nativo)."""
    cursor = x
    for ch in texto:
        draw.text((cursor, y), ch, font=fuente, fill=color)
        w, _ = medir(ch, fuente)
        cursor += w + tracking_px
    return cursor - x  # ancho total renderizado


def medir_tracked(texto, fuente, tracking_px):
    total = 0
    for ch in texto:
        w, _ = medir(ch, fuente)
        total += w + tracking_px
    return total - tracking_px


def dibujar_tracked_centrado(draw, texto, fuente, color, y, ancho_lienzo, tracking_px):
    w = medir_tracked(texto, fuente, tracking_px)
    dibujar_tracked(draw, texto, fuente, color, (ancho_lienzo - w) // 2, y, tracking_px)


# --- Composición -------------------------------------------------------------

def lienzo(ancho, alto):
    """Lienzo verde oscuro liso (sin gradiente fuerte; coherente con canal)."""
    return Image.new("RGB", (ancho, alto), VERDE_OSCURO)


def pegar_redimensionado(base, elem, dest_w, dest_h, x, y):
    """Pega un elemento del cover canal redimensionado en (x,y).
    Como el cover canal tiene fondo verde igual al lienzo nuevo,
    el blending es natural sin necesidad de transparencia."""
    redim = elem.resize((dest_w, dest_h), Image.LANCZOS)
    base.paste(redim, (x, y))


# --- 1. Cover Spotify 1400x1400 ----------------------------------------------

def generar_spotify(sillon, logo):
    W, H = 1400, 1400
    img = lienzo(W, H)
    d = ImageDraw.Draw(img)
    ep = CONTENIDO_EPISODIO

    # Eyebrow superior: "TWIM PODCAST"
    f_eyebrow = font("Medium", 52)
    dibujar_tracked_centrado(d, "TWIM PODCAST", f_eyebrow, BEIGE, 110, W, 6)

    # Numero episodio grande pero sutil
    f_ep = font("ExtraBold", 130)
    ep_color = (BEIGE[0], BEIGE[1], BEIGE[2])
    # Mas tenue: lo composito sobre el verde con menor opacidad via overlay manual
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    ep_w, ep_h = medir(ep["numero"], f_ep)
    ld.text(((W - ep_w) // 2, 175), ep["numero"], font=f_ep,
            fill=(*ep_color, 100))  # ~40% opacidad
    img = Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB")
    d = ImageDraw.Draw(img)

    # Titulo principal dos lineas
    f_titulo = font("Bold", 130)
    dibujar_centrado(d, ep["titulo_l1"], f_titulo, CREMA, 360, W)
    dibujar_centrado(d, ep["titulo_l2"], f_titulo, CREMA, 360 + 125, W)

    # Subtitulo
    f_sub = font("Regular", 50)
    dibujar_centrado(d, ep["subtitulo"], f_sub, BEIGE, 660, W)

    # Sillones (recorte del canal) centrados
    # Sillon original 2280x1050 -> escalar a ~860x395 para encajar
    sw, sh = 860, int(860 * sillon.height / sillon.width)
    pegar_redimensionado(img, sillon, sw, sh, (W - sw) // 2, 780)

    # Pie centrado abajo
    f_pie = font("Regular", 32)
    dibujar_centrado(d, ep["pie_largo"], f_pie, BEIGE, H - 130, W)

    # Logo MIND WORLD abajo centrado-derecha pequeno
    lw = 180
    lh = int(lw * logo.height / logo.width)
    img.paste(logo.resize((lw, lh), Image.LANCZOS),
              (W - lw - 80, H - lh - 60))

    salida = DESTINO / "cover-spotify.png"
    img.save(salida, "PNG", optimize=True)
    print(f"OK cover-spotify.png -> {salida.relative_to(REPO)} ({W}x{H})")


# --- 2. Cover YouTube 1280x720 -----------------------------------------------

def generar_youtube(sillon, logo):
    W, H = 1280, 720
    img = lienzo(W, H)
    d = ImageDraw.Draw(img)
    ep = CONTENIDO_EPISODIO

    # Sillones a la derecha (40% del ancho)
    panel_d_x = int(W * 0.60)
    panel_d_w = W - panel_d_x
    sw = int(panel_d_w * 0.85)
    sh = int(sw * sillon.height / sillon.width)
    sx = panel_d_x + (panel_d_w - sw) // 2
    sy = (H - sh) // 2 - 20
    pegar_redimensionado(img, sillon, sw, sh, sx, sy)

    # Texto a la izquierda (60% del ancho)
    margen_x = 80
    # Eyebrow
    f_eyebrow = font("Medium", 30)
    dibujar_tracked(d, "TWIM PODCAST · " + ep["numero"], f_eyebrow,
                     BEIGE, margen_x, 100, 4)

    # Titulo dos lineas
    f_titulo = font("Bold", 105)
    d.text((margen_x, 165), ep["titulo_l1"], font=f_titulo, fill=CREMA)
    d.text((margen_x, 165 + 100), ep["titulo_l2"], font=f_titulo, fill=CREMA)

    # Subtitulo
    f_sub = font("Regular", 38)
    d.text((margen_x, 165 + 100 + 115), ep["subtitulo"], font=f_sub, fill=BEIGE)

    # Pie
    f_pie = font("Regular", 24)
    d.text((margen_x, H - 70), ep["pie_corto"], font=f_pie, fill=BEIGE)

    # Logo MIND WORLD esquina inferior derecha pequeno
    lw = 120
    lh = int(lw * logo.height / logo.width)
    img.paste(logo.resize((lw, lh), Image.LANCZOS),
              (W - lw - 40, H - lh - 30))

    salida = DESTINO / "cover-youtube.png"
    img.save(salida, "PNG", optimize=True)
    print(f"OK cover-youtube.png -> {salida.relative_to(REPO)} ({W}x{H})")


# --- 3. Video-fondo 1920x1080 (pantalla durante reproduccion) ----------------

def generar_video_fondo(sillon, logo):
    W, H = 1920, 1080
    img = lienzo(W, H)
    d = ImageDraw.Draw(img)
    ep = CONTENIDO_EPISODIO

    # Diseno: eyebrow+titulo en tercio superior, sillon en tercio medio,
    # tercio inferior LIBRE para subtitulos (zona de seguridad ~y>720).

    # Eyebrow superior centrado
    f_eyebrow = font("Medium", 40)
    dibujar_tracked_centrado(d, "TWIM PODCAST · " + ep["numero"], f_eyebrow,
                              BEIGE, 90, W, 5)

    # Titulo dos lineas centrado, mas pequeno que YouTube (no compite con subs)
    f_titulo = font("Bold", 110)
    dibujar_centrado(d, ep["titulo_l1"], f_titulo, CREMA, 165, W)
    dibujar_centrado(d, ep["titulo_l2"], f_titulo, CREMA, 165 + 105, W)

    # Subtitulo
    f_sub = font("Regular", 42)
    dibujar_centrado(d, ep["subtitulo"], f_sub, BEIGE, 165 + 105 + 130, W)

    # Sillon centrado en tercio medio (sin invadir zona inferior)
    sw = 720
    sh = int(sw * sillon.height / sillon.width)
    sx = (W - sw) // 2
    sy = 575
    pegar_redimensionado(img, sillon, sw, sh, sx, sy)

    # Logo MIND WORLD esquina inferior derecha (fuera de zona subs centrada)
    lw = 130
    lh = int(lw * logo.height / logo.width)
    img.paste(logo.resize((lw, lh), Image.LANCZOS),
              (W - lw - 60, H - lh - 50))

    # Marca de zona segura para subtitulos NO se dibuja (solo reservada visualmente)

    salida = DESTINO / "video-fondo.png"
    img.save(salida, "PNG", optimize=True)
    print(f"OK video-fondo.png -> {salida.relative_to(REPO)} ({W}x{H})")


# --- Main --------------------------------------------------------------------

def main():
    print(f"Repo: {REPO}")
    print(f"Cover canal: {COVER_CANAL}")
    sillon, logo = cargar_elementos_canal()
    print(f"Sillon recortado: {sillon.size}  ·  Logo: {logo.size}")
    generar_spotify(sillon, logo)
    generar_youtube(sillon, logo)
    generar_video_fondo(sillon, logo)
    print("Listo.")


if __name__ == "__main__":
    main()
