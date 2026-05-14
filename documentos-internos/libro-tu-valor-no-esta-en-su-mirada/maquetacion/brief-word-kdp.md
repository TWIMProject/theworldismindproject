# Brief de maquetación · «Tu valor no está en su mirada» · Word → Amazon KDP

> Daniel maqueta el interior del libro él mismo en Microsoft Word. Este brief documenta el setup completo + estilos + pasos + checklist para exportar el PDF que sube a Amazon KDP.
>
> Procedencia: brief redactado el 14 may 2026 en sesión `claude/improve-proposal-quality-pq3d9` a partir de los specs KDP de Amazon, el sistema visual TWIM canónico y la estructura real del manuscrito v 14 may.

---

## 0 · Antes de empezar (15 min · una sola vez)

### 0.1 · Descargar fuentes gratuitas

Tres fuentes de Google Fonts (gratis, licencia SIL OFL, uso comercial permitido):

1. **Instrument Serif** — titulares de partes y capítulos. https://fonts.google.com/specimen/Instrument+Serif
2. **Lora** — cuerpo de texto. Versión Regular + Italic + Bold. https://fonts.google.com/specimen/Lora
3. **Barlow Condensed** — kickers, encabezados de página, numeración. Versión Regular + Bold. https://fonts.google.com/specimen/Barlow+Condensed

Descargar cada una desde Google Fonts (botón «Download family»), descomprimir los `.zip`, y hacer doble clic en cada archivo `.ttf` → «Instalar» en Windows / Font Book → «Instalar» en macOS.

Reiniciar Word tras instalar las fuentes para que aparezcan en el desplegable.

### 0.2 · Crear el archivo de maquetación

Abrir Word → Archivo → Nuevo → Documento en blanco → guardar como `manuscrito-maquetado-v1.docx` en `documentos-internos/libro-tu-valor-no-esta-en-su-mirada/maquetacion/`.

Copiar el contenido del `manuscrito-2026-05-14.docx` (o la versión más reciente que tengas) al nuevo archivo. No copiar el formato del original — pegar como texto sin formato (Pegado especial → Sin formato) para empezar limpio.

---

## 1 · Configuración del documento (15 min · una sola vez)

### 1.1 · Tamaño y márgenes

Word → Disposición → Tamaño → Más tamaños de papel → Personalizado:

- **Ancho:** 6 pulgadas (15,24 cm)
- **Alto:** 9 pulgadas (22,86 cm)

Word → Disposición → Márgenes → Personalizado:

- **Superior:** 0,75" (1,9 cm)
- **Inferior:** 0,75" (1,9 cm)
- **Interior (medianil):** **0,75" (1,9 cm)** ← importante para encuadernación
- **Exterior:** 0,5" (1,27 cm)
- **Encuadernación:** 0
- **Posición del medianil:** Izquierda
- **Múltiples páginas:** seleccionar **Márgenes simétricos**

Sin sangrado en el interior del libro. KDP no requiere sangrado en el interior salvo que haya imágenes que se vayan al borde.

### 1.2 · Pie y encabezado

Word → Disposición → Configurar página → pestaña Diseño:

- **Distancia desde el borde — encabezado:** 0,5" (1,27 cm)
- **Distancia desde el borde — pie de página:** 0,5" (1,27 cm)
- **Encabezados y pies diferentes en páginas pares e impares:** activado
- **Primera página diferente:** activado (para que el inicio de cada capítulo no tenga encabezado)

### 1.3 · Idioma del documento

Word → Revisar → Idioma → Establecer idioma de corrección → **Español (España)** + activar «Detectar idioma automáticamente» desactivado. Esto fuerza que el corrector ortográfico funcione siempre en castellano.

---

## 2 · Estilos a definir (45-60 min · una sola vez)

Word → Inicio → panel Estilos (Alt+Ctrl+Shift+S) → crear / modificar los siguientes estilos.

### 2.1 · Título 1 · Partes («Parte I», «Parte II»…)

Modificar el estilo «Título 1»:

