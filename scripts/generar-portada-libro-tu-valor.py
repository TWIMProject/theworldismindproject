#!/usr/bin/env python3
"""
Genera la portada del libro «Tu valor no está en su mirada» para Amazon KDP.

VERSIÓN 2 · CONCEPTO C · «La llave dentro» (elegido por Daniel el 14 may 2026
tras descarte de la v1 por no cumplir el criterio dopamina-comercial).

Diseño: documentado en `documentos-internos/libro-tu-valor-no-esta-en-su-mirada/
portada/conceptos-portada-v2.md` §4 y en `brief-diseno-portada-v2-concepto-c.md`.

Produce dos PDFs:

1. `portada-front-preview.pdf` · solo portada delantera (6×9"), preview.
2. `portada-wraparound-kdp.pdf` · wraparound completo back+spine+front KDP.

CARACTERÍSTICA CRÍTICA · El concepto C requiere una **ilustración real de la
llave dorada con cordel**. Esta v2 incluye un **placeholder visual** centrado
en la portada (rectángulo punteado con texto «AQUÍ ILUSTRACIÓN LLAVE») para
que el diseñador o el flujo IA generativa (Midjourney, DALL-E, Adobe Firefly)
encaje la ilustración real encima. Sin la ilustración, esta v2 NO debe subirse
a KDP — funciona como maqueta de composición y tipografía.

Asunción de páginas: 185 (provisional, punto medio del rango 170-200
estimado tras maquetación con Lora 11pt interlineado 1.4 + preliminares
+ apéndice 21 días + 3 escenas adicionales). El ancho del lomo cambia
cuando se conozca el conteo final tras maquetación. Para recalcular,
modificar la constante NUM_PAGES al inicio y volver a ejecutar el script.

Reproducibilidad: `python3 scripts/generar-portada-libro-tu-valor.py`
"""

import random
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

# ==============================================================================
# CONFIGURACIÓN
# ==============================================================================

NUM_PAGES = 185  # provisional (estimación tras maquetación Word: 170-200 págs
                 # con Lora 11pt interlineado 1.4 + preliminares + apéndice +
                 # 3 escenas adicionales). Recalcular cuando Daniel termine
                 # la maquetación real en Word y conozca el conteo exacto.

# Paleta Concepto C · «La llave dentro» (conceptos-portada-v2.md §4)
CREAM_BG = HexColor("#F4EDE0")           # fondo cálido principal
CREAM_LIGHT = HexColor("#FAF6EF")        # tono más claro para áreas internas
GREEN_BOTELLA = HexColor("#1F4A3A")      # verde botella (NO el TWIM #173D30)
GREEN_BOTELLA_SOFT = HexColor("#2C5A48")
GOLD = HexColor("#C19E5A")               # dorado de la llave / acentos
TEXT_SOFT = HexColor("#3D3530")          # negro suave editorial

# Paleta TWIM original (mantenida por si se quiere comparar)
GREEN_DARK_TWIM = HexColor("#173D30")
BEIGE_TWIM = HexColor("#C2A78B")

# Dimensiones físicas (Amazon KDP tapa blanda 6×9")
TRIM_W_IN = 6.0
TRIM_H_IN = 9.0
BLEED_IN = 0.125

# Ancho del lomo según fórmula KDP: páginas × 0.002252" (papel blanco crema)
SPINE_W_IN = NUM_PAGES * 0.002252

# Wraparound (back + spine + front) con sangrado
WRAP_W_IN = TRIM_W_IN + SPINE_W_IN + TRIM_W_IN + 2 * BLEED_IN
WRAP_H_IN = TRIM_H_IN + 2 * BLEED_IN

WRAP_W = WRAP_W_IN * inch
WRAP_H = WRAP_H_IN * inch
BLEED = BLEED_IN * inch
TRIM_W = TRIM_W_IN * inch
TRIM_H = TRIM_H_IN * inch
SPINE_W = SPINE_W_IN * inch

# Coordenadas (reportlab: origen bottom-left)
BACK_X = BLEED                          # comienzo de back cover (tras sangrado izq)
BACK_RIGHT = BACK_X + TRIM_W
SPINE_X = BACK_RIGHT
SPINE_RIGHT = SPINE_X + SPINE_W
FRONT_X = SPINE_RIGHT
FRONT_RIGHT = FRONT_X + TRIM_W

