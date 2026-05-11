"""Genera las 3 portadas del E5 «Tu valor no está en su mirada».

Hereda el sistema visual establecido en el E5 original (autoexigencia,
ahora renumerado a E6 tras el reordenamiento del 11 may 2026) y en los
episodios NotebookLM E1-E4: foto autor + tipografía serif display +
jerarquía editorial sobre verde oscuro.

Outputs (todos en `contenido-rrss/podcast-e5-tu-valor-no-esta-en-su-mirada/`):
- cover-youtube.png   1280x720   horizontal (texto izq + foto der)
- cover-spotify.png   1400x1400  cuadrado (texto izq + foto der vertical)
- story-vertical.png  1080x1920  vertical (foto arriba + texto abajo)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# --- Configuracion del episodio ----------------------------------------------

CONTENIDO_EPISODIO = {
    "numero": "Ep.5",
    "kicker": "Psicología Aplicada",
    "titulo_lineas": ["TU VALOR NO ESTÁ", "EN SU MIRADA"],
    "subtitulo_par": "(el alivio de dejar de confundir amor con necesidad)",
    "pie": "DANIEL OROZCO  ·  @daniorozcopsicologo",
}

# --- Paleta TWIM -------------------------------------------------------------

VERDE_OSCURO = (23, 61, 48)        # #173D30
BEIGE = (194, 167, 139)            # #C2A78B
BEIGE_CLARO = (212, 192, 170)
CREMA = (245, 235, 220)            # casi blanco con calidez
BLANCO = (250, 246, 240)

# --- Paths -------------------------------------------------------------------

REPO = Path(__file__).resolve().parent.parent.parent
FOTO_AUTOR = REPO / "daniel-orozco-sillon.jpg"
DESTINO = REPO / "contenido-rrss" / "podcast-e5-tu-valor-no-esta-en-su-mirada"
FUENTES = Path("/root/.local/share/fonts")

PLAYFAIR_VF = FUENTES / "PlayfairDisplay-VF.ttf"
PLAYFAIR_ITALIC_VF = FUENTES / "PlayfairDisplay-Italic-VF.ttf"

# --- Fuentes -----------------------------------------------------------------

def serif(size, weight=700, italic=False):
    """Devuelve Playfair Display variable font con peso y estilo dados."""
    archivo = PLAYFAIR_ITALIC_VF if italic else PLAYFAIR_VF
    f = ImageFont.truetype(str(archivo), size)
    try:
        f.set_variation_by_axes([weight])
    except Exception:
        pass
    return f


def sans(weight, size):
    return ImageFont.truetype(str(FUENTES / f"BarlowCondensed-{weight}.ttf"), size)


# --- Helpers de texto --------------------------------------------------------

def medir(texto, fuente):
    bbox = fuente.getbbox(texto)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def medir_tracked(texto, fuente, tracking_px):
    total = 0
    for ch in texto:
        w, _ = medir(ch, fuente)
        total += w + tracking_px
    return total - tracking_px


def dibujar_tracked(draw, texto, fuente, color, x, y, tracking_px):
    cursor = x
    for ch in texto:
        draw.text((cursor, y), ch, font=fuente, fill=color)
        w, _ = medir(ch, fuente)
        cursor += w + tracking_px
    return cursor - x


# --- Foto: fade lateral hacia verde ------------------------------------------

def foto_con_fade_izq(foto, alto_destino, ancho_destino, fade_px):
    """Recorta y escala la foto al tamano destino y aplica fade
    horizontal en el borde izquierdo (de transparente a opaco)
    sobre `fade_px` para fundirla con el lienzo verde."""
    # Escalar a alto destino preservando ratio
    ratio = alto_destino / foto.height
    nuevo_ancho = int(foto.width * ratio)
    foto_e = foto.resize((nuevo_ancho, alto_destino), Image.LANCZOS)

    # Recortar centrado al ancho destino
    if nuevo_ancho > ancho_destino:
        izq = (nuevo_ancho - ancho_destino) // 2
        foto_e = foto_e.crop((izq, 0, izq + ancho_destino, alto_destino))
    else:
        # Si la foto es mas estrecha, padear con verde
        bg = Image.new("RGB", (ancho_destino, alto_destino), VERDE_OSCURO)
        bg.paste(foto_e, ((ancho_destino - nuevo_ancho) // 2, 0))
        foto_e = bg

    # Mascara alpha: gradiente horizontal de 0 a 255 en los primeros fade_px
    foto_rgba = foto_e.convert("RGBA")
    mask = Image.new("L", (ancho_destino, alto_destino), 255)
    md = ImageDraw.Draw(mask)
    for x in range(fade_px):
        alpha = int(255 * (x / fade_px))
        md.line([(x, 0), (x, alto_destino)], fill=alpha)
    foto_rgba.putalpha(mask)
    return foto_rgba


def foto_con_fade_abajo(foto, alto_destino, ancho_destino, fade_px):
    """Variante con fade en el borde inferior (para vertical donde
    foto va arriba y texto abajo)."""
    ratio_w = ancho_destino / foto.width
    ratio_h = alto_destino / foto.height
    ratio = max(ratio_w, ratio_h)
    new_w, new_h = int(foto.width * ratio), int(foto.height * ratio)
    foto_e = foto.resize((new_w, new_h), Image.LANCZOS)
    # Recorte centrado
    izq = (new_w - ancho_destino) // 2
    arr = (new_h - alto_destino) // 2
    foto_e = foto_e.crop((izq, arr, izq + ancho_destino, arr + alto_destino))

    foto_rgba = foto_e.convert("RGBA")
    mask = Image.new("L", (ancho_destino, alto_destino), 255)
    md = ImageDraw.Draw(mask)
    for y in range(fade_px):
        alpha = int(255 * (1 - y / fade_px))
        md.line([(0, alto_destino - fade_px + y),
                 (ancho_destino, alto_destino - fade_px + y)], fill=alpha)
    foto_rgba.putalpha(mask)
    return foto_rgba


# --- Logo MIND WORLD recortado del cover canal --------------------------------

def cargar_logo_mindworld():
    cover = Image.open(REPO / "podcast-cover.png").convert("RGB")
    return cover.crop((2200, 2380, 2880, 2880))


def logo_blanco_translucido(logo_rgb, ancho, opacidad_max=225):
    """Convierte el logo a blanco semi-translucido preservando el
    anti-aliasing original. El alpha de cada pixel es proporcional
    a su distancia euclidea al verde oscuro de fondo del cover canal:
    pixeles verdes -> alpha 0 (transparentes), pixeles beige -> alpha
    cercano a opacidad_max. Asi se evita el halo blanco que produce
    una binarizacion dura."""
    h = int(ancho * logo_rgb.height / logo_rgb.width)
    logo = logo_rgb.resize((ancho, h), Image.LANCZOS).convert("RGBA")
    px = logo.load()
    vr, vg, vb = 23, 61, 48  # verde oscuro #173D30 (fondo cover canal)
    # Distancia de referencia: verde oscuro vs beige #C2A78B = ~226.
    # Usamos 215 como techo para que el beige puro llegue casi al maximo.
    dist_max = 215.0
    for y in range(h):
        for x in range(ancho):
            r, g, b, _ = px[x, y]
            dist = ((r - vr) ** 2 + (g - vg) ** 2 + (b - vb) ** 2) ** 0.5
            t = min(1.0, dist / dist_max)
            px[x, y] = (255, 255, 255, int(t * opacidad_max))
    return logo


# --- Lienzo y separador ------------------------------------------------------

def lienzo(w, h):
    return Image.new("RGB", (w, h), VERDE_OSCURO)


def separador_horizontal(draw, x, y, ancho, color, grosor=2):
    draw.rectangle([(x, y), (x + ancho, y + grosor)], fill=color)


# --- Bloque editorial reusable -----------------------------------------------

def render_bloque_editorial(img, ep, x_izq, ancho_disp, y_centro,
                            f_kicker, kicker_track, f_titulo, gap_titulo,
                            f_subtitulo, separador_w, color_titulo, color_meta):
    """Dibuja eyebrow + separador + titulo + subtitulo paréntesis
    centrados verticalmente alrededor de y_centro. Devuelve el rect
    dibujado para que la funcion llamante coloque pie debajo."""
    d = ImageDraw.Draw(img)

    # Calcular alto total del bloque para centrar
    eyebrow_h = medir(ep["numero"] + ep["kicker"], f_kicker)[1]
    titulo_alto_linea = medir("EM", f_titulo)[1] + gap_titulo
    titulo_total = titulo_alto_linea * len(ep["titulo_lineas"]) - gap_titulo
    sub_h = medir(ep["subtitulo_par"], f_subtitulo)[1]
    espaciado_eyebrow_separador = 18
    espaciado_separador_titulo = 60
    espaciado_titulo_sub = 50
    grosor_sep = 3
    total = (eyebrow_h + espaciado_eyebrow_separador + grosor_sep
             + espaciado_separador_titulo + titulo_total
             + espaciado_titulo_sub + sub_h)
    y_inicio = y_centro - total // 2

    # Eyebrow: TWIM PODCAST (linea 1) + Ep.X · Psicología (linea 2)
    f_kicker_top = sans("Bold", f_kicker.size)
    dibujar_tracked(d, "TWIM PODCAST", f_kicker_top, color_meta,
                     x_izq, y_inicio, kicker_track)
    y_eyebrow2 = y_inicio + medir("TWIM PODCAST", f_kicker_top)[1] + 8
    sub_kicker = f"{ep['numero']} · {ep['kicker']}"
    dibujar_tracked(d, sub_kicker, f_kicker, color_meta,
                     x_izq, y_eyebrow2, max(2, kicker_track // 2))

    # Separador
    y_sep = y_eyebrow2 + medir(sub_kicker, f_kicker)[1] + espaciado_eyebrow_separador
    separador_horizontal(d, x_izq, y_sep, separador_w, color_meta, grosor_sep)

    # Titulo
    y_titulo = y_sep + grosor_sep + espaciado_separador_titulo
    for i, linea in enumerate(ep["titulo_lineas"]):
        d.text((x_izq, y_titulo + i * titulo_alto_linea),
               linea, font=f_titulo, fill=color_titulo)

    # Subtitulo paréntesis (cursiva)
    y_sub = y_titulo + titulo_total + espaciado_titulo_sub
    d.text((x_izq, y_sub), ep["subtitulo_par"], font=f_subtitulo, fill=color_meta)

    return y_sub + sub_h  # bottom y


# --- 1. YouTube horizontal 1280x720 ------------------------------------------

def generar_youtube(foto_orig, logo_rgb):
    W, H = 1280, 720
    img = lienzo(W, H)

    # Foto a la derecha ocupando ~50% con fade izq de 220px
    foto_w = int(W * 0.55)
    foto = foto_con_fade_izq(foto_orig, H, foto_w, fade_px=220)
    img.paste(foto, (W - foto_w, 0), foto)

    # Bloque editorial izquierda
    x_izq = 70
    ancho_disp = int(W * 0.45) - 70
    f_kicker = sans("Medium", 22)
    f_titulo = serif(78, weight=700)
    f_sub = serif(28, weight=400, italic=True)
    bottom = render_bloque_editorial(
        img, CONTENIDO_EPISODIO, x_izq, ancho_disp, H // 2,
        f_kicker=f_kicker, kicker_track=4,
        f_titulo=f_titulo, gap_titulo=14,
        f_subtitulo=f_sub, separador_w=70,
        color_titulo=CREMA, color_meta=BEIGE)

    # Pie inferior izquierda
    d = ImageDraw.Draw(img)
    f_pie = sans("Bold", 18)
    dibujar_tracked(d, CONTENIDO_EPISODIO["pie"], f_pie, BEIGE,
                     x_izq, H - 50, 3)

    # Logo MIND WORLD esquina inf derecha (sobre foto, blanco translucido)
    logo = logo_blanco_translucido(logo_rgb, 130)
    img.paste(logo, (W - 130 - 35, H - logo.height - 30), logo)

    salida = DESTINO / "cover-youtube.png"
    img.save(salida, "PNG", optimize=True)
    print(f"OK cover-youtube.png    -> {salida.relative_to(REPO)} ({W}x{H})")


# --- 2. Spotify cuadrado 1400x1400 -------------------------------------------

def generar_spotify(foto_orig, logo_rgb):
    W, H = 1400, 1400
    img = lienzo(W, H)

    # Foto a la derecha ocupando 50% con fade izq
    foto_w = int(W * 0.50)
    foto = foto_con_fade_izq(foto_orig, H, foto_w, fade_px=240)
    img.paste(foto, (W - foto_w, 0), foto)

    # Bloque editorial izquierda
    x_izq = 90
    ancho_disp = int(W * 0.50) - 90
    f_kicker = sans("Medium", 28)
    f_titulo = serif(105, weight=700)
    f_sub = serif(36, weight=400, italic=True)
    render_bloque_editorial(
        img, CONTENIDO_EPISODIO, x_izq, ancho_disp, H // 2,
        f_kicker=f_kicker, kicker_track=5,
        f_titulo=f_titulo, gap_titulo=20,
        f_subtitulo=f_sub, separador_w=90,
        color_titulo=CREMA, color_meta=BEIGE)

    # Pie inferior izquierda
    d = ImageDraw.Draw(img)
    f_pie = sans("Bold", 24)
    dibujar_tracked(d, CONTENIDO_EPISODIO["pie"], f_pie, BEIGE,
                     x_izq, H - 70, 4)

    # Logo MIND WORLD esquina inf derecha
    logo = logo_blanco_translucido(logo_rgb, 170)
    img.paste(logo, (W - 170 - 50, H - logo.height - 50), logo)

    salida = DESTINO / "cover-spotify.png"
    img.save(salida, "PNG", optimize=True)
    print(f"OK cover-spotify.png    -> {salida.relative_to(REPO)} ({W}x{H})")


# --- 3. Story vertical 1080x1920 --------------------------------------------

def generar_story(foto_orig, logo_rgb):
    W, H = 1080, 1920
    img = lienzo(W, H)

    # Foto arriba ocupando ~58% con fade abajo
    foto_h = int(H * 0.58)
    foto = foto_con_fade_abajo(foto_orig, foto_h, W, fade_px=200)
    img.paste(foto, (0, 0), foto)

    # Bloque editorial CENTRADO en la mitad inferior (texto centrado)
    x_izq = 90
    ancho_disp = W - 180
    y_centro_bloque = int(H * 0.78)
    f_kicker = sans("Medium", 30)
    f_titulo = serif(88, weight=700)  # reducido de 115 a 88 para que «TU VALOR NO ESTÁ» quepa en 1080
    f_sub = serif(34, weight=400, italic=True)

    # Para story: render centrado horizontalmente (no alineado izq como otros)
    d = ImageDraw.Draw(img)
    ep = CONTENIDO_EPISODIO

    # Eyebrow centrado
    f_kicker_top = sans("Bold", 32)
    eyebrow1 = "TWIM PODCAST"
    eyebrow2 = f"{ep['numero']} · {ep['kicker']}"
    w1 = medir_tracked(eyebrow1, f_kicker_top, 6)
    w2 = medir_tracked(eyebrow2, f_kicker, 4)
    titulo_alto = medir("EM", f_titulo)[1] + 22
    titulo_total = titulo_alto * len(ep["titulo_lineas"]) - 22
    sub_h = medir(ep["subtitulo_par"], f_sub)[1]
    eyebrow_h = medir(eyebrow1, f_kicker_top)[1] + 12 + medir(eyebrow2, f_kicker)[1]
    grosor_sep = 4
    total = eyebrow_h + 22 + grosor_sep + 65 + titulo_total + 55 + sub_h
    y0 = y_centro_bloque - total // 2

    dibujar_tracked(d, eyebrow1, f_kicker_top, BEIGE,
                     (W - w1) // 2, y0, 6)
    y0_e2 = y0 + medir(eyebrow1, f_kicker_top)[1] + 12
    dibujar_tracked(d, eyebrow2, f_kicker, BEIGE,
                     (W - w2) // 2, y0_e2, 4)

    y_sep = y0_e2 + medir(eyebrow2, f_kicker)[1] + 22
    sep_w = 90
    separador_horizontal(d, (W - sep_w) // 2, y_sep, sep_w, BEIGE, grosor_sep)

    y_titulo = y_sep + grosor_sep + 65
    for i, linea in enumerate(ep["titulo_lineas"]):
        wt = medir(linea, f_titulo)[0]
        d.text(((W - wt) // 2, y_titulo + i * titulo_alto),
               linea, font=f_titulo, fill=CREMA)

    y_sub = y_titulo + titulo_total + 55
    ws = medir(ep["subtitulo_par"], f_sub)[0]
    d.text(((W - ws) // 2, y_sub), ep["subtitulo_par"], font=f_sub, fill=BEIGE)

    # Pie inferior centrado
    f_pie = sans("Bold", 26)
    pw = medir_tracked(ep["pie"], f_pie, 4)
    dibujar_tracked(d, ep["pie"], f_pie, BEIGE,
                     (W - pw) // 2, H - 90, 4)

    # Logo MIND WORLD esquina inf derecha (mas chico que los otros)
    logo = logo_blanco_translucido(logo_rgb, 130)
    img.paste(logo, (W - 130 - 50, H - logo.height - 130), logo)

    salida = DESTINO / "story-vertical.png"
    img.save(salida, "PNG", optimize=True)
    print(f"OK story-vertical.png   -> {salida.relative_to(REPO)} ({W}x{H})")


# --- Main --------------------------------------------------------------------

def main():
    foto = Image.open(FOTO_AUTOR).convert("RGB")
    print(f"Foto autor: {FOTO_AUTOR.name} {foto.size}")
    logo = cargar_logo_mindworld()
    print(f"Logo MIND WORLD recortado: {logo.size}")
    print()
    generar_youtube(foto, logo)
    generar_spotify(foto, logo)
    generar_story(foto, logo)
    print("Listo.")


if __name__ == "__main__":
    main()