- **Fuente:** Instrument Serif Regular
- **Tamaño:** 36 pt
- **Color:** verde TWIM oscuro `#173D30` (en Word: Más colores → Personalizado → 23, 61, 48)
- **Alineación:** Centrada
- **Espacio antes:** 144 pt (≈ 5 cm, para empujar al centro de la página)
- **Espacio después:** 36 pt
- **Salto de página antes:** activado en el propio estilo (cada Parte empieza en página nueva).
- **Página recto (impar):** esto **no** se configura en el estilo · es un tipo de salto que se inserta manualmente justo antes de cada Heading 1. Pasos en Word: situar el cursor justo antes del título de Parte → pestaña Disposición → Saltos → en el bloque «Saltos de sección», elegir **«Página impar»**. Word automáticamente inserta una página en blanco si la página actual está en par, para que la Parte siempre empiece en página impar (lado derecho del libro abierto).

### 2.2 · Título 2 · Capítulos («Capítulo 1», «Capítulo 2»…)

Modificar el estilo «Título 2»:

- **Fuente:** Instrument Serif Regular
- **Tamaño:** 24 pt
- **Color:** verde TWIM oscuro `#173D30`
- **Alineación:** Centrada
- **Espacio antes:** 96 pt
- **Espacio después:** 24 pt
- **Salto de página antes:** activado en el propio estilo.
- **Página recto (impar):** igual que con Heading 1 · se inserta manualmente un salto de sección «Página impar» antes de cada Heading 2 (Disposición → Saltos → Página impar). Word automáticamente añade página en blanco si hace falta.
- **Mantener con el siguiente:** activado.

### 2.3 · Título 3 · Subapartados internos del capítulo

Modificar el estilo «Título 3»:

- **Fuente:** Instrument Serif Regular
- **Tamaño:** 14 pt
- **Color:** verde TWIM medio `#265C4B` (en Word: 38, 92, 75)
- **Alineación:** Izquierda
- **Espacio antes:** 18 pt
- **Espacio después:** 6 pt
- **Sin salto de página antes**

### 2.4 · Cuerpo de texto

Modificar el estilo «Normal» o crear «Cuerpo libro»:

- **Fuente:** Lora Regular
- **Tamaño:** 11 pt
- **Color:** **no usar el negro puro `#000000`**. Mejor un negro suave editorial · `#1a1a1a` (en Word: Color de fuente → Más colores → Personalizado → introducir RGB **26 · 26 · 26**). Se ve más cálido en imprenta KDP y reduce fatiga lectora.
- **Alineación:** Justificada
- **Interlineado:** Múltiple, 1,4
- **Sangría de primera línea:** 0,25" (0,635 cm) — pero **no** en la primera línea tras un Heading
- **Espacio antes:** 0
- **Espacio después:** 0
- **Sin viudas ni huérfanas:** Activado (Word: Formato → Párrafo → Líneas y saltos de página)

### 2.5 · Cita / aforismo

Crear estilo nuevo «Cita libro»:

- **Fuente:** Lora Italic
- **Tamaño:** 11 pt
- **Color:** verde TWIM oscuro `#173D30`
- **Alineación:** Izquierda
- **Sangría izquierda:** 0,5"
- **Sangría derecha:** 0,5"
- **Espacio antes y después:** 6 pt

### 2.6 · Observaciones al final de capítulo

Las «*observaciones*» que aparecen en el manuscrito al final de los capítulos (en cursiva). Crear estilo «Observación»:

- **Fuente:** Lora Italic
- **Tamaño:** 10,5 pt
- **Color:** verde TWIM medio `#265C4B`
- **Alineación:** Izquierda
- **Sangría izquierda:** 0,5"
- **Espacio antes:** 24 pt (separación visual del cuerpo)
- **Sin sangría primera línea**

### 2.7 · Separador «···»

Crear estilo «Separador»:

- **Fuente:** Barlow Condensed Regular
- **Tamaño:** 14 pt
- **Color:** beige TWIM `#C2A78B` (en Word: 194, 167, 139)
- **Alineación:** Centrada
- **Espacio antes:** 12 pt
- **Espacio después:** 12 pt

Aplicar al carácter `···` (tres puntos centrados, ya está en el manuscrito como separador entre escenas).

### 2.8 · Encabezado par (verso)

Word → Insertar → Encabezado → Editar encabezado (en página par):

- **Texto:** DANIEL OROZCO ABIA (en mayúsculas, letter-spacing manual con espacios)
- **Fuente:** Barlow Condensed Regular
- **Tamaño:** 9 pt
- **Color:** verde TWIM oscuro `#173D30`
- **Alineación:** Izquierda

### 2.9 · Encabezado impar (recto)