# Zona segura interior (KDP recomienda 0.5" desde el borde del trim)
SAFE_MARGIN = 0.5 * inch

# ==============================================================================
# HELPERS
# ==============================================================================


def draw_wrapped(c, text, x, y, max_width, font_name, font_size,
                 leading, fill=None, align="left"):
    """Texto con line-wrap manual. Devuelve la coordenada `y` final tras el último renglón.

    Si `fill` es None, usa TEXT_SOFT (negro suave editorial) como color por
    defecto. Se evita poner TEXT_SOFT como valor por defecto en la firma
    para no acoplar la firma a una constante global del módulo.
    """
    if fill is None:
        fill = TEXT_SOFT
    c.setFillColor(fill)
    c.setFont(font_name, font_size)
    words = text.split()
    line = ""
    lines = []
    for w in words:
        prueba = (line + " " + w).strip()
        if c.stringWidth(prueba, font_name, font_size) <= max_width:
            line = prueba
        else:
            if line:
                lines.append(line)
            line = w
    if line:
        lines.append(line)
    for ln in lines:
        if align == "center":
            tw = c.stringWidth(ln, font_name, font_size)
            c.drawString(x + (max_width - tw) / 2, y, ln)
        elif align == "right":
            tw = c.stringWidth(ln, font_name, font_size)
            c.drawString(x + max_width - tw, y, ln)
        else:
            c.drawString(x, y, ln)
        y -= leading
    return y


# ==============================================================================
# ILUSTRACIÓN DE LA LLAVE (v1 vectorial procedural)
# ==============================================================================


