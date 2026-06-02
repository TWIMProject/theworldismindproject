# Cierre de sesión · 2 jun 2026 (martes)

> Sesión `claude/blissful-lovelace-VPbaj`. Daniel pasó dos transcripciones de vídeos de Matías Tavil («La Asociación Libre») para «sacarles jugo» de cara a su ponencia del Directo del 7 jun «La voz que te juzga». De ahí derivó trabajo editorial + una regla nueva + un banco de frases. Libertad de acción declarada («adelante, las grandes ideas siempre se ejecutan»).

---

## 1 · PRs cerrados (5, todos mergeados)

| PR | Contenido | SHA squash |
|---|---|---|
| #280 | Anexo al guion del directo · «El goce de la falla y el fantasma del rechazo» (HTML editorial, dos partes, mapeado a los 5 bloques) | (mergeado) |
| #281 | Fix `title`/`meta` del anexo (hallazgo de la review de Copilot · no coincidían con el H1) | (mergeado) |
| #282 | Regla de glosa en `CLAUDE.md` §8 + entrada en perfil de handoff | (mergeado) |
| #283 | Renombrado del anexo con keywords SEO (`goce-y-mirada` → `inseguridad-y-miedo-al-rechazo`) | 8040023 |
| (este) | Banco de frases TWIM + este cierre de sesión | en curso |

---

## 2 · Qué se entregó (verbatim)

### Anexo teórico al directo
- `documentos-internos/directo-7jun-anexo-inseguridad-y-miedo-al-rechazo.html` · mismo formato que el guion teórico (paleta TWIM, Instrument Serif + Barlow + Lora, imprimible). Uso interno, no publicado, no en sitemap.
- **Parte A · el goce de la falla** (vídeo «inseguridades») · 6 ideas. Aporte central · detrás de la inseguridad no hay solo déficit, hay un goce que la voz condena → la voz no se calla cumpliendo ni con logros. Profundiza el bloque 4-5 sin contradecir la intervención existente («poner autor a la voz»); añade el segundo movimiento (aceptar lo que la voz condena). Con aviso de vocabulario (traducir «goce»/«fálico», no llevar esa jerga al directo).
- **Parte B · el fantasma del rechazo** (vídeo «rechazo») · «mi deseo produjo el rechazo». Criterio explícito · al directo va solo un matiz (bloque 2); el grueso se reserva para DDBEO (su núcleo) y una carta «Te escribo».
- **Tesis que une los dos vídeos** en una frase para el directo.
- Enlazado desde `directo-7jun-setup-meet-y-tarjetas-bolsillo.md` (no huérfano).

### Regla de glosa (persistida)
- Declarada por Daniel · «para la web, artículos y demás siempre utilizar lenguaje sin jerga o con jerga pero siempre luego explicando esa palabra o palabras desde un lenguaje sin jerga».
- Persistida en `CLAUDE.md` §8 (complementa Claridad de un vistazo) + perfil handoff. En artículos/cuerpo web largo SÍ vale jerga con glosa llana inmediata; en piezas cortas/escaneables y formatos hablados, cero jerga sin glosa.

### Banco de frases
- `contenido-rrss/banco-frases-twim.md` · nuevo. Nace con la frase estrella aprobada por Daniel, las frases-ancla del anexo y las canónicas verificadas del proyecto. Regla simétrica para nutrirlo.

---

## 3 · Decisiones tomadas

1. **Anexo como uso interno**, no pieza pública (fuente de terceros destilada, no citable en público).
2. **Parte B (rechazo) reservada mayormente para DDBEO**, no para el directo (criterio · no sobrecargar la hora).
3. **Nombre del anexo con keywords SEO** (`inseguridad-y-miedo-al-rechazo`) como borrador del slug del futuro insight público · aunque el archivo siga interno. Señalado a Daniel que el nombre de un interno no mueve SEO hoy; el valor está en el slug público cuando se recicle.
4. **Ahrefs Keywords Explorer bloqueado por plan** (`Insufficient plan`) · sin cifras de volumen; decisión SEO fundamentada en principios + ángulo «voz que te juzga» que el proyecto ya trabaja.

---

## 4 · Pendiente de Daniel