En página impar:

- **Texto:** Tu valor no está en su mirada
- **Fuente:** Lora Italic
- **Tamaño:** 9 pt
- **Color:** verde TWIM oscuro `#173D30`
- **Alineación:** Derecha

### 2.10 · Pie de página · Numeración

En ambos pies (par e impar):

- **Fuente:** Barlow Condensed Regular
- **Tamaño:** 9 pt
- **Color:** verde TWIM oscuro `#173D30`
- **Alineación:** Centrada
- **Contenido:** número de página

---

## 3 · Estructura del libro · orden de páginas (1h · construcción)

KDP recomienda que las páginas «recto» (impar, lado derecho cuando el libro está abierto) sean inicio de sección importante. Esto fuerza el siguiente orden:

| Página | Lado | Contenido |
|---|---|---|
| i | recto | **Half title** · solo el título, centrado, en grande. Página decorativa. |
| ii | verso | Blanco |
| iii | recto | **Portadilla completa** · título + subtítulo + autor + sello editorial al pie |
| iv | verso | **Página legal** · ISBN, copyright, créditos, depósito legal |
| v | recto | **Dedicatoria** (si Daniel quiere) o blanco |
| vi | verso | Blanco |
| vii | recto | **Índice** |
| viii | verso | Blanco |
| ix | recto | **Nota al lector** (las 7 notas que ya están en el manuscrito) |
| x | verso | Continuación de la nota o blanco |
| xi | recto | **Introducción · El hambre de mirada** |
| ... | | (continúa la introducción) |
| 1 | recto | **Parte I · El mapa — El origen del vacío** (página de portadilla de parte) |
| 2 | verso | Blanco |
| 3 | recto | **Capítulo 1 · El brillo en los ojos** |
| ... | | (continúa el manuscrito) |

**Regla:** las páginas i-x van numeradas con **romanos minúsculos**. Las páginas a partir de la portadilla de Parte I van con **árabes**, empezando en **1**.

### 3.1 · Cómo cambiar la numeración a romanos al principio

Word → Insertar → Número de página → Formato de los números de página → Formato de número → seleccionar `i, ii, iii…` → Empezar en → `i`.

A partir de la Parte I, insertar un salto de sección (Disposición → Saltos → Sección · Página siguiente) y en el pie de la nueva sección, **desvincular del encabezado anterior** (botón «Vincular al anterior» en la cinta del encabezado · desactivar). Luego cambiar formato a `1, 2, 3…` → Empezar en `1`.

### 3.2 · Páginas en blanco que pueden quedar

Si al cerrar un capítulo la siguiente parte/capítulo tiene que empezar en página recto (impar) y el capítulo terminó en página impar, Word inserta una página en blanco automáticamente. Esto es lo correcto en libros. No quitar esas páginas en blanco.

---

## 4 · Aplicar estilos al manuscrito (6-10h · trabajo principal)

### 4.1 · Estrategia recomendada

1. Pegar el manuscrito en blanco de formato (Pegar especial → Sin formato).
2. Aplicar el estilo «Cuerpo libro» a todo el documento de una vez (Ctrl+A → click en el estilo).
3. Recorrer el documento de arriba abajo aplicando los estilos correctos a cada elemento:
   - Cada `**Parte I · El mapa**` → Título 1
   - Cada `**CAPÍTULO 1**` con el título debajo → Título 2 (consolidar en una línea o dejar en dos según gusto editorial: «Capítulo 1 · El brillo en los ojos» o «Capítulo 1» en una línea + «El brillo en los ojos» en otra de menor tamaño)
   - Cada `**X · Y**` interno de capítulo (escenarios, máscaras) → Título 3
   - Cada `*texto en cursiva*` → marcar como cursiva (Ctrl+I)
   - Cada `**texto en negrita**` → marcar como negrita (Ctrl+B)
   - Cada `···` (separador entre escenas) → estilo «Separador»
   - Cada bloque que parece observación al final de capítulo (en cursiva, indentado) → estilo «Observación»
   - Las citas/aforismos en frases sueltas en cursiva → estilo «Cita libro»

### 4.2 · Capítulos especiales

