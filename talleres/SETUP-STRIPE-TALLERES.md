# Checklist Stripe · Payment Links Talleres

> **Para qué sirve:** crear los 2 productos en Stripe y obtener los Payment Links para que cada padre pueda reservar plaza con un solo clic, sin gestión manual tuya. Tiempo estimado: **15-20 min** total.

---

## Decisión previa: ¿Payment Link visible o privado?

Tienes dos opciones de UX. Lee y decide antes de empezar:

### Opción A · Privado (recomendado para arrancar)
- El Payment Link **NO se muestra en la landing**.
- El padre rellena el form de "reunión informativa".
- Tienes la reunión, evalúas encaje.
- Si encaja, **le mandas el link manualmente** (WhatsApp/email).
- **Pros:** filtras el perfil antes de cobrar. Evitas devoluciones por mal encaje.
- **Contras:** la reunión sigue siendo cuello de botella para ti (~30 min por lead).

### Opción B · Visible
- Pones el Payment Link como CTA en la landing junto al de "reunión informativa".
- Cualquiera puede pagar sin pasar por la reunión.
- **Pros:** el funnel va 100% solo. Conversión inmediata.
- **Contras:** alguien con perfil que no encaja paga, y luego hay que devolverle.

**Mi voto:** **A** para los primeros 1-2 grupos (validas demanda real, refinas el filtro). Después puedes pasar a B si las reuniones siempre acaban en encaje.

Si eliges B me lo dices después de crear los links y los meto en las landings como botón secundario.

---

## 1 · Verificar cuenta Stripe (3 min)

Login en https://dashboard.stripe.com

- [ ] Cuenta en modo **Live** (no Test) — esquina superior derecha
- [ ] Datos fiscales completos (Configuración → Negocio): NIF/CIF, dirección
- [ ] Cuenta bancaria conectada (Configuración → Pagos)
- [ ] Tarjeta de identidad verificada si te lo pide

Si falta algo, completa antes de seguir. Stripe no permite cobrar sin verificación.

---

## 2 · Crear Producto + Price · Taller TDAH (4 min)

Productos → **+ Añadir producto**

| Campo | Valor |
|---|---|
| **Nombre** | Taller TDAH adolescentes — Más allá del TDAH |
| **Descripción** | 16 sesiones presenciales en Valencia para adolescentes de 3º y 4º de ESO con TDAH. Grupo cerrado de 6. Inicio septiembre 2026. Incluye reunión informativa previa con padres. |
| **Imagen** | Sube `/portadalosengranajes.webp` o haz una específica del taller (opcional) |
| **Estadísticas** | (deja por defecto) |

**Sección Precio:**
| Campo | Valor |
|---|---|
| **Modelo** | Estándar (pago único, no recurrente) |
| **Importe** | `720,00 €` |
| **Moneda** | EUR |

→ **Guardar producto**

Apunta el **Price ID** (algo como `price_1Abc...`) — lo necesitarás si automatizamos webhooks más adelante.

---

## 3 · Crear Payment Link · Taller TDAH (3 min)

En la página del producto que acabas de crear → **Crear enlace de pago**

| Campo | Valor |
|---|---|
| **Producto** | Taller TDAH adolescentes (preseleccionado) |
| **Cantidad** | Cliente no puede ajustar / Permitir clientes a comprar más de uno: **NO** |
| **Tras el pago** | Mostrar página de confirmación (luego cambiamos a redirección) |
| **Recopilar datos del cliente** | Email ✅ · Nombre ✅ · Dirección facturación ✅ (NIF para factura, importante en España) |
| **Promoción** | Permitir códigos promocionales: ✅ (útil para descuentos puntuales) |
| **Avanzado → Limit number of payments** | 6 (igual que las plazas — si se llena, el link se desactiva solo) |

→ **Crear enlace**

Te dará una URL tipo `https://buy.stripe.com/xxxxx`. **Cópiala**.

---

## 4 · Crear Producto + Price + Payment Link · Taller Bachillerato (4 min)

Repite los pasos 2 y 3 cambiando:

| Campo | Valor |
|---|---|
| **Nombre** | Taller Bachillerato — Encontrar el rumbo |
| **Descripción** | 16 sesiones presenciales en Valencia para adolescentes de 1º y 2º de Bachillerato con apatía académica o falta de orientación vocacional. Grupo cerrado de 6. Inicio septiembre 2026. Incluye reunión informativa previa con padres. |
| **Importe** | `720,00 €` |
| **Limit number of payments** | 6 |

→ Apunta el segundo Payment Link.

---

## 5 · Pasarme las URLs (1 min)

Cuando tengas los 2 Payment Links, mándamelos así:

```
TDAH:           https://buy.stripe.com/xxxxxxxx
Bachillerato:   https://buy.stripe.com/yyyyyyyy
```

Y dime si vas con **Opción A** (privado) u **Opción B** (visible en landing).

---

## 6 · Lo que haré yo cuando me los pases

**Si elegiste A (privado):**
- Guardo los links en un doc interno (`talleres/PAYMENT-LINKS.md`)
- Te preparo un mensaje plantilla para WhatsApp/email post-reunión
- No toco las landings

**Si elegiste B (visible):**
- Añado un segundo CTA en cada landing: *"¿Ya lo tienes claro? Reservar plaza · 720 €"*
- Tracking GA4 evento `taller_payment_click`
- Aviso visible "Solo 6 plazas" cerca del botón

---

## 7 · Webhooks (fase 2, no para ahora)

Cuando el funnel manual esté validado (1-2 grupos cerrados con plazas vendidas), el siguiente paso es:

- Webhook Stripe `checkout.session.completed` → Netlify Function `/.netlify/functions/stripe-webhook`
- La function:
  1. Verifica la firma del webhook
  2. Identifica qué taller compró (por Price ID)
  3. Mueve al cliente al grupo MailerLite `Taller TDAH - Inscritas` o `Taller Bachillerato - Inscritas`
  4. Dispara email de confirmación con detalles logísticos del taller

Esto lo dejo planificado pero no construido — primero validamos que la gente paga.

---

## Configuración fiscal (España)

Importante para no llevarte sustos en el primer trimestre:

- [ ] **Stripe → Tax → Activar Stripe Tax** (lo gestiona él, IVA español)
- [ ] **Producto → Tax behavior:** `Inclusive` o `Exclusive` según prefieras (recomiendo *Inclusive* — el precio mostrado es el final).
- [ ] **Tax code del producto:** `txcd_20030000` (servicios educativos / formación) — verifica con tu asesor que aplica IVA reducido o exento. Algunos talleres psicoeducativos pueden estar exentos de IVA por ser servicios sanitarios prestados por psicólogo colegiado. **Pregunta a tu gestor antes de activar.**

---

**Cuando me pases los 2 Payment Links + decisión A/B, lo demás lo conecto yo.**