def draw_key(c, box_x, box_y, box_size):
    """Dibuja una llave vertical estilizada con cordel dentro de un cuadrado.

    Coherente con `brief-diseno-portada-v2-concepto-c.md` §4 · anatomía
    cabeza · tija · paletón, trazo verde botella, relleno dorado mate.

    Composición:
      - Cabeza circular en la parte superior del cuadrado (aprox 40% de
        altura). Anillo interior (hueco) por donde pasa el cordel.
      - Cordel saliendo del anillo, cayendo a la izquierda en curva bezier
        suave.
      - Tija vertical estrecha bajando desde la base de la cabeza.
      - Paletón con dos dientes geométricos asomando a la derecha de la
        base de la tija.

    Args:
        c: canvas reportlab.
        box_x, box_y: esquina inferior-izquierda del cuadrado contenedor.
        box_size: lado del cuadrado (la llave se inscribe centrada).
    """
    # Centro horizontal del cuadrado (eje vertical de la llave)
    cx = box_x + box_size / 2

    # Cabeza · círculo dorado con borde verde botella, anillo interior vacío.
    head_radius = box_size * 0.20
    head_cy = box_y + box_size * 0.72        # cabeza alta dentro del cuadrado
    ring_radius = head_radius * 0.46         # hueco proporcional

    # Sombra muy sutil de la cabeza (da volumen sin convertir en realismo)
    c.saveState()
    c.setFillColor(HexColor("#000000"))
    c.setFillAlpha(0.06)
    c.circle(cx + 1.2, head_cy - 1.2, head_radius + 0.5, fill=1, stroke=0)
    c.restoreState()

    # Cabeza (relleno dorado mate con borde verde botella)
    c.setFillColor(GOLD)
    c.setStrokeColor(GREEN_BOTELLA)
    c.setLineWidth(1.6)
    c.circle(cx, head_cy, head_radius, fill=1, stroke=1)

    # Anillo interior (hueco · se rellena con el color de fondo para «vaciar»)
    c.setFillColor(CREAM_BG)
    c.setStrokeColor(GREEN_BOTELLA)
    c.setLineWidth(1.2)
    c.circle(cx, head_cy, ring_radius, fill=1, stroke=1)

    # Tija · rectángulo vertical desde la base de la cabeza hacia abajo.
    # Conecta visualmente con la cabeza (solapa unos puntos).
    tija_w = head_radius * 0.32              # ancho de la tija
    tija_top = head_cy - head_radius + 2     # solapa con la cabeza
    tija_bottom = box_y + box_size * 0.18    # llega cerca del fondo del cuadrado
    tija_h = tija_top - tija_bottom

    c.setFillColor(GOLD)
    c.setStrokeColor(GREEN_BOTELLA)
    c.setLineWidth(1.4)
    c.rect(cx - tija_w / 2, tija_bottom, tija_w, tija_h,
           fill=1, stroke=1)

    # Paletón · dos dientes rectangulares asomando a la derecha de la tija.
    # Diente 1 (el más bajo, más cercano a la punta de la tija)
    tooth_h = tija_w * 1.1
    tooth_w = head_radius * 0.55
    tooth_x = cx + tija_w / 2 - 0.5          # arranca pegado a la tija
    tooth1_y = tija_bottom + tooth_h * 0.4

    c.setFillColor(GOLD)
    c.setStrokeColor(GREEN_BOTELLA)
    c.setLineWidth(1.3)
    c.rect(tooth_x, tooth1_y, tooth_w, tooth_h,
           fill=1, stroke=1)

    # Diente 2 (más arriba, ligeramente más estrecho)
    tooth2_y = tooth1_y + tooth_h * 2.3
    tooth2_w = tooth_w * 0.75
    c.rect(tooth_x, tooth2_y, tooth2_w, tooth_h,
           fill=1, stroke=1)

    # Cordel · curva bezier que sale del anillo de la cabeza por arriba
    # y cae a la izquierda formando un arco suave. Sin nudo barroco · línea
    # limpia que sugiere movimiento natural.
    c.saveState()
    c.setStrokeColor(BEIGE_TWIM)             # cordel beige cálido
    c.setLineWidth(1.3)
    c.setLineCap(1)                          # extremos redondeados

    # Punto de salida del cordel: parte superior del anillo
    rope_start_x = cx - ring_radius * 0.4
    rope_start_y = head_cy + ring_radius - 0.8

    # Control 1 (sale hacia arriba-izquierda)
    rope_c1_x = cx - head_radius * 1.6
    rope_c1_y = head_cy + head_radius * 1.4

    # Control 2 (curva de bajada)
    rope_c2_x = cx - head_radius * 2.4
    rope_c2_y = head_cy + head_radius * 0.3

    # Punto final (cae unos puntos por debajo del lado izquierdo de la cabeza)
    rope_end_x = cx - head_radius * 1.8
    rope_end_y = head_cy - head_radius * 0.6

    c.bezier(rope_start_x, rope_start_y,
             rope_c1_x, rope_c1_y,
             rope_c2_x, rope_c2_y,
             rope_end_x, rope_end_y)

    # Pequeño remate al final del cordel (un punto/nudo simple)
    c.setFillColor(BEIGE_TWIM)
    c.setStrokeColor(BEIGE_TWIM)
    c.circle(rope_end_x, rope_end_y, 1.6, fill=1, stroke=0)

    c.restoreState()


# ==============================================================================
# DIBUJO DE PORTADA DELANTERA (front cover)
# ==============================================================================