- **INTERMEDIO ENTRE CAPÍTULO X Y Y** (los 3 intermedios) → mismo estilo Título 2 que los capítulos pero **sin** salto a página recto (que empiece en la página que toque, par o impar, para no romper el ritmo).
- **TRÁNSITO ENTRE PARTE I Y PARTE II** → mismo tratamiento.
- **APÉNDICE PRÁCTICO · 21 días de mapa de salida** → Título 1 (igual que Parte), porque cierra el libro como pieza propia.

### 4.3 · Drop cap (letra capital al inicio de capítulo) · opcional

Convención editorial premium: la primera letra del cuerpo de cada capítulo va en mayúscula grande de 3-4 líneas de alto, en serif distinta del cuerpo. Si te gusta, configurar:

Word → Insertar → Letra capital → En texto → Configurar:

- **Fuente:** Instrument Serif
- **Líneas:** 3
- **Distancia desde el texto:** 0,1"
- **Color:** beige TWIM `#C2A78B`

Aplicar al primer párrafo de cada capítulo después del Heading 2.

Si no, dejar el primer párrafo del capítulo sin sangría de primera línea (queda más sobrio y editorial).

---

## 5 · Páginas preliminares · texto exacto a maquetar

### 5.1 · Half title (pág. i)

Solo el título centrado, en Instrument Serif 36-40 pt, color verde oscuro, a media altura de la página:

```
Tu valor no está
en su mirada
```

### 5.2 · Portadilla (pág. iii)

```
[Centrado]

TU VALOR NO ESTÁ EN SU MIRADA
(Instrument Serif 28 pt, verde oscuro)

El alivio de dejar de confundir amor con necesidad
(Lora Italic 14 pt, beige)

[Espacio]

Daniel Orozco Abia
(Barlow Condensed Bold 14 pt mayúsculas, beige)

[Espacio amplio hacia abajo]

MIND WORLD PROJECT
(Barlow Condensed Bold 11 pt, verde oscuro · en el pie)
```

### 5.3 · Página legal (pág. iv)

```
[Cuerpo en Lora Regular 9 pt, alineación izquierda]

Tu valor no está en su mirada
El alivio de dejar de confundir amor con necesidad

© Daniel Orozco Abia, 2026
Todos los derechos reservados.

Primera edición · [mes y año de publicación]

ISBN: [generado por Amazon KDP]
Depósito legal: [si aplica]

Editado y publicado por
Daniel Orozco Abia
TWIM Project · The World Is Mind Project
https://twimproject.com
equipo@twimproject.com

Diseño de portada · [tu nombre o el del diseñador]
Maquetación · Daniel Orozco Abia

Reservados todos los derechos. Esta obra no puede ser reproducida,
ni registrada, ni transmitida, total o parcialmente, mediante
ningún sistema de almacenamiento de información sin permiso por
escrito del titular del copyright. La infracción de los derechos
mencionados puede ser constitutiva de delito contra la propiedad
intelectual (arts. 270 y siguientes del Código Penal).

Este libro tiene fines divulgativos y no sustituye la atención
clínica profesional. Si lo que lees en sus páginas se acompaña de
sintomatología clínica seria, busca a un profesional cualificado
al lado del que sostener el proceso.

En España, atención a la conducta suicida: 024.
Emergencias: 112.

Impreso bajo demanda · Amazon Kindle Direct Publishing.
```

### 5.4 · Dedicatoria (pág. v) · opcional

Si Daniel quiere dedicatoria, una sola línea centrada en la mitad de la página, Lora Italic 12 pt, color verde medio. Ejemplo (sustituir por la real):

```
A quienes llegaron tarde a la mirada y aprendieron a esperarla.
```

Si no quiere dedicatoria, esta página queda blanca.

### 5.5 · Índice (pág. vii)

Word puede generar el índice automáticamente:

Referencias → Tabla de contenido → Tabla de contenido personalizada:

- Mostrar niveles: 2 (solo Partes y Capítulos)
- Formato: Personalizado (modificar después fuente a Lora 10 pt, color verde oscuro)
- Mostrar números de página: sí
- Alinear números de página a la derecha: sí
- Carácter de relleno: punto

Word genera el índice basándose en los Heading 1 y Heading 2 ya aplicados. Si añades/quitas capítulos, click derecho sobre el índice → Actualizar campos → Actualizar todo.

### 5.6 · Nota al lector

Las **7 notas** ya están redactadas al inicio del manuscrito v 14 may. Solo pegarlas con el estilo «Cuerpo libro» y conservar la negrita inicial de cada nota (la palabra «Una», «Dos», «Tres»…).

