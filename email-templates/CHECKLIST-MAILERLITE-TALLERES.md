# Runbook activación MailerLite · Talleres adolescentes

> **Para qué sirve este doc:** ejecutarlo de principio a fin deja la captación + secuencias de los talleres TDAH y Bachillerato funcionando sin intervención humana. Tiempo estimado: **45-60 min** la primera vez.
>
> Complementa al [SETUP-MAILERLITE-TALLERES.md](./SETUP-MAILERLITE-TALLERES.md) que ya tienes (ese describe el diseño de las secuencias; este es la guía operacional para activarlas).

---

## 0 · Estado actual (lo que YA está hecho desde código)

✅ Forms de las landings (`/talleres/tdah-adolescentes/`, `/talleres/bachillerato-motivacion/`) registran al padre en MailerLite vía `subscribe.js` automáticamente.
✅ Form de la home (sección talleres) suscribe al grupo genérico al descargar el PDF.
✅ Env vars de Netlify ya tienen las 3 IDs de grupo configuradas:
- `MAILERLITE_GROUP_PADRES_TDAH`
- `MAILERLITE_GROUP_PADRES_BACH`
- `MAILERLITE_GROUP_PADRES_TALLERES` (genérico de descarga PDF homepage)

✅ Los 8 emails de las dos secuencias están escritos en HTML en:
- `email-templates/talleres-tdah/` (4 emails)
- `email-templates/talleres-bachillerato/` (4 emails)

✅ **Grupos `Inscritas` creados vía API (29 abril 2026):**
- `Taller TDAH - Inscritas` → ID `186093787887437444`
- `Taller Bachillerato - Inscritas` → ID `186093790595909010`

✅ **Stripe Payment Links activos** (ver `talleres/PAYMENT-LINKS.md`):
- TDAH 720 € → `https://buy.stripe.com/28E5kD5T45SZasP8jm2sM08`
- Bach 720 € → `https://buy.stripe.com/3cI7sL2GS81758vgPS2sM09`

⏳ **Pendiente que añadas en Netlify** (para el webhook futuro):
- `MAILERLITE_GROUP_INSCRITAS_TDAH` = `186093787887437444`
- `MAILERLITE_GROUP_INSCRITAS_BACH` = `186093790595909010`

**Lo que sigue siendo manual en MailerLite:** pegar los 8 emails en plantillas y montar las 2 automatizaciones con condicionales (la API solo soporta `email` + `delay` — los pasos condicionales hay que añadirlos en el dashboard).

---

## 1 · Verificar grupos en MailerLite (5 min)

Ve a **Suscriptores → Grupos**. Confirma que existen:

| Grupo | Para qué | ID env var | ¿Existe? |
|---|---|---|---|
| **Padres Talleres TDAH** | Padres con interés en TDAH (form landing TDAH) | `MAILERLITE_GROUP_PADRES_TDAH` | ✅ |
| **Padres Talleres Bachillerato** | Padres con interés en Bachillerato (form landing) | `MAILERLITE_GROUP_PADRES_BACH` | ✅ |
| **Padres Talleres Adolescentes** | Form genérico de descarga PDF en homepage | `MAILERLITE_GROUP_PADRES_TALLERES` | ✅ |
| **Taller TDAH - Inscritas** | Padres que YA han pagado plaza TDAH | `MAILERLITE_GROUP_INSCRITAS_TDAH` | ✅ creado vía API |
| **Taller Bachillerato - Inscritas** | Padres que YA han pagado plaza Bachillerato | `MAILERLITE_GROUP_INSCRITAS_BACH` | ✅ creado vía API |
| **Lista General TWIM** | Lista paraguas para newsletter | `MAILERLITE_GROUP_GENERAL` | ✅ |

Los 2 grupos *"Inscritas"* sirven para:
1. Cortar la secuencia automáticamente cuando el padre ya ha pagado.
2. Mover al padre a una lista de comunicación post-inscripción.

---

## 2 · Crear los 8 emails como plantilla (15 min)

Por cada uno de los 8 archivos HTML en `email-templates/talleres-*/`, crea un email en MailerLite:

### Workflow para cada email

1. **Suscriptores → Plantillas** (Templates) → **Crear nueva**
2. Elige tipo **HTML** (no drag-and-drop)
3. Copia el contenido completo del archivo `.html` y pégalo
4. Guarda con un nombre claro (ver tabla)
5. Asunto y preheader según la tabla

### Tabla TDAH (carpeta `email-templates/talleres-tdah/`)

| Archivo | Nombre plantilla | Asunto | Preheader |
|---|---|---|---|
| `email-1-bienvenida-guia.html` | `Talleres TDAH · 1 Bienvenida` | Tu guía está dentro (y no es lo que esperas) | Tu guía ya está dentro. Antes de que la abras, te explico qué vas a encontrar. |
| `email-2-caso-marcos.html` | `Talleres TDAH · 2 Caso Marcos` | Lo que hay debajo de "es que soy tonto" | Un caso clínico anonimizado que explica lo que tu hijo no te puede decir. |
| `email-3-por-que-grupo.html` | `Talleres TDAH · 3 Por qué grupo` | Por qué tu hijo no va a escuchar esto de ti | Lo que un grupo cerrado de adolescentes con TDAH hace que la consulta individual no puede. |
| `email-4-reserva-plaza.html` | `Talleres TDAH · 4 Reserva plaza` | Taller TDAH adolescentes · Sept 2026 · 6 plazas | Todos los detalles. 6 plazas. Si tu hijo encaja, hablamos. |