def draw_front(c, x_offset, y_offset):
    """Dibuja la portada delantera · Concepto C «La llave dentro».

    x_offset/y_offset = esquina inferior-izquierda del front cover
    (con sangrado incluido si aplica).
    """

    # ---------- Fondo crema cálido (concepto C) ----------
    c.setFillColor(CREAM_BG)
    c.rect(x_offset - 1, y_offset - 1,
           TRIM_W + BLEED + 2, TRIM_H + 2 * BLEED + 2,
           fill=1, stroke=0)

    # Textura de papel mate sutil · puntos aleatorios muy claros
    # (simula granulado · el diseñador puede sustituir por textura PNG real)
    c.setFillColor(CREAM_LIGHT)
    c.setFillAlpha(0.35)
    random.seed(7)
    for _ in range(420):
        px = x_offset + random.random() * TRIM_W
        py = y_offset + random.random() * TRIM_H
        size = 0.4 + random.random() * 0.8
        c.circle(px, py, size, fill=1, stroke=0)
    c.setFillAlpha(1.0)

    # Marco interior muy discreto (delimita zona segura sin ser ruido visual)
    c.setStrokeColor(GREEN_BOTELLA)
    c.setLineWidth(0.35)
    c.setStrokeAlpha(0.20)
    c.rect(x_offset + 0.45 * inch, y_offset + 0.45 * inch,
           TRIM_W - 0.9 * inch, TRIM_H - 0.9 * inch,
           fill=0, stroke=1)
    c.setStrokeAlpha(1.0)

    # ---------- Bloque 1 · Autor (tercio superior) ----------
    autor_y = y_offset + TRIM_H - 1.0 * inch
    c.setFillColor(GREEN_BOTELLA)
    c.setFont("Helvetica-Bold", 10)
    autor_text = "D A N I E L  O R O Z C O  A B I A"  # letter-spacing manual
    autor_w = c.stringWidth(autor_text, "Helvetica-Bold", 10)
    c.drawString(x_offset + (TRIM_W - autor_w) / 2, autor_y, autor_text)

    # Filete decorativo muy fino bajo el autor
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.4)
    rule_y = autor_y - 10
    c.line(x_offset + TRIM_W / 2 - 0.35 * inch, rule_y,
           x_offset + TRIM_W / 2 + 0.35 * inch, rule_y)

    # ---------- Bloque 2 · ILUSTRACIÓN DE LA LLAVE (v1 vectorial) ----------
    # Dibujada vectorialmente con primitivas reportlab (sin imagen externa).
    # Estilo: minimalista editorial · trazo verde botella + relleno dorado
    # mate · llave vertical con cordel cayendo a la izquierda. Coherente con
    # las specs del brief en `brief-diseno-portada-v2-concepto-c.md` §4.
    # Esta v1 es un primer trazo procedural · si Daniel quiere refinarla,
    # se itera ajustando proporciones o se sustituye por PNG real de
    # diseñador/IA generativa (instrucciones en brief §8).
    illust_size = 1.5 * inch
    illust_x = x_offset + (TRIM_W - illust_size) / 2
    illust_y = y_offset + TRIM_H * 0.50
    draw_key(c, illust_x, illust_y, illust_size)

    # ---------- Bloque 3 · Título (debajo del placeholder) ----------
    # Título grande en Times-Roman (mock de serif clásico verde botella)
    titulo_lines = ["Tu valor", "no está", "en su mirada"]
    title_y_start = illust_y - 0.7 * inch
    c.setFillColor(GREEN_BOTELLA)
    c.setFont("Times-Roman", 38)
    for i, line in enumerate(titulo_lines):
        tw = c.stringWidth(line, "Times-Roman", 38)
        y = title_y_start - i * 44
        c.drawString(x_offset + (TRIM_W - tw) / 2, y, line)

    # ---------- Bloque 4 · Subtítulo (italic) ----------
    subtitulo_y = title_y_start - 3 * 44 - 24
    c.setFillColor(GREEN_BOTELLA_SOFT)
    c.setFont("Times-Italic", 13)
    partes = ["El alivio de dejar de confundir",
              "amor con necesidad"]
    for i, parte in enumerate(partes):
        tw = c.stringWidth(parte, "Times-Italic", 13)
        c.drawString(x_offset + (TRIM_W - tw) / 2,
                     subtitulo_y - i * 17, parte)

    # ---------- Bloque 5 · Sello editorial discreto al pie ----------
    sello_y = y_offset + 0.7 * inch

    # Filete superior del sello
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.3)
    c.line(x_offset + TRIM_W / 2 - 0.6 * inch, sello_y + 22,
           x_offset + TRIM_W / 2 + 0.6 * inch, sello_y + 22)

    # «MIND WORLD PROJECT»
    c.setFillColor(GREEN_BOTELLA)
    c.setFont("Helvetica-Bold", 8)
    sello_text = "M I N D  W O R L D  P R O J E C T"
    sw = c.stringWidth(sello_text, "Helvetica-Bold", 8)
    c.drawString(x_offset + (TRIM_W - sw) / 2, sello_y + 10, sello_text)

    # Tagline
    c.setFillColor(GREEN_BOTELLA_SOFT)
    c.setFont("Helvetica", 6.5)
    tagline = "PSICOLOGÍA PROFUNDA Y APLICADA"
    tw = c.stringWidth(tagline, "Helvetica", 6.5)
    c.drawString(x_offset + (TRIM_W - tw) / 2, sello_y, tagline)


