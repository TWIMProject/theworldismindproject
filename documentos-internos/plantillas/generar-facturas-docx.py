#!/usr/bin/env python3
# Genera las plantillas .docx de factura (renta anual + mensual) con diseño unificado.
# Diseño base · factura-anual-renta.html. La mensual lo reutiliza con sus
# especificidades (subtítulo, columnas de tabla, declaración).
# Requisitos Daniel (22-may): cabe en UNA página A4 · email danielorozco@twimproject.com
# · fondo crema cálido para calidez.

from docx import Document
from docx.shared import Pt, Mm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# ---- Paleta TWIM ----
GREEN_DARK = "173D30"
BEIGE      = "C2A78B"
CREAM      = "FDFCFA"
WARM       = "F5EFE3"   # crema cálido · fondo de página
INK        = "2B2420"
MUTED      = "6B6258"
BORDER     = "E3DAC9"
FONT = "Century Gothic"
EMAIL = "danielorozco@twimproject.com"

def shade_cell(cell, hex_color):
    sh = OxmlElement('w:shd')
    sh.set(qn('w:val'), 'clear'); sh.set(qn('w:color'), 'auto'); sh.set(qn('w:fill'), hex_color)
    cell._tc.get_or_add_tcPr().append(sh)

def set_cell_borders(cell, color=BORDER, sz=4, sides=('top','bottom','left','right')):
    tcPr = cell._tc.get_or_add_tcPr()
    borders = OxmlElement('w:tcBorders')
    for side in sides:
        el = OxmlElement(f'w:{side}')
        el.set(qn('w:val'), 'single'); el.set(qn('w:sz'), str(sz))
        el.set(qn('w:space'), '0'); el.set(qn('w:color'), color)
        borders.append(el)
    tcPr.append(borders)

def no_cell_borders(cell):
    tcPr = cell._tc.get_or_add_tcPr()
    borders = OxmlElement('w:tcBorders')
    for side in ('top','bottom','left','right'):
        el = OxmlElement(f'w:{side}'); el.set(qn('w:val'), 'nil'); borders.append(el)
    tcPr.append(borders)

def set_cell_margins(cell, top=60, bottom=60, left=100, right=100):
    tcPr = cell._tc.get_or_add_tcPr()
    m = OxmlElement('w:tcMar')
    for side, val in (('top',top),('bottom',bottom),('left',left),('right',right)):
        el = OxmlElement(f'w:{side}')
        el.set(qn('w:w'), str(val)); el.set(qn('w:type'), 'dxa')
        m.append(el)
    tcPr.append(m)

def vcenter(cell):
    va = OxmlElement('w:vAlign'); va.set(qn('w:val'), 'center')
    cell._tc.get_or_add_tcPr().append(va)

def doc_background(doc, hex_color):
    # Fondo de página (vista en pantalla de Word)
    bg = OxmlElement('w:background')
    bg.set(qn('w:color'), hex_color)
    doc.element.insert(0, bg)
    # displayBackgroundShape en settings para que Word lo muestre
    settings = doc.settings.element
    dbg = OxmlElement('w:displayBackgroundShape')
    settings.append(dbg)

def run(paragraph, text, size=11, color=INK, bold=False, italic=False,
        caps=False, spacing=None):
    r = paragraph.add_run(text)
    r.font.name = FONT
    r.font.size = Pt(size)
    r.font.color.rgb = RGBColor.from_string(color)
    r.font.bold = bold; r.font.italic = italic
    if caps: r.font.all_caps = True
    if spacing is not None:
        rPr = r._element.get_or_add_rPr()
        sp = OxmlElement('w:spacing'); sp.set(qn('w:val'), str(spacing))
        rPr.append(sp)
    return r

def para(container, align=None, space_before=0, space_after=3, line=1.2):
    p = container.add_paragraph()
    if align is not None: p.alignment = align
    pf = p.paragraph_format
    pf.space_before = Pt(space_before); pf.space_after = Pt(space_after)
    pf.line_spacing = line
    return p

def hrule(container, color, sz, space_before=0, space_after=8, side='bottom'):
    p = para(container, space_before=space_before, space_after=space_after)
    pPr = p._element.get_or_add_pPr()
    bd = OxmlElement('w:pBdr')
    el = OxmlElement(f'w:{side}')
    el.set(qn('w:val'), 'single'); el.set(qn('w:sz'), str(sz))
    el.set(qn('w:space'), '2'); el.set(qn('w:color'), color)
    bd.append(el); pPr.append(bd)
    run(p, " ", size=2)
    return p

