# Directo «La voz que te juzga» · domingo 7 jun 2026 · 19:00

> **🚨 CORRECCIÓN DE FECHA · 25 may 2026.** El directo se anunció inicialmente para «domingo 8 jun» pero **el 8 de junio de 2026 es LUNES**, no domingo (detectado por un amigo de Daniel). Domingo más cercano hacia atrás = **7 jun**. Decisión Daniel · mantener «domingo» (audiencia óptima) y mover fecha al 7 jun · solo 1 día de diferencia, mínimo impacto (1 sola suscrita real al hacer el cambio). Cambios aplicados en cascada el 25-may en repo + MailerLite (automation registro `187662509833979144` actualizada vía MCP, grupo `187662493483533365` renombrado a `(7 jun)`, **campaña promo `187974522939377362` reprogramada vía API el 25-may 06:49 UTC con `cancel_campaign` → `update_campaign` → `schedule_campaign`** — HTML con «Domingo 7 de junio, 19:00» + URL correcta; `scheduled_for: 2026-06-03 19:00 CEST` (= 17:00 UTC); status `ready`). **Google Calendar creado vía MCP el 25-may** · evento ID `p5f6uqf6fsr0sitslqrciq7hu8` el `2026-06-07T19:00:00 Europe/Madrid` con Meet `https://meet.google.com/fsu-scrz-res` adjunto en descripción + 3 recordatorios popup (24h/1h/15min). Pendiente Daniel · cambiar idioma a Español en panel MailerLite (arista MCP, `language_id` no expuesto) + quote-tweet correcc en X (hilo no editable) + email manual a la suscrita real. El **nombre del archivo se mantiene `*-8-jun-2026.md`** por trazabilidad histórica · no renombrar.

> Creado el 16 may 2026, sesión `claude/improve-proposal-quality-pq3d9`. Kit completo del directo único de captación. Fundamentado en `plan-captacion-verano-2026.md` (Fase 1), `palancas-venta-libro-engranajes-15-may-2026.md`, CEO doc §6.2/§8 y `mailerlite-automation-lectores-engranajes-cap3.md` §4.

---

## 1 · Qué es y qué NO es (líneas rojas del repo)

