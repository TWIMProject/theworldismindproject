# Setup de grabación · Módulo 1 «El Mapa»

> Cómo grabar el módulo con tu cara + slides en pantalla sincronizada.
> Pensado para hacer en una tarde con setup ya existente. ~30 min de preparación, 25-35 min de grabación, 15 min de export.

---

## 1 · Material necesario

- **Ordenador** (Mac o Windows) con Chrome instalado
- **Cámara web o cámara externa** + iluminación lateral (ventana o lámpara, no contraluz)
- **Micrófono** decente (lavalier, USB tipo Yeti o Rode NT-USB). NO el del portátil.
- **Software de grabación con doble fuente** (cámara + pantalla simultánea). Recomendado: **OBS Studio** (gratis, Mac/Win).
- Los slides: `documentos-internos/programa-deja-de-buscarte-en-otros/slides/modulo-01-el-mapa-slides.html`
- El script: `documentos-internos/programa-deja-de-buscarte-en-otros/modulos/01-el-mapa-script.md` (con marcas `[▶ SLIDE N]` ya integradas)

**Alternativa low-budget si no tienes OBS:** grabas vídeo con cámara/móvil aparte + grabas pantalla con QuickTime (Mac) o Xbox Game Bar (Win), después los combinas en CapCut/iMovie/Premiere. Más trabajo en post, pero funciona.

---

## 2 · Setup OBS (10 min · una sola vez)

1. Descarga **OBS Studio** desde https://obsproject.com (Mac/Windows, gratis)
2. Crea una **Escena nueva** llamada «Módulo Programa»
3. Añade dos **fuentes** a esa escena:
   - **Dispositivo de captura de vídeo** → tu cámara → cuadro pequeño abajo-derecha o abajo-izquierda
   - **Captura de pantalla / display** → tu monitor donde abrirás Chrome con los slides → ocupa el resto
4. Posiciona la cámara como un cuadro de ~25-30% del ancho total, en una esquina. Los slides ocupan el resto.
5. Configuración → Audio → asegurarte de que está seleccionado tu micrófono USB/lavalier (no el del Mac)
6. Configuración → Vídeo → Resolución base **1920×1080** · Resolución salida **1920×1080** · FPS **30**
7. Configuración → Salida → Formato grabación **MP4** · Códec **H264** · Bitrate vídeo **8000-12000 kbps**
8. **Test:** pulsa «Iniciar grabación», graba 30 segundos saludando + pasando 1-2 slides, verifica que la cámara se ve, la pantalla se ve, el audio entra. Borrar test.

---

## 3 · Setup de la pantalla de slides

1. Abre el archivo `slides/modulo-01-el-mapa-slides.html` en **Chrome** (no Safari, no Firefox — Chrome respeta mejor las fuentes Google Fonts en pantalla completa).
2. Pulsa **F** en el teclado para entrar en pantalla completa.
3. Verifica que ves el slide 1 (portada «Deja de Buscarte en Otros · Módulo 1 · El Mapa»).
4. Probar navegación: **flecha derecha** → siguiente · **flecha izquierda** → anterior · **F** → salir pantalla completa.
5. Volver al slide 1 (pulsar **Home** o flecha izquierda hasta llegar).

**Importante:** Chrome a veces oculta el cursor del ratón en pantalla completa después de unos segundos sin movimiento — bien, porque OBS no lo capta como ruido visual.

---

## 4 · Antes de grabar (5 min · cada sesión)

- **Cierra notificaciones:** modo «No molestar» en el sistema, silencia WhatsApp / Telegram / Mail
- **Cierra todo lo demás** en Chrome (no quieres que aparezca otra pestaña por error)
- **Bebe agua y carraspea** — la voz necesita estar suelta los primeros 30 segundos
- **Abre el script** en el móvil o en una pestaña aparte (no en la pantalla que estás grabando) para poder consultar
- **Posición:** sentado, espalda recta, micro a 15-20 cm de la boca, mirando a cámara cuando lo dice el script ([A CÁMARA])
- **Iluminación:** ventana a tu lado o lámpara grande lateral. NO de frente (deslumbra), NO detrás (silueta)

---

## 5 · Durante la grabación

