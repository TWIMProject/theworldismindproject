# BRIEFING · Programa «Deja de Buscarte en Otros» · sesión producción 12 may 2026

> Documento de control para Daniel al volver de consulta a las 14:30.
> Aquí encuentras: qué se hizo, qué hay listo para revisar, qué te queda a ti, en qué orden.

---

## 1 · Contexto de esta sesión

A las 12:30 del 12 may identificamos el problema real: el programa **NO existe como producto entregable**. La landing `dejadebuscarteenotros.html` lleva meses prometiendo un material que no se había producido. Tu CEO doc lo daba por «listo». No lo estaba.

Decisión tomada hoy: **producir el contenido del programa esta semana**, montar Stripe + entrega automática, y conectar el embudo con el momentum editorial actual (Carrusel #2 «Saberlo no te lo quita», Recado 01, Carta #2 «La voz que te juzga» del 19 may, Podcast E5).

Mientras atendías pacientes hasta las 14:30, he producido las piezas que están en mi mano. Las que requieren tu cara, tu voz o tu cuenta de Stripe quedan estructuradas y esperándote con instrucciones paso a paso.

---

## 2 · Lo que tienes LISTO para revisar al volver

Está todo en `documentos-internos/programa-deja-de-buscarte-en-otros/`:

| Pieza | Archivo | Estado | Acción tuya |
|---|---|---|---|
| Currículo maestro | [`01-curriculo-maestro.md`](01-curriculo-maestro.md) | ✅ Completo | Revisar coherencia con tu visión |
| **Módulo 1 · El Mapa** (script grabación con marcas `[▶ SLIDE N]`) | [`modulos/01-el-mapa-script.md`](modulos/01-el-mapa-script.md) | ✅ Completo, ~3.000 palabras + sincronización slides | Leer en voz alta junto a slides. Ajustar matices. Grabar. |
| **Módulo 1 · Slides HTML** (22 diapositivas estética TWIM) | [`slides/modulo-01-el-mapa-slides.html`](slides/modulo-01-el-mapa-slides.html) | ✅ Listo · abrir en Chrome, F = pantalla completa, → siguiente | Revisar visualmente. No requieren maquetación adicional. |
| **Setup grabación cara + slides** | [`slides/README-setup-grabacion.md`](slides/README-setup-grabacion.md) | ✅ Paso a paso con OBS + Chrome + alojamiento Vimeo | Seguir instrucciones cuando vayas a grabar (~30 min setup una vez) |
| Módulo 2 · El Ciclo (esqueleto) | [`modulos/02-el-ciclo-script.md`](modulos/02-el-ciclo-script.md) | 🟡 Estructura + puntos clave | Pedirme desarrollo completo en siguiente sesión |
| Módulo 3 · La Trampa (esqueleto) | [`modulos/03-la-trampa-script.md`](modulos/03-la-trampa-script.md) | 🟡 Estructura + puntos clave | Pedirme desarrollo completo |
| Módulo 4 · El Corte (esqueleto) | [`modulos/04-el-corte-script.md`](modulos/04-el-corte-script.md) | 🟡 Estructura + puntos clave | Pedirme desarrollo completo |
| Módulo 5 · La Base (esqueleto) | [`modulos/05-la-base-script.md`](modulos/05-la-base-script.md) | 🟡 Estructura + puntos clave | Pedirme desarrollo completo |
| **Audio 1 · Pausa de 90 segundos** | [`audios/01-pausa-90-segundos.md`](audios/01-pausa-90-segundos.md) | ✅ Completo, ~8 min de lectura | Leer en voz alta. Grabar. |
| Audio 2 · El espejo propio | [`audios/02-el-espejo-propio.md`](audios/02-el-espejo-propio.md) | 🟡 Estructura + puntos clave | Pedirme desarrollo |
| Audio 3 · Cuando el juez aprieta | [`audios/03-cuando-el-juez-aprieta.md`](audios/03-cuando-el-juez-aprieta.md) | 🟡 Estructura + puntos clave | Pedirme desarrollo |
| **Workbook completo** | [`workbook/workbook-completo.md`](workbook/workbook-completo.md) | ✅ Estructura + ejercicios todos los módulos | Maquetar en Canva/InDesign |
| **Protocolo 21 días** | [`protocolo-21-dias.md`](protocolo-21-dias.md) | ✅ Completo, día a día | Revisar. Va dentro del workbook. |
| **Email post-pago automático** | [`email-confirmacion-compra.md`](email-confirmacion-compra.md) | ✅ Listo | Pegar en Stripe (campo confirmation email) |
| **Instrucciones Stripe** | [`stripe-setup-instrucciones.md`](stripe-setup-instrucciones.md) | ✅ Listo | Seguir paso a paso (15 min) |
| Landing actualizada | [`/dejadebuscarteenotros.html`](../../dejadebuscarteenotros.html) | ✅ CTA Stripe placeholder | Reemplazar placeholder con URL Stripe real |

---

## 3 · Lo que SOLO tú puedes hacer (orden estricto)

### Paso 1 · Decidir si avanzas o paras (10 min · HOY al volver de consulta)

Tres cosas que revisar como conjunto unitario:

1. **Script Módulo 1** ([`modulos/01-el-mapa-script.md`](modulos/01-el-mapa-script.md)) — ¿es tu voz? ¿lo grabarías leyéndolo / improvisando alrededor?
2. **Slides Módulo 1** ([`slides/modulo-01-el-mapa-slides.html`](slides/modulo-01-el-mapa-slides.html)) — abre en Chrome, pulsa F (pantalla completa), navega con flecha derecha por los 22 slides. ¿Estética coherente? ¿Conceptos bien anclados visualmente?
3. **Audio 1** ([`audios/01-pausa-90-segundos.md`](audios/01-pausa-90-segundos.md)) — léelo mentalmente en voz baja imaginando que lo grabas. ¿Te suena natural? ¿Te suena tuyo?

Estos tres elementos son la prueba completa de calibración: voz + visual + audio. Si los tres funcionan, el resto del programa se construye con el mismo patrón.

**Si funcionan → seguir.** Si algo no → me lo dices con qué y dónde, ajustamos calibración antes de seguir produciendo.

### Paso 2 · Abrir Stripe + crear Payment Link (15 min · esta semana)

Sigue [`stripe-setup-instrucciones.md`](stripe-setup-instrucciones.md). Es literal: paso por paso, captura por captura. Al final tendrás:
- Cuenta Stripe activa
- Producto «Deja de Buscarte en Otros» creado a 70 €
- Payment Link generado (URL pegable en el HTML)
- Email de confirmación post-pago configurado
- Webhook al MailerLite (opcional, podemos hacerlo después)

### Paso 3 · Grabar Módulo 1 + Audio 1 (1-2 sesiones · esta semana o la próxima)

Una vez aprobada la voz, grabas las dos piezas estrella **con tu cara + slides en pantalla simultáneamente** (decisión tomada hoy: grabación dual cámara + screen share para que el espectador se ponga con papel y boli).

**Sigue el procedimiento exacto de** [`slides/README-setup-grabacion.md`](slides/README-setup-grabacion.md) — está paso a paso con OBS Studio (gratis), Chrome a pantalla completa, Vimeo Pro como alojamiento. ~30 min setup una sola vez, 25-35 min de grabación, 15-30 min de edición.

**Resumen del flujo:**
- OBS captura cámara (esquina) + pantalla con slides (resto)
- Chrome en pantalla completa con `modulo-01-el-mapa-slides.html`
- Lees el script siguiendo marcas `[▶ SLIDE N]` para pulsar flecha derecha y avanzar
- El audio del Módulo 1 (video) se graba con tu micro USB
- El Audio 1 (audio guiado «Pausa de 90 segundos») se graba aparte, solo voz, sin cámara

Duración real esperada del Módulo 1: 25-30 min de video. Si improvisas saltándote partes, 20-25 min. La cámara debe estar en plano cerrado (de hombros para arriba), no plano americano.

### Paso 4 · Subir contenido a Drive/Vimeo (30 min · cuando tengas las grabaciones)

Estructura recomendada en Drive privado (`/programa-deja-de-buscarte-en-otros/`):
```
/01-bienvenida.pdf
/02-modulo-1-video.mp4 (o link Vimeo)
/03-modulo-2-video.mp4
/04-modulo-3-video.mp4
/05-modulo-4-video.mp4
/06-modulo-5-video.mp4
/07-audio-1-pausa-90s.mp3
/08-audio-2-espejo-propio.mp3
/09-audio-3-juez.mp3
/10-cuaderno-de-trabajo.pdf
```
Generar **un único link compartible** del directorio (cualquiera con el link puede ver, no editar). Ese link va en el email post-pago.

### Paso 5 · Reemplazar placeholder en landing (5 min · cuando tengas Stripe Payment Link)

Abre `dejadebuscarteenotros.html`, busca `STRIPE_PAYMENT_LINK_AQUI`, sustituye por la URL real de Stripe. Push a main. Done.

---

## 4 · Tiempos realistas

| Fase | Tiempo Daniel | Cuándo |
|---|---|---|
| Revisar Módulo 1 + Audio 1 | 30-45 min | Hoy 14:30 al volver |
| Pedir desarrollo módulos 2-5 + audios 2-3 (a Claude) | Pedirme cuando me hables | Próximas sesiones |
| Setup Stripe + email post-pago | 15-20 min | Esta semana (cualquier día) |
| Maquetar workbook en Canva | 2-3 horas | Esta semana o la próxima |
| Grabar módulo 1 + audio 1 | 1-2 horas | Cuando tengas espacio mental |
| Grabar módulos 2-5 + audios 2-3 | 4-6 horas total | A lo largo de 2-3 semanas |
| Subir todo a Drive + actualizar landing | 30 min | Cuando esté grabado todo |

**Lanzamiento realista del programa funcional: 2-3 semanas desde hoy** si trabajas con foco. **4-6 semanas** si lo intercalas con clínica intensa.

---

## 5 · Reglas del programa (no romper)

1. **Precio: 70 €** (como ya está en la landing). NO bajarlo en lanzamiento — la landing actual no menciona descuento. Si más adelante quieres ofrecer 49€ a lista cálida con un código, se hace como código privado, no como precio público.
2. **Acceso de por vida** (como está en la landing). Implica que el Drive nunca se cierra para quien pagó.
3. **Sin devoluciones** (FAQ actual). Stripe permite no aceptar refunds — configurar.
4. **El programa es psicoeducativo, NO terapia.** El disclaimer va al inicio del Módulo 1 y al cierre. Ya está incluido en el script.
5. **No hay garantía de resultados.** Nunca prometer «vas a curarte». Sí decir «vas a entender el mecanismo y tener herramientas para intervenirlo».
6. **No usar emojis en contenido educativo.** Sí en marketing/redes.

---

## 6 · Lo que NO se ha tocado hoy

- **NO he tocado tarifas de consulta ni TWIM Clinic.** Esa conversación queda pendiente.
- **NO he tocado talleres TDAH/Bachillerato.** Mi recomendación sigue siendo pausarlos hasta septiembre, pero no he movido nada.
- **NO he tocado el libro «Tu valor no está en su mirada».** Sigue en briefing con CoWork.
- **NO he subido el programa a YouTube ni planificado el embudo desde YouTube.** Cuando esté grabado se hace.
- **NO he pausado los ads activos** (Promote IG 65€ + Business Suite 21€). Cuando termine la campaña actual (a los pocos días), no renovar hasta que el embudo Stripe esté cerrado.

---

## 7 · Si algo me hubieras dicho antes de salir a consulta

Habría preguntado:
1. **¿Stripe o Bizum?** → confirmaste Stripe. Resuelto.
2. **¿Mantienes los 70 € de la landing o vas a 79 €?** → asumo 70 € que es lo que la landing dice hoy. Si quieres 79 €, lo cambio cuando me lo digas.
3. **¿Cuenta Vimeo Pro o YouTube oculto para alojar los videos?** → no resuelto. Mi recomendación: **Vimeo Pro** (12 €/mes) por privacidad real (los videos NO indexables) y experiencia limpia (sin anuncios ni recomendaciones). YouTube oculto se puede saltar la privacidad si alguien comparte el link.
4. **¿Tienes ya un sistema para grabar a cámara o necesitas montar uno?** → no resuelto.

Cuando vuelvas dime: Stripe link cuando lo tengas, Vimeo o YouTube, y precio definitivo. Yo continúo lo demás.

---

## 8 · Resumen de una sola línea

**Tienes producido al 100% el Módulo 1 (script + 22 slides HTML + setup grabación), el Audio 1, el workbook, el protocolo 21 días, el email post-pago y las instrucciones Stripe. Esqueletos para los otros 4 módulos y 2 audios. Cuando me digas que la voz + slides + audio del Módulo 1 son la calibración correcta, en próximas sesiones produzco el resto con el mismo estándar (incluidos slides de cada módulo).**
