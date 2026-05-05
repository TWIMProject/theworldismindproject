# Specs portada · TWIM Podcast E5

> Specs visuales para producir en Canva o herramienta equivalente.
> Plantilla base: `documentos-internos/plantillas/podcast/specs-visuales.md`.
> Sistema visual TWIM: paleta + tipografía Barlow Condensed.

---

## Sistema visual común (recordatorio)

| Atributo | Valor |
|---|---|
| Verde oscuro | `#173D30` |
| Verde medio | `#265C4B` |
| Beige | `#C2A78B` |
| Fondo claro | `#FDFCFA` |
| Tipografía | Barlow Condensed (Regular/SemiBold/Bold/ExtraBold) |
| Logo TWIM | `LOGO.png` o `logo-mindworld.png` |
| Cover canal podcast | `podcast-cover.png` (en raíz del repo) |

Sin emojis. Sin caras gritando. Sin flechas rojas, círculos amarillos ni efectos de zoom.

---

## Portada YouTube · horizontal 1280×720 (16:9)

| Atributo | Valor |
|---|---|
| Dimensiones | 1280 × 720 px |
| Peso máximo | 2 MB |
| Aspect ratio | 16:9 |
| Color de fondo | Verde oscuro `#173D30` con sutil gradiente diagonal hacia verde medio `#265C4B` (135°, suave, no llamativo) |
| Tipografía | Barlow Condensed Bold para título principal, Regular para metadatos |

### Composición

**Lado izquierdo (60% del ancho):**

- **Eyebrow** (kicker arriba): `TWIM PODCAST · E5`
  - Tamaño: 28-32 px
  - Color: beige `#C2A78B`
  - Letter-spacing: 2-3 px
  - Mayúsculas

- **Título principal** (4 palabras, dos líneas):
  - Línea 1: `EL MANDATO`
  - Línea 2: `DE NO PARAR`
  - Tamaño: 90-110 px
  - Color: beige `#C2A78B`
  - Peso: Bold o ExtraBold
  - Alineación: izquierda
  - Line-height: 0.95 (líneas pegadas)

- **Subtítulo descriptivo** (debajo del título principal):
  - Texto: `Autoexigencia y culpa de descansar`
  - Tamaño: 36-42 px
  - Color: beige claro `#FDFCFA` con 70% opacidad o crema
  - Peso: Regular
  - Alineación: izquierda

- **Pie inferior izquierda:**
  - Texto: `Daniel Orozco Abia · CV11515`
  - Tamaño: 22-26 px
  - Color: beige `#C2A78B` con 60% opacidad

**Lado derecho (40% del ancho):**

- **Cover unificado del podcast** (`podcast-cover.png`) reescalado a ~520×520 px, centrado verticalmente, con un margen interno (no que toque los bordes del lienzo).
- O alternativa: bloque visual minimalista — un trazo o forma geométrica en beige sobre el verde, sin elementos figurativos.

### Test de legibilidad

- Reducir el thumbnail al 30% de tamaño y verificar que `EL MANDATO DE NO PARAR` se sigue leyendo. Si no, simplificar a 3 palabras (`MANDATO DE NO PARAR`).
- Verificar que el subtítulo "Autoexigencia y culpa de descansar" se lee al tamaño de smartphone vertical (~150 px de ancho).

---

## Portada Spotify · cuadrada 1400×1400 (1:1)

> Spotify exige cover cuadrado mínimo 1400×1400 px (recomendado 3000×3000 para mantener calidad en pantallas retina). Si Daniel ya tiene un cover canal `podcast-cover.png` que cumple, **se puede mantener** ese sin variante por episodio (estrategia consistente del canal).
>
> **Decisión a tomar por Daniel:** ¿usar el cover canal estándar o producir variante por episodio?

### Opción A · cover canal estándar (recomendada para T1)

Reusar `podcast-cover.png` para los 8 episodios T1 (mayo-agosto). Coste 0, máxima consistencia visual.