### Tabla Bachillerato (carpeta `email-templates/talleres-bachillerato/`)

| Archivo | Nombre plantilla | Asunto | Preheader |
|---|---|---|---|
| `email-1-bienvenida-guia.html` | `Talleres Bach · 1 Bienvenida` | Tu guía está dentro (y no es lo que esperas) | Tu guía ya está dentro. Antes de abrirla, te explico qué vas a encontrar y qué no. |
| `email-2-no-es-apatia.html` | `Talleres Bach · 2 No es apatía` | No es apatía. Es miedo a elegir. | Lo que tu hijo no te puede explicar sobre por qué ya no le importa nada. |
| `email-3-por-que-grupo.html` | `Talleres Bach · 3 Por qué grupo` | Por qué tu hijo no va a escuchar esto de ti | Por qué tu hijo va a aceptar de otro adolescente lo que no te acepta a ti. |
| `email-4-reserva-plaza.html` | `Talleres Bach · 4 Reserva plaza` | Taller Bachillerato · Sept 2026 · 6 plazas | Todos los detalles. 6 plazas. Si tu hijo encaja, hablamos. |

---

## 3 · Crear automatización TDAH (10 min)

✅ **YA CREADA vía API (29 abril 2026 · en draft, sin activar):**
- ID: `186094472462862106`
- URL dashboard: https://dashboard.mailerlite.com/automations/186094472462862106
- Trigger: `subscriber_joins_group` → `Padres Talleres TDAH` (`184266598608012376`)
- Estructura creada: 4 emails + 3 delays de 3 días con asunto y contenido en plain text

✅ **Conflicto resuelto (29 abril 2026):** la automation antigua `Taller TDAH · Nurturing guía` (`184339743593464945`) **fue eliminada vía API** tras audit comparativo. Razones:

| Criterio | Antigua (eliminada) | Nueva (mantenida) |
|---|---|---|
| Coherencia con strategy actual | ❌ Caso "Marcos" descrito como "16 años, 2º Bachillerato" en flujo TDAH/ESO | ✅ Marcos = 3º-4º ESO con TDAH |
| Match con `email-templates/talleres-tdah/` | ❌ Contenido distinto al canónico | ✅ Contenido idéntico |
| Cadencia según runbook | ❌ 2-3-4 días | ✅ 3-3-3 días |
| Asuntos según runbook | ❌ "Las notas no son el síntoma", etc. | ✅ "Lo que hay debajo de 'es que soy tonto'", etc. |
| Stats / subscribers en queue | 0 / 0 (nunca disparó) | 0 / 0 |
| Diseño HTML hecho | ✅ Sí (pero contenido desalineado) | ❌ No (Daniel lo pega) |

El único activo de la antigua era el HTML diseñado, pero el contenido en sí estaba desalineado con el copy actual — Daniel tendría que reescribirlo entero igualmente. Coste de la decisión: 0 envíos perdidos (nunca disparó), Daniel pega el HTML una vez en lugar de dos.

⏳ **Lo que aún tienes que hacer en el dashboard de la nueva:**
1. **Diseño visual**: cada email lleva contenido en plain text (la API no expone el editor HTML rich). Ve a cada paso de email → editor → "Source / HTML" → pega el HTML completo desde `email-templates/talleres-tdah/email-N-*.html`. ~5 min por email × 4 = 20 min.
2. **Pasos condicionales**: la API solo soporta `email` + `delay`, no `if-then-exit`. Tras cada delay, añade un bloque `Condition: subscriber is in group "Taller TDAH - Inscritas"` → SÍ exit / NO continuar. 3 condicionales en total.
3. **Acciones finales**: tras el email 4 + 1 día de espera, añade `Acción: Copy subscriber to "Lista General TWIM"` y `Acción: Remove from "Padres Talleres TDAH"`.
4. **Sender**: confirma que el remitente del email (from name + email) está configurado correctamente.

### Configuración general (referencia histórica)
- **Nombre interno:** `Secuencia Padres TDAH`
- **Trigger:** `Cuando el suscriptor se une al grupo: Padres Talleres TDAH`

### Bloques del workflow (en orden)

