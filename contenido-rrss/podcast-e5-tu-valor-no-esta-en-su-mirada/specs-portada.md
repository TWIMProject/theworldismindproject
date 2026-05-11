# Specs portada · TWIM Podcast E5 · «Tu valor no está en su mirada»

> Specs visuales del E5 reordenado el 11 may 2026 (ver §14 de
> `documentos-internos/youtube-podcast-estrategia-canal.md`).
> Generado por código en `generar-portadas.py` con la misma plantilla
> heredada del E5 original (ahora E6 autoexigencia).
> Plantilla base: `documentos-internos/plantillas/podcast/specs-visuales.md`.
> Sistema visual TWIM: paleta + Barlow Condensed + Playfair Display.

---

## Contenido editorial usado en este episodio

| Campo | Valor |
|---|---|
| Numero | `Ep.5` |
| Kicker | `Psicología Aplicada` |
| Título (2 líneas) | `TU VALOR NO ESTÁ` / `EN SU MIRADA` |
| Subtítulo paréntesis | `(el alivio de dejar de confundir amor con necesidad)` |
| Pie | `DANIEL OROZCO  ·  @daniorozcopsicologo` |

Cualquier ajuste de copy se hace editando `CONTENIDO_EPISODIO` en `generar-portadas.py` y re-ejecutando el script.

### Nota técnica del 11 may 2026

En la story vertical (1080×1920), el tamaño del título serif se redujo de 115 a 88 px porque «TU VALOR NO ESTÁ» (16 caracteres) excedía el ancho disponible al tamaño original. El sub-tamaño también bajó de 40 a 34 px para mantener proporción. Si en futuros episodios el título es más corto (≤12 caracteres por línea), se puede subir a 115 / 40 como en E6.

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

## Salidas y dimensiones

| Archivo | Formato | Dimensiones | Uso |
|---|---|---|---|
| `cover-youtube.png` | Horizontal | 1280 × 720 px (16:9) | Thumbnail YouTube. Subir vía YouTube Studio antes de publicar el vídeo. Peso ≤ 2 MB. |
| `cover-spotify.png` | Cuadrado | 1400 × 1400 px (1:1) | Variante por episodio para Spotify for Podcasters. Si se decide usar el cover canal estándar (`podcast-cover.png`), este archivo se conserva como respaldo pero no se sube. Peso ≤ 5 MB. |
| `story-vertical.png` | Vertical | 1080 × 1920 px (9:16) | Story de Instagram / Facebook anunciando el episodio. Acompañar con sticker «Link» a la URL del vídeo o a `/newsletter/` según objetivo del día. |

---

## Composición

Las tres portadas comparten estructura editorial:

1. **Foto autor** (`daniel-orozco-sillon.jpg` de la raíz del repo) con fade lateral / inferior hacia el verde oscuro de fondo. La foto ocupa ~50-58 % del lienzo según orientación.
2. **Eyebrow** en dos líneas:
   - Línea 1: `TWIM PODCAST` (Barlow Condensed Bold, tracked).
   - Línea 2: `Ep.X · Psicología Aplicada` (Barlow Condensed Medium, tracked menor).
3. **Separador horizontal** corto en beige `#C2A78B`.
4. **Título principal** en Playfair Display Bold (peso 700), 1-2 líneas, color crema, alineación izquierda en YouTube/Spotify y centrada en Story.
5. **Subtítulo entre paréntesis** en Playfair Display Italic, color beige, debajo del título.
6. **Pie inferior** con `DANIEL OROZCO  ·  @daniorozcopsicologo` en Barlow Condensed Bold tracked, beige.
7. **Logo MIND WORLD** (recortado del cover canal) en blanco translúcido, esquina inferior derecha.

El contenido editorial exacto del E5 está al inicio de este documento (sección «Contenido editorial usado en este episodio»). El ground truth visual es lo que produce `generar-portadas.py`.

---

## Flujo de generación

Estas portadas se producen **por código** con Pillow (no en Canva, no a mano). El script `generar-portadas.py` de esta misma carpeta es la fuente única de verdad. Para producir o regenerar las portadas:

```bash
python3 contenido-rrss/podcast-e5-tu-valor-no-esta-en-su-mirada/generar-portadas.py
```

Para cambiar copy del episodio: editar el dict `CONTENIDO_EPISODIO` al principio del script y re-ejecutar. Sin Canva, sin export manual.

Dependencias:
- **Pillow**: `pip install Pillow`.
- **Tipografías**: Barlow Condensed (Regular/Medium/Bold) + Playfair Display Variable (`PlayfairDisplay-VF.ttf`) + Playfair Display Italic Variable (`PlayfairDisplay-Italic-VF.ttf`). El script las busca en `$TWIM_FONTS_DIR` si está definido, después en `/root/.local/share/fonts/`, después en `~/.local/share/fonts/`. Si no encuentra alguna, falla con error claro. Descarga: repo oficial `google/fonts`.
- **Foto autor**: `daniel-orozco-sillon.jpg` en la raíz del repo (ya presente).

---

## Verificación pre-publicación

- [ ] Las 3 portadas existen en esta carpeta y se ven correctamente al abrirlas.
- [ ] Test de legibilidad del thumbnail YouTube al 30 %: el título sigue siendo legible.
- [ ] Sin emojis, sin caras gritando, sin flechas / círculos / zooms.
- [ ] Paleta y tipografía coherentes con el resto del canal y con el sistema visual TWIM.
- [ ] Story al 9:16 con el título completo dentro de los márgenes (no cortado por los bordes).
- [ ] Subido a YouTube Studio + Spotify for Podcasters + IG Stories según corresponda.

---

## Refs

- Plantilla base: `documentos-internos/plantillas/podcast/specs-visuales.md`
- Sistema visual IG (PR #94): `documentos-internos/instagram-sistema-visual-marca.md`
- Cover canal existente: `podcast-cover.png` en raíz del repo.
