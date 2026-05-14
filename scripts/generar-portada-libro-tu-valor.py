#!/usr/bin/env python3
"""
Genera la portada del libro «Tu valor no está en su mirada» para Amazon KDP.

Produce dos PDFs:

1. `portada-front-preview.pdf` · solo la portada delantera (6×9"), útil para
   compartir como preview en social media / web / mockups.

2. `portada-wraparound-kdp.pdf` · portada completa (back + spine + front)
   en el formato que pide Amazon KDP para tapa blanda 6×9".

Diseño: Opción A del documento `propuestas-edicion-libro-2026-05-14.md` §4
(verde dominante TWIM `#173D30`).

Asunción de páginas: 250 (provisional). El ancho del lomo cambia cuando se
conozca el conteo final tras maquetación. Para recalcular, modificar la
constante NUM_PAGES y volver a ejecutar el script.

Tipografía: Times-Roman + Helvetica como **aproximación built-in** a las
fuentes oficiales del sistema visual TWIM (Instrument Serif + Barlow
Condensed). La versión final para imprenta debe sustituirse con las fuentes
correctas — esta es una v1 para revisión visual de Daniel.

Reproducibilidad: `python3 scripts/generar-portada-libro-tu-valor.py`
"""

import io
import subprocess
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

# ==============================================================================
# CONFIGURACIÓN
# ==============================================================================

NUM_PAGES = 250  # provisional · recalcular cuando esté el conteo final

# Paleta TWIM (sistema visual canónico)
GREEN_DARK = HexColor("#173D30")
GREEN_MEDIUM = HexColor("#265C4B")
BEIGE = HexColor("#C2A78B")
BEIGE_DARK = HexColor("#A88A6E")
CREAM = HexColor("#FDFCFA")
CREAM_SOFT = HexColor("#F2EDE5")

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
                 leading, fill=CREAM, align="left"):
    """Texto con line-wrap manual. Devuelve y final tras el último renglón."""
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
# DIBUJO DE PORTADA DELANTERA (front cover)
# ==============================================================================


def draw_front(c, x_offset, y_offset):
    """Dibuja la portada delantera. x_offset/y_offset = esquina inf-izquierda."""

    # Fondo verde sólido cubre todo el trim + sangrado del lado derecho/inferior/superior
    c.setFillColor(GREEN_DARK)
    c.rect(x_offset - 1, y_offset - 1,
           TRIM_W + BLEED + 2, TRIM_H + 2 * BLEED + 2,
           fill=1, stroke=0)

    # Sutil viñeta interior con verde medio (opcional · superpone tono)
    c.setFillColor(GREEN_MEDIUM)
    c.setFillAlpha(0.18)
    c.rect(x_offset + 0.4 * inch, y_offset + 0.4 * inch,
           TRIM_W - 0.8 * inch, TRIM_H - 0.8 * inch,
           fill=1, stroke=0)
    c.setFillAlpha(1.0)

    # ---------- Bloque 1: Autor (tercio superior) ----------
    autor_y = y_offset + TRIM_H - 1.4 * inch
    c.setFillColor(BEIGE)
    c.setFont("Helvetica-Bold", 13)
    autor_text = "DANIEL OROZCO ABIA"
    autor_w = c.stringWidth(autor_text, "Helvetica-Bold", 13)
    # letter-spacing manual aproximado (espacios entre letras para destacar)
    c.drawString(x_offset + (TRIM_W - autor_w) / 2, autor_y, autor_text)

    # Línea decorativa bajo el autor
    c.setStrokeColor(BEIGE)
    c.setLineWidth(0.5)
    rule_y = autor_y - 14
    c.line(x_offset + TRIM_W / 2 - 0.6 * inch, rule_y,
           x_offset + TRIM_W / 2 + 0.6 * inch, rule_y)

    # ---------- Bloque 2: Título (tercio medio) ----------
    # Título grande en Times-Roman (mock de Instrument Serif)
    titulo_lines = ["Tu valor", "no está", "en su mirada"]
    title_y_start = y_offset + TRIM_H * 0.62
    c.setFillColor(CREAM)
    c.setFont("Times-Roman", 56)
    for i, line in enumerate(titulo_lines):
        tw = c.stringWidth(line, "Times-Roman", 56)
        y = title_y_start - i * 64
        c.drawString(x_offset + (TRIM_W - tw) / 2, y, line)

    # Subtítulo en cursiva
    subtitulo_y = y_offset + TRIM_H * 0.32
    c.setFillColor(BEIGE)
    c.setFont("Times-Italic", 18)
    subtitulo = "El alivio de dejar de confundir amor con necesidad"
    # Wrap subtitulo en 2 líneas si hace falta
    sub_w = c.stringWidth(subtitulo, "Times-Italic", 18)
    if sub_w <= TRIM_W - 1.4 * inch:
        c.drawString(x_offset + (TRIM_W - sub_w) / 2, subtitulo_y, subtitulo)
    else:
        # Dividir en dos líneas
        partes = ["El alivio de dejar de confundir",
                  "amor con necesidad"]
        for i, parte in enumerate(partes):
            tw = c.stringWidth(parte, "Times-Italic", 18)
            c.drawString(x_offset + (TRIM_W - tw) / 2,
                         subtitulo_y - i * 22, parte)

    # ---------- Bloque 3: Sello editorial (tercio inferior) ----------
    sello_y = y_offset + 1.0 * inch
    # Filete superior del sello
    c.setStrokeColor(BEIGE)
    c.setLineWidth(0.4)
    c.line(x_offset + TRIM_W / 2 - 1.0 * inch, sello_y + 38,
           x_offset + TRIM_W / 2 + 1.0 * inch, sello_y + 38)

    # «MIND WORLD PROJECT»
    c.setFillColor(CREAM)
    c.setFont("Helvetica-Bold", 11)
    sello_text = "MIND WORLD PROJECT"
    sw = c.stringWidth(sello_text, "Helvetica-Bold", 11)
    c.drawString(x_offset + (TRIM_W - sw) / 2, sello_y + 18, sello_text)

    # Tagline
    c.setFillColor(BEIGE)
    c.setFont("Helvetica", 8)
    tagline = "PSICOLOGÍA PROFUNDA Y APLICADA"
    tw = c.stringWidth(tagline, "Helvetica", 8)
    c.drawString(x_offset + (TRIM_W - tw) / 2, sello_y + 4, tagline)


