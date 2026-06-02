#!/usr/bin/env python3
"""
Ensambla el PDF de la EDICIÓN DIGITAL de «Los engranajes de la mente».

Orden: portada digital TWIM  +  interior (LEDLM.pdf, 186 págs)  +  extra
exclusivo «De los engranajes a tu día»  +  contraportada (contraportadaretro.jpg).

- El extra (HTML) se renderiza con WeasyPrint al tamaño de página del interior,
  registrando Instrument Serif (tipografía de marca) para titulares/citas.
- Portada y contraportada se insertan como páginas del tamaño del interior, con
  fondo crema y la imagen "contain" centrada (las bandas, si las hay, son crema
  y resultan invisibles; no hay deformación ni recorte).

IMPORTANTE · el PDF resultante es el PRODUCTO DE PAGO: NO debe commitearse al
repo (Netlify lo serviría público). Se genera fuera del repo (/tmp) y se entrega
solo vía la función de descarga tras la compra. Este script SÍ es versionable.

Salida: /tmp/LEDLM-edicion-digital.pdf
Reproducir: python3 scripts/montar-pdf-engranajes-digital.py
"""
from pathlib import Path
import fitz  # PyMuPDF
from weasyprint import HTML, CSS

ROOT = Path(__file__).resolve().parent.parent
INTERIOR = ROOT / "LEDLM.pdf"
EXTRA_HTML = ROOT / "documentos-internos" / "producto-engranajes-digital" / "extra-de-los-engranajes-a-tu-dia.html"
PORTADA = ROOT / "documentos-internos" / "producto-engranajes-digital" / "portada-edicion-digital-twim.jpg"
CONTRA = ROOT / "contraportadaretro.jpg"
OUT = Path("/tmp/LEDLM-edicion-digital.pdf")

FONT_DIR = Path("/mnt/skills/examples/canvas-design/canvas-fonts")
CREAM = (251/255, 228/255, 187/255)

# tamaño de página del interior
doc_int = fitz.open(str(INTERIOR))
PW, PH = doc_int[0].rect.width, doc_int[0].rect.height  # pt

# 1 · EXTRA HTML -> PDF (mismo tamaño que el interior, con Instrument Serif)
print_css = CSS(string=f"""
@font-face {{ font-family:'Instrument Serif'; font-style:normal;
  src:url('file://{FONT_DIR}/InstrumentSerif-Regular.ttf'); }}
@font-face {{ font-family:'Instrument Serif'; font-style:italic;
  src:url('file://{FONT_DIR}/InstrumentSerif-Italic.ttf'); }}
@page {{ size:{PW}pt {PH}pt; margin:0; }}
html,body {{ background:#FDFCFA !important; }}
.sheet {{ box-shadow:none !important; margin:0 !important; max-width:none !important;
  padding:34pt 38pt 30pt !important; min-height:auto !important; }}
""")
html = EXTRA_HTML.read_text(encoding="utf-8")
HTML(string=html, base_url=str(EXTRA_HTML.parent)).write_pdf(str("/tmp/_extra.pdf"), stylesheets=[print_css])
doc_extra = fitz.open("/tmp/_extra.pdf")
print(f"Extra: {doc_extra.page_count} págs")

# 2 · ENSAMBLAR
out = fitz.open()

def img_page(path):
    pg = out.new_page(width=PW, height=PH)
    pg.draw_rect(pg.rect, color=CREAM, fill=CREAM)
    pg.insert_image(pg.rect, filename=str(path), keep_proportion=True)

img_page(PORTADA)                 # portada
out.insert_pdf(doc_int)           # interior 186 págs
out.insert_pdf(doc_extra)         # extra
img_page(CONTRA)                  # contraportada

out.save(str(OUT), deflate=True, garbage=4)
print(f"PDF ensamblado: {OUT}  ({out.page_count} págs)")
out.close(); doc_int.close(); doc_extra.close()
