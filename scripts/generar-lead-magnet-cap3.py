#!/usr/bin/env python3
"""
Genera el PDF lead-magnet del Capítulo III «El Yo frente al Superyó».

Estructura del PDF final:
  - 1 página de portadilla editorial con copy firmado por Daniel.
  - 21 páginas del Capítulo III (extraídas de LEDLM.pdf, físicas 49-69).
  - 1 página de cierre con CTA al libro completo + a la newsletter «Te escribo».

Salida: libro-engranajes-mente/lead-magnet/capitulo-3-superyo.pdf

Reproducibilidad: ejecutar con `python3 scripts/generar-lead-magnet-cap3.py`
desde la raíz del repo. Requiere reportlab + qpdf en el PATH.
"""

import io
import subprocess
import sys
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

# Tamaño exacto del libro original (pdfinfo LEDLM.pdf)
PAGE_W = 438
PAGE_H = 631.68

# Paleta TWIM (coherente con CLAUDE.md y el sistema visual)
GREEN_DARK = HexColor("#173D30")
GREEN_MEDIUM = HexColor("#265C4B")
BEIGE = HexColor("#C2A78B")
CREAM = HexColor("#FDFCFA")
TEXT_DARK = HexColor("#173D30")
TEXT_SOFT = HexColor("#3a4a42")


def draw_wrapped(c, text, x, y, max_width, font_name, font_size, leading, fill=TEXT_DARK):
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
        c.drawString(x, y, ln)
        y -= leading
    return y


def generar_portadilla(path):
    c = canvas.Canvas(str(path), pagesize=(PAGE_W, PAGE_H))

    c.setFillColor(CREAM)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    c.setFillColor(GREEN_DARK)
    c.rect(0, PAGE_H - 80, PAGE_W, 80, fill=1, stroke=0)

    c.setFillColor(BEIGE)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 36, "TWIM PROJECT · LECTURA DE CORTESÍA")
    c.setFillColor(CREAM)
    c.setFont("Times-Italic", 12)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 58, "Los engranajes de la mente")

    c.setFillColor(GREEN_DARK)
    c.setFont("Times-Roman", 22)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 150, "Una carta antes")
    c.drawCentredString(PAGE_W / 2, PAGE_H - 180, "de que empieces a leer.")

    margin_x = 60
    text_x = margin_x
    text_w = PAGE_W - 2 * margin_x
    y = PAGE_H - 240

    parrafos = [
        "Vas a leer un capítulo del libro «Los engranajes de la mente».",
        "Es el capítulo sobre la voz que llevas dentro y te dice "
        "«no es suficiente», «esto te ha quedado regular», «otros lo "
        "habrían hecho mejor». No la imaginas.",
        "Tiene historia, tiene nombre y tiene función. Este capítulo "
        "va de cómo se monta.",
        "Léelo despacio. No es ejercicio, no es deber. Es lectura.",
        "Si al cerrarlo te has visto en alguna escena, ya sabes "
        "lo que toca: seguir leyendo el resto.",
    ]

    for p in parrafos:
        y = draw_wrapped(c, p, text_x, y, text_w,
                         "Times-Roman", 12.5, 18, fill=TEXT_SOFT)
        y -= 8

    y -= 12
    c.setFillColor(GREEN_MEDIUM)
    c.setFont("Times-Italic", 13)
    c.drawString(text_x, y, "— Daniel Orozco Abia")
    c.setFillColor(TEXT_SOFT)
    c.setFont("Helvetica", 9)
    y -= 16
    c.drawString(text_x, y, "Psicólogo General Sanitario · CV11515 · TWIM Project")

    c.setStrokeColor(BEIGE)
    c.setLineWidth(0.5)
    c.line(margin_x, 80, PAGE_W - margin_x, 80)

    c.setFillColor(GREEN_MEDIUM)
    c.setFont("Helvetica", 9)
    c.drawCentredString(PAGE_W / 2, 60, "twimproject.com")
    c.setFillColor(TEXT_SOFT)
    c.setFont("Helvetica", 8)
    c.drawCentredString(PAGE_W / 2, 46,
                        "Lectura de cortesía. Comparte si te ha movido algo; no lo redistribuyas sin pedir.")

    c.showPage()
    c.save()


