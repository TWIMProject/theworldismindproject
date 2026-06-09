# Google Ads · Cumplimiento y reactivación para TWIM Project

> Documento de referencia · 1 mayo 2026
> Cuando Daniel pregunte sobre Google Ads, reactivación de cuenta, políticas de salud mental en publicidad, o verificación de anunciante, abrir este documento.
> Complementa: política de privacidad (`privacy.html`), aviso legal y cookies.

> **⚠️ CORRECCIÓN 9 jun 2026 (verificada contra la política oficial de Google Ads):** este documento (1 may) afirmaba que un psicólogo necesita la certificación «Healthcare and Medicines» para anunciarse. **Es INCORRECTO para anuncios de Búsqueda de terapia/psicología en España.** Esa certificación es solo para **farmacias online, telemedicina que prescribe medicamentos, tratamiento de adicciones y medicamentos con receta**. Un psicólogo que da terapia (presencial/online, sin medicación) **NO necesita certificación**. El aviso «Health in personalized advertising» que aparece sobre las keywords es **informativo**: limita audiencias de **Display/remarketing**, NO la campaña de **Búsqueda**. Requisitos reales: copy veraz sin promesas de cura, colegiado CV11515 visible, política de privacidad RGPD con consentimiento en formularios. **Tratar como obsoletos** los puntos sobre certificación de salud del TL;DR, §1.1(b), §1.2 y §2.4. Fuente: `support.google.com/adspolicy/answer/176031`.

---

## TL;DR

- **Por qué Google pausó la cuenta anterior:** casi seguro por (a) verificación de anunciante incompleta, (b) categoría de salud mental restringida sin certificación, o (c) landing pages que no cumplen política de Google.
- **Para reactivar / poder volver a publicar:**
  1. Verificar anunciante (Advertiser Verification — proceso de Google de 3-5 semanas).
  2. Verificar dominio `twimproject.com` (1 día, vía DNS).
  3. Aplicar a certificación para profesionales de salud (no obligatoria pero muy recomendada).
  4. Reescribir landing pages para cumplir política de salud (disclaimers, fuentes, About).
  5. Reescribir anuncios para evitar lenguaje prohibido por política.
  6. Política de privacidad y cookies completas (ver `privacy.html` v2).
- **Coste de cumplimiento:** 0 € (solo tiempo de Daniel).
- **Tiempo estimado hasta poder anunciar:** 4-8 semanas desde el día que se inicia el proceso.

---

## 1 · Por qué Google pausa cuentas en categoría psicología

Google Ads tiene políticas más restrictivas para anuncios relacionados con **salud mental** que para casi cualquier otra categoría. Las tres causas más frecuentes de pausa o suspensión:

### 1.1 · Verificación de anunciante incompleta

Desde 2021, Google exige que **todos los anunciantes** completen *Advertiser Verification* (verificación de identidad del anunciante). Si no se completa en el plazo dado, la cuenta queda pausada.

Para profesionales individuales (psicólogos autónomos), Google pide:
- Documento de identidad (DNI o pasaporte).
- Documento que pruebe la titularidad de la cuenta (factura, certificado fiscal).
- En algunos casos, declaración jurada de identidad.

Tiempo de tramitación: 3-5 días una vez enviada la documentación.

### 1.2 · Falta de certificación para profesionales de salud

Google requiere certificación específica para anunciar servicios de salud (incluyendo psicología clínica). Sin esta certificación, los anuncios con palabras clínicas son rechazados sistemáticamente.

Esto se llama **Healthcare and Medicines certification** y se solicita desde la cuenta de Google Ads. Documentos típicos:
- Colegiación profesional (CV11515 en tu caso).
- Titulación universitaria.
- Habilitación como Psicólogo General Sanitario (Ministerio de Sanidad).

Tiempo de tramitación: 1-2 semanas.

### 1.3 · Landing pages que no cumplen política

