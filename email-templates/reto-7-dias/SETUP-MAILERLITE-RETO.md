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

## Paso a paso detallado (panel de MailerLite "nuevo", app.mailerlite.com)

> Asume que usas la interfaz nueva (rediseño 2020+). Si ves "MailerLite Classic" en el login, algunas rutas cambian pero los pasos son equivalentes.

### Paso 0 · Preflight (5 min)

1. **Verificar env vars en Netlify** (si ya las tenías, salta este paso):
   - Netlify → site `twimproject` → **Site configuration** → **Environment variables**
   - Comprobar que existen: `MAILERLITE_API_KEY`, `MAILERLITE_GROUP_RETO`, `MAILERLITE_GROUP_GENERAL`
   - Si `MAILERLITE_GROUP_RETO` no existe: el form ya está enviando y fallando con 500. El ad de IG estaría quemando tráfico. Revísalo primero.

2. **Verificar que el grupo existe en MailerLite:**
   - MailerLite → sidebar izquierda → **Subscribers** → **Groups**
   - Debe aparecer el grupo que corresponde al ID guardado en `MAILERLITE_GROUP_RETO`. Si no sabes cuál es, abre la env var en Netlify para copiar el ID y búscalo aquí.
   - Si no existe: créalo con **Create new group** → nombre `Reto 7 Días` → copia su ID y actualiza la env var en Netlify (Site configuration → Environment variables → edit).

3. **Verificar dominio autenticado** (solo si es la primera vez que envías):
   - MailerLite → **Account** (arriba derecha) → **Domains**
   - `twimproject.com` debe figurar con SPF + DKIM en verde. Si no, autentica antes de seguir (Gmail puede enviar a spam si no).

---

### Paso 1 · Subir los 8 emails como plantillas (20-30 min)

Vas a crear 8 plantillas, una por email. Las vas a usar después en la automatización.

**Para cada uno de los 8 archivos en `email-templates/reto-7-dias/`:**

1. MailerLite → sidebar → **Campaigns** → botón **Create campaign** (arriba derecha).
2. Seleccionar tipo: **Regular campaign** → **Next**.
3. En **Campaign name** pon el nombre interno (ejemplo: `Reto D0 · Bienvenida`). Este nombre solo lo ves tú.
4. En **Subject** pega el subject de la tabla de arriba (ejemplo D0: `Estás dentro. Te explico qué va a pasar estos 7 días.`).
5. **Preheader**: pega el preheader de la tabla.
6. **From name:** `Daniel Orozco` — **From email:** el que uses habitualmente (recomendado: `daniel@twimproject.com` o similar).
7. **Language:** Spanish. **Next**.
8. En el selector de editor, elegir **Custom HTML editor** (NO el drag-and-drop, NO el rich text). Es un botón/tarjeta que suele estar abajo del todo con etiqueta "HTML editor" o "Code your own".
9. Abrir el archivo `.html` local (VSCode), seleccionar TODO (`Ctrl+A` / `Cmd+A`), copiar, y pegar en el editor de código de MailerLite reemplazando lo que haya.
10. Click en **Save** (arriba derecha).
11. **IMPORTANTE:** NO envíes la campaña. En vez de eso, sube-lo como plantilla:
    - MailerLite → sidebar → **Campaigns** → al lado de esta campaña aparece un menú `...` → **Save as template**. Nombre de plantilla: `Reto D0 - Bienvenida` (mismo nombre que la campaña).
    - Alternativa: crea directamente la plantilla vía **Templates** → **Create template** → HTML editor. Más limpio si no te importa saltarte el flujo de campaña.

**Repite los pasos 1-11 para los 8 emails** (día 0 bienvenida, día 1 registro, …, día 7 revisión). Al terminar tienes 8 plantillas en **Templates**.

**Test rápido**: antes de seguir, envíate el Email 0 a ti mismo:
- Abrir la plantilla → **Send a test email** → pon tu correo → Enviar.
- Verifica en Gmail móvil, Gmail web y Outlook (son los 3 clientes que más suelen romper HTML).
- Confirma que `{$name}` se sustituye por algo (si envías test, suele salir vacío o con el nombre de tu cuenta — ok).
- Si algo se ve raro, dímelo con captura y lo arreglo en el HTML del repo.

---

### Paso 2 · Crear la automatización (10 min)

1. MailerLite → sidebar → **Automations** → botón **Create new automation**.
2. **Name:** `Reto 7 Días`. **Next**.
3. **Trigger** → elegir `When subscriber joins a group` → grupo: `Reto 7 Días` (el del paso 0). **Save**.
4. Ahora ves el canvas vacío con el trigger arriba y un `+` debajo. Vas a construir la secuencia haciendo click en `+` y eligiendo el bloque.

