# Pegar contenido en las 3 automations de listas/lead — 21 may 2026

> **Por qué este doc.** Las 3 automations creadas el 20-may vía MCP MailerLite quedaron con la carcasa (trigger + subject + remitente) pero **sin cuerpo HTML diseñado** (`is_designed: false` confirmado en API). El conector MCP solo permite editar `plain_text` vía `update_automation_email`, no HTML del builder. Auditoría completa registrada en `contenido-rrss/te-escribo-newsletters/PLAN-CAPTACION-30D.md` §6 del 21-may.

> **Actualización 11 jun 2026 (verificado contra API MailerLite):**
>
> - Las automations **2 (DDBEO) y 3 (DDO) ya están ACTIVAS** (`enabled: true`, emails diseñados en builder, envíos de prueba realizados). El estado «en borrador» de este doc quedó obsoleto.
> - La automation **1 (lead magnet 5 señales, `188015660948784728`) ya NO existe** · fue sustituida el 26-may por «Secuencia · Lista espera Volver a Mí · 3 emails» (`188524234377528522`, activa, copy propio sin la frase de jerga). El cuerpo de la sección 1 queda solo como referencia histórica.
> - **Cambio de copy 11 jun** (criterio claridad de un vistazo, mismo aplicado a la web en PR #334): se elimina «sin secuencia agresiva» de los cuerpos de este doc — es jerga de embudo que el público no entiende a la primera. Sustituido por «solo el capítulo».
> - **Pendiente manual de Daniel (1 línea, ~2 min):** el email VIVO de la automation DDBEO aún dice «Te lo regalo en PDF, sin secuencia agresiva:» (verificado en captura del builder). Editar en panel → <https://dashboard.mailerlite.com/automations/188015669577516322> → step de email → cambiar esa línea por «Te lo regalo en PDF · solo el capítulo:». El email vivo de DDO está limpio (no lleva la frase).

## Flujo para activar cada automation (5 min cada una)

1. Abrir <https://dashboard.mailerlite.com/automations/status/drafts>.
2. Hacer clic en la automation (`Editar`).
3. Hacer clic en el step de email → `Editar contenido`.
4. Elegir plantilla en blanco o cualquier plantilla simple TWIM. Pegar el cuerpo del email correspondiente (sección «Cuerpo del email» de este doc).
5. Cerrar el editor de email. **Cambiar el idioma a Español** en `Configuración del email → idioma` (importante: por defecto se queda en inglés y el footer legal saldría en inglés).
6. Volver al canvas del workflow. El badge debería decir «El flujo de trabajo está completo».
7. Activar el toggle del workflow (esquina superior derecha) → confirmar.

## 1 · Secuencia · Lead magnet 5 señales + lista taller

- **Automation ID:** `188015660948784728`
- **Trigger:** suscriptor entra al grupo `Lead · Pre-venta Volver a Mí` (`188015567896052961`).
- **Subject (ya cargado, no tocar):** `Aquí tienes «5 señales de hambre de mirada» + estás en la lista del taller`

### Cuerpo del email

```
Hola,

Aquí tienes el documento que te prometí.

«5 señales de hambre de mirada · cómo entender ese tirón hacia la mirada del otro que no se va con razones.» Te lo dejo en PDF aquí:

→ https://twimproject.com/talleres/volver-a-mi/pdfs/lead-magnet-5-senales-hambre-de-mirada.pdf

Aprovecho para confirmarte que estás en la lista del taller «Volver a Mí». No es una pre-venta dura todavía · la pre-venta empezará el 1 de septiembre. Cuando esté abierta, te avisaré primero a ti, antes que al resto.

Mientras tanto, en mi newsletter «Te escribo» voy publicando piezas más largas sobre la mente, el cansancio y lo que no se dice. Si quieres recibirlas, te puedes apuntar aquí:

→ https://twimproject.com/newsletter/

Y si te interesa entender cómo se monta la voz interna que juzga (el aparato Yo / Ello / Superyó), te regalo el Capítulo III de mi libro «Los Engranajes de la Mente» en PDF · solo el capítulo:

→ https://twimproject.com/libro/capitulo-3/

— Daniel
Psicólogo General Sanitario · Col. CV11515 · Valencia
```

---

## 2 · Secuencia · Lista espera Deja de Buscarte en Otros

- **Automation ID:** `188015669577516322`
- **Trigger:** suscriptor entra al grupo `Lead · Lista espera · Deja de Buscarte en Otros` (`188015570570970973`).
- **Subject (ya cargado, no tocar):** `Estás en la lista · «Deja de Buscarte en Otros»`

### Cuerpo del email

```
Hola,

Te confirmo que estás en la lista de espera de «Deja de Buscarte en Otros».

Es un programa en producción. Aún no está disponible. La ventana de grabación se abre el 15 de junio y se cierra a finales de julio · estimación realista de entrega · finales de verano 2026.

Cuando esté listo, te aviso primero a ti, antes que al resto, y con condiciones de lista de espera (no precio inflado, no urgencia falsa, no upsells por todas partes).

Mientras tanto, si lo que te trajo hasta aquí fue la sensación de buscarte en el otro y no encontrarte, en el Capítulo III de mi libro «Los Engranajes de la Mente» toco un fragmento adyacente sobre cómo se monta el juez interno que aprende a hablarte con voz de los demás. Te lo regalo en PDF · solo el capítulo:

→ https://twimproject.com/libro/capitulo-3/

Y si quieres recibir mis cartas «Te escribo» cada tanto (sobre la mente, el cansancio y lo que no se dice):

→ https://twimproject.com/newsletter/

— Daniel
Psicólogo General Sanitario · Col. CV11515 · Valencia
```

---

## 3 · Secuencia · Lista espera Deja de Obligarte

- **Automation ID:** `188015675634091134`
- **Trigger:** suscriptor entra al grupo `Lead · Lista espera · Deja de Obligarte` (`188015573363328332`).
- **Subject (ya cargado, no tocar):** `Estás en la lista · «Deja de Obligarte»`

### Cuerpo del email

```
Hola,

Te confirmo que estás en la lista de espera de «Deja de Obligarte».

Es un programa en revisión de formato. Estimación realista de entrega · finales de 2026.

Cuando esté listo, te aviso primero a ti, antes que al resto, y con condiciones de lista de espera.

Mientras tanto, si lo que te trajo hasta aquí fue la sensación de que te obligas todo el día (al trabajo, a estar bien, a rendir, a no parar), en mis cartas «Te escribo» voy publicando piezas sobre eso · el cansancio que no es físico, la voz que te juzga, el sistema interno que se monta para regular el malestar y termina pesando más que la vida que regulaba.

Si quieres recibirlas:

→ https://twimproject.com/newsletter/

Y si te interesa entender cómo se monta la voz interna que te empuja a obligarte (el aparato Yo / Ello / Superyó), te regalo el Capítulo III de «Los Engranajes de la Mente» en PDF:

→ https://twimproject.com/libro/capitulo-3/

— Daniel
Psicólogo General Sanitario · Col. CV11515 · Valencia
```

---

## Verificación post-activación

Tras activar cada automation, suscribirse uno mismo (Daniel) con un email de prueba al grupo correspondiente, verificar que el email llega en castellano (incluido el footer legal), que los links funcionan, y que el grupo `active_count` sube de 0 → 1. Después borrar la suscripción de prueba.

## Por qué este copy y no otro

- **Anti-coaching, descriptivo, tuteo · alineado con voz TWIM.**
- **Honestidad clínica · ningún producto se vende como inminente.** Las fechas reales del producto van en cada email para que el suscriptor sepa qué esperar.
- **Cross-sell honesto a Cap 3 + newsletter en los 3 emails.** El embudo aprovecha que quien entra ya tiene intención emocional · el cross-sell convierte mejor en ese momento que en cualquier otro.
- **Sin emojis, sin frases motivacionales, sin urgencia falsa.**
- **Cierre con CV11515 y Valencia · firma operativa estable** (igual que Carta #1, Carta #2 y Recado 01).
