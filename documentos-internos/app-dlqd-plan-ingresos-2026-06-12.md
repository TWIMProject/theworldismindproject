# Plan de ingresos · App «Di lo que quieres decir» · 12 jun 2026

> Encargo de Daniel (12 jun 2026, verbatim): «el objetivo es conseguir un plan de ejecución que nos lleve por el camino hacia generar ingresos con esta app de forma "pasiva" por mi parte. que la app funcione sola y solo haya que supervisar y actualizar la calidad. [...] quiero que esta herramienta me genere dinero y sea una de las partes del puente (o un puente entero) que me lleve a mi reducción de pacientes y poder pasar más tiempo con Bosco sin perder ingresos e incluso aumentándolos.»
>
> Método: regla §1 cumplida — construido sobre `analisis-foco-x2-ingresos-2026-06-10.md`, `plan-x10-lista-email-2026-06-10.md`, `briefing-meta-ads-x10-clic-a-clic.md`, auditoría Stripe 25 may y calendario H2 descargado. **No abre un frente nuevo: refuerza los 3 existentes.**

---

## 0 · Tesis en cinco líneas

1. **La app no compite con el plan x10: lo acelera.** Es el mejor imán de captación de TWIM — interactivo, con momento «wow» propio (ver tu mensaje transformado), público idéntico al de DDBEO y Volver a Mí, y operado al 100 % por Claude. Cero horas de cuerpo/voz de Daniel.
2. **El dinero directo de la app en 2026 será pequeño; su ROI real está en la lista.** Misma doctrina del análisis del 10 jun (§1.2): sin tráfico no hay producto digital que facture. Primero volumen y emails, después paywall.
3. **Dos motores + un horizonte:** Motor A (ya) — captación: app gratis → email → lista x10 → DDBEO oct + Volver a Mí sep. Motor B (oct 2026, con compuerta) — freemium: Pase de pago para uso ilimitado y extras. Horizonte C (2027, solo inbound) — licencia B2B a psicólogos/centros.
4. **Pasividad real:** la app ya funciona sola (motor IA + modo degradado + rate limit). La supervisión queda en el dashboard de los lunes; la calidad, en iteraciones del prompt cuando Daniel detecte desvíos (como hoy).
5. **Respeto absoluto a la regla foco:** nada de esto pide la voz/cuerpo de Daniel hasta el 28 jul salvo publicar 1 carrusel (~10 min). Septiembre sigue siendo solo Volver a Mí; el paywall espera a octubre.

## 1 · Economía de la app (verificado)

| Concepto | Cifra | Nota |
|---|---|---|
| Coste por análisis (Haiku 4.5, prompt v4.1) | ~0,5-0,8 céntimos € | input ~2,5k tokens + output ~1k |
| Coste a 1.000 análisis/mes | ~6-8 €/mes | techo protegido por rate limit (6/min/IP, 60/min global) |
| Coste fijo | 0 € | Netlify free tier + función existente |
| CPL del canal app (orgánico) | ~0 € | frente a 0,39-1,94 € estimado en Meta (plan x10 §0) |

La app es la fuente de leads más barata del sistema. Cada email que capta vale lo que cuesta conseguirlo por Ads.

## 1.bis · El diferencial frente a las IAs generalistas (análisis del 12 jun, segunda iteración)

> Planteamiento de Daniel (verbatim): «ya existe la IA y esta app no hace algo diferente al resto de IAs como Claude, ChatGPT, Gemini [...] analiza si podemos crear algo que sí señalemos como diferencial y a su vez ver que si no es así, tiene entiendo que valer menos que las IAs pero no 0 €.»

**Veredicto: el diferencial existe y es defendible, pero no es la tecnología — es el criterio clínico encapsulado.** Cinco capas, de más a menos copiable:

1. **El método del vínculo** (doctrina de 8 reglas, `app-dlqd-principio-vinculo.md`): una IA generalista da «mensaje-yo» de manual (CNV estándar) — exactamente el enfoque que la doctrina de Daniel supera. El usuario de ChatGPT no sabe pedir lo que no sabe que existe.
2. **El paso 3 es pedagógico**: ver TU texto con el ruido resaltado y explicado te enseña a verte. ChatGPT hace el trabajo por ti sin que aprendas nada; la app trabaja como un terapeuta: te muestra el patrón.
3. **Ritual guiado sin deriva**: 5 pasos, un resultado, frases ancla para el después. ChatGPT chatea, repregunta, moraliza y se va por las ramas — justo lo que la persona activada no puede gestionar.
4. **Privacidad estructural**: sin cuenta, sin historial, sin entrenar con tus datos. La gente no quiere pegar su conflicto de pareja en ChatGPT.
5. **Firma clínica**: detrás hay un Psicólogo General Sanitario colegiado con consulta desde 2012, no una herramienta anónima.

**Implicación de precio** (la intuición de Daniel es correcta): la app vale menos que una IA generalista pero no 0 €. Posicionamiento del Pase: **14,90 €/año = «menos que UN MES de ChatGPT (20 €), para todo el año, y hace una sola cosa mejor que ninguna»**. Refuerzo del diferencial a construir (Fase 2): packs por tipo de vínculo con profundidad clínica, seguimiento de la conversación real («pega su respuesta y prepara la siguiente»), y nombrar el método en la interfaz como sello TWIM.

## 2 · Motor A · Captación · MODELO PUERTA-EMBAJADOR (refinado el 12 jun con el brainstorming de Daniel)

> Propuesta de Daniel (verbatim): «regalar a los suscritos la opción de usar ellos la app para que ellos sean de forma indirecta nuestros mejores embajadores y que para los que vengan, tienen que suscribirse a la newsletter y se les envía el enlace para utilizar la app de forma gratuita [...] que cada uno tuviera su código de entrada, o que darse de alta con su email y contraseña.»

**Refinamiento implementado** (mejora sobre la puerta dura: el «wow» va antes que la puerta):

- **1 análisis completo de regalo, sin pedir nada.** El mejor anuncio de la app es usarla; una puerta antes del valor hace rebotar a la mayoría (y mataría el destino de Ads/SEO).
- **Del 2º análisis en adelante: puerta de suscriptor.** Email → alta en newsletter → **código personal al instante** en la propia app (8 caracteres, ligado a su email).
- **Sin contraseñas ni cuentas** (la opción email+contraseña del brainstorming se descarta: rompe la promesa de privacidad y añade infraestructura): el código es criptográfico (HMAC del email con secreto del servidor `DLQD_CODE_SECRET`), **sin base de datos**, revocable en bloque rotando el secreto. La emisión verifica contra MailerLite que el email está suscrito de verdad.
- **Mecánica embajador**: el código es personal e intransferible en la práctica (va ligado al email); para que un amigo use la app tiene que suscribirse y obtener el suyo → cada usuario recurrente = un suscriptor, y cada recomendación = un lead. Los suscriptores actuales ya tienen acceso: con poner su email en la puerta, reciben su código (están en MailerLite).
- Datos en el navegador limitados a contador de usos + email/código si se suscribe, con botón visible «Borrar mis datos de este navegador» (regla de la spec original). El texto de la conversación sigue sin guardarse jamás.
- Medición: evento `dlqd_puerta_vista` + altas por vía (`puerta` / `paso5`) → la conversión de la puerta es EL kpi del Motor A.

## 2.bis · Motor A · superficies de distribución (implementado el 12 jun, primera iteración)