**Construir los 8 pasos:**

| # | Bloque a añadir | Configuración |
|---|----------------|---------------|
| 1 | **Email** | Plantilla: `Reto D0 - Bienvenida`. Delay: ninguno (inmediato). |
| 2 | **Delay** | 1 day |
| 3 | **Email** | Plantilla: `Reto D1 - Registro` |
| 4 | **Delay** | 1 day |
| 5 | **Email** | Plantilla: `Reto D2 - Mapa` |
| 6 | **Delay** | 1 day |
| 7 | **Email** | Plantilla: `Reto D3 - Juez` |
| 8 | **Delay** | 1 day |
| 9 | **Email** | Plantilla: `Reto D4 - Cuerpo` |
| 10 | **Delay** | 1 day |
| 11 | **Email** | Plantilla: `Reto D5 - Máscara` |
| 12 | **Delay** | 1 day |
| 13 | **Email** | Plantilla: `Reto D6 - Ciclo` |
| 14 | **Delay** | 1 day |
| 15 | **Email** | Plantilla: `Reto D7 - Revisión` |

**Hora de envío:** dentro de cada bloque Email, en **Delivery time**, elige "Send at specific time" → **09:00** (hora España). Aplícalo a los 8 emails para que lleguen siempre a la misma hora.

**Post-secuencia (después del Email 7):**

| # | Bloque | Configuración |
|---|--------|---------------|
| 16 | **Action** → `Copy subscriber to group` | Grupo: `Lista General TWIM` |
| 17 | **Action** → `Remove subscriber from group` | Grupo: `Reto 7 Días` |

Esto mueve al suscriptor a la lista general al terminar el reto para futuras newsletters. Si no tienes todavía el grupo `Lista General TWIM` creado, crea uno igual que en paso 0.2.

5. Click **Save** arriba derecha.

---

### Paso 3 · QA con email real (10 min)

Antes de activar la automatización, prueba el flujo completo con un email tuyo real:

1. **Apúntate tú mismo** en `https://twimproject.com/reto-7-dias.html` con un email que controles (gmail personal, no el de trabajo).
2. **Verifica en Netlify** (Functions → `subscribe` → logs) que la llamada devuelve 200.
3. **Verifica en MailerLite** (Subscribers → busca tu email) que apareces en el grupo `Reto 7 Días`.
4. **Espera 2-5 minutos** → debe llegarte el Email 0 a tu bandeja.
5. Si llega → **todo bien hasta día 0**. Apunta en calendario:
   - `+24h`: debe llegar Email 1. Si no llega en ±1h, revisa en MailerLite → Automations → `Reto 7 Días` → Activity, busca tu email y mira en qué paso está atascado.
   - `+2d`, `+3d`, etc. hasta `+7d`: mismo check.

**Si algo falla en mitad de la secuencia**, el suscriptor queda atascado y no avanza, pero los siguientes nuevos registros sí entran. Puedes hacer Hotfix sobre la plantilla sin parar la automatización.

---

### Paso 4 · Activar (1 min)

1. MailerLite → Automations → `Reto 7 Días` → toggle **Active** (arriba derecha, normalmente verde).
2. **A partir de ahora, cada persona que se apunte en la landing recibe los 8 emails automáticamente.**
3. Si el ad de IG está activo, monitoriza el primer día:
   - Cuántos registros entraron (MailerLite → Subscribers → grupo `Reto 7 Días`)
   - Cuántos Email 0 se abrieron (MailerLite → Automations → Activity)
   - Si la tasa de apertura del Email 0 es <50%, algo falla (asunto, spam, o envío no llega). Dímelo.

---

## Checklist rápido de activación (marcar conforme avanzas)

- [ ] Env vars Netlify verificadas (`MAILERLITE_API_KEY`, `MAILERLITE_GROUP_RETO`, `MAILERLITE_GROUP_GENERAL`)
- [ ] Grupo `Reto 7 Días` existe en MailerLite con el ID correcto
- [ ] Dominio `twimproject.com` autenticado (SPF + DKIM)
- [ ] 8 plantillas creadas en MailerLite con subject y preheader de la tabla
- [ ] Test de envío del Email 0 a tu correo → OK en Gmail móvil/web y Outlook
- [ ] Automatización `Reto 7 Días` creada con 8 bloques Email + 7 Delay + 2 Action post-secuencia
- [ ] Hora de envío configurada en 09:00 en los 8 emails
- [ ] Registro de prueba tuyo desde `reto-7-dias.html` → Email 0 llega en <5 min
- [ ] Calendario con alarmas `+24h`, `+2d`, …, `+7d` para verificar que la cadena avanza
- [ ] Automatización en estado **Active**

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