Google revisa cada URL de destino y la rechaza si:
- No tiene **About / Quién soy** visible y verificable.
- No tiene política de privacidad enlazada en footer.
- No tiene aviso legal (LSSI-CE en España).
- Promete resultados clínicos imposibles o exagerados ("cura la ansiedad en 7 días", "garantizado").
- Usa testimonios de pacientes (prohibido en categoría salud).
- Tiene contenido que sugiere autodiagnóstico médico sin disclaimers.
- Tiene formularios que recogen datos sensibles sin justificación.

### 1.4 · Lenguaje prohibido en anuncios

Aunque la landing esté bien, Google rechaza anuncios que:
- Sugieren diagnóstico ("¿Tienes depresión? Click aquí").
- Apelan a vulnerabilidades emocionales explícitas ("¿Te sientes solo? Llámame").
- Mencionan medicamentos.
- Garantizan resultados clínicos.
- Usan superlativos médicos no avalados ("la mejor terapia").

---

## 2 · Plan de reactivación paso a paso

### 2.1 · Paso 1 — Auditoría de la cuenta actual (Día 1)

1. Entrar en `https://ads.google.com` con la cuenta pausada.
2. Ir a **Configuración → Resumen** → ver el motivo exacto de la pausa.
3. Captura/copia el motivo. Eso determina los pasos siguientes.

Posibles motivos típicos:
- *"Verificación de anunciante pendiente"* → ir a paso 2.2.
- *"Política de salud mental"* → ir a paso 2.3 + 2.4.
- *"Landing page no cumple política"* → ir a paso 2.5.
- *"Política de uso aceptable"* → revisar mensajes detallados, puede ser combinación.

### 2.2 · Paso 2 — Verificación de anunciante (Días 1-7)

1. En Google Ads, ir a **Configuración → Verificación del anunciante**.
2. Si pide *Identity Verification*: subir DNI escaneado.
3. Si pide *Business Operation Verification*: subir documento que pruebe que ejerces como Psicólogo General Sanitario en España (titulación + certificado de colegiación CV11515).
4. Si pide *Legal Entity Verification* (solo para sociedades): subir CIF + escritura de constitución.
5. Esperar email de Google (2-5 días).

### 2.3 · Paso 3 — Verificación de dominio (Día 1)

1. En Google Ads → **Configuración → Dominios verificados**.
2. Añadir `twimproject.com`.
3. Google da un código (TXT record o meta tag).
4. Añadir el código a tu dominio:
   - Si TXT record: ir a Netlify → Domains → DNS settings → añadir TXT record.
   - Si meta tag: añadir a `<head>` del `index.html`.
5. Verificar en Google Ads (botón "Verificar").
6. 1 hora típicamente.

### 2.4 · Paso 4 — Solicitud de certificación de salud (Días 7-21)

1. En Google Ads → **Soporte → Certificaciones → Healthcare**.
2. Aplicar a "Healthcare and Medicines certification" como **Health professional / Psychologist**.
3. Subir documentación:
   - Habilitación profesional como Psicólogo General Sanitario (Ministerio de Sanidad).
   - Certificado de colegiación CV11515 (Colegio Oficial Psicólogos Comunidad Valenciana).
   - Título universitario en Psicología.
   - DNI.
4. Esperar revisión manual de Google (1-3 semanas).
5. Si rechaza: solicitar revisión con info adicional.

> **Nota:** sin esta certificación, **puedes anunciar pero con keywords y wording muy limitados** ("psicólogo Valencia", "consulta psicología", "terapia online"). CON certificación: amplía drásticamente lo que puedes decir y los temas (dependencia emocional, ansiedad, burnout, etc.).

### 2.5 · Paso 5 — Reescribir landing pages (Días 1-7, en paralelo)

Cada landing que sea destino de anuncio debe cumplir checklist:

- [ ] **Footer con enlaces visibles** a: política de privacidad, aviso legal, cookies.
- [ ] **About / Quién soy** accesible (link en navegación o footer): nombre completo, CV11515, foto real, dirección de consulta.
- [ ] **Datos verificables**: dirección física Valencia, teléfono, email.
- [ ] **Disclaimer clínico** en landings de servicios: "Esta información es educativa, no sustituye consulta clínica. Para diagnóstico o tratamiento, agenda una consulta."
- [ ] **Sin testimonios de pacientes** (anonimizados en cita o caso sí, pero no "María dice que la terapia le cambió la vida").
- [ ] **Sin promesas de resultados** ("aprende a frenar la rumiación" sí; "cura tu ansiedad" no).
- [ ] **Sin medicamentos** mencionados (a menos que sea editorial / informativo en blog).
- [ ] **Schema.org** Person + ProfessionalService correctamente marcados.

Landings prioritarias para Google Ads:
- `/psicologo-dependencia-emocional-valencia.html`
- `/psicologo-burnout-valencia.html`
- `/psicologo-ansiedad-valencia/`
- `/psicologo-online.html`
- `/reto-7-dias.html`
- Landings de programas digitales (si vas a anunciarlos).

### 2.6 · Paso 6 — Reescribir anuncios (Días 7-14)

Cada anuncio debe pasar este filtro:

- [ ] No menciona diagnóstico médico ("¿Tienes ansiedad?" → mejor: "Información sobre ansiedad").
- [ ] No promete resultados ("Termina con tu burnout" → mejor: "Comprende y aborda tu burnout").
- [ ] No apela emocionalmente extremo ("¿Te sientes desesperado?" → fuera).
- [ ] No usa superlativos médicos sin aval ("la mejor terapia" → fuera).
- [ ] Es claramente educativo/informativo, no diagnóstico.
- [ ] Identifica claramente al anunciante (Daniel Orozco · CV11515 visible en algún lugar del anuncio o landing inmediatamente).

### 2.7 · Paso 7 — Resubir cuenta a revisión (Día 21+)

1. Una vez cumplidos pasos 2-6, en Google Ads → **Configuración → Estado de la cuenta** → solicitar revisión.
2. Tiempo de respuesta: 3-7 días.
3. Si aprueban: cuenta activa, puedes empezar campañas.
4. Si rechazan: motivo específico → iterar sobre el motivo.

---

## 3 · Política mínima de campañas a respetar

Cuando la cuenta esté activa, mantener disciplina:

### 3.1 · Estructura de cuenta limpia

- **1 campaña por objetivo** (no mezclar awareness + conversión en misma campaña).
- **1 ad group por tema clínico** (dependencia, burnout, ansiedad, autoexigencia, adolescencia).
- **2-3 anuncios por ad group** para test A/B.
- Conversion tracking configurado correctamente (envíos de formulario, suscripción a newsletter, click WhatsApp).

### 3.2 · Presupuestos iniciales

- Empezar conservador: **5-10 €/día por campaña** durante las primeras 4 semanas.
- Si el embudo convierte y CPL ≤ 4 €, subir a 15-25 €/día.
- Subir solo después de 50+ conversiones registradas (suficiente para optimizar).

### 3.3 · Geo y horario

- Geo: **Valencia + provincia** para servicios presenciales. **España** para online. **Hispanohablantes globales** solo si la landing está adaptada.
- Horario: lunes-viernes 8h-22h, sábados 9h-14h. Pausar madrugadas (CPL alto, baja calidad).

### 3.4 · Quality Score

- Apuntar a Quality Score ≥ 7/10 en cada keyword.
- Mejora con: relevancia anuncio-keyword-landing, CTR alto, landing rápida.
- Si Quality Score < 5 sostenido: pausar y rediseñar.

---

## 4 · Compatibilidad con Meta Ads (cuando esté en marcha)

Recordatorio: Daniel ya tiene Meta Ads en configuración (decisión 2 del doc CEO §8). Google Ads y Meta Ads se complementan así:

