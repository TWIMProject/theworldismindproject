# Libro «Tu valor no está en su mirada»

> El alivio de dejar de confundir amor con necesidad.

**Estado:** en producción. Tercer libro de Daniel Orozco Abia.
**Carpeta creada:** 11 mayo 2026.
**Por qué existe esta carpeta:** Daniel quiere que **cualquier sesión futura de Claude pueda leer el manuscrito completo** y que el contenido del libro sea auditable / iterable como cualquier otro artefacto del repo. El libro es activo crítico — fuente de ingresos económicos cuando salga a la venta.

---

## Qué hay en esta carpeta

| Archivo | Qué es | Cuándo se actualiza |
|---|---|---|
| `manuscrito-YYYY-MM-DD.docx` | Versión binaria oficial del manuscrito tal cual la sube Daniel desde Word. Es la fuente de verdad para edición visual. | Cuando Daniel suba una nueva versión a una sesión. Se versiona por fecha — **no se sobrescribe** la anterior. |
| `manuscrito-YYYY-MM-DD.md` | Misma versión extraída a markdown. Diffeable por git, legible por Claude sin herramientas externas. | Se genera automáticamente cada vez que entra una nueva `.docx`. |
| `README.md` | Este archivo. Índice, estado, workflow. | Cuando cambie el estado del libro o el workflow. |

**Versión actual:** `manuscrito-2026-05-14.docx` + `manuscrito-2026-05-14.md`. **Estado: ~92 % completo** — manuscrito editorial redactado entero, pendientes 4 inconsistencias internas + 2 decisiones editoriales + producción técnica + integración ecosistema. Detalle en `estado-completitud-2026-05-14.md`.

---

## Cómo se trabaja con esto

### Cuando Daniel envía una nueva versión del manuscrito

1. Daniel adjunta el `.docx` actualizado en la sesión.
2. Claude:
   - Copia el archivo a esta carpeta como `manuscrito-YYYY-MM-DD.docx` (fecha del día).
   - Extrae el texto a `manuscrito-YYYY-MM-DD.md` con el script estándar (ver más abajo).
   - **No borra versiones anteriores.** El historial queda en la carpeta para trazabilidad.
   - Commit + PR a la rama de trabajo.
3. La «versión activa» es siempre la `.docx` con la fecha más reciente.

### Cuando alguien quiere consultar o citar contenido del libro

- Para lectura humana / edición fina: abrir el `.docx` más reciente.
- Para que Claude analice, cite, resuma o proponga ajustes: leer el `.md` más reciente.
- Si hay discrepancia entre `.docx` y `.md`, la fuente canónica es el `.docx` (porque el `.md` puede haber perdido formato fino al extraerse).

### Cuando se acuerden cambios de contenido tras una sesión de Claude

- No editar el `.docx` desde Claude (no tenemos herramientas para preservar el formato Word).
- Sí editar el `.md` con propuestas de Claude → Daniel las incorpora manualmente al `.docx` desde Word → vuelve a subir el `.docx` actualizado en la siguiente sesión y se regenera el ciclo.

---

## Script de extracción `.docx` → markdown

Para que cualquier sesión futura pueda regenerar el `.md` si hace falta, este es el comando exacto que funcionó la primera vez (11 may 2026), basado en `unzip` + Python estándar (sin pandoc ni `python-docx`):

```bash
cd /tmp && rm -rf docx-extract && mkdir docx-extract && cd docx-extract \
  && unzip -q "<ruta-al-docx>" \
  && python3 -c "
import xml.etree.ElementTree as ET
import re
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
tree = ET.parse('/tmp/docx-extract/word/document.xml')
root = tree.getroot()
body = root.find('w:body', ns)
lines = []
for p in body.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
    style = ''
    pPr = p.find('w:pPr', ns)
    if pPr is not None:
        pStyle = pPr.find('w:pStyle', ns)
        if pStyle is not None:
            style = pStyle.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', '')
    text_parts = []
    for r in p.findall('w:r', ns):
        rPr = r.find('w:rPr', ns)
        is_bold = rPr is not None and rPr.find('w:b', ns) is not None
        is_italic = rPr is not None and rPr.find('w:i', ns) is not None
        for t in r.findall('w:t', ns):
            txt = t.text or ''
            if is_bold and is_italic:
                txt = f'***{txt}***' if txt.strip() else txt
            elif is_bold:
                txt = f'**{txt}**' if txt.strip() else txt
            elif is_italic:
                txt = f'*{txt}*' if txt.strip() else txt
            text_parts.append(txt)
        for br in r.findall('w:br', ns):
            text_parts.append('\n')
    text = ''.join(text_parts)
    if style.startswith('Heading') or style.startswith('Ttulo') or style.startswith('Titulo') or style == 'Title':
        level = 1
        m = re.search(r'(\d+)', style)
        if m: level = int(m.group(1))
        if style == 'Title': level = 1
        lines.append(f'{\"#\" * level} {text}')
    else:
        lines.append(text)
output = '\n\n'.join(lines)
output = re.sub(r'\n{4,}', '\n\n\n', output)
# Limpieza: eliminar pares bold-bold adyacentes (cierre + apertura redundantes)
# que producen exactamente 4 asteriscos consecutivos. NO toca 3 (bold-italic) ni 5+.
output = re.sub(r'(?<!\*)\*\*\*\*(?!\*)', '', output)
print(output)
" > <ruta-al-md>
```

