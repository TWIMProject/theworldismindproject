# Cierre de sesión · 25 may 2026 (domingo)

> Sesión `claude/social-media-link-naming-tcIUA`. Día de alta productividad bajo libertad de acción declarada por Daniel. Documenta verbatim lo entregado, lo manual pendiente y los hallazgos descubiertos al pasar.

---

## 1 · PRs cerrados (3)

### PR #235 · mergeado (bc5fd6b)
Google Calendar del Directo + Banner email Te escribo v2 + Auditoría Stripe + setup Volver a Mí + regla naming.

### PR #236 · mergeado (1732bb6)
Google Calendar evento Directo creado vía MCP (eventId `p5f6uqf6fsr0sitslqrciq7hu8`).

### PR #237 · mergeado (332f8de)
Bloque grande: métricas Meta Ads + corrección auditoría Stripe (talleres adolescentes MANTENER tras verificar landings sept 2026) + limpieza landing nopuedoparar + 7 portadas Stripe + doc copy editorial + 2 productos Volver a Mí creados en archivado.

---

## 2 · Cosas operativas hechas vía API

### MailerLite (vía MCP)
- ✅ Campaña promo Directo (`187974522939377362`) reprogramada vía `cancel → update → schedule` para `2026-06-03 19:00 CEST`. HTML actualizado con «Domingo 7 de junio» + URL canónica. Pendiente solo: Daniel cambia idioma a Español en panel (arista MCP `language_id`).
- ✅ Automation Directo (`187662509833979144`) email actualizado con nueva fecha.
- ✅ Grupo `187662493483533365` renombrado a «Lead · Directo · La voz que te juzga (7 jun)».

### Google Calendar (vía MCP)
- ✅ Evento Directo creado · `p5f6uqf6fsr0sitslqrciq7hu8` · 2026-06-07T19:00 Europe/Madrid · color 10 Basil · Meet existente + 3 recordatorios popup (24h/1h/15min).

### Stripe (vía MCP)
- ✅ 5 productos activos actualizados con metadata (`taller_id`, `edicion`, `funcion`), tax_code `txcd_20030000` (Educational services), `statement_descriptor` específico, `default_price` corregido en los 2 talleres 720 €.
- ✅ 2 productos «Volver a Mí» CREADOS en archivado:
  - `prod_UaB5q1ltsU9AWT` · Reserva 100 € · `price_1Tb0jdFW3OLCwM3HSTAxzHef`
  - `prod_UaB5KRdkycWI6O` · Resto 597 € · `price_1Tb0jgFW3OLCwM3HemUWSWK2`

---

## 3 · Cosas operativas hechas en repo