# ==============================================================================
# DIBUJO DEL LOMO (spine)
# ==============================================================================


def draw_spine(c):
    """Dibuja el lomo. El lomo se lee girado 90° (cabeza arriba)."""

    # Fondo lomo (verde oscuro continuo desde el front/back)
    c.setFillColor(GREEN_DARK)
    c.rect(SPINE_X, 0, SPINE_W, WRAP_H, fill=1, stroke=0)

    # Margen de seguridad del lomo (KDP recomienda 0.0625" de cada lado del lomo)
    spine_safe_margin = 0.0625 * inch

    # Centro vertical del lomo
    spine_center_x = SPINE_X + SPINE_W / 2

    # Texto del lomo (rotado 90°)
    # Para libros con lomo > 0.5" (12mm) se puede leer cabeza arriba
    # Si el lomo es muy estrecho, mejor solo el título corto

    if SPINE_W >= 0.5 * inch:
        # Lomo amplio: título arriba, autor abajo, logo centro
        c.saveState()
        c.translate(spine_center_x, WRAP_H / 2)
        c.rotate(90)

        # Título
        c.setFillColor(CREAM)
        c.setFont("Times-Roman", 16)
        titulo_lomo = "Tu valor no está en su mirada"
        tw = c.stringWidth(titulo_lomo, "Times-Roman", 16)
        c.drawString(-tw / 2, 1.4 * inch, titulo_lomo)

        # Autor
        c.setFillColor(BEIGE)
        c.setFont("Helvetica-Bold", 10)
        autor_lomo = "DANIEL OROZCO ABIA"
        tw = c.stringWidth(autor_lomo, "Helvetica-Bold", 10)
        c.drawString(-tw / 2, -2.2 * inch, autor_lomo)

        # Sello centro
        c.setFillColor(CREAM)
        c.setFont("Helvetica-Bold", 7)
        sello = "MIND WORLD"
        tw = c.stringWidth(sello, "Helvetica-Bold", 7)
        c.drawString(-tw / 2, -0.1 * inch, sello)

        c.setFillColor(BEIGE)
        c.setFont("Helvetica-Bold", 7)
        sello2 = "PROJECT"
        tw = c.stringWidth(sello2, "Helvetica-Bold", 7)
        c.drawString(-tw / 2, -0.25 * inch, sello2)

        c.restoreState()


# ==============================================================================
# DIBUJO DE CONTRAPORTADA (back cover)
# ==============================================================================


