# Automation MailerLite · «Lectores · Engranajes Cap3»

> Documento operativo creado el **13 may 2026 ~12:00 CEST** en la sesión `claude/improve-proposal-quality-pq3d9`. Acompaña al PR que activa el lead magnet del Capítulo III «El Yo frente al Superyó» del libro *Los Engranajes de la Mente*.
>
> Función: dejar por escrito el grupo, las variables de entorno, la secuencia de 3 emails y las métricas a vigilar — para que Daniel pueda terminar la pieza desde el dashboard MailerLite + Netlify sin tener que ensamblar nada desde memoria.

---

## 1 · TL;DR — qué falta por tu lado

Después del merge del PR, **tres cosas manuales** que solo tú puedes hacer (yo no tengo acceso al dashboard MailerLite ni a las env vars de Netlify):

1. **Crear el grupo** «Lectores · Engranajes Cap3» en MailerLite. Apuntar el ID.
2. **Añadir la env var** `MAILERLITE_GROUP_LEAD_ENGRANAJES_CAP3` en Netlify con el ID del grupo.
3. **Crear la automation** con los 3 emails de la §3 de este doc, activarla.

Tiempo total estimado: 60-90 min (la mayor parte es pegar el copy de los 3 emails y revisarlos).

---

## 2 · Setup paso a paso

### 2.1 · Crear el grupo en MailerLite

- Dashboard MailerLite → **Subscribers** → **Groups** → **Create group**.
- Nombre: `Lectores · Engranajes Cap3`.
- Descripción interna: *«Suscriptores que descargaron el Capítulo III gratuito desde `/libro/capitulo-3/`. Entrada al embudo del libro Engranajes y a la newsletter Te escribo.»*
- Guardar y copiar el **Group ID** (formato `185xxxxxxxxxxxxxxx`).

### 2.2 · Añadir la env var en Netlify

- Netlify → site `twimproject` → **Site configuration** → **Environment variables** → **Add a single variable**.
- Key: `MAILERLITE_GROUP_LEAD_ENGRANAJES_CAP3`
- Value: el Group ID del paso 2.1.
- Scope: All scopes (production + previews).
- Guardar. Redeploy del site (Netlify lo hace automáticamente al cambiar env vars, pero verificar que pasa).

### 2.3 · Verificar conexión

Una vez desplegado, abrir `https://twimproject.com/.netlify/functions/subscribe?diag=1`. El JSON devuelto debe incluir `MAILERLITE_GROUP_LEAD_ENGRANAJES_CAP3: true`. Si aparece `false`, la env var no se ha propagado — revisar.

### 2.4 · Test funcional end-to-end

- Abrir `/libro/capitulo-3/` en una ventana de incógnito.
- Rellenar form con un email tuyo de prueba (gmail funciona bien).
- Verificar:
  - El mensaje de éxito aparece y el botón de descarga directa funciona.
  - El email de bienvenida (email D0 de la §3.1 de este doc) llega en < 60 segundos.
  - El suscriptor aparece en el grupo «Lectores · Engranajes Cap3» en MailerLite.
  - GA4 recibe el evento `cap3_lead_capture` en tiempo real (DebugView).

---

## 3 · La secuencia · 3 emails

> Todos los emails firmados como Daniel Orozco · `danielorozco@twimproject.com`. Sin imágenes pesadas, en HTML simple (mismo estilo que las Cartas «Te escribo»). Plain text version recomendable.

### 3.1 · Email D0 — entrega inmediata · «Aquí lo tienes»

**Asunto:** Aquí lo tienes — Capítulo III de Los Engranajes

**Preview text:** Las 21 páginas sobre la voz que te dice que no es suficiente.

**Trigger:** inmediato tras añadirse al grupo.

**Cuerpo:**

```
Hola, {{name|"hola"}}.

Aquí tienes el Capítulo III de Los Engranajes de la Mente.

[BOTÓN] Descargar el PDF (21 páginas) → https://twimproject.com/libro-engranajes-mente/lead-magnet/capitulo-3-superyo.pdf

Es el capítulo sobre la voz interna que te dice «no es suficiente», «esto te ha quedado regular», «otros lo habrían hecho mejor».

No la imaginas. Tiene historia, tiene nombre y tiene función. Este capítulo va de cómo se monta esa voz, por qué no se calla con razones ni con motivación, y qué cosa muy concreta sí empieza a debilitarla.

Léelo despacio. No es ejercicio, no es deber. Es lectura.

Si al cerrarlo te has visto en alguna escena, te escribo en unos días con una pregunta más concreta.

— Daniel

PD: Si el PDF no te llega o se te ha colado a promociones, escríbeme respondiendo a este correo y te lo paso por aquí.
```

### 3.2 · Email D3 — reflexión · «¿Te has visto en alguna escena?»

**Asunto:** ¿Te ha movido algo el capítulo?

**Preview text:** Una pregunta concreta, antes de que cierres el documento y te olvides.

**Trigger:** 3 días después del email D0.

**Cuerpo:**

```
Hola, {{name|"hola"}}.

¿Has tenido tiempo de leerlo?

Si te ha llegado, lo más probable es que te hayas reconocido en alguna de las frases del juez interno («no estás siendo bastante», «otros lo habrían hecho mejor»…). La mayoría de personas que descargan ese capítulo me responden este email diciendo cuál de las cinco les sonaba más a algo que se dirían hoy.

Si te apetece contestarme, lo leo personalmente.

Si todavía no has tenido tiempo, no pasa nada. El PDF sigue ahí, no caduca:

→ https://twimproject.com/libro-engranajes-mente/lead-magnet/capitulo-3-superyo.pdf

Una cosa más, que viene en el capítulo y que conviene subrayar:

«El cambio no es decir "soy suficiente". Es notar quién está hablando antes de creérselo.»

Esa frase es pequeña pero compleja. La trabajo más a fondo en las cartas que mando cada tanto desde Te escribo y en el programa Deja de Buscarte en Otros, que es para gente que ya está cansada de discutir la voz y quiere empezar a verla.

De eso te escribo en unos días.

— Daniel
```

