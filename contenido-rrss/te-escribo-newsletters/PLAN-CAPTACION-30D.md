# Te escribo · Plan de captación 30 días

> Objetivo: 200 suscriptoras netas en mes 1 al grupo `Web - Newsletter Home` (ID `185936045160793620`). Automation de bienvenida ID `185842047616288664`.
> Punto de partida: 30 abril 2026.
> Estrategia: orgánico-primero. Meta ads como gate condicional en semana 4 si el ritmo orgánico no llega al objetivo.

---

## 1 · Estado del funnel tras esta tanda

### Implementado en código (esta rama)

- **Cross-sell "Te escribo" en 7 landings SEO** que antes no captaban. Cada bloque tiene una *subhead psicoanalítica* específica del síntoma de la página, no copy genérico.

  | Landing | Subhead (impulso) |
  |---|---|
  | `psicologo-burnout-valencia.html` | Lo que llaman cansancio es otra cosa, y lleva años pidiendo ser nombrada. |
  | `psicologo-ansiedad-valencia/` | Lo que no se calma a las 3 de la mañana no se calma con respiraciones. |
  | `psicologo-adolescentes-valencia.html` | Lo que tu hija o tu hijo no te cuenta no es porque no quiera. Es porque todavía no tiene palabras. |
  | `psicologo-dependencia-emocional-valencia.html` | Eso que llamas amor cuando te vacía es otra cosa. Y la has aprendido. |
  | `terapia-pareja-valencia.html` | Casi nada de lo que se repite en pareja empezó en la pareja. |
  | `psicologo-online.html` | Si esto que llevas tiempo sintiendo se hubiera resuelto solo, ya estaría resuelto. |
  | `soluciones/index.html` | Si has llegado hasta aquí buscando, algo dentro lleva tiempo pidiéndolo. |

  Bloque: dark-green box, kicker "Te escribo", H2 con la subhead, sub-explicación ("Una carta cada tanto, escrita por mí. Sobre la mente, el cansancio y lo que no se dice. No es coaching. No es positividad. Es leer la propia historia."), input email + botón "Quiero recibirlas". Sin campo nombre — fricción mínima en frío.

  POST → `/.netlify/functions/subscribe` con `group: 'newsletter-home'`. Misma automation MailerLite Web - Newsletter Home dispara la bienvenida.

- **Exit-intent modal** (`assets/te-escribo-exit-intent.js`) cargado en las 7 landings SEO. Trigger: mouse-leave hacia la barra del navegador (desktop) o 35 s en página (touch). 1× por sesión (sessionStorage `twim_te_seen`). NO se dispara en `/`, `/index.html` ni `/newsletter/`. Copy modal: "Antes de irte: lo que has venido a buscar a lo mejor está aquí." Mismo backend que el bloque cross-sell.

- **GA4 events**: `newsletter_signup` (con `source: 'cross_sell_seo' | 'exit_intent'` + `landing: location.pathname`) y `newsletter_modal_shown`. Permite calibrar ratios CPL → suscriptora real.

### Ya en producción de antes

- Form newsletter en `index.html` (hero) y `/newsletter/index.html` (fullscreen).
- Lead magnets activos: `lead-burnout-5-senales.html`, `test-sindrome-impostora.html`, `reto-7-dias.html`. Capturan a grupos propios (no a "Newsletter Home").
- Automation MailerLite "Web - Newsletter Home" enabled.
- Carta #1 ("esto es lo que vas a recibir") programada como campaña ML para 5 mayo 19:00 CET.
- Carrusel #1 "cansancio psíquico" programado IG/LinkedIn 5 mayo 19:00 CET.

---

## 2 · Calendario semanal

### Semana 1 · 30 abril – 6 mayo · CIERRE DEL COLADOR

- ✅ Cross-sell + exit-intent en 7 landings (esta rama). Merge → en cuanto Netlify haga deploy preview verde.
- ✅ Carta #1 sale 5 mayo 19:00 CET (ya programada).
- ✅ Carrusel #1 IG/LinkedIn 5 mayo 19:00 CET (ya programado).
- ⏳ **Manual ML (Daniel):** verificar que la automation "Web - Newsletter Home" tiene como Carta #1 la versión definitiva (no la versión draft). Pasos: dashboard ML → automations → Web - Newsletter Home → revisar email 1.

### Semana 2 · 7 – 13 mayo · AMPLIFICACIÓN