# ==============================================================================
# DIBUJO DEL LOMO (spine)
# ==============================================================================


def draw_spine(c):
    """Dibuja el lomo · Concepto C «La llave dentro».

    Mantiene continuidad cromática con front y back · fondo crema con
    texto en verde botella. El lomo se lee girado 90° (cabeza arriba
    según convención KDP).
    """

    # Fondo lomo crema (continuo desde front/back)
    c.setFillColor(CREAM_BG)
    c.rect(SPINE_X, 0, SPINE_W, WRAP_H, fill=1, stroke=0)

    # Filete vertical decorativo en dorado a cada lado del lomo
    c.setStrokeColor(GOLD)
    c.setStrokeAlpha(0.4)
    c.setLineWidth(0.4)
    c.line(SPINE_X + 0.04 * inch, BLEED + 1.0 * inch,
           SPINE_X + 0.04 * inch, WRAP_H - BLEED - 1.0 * inch)
    c.line(SPINE_X + SPINE_W - 0.04 * inch, BLEED + 1.0 * inch,
           SPINE_X + SPINE_W - 0.04 * inch, WRAP_H - BLEED - 1.0 * inch)
    c.setStrokeAlpha(1.0)

    # Centro del lomo
    spine_center_x = SPINE_X + SPINE_W / 2

    if SPINE_W >= 0.5 * inch:
        # Lomo amplio (≥ 0.5"): título completo arriba, autor abajo, sello centro.
        c.saveState()
        c.translate(spine_center_x, WRAP_H / 2)
        c.rotate(90)

        # Título · verde botella, serif clásica
        c.setFillColor(GREEN_BOTELLA)
        c.setFont("Times-Roman", 14)
        titulo_lomo = "Tu valor no está en su mirada"
        tw = c.stringWidth(titulo_lomo, "Times-Roman", 14)
        c.drawString(-tw / 2, 1.4 * inch, titulo_lomo)

        # Autor
        c.setFillColor(GREEN_BOTELLA_SOFT)
        c.setFont("Helvetica-Bold", 9)
        autor_lomo = "DANIEL OROZCO ABIA"
        tw = c.stringWidth(autor_lomo, "Helvetica-Bold", 9)
        c.drawString(-tw / 2, -2.2 * inch, autor_lomo)

        # Sello centro
        c.setFillColor(GREEN_BOTELLA)
        c.setFont("Helvetica-Bold", 6.5)
        sello = "MIND WORLD"
        tw = c.stringWidth(sello, "Helvetica-Bold", 6.5)
        c.drawString(-tw / 2, -0.05 * inch, sello)

        c.setFillColor(GOLD)
        c.setFont("Helvetica-Bold", 6.5)
        sello2 = "PROJECT"
        tw = c.stringWidth(sello2, "Helvetica-Bold", 6.5)
        c.drawString(-tw / 2, -0.2 * inch, sello2)

        c.restoreState()
    elif SPINE_W >= 0.25 * inch:
        # Lomo estrecho (0.25"-0.5"): solo título corto.
        print(f"AVISO · lomo estrecho ({SPINE_W_IN:.3f}\" / {SPINE_W_IN * 25.4:.1f} mm) · "
              "se dibuja versión reducida del lomo solo con título corto.")
        c.saveState()
        c.translate(spine_center_x, WRAP_H / 2)
        c.rotate(90)

        c.setFillColor(GREEN_BOTELLA)
        c.setFont("Times-Roman", 10)
        titulo_corto = "Tu valor no está en su mirada"
        tw = c.stringWidth(titulo_corto, "Times-Roman", 10)
        c.drawString(-tw / 2, 0, titulo_corto)

        c.restoreState()
    else:
        # Lomo demasiado estrecho (< 0.25"): KDP advierte que no se imprima
        # texto. Dejar solo el fondo crema.
        print(f"AVISO · lomo demasiado estrecho ({SPINE_W_IN:.3f}\" / "
              f"{SPINE_W_IN * 25.4:.1f} mm) para imprimir texto según "
              "recomendación KDP. Lomo se queda en crema sólido sin texto.")