**Nota:** este docx en particular usa **negrita como sustituto de heading** (en vez de los estilos oficiales Heading de Word). El script extrae texto fielmente, pero los `#` markdown no se autogeneran. La estructura sigue siendo legible por la negrita preservada (`**Capítulo 1: ...**`). Si en el futuro Daniel cambia a usar estilos Heading nativos, el script empieza a generar `#`/`##` automáticamente sin tocar nada.

---

## Vínculos al ecosistema del libro

- **Briefing CoWork (esencia, voz, tono, dos & don'ts):** [`../briefing-cowork-libro-tu-valor-no-esta-en-su-mirada.md`](../briefing-cowork-libro-tu-valor-no-esta-en-su-mirada.md). Lectura obligatoria antes de proponer cambios de fondo.
- **Programa hermano del libro:** [`../../dejadebuscarteenotros.html`](../../dejadebuscarteenotros.html) (landing pública) + [`../../BRIEFING-PROGRAMA-DEJADEBUSCARTE.md`](../../BRIEFING-PROGRAMA-DEJADEBUSCARTE.md) (briefing operativo).
- **Vídeo-ensayo de YouTube que siembra el campo semántico:** [`../../contenido-rrss/youtube-dependencia-emocional-amor-vs-necesidad/guion.md`](../../contenido-rrss/youtube-dependencia-emocional-amor-vs-necesidad/guion.md) (publicación en mayo 2026, **no nombra el libro todavía**).
- **Reto 7 Días y newsletter «Te escribo»:** ambos forman parte del mismo universo. El libro es la pieza largoformato que cierra el círculo.

---

## Estado de iteración

| Fecha | Acción | Resultado |
|---|---|---|
| 7 may 2026 | Briefing CoWork redactado (`../briefing-cowork-libro-tu-valor-no-esta-en-su-mirada.md`) | Departamento CoWork situado en marca, voz, público y reglas editoriales. |
| 11 may 2026 | Daniel sube primer manuscrito al repo (`manuscrito-2026-05-11.docx` + `.md`) | El libro queda accesible para todas las sesiones de Claude. |
| 11 may 2026 | Script de extracción mejorado tras review de Copilot en PR #140 | `re.sub(r'(?<!\*)\*\*\*\*(?!\*)', '', output)` elimina artefactos `****` espurios del cierre + apertura bold adyacentes, sin tocar `***` (bold-italic) ni `*****` (bold-italic + bold). `.md` regenerado. |
| 11 may 2026 | Revisión específica del temario completada | Documento `revision-temario-2026-05-11.md` mapea los 16 capítulos reales, detecta inconsistencias entre índice anunciado y desarrollo, propone 4 acciones de prioridad alta y abre 5 decisiones editoriales que requieren conversación con Daniel. Veredicto: temario sólido conceptualmente, problemas son de gestión documental, no de fondo. |
| 11 may 2026 | `manuscrito-limpio-2026-05-11.md` generado tras petición explícita de Daniel | Versión editorial limpia del manuscrito v1: índice actualizado a los 16 capítulos reales con las 5 máscaras correctas (Salvadora · Radar · Complaciente · Devota · Víctima), notas estratégicas del consultor IA eliminadas, disclaimer clínico añadido en intro, placeholders explícitos en los huecos del embudo del audio. **NO se redactó contenido nuevo** — los 15 capítulos en estado de esqueleto se conservan como esqueleto. La Introducción, cap 8, Epílogo + Apéndice 21 días + Rompe-cristales y Nota final están redactados completos. Decisiones tomadas: Kohut+Freud (sin apego), voz neutra, disclaimer sí, foco B2C. Pendiente: completar URL y nombre de la landing del audio antes de imprimir. |
| **14 may 2026** | Daniel sube `manuscrito-2026-05-14.docx` (175 KB · ~2,5× la v anterior) tras 3 días de trabajo intenso de redacción | **Salto enorme**: 19 capítulos numerados redactados completos en prosa + 3 «Capítulos Nuevos» sin numeración final + 1 tránsito sobre el cuerpo entre Parte I y Parte II. La estructura pasa de 5 partes/16 caps (v 11 may) a 5 partes/22 piezas (v 14 may). Auditoría completa en `estado-completitud-2026-05-14.md` con mapa por capítulo, 4 inconsistencias internas detectadas (3 caps sin numerar · protocolo 21 días prometido pero ausente · anexo audio ausente · contraportada ausente), 2 decisiones editoriales aún abiertas, cronograma sugerido hasta lanzamiento KDP en julio 2026 sincronizado con el taller Volver a Mí. **Veredicto: ~92 % completo**. |
| **14 may 2026** | Daniel cierra las 4 inconsistencias internas: 3 caps → Intermedios sin numerar · Apéndice 21 días → recuperar · anexo audio → NO (libro físico) · portada y contraportada → adecuadas | Propuestas de edición concretas en `propuestas-edicion-libro-2026-05-14.md`: renombramientos exactos de los 3 Intermedios con párrafos de entrada redactados, texto completo del Apéndice 21 días adaptado al v 14 may (sin duplicar el rompe-cristales ni la nota final que ya están en caps 15 y 19), contraportada editorial redactada con voz Daniel, specs de portada para Amazon KDP 6×9" con paleta TWIM y tipografías Instrument Serif + Barlow Condensed. Pendiente · Daniel incorpora al `.docx` desde Word y vuelve a subir como `manuscrito-2026-05-15.docx` (o fecha del día). |

**Próximo paso operativo previsto:** iterar contenido del manuscrito. Daniel quiere perfeccionar el libro porque será fuente de ingresos cuando salga a la venta. Las propuestas concretas de iteración se anotarán aquí cuando se acuerden, junto con la versión a la que aplican.

### Pendientes editoriales detectados al revisar la versión 2026-05-11

Estos son puntos que **dependen de Daniel** — no se editan a tijeretazo desde Claude porque son contenido del libro, no artefactos de extracción. Aparecen aquí como recordatorio para la próxima sesión de iteración con Daniel:

- **Línea 948 del `.md`:** «`**2. LA LANDING PAGE (El Copy para )**`» — falta el nombre o referencia de la landing tras «El Copy para». Probablemente quedó pendiente al escribir.
- **Línea 433 del `.md`:** «`*****Self***** Hambriento`» con cinco asteriscos a cada lado del término *Self*. Posiblemente lo correcto era `***Self***` (bold italic, concepto clínico de Kohut) sin la negrita adicional. Revisar en Word y normalizar.
- **Otras ocurrencias de huecos editoriales**, `[CTA]`, `[URL]` o similares: cuando Daniel suba una nueva versión, conviene barrerlas todas y completarlas o convertirlas en placeholders explícitos con corchetes.

---

## Reglas para sesiones futuras de Claude

1. **Antes de proponer cambios al manuscrito**, leer:
   - El `.md` más reciente entero (al menos la parte que se pretende tocar).
   - El briefing CoWork (`../briefing-cowork-libro-tu-valor-no-esta-en-su-mirada.md`) para no romper la voz editorial.
   - Si el cambio toca terreno conceptual (mecanismo, máscaras, Kohut, ciclo), consultar también `BRIEFING-PROGRAMA-DEJADEBUSCARTE.md` para coherencia con el programa hermano.
2. **Nunca proponer reescrituras desde memoria.** Citar siempre el fragmento exacto del `.md` que se sugiere modificar, indicando línea o sección.
3. **Nunca sobrescribir** una versión anterior del manuscrito al añadir una nueva. Cada `.docx` queda como histórico, fechado.
4. **Cuando se acuerde una iteración**, registrar la decisión en este README → sección «Estado de iteración» (fecha + resumen del cambio + versión afectada).
5. **El `.docx` es la fuente canónica.** El `.md` se regenera; nunca se considera definitivo si entra en conflicto con el `.docx`.
