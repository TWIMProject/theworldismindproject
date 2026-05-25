# Setup Stripe · Taller «Volver a Mí» · 25 may 2026

> Generado por Claude bajo libertad de acción declarada por Daniel (25-may-2026). Setup verificado contra `decisiones-cerradas.md` (precio 697 €, 8 plazas, modalidad online + presencial Valencia opcional, reserva 100 € + sesión individual previa, 597 € restantes tras aceptación mutua). MCP Stripe desconectado en esta sesión · todo el setup queda **listo para copy-paste manual** por Daniel.

---

## 0 · Estructura · DOS productos

Patrón **commitment device** análogo al de talleres adolescentes (deposit 40 € + taller 720 €), pero con una capa clínica añadida: la sesión individual de 30 min entre la reserva y el cobro del resto.

```
┌────────────────────────────────────────────────────────────────────┐
│ PRODUCTO 1 · Reserva «Volver a Mí» · 100 €                         │
│ → Payment link público en landing pre-venta /talleres/volver-a-mi/ │
│ → Tras cobro: acceso a la sesión individual de 30 min con Daniel   │
│ → Si Daniel rechaza tras sesión OR inscrita declina: refund total  │
│ → Si no se presenta a la sesión individual: 100 € retenidos        │
├────────────────────────────────────────────────────────────────────┤
│ PRODUCTO 2 · Resto «Volver a Mí» · 597 €                           │
│ → Payment link privado (Daniel lo envía por email tras aceptación) │
│ → Pago confirma la entrada al grupo (S1 = 30 sep 2026)             │
│ → Si después de pagar el resto se cancela: política de devolución  │
│   estándar a definir (recomendación: refund total hasta 7 días     │
│   antes de S1, parcial 50% entre 7 días y S1, no-refund post-S1)   │
└────────────────────────────────────────────────────────────────────┘

Precio total al cliente: 100 + 597 = 697 €
```

---

## PRODUCTO 1 · Reserva «Volver a Mí» · 100 €

### 1.1 · Crear producto

Dashboard Stripe → `Catálogo de productos` → `+ Crea un producto`.

| Campo | Valor |
|---|---|
| **Nombre del producto** | `Reserva · Volver a Mí · Grupo cerrado otoño 2026` |
| **Descripción** | `Reserva tu plaza en «Volver a Mí», un grupo cerrado de 8 personas guiado por Daniel Orozco Abia (Psicólogo Sanitario CV11515). 8 sesiones online semanales de 90 min · miércoles 20:00-21:30 hora Madrid · del 30 sep al 18 nov 2026. Incluye sesión individual previa de 30 min con Daniel para confirmar el encaje. Si Daniel rechaza el encaje tras la sesión individual, devolución total. Si no te presentas a la sesión individual, la reserva no se devuelve. Si aceptáis ambos el encaje, se cobra el resto del taller (597 €) antes de S1.` |
| **Imagen** | (subir cuando esté la portada del taller diseñada · si no, `logo-mindworld.png` como placeholder) |
| **Estadísticas / Metadata** | `taller_id=volver-a-mi` · `edicion=otono-2026` · `funcion=reserva` |
| **Categoría del producto** | `Talleres en vivo` (crear categoría si no existe) |

### 1.2 · Precio

| Campo | Valor |
|---|---|
| **Modelo de precio** | Estándar / pago único |
| **Importe** | `100,00` |
| **Moneda** | EUR |
| **Inclusión de impuestos** | IVA incluido en el precio |
| **Tipo de impuesto** | Formación (igual que talleres adolescentes) |

### 1.3 · Payment Link

Tras guardar el producto → `+ Crear enlace de pago`.

| Campo | Valor |
|---|---|
| **Producto** | Reserva · Volver a Mí (preseleccionado) |
| **Cantidad** | Cliente NO puede ajustar · NO permitir comprar más de 1 |
| **Tras el pago** | `Redirigir a una URL personalizada` → `https://twimproject.com/talleres/volver-a-mi/gracias-reserva.html` |
| **Recopilar datos del cliente** | Email ✅ · Nombre ✅ · Teléfono ✅ · Dirección facturación ✅ (NIF necesario para factura España) |
| **Idioma del checkout** | Español |
| **Métodos de pago** | Tarjeta ✅ · Bizum ✅ (si disponible) · Apple Pay ✅ · Google Pay ✅ · Klarna ❌ (commitment device — no fragmentar en cuotas) |
| **Restricciones de país** | España + UE + LatAm (México, Argentina, Colombia, Chile, Perú) |
| **Permitir promocodes** | ✅ (útil para descuento «EARLY» a la lista pre-pre-venta agosto) |
| **Limit number of payments** | **8** (máximo de plazas · evita overbooking automático) |

> ⚠️ El campo `Limit number of payments` no se expone vía API. Configurar **siempre desde el dashboard** una vez creado el Payment Link.

### 1.4 · Conectar con MailerLite (integración recién activada)

En **MailerLite → Integraciones → Stripe → Ajustes**:

- **Producto «Reserva · Volver a Mí»** → añadir comprador a grupo MailerLite **`Reservas · Volver a Mí · otoño 2026`** (crear grupo si no existe).
- **Disparar automation** `Bienvenida Reserva Volver a Mí` (a crear en MailerLite) con la siguiente secuencia:
  - E1 (inmediato) · «Confirmación de tu reserva + enlace para agendar la sesión individual con Daniel»
  - E2 (1 día después) · «Qué encontrarás en el grupo · 3 cosas que el taller no es»
  - E3 (3 días después) · «Recordatorio sesión individual + qué llevar preparado»

