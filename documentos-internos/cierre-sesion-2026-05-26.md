# Cierre de sesión · 26 may 2026 (martes)

> Sesión `claude/social-media-link-naming-tcIUA` · día martes 26 may 2026 (hora Madrid). Continuación de `cierre-sesion-2026-05-25.md` (lunes). Documenta verbatim lo entregado, los hallazgos y las tareas manuales priorizadas para que la siguiente sesión opere desde la verdad, no desde memoria.

---

## 1 · PRs cerrados en el día (5)

### PR #239 · mergeado (131ff38)
Auditoría Stripe Payment Links · 2 mejoras aplicadas vía API a los 2 Payment Links de 720 € (automatic_tax + allow_promotion_codes) · 3 gaps pendientes documentados.

### PR #240 · mergeado (590e66d)
CTA al Directo en 25 insights · alto ROI SEO. Script Python idempotente reproducible en plantillas. 1 placeholder vacío eliminado (`artículo-vacio-idealizacion.html`).

### PR #241 · mergeado (0494c9e)
CTA insights v2 · bloque combinado Directo (primario, hasta 7-jun) + Newsletter Te escribo (secundario, evergreen). Transición post-7-jun preparada.

### PR #242 · mergeado (c5baddd)
UTM tracking en form Directo · atribución por canal en GA4.

### PR #243 · mergeado (5afa5cc)
UTM tracking propagado a TODOS los forms de captación · exit-intent (cubre 7 landings SEO), cross-sell (7 landings), home (2 forms · padres-talleres + newsletter), newsletter/, reto-7-dias. Hallazgo extra · los 2 forms de home NO disparaban gtag event en absoluto · arreglado.

### PR #244 · mergeado (63cf258)
Carta #3 «Hambre de mirada» · borrador .txt + HTML para MailerLite. Pieza pública S21 lista para programar.

---

## 2 · Cosas operativas hechas vía API

### Stripe (vía MCP)
- ✅ 2 Payment Links de 720 € actualizados con `automatic_tax.enabled: true` y `allow_promotion_codes: true`.
- ✅ Inventario completo verificado de los 4 Payment Links activos (Reserva Bach + Reserva TDAH + Taller Bach + Taller TDAH).

### Cero acciones MailerLite ni Google Calendar hoy
- Daniel está saturado · no se ha tocado MailerLite ni Calendar en este turno. Pendientes manuales suyas siguen vivos (ver §4).

---

## 3 · Cosas operativas hechas en repo

- ✅ **CTA al Directo en 25 insights** + script Python reproducible. **Mejora SEO importante** · 25 páginas con tráfico orgánico SEO acumulado ahora invitan al Directo del 7 jun.
- ✅ **CTA v2 combinado** · cobertura post-7-jun ya preparada con copy Newsletter secundario.
- ✅ **UTM tracking en 5 forms** · atribución por canal completa para GA4 (Newsletter, Reto, Directo, padres-talleres).
- ✅ **Carta #3 «Hambre de mirada»** · borrador completo en .txt + HTML MailerLite. Voz Te escribo, sin venta dura, cierre puente al Directo.
- ✅ **Calendario operativo PDF** · 26 may → 31 jul 2026 · paleta TWIM, leyenda estados, hitos críticos marcados, podcast E5 destacado como pendiente urgente. Generado con WeasyPrint desde HTML autónomo (regla §5 formato entregables visuales).
- ✅ **2 reglas inviolables nuevas persistidas en CLAUDE.md**:
  - Naming Stripe (formalmente del 25-may, mantiene)
  - **Handoff de sesión** (declarada hoy 26-may por Daniel · NO se borra perfil sin OK explícito)
- ✅ **Perfil Daniel handoff sesiones** · `documentos-internos/perfil-daniel-handoff-sesiones.md` · nueva regla inviolable que permite a sesiones futuras hablar con Daniel como Daniel desde el primer turno.

---

## 4 · Pendientes manuales Daniel (acumulados · no se han movido hoy)

