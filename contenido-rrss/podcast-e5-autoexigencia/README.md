# TWIM Podcast E5 · Autoexigencia

> Carpeta del episodio piloto T1 (primer episodio del nuevo formato grabación humana).
> Pilar: Autoexigencia.
> Ventana publicación: 12-18 mayo 2026 (idealmente martes 12 mayo, antes de la Carta #2 del 19 mayo).

---

## Archivos en esta carpeta

| Archivo | Contenido | Estado |
|---|---|---|
| `guion.md` | Guion completo del episodio (~2.900 palabras, 16 min 30 s reales tras edición) | ✅ generado 5-may-2026 · grabado y editado 6-may-2026 |
| `caption-youtube.md` | Título + descripción + capítulos + tags YouTube | ✅ generado 5-may-2026 |
| `caption-spotify.md` | Título + descripción corta Spotify | ✅ generado 5-may-2026 |
| `specs-portada.md` | Specs portada YouTube horizontal 1280×720 + Spotify 1:1 | ✅ generado 5-may-2026 |
| `cover-youtube.png` | Portada YouTube 1280×720 (thumbnail) | ✅ generado 6-may-2026 vía `generar-portadas.py` |
| `cover-spotify.png` | Portada Spotify 1400×1400 (Opción B, variante por episodio) | ✅ generado 6-may-2026 vía `generar-portadas.py` |
| `video-fondo.png` | Pantalla estática 1920×1080 para reproducción YouTube (zona inferior libre para subtítulos) | ✅ generado 6-may-2026 vía `generar-portadas.py` |
| `generar-portadas.py` | Script Pillow que recompone las 3 portadas a partir de `podcast-cover.png` raíz. Reusable en E6+ cambiando el bloque `CONTENIDO_EPISODIO`. | ✅ generado 6-may-2026 |
| `audio-bruto.wav` | Grabación bruta del episodio | ✅ grabado 6-may-2026 |
| `audio-final.mp3` | Audio final con intro/outro y normalización · 16 min 30 s | ✅ editado 6-may-2026 |

---

## Material editorial reciclado

Para que cualquier compañero futuro pueda verificar la trazabilidad sin re-investigar:

- `dejadeobligarte.html` — landing del programa, hero del pilar.
- `insights/senales-vivir-en-obligacion.html` — 15 señales (cognitivas, corporales, conductuales). Sección 2 del guion.
- `insights/del-deberia-al-quiero-ejercicios.html` — distinción debería/quiero. Sección 4 del guion.
- `insights/como-dejar-de-hacer-las-cosas-por-obligacion.html` — mapa completo del mecanismo + ejemplo correo. Sección 3 y 5 del guion.
- `insights/juez-interno-como-desactivar.html` — referenciado solo como puente a la Carta #2 (NO se profundiza en este episodio para no canibalizar la newsletter).

---

## Conexión con calendario editorial

| Fecha | Pieza | Pilar | Estado |
|---|---|---|---|
| 12-18 mayo (ventana) | **E5 podcast (este episodio)** | Autoexigencia | ⏳ pendiente grabación |
| 19 mayo 19:00 | Carta #2 "La voz que te juzga" (newsletter) | Autoexigencia (juez interno) | ✅ programada en MailerLite |

El E5 trata el **mandato de autoexigencia como estructura general**. La Carta #2 del 19 mayo profundiza una pieza concreta dentro de esa estructura: **el juez interno**. Por eso el cierre del E5 (Sección 6) anuncia explícitamente la Carta #2 del 19 mayo como continuación natural.

> **Nota editorial:** la Carta #2 es deliberadamente DISTINTA al podcast — los suscriptores de "Te escribo" reciben contenido exclusivo, no derivado. Coherencia con la nota editorial de `carta-02-la-voz-que-te-juzga.txt`.

---

## Workflow de producción referenciado

- Workflow §3.1 del doc #5 (`reciclaje-contenido-pipeline.md`).
- Hoja de cronometraje E5: `documentos-internos/cronometraje-episodio-piloto-e5.md` (rellenar mientras grabas).
- Plantillas: `documentos-internos/plantillas/podcast/`.

---

## Próximos pasos operativos (lado Daniel)

1. **Leer el guion completo en voz alta** una vez antes de grabar. Marcar palabras donde tropieces para regrabar después.
2. **Cronometrar** la lectura completa con la hoja `cronometraje-episodio-piloto-e5.md` abierta. Si pasa de 22 min, recortar; si baja de 16 min, expandir secciones cortas.
3. **Diseñar portada YouTube** en Canva siguiendo `specs-portada.md`. Decidir si Spotify reusa `podcast-cover.png` (Opción A recomendada) o produce variante (Opción B).
4. **Grabar** en bloque único o por secciones (5 secciones independientes encajan bien). No re-grabar a media frase: re-grabar la frase completa y limpiar en Audacity.
5. **Edición rápida** según workflow §3.1 paso 5 (Audacity: limpieza + normalización + intro + outro).
6. **Subir a YouTube** (con `caption-youtube.md`) y **Spotify** (con `caption-spotify.md`).
7. **Completar la hoja de cronometraje** con tiempos reales.
8. Tras 30 días: rellenar la sección de métricas de la hoja de cronometraje y traer datos para actualizar el doc #5 §3.1 con estimaciones reales (no inventadas).

---

## Trazabilidad

Generado el 5 mayo 2026 siguiendo regla `CLAUDE.md` "leer el repo primero" recién mergeada. Todo el contenido del guion proviene de material editorial existente del repo, sin invención propia. Cualquier sesión futura que retoque este episodio debe verificar la trazabilidad de los párrafos contra los artículos `insights/` referenciados arriba.