---

## PRODUCTO 2 · Resto «Volver a Mí» · 597 €

### 2.1 · Crear producto

| Campo | Valor |
|---|---|
| **Nombre del producto** | `Resto · Volver a Mí · Grupo cerrado otoño 2026` |
| **Descripción** | `Pago del resto del taller «Volver a Mí» (597 €). Daniel envía este enlace tras la sesión individual de 30 min, una vez confirmado el encaje mutuo. Cubre las 8 sesiones grupales online de 90 min (miércoles 20:00-21:30 hora Madrid, S1=30 sep → S8=18 nov 2026), el material PDF complementario y el acceso a la comunidad cerrada del grupo (WhatsApp/Telegram). La reserva previa de 100 € ya está cobrada.` |
| **Imagen** | (la misma que Producto 1) |
| **Metadata** | `taller_id=volver-a-mi` · `edicion=otono-2026` · `funcion=resto` |
| **Categoría del producto** | `Talleres en vivo` |

### 2.2 · Precio

| Campo | Valor |
|---|---|
| **Modelo de precio** | Estándar / pago único |
| **Importe** | `597,00` |
| **Moneda** | EUR |
| **Inclusión de impuestos** | IVA incluido |
| **Tipo de impuesto** | Formación |

### 2.3 · Payment Link

| Campo | Valor |
|---|---|
| **Producto** | Resto · Volver a Mí |
| **Cantidad** | Cliente NO ajusta · NO comprar más de 1 |
| **Tras el pago** | `Redirigir a una URL personalizada` → `https://twimproject.com/talleres/volver-a-mi/gracias-confirmacion.html` |
| **Recopilar datos del cliente** | Email ✅ (ya lo tenemos del Producto 1 · sirve para reconciliar) |
| **Idioma del checkout** | Español |
| **Métodos de pago** | Tarjeta ✅ · Bizum ✅ · Apple Pay ✅ · Google Pay ✅ · Klarna ✅ (en 597 € tiene sentido permitir 3 cuotas si Stripe lo ofrece) |
| **Restricciones de país** | España + UE + LatAm |
| **Permitir promocodes** | ❌ (este link va privado a inscritas ya aceptadas · no hay descuentos a este nivel) |
| **Limit number of payments** | **8** (igual que reserva, máximo plazas) |

### 2.4 · Conectar con MailerLite

- **Producto «Resto · Volver a Mí»** → mover comprador del grupo `Reservas · Volver a Mí · otoño 2026` al grupo `Inscritas · Volver a Mí · otoño 2026`.
- **Disparar automation** `Bienvenida Inscrita Volver a Mí`:
  - E1 (inmediato) · «Bienvenida oficial al grupo + 3 PDFs preparatorios + calendario S1-S8 + enlace Zoom»
  - E2 (1 semana antes de S1) · «Recordatorio práctico + cómo prepararte mentalmente para S1»
  - E3 (24 h antes de S1) · «Mañana a las 20:00 · enlace Zoom + ritual de entrada»

---

## 3 · URLs gracias-* que hay que crear en `talleres/volver-a-mi/`

Después del setup en Stripe, falta crear 2 páginas HTML en el repo (Netlify):

| URL | Función |
|---|---|
| `talleres/volver-a-mi/gracias-reserva.html` | Página tras cobro de los 100 €. Confirma reserva, da enlace para agendar sesión individual con Daniel (Cal.com o similar), recordatorio de qué encontrarán en el grupo. |
| `talleres/volver-a-mi/gracias-confirmacion.html` | Página tras cobro de los 597 €. Confirma inscripción oficial, agradece, anuncia que Daniel les escribirá personalmente en X días con material. |

Estas se generan más adelante (no urgente para esta sesión). Mientras tanto, los Payment Links pueden apuntar a un fallback genérico (`/talleres/gracias-reserva.html` que ya existe).

---

## 4 · Antes del 1 sept 2026 · checklist final

- [ ] Producto 1 (Reserva 100 €) creado · activo · Payment Link copiado a `documentos-internos/taller-volver-a-mi/payment-links.md`
- [ ] Producto 2 (Resto 597 €) creado · activo · Payment Link copiado igual
- [ ] Integración Stripe-MailerLite enchufada a los 2 productos
- [ ] Grupos MailerLite creados (`Reservas · VAM · otoño 2026` y `Inscritas · VAM · otoño 2026`)
- [ ] Automations MailerLite creadas (`Bienvenida Reserva VAM` + `Bienvenida Inscrita VAM`)
- [ ] Páginas gracias-* creadas en `talleres/volver-a-mi/`
- [ ] Landing pública `talleres/volver-a-mi/index.html` lista (independiente de este setup, lo decidirá Daniel cuando estén las piezas pendientes)
- [ ] Stripe Tax activado (si vendes UE)
- [ ] Métodos de pago verificados (Bizum, Apple/Google Pay)
- [ ] Test de compra en modo Live con tarjeta personal · refund inmediato → verificar que el flujo entero funciona

---

## 5 · Después del taller (nov 2026)

- Archivar ambos productos para que no acumulen leads zombi
- Documentar métricas reales (CR de pre-venta → reserva → sesión individual → resto) en `documentos-internos/taller-volver-a-mi/metricas-edicion-otono-2026.md`
- Decidir si hay edición primavera 2027 (replica el patrón con nuevas fechas)

---

**Última actualización:** 25 may 2026 · Claude (auditoría Stripe en sesión `claude/social-media-link-naming-tcIUA`).