---

## 6 · Páginas finales del libro

### 6.1 · Después del Capítulo 19

Tras el último párrafo del Cap 19 («Si has llegado hasta aquí, ya has empezado. Cuídate.»), añadir salto a página recto y empezar el **Apéndice 21 días** con el texto que está en `propuestas-edicion-libro-2026-05-14.md` §2.2 listo para pegar.

### 6.2 · Sobre el autor · página recto al final · opcional

Una página con:

- Foto de Daniel en blanco y negro o con tratamiento verde (tamaño 4-5 cm de alto), arriba.
- Bio extensa de 2-3 párrafos. Coherente con la bio canónica de CLAUDE.md:

```
Daniel Orozco Abia es Psicólogo General Sanitario, colegiado en
Valencia con el número CV11515, en consulta privada desde 2012.
Formado en psicoanálisis, psicología del self, psicología profunda
y psicología aplicada.

Es autor de dos libros previos · Los engranajes de la mente —
comprendiendo el Yo, el Ello y el Superyó y Burnout · el libro
para no petar. Tu valor no está en su mirada es su tercer libro
y el primero centrado específicamente en dependencia emocional.

Fundador y CEO de TWIM Project · The World Is Mind Project, la
plataforma editorial-clínica desde la que divulga psicología
profunda y aplicada en YouTube, Instagram (@daniorozcopsicologo)
y la newsletter Te escribo.

Vive y trabaja en Valencia.
```

### 6.3 · Última página · web del autor · opcional

Página final con datos web sobrios:

```
[Centrado, Lora Italic 11 pt, beige]

Si lo que has leído aquí te ha movido algo,
en twimproject.com encontrarás más.

Newsletter «Te escribo» · cada tanto, una carta
sobre la mente, el cansancio y lo que no se dice.

twimproject.com/newsletter

[Pie de página]
@daniorozcopsicologo
```

No vender el programa explícitamente — Daniel decidió el 14 may **no cross-sell explícito en el libro**. Esto es solo direccionar a la web donde el funnel se gestiona aparte.

---

## 7 · Exportar el PDF para subir a KDP (30 min)

### 7.1 · Verificaciones previas a exportar

Antes de exportar, recorrer el documento desde el principio:

- [ ] Páginas preliminares numeradas con romanos (i, ii, iii…).
- [ ] Páginas del cuerpo numeradas con árabes empezando en 1 en la portadilla de Parte I.
- [ ] Cada Parte empieza en página recto (impar).
- [ ] Cada Capítulo empieza en página recto (impar).
- [ ] Los Intermedios y el tránsito **no** fuerzan página recto · empiezan donde toque.
- [ ] El índice está actualizado (click derecho → Actualizar campos).
- [ ] Encabezados visibles en cuerpo, no en preliminares ni en inicios de capítulo (Word inserta «Primera página diferente» en cada sección).
- [ ] No hay líneas viudas u huérfanas al final/inicio de página (revisar manualmente).
- [ ] No hay palabras cortadas raras al final de línea (revisar guionado).
- [ ] Texto justificado en todo el cuerpo · sin párrafos sueltos en alineación izquierda por error.
- [ ] Corrector ortográfico ha pasado (Revisar → Ortografía y gramática).

### 7.2 · Exportar como PDF de calidad de imprenta

Word → Archivo → Exportar → Crear PDF/XPS → click «Crear PDF/XPS» → en el diálogo:

- **Tipo:** PDF (.pdf)
- **Optimizar para:** **Estándar (publicación en línea e impresión)** — NO «Tamaño mínimo».
- **Opciones** (botón Opciones a la derecha):
  - Intervalo de páginas: Todo
  - Información no imprimible: desactivar todo
  - Opciones PDF:
    - **Compatible con ISO 19005-1 (PDF/A):** desactivado (KDP no lo necesita y a veces da problemas)
    - **Texto de mapa de bits cuando las fuentes no se pueden incrustar:** activado (failsafe)

Guardar como `manuscrito-maquetado-v1-interior.pdf` en la misma carpeta.

### 7.3 · Verificar que las fuentes están embebidas

Abrir el PDF generado con Adobe Acrobat Reader gratis. Archivo → Propiedades → pestaña Fuentes. Todas las fuentes (Instrument Serif, Lora, Barlow Condensed) deben aparecer con el sufijo **«Embedded»** o **«Embedded Subset»**.

