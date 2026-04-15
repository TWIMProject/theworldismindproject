# Setup MailerLite · Reto 7 Días (Deja de Buscarte en Otros)

Secuencia de 8 emails (día 0 bienvenida + día 1-7) para el reto gratuito al que se apuntan desde `reto-7-dias.html`.

---

## Grupos a usar en MailerLite

| Grupo | Trigger | Netlify env var |
|-------|---------|-----------------|
| `Reto 7 Días` | Registro desde `reto-7-dias.html` | `MAILERLITE_GROUP_RETO` |
| `Lista General TWIM` | Post-secuencia (tras email 7) | `MAILERLITE_GROUP_GENERAL` |

El formulario de la landing ya envía `group: 'reto-7-dias'` a `/.netlify/functions/subscribe`. La Netlify Function lo mapea al env var `MAILERLITE_GROUP_RETO` (ver `netlify/functions/subscribe.js:42`). **No hay cambios que hacer en web**, solo en MailerLite.

---

## Secuencia · 8 emails

**Archivos HTML:** `email-templates/reto-7-dias/`

| Email | Archivo | Día (delay) | Asunto | Preheader |
|-------|---------|-------------|--------|-----------|
| 0 · Bienvenida | `email-0-bienvenida.html` | **0** (inmediato al suscribirse) | Estás dentro. Te explico qué va a pasar estos 7 días. | 7 días, 7 observaciones de 10 minutos. Mañana empezamos. Hoy te cuento qué vas a encontrar y qué no. |
| 1 · Registro | `email-1-registro.html` | **+1 día** | Día 1 · Cuántas veces al día buscas que te confirmen | Primer ejercicio. Solo observar. No cambiar nada. 10 minutos repartidos a lo largo del día. |
| 2 · Mapa | `email-2-mapa.html` | **+1 día** | Día 2 · Tu dependencia tiene lugares favoritos | Las búsquedas no son aleatorias. Tienen lugares preferidos. Hoy los identificas. |
| 3 · Juez | `email-3-juez.html` | **+1 día** | Día 3 · La frase que te dices justo antes | Justo antes de buscar confirmación hay una frase. Hoy la vas a oír literal, sin cambiarla. |
| 4 · Cuerpo | `email-4-cuerpo.html` | **+1 día** | Día 4 · Dónde sientes la urgencia antes de pensarla | El cuerpo se entera antes que la cabeza. Hoy aprendes a escucharlo. |
| 5 · Máscara | `email-5-mascara.html` | **+1 día** | Día 5 · Qué máscara usa tu dependencia | Entrega excesiva, hipervigilancia, evitación, idealización, culpa. Una es tuya. |
| 6 · Ciclo | `email-6-ciclo.html` | **+1 día** | Día 6 · Ver el circuito entero | Disparador → duda → búsqueda → alivio → vacío. Hoy lo ves en directo. |
| 7 · Revisión + CTA | `email-7-revision.html` | **+1 día** | Día 7 · Lo que has visto esta semana | Última observación del reto. Qué has visto, y qué viene después si quieres seguir. |

**Ritmo total:** 8 días (día 0 al sumarse + 7 días consecutivos). Se recomienda enviar siempre a la misma hora (ej. 9:00 hora España).

---

## Condiciones entre emails (opcional pero recomendado)

Si el suscriptor se da de baja o se va a otro grupo durante el reto, MailerLite lo saca automáticamente. No hace falta condición extra.

**Condición recomendada antes del Email 7 (CTA al programa):**
- Antes del Email 7, añadir `Condición: ¿está en grupo "Deja de Buscarte en Otros - Comprado"?`
  - Sí → Flujo de salida (no spammear con CTA a quien ya lo compró)
  - No → Email 7

Si aún no tienes ese grupo de compradores creado, sáltate la condición por ahora.

---

## Post-secuencia (tras Email 7)

Añadir al final de la automatización:
1. **Copiar a grupo:** `Lista General TWIM`
2. **Eliminar de grupo:** `Reto 7 Días`
3. **Flujo de salida**

De esta forma los suscriptores del reto alimentan la lista general de TWIM (newsletter habitual, lanzamientos futuros) y se liberan del grupo del reto para poder entrar otra vez si en algún momento se relanza la secuencia.

---

## Checklist de activación (orden)

### 1. Netlify Dashboard
Verificar env vars (Settings → Environment variables):
- [ ] `MAILERLITE_API_KEY` (ya debe existir)
- [ ] `MAILERLITE_GROUP_RETO` (ya debe existir — es el grupo al que el form ya manda)
- [ ] `MAILERLITE_GROUP_GENERAL` (ya debe existir)