```
1. [Email]   Talleres TDAH · 1 Bienvenida           → enviar inmediatamente
2. [Espera]  3 días
3. [Condición] ¿Está en grupo "Taller TDAH - Inscritas"?
   ├─ SÍ → [Salir del flujo]
   └─ NO → continuar
4. [Email]   Talleres TDAH · 2 Caso Marcos
5. [Espera]  3 días
6. [Condición] ¿Está en grupo "Taller TDAH - Inscritas"?
   ├─ SÍ → [Salir del flujo]
   └─ NO → continuar
7. [Email]   Talleres TDAH · 3 Por qué grupo
8. [Espera]  3 días
9. [Condición] ¿Está en grupo "Taller TDAH - Inscritas"?
   ├─ SÍ → [Salir del flujo]
   └─ NO → continuar
10. [Email]  Talleres TDAH · 4 Reserva plaza
11. [Espera] 1 día
12. [Acción] Copiar suscriptor al grupo "Lista General TWIM"
13. [Acción] Eliminar suscriptor del grupo "Padres Talleres TDAH"
14. [Fin]
```

**No actives todavía.** Antes haz el test del paso 5.

---

## 4 · Crear automatización Bachillerato (5 min)

✅ **YA CREADA vía API (29 abril 2026 · en draft, sin activar):**
- ID: `186094552519541764`
- URL dashboard: https://dashboard.mailerlite.com/automations/186094552519541764
- Trigger: `subscriber_joins_group` → `Padres Talleres Bachillerato` (`184266663513818179`)
- Estructura creada: 4 emails + 3 delays de 3 días con asunto y contenido en plain text

⏳ **Lo que aún tienes que hacer en el dashboard:**
1. Pegar el HTML rico de `email-templates/talleres-bachillerato/email-N-*.html` en cada email (modo "Source / HTML")
2. Añadir los 3 condicionales `is in "Taller Bachillerato - Inscritas"` → SÍ exit / NO continuar
3. Tras el email 4 + 1 día: `Copy to "Lista General TWIM"` + `Remove from "Padres Talleres Bachillerato"`
4. Verificar sender

---

## 5 · Test antes de activar (10 min)

Antes de poner esto frente a usuarios reales, comprueba que la cadena completa funciona.

### Test TDAH
1. Crea o pide a un colaborador un email **fresco** (que no esté en MailerLite).
2. Ve a https://twimproject.com/talleres/tdah-adolescentes/ → rellena el form de la sección "Solicitar reunión informativa".
3. Comprueba en MailerLite (filtro **Activo**): el email debe aparecer en el grupo `Padres Talleres TDAH`.
4. **Email 1** debe llegar al instante. Abre y verifica:
   - Texto correcto en español
   - El botón funciona (lleva a `/talleres/tdah-adolescentes/#cta-final`)
   - El logo y la firma se ven
5. Para no esperar 3 días, en la automatización pulsa **Acelerar / Skip wait** (si tu plan lo permite) o crea un suscriptor de prueba con la fecha "hace 3 días" para forzar el siguiente paso.
6. Verifica los 4 emails y la salida del flujo.

### Test "salir del flujo"
1. Mientras la prueba de TDAH está en mitad de secuencia, **manualmente añade** ese email al grupo `Taller TDAH - Inscritas`.
2. Verifica que en el siguiente bloque de condición, el flujo lo saca y no recibe el email siguiente.

### Test Bachillerato
Mismo proceso en `/talleres/bachillerato-motivacion/`.

---

## 6 · Activar (1 min)

Solo cuando todo esté testeado:

- [ ] Activar workflow `Secuencia Padres TDAH`
- [ ] Activar workflow `Secuencia Padres Bachillerato`

---

## 7 · Cuando alguien pague (proceso semi-manual por ahora)

Hasta que el webhook de Stripe esté integrado:

1. Padre te paga vía Stripe Payment Link.
2. Tú lo añades manualmente al grupo `Taller TDAH - Inscritas` o `Taller Bachillerato - Inscritas` en MailerLite.
3. Eso automáticamente lo saca de la secuencia activa (si aún la estaba recibiendo).
4. (Opcional) Le mandas un email manual de bienvenida al taller con detalles logísticos.

**Mejora futura:** webhook Stripe → endpoint Netlify Function → añadir al grupo de Inscritas en MailerLite. Lo monto cuando me digas que el funnel manual está validado con al menos 1-2 inscripciones reales.

---

## Notas técnicas

- Los emails ya tienen variables `{$name}`, `{$unsubscribe}`, `{$url}` de MailerLite — no las cambies.
- Sistema visual: hero verde degradado, Barlow Condensed, CTA beige, footer verde oscuro.
- Casos clínicos (Marcos, Laura) son ficticios — indicado en PD de cada email.
- Si un padre se suscribe por **dos vías** (descarga PDF en home + landing TDAH), entrará en dos grupos distintos y podría recibir secuencias paralelas. Si esto se vuelve problema, lo solucionamos con una condición global "no enviar si ya está en grupo X".
- Si decides cambiar el ritmo (3 días entre emails es estándar), recuerda que MailerLite no admite "días laborables" — usa "horas" si quieres más finura (72 horas = 3 días).

---

**Cuando termines este checklist, dime "MailerLite activado"** y paso a montar:
- Webhook Stripe → MailerLite (auto-mover a Inscritas al pagar)
- Email de confirmación post-pago
- Reporte semanal de leads/conversión