Si alguna fuente no está embebida, KDP rechaza el PDF. Solución: en Word, abrir Archivo → Opciones → Guardar → activar «Incrustar fuentes en el archivo» y «Incrustar solo los caracteres usados en el documento». Volver a exportar.

### 7.4 · Si Word no consigue embeber Instrument Serif

Posible problema: Word no embebe display fonts gratuitas porque su licencia se interpreta como «embebible solo para impresión», no para distribución digital. Tres soluciones:

1. **Mejor opción:** convertir los titulares de Instrument Serif a imagen (rasterizar) usando Adobe Acrobat o herramientas online. Conservas el visual y embeber deja de ser problema.
2. **Sustituto editorial cercano:** cambiar Instrument Serif por **Cormorant Garamond** (Google Fonts, gratis, sí embeber). Aspecto muy similar.
3. **Sustituto más amplio:** **EB Garamond** (Google Fonts, clásico, embeber sin problemas).

Si haces sustitución, hazla en todos los Heading 1, Heading 2 y Heading 3 + en la portadilla. Regenerar el PDF y verificar.

---

## 8 · Subir a Amazon KDP

### 8.1 · Cuenta y proyecto

- Acceder a https://kdp.amazon.com con la cuenta de Daniel.
- + Crear → Tapa blanda en español.
- Datos del libro:
  - Idioma: Español (Castellano)
  - Título: «Tu valor no está en su mirada»
  - Subtítulo: «El alivio de dejar de confundir amor con necesidad»
  - Autor: Daniel Orozco Abia
  - Edición: 1
  - Descripción: [redactar 300-400 palabras siguiendo el copy de contraportada — Code lo prepara aparte si Daniel lo pide]
  - Palabras clave: 7 slots (Code los propone aparte)
  - Categorías: «Salud, mente y cuerpo > Psicología > Psicoanálisis» + «Familia y relaciones > Relaciones interpersonales > Amor y romance»

### 8.2 · Detalles del libro

- ISBN: Obtener uno gratis de KDP (recomendable salvo que Daniel quiera comprar uno propio del ISBN español, lo cual es opcional).
- Tipo de publicación: Tapa blanda en blanco y negro con interior en blanco crema (recomendado para libros editoriales · más cálido que blanco puro).
- Trim size: 6 × 9 pulgadas.
- Sangrado: «Sin sangrado» (no hay imágenes a borde).
- Acabado de portada: Mate (más editorial que brillo).

### 8.3 · Subida de archivos

- **Manuscrito (interior):** subir `manuscrito-maquetado-v1-interior.pdf`. Esperar a que KDP procese y verifique.
- **Portada:** subir el PDF wraparound de la **v2 final** del libro (concepto A, B o C de `portada/conceptos-portada-v2.md` ya implementado por Code tras decisión de Daniel + ilustrado por diseñador + recalculado con el conteo real de páginas tras maquetación). **NO subir `portada-wraparound-kdp.pdf` actual** · ese archivo es la v1 descartada el 14 may por no cumplir el criterio dopamina-comercial. Si por error está aún en el repo, será sustituido cuando Daniel elija concepto v2 y Code regenere. KDP recalcula y muestra preview tras la subida.

### 8.4 · Previsualización

- Abrir el **Previsor de Vista Previa** de KDP (botón al final de la página).
- Revisar página a página el interior + portada.
- Errores típicos que detecta el previsor:
  - Texto fuera del margen seguro.
  - Lomo desalineado.
  - Páginas en blanco no intencionadas.
  - Fuentes sin embeber.

### 8.5 · Precio y derechos

- Distribución: España + Europa + EEUU + LatAm.
- Royalty: 60 %.
- Precio sugerido: rango entre **15,99 € y 19,99 €** para libros de psicología premium en España. Code propone precio exacto en documento aparte.

### 8.6 · Publicar

Una vez todo verde, click «Publicar libro». Amazon revisa en 24-72 h y lo activa.

---

## 9 · Cronograma realista de maquetación