- **Es:** un directo gratuito **único** (no recurrente), 60 min, domingo 7 jun 19:00 (hora España). Captación editorial pura: el registro por email es la entrada al embudo (newsletter + Cap III). Se graba → queda como evergreen que sigue trayendo gente meses.
- **NO es:** una venta, ni un compromiso recurrente (CEO §8: horario fijo recurrente roba tiempo de escribir; concentración sobre dispersión), ni vídeo largo de YouTube como formato sostenido. No se vende nada en directo.
- **Por qué 7 jun 19:00 (objetivo):** último domingo entero dentro de Fase 1 antes del bloque de grabación del 15 jun → 3 semanas de promoción (Carta #2 ya salió, Carta #3 «hambre de mirada» S21, Carrusel #3, carrusel «niño»). 19:00 acaba ~20:00: respeta familia y que el lunes es consulta.

## 2 · Estado del montaje (16 may)

| Pieza | Estado | ID |
|---|---|---|
| Grupo MailerLite | ✅ creado | `187662493483533365` · «Lead · Directo · La voz que te juzga (8 jun)» |
| Formulario embebido | ✅ creado, **sin diseñar** | `187662502229706033` · slug `R3OFrx` |
| Automation confirmación | ✅ creada, **sin diseñar/activar** | `187662509833979144` · «Secuencia · Directo 8 jun» |

### Pasos manuales de Daniel (solo escritorio, ~15 min — mismo patrón que Cap III)

1. **Formulario** (`dashboard.mailerlite.com/forms/187662502229706033/overview`): diseñar — solo campo **email**, paleta de marca (`#173D30 / #C2A78B / #FDFCFA`), titular y mensaje de éxito (copys en §3). Decisión **DECIDIDA 18-may: opt-in simple** (no doble) — un evento no debe perder registros tras un clic de confirmación. Cambiar en ajustes del formulario a opt-in simple.
2. **Automation** (`dashboard.mailerlite.com/automations/187662509833979144`): el email de confirmación ya tiene el copy cargado; diseñarlo en el editor (texto plano estilo «Te escribo», sin `{{name}}` ni `[BOTÓN]`, enlaces desde el icono — reglas de `mailerlite-automation-lectores-engranajes-cap3.md` §3) y **Activar**.
3. **Plataforma del directo — DECIDIDO 18-may: Google Meet.** Enlace de acceso: `https://meet.google.com/fsu-scrz-res` (enlace limpio; **no** usar el `?authuser=0` que da Google en el navegador de Daniel — fuerza su cuenta y puede fallar a otros). Daniel contrata el **plan de pago Flexible (16,20 €)**, lo que **elimina el corte de 60 min** del Meet gratuito → el directo puede durar los 60 min completos del guion §4 sin riesgo de corte.
4. **Recordatorio del día 8 jun:** crear una **campaña** a ese grupo, programada para el 8 jun ~10:00 con el enlace de acceso (copy en §3). Una segunda campaña 1 h antes (18:00) opcional.

## 3 · Copys (verbatim, listos)

### 3.1 · Formulario — titular + éxito

- **Titular:** Un domingo, una hora: la voz que te juzga.
- **Subtítulo:** Domingo 7 de junio, 19:00 (hora de España). En directo, gratuito. Déjame tu email y te mando el acceso.
- **Botón:** Reservar mi plaza
- **Mensaje de éxito:** Hecho. Tienes la plaza reservada. Te escribo el mismo domingo con el enlace de acceso (y un recordatorio una hora antes). Si ese día no puedes en directo, igual te dejo después el material.

### 3.2 · Email de confirmación

Ya cargado en la automation `187662509833979144` (asunto «Estás dentro — Directo «La voz que te juzga» (domingo 7 jun, 19:00)»). Solo diseñarlo y activarlo.

### 3.3 · Campaña recordatorio (8 jun ~10:00)

- **Asunto:** Hoy a las 19:00 — el enlace para entrar
- **Cuerpo:**
```
Hola,

Hoy es el directo. A las 19:00 (hora de España), una hora sobre la voz que te dice «no es suficiente».

Entrar aquí: [PEGAR ENLACE DE LA PLATAFORMA]

Si te lo pierdes en directo, no te preocupes: a quienes os registrasteis os dejo después el material relacionado.

Nos vemos a las 19:00.

— Daniel
```
Enlace: seleccionar «Entrar aquí» y enlazarlo a la URL de la plataforma (no pegar la URL cruda — regla de `…cap3.md` §3).

## 4 · Guion-esqueleto del directo (60 min)

Tono: descriptivo del mecanismo, anti-coaching, sin «tú puedes». Psicología profunda y aplicada.

1. **Apertura (0-5):** sin presentación larga. Una frase ancla: «Hay una voz que no elegiste y que habla como si fuera tú.» Qué vamos a ver y qué no (no es terapia, es lectura en voz alta de un mecanismo).
2. **El mecanismo (5-25):** de dónde sale el juez interno — vínculo temprano, lo que se le dice a un niño se vuelve su voz adulta (hilo del carrusel), superyó traducido. Ejemplos cotidianos, no clínicos identificables.
3. **Por qué no se calla con razones (25-40):** comprender ≠ elaborar. Por qué la motivación y el «sé positivo» no lo tocan. Qué tipo de trabajo sí.
4. **Una intervención concreta (40-52):** una cosa observable que empieza a debilitar la voz (sin convertirlo en «ejercicio de coaching»: nombrarla, notar quién habla antes de creérselo).
5. **Cierre + puente (52-60):** recapitulación. Entrega del **Capítulo III gratuito** como continuación natural («esto está escrito y ampliado aquí») y mención sobria de la newsletter «Te escribo». Sin venta. El libro completo solo se nombra como existe, no se empuja.

## 5 · Kit de promoción

### 5.1 · Carta de promoción (newsletter «Te escribo», ~3-5 días antes)

> ✅ **Programada el 20-may-2026** vía MCP MailerLite. ID campaña `187974522939377362`, status `ready`, `scheduled_for: 2026-06-03 17:00 UTC` (= miércoles **3 jun 19:00 CEST**, 5 días antes del directo). HTML en `contenido-rrss/te-escribo-newsletters/carta-promo-directo-8-jun-voz-que-te-juzga.html`.
>
> **Actualización 30-may-2026 (verificado en panel + API por Daniel y Code):**
> - **Audiencia real: `all_active_subscribers` = TODOS los suscriptores activos · 57 destinatarios** (no los 4 grupos / 49 que se anotaron al programar; la campaña quedó configurada a «todos los activos»). Decisión Daniel · mantener envío amplio (captación). Asunto, remitente verificado (`danielorozco@twimproject.com` / «Daniel Orozco - TWIM Project»), HTML español y CTA a `twimproject.com/directo-la-voz-que-te-juzga/` confirmados correctos.
> - **Idioma de la campaña → Español: CORREGIDO por Daniel el 30-may** en el panel (Configuración del email). Resuelta la arista #1 del conector (`language_id` nacía en `en-US` por API y no era editable desde MCP). Pendiente del envío: que el badge siga en «Español» al programar y que el pie legal salga en español (verificar con «Enviar una prueba»).
> - **Reprogramación final:** Daniel reprograma vía panel con «Enviar después» → **3 jun 19:00 (zona Europe/Madrid)**. Verificar que la zona horaria mostrada sea Madrid/CEST y no UTC.

```
Asunto: Te invito a una hora, en directo, sobre la voz que te juzga

Hola,

El domingo 7 de junio, a las 19:00, voy a hacer algo que no suelo: una hora en directo.

No es un curso ni una clase motivacional. Es lo que hago en las cartas, pero en voz alta y de una sentada: desmontar la voz interna que te dice «no es suficiente» — de dónde sale, por qué no se calla con razones, y qué empieza a debilitarla.

Es gratuito. Se entra con un enlace que te mando si te registras.

[Reservar mi plaza]

Si ese domingo no puedes, regístrate igual: a quienes os apuntáis os dejo después el material.

— Daniel
```
Enlace «Reservar mi plaza» → URL del formulario de registro.

### 5.2 · Caption IG / LinkedIn

```
El domingo 7 de junio, 19:00 (hora España), una hora en directo: la voz interna que te dice «no es suficiente». De dónde viene, por qué no se calla con razones, y qué empieza a debilitarla. Gratuito, con registro. Link para reservar en la bio.
```

### 5.3 · Carrusel anuncio (3 slides, sistema A2 — reutilizar plantilla del repo)

- S1: «Un domingo. Una hora. / La voz que te juzga.» (mismo estilo que el carrusel «niño»).
- S2: Qué es / qué no es (3 líneas: no es coaching · no es motivación · es leer el mecanismo en voz alta).
- S3: «Domingo 7 jun · 19:00 · gratuito / Reserva en la bio» + logo.

### 5.4 · CTA kit canales propios (capa 1 del plan Cap III — hacer esta semana)

Pegar el enlace del **formulario de registro** mientras dure la promo; tras el directo, sustituir por `twimproject.com/libro/capitulo-3/`:

- Bio Instagram (link) + Historia destacada «DIRECTO».
- LinkedIn → Featured.
- YouTube → comentario fijado + descripción de los vídeos top.
- Descripción de los podcasts (plantilla `documentos-internos/plantillas/podcast/`).
- Firma de email.
- Cross-link en las 7 landings SEO.

### 5.5 · Naming del enlace en canales (confirmado 19-may por Daniel)

> Daniel preguntó (19-may) con qué nombre etiquetar el Share URL del formulario en IG / LinkedIn / Facebook / YouTube para que se entienda de un vistazo. Coherente con el botón del formulario «Reservar mi plaza» (§3.1), el caption (§5.2) y el highlight «DIRECTO» (§5.4).

**Fórmula:** qué (directo gratuito) + tema («La voz que te juzga») + cuándo (dom 7 jun, 19:00) + acción (reservar plaza). Sin emojis (activo editorial puro, §1).

| Canal | Dónde | Nombre/etiqueta del enlace |
|---|---|---|
| Instagram | Link en bio | `Directo gratis «La voz que te juzga» · dom 7 jun 19h → reservar` |
| Instagram | Sticker historia / cover highlight | Sticker: `Reservar plaza` · Highlight: `DIRECTO` |
| LinkedIn | Featured / post | Título: `Directo: La voz que te juzga` · Desc.: `Domingo 7 jun, 19:00 (España). Gratuito, con registro. Reserva tu plaza.` |
| Facebook | Post / botón de página | `Reservar plaza — Directo «La voz que te juzga» (dom 7 jun, 19:00)` |
| YouTube | Comentario fijado / descripción | `Directo gratuito «La voz que te juzga» — domingo 7 jun, 19:00 (España). Reserva tu plaza:` |

**Universal corto** (cuando solo cabe una línea): `Directo gratuito · «La voz que te juzga» · dom 7 jun 19:00 — Reservar plaza`

**URL a difundir (VERIFICADA 19-may, panel + conector):**

```
https://preview.mailerlite.io/forms/2232121/187662502229706033/share
```

Esa es la **Compartir URL** oficial que MailerLite da para este formulario integrado (panel: Formularios → «Registro · Directo «La voz que te juzga» · 8 jun» → campo «Compartir URL»). Es la buena para redes; **se difunde tal cual**.

- Corrección de una nota previa errónea: en formularios *integrados* de MailerLite el dominio `preview.mailerlite.io/.../share` **ES** la página pública para compartir, no una vista previa del editor. No buscar otra URL «más pública»: no existe.
- El conector MCP devuelve `active:false` para este formulario: es una **pista falsa** en formularios integrados (no bloquea la Compartir URL). El panel es la fuente de verdad y muestra el formulario correcto, opt-in simple (double opt-in OFF) y grupo asignado.
- Grupo `187662493483533365` a 0 suscriptores hasta que alguien se registra: **esperado** (§9.4), no un fallo. Se llena al difundir.

**Portada del enlace en redes (1080×1080, generada 19-may 2026, sistema A1 verde):** [`portada-rrss-directo-la-voz-que-te-juzga.png`](../portada-rrss-directo-la-voz-que-te-juzga.png) (raíz del repo). Paleta y tipografía de marca (Instrument Serif + Barlow Condensed), sin emojis. Reto 7 días tiene su par A2 crema: [`portada-rrss-reto-7-dias-deja-de-buscarte.png`](../portada-rrss-reto-7-dias-deja-de-buscarte.png).

## 6 · Cómo encaja en el plan (no rompe Fase 1, la acelera)

- KPIs Fase 1 (`plan-captacion-verano-2026` §2): newsletter ≥120 y lista de espera taller ≥30 al 14 jun. Cada registro al directo entra al grupo y alimenta esos números.
- Métrica propia del directo: registros ≥ (objetivo realista a fijar por Daniel; suelo razonable para una cuenta de este tamaño: 30-60 registros).
- La grabación se recicla (pipeline `reciclaje-contenido-pipeline.md`) → entra en el embudo Cap III como evergreen durante meses.
- Compuerta: nada de Meta Ads hasta que el orgánico demuestre que el registro convierte (CEO §7 Decisión 2).

## 7 · Decisiones — CERRADAS el 18-may 2026

1. **Plataforma:** Google Meet · enlace `https://meet.google.com/fsu-scrz-res` · plan Flexible de pago (sin corte 60 min). ✅
2. **Opt-in:** simple (no doble). ✅
3. **Objetivo de registros:** 30-60 (suelo 30 = aceptable, 60 = bueno para una cuenta de este tamaño). ✅
4. **Formato:** pieza **única** (no recurrente), por defecto del repo hasta newsletter >1.000 + asistente (CEO §8). ✅
5. **Grabación post-directo:** sí se entrega a los registrados que no asistan (coherente con §1 «evergreen» y el mensaje de éxito §3.1). ✅

---

## 8 · Propuesta final cerrada · secuencia para inscritos (18-may)

> Patrón del repo (igual que Cap III): Code deja todo especificado y montado hasta donde la API permite; **Daniel da los clics finales de diseño/activación en el editor de MailerLite** (el render visual no se toca a ciegas por API). Tiempo estimado de Daniel: ~20 min.

### 8.1 · Calendario de envíos (qué recibe un inscrito)

> **Actualización 5 jun 2026 (vie 18:10 CEST)** · Daniel revisa el Outbox de MailerLite y aplica dos cambios:
>
> 1. **Excepción de idioma autorizada solo para el Recado 04.** El conector deja el `language_id` en `en-US` (solo afecta al bloque legal/pie automático que MailerLite inyecta · el contenido HTML va en español). Daniel autoriza expresamente esa excepción solo para el Recado 04 (campaña `189428295344850350`, sáb 6 jun 10:00 CEST).
> 2. **Cancelación de E2 y E4 por idioma sin autorizar.** Ambos estaban en inglés como el Recado 04, pero no entran en la excepción · pasan a `draft` con `is_stopped: true`:
>    - **E2 cancelado** (`189196741644388190` · stopped 18:02 CEST · era duplicidad con Recado 04 el sábado).
>    - **E4 cancelado** (`189196809348843111` · stopped 18:10 CEST · era el aviso «en una hora» del domingo 18:00).
>
> Para reactivar E4 el domingo · cambiar `language_id` a Español en panel (Configuración del email → idioma Español) y reprogramar para dom 7 jun 18:00 CEST.

| # | Cuándo | Estado real (5 jun 18:10 CEST) | ID | Idioma | Contenido |
|---|---|---|---|---|---|
| E1 | Inmediato al registrarse | `active` (automation) | `187662509833979144` paso 1 | n/a | «Estás dentro» (§3.2) |
| ~~E2~~ | ~~sáb 6 jun 19:00~~ | `draft` (`is_stopped: true`) | `189196741644388190` | `en` | ~~Recordatorio víspera + enlace Meet~~ |
| **Recado 04** | **sáb 6 jun 10:00** | `ready` (`scheduled`) | `189428295344850350` | `en` (excepción) | «Recordatorio · mañana domingo 19h» |
| E3 | dom 7 jun 10:00 | `ready` (`scheduled`) | `187809536941229345` | `es` | «Hoy a las 19:00 — el enlace para entrar» (§3.3) |
| ~~E4~~ | ~~dom 7 jun 18:00~~ | `draft` (`is_stopped: true`) | `189196809348843111` | `en` | «En una hora» |
| E5 | lun 9 jun ~10:00 | `draft` (pendiente programar tras directo) | `187809557833058027` | `es` | Gracias + Capítulo III + grabación |

**Resultado del calendario (los 11 inscritos reciben):**
- sáb 6 jun 10:00 · Recado 04 (víspera).
- dom 7 jun 10:00 · E3 día D.
- lun 9 jun ~10:00 · E5 (programar manualmente con URL de la grabación).

Opcional pero recomendado · si Daniel cambia el `language_id` del E4 a Español el domingo por la mañana y lo reprograma para 18:00 CEST, se recupera el aviso «en una hora» en español.

Enlace Meet a insertar como hipervínculo sobre el texto «Entrar aquí» (nunca pegar la URL cruda — regla `…cap3.md` §3): `https://meet.google.com/fsu-scrz-res`

### 8.2 · Copys nuevos (E2, E4, E5) — verbatim, voz «Te escribo»

**E2 · víspera (7 jun ~19:00) · asunto:** Mañana, 19:00 — te dejo ya el enlace
```
Hola,

Mañana domingo, a las 19:00 (hora de España), es el directo: una hora sobre la voz que te dice «no es suficiente».

Te dejo ya el enlace para no buscarlo a última hora: Entrar aquí.

Si mañana no puedes en directo, no pasa nada: a quienes os registrasteis os dejo después el material.

Nos vemos mañana.

— Daniel
```

**E4 · 8 jun ~18:00 · asunto:** En una hora
```
Hola,

En una hora, a las 19:00, empezamos. Una hora, sin prisa, sobre la voz que te juzga.

Entrar aquí.

— Daniel
```

**E5 · post-directo (9 jun ~10:00) · asunto:** Lo de ayer, por escrito
```
Hola,

Ayer estuvimos una hora con la voz que te juzga: de dónde sale, por qué no se calla con razones, y qué empieza a debilitarla.

Si quieres seguir, esto está escrito y ampliado en el Capítulo III, gratuito: Leerlo aquí.

Y si te lo perdiste en directo, aquí tienes la grabación: Verla aquí.

Te sigo escribiendo.

— Daniel
```
(E1 y E3 ya están redactados en §3.2 y §3.3.)

### 8.3 · Checklist de activación (clics de Daniel, ~20 min)

```
ORDEN ESTRICTO (override, ver §9.4): primero captación, DESPUÉS programar.
No se puede programar E2–E5 con el grupo vacío (MailerLite lo impide).

FASE A · abrir captación (ya):
[ ] Formulario 187662502229706033: opt-in SIMPLE + diseñar (campo email,
    paleta marca, titular y éxito de §3.1) + ACTIVAR.
[ ] Automation 187662509833979144: diseñar E1 + idioma ES + Prueba + ACTIVAR.
[ ] Crear/confirmar Meet (enlace fijo https://meet.google.com/fsu-scrz-res,
    plan Flexible = sin corte 60 min).
[ ] Pegar el enlace del FORMULARIO en los canales (§5.4) → el grupo empieza
    a llenarse.

FASE B · programar (SOLO con inscritos en el grupo, ~5-6 jun):
[ ] Campaña E2 al grupo 187662493483533365, programada sáb 7 jun 19:00.
[ ] Campaña E3 programada dom 7 jun 10:00.
[ ] Campaña E4 programada dom 7 jun 18:00.
[ ] Campaña E5 programada lun 9 jun 10:00 (revisar enlace de grabación tras grabar).
```

---

## 9 · Ejecución 18-may vía conector MailerLite · estado real + aprendizajes

> Sesión `claude/improve-proposal-quality-pq3d9`, 18-may 2026. Code ejecutó por el conector MCP lo que la API permite. Regla simétrica + inoculación de futuras sesiones contra las aristas del conector (precedente: `veredicto-…-15-may` §5).

### 9.1 · Hecho por Code (verificado)

- **E1** (automation `187662509833979144`, step 0): `update_automation_email` → asunto + texto en español cargados. Falta que Daniel lo «diseñe» y **Active** en el editor (no hay API para eso).
- **E2–E5**: campañas creadas en **borrador** con diseño de marca «Te escribo» (plantilla replicada de `contenido-rrss/te-escribo-newsletters/carta-02-la-voz-que-te-juzga.html`: kicker beige, H1 `#173D30`, footer CV11515 + twimproject.com + baja en español), remitente verificado `danielorozco@twimproject.com` / «Daniel Orozco - TWIM Project», **grupo `187662493483533365`** (Lead · Directo). IDs vigentes (los primeros se borraron, ver 9.2.2):
  - E2 `187809525929084347` · E3 `187809536941229345` · E4 `187809546704520781` · E5 `187809557833058027`

### 9.2 · Aristas del conector — NO repetir estos errores

1. **`create_campaign` nace en `language_id` en-US** y no hay endpoint para cambiar idioma. El bloque legal que MailerLite inyecta puede salir en inglés. Mitigación: footer propio en el HTML, en español. Arreglo definitivo **solo en panel** (Configuración del email → idioma Español). Verificar SIEMPRE el idioma antes de programar.
2. **`update_campaign` NO acepta `groups` y resetea el destinatario a `all_active_subscribers` (toda la lista).** Ocurrió: tras `update_campaign`, las 4 apuntaban a 51 (toda la base) en vez del grupo del Directo. Corregido borrando y recreando con `create_campaign` pasando `content` + `groups` **juntos**. Regla: nunca cambiar el contenido de una campaña con grupo vía `update_campaign`; recrear con `create_campaign(content, groups)` y verificar `filter` / `recipients_count` después.
3. **`update_form` solo cambia el nombre.** `double_optin` y el diseño visual del formulario no son API.
4. **No hay endpoint para activar una automation** (`enabled` false→true).

### 9.3 · Lo que queda en Daniel (lo que el conector no permite)

- 4 campañas: idioma → Español (panel). Diseño/copy/remitente/grupo ya correctos.
- Automation E1: diseñar email + idioma Español + **Activar**.
- Formulario: opt-in simple + diseñar + activar.
- Pegar enlace del formulario en canales (§5.4).
- **Programación de E2–E5 pendiente:** la hace Daniel en panel tras poner idioma, o avisa a Code y Code la programa por API **verificando el `scheduled_for` resultante** (hora de Madrid; riesgo de desfase si no se verifica).

### 9.4 · Orden inviolable: captación ANTES de programar (aprendido 18-may)

MailerLite **no deja programar ni enviar una campaña a un grupo con 0 destinatarios** (aviso: «por favor añadir más destinatarios»). El grupo `187662493483533365` está vacío hasta que alguien se registra. Por tanto el orden del checklist §8.3 es **estricto**:

1. **Primero abrir captación:** formulario (opt-in simple + diseño + **activar**) → automation E1 (diseñar + idioma ES + **Activar**) → **pegar el enlace del formulario en los canales** (§5.4).
2. La gente se registra y entra al grupo.
3. **Solo entonces** (idealmente 5-6 jun, con inscritos en el grupo) se programan E2–E5 (precabecera + «Enviar después» + fecha/hora §8.1).

E2–E5 quedan completas en **borrador** (diseño de marca, copy, remitente, grupo, idioma); lo único pendiente es el clic de programar, que **no es posible hasta que el grupo tenga inscritos**. Ninguna sesión futura debe intentar programarlas con el grupo vacío: es esperado, no un fallo.

### 9.5 · Estado del embudo al cierre del 18-may (activado)

Ejecutado en vivo con Daniel:

- **Formulario** `187662502229706033`: diseñado con paleta de marca (crema/verde/beige, Helvetica como fallback de Barlow), textos §3.1, reCAPTCHA y política de privacidad activados, **opt-in simple** (double opt-in OFF, es por-formulario, no afecta a otros), grupo correcto. **ACTIVO/publicado.** Compartir URL (verificada 19-may): `https://preview.mailerlite.io/forms/2232121/187662502229706033/share` — es la URL pública oficial, ver §5.5 (el `active:false` del conector es pista falsa en formularios integrados).
- **Automation E1** `187662509833979144`: email rediseñado de marca (kicker «TE ESCRIBO · DIRECTO», «Estás dentro.» en verde, Barlow Condensed, crema), idioma ES. **ACTIVA** (verificado en panel: estado «Activo»).
- **Pie global de cuenta**: limpiado del copy informal con emoji → «Recibes este correo porque te registraste en TWIM Project.» + «Darte de baja» (Configuración de la cuenta → Detalles de empresa). Pendiente de confirmar que Daniel guardó con las 3 casillas «Forzar la actualización» (afecta retroactivamente a Carta #2, automations y borradores).
- **Campañas E2–E5**: en borrador, diseño de marca, grupo correcto. Sin programar (Fase B, §9.4).

**Único pendiente de Daniel para captar:** difundir el Share URL del formulario en canales (§5.4). Sin difusión, la automation activa no recibe a nadie.

— Actualizado 18-may 2026: embudo del Directo montado y activado; solo falta difusión del enlace + programar E2–E5 en junio con inscritos.
