# Brief de diseño · Portada v2 · Concepto C «La llave dentro»

> Concepto **elegido por Daniel el 14 may 2026** entre las 3 opciones documentadas en `conceptos-portada-v2.md` tras descartar la v1 por no cumplir el criterio dopamina-comercial.
>
> Este brief es la dirección artística completa para el diseñador humano o el flujo de IA generativa (Midjourney, DALL-E 3, Adobe Firefly, Leonardo) que produzca la **ilustración real de la llave dorada con cordel** que va en el centro de la portada delantera. La maqueta del libro (composición tipográfica, paleta, fondos, contraportada, lomo) ya está generada con reportlab en `portada-front-preview.pdf` y `portada-wraparound-kdp.pdf` con un placeholder rectangular en la zona de la llave.

---

## 1 · Brief en una frase

> Ilustración minimalista y editorial de una **pequeña llave dorada con cordel suave**, vista de frente, sobre fondo cálido crema, en estilo dibujo de línea moderna con peso medio · transmite intimidad doméstica + descubrimiento sereno · sin esoterismo, sin religiosidad, sin frialdad.

---

## 2 · Referencias visuales

Tres autores cuya portada nos sirve como vector estético:

- **«Atlas of the Heart» · Brené Brown.** Fondo cálido + ilustración minimalista + tipografía clásica.
- **«El dilema de la pareja» · Esther Perel.** Verde sobrio + minimalismo editorial premium europeo.
- **«Untamed» · Glennon Doyle.** Calidez intimista + ilustración delicada.

Lo que **no** queremos:

- Fotografía realista de una llave (suena a hardware de cerrajería).
- Llave en estilo «vintage llave antigua dorada» (sugiere mística esotérica).
- Cualquier acabado tipo «stock photo» de banco de imágenes.
- Tipografía display agresiva tipo bestseller-aeropuerto.
- Filtros vintage o de Instagram envejecido.

---

## 3 · Especificaciones técnicas de la ilustración