1. En OBS, pulsa **Iniciar grabación**
2. Cuenta hasta 3 mentalmente (para tener margen de corte en post)
3. Empiezas con **Slide 1 visible** y di la apertura del script
4. Cuando el script marque `[▶ SLIDE N]`, pulsa **flecha derecha** una vez. El slide pasa con fade suave.
5. Lee con naturalidad. **No tienes que recitar el script palabra por palabra** — el script es la base, tú improvisas alrededor manteniendo la estructura.
6. Si te equivocas, **no pares la grabación.** Di simplemente «vamos a por la siguiente toma de este bloque» y repite el párrafo. En post se corta.
7. Las pausas marcadas `[PAUSA]` son reales: mantén silencio 2-3 segundos. Da peso a lo dicho.
8. Los `[A CÁMARA]` significan: levanta los ojos del guion y mira directo a la lente. Conexión.

**Cuando termines el slide 22 (cierre), pulsa Detener grabación.**

---

## 6 · Edición post (15-30 min)

Edita en CapCut / Final Cut / Premiere / DaVinci Resolve:

1. Importa el archivo MP4 resultante
2. Corta los principios y finales (cuentas atrás, errores)
3. **No edites cortes en mitad de un párrafo del script.** Mejor que se note una pausa larga que un corte que rompe ritmo.
4. **Normaliza audio** a -16 LUFS (estándar streaming)
5. **No añadas música de fondo.** Voz limpia. Si quieres pequeño «ambiente», ruido marrón al -45 dB. No más.
6. **No añadas intro / outro animados.** El slide 1 y el slide 22 ya hacen ese trabajo.
7. **Texto sobreimpreso opcional:** si en alguna frase quieres reforzar la cita («Margen», «No es tu culpa») puedes añadir texto en pantalla unos segundos. Mínimo intervencionismo.
8. Export final: **MP4 H264 · 1080p · 30fps · bitrate 8000-12000**

**Tamaño esperado del MP4 final:** 200-400 MB para 25-30 min a 1080p. Si va al alojamiento Vimeo Pro, Vimeo lo recodifica y el archivo final reproduce a calidades adaptativas.

---

## 7 · Subir a alojamiento

Recomendación: **Vimeo Pro** (12 €/mes plan «Standard» o «Advanced»). Razones:
- Privacidad real (videos no indexables, no rastreables por buscadores)
- Sin anuncios al espectador
- Player limpio embebible
- Acceso por link sin login para los compradores
- Quality automático según conexión del espectador
- Estadísticas básicas de visualización

Alternativa más barata: **YouTube oculto**. Gratis pero el link es público (cualquiera con él lo ve), y al cliente le aparece sugerencias de otros videos al final. Menos premium. Solo lo recomiendo si vas a probar el producto con baja inversión y luego migrar.

---

## 8 · Checklist final antes de mandar el primer link al primer comprador

- ✅ MP4 del Módulo 1 subido a Vimeo Pro
- ✅ Configurado como «Solo con link» (no público)
- ✅ Reproducido en otra ventana/incógnito para verificar acceso
- ✅ Audio se escucha bien en altavoces pequeños (móvil) y grandes
- ✅ Cámara y slides están sincronizados (no hay desfase audio-video)
- ✅ Los 22 slides aparecen completos
- ✅ El link añadido al email post-pago Stripe

---

## 9 · Para los próximos módulos

Una vez que hayas grabado el Módulo 1 con éxito, los Módulos 2-5 son repetir el mismo patrón:
- Esperar a tener el script desarrollado (pedírmelo cuando quieras)
- Generar slides correspondientes (estructura ya establecida con Módulo 1, replicable en 15 min de mi parte por módulo)
- Grabar siguiendo este mismo README

**Tiempo total estimado por módulo después del primero:** 1.5-2h (preparación + grabación + edición).

---

## 10 · Si algo falla

- **OBS no detecta tu cámara:** preferencias → seguridad → cámara → permitir OBS. Reinicia OBS.
- **Audio sale con eco / dos veces:** desactiva el micro del Mac en OBS, deja solo el USB/lavalier
- **Los slides no se ven a pantalla completa con la tipografía bonita:** verifica conexión a Internet (las Google Fonts se cargan desde CDN). Sin Internet caen a fonts genéricas. Para grabar sin Internet, dime y empaqueto las fonts dentro del HTML.
- **El cursor del ratón aparece sobre los slides en la grabación:** mueve el ratón fuera del área de captura antes de empezar, o usa OBS para recortar el cursor.

Si surge cualquier otra cosa, dímelo y resolvemos.