def build_invoice(path, *, titulo, subtitulo, servicios_headers, servicios_row,
                  sesiones_extra, declaracion):
    doc = Document()
    doc_background(doc, WARM)

    sec = doc.sections[0]
    sec.page_width = Mm(210); sec.page_height = Mm(297)
    sec.orientation = WD_ORIENT.PORTRAIT
    sec.top_margin = Mm(0); sec.bottom_margin = Mm(0)
    sec.left_margin = Mm(0); sec.right_margin = Mm(0)

    # ===== HEADER verde =====
    header = doc.add_table(rows=1, cols=2)
    header.alignment = WD_TABLE_ALIGNMENT.CENTER
    header.autofit = False
    hl, hr = header.rows[0].cells
    hl.width = Mm(125); hr.width = Mm(85)
    for c in (hl, hr):
        shade_cell(c, GREEN_DARK); no_cell_borders(c)
        set_cell_margins(c, top=150, bottom=150, left=320, right=320)
        vcenter(c)
    hl.paragraphs[0].clear()
    pic_p = hl.paragraphs[0]
    try:
        pic_p.add_run().add_picture('assets/logo-mindworld-on-dark.png', width=Mm(17))
    except Exception:
        pass
    pb = para(hl, space_after=0, line=1.15)
    run(pb, "TWIM PROJECT", size=8.5, color=BEIGE, bold=True, spacing=30)
    pb2 = para(hl, space_after=0, line=1.15)
    run(pb2, "Daniel Orozco Abia · CV11515", size=9.5, color=CREAM)

    hr.paragraphs[0].clear()
    m1 = hr.paragraphs[0]; m1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    m1.paragraph_format.space_after = Pt(2)
    run(m1, "Nº FACTURA  ", size=8, color=BEIGE, bold=True, spacing=12)
    run(m1, "{{NUMERO_FACTURA}}", size=10, color=CREAM)
    m2 = para(hr, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=0)
    run(m2, "FECHA DE EMISIÓN  ", size=8, color=BEIGE, bold=True, spacing=12)
    run(m2, "{{FECHA_EMISION}}", size=10, color=CREAM)

    # ===== CUERPO · tabla 1x1 con fondo crema cálido =====
    body_tbl = doc.add_table(rows=1, cols=1)
    body_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    body = body_tbl.rows[0].cells[0]
    body.width = Mm(210)
    no_cell_borders(body); shade_cell(body, WARM)
    set_cell_margins(body, top=320, bottom=260, left=560, right=560)
    body.paragraphs[0].clear()

    t = body.paragraphs[0]
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    t.paragraph_format.space_after = Pt(2)
    run(t, titulo, size=18, color=GREEN_DARK, bold=True)

    st = para(body, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
    run(st, subtitulo, size=10, color=MUTED)

    hrule(body, BEIGE, 6, space_before=0, space_after=10)

    # ===== PARTES =====
    parties = body.add_table(rows=1, cols=2)
    parties.alignment = WD_TABLE_ALIGNMENT.CENTER
    pl, pr = parties.rows[0].cells
    pl.width = Mm(94); pr.width = Mm(94)

    def fill_party(cell, role, name, lines):
        set_cell_borders(cell, color=BEIGE, sz=6)
        shade_cell(cell, CREAM)
        set_cell_margins(cell, top=110, bottom=110, left=160, right=160)
        cell.paragraphs[0].clear()
        rp = cell.paragraphs[0]
        rp.paragraph_format.space_after = Pt(4)
        run(rp, role, size=8, color=GREEN_DARK, bold=True, spacing=20, caps=True)
        npar = para(cell, space_after=2)
        run(npar, name, size=11.5, color=GREEN_DARK, bold=True)
        for ln in lines:
            lp = para(cell, space_after=0, line=1.3)
            run(lp, ln, size=9, color=INK)

    fill_party(pl, "Emisor (profesional)", "Daniel Orozco Abia", [
        "NIF: 48442701D",
        "Psicólogo General Sanitario · Col. CV11515",
        "Calle Embajador Vich 3, 1B · 46002 Valencia · España",
        f"Tel.: 625 231 297 · {EMAIL}",
    ])
    fill_party(pr, "Receptor (paciente)", "{{NOMBRE_PACIENTE}}", [
        "DNI: {{DNI_PACIENTE}}",
        "{{DIRECCION_PACIENTE_LINEA1}}",
        "{{DIRECCION_PACIENTE_LINEA2}}",
    ])

    para(body, space_after=4)

    # ===== TABLA SERVICIOS =====
    ncols = len(servicios_headers)
    serv = body.add_table(rows=2, cols=ncols)
    serv.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(servicios_headers):
        c = serv.rows[0].cells[i]
        shade_cell(c, GREEN_DARK)
        set_cell_borders(c, color=GREEN_DARK, sz=4)
        set_cell_margins(c, top=90, bottom=90, left=130, right=130)
        c.paragraphs[0].clear()
        hp = c.paragraphs[0]
        if h.get('right'): hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        run(hp, h['t'], size=8, color=CREAM, bold=True, spacing=12, caps=True)
    for i, val in enumerate(servicios_row):
        c = serv.rows[1].cells[i]
        set_cell_borders(c, color=BORDER, sz=4)
        shade_cell(c, CREAM)
        set_cell_margins(c, top=110, bottom=110, left=130, right=130)
        c.paragraphs[0].clear()
        dp = c.paragraphs[0]
        right = servicios_headers[i].get('right')
        if right: dp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        run(dp, val, size=10, color=INK, bold=bool(right))

    if sesiones_extra:
        extra = body.add_table(rows=1, cols=1)
        extra.alignment = WD_TABLE_ALIGNMENT.CENTER
        ec = extra.rows[0].cells[0]
        shade_cell(ec, "F2F7F4")
        set_cell_borders(ec, color=BORDER, sz=4)
        set_cell_margins(ec, top=90, bottom=90, left=130, right=130)
        ec.paragraphs[0].clear()
        run(ec.paragraphs[0], sesiones_extra, size=9, color="5C6F66", italic=True)

    iva = para(body, space_before=6, space_after=10)
    run(iva, "* Servicio exento de IVA según art. 20.1.3º Ley 37/1992 "
             "(servicios de asistencia sanitaria).", size=8, color=MUTED, italic=True)

    # ===== TOTAL BOX =====
    total = body.add_table(rows=1, cols=2)
    total.alignment = WD_TABLE_ALIGNMENT.CENTER
    tl, tr = total.rows[0].cells
    tl.width = Mm(120); tr.width = Mm(68)
    for c in (tl, tr):
        shade_cell(c, GREEN_DARK); no_cell_borders(c)
        set_cell_margins(c, top=120, bottom=120, left=220, right=220)
        vcenter(c)
    tl.paragraphs[0].clear()
    run(tl.paragraphs[0], "Total a abonar", size=10.5, color=CREAM, bold=True,
        spacing=12, caps=True)
    tr.paragraphs[0].clear()
    trp = tr.paragraphs[0]; trp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run(trp, "{{IMPORTE}}", size=16, color=CREAM, bold=True)

    para(body, space_after=6)

    for ln in declaracion:
        dp = para(body, space_after=1, line=1.4)
        run(dp, ln, size=9.5, color=INK)

    # ===== FIRMA =====
    para(body, space_after=14)
    hrule(body, INK, 6, space_before=0, space_after=3)
    sn = para(body, space_after=0)
    run(sn, "Daniel Orozco Abia", size=10.5, color=GREEN_DARK, bold=True)
    sm = para(body, space_after=0)
    run(sm, "Psicólogo General Sanitario · Col. CV11515", size=9, color=MUTED)

    # ===== FOOTER =====
    foot = para(body, space_before=14, space_after=0, align=WD_ALIGN_PARAGRAPH.CENTER)
    pPr = foot._element.get_or_add_pPr()
    bd = OxmlElement('w:pBdr')
    top = OxmlElement('w:top')
    top.set(qn('w:val'), 'single'); top.set(qn('w:sz'), '6')
    top.set(qn('w:space'), '6'); top.set(qn('w:color'), BEIGE)
    bd.append(top); pPr.append(bd)
    run(foot, f"Calle Embajador Vich 3, 1B  ·  46002 Valencia  ·  "
              f"Tel. 625 231 297  ·  {EMAIL}", size=8.5, color=MUTED)

    doc.save(path)
    print(f"Generado · {path}")


build_invoice(
    'documentos-internos/plantillas/factura-anual-renta.docx',
    titulo="FACTURA DE HONORARIOS",
    subtitulo="Ejercicio fiscal {{ANIO}} · Honorarios por tratamiento psicológico",
    servicios_headers=[
        {'t': 'Descripción del servicio'},
        {'t': 'Período'},
        {'t': 'Sesiones'},
        {'t': 'Importe', 'right': True},
    ],
    servicios_row=[
        "Honorarios por tratamiento psicológico",
        "{{PERIODO}}", "{{NUM_SESIONES}}", "{{IMPORTE}}",
    ],
    sesiones_extra=None,
    declaracion=[
        "El presente documento acredita los honorarios satisfechos en concepto de "
        "tratamiento psicológico durante el ejercicio fiscal {{ANIO}}, a efectos de "
        "declaración del IRPF.",
        "Emitido en Valencia, a {{FECHA_EMISION}}.",
    ],
)

build_invoice(
    'documentos-internos/plantillas/factura-mensual-paciente.docx',
    titulo="FACTURA DE HONORARIOS",
    subtitulo="{{MES}} · Honorarios por tratamiento psicológico",
    servicios_headers=[
        {'t': 'Descripción del servicio'},
        {'t': 'Sesiones'},
        {'t': 'Importe', 'right': True},
    ],
    servicios_row=[
        "Honorarios por tratamiento psicológico",
        "{{NUM_SESIONES}}", "{{IMPORTE}}",
    ],
    sesiones_extra="Sesiones {{MES}}: {{SESIONES_FECHAS}}",
    declaracion=[
        "El presente documento acredita los honorarios satisfechos en concepto de "
        "tratamiento psicológico correspondientes a {{MES}}.",
        "Emitido en Valencia, a {{FECHA_EMISION}}.",
    ],
)
print("OK · 2 plantillas .docx generadas")