Argumentos a favor:
- Spotify y plataformas de hosting muestran el cover canal asociado al episodio si no hay artwork específico.
- En T1 (mayo-agosto, 8 episodios) la consistencia visual ayuda al reconocimiento de marca.
- Variantes por episodio se pueden introducir desde T2 (septiembre+) cuando el canal tenga más volumen.

### Opción B · variante por episodio (si Daniel quiere diferenciar visualmente)

| Atributo | Valor |
|---|---|
| Dimensiones | 1400 × 1400 px (mínimo) o 3000 × 3000 px (recomendado) |
| Aspect ratio | 1:1 |
| Color base | Verde oscuro `#173D30`, mismo de la portada YouTube (consistencia) |

### Composición Opción B

**Composición central, jerárquica vertical:**

- **Eyebrow arriba:**
  - Texto: `TWIM PODCAST`
  - Tamaño: 60 px
  - Color: beige `#C2A78B`
  - Letter-spacing: 4 px
  - Mayúsculas
  - Posición: centro horizontal, ~150 px desde arriba

- **Número de episodio:**
  - Texto: `E5`
  - Tamaño: 200 px
  - Color: beige `#C2A78B` con 40% opacidad
  - Peso: ExtraBold
  - Posición: centrado, debajo del eyebrow

- **Título principal** (centrado, dos líneas):
  - Línea 1: `EL MANDATO`
  - Línea 2: `DE NO PARAR`
  - Tamaño: 120 px
  - Color: beige `#C2A78B`
  - Peso: Bold
  - Line-height: 0.95

- **Subtítulo:**
  - Texto: `Autoexigencia y culpa de descansar`
  - Tamaño: 50 px
  - Color: beige claro / crema (70% opacidad)
  - Peso: Regular

- **Pie centrado:**
  - Texto: `Daniel Orozco Abia · CV11515 · Valencia`
  - Tamaño: 32 px
  - Color: beige `#C2A78B` con 60% opacidad
  - Posición: ~150 px desde abajo

- **Logo TWIM** (`logo-mindworld.png`) abajo, centrado, ~80 px de altura.

### Test de legibilidad Opción B

- Reducir al 5% (cover en buscador Spotify) y verificar que al menos `E5` y `EL MANDATO` se distinguen.
- Verificar contraste sobre fondo verde oscuro: el beige `#C2A78B` cumple WCAG AA sobre `#173D30`.

---

## Recomendación para E5

**Ir con Opción A (cover canal estándar) para Spotify** y **producir portada YouTube horizontal específica del E5**.

Razones:
- YouTube necesita thumbnail diferenciado por vídeo para el algoritmo (vídeos con thumbnail genérico tienen menor CTR).
- Spotify en cambio asocia el episodio al cover canal sin penalización algorítmica si no hay variante.
- En T1 (mayo-agosto) priorizamos velocidad de producción; las variantes Spotify por episodio pueden introducirse en T2.

---

## Verificación pre-publicación

### Para portada YouTube

- [ ] Archivo final 1280×720 px, peso ≤ 2 MB.
- [ ] Test de legibilidad al 30% superado.
- [ ] Paleta y tipografía coherentes con sistema visual TWIM.
- [ ] Sin emojis, sin elementos prohibidos.
- [ ] Subido a YouTube Studio antes de publicar el vídeo.

### Para Spotify

- [ ] Si Opción A: el cover canal `podcast-cover.png` se aplica automáticamente al episodio.
- [ ] Si Opción B: archivo 3000×3000 px (o mínimo 1400×1400), peso ≤ 5 MB, formato JPG o PNG.
- [ ] Subido al hosting (Spotify for Podcasters / Buzzsprout / equivalente).

---

## Lo que sí queda manual fuera del repo

- **Diseñar las portadas en Canva** o herramienta equivalente. El repo deja las specs textuales — el archivo visual final lo produce un humano (o diseñador externo cuando entre la VA en sept).
- **Subir al sitio correspondiente** (YouTube Studio + Spotify for Podcasters).

---

## Refs

- Plantilla base: `documentos-internos/plantillas/podcast/specs-visuales.md`
- Sistema visual IG (PR #94): `documentos-internos/instagram-sistema-visual-marca.md`
- Cover canal existente: `podcast-cover.png` en raíz del repo.