def draw_back(c):
    """Dibuja la contraportada en el lado izquierdo del wraparound."""

    # Fondo verde
    c.setFillColor(GREEN_DARK)
    c.rect(-1, -1, BACK_RIGHT + 1, WRAP_H + 2, fill=1, stroke=0)

    # Marco interior sutil
    c.setFillColor(GREEN_MEDIUM)
    c.setFillAlpha(0.18)
    c.rect(BACK_X + 0.4 * inch, BLEED + 0.4 * inch,
           TRIM_W - 0.8 * inch, TRIM_H - 0.8 * inch,
           fill=1, stroke=0)
    c.setFillAlpha(1.0)

    # Zona de texto (margen seguro)
    text_x = BACK_X + 0.7 * inch
    text_width = TRIM_W - 1.4 * inch
    y_top = BLEED + TRIM_H - 1.1 * inch

    # ---------- Header: Kicker ----------
    c.setFillColor(BEIGE)
    c.setFont("Helvetica-Bold", 9)
    kicker = "PSICOLOGÍA PROFUNDA Y APLICADA"
    c.drawString(text_x, y_top, kicker)

    # Línea sutil
    c.setStrokeColor(BEIGE)
    c.setLineWidth(0.4)
    c.line(text_x, y_top - 10, text_x + 1.5 * inch, y_top - 10)

    # ---------- Cuerpo del texto (hook editorial) ----------
    y = y_top - 30

    paragrafos = [
        "Hay algo que se repite. En silencio, casi sin darte cuenta, hasta que se enciende.",
        "Alguien a quien quieres tarda en responder. Cambia el tono. Se aleja un poco. Y el suelo se va.",
        "El estómago se encoge. La cabeza empieza a girar. Buscas el error que has cometido sin saber muy bien cuál. Quieres recuperar la mirada que sientes que se ha ido.",
        "Eso no es «ser demasiado intensa». No es «ser de las que se enganchan». Es un sistema · una manera muy concreta de regular tu sentido de quién eres usando lo que hace o dice otra persona. Se aprendió cuando no había otra opción. Y se enciende sin pedirte permiso.",
        "Este libro habla de eso. En consulta lo llamo el hambre de mirada.",
    ]

    for p in paragrafos:
        y = draw_wrapped(c, p, text_x, y, text_width,
                         "Times-Roman", 9.5, 13, fill=CREAM)
        y -= 5

    # Separador
    y -= 4
    c.setStrokeColor(BEIGE)
    c.setLineWidth(0.3)
    c.line(text_x, y, text_x + 0.8 * inch, y)
    y -= 14

    # Frase aforística de cierre
    c.setFillColor(BEIGE)
    c.setFont("Times-Italic", 11)
    aforismo_lines = [
        "No se trata de no necesitar a nadie.",
        "Se trata de que necesitar no te destruya.",
    ]
    for line in aforismo_lines:
        tw = c.stringWidth(line, "Times-Italic", 11)
        c.drawString(text_x, y, line)
        y -= 14

    y -= 8

    # ---------- Bio del autor (pie) ----------
    bio = ("Daniel Orozco Abia es Psicólogo General Sanitario, Col. CV11515, "
           "en consulta privada en Valencia desde 2012. Formado en psicoanálisis, "
           "psicología del self, psicología profunda y psicología aplicada. "
           "Autor de Los engranajes de la mente y Burnout · el libro para no petar. "
           "CEO de TWIM Project.")

    c.setFillColor(CREAM)
    y = draw_wrapped(c, bio, text_x, y, text_width,
                     "Times-Roman", 8, 11, fill=CREAM)

    # ---------- ISBN / código de barras placeholder ----------
    # KDP genera el código real al subir, aquí solo placeholder visual
    isbn_x = BACK_X + TRIM_W - 1.7 * inch
    isbn_y = BLEED + 0.45 * inch

    c.setFillColor(CREAM)
    c.rect(isbn_x, isbn_y, 1.3 * inch, 0.55 * inch, fill=1, stroke=0)

    c.setFillColor(GREEN_DARK)
    c.setFont("Helvetica", 6)
    c.drawString(isbn_x + 0.06 * inch, isbn_y + 0.46 * inch, "ISBN")
    c.setFont("Helvetica-Bold", 7)
    c.drawString(isbn_x + 0.06 * inch, isbn_y + 0.36 * inch,
                 "[generado por KDP]")
    # Imitar líneas verticales del código de barras (placeholder)
    c.setStrokeColor(GREEN_DARK)
    c.setLineWidth(0.5)
    barcode_y = isbn_y + 0.08 * inch
    barcode_h = 0.22 * inch
    x_bar = isbn_x + 0.06 * inch
    import random
    random.seed(42)
    while x_bar < isbn_x + 1.24 * inch:
        w = random.choice([0.4, 0.8, 1.2]) * 0.5
        c.setLineWidth(w)
        c.line(x_bar, barcode_y, x_bar, barcode_y + barcode_h)
        x_bar += 1.2

    # ---------- Footer logo MIND WORLD ----------
    c.setFillColor(BEIGE)
    c.setFont("Helvetica-Bold", 8)
    sello_text = "MIND WORLD PROJECT"
    sw = c.stringWidth(sello_text, "Helvetica-Bold", 8)
    c.drawString(text_x, BLEED + 0.4 * inch, sello_text)
    c.setFont("Helvetica", 6)
    c.drawString(text_x, BLEED + 0.3 * inch,
                 "twimproject.com")


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