### Inmediato (esta semana)
1. **Programar Carta #3 en MailerLite** · `contenido-rrss/te-escribo-newsletters/carta-03-hambre-de-mirada.html` · cadencia sugerida hoy mar 26 may o mañana mié 27 may 19:00 hora Madrid.
2. **Subir Podcast E5 «Autoexigencia»** a YouTube + Spotify (todo el material está listo en `contenido-rrss/podcast-e6-autoexigencia/`).
3. **Pegar métricas Carrusel #3 a 7 días** en `metricas-carrusel-3-voz-que-te-juzga-19-may-2026.md` (datos disponibles desde hoy 17:07 hora Madrid).
4. **Antes del 3 jun 19:00 hora Madrid** · idioma a Español de la campaña promo Directo en MailerLite (ID `187974522939377362`).

### Esta semana / próximas
5. **Stripe Bizum nativo** activar en `Configuración → Métodos de pago` y desactivar el CPM creado por error.
6. **Stripe PayPal** activar (requiere cuenta PayPal Business · si no la tiene, crearla antes).
7. **Stripe Tax** activar antes del 1-sept (pre-venta Volver a Mí).
8. **Quote-tweet X** con corrección fecha Directo (hilo `2058249444194471967` no editable).
9. **Email manual** a la 1 suscrita real avisando del cambio de fecha del Directo.

### Antes del 31-jul-2026
10. **Activar productos Volver a Mí** en Stripe (de Archivados a Activos) · 1 click cada uno.
11. **Subir portadas Volver a Mí** desde su disco al panel Stripe.
12. **Pedir a Claude crear Payment Links** Volver a Mí vía API (cuando esté listo).

---

## 5 · Hallazgos descubiertos al pasar

### Hallazgo 1 · 26 insights · 0 con CTA al Directo
Tráfico SEO orgánico de búsquedas tipo «autoexigencia», «dependencia emocional», «juez interno», «burnout invisible» llegaba sin invitación al Directo. Ahora 25 insights cubiertos (1 era placeholder vacío · eliminado).

### Hallazgo 2 · 2 forms de home sin tracking GA4
Los forms padres-talleres + newsletter principal de la home NO disparaban gtag event · suscripciones invisibles en GA4. Arreglado.

### Hallazgo 3 · 1 placeholder vacío en producción
`insights/artículo-vacio-idealizacion.html` · 19 líneas con literalmente «Este es un artículo vacío que habla sobre el concepto de idealización». Thin content perjudicial SEO global · eliminado.

### Hallazgo 4 · 2 Payment Links 720 € sin automatic_tax
Sin esto, Stripe Tax (cuando Daniel lo active) no calcularía IVA en esos checkouts. Aplicado.

---

## 6 · Estado emocional CEO al cierre

Daniel reporta carga clínica de mañana («tengo que atender pacientes») pero **energía sostenida durante el día** · mensajes verbatim: «Dale duro💪🏻 A por todasss · Tu fuerza es mi aliento y mi energía», «Sigue!!!!», «Adelante», «Sigue». Es la segunda sesión consecutiva de alta productividad bajo libertad de acción declarada · Daniel confía en el delegado y autoauditoría se honra.

Al cierre del turno Daniel declara nueva regla inviolable de handoff. Lo hace porque la sesión ha sido larga y quiere asegurar continuidad para la próxima.

---

## 7 · Reglas inviolables actualizadas a hoy

Lista al cierre del 26 may (orden de aparición en CLAUDE.md):

1. Leer el repo primero antes de proponer (§1)
2. Cambios de infraestructura · verificación obligatoria (§2)
3. Criterio dopamina-comercial · piezas de venta
4. Idioma castellano siempre
5. Formato entregables visuales · HTML autónomo paleta TWIM
6. Autoauditoría tras libertad de acción
7. Auto-merge de PRs cuando CI verde y no infraestructura
8. Claridad de un vistazo en copy público
9. Naming de productos Stripe
10. **Handoff de sesión** (NUEVA · 26 may 2026)

---

## 8 · Próximo hito calendario inmediato

- **HOY mar 26 may · finales del día** · datos Meta Business Suite del Carrusel #3 a 7 días disponibles.
- **MAR 26 o MIÉ 27 may · 19:00 hora Madrid** · ventana óptima para programar Carta #3.
- **MIÉ 3 jun · 19:00 hora Madrid** · sale automática la campaña promo Directo (verificar idioma antes).
- **DOM 7 jun · 19:00 hora Madrid** · Directo «La voz que te juzga».
- **LUN 15 jun** · inicio ventana grabación DDBEO.

---

**Última actualización:** 26 may 2026 · sesión `claude/social-media-link-naming-tcIUA`.
