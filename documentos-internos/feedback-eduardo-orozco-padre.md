# Feedback Eduardo José Orozco Díaz · Padre · Psicoanalista (Valencia)

> Documento interno · 4 mayo 2026
> Eduardo José Orozco Díaz, padre de Daniel y psicoanalista referente en Valencia, revisa periódicamente el contenido de TWIM Project. Su feedback se registra aquí para mantener trazabilidad y aplicar revisiones de forma sistemática.

---

## Por qué este documento existe

Eduardo es:

- Psicoanalista con consulta privada en Valencia.
- Mentor clínico de Daniel desde el inicio de su carrera.
- Quien le ha facilitado parte del camino dentro de la consulta privada y la formación.

Su lectura del contenido de TWIM Project es **clínicamente autorizada** y, por tanto, su feedback es prioritario: corrige cosas que el lector clínico nota inmediatamente y que erosionan la credibilidad profesional del proyecto si no se atienden.

A partir de ahora, cada revisión suya se transcribe aquí, con la corrección, el archivo afectado, y el commit/PR que la aplica.

---

## Revisión #1 · 4 mayo 2026

### Lo que dijo (literal vía WhatsApp)

> Te digo dos o tres cosas a corregir bastante obvias.
>
> 1. En consulta privada desde 2012, no en consulta desde 2012 privada.
> 2. Si tuteas y personalizas, pon todo lo que (te) frena.
> 3. Trabajo (con, la, tu, u otra palabra que se te ocurra) ansiedad, depresión, etc.
> 4. No te comas artículos: Para frenar (la) urgencia.
> 5. Motivación, apatía e (in)decisión.
>
> Entre paréntesis va lo que yo agregaría en las frases.

### Acciones aplicadas

| # | Corrección | Aplicada en | Commit |
|---|---|---|---|
| 1 | "consulta desde 2012 privada" → "consulta privada desde 2012" + cred badge "En consulta desde 2012" → "En consulta privada desde 2012" en 4 landings | `index.html`, `daniel-orozco-abia.html`, `psicologo-burnout-valencia.html`, `psicologo-dependencia-emocional-valencia.html`, `terapia-pareja-valencia.html` | 4 may 2026 |
| 1 bis | Meta description: "Trabajando desde 2012 ansiedad..." → "En consulta privada desde 2012 trabajando con ansiedad..." | `daniel-orozco-abia.html` | 4 may 2026 |
| 4 | "para frenar urgencia mental" → "para frenar la urgencia mental" | `index.html`, `soluciones/index.html` | 4 may 2026 |
| 5 | "Motivación, apatía académica y decisión vocacional" → "Motivación, apatía académica e indecisión vocacional" | `index.html` | 4 may 2026 |

### Acción pendiente

| # | Corrección | Estado | Próximo paso |
|---|---|---|---|
| 2 | "Si tuteas y personalizas, pon todo lo que (te) frena" — auditar landings donde tuteas, asegurar que las frases incluyan el `te` cuando corresponda | ⏳ pendiente | Auditoría página por página (1-2 horas en sesión dedicada) |
| 3 | "Trabajo (con, la, tu, u otra palabra que se te ocurra) ansiedad, depresión..." — verificar caso por caso si ya se aplican preposiciones correctamente | 🔍 verificación parcial: la mayoría de menciones ya llevan "Trabajo CON ansiedad..." o "Trabajo LA ansiedad..." | Repaso editorial completo en sesión dedicada |

---

## Observación estratégica de Eduardo (4 mayo 2026)

> *"Él piensa que ofrezco demasiado siendo que estoy yo solo."*

Esto **no es un fix de copy** — es una crítica estratégica de fondo sobre el catálogo de TWIM Project. Eduardo señala que la oferta es excesivamente amplia para una persona que opera sola.

### Inventario actual del catálogo (al 4 mayo 2026)

- Consulta privada presencial Valencia
- Consulta online (hispanohablantes)
- 7 landings SEO de servicios
- 3 programas digitales (*Deja de Buscarte en Otros*, *Rompe el TENGO QUE*, *Deja de Obligarte*)
- 3 talleres (TDAH adolescentes, bachillerato motivación, "No puedo parar")
- Newsletter "Te escribo"
- Libro *Los engranajes de la mente* (Amazon)
- Método MindShift / In-Company (B2B)
- TWIM Podcast · Psicología Aplicada (4 episodios)
- Los Invitados · TWIM Podcast (15 episodios)
- YouTube @daniorozcopsicologo (10,1K subs)
- Instagram @daniorozcopsicologo
- LinkedIn
- X @DaniOrozcoPsico
- TWIM Clinic (modelo derivación supervisada con Sergio · en setup)

**Eduardo tiene razón clínicamente.** Para una marca de "Psicólogo individual con CV11515 en consulta desde 2012", esto **suena a sobrecarga**. El visitante puede pensar: ¿realmente atiende todo esto bien? ¿O es marketing?

### Cómo se conecta con decisiones ya tomadas

Esta crítica encaja con la **Decisión 1 del doc CEO §7** (consolidado v2 al 1 mayo): *Concentración o expansión de embudos*. Decisión cocida: **Camino A — Concentración**, con apoyo de:

- Stack producción audio+vídeo (NotebookLM + ElevenLabs) → libera tiempo Daniel.
- TWIM Clinic con Sergio → Daniel deja de ser el único atendiendo.
- VA en junio (palanca #5 del doc CEO §6.3).

Pero la observación de Eduardo añade un matiz: **no basta con consolidar internamente — hay que reducir la apariencia de sobre-oferta de cara al lector**. Mientras Sergio o la VA no estén operativos, lo que el visitante ve es "Daniel solo ofreciendo 15 cosas".

### Acciones derivadas (a tratar en sesión dedicada con calma)

- [ ] **Auditar la home y el menú principal de twimproject.com.** Identificar las ofertas que conviene **ocultar/desindexar/posponer** mientras no haya equipo — sin perder lo que ya está produciendo.
- [ ] **Decidir qué se pausa y qué se queda visible**:
  - Programas digitales: ¿solo el *Deja de Buscarte en Otros* hasta que el segundo esté validado?
  - Talleres adolescencia: ¿esperar a que Sergio entre como principal antes de comunicarlos abiertamente?
  - Método MindShift / In-Company: ¿quitar de la home hasta que haya pipeline real?
- [ ] **Reorganizar la home** para que la primera impresión sea: *"Psicólogo en consulta + autor + newsletter"*, no un catálogo.
- [ ] **Revisar con Eduardo** la versión consolidada antes de publicarla.

> **No urgente.** Esto requiere sesión dedicada, decisiones de Daniel sobre qué seguir vendiendo activamente y qué pasar a "modo silencioso", y posiblemente conversación con Eduardo. Reservar 90 min en agenda — no improvisar.

---

## Cómo procesar futuras revisiones de Eduardo

1. **Transcribir literal** lo que diga (WhatsApp / nota de voz / lo que sea).
2. Crear nueva sección `## Revisión #N · [fecha]` en este documento.
3. Aplicar las correcciones de copy que sean obvias **inmediatamente** y registrarlas.
4. Las observaciones estratégicas (como la de "ofreces demasiado") **no se aplican como parche** — se documentan, se conectan con decisiones del doc CEO, y se reservan para sesión dedicada.
5. Commit + PR cada vez. Daniel revisa y aprueba.
6. Ofrecer a Eduardo, cuando proceda, una versión consolidada antes de publicar cambios mayores.

---

**Última actualización:** 4 mayo 2026 — Revisión #1 aplicada.