- ✅ **Cascada corrección Directo 7-jun** · 21 archivos en cascada + autoauditoría 4 residuos + nopuedoparar-taller.html eliminado + _redirects 301 a /soluciones/ (regla §2 verificada con deploy preview).
- ✅ **5 emails MailerLite traducidos** (con Daniel · email confirmación + página agradecimiento + página preferencias + email centro preferencias + actualización preferencias). Banner Te escribo retina-ready 1200×300 generado.
- ✅ **7 portadas Stripe** generadas con script reproducible (`generar-portadas-stripe.py`) · paleta TWIM exacta, Instrument Serif + Barlow Condensed.
- ✅ **Carrusel libro Engranajes** · 4 slides IG + script reproducible (PR #235 anterior).
- ✅ **Doc métricas Meta Ads carrusel «5 señales validación»** · 7 días completados (CPC histórico 0,02 €).
- ✅ **Reglas inviolables persistidas en CLAUDE.md** · naming Stripe.
- ✅ **Sitemap lastmod actualizado** · 5 URLs que cambiaron hoy (daniel-orozco-abia, psicologo-burnout-valencia, lead-burnout-5-senales, soluciones, directo-la-voz-que-te-juzga).

---

## 4 · Hallazgos descubiertos al pasar (regla §1 leer el repo primero)

### Hallazgo 1 · No archivar talleres adolescentes
Antes de archivar productos Stripe «talleres adolescentes» verifico el repo · `talleres/bachillerato-motivacion/index.html` y `talleres/tdah-adolescentes/index.html` están EN sitemap, EN producción, con `startDate: "2026-09"`. Cambio de criterio · MANTENER los 4 productos. Si hubiera archivado a ciegas, rompía funnel comercial de septiembre.

### Hallazgo 2 · Landing nopuedoparar obsoleta en sitemap
`nopuedoparar-taller.html` estaba en sitemap con fecha 30-mar (pasada), precio 99 € en HTML pero 19 € en Stripe (incoherente), sin Payment Link funcional. Eliminado + 301 redirect a `/soluciones/`. Limpios 5 enlaces internos.

### Hallazgo 3 · default_price null en talleres 720 €
Los 2 talleres adolescentes 720 € no tenían `default_price` marcado · el dashboard no mostraba precio principal. Fixed.

### Hallazgo 4 · Bizum nativo SÍ disponible (no solo CPM)
Daniel creó por error un Bizum como Custom Payment Method (CPM · requiere conciliación manual). Verificando el PMC `Default · Tu cuenta` apareció Bizum NATIVO disponible para activar · pendiente Daniel.

---

## 5 · Pendiente manual Daniel (no automatizable vía MCP)

### Inmediato (esta semana)
1. **MailerLite · idioma campaña promo Directo** a Español en panel (antes del **3-jun 19:00 CEST**, envío automático).
2. **MailerLite · banner Te escribo** subido a los 3 emails de doble opt-in / preferencias (Daniel ya está con ello).
3. **Quote-tweet X corrección fecha Directo** (hilo `2058249444194471967` no editable).
4. **Email manual a la 1 suscrita real** avisando del cambio de fecha del Directo.

### Cuando pueda (esta semana / próximas)
5. **Stripe Bizum** · activar nativo en `Configuración → Métodos de pago → PMC Default Tu cuenta`. Después desactivar el CPM `cpmt_1Tb18kFW3OLCwM3H1VNceuMw`.
6. **Stripe PayPal** · ACTIVAR (requiere cuenta PayPal Business · si no la tiene, crearla antes). Para LatAm + España es +10-20 % conversión.
7. **Stripe Tax** · activar `Configuración → Impuestos` antes del 1-sept (pre-venta Volver a Mí).
8. **MailerLite · email cancelación de suscripción** · probablemente también en inglés, traducir.

### Antes del 31-jul-2026
9. **Activar productos Volver a Mí** (de Archivados a Activos) · 1 click cada uno.
10. **Subir portadas Volver a Mí** (06-reserva-volver-a-mi.png + 07-resto-volver-a-mi.png) desde su disco.
11. **Pedir a Claude crear Payment Links** vía API una vez activos.

---

## 6 · Métricas declaradas

- **Meta Ads campaña «5 señales validación»** · 7 días, 139,93 € · CPC 0,02 €/visita web · 7.172 visitas · CTR 12,89 % · benchmark sector x30-150 mejor.
- **Pendiente verificar CR** · suscriptores nuevos al grupo del Reto durante 18-25 may en MailerLite.

---

## 7 · Carga acumulada del repo

- 4 PRs mergeados hoy
- ~13 documentos creados (auditorías, métricas, setup, cierre)
- 7 portadas Stripe + 2 banners email + 4 slides carrusel libro
- ~60 archivos modificados en cascada Directo corrección

---

## 8 · Estado emocional del CEO al cierre

Daniel reporta saturación al cierre del día («estoy ya saturado del día con tanto paciente y además esto»). Declara plena libertad para que Claude actúe como mano derecha y cierre lo que pueda solo. Honrar la confianza con autoauditoría y no acumular trabajo no comunicado.

---

**Última actualización:** 25 may 2026 · sesión `claude/social-media-link-naming-tcIUA`.
