# Política de booking de consulta clínica · Daniel Orozco

> Documento interno · 4 mayo 2026
> Decisión sobre cómo se gestiona el primer contacto para consulta clínica privada de Daniel.

---

## Decisión

**No se usa Cal.com (ni ningún sistema de booking automático) para la consulta clínica privada de Daniel.**

La agenda clínica se gestiona **manualmente y caso a caso**, con conversación previa por email/DM/teléfono.

---

## Por qué

### Razón clínica

- **Pacientes fijos** tienen slot semanal estable que forma parte del encuadre terapéutico. Forzar Cal.com para encajar paciente nuevo automatizado rompe el slot del fijo.
- **Pacientes variables** (turnos laborales rotativos, etc.) cuadran semana a semana en conversación. No es trabajo logístico, es coordinación clínica con información subjetiva del paciente.
- **Filtro de entrada de paciente nuevo:** que escriba primero da información clínica antes de la primera sesión. Si reserva sin escribir, Daniel llega ciego.

### Razón estratégica

- TWIM Project nace para **proyecto editorial** (grupos, talleres, libros, podcast, formación), no para escalar la consulta privada de Daniel.
- La consulta privada es la **base sólida que financia todo lo demás** (consulta presencial Valencia + online), pero NO es el motor de crecimiento.
- Modelo de referencia: Recalcati, Anabel González, Lori Gottlieb. Clínica restringida + obra editorial expansiva. La consulta queda como pieza de prestigio limitada.

---

## Política aplicada en la web

### CTA en landings SEO (header + hero)

Sustituido en las landings (4 may 2026):

- ❌ Antes: `Reservar consulta`, `Reservar primera consulta`, `Reservar primera sesión`, `Reservar primera entrevista` (variaba por página).
- ✅ Ahora: **`Escribir para empezar`** (estándar único en todos los CTAs, header + hero).

### Headings (h2) de sección final

- ❌ Antes: `Reservar primera consulta para tratar tu [X]`.
- ✅ Ahora: `Empezar tu proceso para tratar tu [X]` / `Empezar terapia de pareja` / `Empezar primera sesión online`.

### Mailto subject (no estándar único — se mantienen variantes contextuales)

Cada landing tiene su subject específico para que Daniel identifique de dónde viene el email. Estandarizados:

| Landing | Subject |
|---|---|
| `daniel-orozco-abia.html` (×2 botones) | `Primera consulta en Valencia` |
| `psicologo-burnout-valencia.html` | `Consulta burnout Valencia` (hero) y `Primera consulta en Valencia` (header) |
| `psicologo-dependencia-emocional-valencia.html` | `Consulta dependencia emocional Valencia` (hero) y `Primera consulta en Valencia` (header) |
| `psicologo-adolescentes-valencia.html` | `Consulta adolescente Valencia` (hero) y `Primera consulta en Valencia` (header) |
| `psicologo-online.html` | `Terapia online en español` (hero, CTA banner) y `Primera consulta online` (header) — sin "Valencia" porque es online global |
| `terapia-pareja-valencia.html` | `Terapia pareja Valencia` (hero) y `Primera consulta en Valencia` (header) |

### Archivos afectados

- `psicologo-adolescentes-valencia.html` — header + hero + CTA banner
- `psicologo-burnout-valencia.html` — header + hero + h2 + CTA banner
- `psicologo-dependencia-emocional-valencia.html` — header + hero + h2 + CTA banner
- `psicologo-online.html` — header (subject específico online) + hero + h2
- `terapia-pareja-valencia.html` — header + hero + h2 + CTA banner
- `daniel-orozco-abia.html` — header + hero + CTA banner (3 ocurrencias homogeneizadas)
- `index.html` — ya tenía `Pedir cita` (mantenido)
- `insights/_template-insight.html` — ya tenía `Pedir cita` (mantenido)

---

## Dónde Cal.com SÍ se usa (sin tocar consulta privada)

| Uso | Estado | Notas |
|---|---|---|
| **Talleres adolescencia** — entrevista informativa post-pago | ✅ Activo | URL: `cal.com/daniel-orozco/entrevista-informativa`. Enchufado en `talleres/gracias-reserva.html`. |
| **TWIM Clinic con Sergio cuando entre** | ⏳ Pendiente | Sergio probablemente sí quiere agenda estandarizada para sus derivados. Decisión suya, no afecta a Daniel. |
| **Sesión exploratoria 30 min con paciente nuevo (futuro)** | ❌ No activo | Solo si Daniel decide algún día abrir esa ventana específica. No prioritario. |

---

## Lo que se le dice al usuario que llega buscando consulta

El usuario que clica "Escribir para empezar" → se abre su email con asunto preestablecido. Daniel responde personalmente con conversación clínica de entrada. Eso filtra y construye relación desde antes de la primera sesión.

Si en algún momento Daniel quiere reforzar la transparencia, conviene añadir en alguna sección de la home o de `daniel-orozco-abia.html` una línea como:

> *"Mi agenda es manual y se cuadra caso a caso por email. Escríbeme contándome brevemente lo que te trae y te respondo personalmente."*

(No urgente, pero coherente con el modelo declarado aquí.)

---

## Conexión con otros docs

Esta decisión se alinea con:

- **Doc CEO v2 §2 (Cultura TWIM):** anti-coaching, voz clínica, "Daniel-clínico no Daniel-influencer".
- **Doc CEO v2 §7 Decisión 1:** Camino A — Concentración (no expandir oferta).
- **Feedback Eduardo Orozco padre (4 may):** observación "ofreces demasiado siendo que estás solo" — esta política reduce apariencia de sobre-oferta sin tocar lo que ya funciona.
- **Doc TWIM Clinic:** la red supervisada con Sergio es lo que escala la atención clínica, no Cal.com en la cuenta de Daniel.

---

## Cuándo revisar esta política

- Si en 12-18 meses la cartera de pacientes cambia drásticamente (ej. menos pacientes fijos por traspaso a Sergio, más demanda de exploratorias).
- Si Daniel decide abrir una ventana de "sesión exploratoria 30 min" como filtro de entrada a precio reducido.
- Si entra una VA que pueda gestionar la primera coordinación y entonces tenga sentido un sistema híbrido.

Mientras tanto, la política se mantiene: **clínica artesanal, NO automatizada**.

---

**Última actualización:** 4 mayo 2026 · decisión aplicada en código.