Si alguna falta, la función `subscribe.js` dará 500 y el ad de IG está quemando tráfico. Revisa.

### 2. MailerLite · crear los 8 emails
Para cada email de la tabla:
- [ ] Nuevo email en MailerLite
- [ ] Copiar HTML del archivo correspondiente en `email-templates/reto-7-dias/`
- [ ] Pegarlo en la vista de código fuente (editor HTML, no drag-and-drop)
- [ ] Asunto y preheader según tabla
- [ ] Nombre/email de remitente: `Daniel Orozco <danielorozco@twimproject.com>` (o el que uses habitualmente)
- [ ] Marcar como plantilla lista para usar en automatización

### 3. MailerLite · automatización
- [ ] Crear nueva automatización: "Reto 7 Días"
- [ ] **Trigger:** Suscriptor se une al grupo `Reto 7 Días`
- [ ] **Bloque 1:** Enviar Email 0 (bienvenida) — sin delay
- [ ] **Bloque 2:** Esperar 1 día → Enviar Email 1
- [ ] **Bloque 3:** Esperar 1 día → Enviar Email 2
- [ ] **Bloque 4:** Esperar 1 día → Enviar Email 3
- [ ] **Bloque 5:** Esperar 1 día → Enviar Email 4
- [ ] **Bloque 6:** Esperar 1 día → Enviar Email 5
- [ ] **Bloque 7:** Esperar 1 día → Enviar Email 6
- [ ] **Bloque 8:** Esperar 1 día → Enviar Email 7
- [ ] **Bloque 9 (post-secuencia):** Copiar a grupo `Lista General TWIM`
- [ ] **Bloque 10 (post-secuencia):** Eliminar de grupo `Reto 7 Días`
- [ ] **Bloque 11:** Flujo de salida

### 4. QA antes de activar
- [ ] Prueba de envío de los 8 emails a tu propio correo (desde MailerLite → vista previa → envío de prueba)
- [ ] Confirmar que los 8 se ven bien en Gmail móvil, Gmail web y Outlook (son los 3 donde más problemas hay con HTML emails)
- [ ] Confirmar que `{$name}`, `{$unsubscribe}` y `{$url}` se renderizan correctamente
- [ ] Confirmar que el CTA del Email 7 lleva a una landing que existe y funciona (hoy apunta a `https://twimproject.com/dejadebuscarteenotros.html`)

### 5. Activar
- [ ] Activar automatización
- [ ] Enviar desde un email tuyo real de prueba apuntándote tú mismo en `reto-7-dias.html`
- [ ] Confirmar que el Email 0 llega en <5 minutos
- [ ] Dejar una alerta en tu calendario para +1 día: verificar que llega el Email 1

---

## Variables MailerLite usadas en los emails

- `{$name}` → nombre del suscriptor (recogido por el form). Si el suscriptor no puso nombre, llegará vacío; el copy está escrito para que "Hola ," siga siendo aceptable.
- `{$unsubscribe}` → link de darse de baja (obligatorio por LSSI/GDPR).
- `{$url}` → link para ver el email en el navegador.

---

## Notas editoriales

- **Tono**: psicoanalítico aplicado, descriptivo, sin positivismo tóxico, sin emojis, tuteo. Voz de Daniel Orozco según `BRIEFING-PROGRAMA-DEJADEBUSCARTE.md`.
- **Publico**: mujeres 25-50 con dependencia emocional / necesidad de validación externa.
- **No se usan testimonios reales de pacientes**. Los ejemplos son genéricos o inventados.
- **El Email 7 incluye CTA al programa pagado**. Los emails 0-6 NO venden. Son pura educación/observación para construir confianza.
- **Ritmo de 1 email al día** = el compromiso prometido en la landing (`reto-7-dias.html` línea 506: "Recibes un email al día durante 7 días"). NO alargar ni acortar sin actualizar la landing.

---

## Si quieres personalizar más tarde

- **A/B test del Email 0**: probar variante con/sin lista "Qué no vas a encontrar" (puede leerse negativo para algunos perfiles).
- **Trigger complementario**: cuando alguien compra el programa, sacarla automáticamente del grupo `Reto 7 Días` para no mandar el Email 7 con CTA al programa que acaba de comprar.
- **Resend**: si el open rate del Email 0 baja de 40%, probar re-send a no-abridores con asunto alternativo ("Te acabas de apuntar al reto. Así empezamos").
