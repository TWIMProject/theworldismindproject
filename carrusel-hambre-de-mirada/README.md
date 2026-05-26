# Carrusel #4 IG · «3 escenas de hambre de mirada»

> Sistema visual **A2 crema** · 1080×1350 (4:5) · 8 slides · companion editorial de la Carta #3 «Hambre de mirada» con ángulo distinto (no canibaliza · regla `plan-captacion-verano-2026.md` S21).

## Decisión editorial · 26 may 2026

Tras la auditoría a 7 días del Carrusel #3 (`documentos-internos/metricas-carrusel-3-voz-que-te-juzga-19-may-2026.md`) la causa dominante del infrarrendimiento es **hipótesis B (señales acumuladas de cuenta)** · 94,3 % de visualizaciones del #3 vinieron de seguidores, solo 5,7 % de no-seguidores. La cuenta está en distribución cerrada.

**Decisión Daniel (verbatim · 26 may 21:25):** «No esperemos al carrusel 5 y hagamos el 4 con formato Carrusel pero A2 crema y foto creada con IA para romper expectativa del algoritmo.»

## Cambios sobre el Carrusel #4 anterior (A1 verde 1080×1080)

| Variable | Versión previa | Versión actual |
|---|---|---|
| Sistema visual | A1 verde dominante | **A2 crema dominante** |
| Formato | 1080×1080 (cuadrado) | **1080×1350 (4:5)** · spec correcto del sistema visual |
| Slide 1 | Tipográfico puro | **Foto IA + tipografía** |
| Slides 2-8 | Tipográficos verde | **Tipográficos crema** |
| Copy | (mismo) | (mismo · ya pasó review editorial) |

## Cómo añadir la foto IA al slide 1

1. **Generar la foto** con DALL-E / ChatGPT image / Sora usando el prompt de §3.
2. **Guardar** en esta carpeta como `foto-hook.jpg` (también acepta `.jpeg`, `.png`, `.webp`).
3. **Ejecutar**:
   ```bash
   python3 documentos-internos/plantillas/generar-carrusel-hambre-de-mirada.py
   ```
   El script detecta el archivo y lo incorpora al slide 1 con recorte tipo cover (1080×720 superior).

Si no existe `foto-hook.*` el slide 1 se genera con un placeholder gris claro para que veas el layout sin bloquear.

## Prompt foto IA · principal (recomendado)

Escena · «escaneando el móvil antes de enviar el mensaje».

```
Photograph, vertical 4:5 ratio, cinematic still from an intimate Spanish indie film.
A woman in her late thirties, soft expression of contained worry — not crying, not
dramatic, just slightly suspended — looking down at her phone in her hands. Natural
side light from a window out of frame, warm muted afternoon light, golden hour
fading. Visible texture of skin and fabric, no makeup look. She wears a beige
linen shirt, neutral background of a softly out-of-focus kitchen or living room
with cream walls, warm wood tones, no clutter, no other people, no text, no logo.
The composition leaves the upper two-thirds for the subject and the bottom third
should be quieter, with empty soft-focus space for typography to be added later.
Color palette: warm creams, soft beiges, muted greens in the background like
#173D30 toned down to ambient shadow, no saturated reds or blues. Shallow depth
of field, 35mm lens feel, grain subtle, naturalistic, editorial. Mood: the silent
moment of re-reading a message three times before sending it. No phone screen
content visible, no notifications. Anti-stock, anti-clickbait, no smiling, no
influencer pose.
```

### Variante B · «escaneando la cara del otro al entrar»

```
Same style as above. Vertical 4:5 cinematic still. A woman in her late thirties,
just having entered a softly lit Spanish apartment hallway, looking past the
camera with a quick searching glance — the half-second she reads someone else's
face before saying hello. Warm interior light from a lamp, cream walls, wooden
floor, soft shadow on her cheek. Slightly off-center composition, lower third
quieter for text. Muted naturalistic palette aligned with creams, beiges, warm
greens in shadow. No other figures visible. Editorial documentary feel, no
makeup look, anti-stock.
```

### Variante C · «pedir perdón sin causa» (manos)

```
Same style as above. Vertical 4:5 cinematic still. Close shot from above of a
woman's hands together on her lap, slightly fidgeting, fingers loosely
interlaced. Beige linen trousers, warm afternoon light from the left, soft
cream background out of focus, possibly a kitchen table edge. The hands tell
the story of someone about to apologize without cause. Lower third quieter for
text. Naturalistic warm palette, muted creams and beiges. No face visible.
Anti-stock, editorial intimacy.
```

## Qué evitar al elegir la foto

- Sonrisa forzada, ojos a cámara, pose tipo influencer.
- Lágrimas, manos en la cara estilo «desesperación».
- Paletas saturadas (rojos, azules, magentas).
- Fondos urbanos genéricos, estética stock.
- Texto / logos / pantallas con contenido visible.
- Más de una persona en el encuadre.

## Cuándo NO usar foto IA

Si la foto resultante no encaja con la marca o resulta ambigua, **mejor publicar sin foto** (slide 1 tipográfico A2 puro). El experimento es romper expectativa del algoritmo, no rebajar coherencia editorial.

## Pendientes Daniel antes de publicar

- [ ] Generar foto IA con el prompt (§3) y guardarla como `foto-hook.jpg`.
- [ ] Re-ejecutar el script para que slide 1 incorpore la foto real.
- [ ] Revisar los 8 slides visualmente.
- [ ] Programar en Meta Business Suite (horario sugerido · 20:00 hora Madrid, miércoles o jueves, en línea con la regla de cambiar señales del algoritmo).
- [ ] Auditar a 7 días en doc paralelo al del Carrusel #3.
