# Roadmap libros · audiolibros (ElevenLabs) + tapa blanda/dura (Amazon KDP) · 2026

> Documento operativo · 9 jun 2026 · sesión `claude/awesome-hopper-3ejG1`.
> Origen · Daniel plantea (9 jun, verbatim resumido): pasar a **audiolibro con su voz clonada (ElevenLabs)** *Los engranajes de la mente* (+ el extra) ahora, y el libro nuevo cuando salga en septiembre; y meter en **Amazon en tapa blanda/dura** *Los Engranajes* (+ el extra).
> Registrado como plan bajo regla simétrica + handoff. Las intenciones eran condicionales; aquí quedan como hoja de ruta con decisiones marcadas.
> **Cruza con:** `elevenlabs-clonacion-voz-podcast.md` (§9 ya lista el audiolibro; §4 disclosure; §2.2 entrenamiento de voz), `producto-engranajes-digital/README.md` (qué es «el extra»), `libro-tu-valor-no-esta-en-su-mirada/maquetacion/brief-word-kdp.md` (flujo KDP reutilizable), `youtube-podcast-estrategia-canal.md` §5 (ElevenLabs T2 septiembre).

---

## 0 · Qué es «el extra» (para no confundirlo)

«El extra» = **«De los engranajes a tu día»** (~10 págs). Hoy es el **diferenciador EXCLUSIVO** de la *edición digital ampliada* que se vende **directa desde la web a 9,90 €**, frente al **ebook de Amazon a 7,68 €** (`producto-engranajes-digital/README.md`). El extra es la razón por la que alguien paga +2 € y compra directo → más margen para Daniel y canal propio.

---

## 1 · Decisión sobre el extra · A vs B

> **Decisión provisional: A** (recomendación de Code; Daniel dio «vale» general el 9 jun). Si Daniel quiere B, se cambia y se actualiza este doc.

- **A (elegida) · el extra sigue exclusivo de la web.** En Amazon (tapa blanda/dura) va **solo la base** de *Los Engranajes* (la misma que el ebook). Protege el canal directo de más margen y no canibaliza el motivo de comprar la edición ampliada.
- **B · el extra va a todos lados** (incluido Amazon papel). Más simple, pero se pierde el diferenciador y el +margen del canal propio.

**Consecuencia operativa de A:** el audiolibro y la edición de papel de Amazon usan el **interior base** (sin el extra). El extra solo vive en la edición digital web (y, si se quiere, en un futuro audiolibro «ampliado» vendido directo desde la web).

---

## 2 · Audiolibros con voz clonada (ElevenLabs)

Encaja con lo ya escrito — el doc de ElevenLabs lista textualmente «Audiolibro de *Los engranajes de la mente*» (§9). Tres condiciones antes de lanzar:

### 2.1 · Prerrequisito · entrenar la voz una sola vez

- Hay que **entrenar el modelo de voz** primero (grabar **30-60 min de audio limpio**, `elevenlabs…md` §2.2). Sin modelo no hay audiolibro.
- **Esa misma grabación desbloquea también el podcast T2** (voz clonada, septiembre, `youtube-podcast…md` §5). → Se graba **una vez** y sirve para las dos cosas. No duplicar.
- Backup obligatorio del audio fuente (local + cloud cifrado + disco), `elevenlabs…md` §5.

### 2.2 · Disclosure obligatorio (no opcional)

- En el audiolibro hay que declarar que es **la voz de Daniel, sintetizada con clonación** (`elevenlabs…md` §4). Va en la descripción del producto y, idealmente, en una nota de audio al inicio.

### 2.3 · OJO con la tienda (lo que casi nadie sabe)

Según políticas a 2026 (verificar al subir, cambian):

| Tienda | ¿Admite voz clonada / narración IA? |
|---|---|
| **Audible / ACX** | **NO** · exige narración humana. Tu voz clonada probablemente se rechaza. |
| **Amazon KDP «Virtual Voice»** | Solo voces **de Amazon** (no tu clon). No sirve para «tu voz». |
| **Google Play Libros** | **SÍ** con disclosure · admite narración auto/IA. |
| **Spotify (vía Findaway Voices)** | **SÍ** con disclosure. |
| **Apple Books** | **SÍ** (narración digital) con disclosure. |
| **Venta directa desde tu web** | **SÍ**, control total (MP3/M4B con entrega tipo Cap III). |

→ **No dar por hecho que el audiolibro va en Amazon/Audible.** Ruta recomendada para tu voz clonada: **Google Play Libros + Spotify + Apple + venta directa**. Audible queda fuera mientras mantengan la regla anti-IA.

### 2.4 · Alcance