def generar_cierre(path):
    c = canvas.Canvas(str(path), pagesize=(PAGE_W, PAGE_H))

    c.setFillColor(GREEN_DARK)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    c.setFillColor(BEIGE)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 60, "AHORA QUE HAS LEÍDO ESTO")

    c.setFillColor(CREAM)
    c.setFont("Times-Roman", 22)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 110, "Hay otros cinco engranajes")
    c.drawCentredString(PAGE_W / 2, PAGE_H - 140, "como este dentro del libro.")

    margin_x = 60
    text_x = margin_x
    text_w = PAGE_W - 2 * margin_x
    y = PAGE_H - 200

    parrafos = [
        "Este era el capítulo III. Hay otros cinco que trabajan el resto "
        "del mapa: el Yo y el Ello, las pulsiones de vida y de muerte, "
        "los mecanismos de defensa, la angustia y los síntomas, y cómo "
        "se cambia algo de verdad cuando se ha entendido.",
        "Es psicoanálisis aplicado, escrito para gente que no es "
        "psicólogo y no quiere serlo. 186 páginas. Sin jerga.",
    ]

    for p in parrafos:
        y = draw_wrapped(c, p, text_x, y, text_w,
                         "Times-Roman", 12, 18, fill=CREAM)
        y -= 8

    y -= 20
    c.setFillColor(BEIGE)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(text_x, y, "EL LIBRO COMPLETO")
    y -= 18
    c.setFillColor(CREAM)
    c.setFont("Helvetica", 11)
    c.drawString(text_x, y, "Kindle 7,68 € · Tapa blanda 15,38 € · Tapa dura 14,94 €")
    y -= 18
    c.setFillColor(BEIGE)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(text_x, y, "amazon.es/dp/B0FR8PSQT3")

    y -= 36
    c.setFillColor(BEIGE)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(text_x, y, "Y SI NO QUIERES LIBRO, PERO SÍ QUIERES SEGUIR LEYENDO")
    y -= 18
    c.setFillColor(CREAM)
    c.setFont("Times-Roman", 11.5)
    y = draw_wrapped(
        c,
        "«Te escribo» — una carta cada tanto, sobre la mente, "
        "el cansancio y lo que no se dice. Sin algoritmo, "
        "sin spam, sin nada que vender en cada email.",
        text_x, y, text_w, "Times-Roman", 11.5, 16, fill=CREAM,
    )
    y -= 6
    c.setFillColor(BEIGE)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(text_x, y, "twimproject.com/newsletter/")

    c.setStrokeColor(BEIGE)
    c.setLineWidth(0.5)
    c.line(margin_x, 80, PAGE_W - margin_x, 80)

    c.setFillColor(BEIGE)
    c.setFont("Helvetica", 9)
    c.drawCentredString(PAGE_W / 2, 60, "Daniel Orozco Abia · Psicólogo General Sanitario · CV11515")
    c.setFillColor(CREAM)
    c.setFont("Helvetica", 8)
    c.drawCentredString(PAGE_W / 2, 46, "TWIM Project · twimproject.com")

    c.showPage()
    c.save()


def main():
    repo = Path(__file__).resolve().parent.parent
    src = repo / "LEDLM.pdf"
    dst = repo / "libro-engranajes-mente" / "lead-magnet" / "capitulo-3-superyo.pdf"
    dst.parent.mkdir(parents=True, exist_ok=True)

    if not src.exists():
        sys.exit(f"No se encuentra el PDF fuente: {src}")

    tmpdir = Path("/tmp/lead-magnet")
    tmpdir.mkdir(exist_ok=True)
    portadilla_pdf = tmpdir / "portadilla.pdf"
    capitulo_pdf = tmpdir / "capitulo3.pdf"
    cierre_pdf = tmpdir / "cierre.pdf"

    generar_portadilla(portadilla_pdf)
    generar_cierre(cierre_pdf)

    subprocess.run(
        ["qpdf", str(src), "--pages", str(src), "49-69", "--", str(capitulo_pdf)],
        check=True,
    )

    subprocess.run(
        ["qpdf", "--empty",
         "--pages", str(portadilla_pdf), "1",
         str(capitulo_pdf), "1-z",
         str(cierre_pdf), "1",
         "--", str(dst)],
        check=True,
    )

    print(f"PDF generado: {dst}")
    print(f"Tamaño: {dst.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
