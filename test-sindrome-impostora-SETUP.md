# Test Síndrome de la Impostora · Setup

> Asset live en `https://twimproject.com/test-sindrome-impostora.html`
> Lead magnet interactivo (CIPS adaptado) que captura emails al grupo MailerLite "Lead Magnet · Síndrome Impostora".

---

## ¿Qué hace?

Visitante responde 10 preguntas Likert (1-5) → JS calcula score 10-50 → muestra resultado en 4 bandas (bajo / moderado / frecuente / intenso) → form de captura email opcional → POST a `/.netlify/functions/subscribe` con grupo `lead-magnet-impostora`.

GA4 events que dispara:
- `impostor_test_completed` (con `score` y `band`)
- `impostor_lead_signup` (con `score`)

---

## Lo que aún tienes que hacer (5 min en MailerLite + Netlify)

### 1 · Crear el grupo en MailerLite

1. https://dashboard.mailerlite.com/subscribers/groups → **+ Create group**
2. Nombre: `Lead Magnet - Síndrome Impostora`
3. → Crear → copiar el **ID del grupo** (lo verás en la URL del grupo, ej. `186XXXXX...`)

### 2 · Añadir env var en Netlify

Site configuration → Environment variables → **Add variable**:
- Nombre: `MAILERLITE_GROUP_LEAD_IMPOSTORA`
- Valor: el ID que copiaste arriba

→ Guardar → trigger re-deploy en Netlify (Deploys → Trigger deploy → Deploy site)

### 3 · (Opcional pero potente) Crear automation de seguimiento

Cuando la env var esté configurada, los suscriptores irán entrando al grupo. Si quieres que reciban automáticamente el "análisis personalizado por email" que les prometo en el copy del test, monta una secuencia básica:

**Trigger:** Cuando un suscriptor se une al grupo `Lead Magnet - Síndrome Impostora`

**Email 1 (inmediato):** "Tu análisis del test"
- Asunto: `Sobre tu resultado en el test (lo que indica de fondo)`
- Plain text:

```
Hola {$name},

Acabo de ver tu resultado del test del síndrome de la impostora.

Te paso una lectura más profunda de lo que indica esa puntuación, que el test no te puede dar por sí solo:

El síndrome de la impostora no es "falta de confianza" — es un patrón mucho más específico. Lo que se activa es un Superyó interno que necesita que sigas siendo "la que se esfuerza" para validarte. Cuando hay éxito, ese Superyó no te deja apropiártelo: lo atribuye a la suerte, al engaño, al momento. Si lo apropiaras, ya no necesitarías esforzarte tanto — y eso, internamente, es lo que se vive como peligroso.

La parte difícil: no se desactiva con autoafirmaciones. Esas son del Yo, y el Yo no manda en este conflicto. Se desactiva cuando entiendes qué está protegiendo el patrón, qué te garantiza mantenerlo.

Si quieres explorar esto con más profundidad, en TWIM Project tengo un programa específico de 6 sesiones de 90 min en grupo cerrado. Es donde se trabaja exactamente este mecanismo desde la psicología profunda. Si te interesa el formato, escríbeme y hablamos.

Mientras tanto, este artículo te puede acompañar:
https://twimproject.com/insights/sindrome-del-impostor-cuando-mejor-te-va.html

Un abrazo,
Daniel Orozco
Psicólogo General Sanitario · CV11515
```

**Email 2 (3 días después):** "Caso clínico (Marta, 38 años, médico)"
**Email 3 (5 días después):** "El programa: cuándo abre y cómo funciona"
**Email 4 (3 días después):** "Te dejo en mi newsletter mensual"

(Estos los redactas tú o me pides que los escriba — son secuencia tipo nurturing similar a los talleres.)

---

## Pendiente programa síndrome impostora

El test acaba apuntando a "un programa" que mencionas pero que aún no tiene landing dedicada en el site. Cuando lo crees, conecto el cross-sell del test al programa directamente. Mientras, el test funciona como captador puro al grupo MailerLite.

---

## Preguntas frecuentes (para ti, no para usuarios)

**¿Por qué no incluí precio del programa en el test?**
Porque el visitante todavía no está listo para ver precio. El test capta interés cualificado (rellena 10 preguntas + email = baja fricción/alta señal), y la secuencia de emails va calentando hasta el pitch del programa. Vender en frío después del test bajaría conversión.

**¿Por qué CIPS adaptado y no otro?**
Es el instrumento más usado en literatura clínica desde 1985 (Pauline Rose Clance). Adaptación al español con ítems redactados en lenguaje cotidiano. No es diagnóstico — está claro en la intro — pero da una buena señal de orientación.

**¿Qué hago con los resultados altos (40-50)?**
Esos perfiles son tu cliente ideal del programa. Cuando recibas el lead, mira la `meta.test_score` que llegará en `subscribe.js` (si añadimos el campo en MailerLite, lo guarda como tag). Los 40+ deberían recibir trato preferencial.