**Implementado el 12 jun (Claude, sin Daniel):**
- Bloque de email opcional en el paso 5 («te escribo cuando algo merece tu tiempo» — promesa sin cadencia intacta, honestidad de privacidad: solo el email, jamás el texto) → grupo `newsletter-home` vía `subscribe.js`. *Pendiente técnico: migrar a grupo dedicado «Lead · App DLQD» cuando el conector MailerLite vuelva, para segmentar; mientras, el origen se distingue por GA4.*
- GA4 en la app: `dlqd_analisis` (modo ia/básico, destinatario, objetivo — jamás el texto), `dlqd_mensaje_copiado`, `dlqd_alta_newsletter`, `generate_lead` (origen app-dlqd).
- Tarjeta en la home (sección tras el Cap. III) + ya estaba en sitemap.
- Kit IG de lanzamiento listo (`contenido-rrss/app-dlqd-lanzamiento-ig.md`) — Daniel publica tras el Directo (≥15 jun), ~10 min.

**Goteo continuo (Claude, lunes):** métricas de la app dentro del dashboard semanal · la app entra en la rotación de promo IG del plan x10 (1 de cada 4 semanas) · regla de un solo CTA respetada: la app ES superficie de captación (el email se capta dentro).

**Ads:** cuando la campaña Meta del x10 esté publicada, añadir **anuncio C** con la app como destino (`?utm_source=meta&utm_medium=cpc&utm_campaign=lista-calentamiento-jun26&utm_content=app-dlqd`) **dentro del mismo presupuesto de 6 €/día** — compite con los anuncios A/B por CR de lead; el ganador se queda el tráfico. Cero presupuesto nuevo.

**SEO/AEO (Claude, próxima sesión):** 1 insight «Cómo decir lo que quieres decir sin que acabe en pelea» (jerga+glosa, concreción) enlazando la app + schema.org `WebApplication` + entrada en `llms.txt`. La app puede rankear por «cómo decirle a mi pareja que…» — búsquedas de intención altísima.

## 3 · Motor B · Freemium (ADELANTADO · orden inviolable de Daniel, 12 jun 15:48)

> Verbatim: «Inviolable: monta ya el freemium [...] los usuarios merecen esto que les estamos creando porque va a ayudar una barbaridad a mejorar las relaciones personales.»

**Estado (12 jun, tarde): maquinaria COMPLETA y dormida.** Implementado: códigos de Pase con caducidad incorporada (HMAC `email|YYMM`, sin BD, inalargables), límite de 3 análisis/mes para suscriptores (contador mensual local), panel de compra en la app, canje automático al volver de Stripe (verificación de la Checkout Session: pagada + precio correcto) y entrada manual «Ya tengo mi Pase». El interruptor es `URL_PASE` en `app.js`: mientras esté vacío, los suscriptores siguen sin límite (cero riesgo al mergear).

**Para encender el cobro (10 min, una vez):**
1. Stripe → Product catalog → Add product: nombre exacto `Infoproducto · Di lo que quieres decir · Pase 12 meses` · 14,90 € · pago único · metadata `funcion: infoproducto`, `taller_id: app-dlqd`. (El conector MCP de Stripe pedía re-autorización el 12 jun; si Daniel lo re-autoriza, Claude lo crea todo.)
2. Crear Payment Link de ese precio · After payment → redirect a `https://twimproject.com/di-lo-que-quieres-decir/?pase_sesion={CHECKOUT_SESSION_ID}`.
3. Pasar a Claude el `price_...` y la URL del link → Claude configura `DLQD_PASE_PRICE_ID` en Netlify y rellena `URL_PASE` (1 commit).
4. **`STRIPE_SECRET_KEY` en Netlify** (Developers → API keys → pegar en el panel, jamás por chat). Hallazgo del 12 jun: NO existe pese a que `stripe-webhook.js` la declara requerida — sin ella tampoco funcionaba la entrega de productos digitales existente.

La compuerta de tráfico de octubre deja de ser bloqueante y pasa a ser **métrica de seguimiento** (conversión del panel: `dlqd_pase_visto` → `dlqd_pase_canjeado`).