| Canal | Mejor para | Cuándo |
|---|---|---|
| **Meta Ads** | Descubrimiento, audiencias frías, awareness, lead generation | Mes 1-3 desde reactivación. Empezar aquí porque está más cerca de listo. |
| **Google Ads Search** | Intención alta, gente buscando "psicólogo Valencia" | Mes 3-6, una vez certificación de salud aprobada. |
| **Google Ads Display + YouTube** | Retargeting de visitantes, awareness en vídeo | Mes 6+. |

**No conviene activar ambos a la vez al inicio.** Meta primero, validar embudo, después añadir Google Search.

---

## 5 · Documentos legales requeridos por Google

Para que Google apruebe, las siguientes páginas deben existir y estar enlazadas en el footer de cada landing:

- [x] `privacy.html` — política de privacidad GDPR + LOPDGDD + cookies + Google + Meta + tracking. **Pendiente reescritura completa** (en curso).
- [ ] `aviso-legal.html` — requerido por LSSI-CE (Ley Servicios Sociedad Información). **No existe, hay que crear.**
- [ ] `cookies.html` o sección dentro de `privacy.html` — política específica de cookies con tabla. **No existe, hay que crear.**
- [ ] **Banner de consentimiento de cookies** (JS) que aparezca en primera visita y registre consentimiento. **No existe, hay que crear.**

---

## 6 · Decisiones a cerrar este mes

- [ ] **Acceso a la cuenta de Google Ads pausada** y captura del motivo exacto.
- [ ] **Documentación física preparada**: DNI escaneado + certificado de colegiación CV11515 + título universitario + habilitación PGS Ministerio Sanidad. Todo en PDF en una carpeta dedicada.
- [ ] **Verificación de anunciante** iniciada (paso 2.2).
- [ ] **Verificación de dominio** completada (paso 2.3) — 1 hora.
- [ ] **Solicitud de Healthcare certification** enviada (paso 2.4).
- [ ] **Auditoría de las 5 landings prioritarias** contra checklist 2.5.
- [ ] **Reescritura `privacy.html`** completada (en curso).
- [ ] **Creación `aviso-legal.html`** (pendiente).
- [ ] **Creación `cookies.html` + banner JS** (pendiente).
- [ ] **Linkado en footer** de todas las landings.

---

## 7 · Riesgos y mitigación

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Google rechaza certificación de salud | Media (10-30 %) | Alto | Tener documentación impecable. Si rechaza, solicitar revisión con info adicional o contactar partner Google con experiencia en salud. |
| Anuncios rechazados individualmente por wording | Alta (≥50 % al inicio) | Bajo | Iterar el wording. Tener lista de keywords prohibidas a mano. Cumplir checklist 2.6. |
| Landing rechazada después de cambios | Media | Medio | Auditoría exhaustiva antes de enviar a revisión. Probar primero con 1 landing antes de las 5. |
| Cuenta suspendida definitivamente | Baja si se cumplen pasos 2.1-2.6 | Muy alto | Si pasa, abrir cuenta nueva con estructura limpia y dominio verificado. |
| Daniel se cansa del proceso (4-8 semanas) | Media | Medio | Mantener checklist visible. Avanzar en bloques de 30 min. Resultado vale la pena. |

---

## Cierre

Google Ads es la cuarta palanca de captación pendiente de activar (junto con SEO + Newsletter + Meta Ads + YouTube/Podcast del stack). Su característica diferencial: **captura intención alta** — gente que está buscando explícitamente "psicólogo dependencia emocional Valencia" o "ayuda burnout". Eso es tráfico cualificado al máximo, pero requiere paciencia (4-8 semanas de cumplimiento) antes de poder activar.

Una vez activa, complementa Meta Ads (que captura descubrimiento). Los dos juntos son el motor de captación pagada de TWIM.

— Notas técnicas: documento generado el 1-05-2026. Si Google cambia políticas (ocurre 1-2 veces al año en categoría salud), revisar §1 y §2.4. Si la cuenta se reactiva sin necesidad de Healthcare certification, marcar §2.4 como opcional.