# ==============================================================================
# DIBUJO DE CONTRAPORTADA (back cover)
# ==============================================================================


def draw_back(c):
    """Dibuja la contraportada · Concepto C «La llave dentro».

    Fondo crema cálido, texto en verde botella + negro suave, acentos
    dorados. Mantiene contraportada limpia editorial sin clickbait.
    """

    # Fondo crema (continuo desde front y spine)
    c.setFillColor(CREAM_BG)
    c.rect(-1, -1, BACK_RIGHT + 1, WRAP_H + 2, fill=1, stroke=0)

    # Textura sutil de papel mate (igual que front, para coherencia)
    c.setFillColor(CREAM_LIGHT)
    c.setFillAlpha(0.35)
    random.seed(13)
    for _ in range(420):
        px = BACK_X + random.random() * TRIM_W
        py = BLEED + random.random() * TRIM_H
        size = 0.4 + random.random() * 0.8
        c.circle(px, py, size, fill=1, stroke=0)
    c.setFillAlpha(1.0)

    # Marco interior discreto
    c.setStrokeColor(GREEN_BOTELLA)
    c.setStrokeAlpha(0.20)
    c.setLineWidth(0.35)
    c.rect(BACK_X + 0.45 * inch, BLEED + 0.45 * inch,
           TRIM_W - 0.9 * inch, TRIM_H - 0.9 * inch,
           fill=0, stroke=1)
    c.setStrokeAlpha(1.0)

    # Zona de texto
    text_x = BACK_X + 0.7 * inch
    text_width = TRIM_W - 1.4 * inch
    y_top = BLEED + TRIM_H - 1.0 * inch

    # ---------- Header · Kicker ----------
    c.setFillColor(GREEN_BOTELLA)
    c.setFont("Helvetica-Bold", 8.5)
    kicker = "P S I C O L O G Í A  P R O F U N D A  Y  A P L I C A D A"
    c.drawString(text_x, y_top, kicker)

    # Filete dorado
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.4)
    c.line(text_x, y_top - 8, text_x + 1.0 * inch, y_top - 8)

    # ---------- Cuerpo · hook editorial ----------
    y = y_top - 28

    paragrafos = [
        "Hay algo que se repite. En silencio, casi sin darte cuenta, hasta que se enciende.",
        "Alguien a quien quieres tarda en responder. Cambia el tono. Se aleja un poco. Y el suelo se va.",
        "El estómago se encoge. La cabeza empieza a girar. Buscas el error que has cometido sin saber muy bien cuál. Quieres recuperar la mirada que sientes que se ha ido.",
        "Eso no es «ser demasiado intensa». No es «ser de las que se enganchan». Es un sistema · una manera muy concreta de regular tu sentido de quién eres usando lo que hace o dice otra persona. Se aprendió cuando no había otra opción. Y se enciende sin pedirte permiso.",
        "Este libro habla de eso. En consulta lo llamo el hambre de mirada.",
    ]

    for p in paragrafos:
        y = draw_wrapped(c, p, text_x, y, text_width,
                         "Times-Roman", 9.5, 13, fill=TEXT_SOFT)
        y -= 5

    # Separador
    y -= 4
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.4)
    c.line(text_x, y, text_x + 0.6 * inch, y)
    y -= 14

    # Frase aforística de cierre
    c.setFillColor(GREEN_BOTELLA)
    c.setFont("Times-Italic", 11)
    aforismo_lines = [
        "No se trata de no necesitar a nadie.",
        "Se trata de que necesitar no te destruya.",
    ]
    for line in aforismo_lines:
        c.drawString(text_x, y, line)
        y -= 14

    y -= 10

    # ---------- Bio del autor ----------
    bio = ("Daniel Orozco Abia es Psicólogo General Sanitario, Col. CV11515, "
           "en consulta privada en Valencia desde 2012. Formado en psicoanálisis, "
           "psicología del self, psicología profunda y psicología aplicada. "
           "Autor de Los engranajes de la mente y Burnout · el libro para no petar. "
           "CEO de TWIM Project.")

    y = draw_wrapped(c, bio, text_x, y, text_width,
                     "Times-Roman", 8, 11, fill=TEXT_SOFT)

    # ---------- ISBN · código de barras placeholder ----------
    isbn_x = BACK_X + TRIM_W - 1.7 * inch
    isbn_y = BLEED + 0.45 * inch

    # Caja blanca para ISBN (KDP requiere fondo blanco para el código de barras)
    c.setFillColor(HexColor("#FFFFFF"))
    c.rect(isbn_x, isbn_y, 1.3 * inch, 0.55 * inch, fill=1, stroke=0)

    c.setFillColor(TEXT_SOFT)
    c.setFont("Helvetica", 6)
    c.drawString(isbn_x + 0.06 * inch, isbn_y + 0.46 * inch, "ISBN")
    c.setFont("Helvetica-Bold", 7)
    c.drawString(isbn_x + 0.06 * inch, isbn_y + 0.36 * inch,
                 "[generado por KDP]")

    # Líneas verticales del código de barras (placeholder)
    c.setStrokeColor(TEXT_SOFT)
    c.setLineWidth(0.5)
    barcode_y = isbn_y + 0.08 * inch
    barcode_h = 0.22 * inch
    x_bar = isbn_x + 0.06 * inch
    random.seed(42)
    while x_bar < isbn_x + 1.24 * inch:
        w = random.choice([0.4, 0.8, 1.2]) * 0.5
        c.setLineWidth(w)
        c.line(x_bar, barcode_y, x_bar, barcode_y + barcode_h)
        x_bar += 1.2

    # ---------- Footer · sello + web ----------
    c.setFillColor(GREEN_BOTELLA)
    c.setFont("Helvetica-Bold", 7.5)
    sello_text = "MIND WORLD PROJECT"
    c.drawString(text_x, BLEED + 0.4 * inch, sello_text)

    c.setFillColor(GREEN_BOTELLA_SOFT)
    c.setFont("Helvetica", 6)
    c.drawString(text_x, BLEED + 0.3 * inch, "twimproject.com")


