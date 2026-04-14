# Setup MailerLite · Secuencias Talleres Adolescentes

Dos secuencias independientes de 4 emails cada una. Se disparan desde los formularios de descarga de guías del homepage.

---

## Grupos a crear en MailerLite

| Grupo | Trigger | Netlify env var |
|-------|---------|-----------------|
| `Guía TDAH - Padres` | Descarga guía TDAH desde homepage | `MAILERLITE_GROUP_PADRES_TDAH` |
| `Guía Bachillerato - Padres` | Descarga guía Bachillerato desde homepage | `MAILERLITE_GROUP_PADRES_BACH` |
| `Taller TDAH - Inscritas` | Ha reservado plaza TDAH | — |
| `Taller Bachillerato - Inscritas` | Ha reservado plaza Bachillerato | — |
| `Lista General TWIM` | Post-secuencia | `MAILERLITE_GROUP_GENERAL` |

**Nota:** el formulario actual del homepage usa `group: 'padres-talleres-adolescentes'`, que mapea a `MAILERLITE_GROUP_PADRES_TALLERES`. Hay que **desglosarlo en dos grupos separados** (TDAH vs Bachillerato) para poder mandar la secuencia correcta según qué guía descargó el padre. Esto requiere dividir el formulario homepage en dos (o añadir un campo oculto que indique el interés).

---

## Secuencia 1: Guía TDAH · 4 emails

**Archivos HTML:** `email-templates/talleres-tdah/`

| Email | Día | Asunto sugerido | Preheader |
|-------|-----|-----------------|-----------|
| 1 · Bienvenida + Guía | 0 | Tu guía está dentro (y no es lo que esperas) | Tu guía ya está dentro. Antes de que la abras, te explico qué vas a encontrar. |
| 2 · Caso Marcos | +3d | Lo que hay debajo de &ldquo;es que soy tonto&rdquo; | Un caso clínico anonimizado que explica lo que tu hijo no te puede decir. |
| 3 · Por qué grupo | +3d | Por qué tu hijo no va a escuchar esto de ti | Lo que un grupo cerrado de adolescentes con TDAH hace que la consulta individual no puede hacer. |
| 4 · Reserva plaza | +3d | Taller TDAH adolescentes · Sept 2026 · 6 plazas | Todos los detalles. 6 plazas. Si tu hijo encaja, vamos a hablarlo. |

**Ritmo total:** 9 días.

**Condiciones entre emails (patrón idéntico a DDBEO):**
- Antes de cada email 2, 3 y 4 añadir Condición: `¿está en Taller TDAH - Inscritas?`
  - Sí → Flujo de salida
  - No → Email

**Post-secuencia (tras Email 4):**
- Copiar a grupo: `Lista General TWIM`
- Eliminar de grupo: `Guía TDAH - Padres`
- Flujo de salida

---

## Secuencia 2: Guía Bachillerato · 4 emails

**Archivos HTML:** `email-templates/talleres-bachillerato/`

| Email | Día | Asunto sugerido | Preheader |
|-------|-----|-----------------|-----------|
| 1 · Bienvenida + Guía | 0 | Tu guía está dentro (y no es lo que esperas) | Tu guía ya está dentro. Antes de abrirla, te explico qué vas a encontrar y qué no. |
| 2 · No es apatía | +3d | No es apatía. Es miedo a elegir. | Lo que tu hijo no te puede explicar sobre por qué ya no le importa nada. |
| 3 · Por qué grupo | +3d | Por qué tu hijo no va a escuchar esto de ti | Por qué tu hijo va a aceptar de otro adolescente lo que no te acepta a ti. |
| 4 · Reserva plaza | +3d | Taller Bachillerato · Sept 2026 · 6 plazas | Todos los detalles. 6 plazas. Si tu hijo encaja, vamos a hablarlo. |

**Ritmo total:** 9 días.

**Condiciones:** idéntico patrón a secuencia TDAH pero comprobando `Taller Bachillerato - Inscritas`.

**Post-secuencia (tras Email 4):**
- Copiar a grupo: `Lista General TWIM`
- Eliminar de grupo: `Guía Bachillerato - Padres`
- Flujo de salida

---

## Checklist de activación (orden)

### 1. Netlify Dashboard
Añadir env vars (Settings → Environment variables):
- [ ] `MAILERLITE_API_KEY` (la key de MailerLite)
- [ ] `MAILERLITE_GROUP_LEAD_MAGNET` (ID grupo DDBEO — ya debe existir)
- [ ] `MAILERLITE_GROUP_RETO` (ID grupo Reto 7 Días — ya debe existir)
- [ ] `MAILERLITE_GROUP_GENERAL` (ID Lista General TWIM)
- [ ] `MAILERLITE_GROUP_PADRES_TDAH` (ID grupo Guía TDAH)
- [ ] `MAILERLITE_GROUP_PADRES_BACH` (ID grupo Guía Bachillerato)

### 2. MailerLite
- [ ] Crear los 5 grupos listados arriba
- [ ] Pegar el HTML de cada email en un nuevo email de MailerLite
- [ ] Configurar asunto y preheader de cada email según la tabla
- [ ] Construir automatización "Secuencia Guía TDAH" con trigger → grupo
- [ ] Construir automatización "Secuencia Guía Bachillerato" con trigger → grupo
- [ ] Añadir condiciones entre emails (idéntico patrón a DDBEO)
- [ ] Añadir bloques post-secuencia (copiar/eliminar grupos)
- [ ] Prueba de envío a tu propio correo (los 8 emails)
- [ ] Activar ambas automatizaciones

### 3. Web (homepage form)
- [ ] Dividir `workshops-info-form` en dos formularios (TDAH / Bachillerato) **O** añadir un `<select>` con radio buttons que mande el grupo correcto
- [ ] Actualizar el `group` que envía la Netlify Function según qué guía descargue

---

## Notas
- Los emails ya vienen con variables `{$name}`, `{$unsubscribe}` y `{$url}` de MailerLite.
- El sistema visual es idéntico a la secuencia DDBEO (hero verde degradado, Barlow Condensed, CTA beige, footer verde oscuro).
- Los casos clínicos (Marcos, Laura) son ficticios. Se indica explícitamente en la PD para cumplir el compromiso de no usar testimonios reales de pacientes.
- Los enlaces a landing pages apuntan a `#cta-final` para que el usuario caiga directo en el formulario.