### Del calendario (recordatorio del día)
- **3 jun 19:00 CEST** · carta promo Directo · verificar idioma a Español en panel MailerLite antes del envío automático.
- **7 jun 19:00 CEST** · Directo «La voz que te juzga» vía Meet.
- **vencido (26 may)** · doc métricas Carrusel #3 a 7 días · sin cerrar.

### Derivado de esta sesión
- Decidir si alguna frase del banco se lleva a slide de reciclaje / carta / hook DDBEO al producir esas piezas.
- Cuando se recicle el directo a insight público · definir slug + `title` + meta con keywords reales (jerga solo glosada en el cuerpo, por la regla nueva).

---

## 5 · Estado emocional del CEO al cierre

Energía alta y confianza · «adelante, las grandes ideas siempre se ejecutan :)». Libertad de acción plena; honrada con autoauditoría en cada bloque y persistencia de la regla nueva sin pedir confirmaciones triviales.

---

## 6 · Continuación (tarde-noche 2 jun) · más trabajo de libertad de acción

### Google Ads tag
- Instalado `gtag('config','G-8PCYMX2NDX')` junto al GA4 en los 58 HTML (PR #285, mergeado). Para medición de conversiones de Google Ads. Sin tocar CSP.

### Producto nuevo · «Los engranajes de la mente» · EDICIÓN DIGITAL (venta directa)
Carpeta `documentos-internos/producto-engranajes-digital/` (ver su `README.md`).
- **Portada nueva TWIM** de cero (Daniel descartó recolorear la de Amazon, «horrenda»). Crema + engranajes a trazo + doble filete + logo + autor/colegiado correctos (sin «Psicólogo Random»). Aprobada «así genial». Script `scripts/generar-portada-engranajes-digital.py`.
- **Extra exclusivo** «De los engranajes a tu día» (`extra-...html`): baja Yo/Ello/Superyó a la vida del lector + juego defensivo + síntoma como intento + equilibrio sano + «qué puedes hacer hoy» + cierre con «Wo Es war, soll Ich werden». Fiel al libro, jerga+glosa, anti-coaching. Validado «ahora sí».
- **PDF completo ensamblado**: portada + 186 interior + extra (10 págs) + contraportada = **198 págs**. Script `scripts/montar-pdf-engranajes-digital.py` (WeasyPrint + PyMuPDF). **El PDF NO se commitea** (producto de pago; gitignored; se genera en /tmp). Enviado a Daniel por chat.
- **Precio**: 9,90 € (edición ampliada; Amazon está a 7,68 €).

### Cuaderno «La mirada del otro» (infoproducto dependencia, sesión de mañana)
- Añadido el **logo** en portada (Daniel lo pidió). Precio 8,90 €. Falta: portada con más fuerza (opcional), Stripe, entrega, landing.

### PENDIENTE · requiere OK de Daniel (NO ejecutado · regla §2 infraestructura)
- **Entrega segura** de ambos productos: Stripe Checkout + webhook (`stripe-webhook.js` ya existe) → enlace de descarga firmado (caduca, nº descargas) al email + función `descarga` que sirve el PDF desde ubicación no pública + marca de agua con email del comprador. Plan detallado en `producto-engranajes-digital/README.md`. **No mergear a producción sin OK** (precedente PR #133).
- **Landings de venta** (libro + cuaderno): pendientes; dependen del cobro.
- Mover el extra/cuaderno HTML fuera de `documentos-internos/` público (o bloquear) al montar la entrega.

### Decisiones tomadas (Daniel)
- vA→portada de cero (de las candidatas, eligió portada 1 + contraportada 4, luego pidió de cero).
- Idioma carta promo Directo: **ya en castellano** (confirmado, resuelto).
- Quiere venta directa de Los Engranajes; PDF interior estaba en repo (`LEDLM.pdf`).

### Autoauditoría continuación
- Portada: 2 errores corregidos en el acto (banda corta / colegiado en cursiva ilegible) + ruta del logo del cuaderno (../../). 
- Hallazgo que evitó error: el libro YA tiene glosario y apéndice teórico → el extra se replanteó para no duplicar.
- PDF protegido de exposición pública (gitignore). Infra intacta. Commits pusheados, working tree limpio.

---

**Última actualización:** 2 jun 2026 noche · sesión `claude/blissful-lovelace-VPbaj`.