- **Ahora (tras DDBEO):** audiolibro de *Los engranajes* (interior **base**, decisión A).
- **Septiembre:** audiolibro del libro nuevo *«Tu valor no está en su mirada»* cuando se publique.

---

## 3 · Amazon tapa blanda / tapa dura (Los Engranajes · base)

### 3.1 · Lo bueno: el flujo ya está documentado

El **brief KDP** de *«Tu valor…»* (`…/maquetacion/brief-word-kdp.md`) es **reutilizable casi entero** para Engranajes: mismo trim 6×9, mismos estilos TWIM (Instrument Serif + Lora + Barlow Condensed), misma estructura de preliminares y mismos pasos de subida a KDP. Y ya hay **arte de tapa dura explorado** en el repo (`tapadurapixelada.png`, `contraportadadurapixelada.png`).

### 3.2 · Lo que falta de verdad

- **Interior maquetado para imprenta.** El PDF digital de la edición ampliada **no vale tal cual** (no tiene trim/márgenes/recto-verso de imprenta). Hay que maquetar el **texto base** de Engranajes con el brief (mismos estilos). Verificar antes si ya existe un interior de imprenta de Engranajes; si no, se maqueta.
- **Portada wraparound recalculada** con el conteo final de páginas (el lomo depende de las páginas; mismo proceso que el brief §10 — Daniel pasa el conteo, Code regenera la portada).
- **Tapa dura (delta):** KDP hardcover usa su propia plantilla de portada (lomo + solapa de caja distintos), mínimo 75 págs, acabado mate. Trim 6×9 disponible también en tapa dura.

### 3.3 · CHECKLIST · tapa blanda/dura de Los Engranajes (base)

```
[ ] 0. Confirmar decisión del extra (A = base sin extra en Amazon). ← hecho, provisional
[ ] 1. Conseguir el texto base de Engranajes en Word (sin el extra).
[ ] 2. Maquetar el interior con brief-word-kdp.md (trim 6×9, estilos TWIM,
       preliminares, numeración romana→árabe, recto en Partes/Capítulos).
[ ] 3. Exportar PDF de imprenta (fuentes embebidas, verificado en Acrobat) — brief §7.
[ ] 4. Pasar a Code el CONTEO FINAL de páginas.
[ ] 5. Code regenera la portada wraparound (tapa blanda) con el lomo exacto.
       Para tapa dura, generar además la portada con plantilla hardcover de KDP.
[ ] 6. KDP → Crear → Tapa blanda (y repetir para Tapa dura) en español.
       Vincular ambas al MISMO título/ASIN del ebook (B0FR8PSQT3) para que
       salgan como formatos en la misma página de producto.
[ ] 7. Datos: título, subtítulo, autor, descripción, 7 keywords, categorías
       (Psicología/Psicoanálisis). ISBN gratis de KDP.
[ ] 8. Subir interior + portada. Usar el Previsor de KDP página a página.
[ ] 9. Precio (psicología premium ES: tapa blanda ~14-18 €, tapa dura ~22-26 €).
[ ] 10. Publicar. Amazon revisa 24-72 h.
```

---

## 4 · Secuencia y capacidad (lo más importante de gestión)

Daniel va a tope. Para no solapar:

| Ventana | Foco | No meter aquí |
|---|---|---|
| **15 jun – 28 jul** | **Grabación DDBEO** (bloque grande ya comprometido) | Nada de audiolibro ni maquetación pesada. |
| **Agosto** (hueco) | **Maquetar + publicar tapa blanda/dura de Engranajes** · **grabar los 30-60 min de voz** y entrenar el modelo ElevenLabs · **producir el audiolibro de Engranajes** | — |
| **Septiembre** | Libro nuevo *«Tu valor…»* + **pre-venta Volver a Mí** (1 sep) + arranque **ElevenLabs T2** podcast | NO encajar aquí el audiolibro de Engranajes (se hace en agosto). El audiolibro del libro nuevo, cuando el libro esté publicado. |

**Regla:** la grabación de voz (§2.1) es la pieza que desbloquea audiolibro **y** podcast T2 → hacerla en **agosto** y todo lo demás cae detrás.

---

## 5 · Trazabilidad

- Decisión de origen: Daniel, 9 jun 2026 (intenciones condicionales registradas como plan). Decisión del extra: **A**, provisional, pendiente de confirmación explícita si se quiere B.
- Docs base: `elevenlabs-clonacion-voz-podcast.md`, `producto-engranajes-digital/README.md`, `libro-tu-valor-no-esta-en-su-mirada/maquetacion/brief-word-kdp.md`, `youtube-podcast-estrategia-canal.md`.
- Pendiente de Daniel: confirmar A/B del extra; pasar el texto base de Engranajes en Word para maquetar.