# ==============================================================================
# GENERAR PDFs
# ==============================================================================


def generar_front_preview(path: Path) -> None:
    """PDF solo de la portada delantera (6×9"), para mockups y previews."""
    c = canvas.Canvas(str(path), pagesize=(TRIM_W + 2 * BLEED, TRIM_H + 2 * BLEED))
    draw_front(c, BLEED, BLEED)
    c.showPage()
    c.save()


def generar_wraparound(path: Path) -> None:
    """PDF wraparound completo (back + spine + front) listo para KDP."""
    c = canvas.Canvas(str(path), pagesize=(WRAP_W, WRAP_H))
    draw_back(c)
    draw_spine(c)
    draw_front(c, FRONT_X, BLEED)
    c.showPage()
    c.save()


def main():
    repo = Path(__file__).resolve().parent.parent
    out_dir = repo / "documentos-internos" / "libro-tu-valor-no-esta-en-su-mirada" / "portada"
    out_dir.mkdir(parents=True, exist_ok=True)

    front_pdf = out_dir / "portada-front-preview.pdf"
    wrap_pdf = out_dir / "portada-wraparound-kdp.pdf"

    generar_front_preview(front_pdf)
    generar_wraparound(wrap_pdf)

    print(f"Portada delantera (preview): {front_pdf}")
    print(f"  Tamaño: {front_pdf.stat().st_size / 1024:.1f} KB")
    print(f"  Dimensiones: {TRIM_W_IN + 2 * BLEED_IN}\" × {TRIM_H_IN + 2 * BLEED_IN}\"")
    print()
    print(f"Portada wraparound KDP: {wrap_pdf}")
    print(f"  Tamaño: {wrap_pdf.stat().st_size / 1024:.1f} KB")
    print(f"  Dimensiones: {WRAP_W_IN:.3f}\" × {WRAP_H_IN:.3f}\"")
    print(f"  Lomo (basado en {NUM_PAGES} páginas): {SPINE_W_IN:.3f}\" "
          f"({SPINE_W_IN * 25.4:.1f} mm)")


if __name__ == "__main__":
    main()
