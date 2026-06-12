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

## 2 · Motor A · Captación (ACTIVO desde hoy)

**Implementado el 12 jun (Claude, sin Daniel):**
- Bloque de email opcional en el paso 5 («te escribo cuando algo merece tu tiempo» — promesa sin cadencia intacta, honestidad de privacidad: solo el email, jamás el texto) → grupo `newsletter-home` vía `subscribe.js`. *Pendiente técnico: migrar a grupo dedicado «Lead · App DLQD» cuando el conector MailerLite vuelva, para segmentar; mientras, el origen se distingue por GA4.*
- GA4 en la app: `dlqd_analisis` (modo ia/básico, destinatario, objetivo — jamás el texto), `dlqd_mensaje_copiado`, `dlqd_alta_newsletter`, `generate_lead` (origen app-dlqd).
- Tarjeta en la home (sección tras el Cap. III) + ya estaba en sitemap.
- Kit IG de lanzamiento listo (`contenido-rrss/app-dlqd-lanzamiento-ig.md`) — Daniel publica tras el Directo (≥15 jun), ~10 min.

**Goteo continuo (Claude, lunes):** métricas de la app dentro del dashboard semanal · la app entra en la rotación de promo IG del plan x10 (1 de cada 4 semanas) · regla de un solo CTA respetada: la app ES superficie de captación (el email se capta dentro).

**Ads:** cuando la campaña Meta del x10 esté publicada, añadir **anuncio C** con la app como destino (`?utm_source=meta&utm_medium=cpc&utm_campaign=lista-calentamiento-jun26&utm_content=app-dlqd`) **dentro del mismo presupuesto de 6 €/día** — compite con los anuncios A/B por CR de lead; el ganador se queda el tráfico. Cero presupuesto nuevo.

**SEO/AEO (Claude, próxima sesión):** 1 insight «Cómo decir lo que quieres decir sin que acabe en pelea» (jerga+glosa, concreción) enlazando la app + schema.org `WebApplication` + entrada en `llms.txt`. La app puede rankear por «cómo decirle a mi pareja que…» — búsquedas de intención altísima.

## 3 · Motor B · Freemium (OCTUBRE 2026 · con compuerta)

**Por qué no ahora:** paywall sin tráfico = fricción sin ingresos que además mata el Motor A. Doctrina 10 jun: la lista precede al producto.

**Compuerta de activación (cualquiera de las dos):** ≥750 análisis/mes en GA4 o ≥1.500 usuarios acumulados. Si no se alcanza en octubre, se revisa en diciembre — no se fuerza.

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