- ✅ **Carrusel #2 «Saberlo no te lo quita»** publicado **martes 12 mayo 2026** (mismo ritual que Carrusel #1). Distribución multicanal completa:
  - X (publicado manual ~12:30 CEST): `https://x.com/DaniOrozcoPsico/status/2054126914877407275`
  - Threads (publicado manual ~12:30 CEST, formato condensado 2 posts)
  - Instagram + Facebook (programados 19:00 CEST vía Meta Business Suite, ambos como carrusel 7 slides)
  - LinkedIn (programado 19:00 CEST, formato PDF con título «Saberlo no te lo quita. Aunque a veces lo creas.»)
  - Story IG Recado 01 «Antes de ponerle nombre» (subida manual ~14:30 CEST, con sticker link a `/newsletter/`)
- ✅ **Carta #2 "La voz que te juzga"** programada vía MCP MailerLite (ID `186162435789423797`) para martes **19 mayo 2026 19:00 CEST** (status `ready`). Audiencia: Newsletter Home + Reto + Lead Magnet Dependencia + Lista General. HTML editorial conservado en `contenido-rrss/te-escribo-newsletters/carta-02-la-voz-que-te-juzga.html`.

### Semana 3 · 14 – 20 mayo · UPSELL LEAD MAGNETS

- **Manual ML (Daniel):** añadir P.S. de upsell a la **welcome email de cada lead magnet**. La idea: quien descarga el material extra de burnout / test impostora / reto 7 días es alta intención; la mayoría debería terminar también en "Te escribo". Texto sugerido para añadir al final de las 3 welcome emails:

  > P.D. — Si esto te ha resonado, escribo cada tanto cartas más largas en *Te escribo* (sobre la mente, el cansancio y lo que no se dice). [Apuntarte aquí](https://twimproject.com/newsletter/) — sin spam, te das de baja cuando quieras.

  Automations a tocar:
  - `Secuencia Anti-Test Dependencia Emocional` (ID `183366876869428872`) — añadir P.D. al email de bienvenida.
  - Lead Magnet Burnout (cuando exista la automation, hoy sólo está la lista).
  - Lead Magnet Síndrome Impostora (cuando exista la automation).

- **Social proof on-site:** cuando crucemos 50 suscriptoras visibles, añadir "Únete a [N] mujeres que…" a los 3 forms (home, /newsletter/, los 7 landings cross-sell). Antes no — queda ridículo.

### Semana 4 · 21 – 27 mayo · GATE META ADS

Si a 21 mayo el contador del grupo `newsletter-home` en MailerLite es:
- ≥ 150 suscriptoras → quedamos 100 % orgánico, no hace falta Meta.
- 100-149 → activamos Meta a 5 €/día × 5 días (25 € test).
- < 100 → activamos Meta a 5 €/día × 7 días (35 € test).

Brief Meta detallado: § 4.

---

## 3 · Lo que sí queda manual

| Tarea | Sistema | Quién |
|---|---|---|
| ✅ Programar Carta #2 (D+14 desde Carta #1, martes 19 mayo 19:00 CEST) | MailerLite (vía MCP) | Auto |
| Verificar email 1 de la automation Web-Newsletter-Home (que sea la versión final, no draft) | MailerLite dashboard | Daniel |
| Añadir P.D. de upsell a las 3 welcome emails de lead magnets | MailerLite dashboard | Daniel |
| Publicar Carrusel #2 IG/LinkedIn semana 2 | Manual social | Daniel |
| Activar 2 automations talleres TDAH/Bach (pendiente desde antes) | MailerLite dashboard | Daniel |
| Verificar contador grupo newsletter-home el 21 mayo | MailerLite dashboard | Daniel |

---

## 4 · Brief Meta Ads · semana 4 · gate condicional

> Sólo se activa si el contador a 21 mayo está por debajo de 150 (ver § 2). Presupuesto máximo: 35 €. Métrica de corte: CPL > 2 € → cortar antes de gastar todo.

### 4.1 · Audiencia

- **Geo:** España. Si CPL bajo, ampliar a hispanohablantes América Latina (México, Argentina, Colombia, Chile) en una segunda creative split.
- **Demo:** mujeres 28-45.
- **Intereses:** psicología, mindfulness, autoconocimiento, terapia, *burnout*, ansiedad, libros de Brené Brown, Lori Gottlieb, Massimo Recalcati, Marian Rojas, *Mindfulness*. NO usar intereses puramente comerciales tipo "marketing femenino".
- **Excluir:** ya suscriptoras (custom audience: lista MailerLite "Newsletter Home") + ya pacientes (lista contacto). Esto evita gastar en gente ya convertida.
- **Lookalike:** una vez tengamos ≥ 100 suscriptoras, generar LAL 1 % España sobre la lista Newsletter Home y testar contra la audiencia de intereses.

### 4.2 · Creative principal · variante A (la psicoanalítica directa)

**Formato:** carrusel 4 slides, 1080 × 1350.

**Origen:** reciclar slides 2, 3 y 4 del carrusel "cansancio psíquico" (`contenido-rrss/te-escribo-cansancio-psiquico/slide-02.png` … `slide-04.png`) + cierre nuevo con CTA.

- **Slide 1 (gancho):** "duermo bien pero me levanto cansada" (frase de paciente real, ya producida en slide 02).
- **Slide 2 (giro):** "El cuerpo se recupera con horas. La psique se recupera con honestidad." (slide 04).
- **Slide 3 (nombrar):** "Reprimir cansa más que correr. Sostener una imagen cansa más que cargar peso." (slide 03).
- **Slide 4 (CTA — slide nueva, fondo verde oscuro #173D30, beige #C2A78B en H1):**
  - Kicker (beige, mayúsculas, letter-spacing 3): TE ESCRIBO
  - H1 (cream): "Te lo escribo despacio, una carta cada tanto."
  - Body (cream 80 %): "Sobre la mente, el cansancio y lo que no se dice. No es coaching. No es positividad. Es leer la propia historia."
  - Footer: "twimproject.com/newsletter"

**Caption (lo que va arriba del carrusel en el ad):**

> Si te dicen que descanses más y no funciona, no es que descanses mal.
>
> Lo que llaman cansancio casi nunca es físico. Es lo que el cuerpo sostiene cuando la psique no puede dejar de obedecer.
>
> Escribo una carta cada tanto sobre esto — sobre la mente, el cansancio y lo que no se dice. Sin coaching, sin positividad. Para leer despacio.
>
> Si quieres recibirla → twimproject.com/newsletter
>
> — Daniel Orozco · Psicólogo CV11515

**CTA del botón Meta:** *Saber más* (NO *Suscribirse*: rompe la promesa de carta editorial).

**URL destino:** `https://twimproject.com/newsletter/?utm_source=meta&utm_medium=cpc&utm_campaign=te-escribo-cansancio-w4&utm_content=carrusel-a`

### 4.3 · Creative · variante B (la pregunta directa, formato reel)

**Formato:** reel vertical 9:16, 8-12 s, sin voz (caption sobre fondo verde oscuro con tipografía Barlow Condensed grande).

Texto en pantalla (3 cards consecutivas, ~3 s cada una):
1. *Has dormido 8 horas.*
2. *Sigues cansada.*
3. *Saber por qué cambia todo.*

End-card: logo TWIM + "Te escribo · twimproject.com/newsletter".

Caption del reel: igual que 4.2.
URL destino: igual que 4.2 con `utm_content=reel-b`.

### 4.4 · KPIs y stop-loss

- **Métrica primaria:** Cost per Lead (CPL = €gastados / suscripciones a `newsletter-home`).
- **Cota objetivo:** CPL ≤ 1.50 € en España, ≤ 0.80 € si ampliamos a LatAm.
- **Stop-loss:** si tras 15 € gastados el CPL > 3 €, pausar la creative y rotar a la otra variante. Si las dos > 3 €, parar el test entero — el problema es de copy/promesa, no de pujas.
- **Métricas secundarias:** CTR > 1.5 %, time on `/newsletter/` > 30 s, scroll depth > 50 %.

### 4.5 · Setup técnico

- Píxel Meta ya cargado en site (verificar).
- Conversion event "Lead" disparado por el evento GA4 `newsletter_signup` ya implementado en cross-sell + exit-intent. Si falta cablear el píxel a este evento, **Daniel me lo dice y lo cablo en el JS** (5 min).
- UTMs ya definidos en 4.2 / 4.3 — GA4 los recoge automáticamente.

---

## 5 · Métricas de seguimiento (revisar lunes y jueves)

| Métrica | Fuente | Cota saludable |
|---|---|---|
| Suscriptoras netas semanales (grupo Newsletter Home) | MailerLite | ≥ 50 |
| Conversión visitante → suscriptora landings SEO | GA4 (sessions vs newsletter_signup con source=cross_sell_seo) | ≥ 1.5 % |
| Conversión exit-intent | GA4 (newsletter_modal_shown vs newsletter_signup con source=exit_intent) | ≥ 8 % de los que ven el modal |
| Open rate Carta #1 | MailerLite | ≥ 35 % |
| Click rate Carta #1 → /newsletter | MailerLite | ≥ 5 % |
| Unsubscribe rate Carta #1 | MailerLite | < 1 % |

---

## 6 · Log de acciones manuales fuera del calendario

> Regla simétrica CLAUDE.md: cada publicación manual se registra el mismo día.

### 12 mayo 2026 (martes) — Tanda multicanal Carrusel #2 + Recado 01 story

| Hora | Canal | Pieza | URL | Estado |
|---|---|---|---|---|
| ~12:30 CEST | X / Twitter | Hilo «Saberlo no te lo quita» (7 tweets + PD, slide-01 adjunto al Tweet 1) | `https://x.com/DaniOrozcoPsico/status/2054126914877407275` | ✅ Publicado |
| ~12:30 CEST | Threads | Hilo condensado 2 posts (cierre del carrusel + PD newsletter) | URL pendiente de capturar | ✅ Publicado |
| ~14:30 CEST | Instagram Story | Story Recado 01 «Antes de ponerle nombre» con sticker link a `/newsletter/` | Stories sin URL pública (caducan 24h) | ✅ Publicado |
| 19:00 CEST | Instagram | Carrusel 7 slides + caption editorial | Pendiente publicación automática | 🟡 Programado vía Meta Business Suite |
| 19:00 CEST | Facebook | Carrusel 7 slides + caption editorial | Pendiente publicación automática | 🟡 Programado vía Meta Business Suite |
| 19:00 CEST | LinkedIn | PDF carrusel «Saberlo no te lo quita. Aunque a veces lo creas.» | Pendiente publicación automática | 🟡 Programado nativo LinkedIn |

**Notas de la tanda:**

- Carrusel #2 mantiene horario 19:00 CEST por **comparabilidad con Carrusel #1** (mismo control horario para poder leer diferencias de engagement). Decisión documentada: probar 20:00 CEST en Carrusel #3 (pico de actividad declarado por Meta para esta audiencia).
- Hilo X publicado a las 12:30 fuera del ritual de 19:00 — decisión operativa de Daniel para tener engagement directo en la primera hora.
- Threads se incorpora como canal nuevo (no estaba en el calendario documentado de `x-twitter-estrategia-canal.md`).
- Recado 01 story sale con corrección temporal de última hora (atribución «envié hoy» → «envié ayer» + footer; marca de agua MindWorld añadida). Commit `87a1ffa`.

**Métricas a 24 h del Carrusel #2 (capturadas 13 may ~10:00 CEST):**

| Canal | Visualizaciones | Alcance | Save rate | Share rate | Likes | Comentarios | Follows |
|---|---|---|---|---|---|---|---|
| Instagram | 1.207 | 625 | 0,41 % (5/1.207) | 0,17 % (2/1.207) | 12 | 0 | 0 |
| Facebook | 3 | 3 | 0 | 33 % (1/3) | 0 | 0 | 0 |

- Save rate IG **5× por debajo** del benchmark mes 3 declarado (`instagram-sistema-visual-marca.md §13.1`: ≥2 %).
- Share rate IG **6× por debajo** del benchmark mes 3 (≥1 %).
- Audiencia IG sesgada a 81,6 % mujeres (vs 60,1 % baseline orgánico del 12 may), franja 35-44 dominante (35 %).
- FB con 3 views = sospecha de fallo técnico de cross-post, no bajo rendimiento orgánico.
- Análisis completo, causas y plan de mejora para Carrusel #3 en `documentos-internos/metricas-carrusel-2-saberlo-12-may-2026.md`.
- Revisión final a 7 días: 19 may ~10:00 CEST (rellenar §7 del doc anterior).

### 11 mayo 2026 (lunes) — Recado 01 enviado vía MailerLite

Ver `REACCION-9-MAYO.md` y commit `6646711` (log del envío urgente del Recado 01 a las 22:04 CEST).

---

## 7 · Baseline de audiencia IG (capturado 12 may 2026)

> Datos extraídos del panel Audiencia de Instagram Insights de @daniorozcopsico. Primera medición documentada en el repo. Detalle completo en `documentos-internos/metricas-audiencia-ig-baseline-12-may-2026.md`.

- **Sexo:** Mujeres 60,1 % · Hombres 39,9 % (audiencia más mixta de lo previsto: el promote del 9 may sesgó al 89% mujeres por el creativo)
- **Edad dominante:** 25-34 (38 %) · 35-44 (24,7 %) · 45-54 (17,7 %) · 55-64 (8,9 %). Cohorte 25-44 concentra 62,7 %.
- **Top ciudades:** Madrid 5,4 % · Barcelona 2,9 % · Valencia 1,6 % · Sevilla 1,4 %. Cuatro picos suman solo 11,3 % → alcance disperso fuera de grandes capitales.
- **Hora pico declarada por Meta esta semana:** 20:00 CEST. Hipótesis para test deliberado en Carrusel #3.

**Implicaciones para el plan:**
- Audiencia más joven y mixta de lo asumido → no caricaturizar copy hacia «mujer 45 con dependencia». Mantener voz editorial transversal.
- El pico 20:00 está a 1h de la ventana 19:00 actual: la diferencia es marginal pero medible. Carrusel #3 servirá para validar empíricamente.