| Bloque | Tiempo estimado |
|---|---|
| 0 · Descargar fuentes y crear archivo | 30 min |
| 1 · Configurar página y márgenes | 15 min |
| 2 · Definir 10 estilos | 60 min |
| 3 · Estructura preliminar (numeración, secciones) | 60 min |
| 4 · Aplicar estilos al manuscrito completo | 6-10 h |
| 5 · Maquetar páginas preliminares | 60 min |
| 6 · Añadir Apéndice 21 días + Sobre el autor + Última | 30 min |
| 7 · Revisión + ajustes (viudas, huérfanas, ortografía) | 2-3 h |
| 8 · Exportar PDF + verificar fuentes | 30 min |
| 9 · Subir a KDP + previsualizar | 60 min |
| **TOTAL** | **15-20 horas** |

Lo más realista: 3-4 sesiones de **4-5 horas** en días distintos, con revisión por la mañana fresca cuando algo te cante. No intentar maquetar todo en una sesión maratoniana · el ojo se cansa y se cuelan errores difíciles de detectar después.

---

## 10 · Después de maquetar · medidas exactas para Code

Cuando termines la maquetación, antes de subir a KDP, **avísame del conteo final de páginas** del interior maquetado.

Con ese conteo, regenero la portada wraparound con el ancho de lomo exacto. Hoy la portada está calculada con `NUM_PAGES = 185` (estimación). Si tu maquetación da 167 páginas o 198, el lomo cambia entre 9,6 mm y 11,3 mm respectivamente, y la portada actual quedaría desalineada.

Pasos:

1. Daniel me dice: «la maquetación final tiene N páginas».
2. Modifico `NUM_PAGES = N` en `scripts/generar-portada-libro-tu-valor.py`.
3. Regenero ambos PDFs (`python3 scripts/generar-portada-libro-tu-valor.py`).
4. Hago commit + push.
5. Daniel descarga el `portada-wraparound-kdp.pdf` actualizado y sube ese a KDP.

---

## 11 · Errores comunes que evita este brief

| Error | Cómo lo evitamos |
|---|---|
| Capítulos que empiezan en página par | Saltos de sección «Página impar» en Heading 2 |
| Fuentes no embebidas | Activar incrustación en Opciones de Word + verificar en Acrobat |
| Numeración romana sigue en el cuerpo | Salto de sección + cambio de formato de numeración en Parte I |
| Encabezados en páginas de inicio de capítulo | «Primera página diferente» activado |
| Lomo desalineado en portada | Recalcular `NUM_PAGES` con conteo final tras maquetación |
| Sangrías inconsistentes | Estilo «Cuerpo libro» con sangría de primera línea única + manualmente quitar la sangría en el primer párrafo tras cada Heading 2 |
| Viudas y huérfanas | Activar «Sin viudas ni huérfanas» en el estilo Cuerpo libro |
| Texto justificado con espacios raros | Activar Word → Opciones → Avanzado → Mostrar configuración para el guionado correcto |

---

## 12 · Recursos externos opcionales

Si en algún punto te atascas, hay dos opciones razonables que no rompen presupuesto:

- **Vellum** (macOS, 250 USD pago único): software dedicado a maquetar libros KDP que automatiza casi todo. Si Daniel maqueta varios libros más, vale la pena. Para este libro solo, no compensa por el aprendizaje.
- **Reedsy Book Editor** (gratis, web): editor online que exporta PDF KDP listo. Más limitado que Word en estilos personalizados pero más automático.

Word funciona perfectamente para este libro. No hace falta saltar a otra herramienta salvo que en algún paso te frustres.

---

## 13 · Cómo iterar este brief si encuentras algo que no funciona

Este brief es un documento vivo. Si al maquetar encuentras un paso que no funciona como dice aquí (Word ha cambiado opciones, KDP rechaza algo que no preveíamos, una fuente no embebe), avísame:

1. Anota el problema con el paso exacto donde aparece.
2. Me lo pasas en chat.
3. Lo investigamos y actualizo este brief con la solución.

Lo importante: **no improvisar soluciones sin documentarlas aquí**, para que la próxima maquetación (segundo libro, segunda edición, …) se haga sobre verdad escrita, no sobre memoria.

---

**Última actualización:** 14 may 2026 · sesión `claude/improve-proposal-quality-pq3d9`. Brief redactado a partir de los specs oficiales de Amazon KDP, el sistema visual TWIM canónico (CLAUDE.md + `instagram-sistema-visual-marca.md`) y el conteo real de palabras del manuscrito v 14 may (53.384 palabras · estimación 170-200 páginas maquetado).

