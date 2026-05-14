# Portada · libro «Tu valor no está en su mirada»

> Carpeta creada el **14 may 2026** tras la decisión de Daniel de subir la portada/contraportada como PDF a Amazon KDP (no recurrir a Cover Creator).
>
> **Estado a 14 may 2026 (tercer movimiento del día):**
> - v1 (verde TWIM dominante) **descartada por Daniel** por no cumplir el criterio dopamina-comercial.
> - v2 con tres conceptos alternativos (A · ojo · B · cuerda · C · llave) documentados en `conceptos-portada-v2.md`.
> - **Daniel elige el Concepto C «La llave dentro»** (paleta crema + verde botella + acentos dorados + ilustración minimalista de llave).
> - Maqueta tipográfica y compositiva regenerada en `portada-front-preview.pdf` y `portada-wraparound-kdp.pdf` con la paleta del Concepto C y **placeholder** centrado para la ilustración real de la llave (que produce diseñador o flujo IA generativa).
>
> **Regla aplicable:** las piezas de venta TWIM se diseñan bajo el criterio dopamina-comercial (`CLAUDE.md` + `documentos-internos/marca-twim-criterio-dopamina-comercial.md`).

---

## 1 · Archivos en esta carpeta

| Archivo | Función | Estado |
|---|---|---|
| `portada-front-preview.pdf` | Maqueta de la portada delantera (6.25 × 9.25" con sangrado) en Concepto C · paleta crema + texto verde botella + placeholder centrado de la llave. | v2 con placeholder |
| `portada-wraparound-kdp.pdf` | Maqueta wraparound back+spine+front en el formato KDP. | v2 con placeholder · **NO subir a KDP hasta integrar la ilustración real de la llave** |
| `conceptos-portada-v2.md` | Los 3 conceptos visuales propuestos tras descarte de v1 (A·ojo · B·cuerda · C·llave) + comparativa + recomendación. | ✅ |
| `brief-diseno-portada-v2-concepto-c.md` | Dirección artística completa para producir la ilustración de la llave (diseñador humano o IA generativa) + prompts sugeridos + checklist de validación + integración técnica con el script. | ✅ |
| `README.md` | Este documento. | ✅ |

El script reproducible que genera ambos PDFs vive en `scripts/generar-portada-libro-tu-valor.py`.

---

## 2 · Parámetros de la versión 2 (Concepto C)

| Parámetro | Valor | Notas |
|---|---|---|
| Formato | Tapa blanda Amazon KDP | El más vendido para no-ficción en español. |
| Trim size | 6 × 9 pulgadas (15,24 × 22,86 cm) | Estándar KDP. |
| Sangrado | 0,125 pulgadas (3,175 mm) cada lado | Obligatorio KDP. |
| Páginas asumidas | **185** | **Provisional · punto medio del rango 170-200 estimado**. Recalcular cuando Daniel termine la maquetación y conozca el conteo real. |
| Ancho de lomo | 0,417 pulgadas (10,6 mm) | Calculado con fórmula KDP papel blanco/crema: páginas × 0,002252". Por estar entre 0.25" y 0.5", el script imprime versión reducida del lomo solo con título corto (sin autor ni sello rotados). |
| Wraparound total | 12,667 × 9,25 pulgadas | Back + spine + front + sangrados. |
| Paleta | Fondo crema cálido `#F4EDE0` · texto verde botella `#1F4A3A` · acentos dorados `#C19E5A` · cuerpo en negro suave `#3D3530` | Concepto C de `conceptos-portada-v2.md`. |
| Tipografía | Times-Roman + Times-Italic + Helvetica · **placeholders built-in** | La versión final debe usar **Instrument Serif** (titulares) + **Barlow Condensed** (kickers, body). Las built-ins son aproximación visual razonable para que Daniel revise composición y peso. |
| Ilustración central | **Placeholder** rectangular 1.5 × 1.5" centrado | El diseñador o flujo IA generativa produce la ilustración real según `brief-diseno-portada-v2-concepto-c.md`. |

---

## 3 · Composición de la versión 1

### Front cover (portada delantera)

Tres bloques verticales sobre fondo verde oscuro con sutil viñeta interior de verde medio:

- **Tercio superior** · «DANIEL OROZCO ABIA» en beige sobre filete decorativo.
- **Tercio medio** · Título «Tu valor / no está / en su mirada» en serif grande (56 pt) sobre crema. Subtítulo «El alivio de dejar de confundir amor con necesidad» en italic 18 pt beige.
- **Tercio inferior** · Sello «MIND WORLD PROJECT» + tagline «PSICOLOGÍA PROFUNDA Y APLICADA».

### Lomo

Con 0,563 pulgadas (14,3 mm) hay margen para texto rotado. Distribución:

- Título completo arriba (rotado 90°, leído cabeza arriba).
- Autor abajo (rotado 90°, leído cabeza arriba).
- Sello «MIND WORLD / PROJECT» en el centro (dos líneas, no rotado).

### Back cover (contraportada)

- Kicker «PSICOLOGÍA PROFUNDA Y APLICADA» en beige + filete.
- Copy editorial en cinco párrafos (voz Daniel sostenida, sin emojis, sin frases motivacionales).
- Frase aforística de cierre en italic beige: *«No se trata de no necesitar a nadie. Se trata de que necesitar no te destruya.»*
- Bio del autor (Col. CV11515, libros previos, TWIM Project).
- Caja blanca para ISBN + código de barras EAN-13 (placeholder · KDP genera el real al subir el manuscrito).
- Footer con sello + `twimproject.com`.

---

## 4 · Cómo iterar

### Si Daniel quiere cambios en el copy

Editar las constantes de texto en `scripts/generar-portada-libro-tu-valor.py` y volver a ejecutar:

```bash
python3 scripts/generar-portada-libro-tu-valor.py
```

Cualquier sesión futura puede modificar el script sin romper nada — los PDFs se regeneran encima.

### Si cambia el conteo de páginas

Modificar la constante `NUM_PAGES` al inicio del script y volver a ejecutar. El ancho del lomo se recalcula automáticamente con la fórmula KDP `páginas × 0.002252"`.

### Si Daniel quiere probar otras paletas

El script propone Opción A (verde dominante). Para probar Opción B (crema dominante) o Opción C (imagen sutil), modificar las funciones `draw_front()` y `draw_back()` con las paletas alternativas documentadas en `propuestas-edicion-libro-2026-05-14.md` §4.3.

### Cuando se quieran las fuentes correctas

Descargar Instrument Serif y Barlow Condensed (Google Fonts, gratis) como TTF. Registrarlas en el script con `pdfmetrics.registerFont(TTFont(...))` y sustituir las llamadas a `Times-Roman` / `Helvetica` por los nombres registrados.

---

## 5 · Validación antes de subir a KDP

Antes de subir el `portada-wraparound-kdp.pdf` a Amazon KDP, verificar manualmente:

- [ ] El conteo de páginas asumido (250) coincide con el conteo real tras maquetación del interior. Si no, recalcular el lomo regenerando el PDF.
- [ ] Las dimensiones del wraparound coinciden con las que KDP exige para 6×9" + tu conteo de páginas (KDP tiene calculadora en su flujo de publicación; pegar las dimensiones del PDF generado debe dar verde).
- [ ] El sangrado de 0,125" en cada lado está respetado (los elementos visuales importantes están como mínimo a 0,25" del trim line interior).
- [ ] El ISBN del placeholder se sustituye por el real generado por KDP (KDP lo genera automáticamente y reemplaza el código de barras en su flujo, así que el placeholder se borra antes de subir o se confía en que KDP lo cubra).
- [ ] No hay imágenes con copyright (esta versión no usa imágenes).
- [ ] Las fuentes built-in (Times-Roman + Helvetica) **se sustituyen por Instrument Serif + Barlow Condensed** antes del envío final. Esta v1 es para revisión visual de Daniel, no para imprenta.

---

## 6 · Notas de licencias

- **Fuentes Instrument Serif y Barlow Condensed** · Google Fonts, licencia SIL Open Font, uso libre incluido comercial. Verificar antes de imprimir que la fundición no cambia condiciones.
- **Times-Roman y Helvetica** (placeholders v1) · fuentes core PostScript, libres para cualquier uso. La versión final no las usa, así que no aplica para imprenta.
- **Colores TWIM** · paleta propietaria del proyecto, documentada en CLAUDE.md.

---

**Última actualización:** 14 may 2026 · sesión `claude/improve-proposal-quality-pq3d9` · v1 mock para revisión.