**Diseño propuesto** (decisión final de Daniel en octubre, con datos):
- **Gratis:** 3 análisis completos/mes (contador localStorage, límite blando) — suficiente para resolver LA conversación que te trajo.
- **Pase 12 meses · 14,90 €** (pago único, sin suscripción ni cuentas): análisis ilimitados + guía descargable «El enfoque vínculo» (PDF, destilado del principio — Claude lo redacta) + packs de situaciones (pareja · familia · trabajo · amistad).
- **Mecánica sin login** (coherente con la privacidad): Stripe Payment Link → `stripe-webhook.js` (ya existe) → email con código de acceso (patrón `descarga-libro.js` + Netlify Blobs ya montado) → código en la app → desbloqueo. Naming Stripe (regla 25 may): `Infoproducto · Di lo que quieres decir · Pase 12 meses` + metadata `funcion: infoproducto`.
- **Cross-sell dentro del paso 5** (esto puede valer más que el Pase): tras copiar el mensaje — «Si esta conversación se te repite con todo el mundo, el problema no es el mensaje: es el lugar desde el que te vinculas» → DDBEO (oct, evergreen 70 €) · y durante la preventa de sept, banner único a Volver a Mí (697 €).

**Proyección honesta (sin autoengaño, doctrina §1.2):** ingresos directos 2026 ≈ 0-300 €. Con lista ×10 y tráfico compuesto, 2027: Pase ~30-80 ventas/año (450-1.200 €) + atribución a DDBEO/talleres como canal de entrada — ahí está el dinero real. La app es puente, no la meta entera: **suma al x2 sobre todo por la vía A (leads) y por hacer más grande el embudo de los productos que ya existen.**

## 4 · Horizonte C · B2B (2027 · solo inbound)

Licencia de la app con marca blanca o acceso profesional para psicólogos/centros/RRHH (el In-Company de ansiedad laboral ya existe como producto a 2.450 €). CONGELADO según regla foco; se documenta para no perderlo. Revisión: Q1 2027.

## 5 · Calendario integrado (no choca con nada)

| Fecha | Acción | Quién |
|---|---|---|
| 12 jun | Motor A implementado (captación + GA4 + home + kit IG) | Claude ✔ |
| ≥15 jun | Publicar carrusel IG + bio (~10 min) | **Daniel** |
| lunes (cada) | Métricas app en dashboard semanal | Claude |
| al publicar campaña Meta x10 | Añadir anuncio C (destino app, mismo presupuesto) | Claude prepara · Daniel publica |
| jun-jul | Insight SEO + schema + grupo MailerLite dedicado | Claude |
| sept | Banner único Volver a Mí en paso 5 (solo preventa) | Claude |
| **oct** | **Compuerta freemium:** si ≥750 análisis/mes → montar Pase + cross-sell DDBEO | Claude monta · **Daniel decide precio/OK** |
| dic | Revisión del plan con datos reales | ambos |

## 6 · Qué decide Daniel (y nada más)

1. Publicar el carrusel IG cuando pase el Directo (10 min).
2. En octubre, con datos delante: activar o no el Pase y validar el precio (14,90 € propuesto).
3. (Ya pendiente del x10, no de este plan): publicar la campaña Meta + evento clave GA4.

## 7 · Riesgos y salvaguardas

- **Coste API si hay pico viral:** rate limit ya activo; a 10.000 análisis/mes serían ~70 € — buen problema; avisaría el lunes.
- **Abuso de la función:** mitigado 11 jun (Origin + rate limit); escalón Turnstile documentado en el PR #338 si hay tracción.
- **Clave API expuesta (12 jun):** rotar — pendiente de seguridad ya registrado.
- **Privacidad como activo de marca:** el bloque de email deja explícito que el texto jamás se guarda. Cualquier evolución (historial, cuentas) pasa por Daniel.
- **Calidad clínica:** el prompt encapsula la doctrina (`app-dlqd-principio-vinculo.md`); cualquier sesión futura que lo toque debe re-validar contra los 8 puntos.

---

*Registro de ejecución: [2026-06-12]: Motor A implementado y mergeado · informe visual entregado a Daniel en chat (no versionado, regla §5).*