| Parámetro | Valor |
|---|---|
| **Formato de entrega** | PNG con fondo transparente · 300 dpi · perfil sRGB |
| **Dimensiones finales** | 1500 × 1500 px mínimo (escalable sin pérdida en KDP 6×9") |
| **Estilo** | Dibujo de línea moderno editorial · trazo medio uniforme |
| **Color principal del trazo** | Verde botella `#1F4A3A` |
| **Color del relleno de la llave** | Dorado mate `#C19E5A` (no oro brillante metalizado) |
| **Color del cordel** | Beige cálido `#A88A6E` o crema más oscuro que el fondo |
| **Sombras y luces** | Mínimas · ligero degradado en la cabeza de la llave para dar volumen sin convertir en realismo |
| **Composición** | Llave vertical o ligeramente inclinada · cordel cayendo en curva natural por uno de los lados o reposando en círculo abierto |
| **Tamaño de la llave en el lienzo** | Llenar 60-70 % del cuadrado · espacio respirable alrededor |

---

## 4 · Anatomía de la llave (composición)

La llave tiene tres partes y cada una vehiculiza un significado clínico:

- **Cabeza (parte superior, donde se sostiene la llave con los dedos):**
  - Forma circular, ovalada o lobulada simple. Nada barroco.
  - Por donde pasa el cordel.
  - Esta parte concentra el dorado más visible · el «brillo» de la llave.

- **Tija (cuerpo central, parte vertical más larga):**
  - Simple, sin ornamentos.
  - Mate, no brillante.

- **Paletón (parte inferior, dientes de la llave):**
  - Limpio, geométrico. Dos o tres dientes sencillos.
  - Da pie a leer la metáfora: «esta llave abre algo concreto».

**Cordel:** suave, anudado limpiamente a la cabeza · cae con movimiento natural · no enroscado ni rígido. Color beige cálido o crema más oscuro que el fondo principal.

---

## 5 · Composición sobre el placeholder

La zona reservada en `portada-front-preview.pdf` es un **cuadrado de 1.5 × 1.5 pulgadas** (≈ 38 × 38 mm) centrado horizontalmente en la portada, en la zona alta-media. Coordenadas exactas en pulgadas dentro del trim 6 × 9":

- X centrado · de 2.25 a 3.75 pulgadas (centro = 3.0")
- Y vertical · de aproximadamente 4.50 a 6.00 pulgadas desde el borde inferior

El diseñador debe encajar la ilustración dentro de esa caja, **respetando un margen visual de ≈ 0.1"** alrededor (para que no toque exactamente los límites).

---

## 6 · Prompt sugerido para IA generativa (Midjourney v6, DALL-E 3, Adobe Firefly)

> **Prompt en inglés (las IA gráficas funcionan mejor en inglés):**
>
> `minimalist editorial illustration of a small golden key with a soft beige cord, vertical key with simple oval head and clean geometric teeth, gold flat shading without metallic shine, dark bottle-green line drawing style #1F4A3A, transparent background, warm cream tone reference, calm intimate aesthetic similar to Brené Brown's "Atlas of the Heart" cover, no realism, no vintage style, no esoteric symbolism, no religious motifs, 1500x1500px, sRGB, 300dpi, editorial book cover quality, european publishing aesthetic`
>
> **Negative prompt:**
>
> `realistic photo, vintage style, esoteric, religious symbolism, ornate, baroque, fantasy, gothic, brass texture, metallic shine, hardware catalog, stock photo, instagram filter, blurry, low resolution`

Generar **3-5 variantes** con la misma prompt + variaciones de inclinación de la llave (vertical, ligeramente inclinada a la derecha, ligeramente inclinada a la izquierda) y elegir la que mejor case con el peso del título debajo.

Si el diseñador es humano: el prompt arriba sirve como descripción del entregable.

---

## 7 · Validación de la ilustración antes de integrar

Antes de subir la portada definitiva a KDP, comprobar:

- [ ] La llave se reconoce como llave en miniatura ≤ 150 px (tamaño de thumbnail Amazon). Si no se lee, simplificar.
- [ ] La llave funciona en blanco y negro · convertir a B&W y verificar que sigue siendo legible (algunas búsquedas Amazon usan thumbnails B&W).
- [ ] El cordel no parece soga ni nudo de horca. Si lo parece, suavizar la caída y simplificar el nudo.
- [ ] La llave no parece llave de hotel / llave maestra / símbolo masón. Si lo parece, simplificar.
- [ ] El dorado no compite con el verde botella del título · queda en segundo plano cromático.
- [ ] Hay espacio respirable alrededor de la llave dentro del cuadrado de 1.5".

---

## 8 · Integración técnica con la maqueta reportlab

Una vez producida la PNG de la llave:

1. Guardar como `documentos-internos/libro-tu-valor-no-esta-en-su-mirada/portada/llave-ilustracion.png`.
2. Modificar el script `scripts/generar-portada-libro-tu-valor.py` · en la función `draw_front`, sustituir el bloque del placeholder por un `c.drawImage(...)` apuntando al PNG real.
3. Volver a ejecutar `python3 scripts/generar-portada-libro-tu-valor.py`.
4. Los dos PDFs (`portada-front-preview.pdf` y `portada-wraparound-kdp.pdf`) se regeneran con la llave real integrada.
5. Validar visualmente y subir a KDP.

Si Daniel quiere que Code haga este último paso (integrar el PNG en el script), basta con que pegue el archivo en la sesión de Claude o lo suba al repo · Code modifica el script y regenera los PDFs.

---

## 9 · Alternativas si la IA generativa no da resultado satisfactorio

Si tras 3-5 iteraciones de IA generativa no se llega a una ilustración aceptable:

- **Plan B · diseñador humano.** Contratar ilustrador editorial freelance (referencias · Fiverr nivel profesional, Behance buscando «editorial book illustration», o ilustradores españoles tipo @hattie.stewart, @perico_pastor, @malota_studio en Instagram). Coste estimado 80-250 € para una pieza simple como esta. Tiempo 3-7 días.
- **Plan C · ilustración propia + retoque IA.** Daniel dibuja a mano una llave en papel (cualquiera vale como base) y un flujo de IA tipo Adobe Firefly «Generative Fill» limpia y estiliza el resultado. Más artesanal y con sello personal.

---

## 10 · Estado actual

- ✅ Concepto C elegido por Daniel.
- ✅ Maqueta con placeholder generada por reportlab (`portada-front-preview.pdf`, `portada-wraparound-kdp.pdf`).
- ✅ Brief de diseño completo (este documento).
- ⚠️ **Pendiente** · producción de la ilustración de la llave (IA o diseñador humano).
- ⚠️ **Pendiente** · integración del PNG en el script y regeneración de los PDFs finales.
- ⚠️ **Pendiente** · ajuste del lomo cuando se conozca el conteo final de páginas tras la maquetación interior.

**Una vez producida la ilustración + integrada + recalculado el lomo = portada lista para subir a Amazon KDP.**

---

**Última actualización:** 14 may 2026 · sesión `claude/improve-proposal-quality-pq3d9`.