### 3.3 · Email D7 — puente al programa / a la newsletter · «Si te ha llegado, hay sitio donde seguir»

**Asunto:** Cuando ya has leído pero sigues haciendo lo mismo

**Preview text:** El paso que casi nadie nombra entre saber qué te pasa y dejar de hacerlo.

**Trigger:** 7 días después del email D0.

**Cuerpo:**

```
Hola, {{name|"hola"}}.

Hay una distinción que casi nadie hace y que es la base de todo lo que escribo:

Comprender ≠ elaborar.

Comprender es del intelecto. Es leer un buen capítulo y decir «ah, claro». Es rápido, limpio, no duele. Por eso no cambia nada.

Elaborar es del cuerpo, del afecto, del dolor concreto que decidiste no sentir cuando te pasó la primera vez. Por eso sí cambia las cosas.

Si has leído el Capítulo III y te has reconocido en la voz que te juzga, ya estás del lado del «comprender». Esa parte está hecha.

La parte de «elaborar» —dejar de obedecer a esa voz en automático— es un trabajo más largo. Tres caminos honestos, según lo que necesites:

1) Si lo que quieres es seguir leyendo despacio, sin ruido y sin nada que comprar: Te escribo. Una carta cada tanto, sobre la mente, el cansancio y lo que no se dice.
   → https://twimproject.com/newsletter/

2) Si lo que quieres es el libro completo (hay otros cinco capítulos como el que has leído):
   → https://www.amazon.es/dp/B0FR8PSQT3

3) Si lo que quieres es trabajar el patrón en concreto — dejar de buscarte en otros, dejar de obedecer al juez, dejar de validarte por fuera — tengo un programa autoguiado pensado para eso. 79 €, sin terapeuta de por medio. Lo trabajas a tu ritmo en un mes.
   → [LINK al programa Deja de Buscarte en Otros · pendiente de añadir cuando el link público esté listo]

No tienes que elegir hoy. Lo que sí: no dejes que el capítulo se quede en «interesante». Algo del orden de las decisiones tiene que mover.

— Daniel

Daniel Orozco Abia
Psicólogo General Sanitario · CV11515
twimproject.com
```

---

## 4 · Métricas a vigilar (revisar lunes)

| Métrica | Fuente | Cota saludable mes 1 | Cota objetivo mes 3 |
|---|---|---|---|
| Suscriptores netos nuevos al grupo / semana | MailerLite | ≥ 5 | ≥ 20 |
| Open rate Email D0 | MailerLite | ≥ 60 % | ≥ 70 % |
| Click rate Email D0 → PDF | MailerLite | ≥ 50 % | ≥ 65 % |
| Open rate Email D3 | MailerLite | ≥ 40 % | ≥ 50 % |
| Open rate Email D7 | MailerLite | ≥ 35 % | ≥ 45 % |
| Click rate Email D7 → newsletter o programa | MailerLite | ≥ 8 % | ≥ 15 % |
| Unsubscribe rate del grupo | MailerLite | < 3 % | < 2 % |
| Visitas únicas a `/libro/capitulo-3/` | GA4 | ≥ 30/semana | ≥ 150/semana |
| Conversión visitante → lead (form submit) | GA4 (`cap3_lead_capture`) | ≥ 15 % | ≥ 25 % |
| Compras del libro en Amazon atribuibles | Amazon KDP + correlación temporal | ≥ 2/mes | ≥ 10/mes |

Si en 60 días el open rate D0 está < 50 % o el click rate D0 < 35 %, el problema es el asunto/preview del email D0 — A/B testar.

Si la conversión visitante → lead está < 10 % a los 30 días, el problema es la landing `/libro/capitulo-3/` — revisar hook del hero, peso visual del form, o testimonios verbatim (pendientes de pegar desde Amazon).

---

## 5 · Refs

- PDF lead magnet: `/libro-engranajes-mente/lead-magnet/capitulo-3-superyo.pdf` (363 KB · 23 págs: portadilla + 21 del Cap III + cierre).
- Script reproducible: `scripts/generar-lead-magnet-cap3.py`.
- Landing: `/libro/capitulo-3/index.html`.
- Netlify Function: `netlify/functions/subscribe.js` (grupo `lead-magnet-engranajes-cap3`).
- Decisión científica de elegir el Cap III: chat sesión 13 may, scoring 23/25 contra 4 candidatos.
- CEO doc §3.6 (libro como puerta inversa) y §7.3 palanca 3 (activar libro como puerta inversa al ecosistema): justificación estratégica.
- Plan de captación newsletter §2 (`PLAN-CAPTACION-30D.md`): cómo encaja este nuevo embudo con el de Reto 7 días + Te escribo.

---

**Última actualización:** 13 may 2026 ~12:00 CEST · sesión `claude/improve-proposal-quality-pq3d9`. Próxima revisión sugerida: una vez Daniel haya creado el grupo + automation, hacer test E2E (§2.4) y anotar la fecha de primera lead real captada en el log §6 de `PLAN-CAPTACION-30D.md`.
