# Newsletter «Te escribo» · Sistema de constancia y automatización · 10 jun 2026

> Regla declarada por Daniel el 10 jun 2026, verbatim (en CAPS en el original): «LA NEWSLETTER TIENE QUE SEGUIR SIEMPRE MANDANDO CARTAS A LOS SUSCRIPTORES AUNQUE YO NO TE LO DIGA. TIENE QUE HABER UNA CONSTANCIA EN LA CREACIÓN DE CONTENIDO VALIDO Y COHERENTE Y UNA AUTOMATIZACIÓN.»
>
> **Evolución de regla, no contradicción.** La línea roja previa (perfil §4: «su modelo es "cuando tengo algo que escribirte" · no prometer cadencia») se evoluciona, no se borra, con el patrón ya usado el 26 may (compuerta Meta Ads): la **promesa pública** al suscriptor sigue siendo sin cadencia («te escribo cuando algo merece tu tiempo» — es el gancho premium del re-encuadre del 4 jun). Lo que cambia es la **garantía interna del equipo**: el ritmo de producción ya no depende de que Daniel lo pida cada vez. El lector no nota promesa rota si una carta tarda 3 semanas; sí nota el silencio de 6.

## 1 · El mecanismo (quién hace qué, sin horas de Daniel)

1. **Ritmo interno garantizado: una carta cada ~2 semanas** (martes 19:00, el hueco que ya funciona — Cartas 1, 2 y 3 salieron/salen martes 19:00 con open 61-75 %).
2. **Claude redacta** cada carta en voz «Te escribo» destilando material propio ya existente (insights, podcast, banco de frases, carruseles) — nunca desde memoria genérica. Audit contra `contenido-rrss/te-escribo-newsletters/README.md` (mecanismo > etiqueta · origen > síntoma · sin positivismo · cierre sin presión).
3. **Claude la crea y la programa en MailerLite vía API** (language_id 8 = es-ES siempre · verificar `filter`/`recipients_count` tras crear · destinatarios: toda la lista activa, como Cartas 1-3).
4. **Ventana de veto de Daniel: 48 h.** Cada carta programada se avisa en chat y en el cierre de sesión con su preview URL. Si Daniel no dice nada, sale — eso es el «aunque yo no te lo diga». Si la veta o corrige, se ajusta antes del envío.
5. **Toda sesión nueva debe comprobar** (parte de leer el repo primero): ¿hay carta programada en los próximos 15 días? Si no, preparar y programar la siguiente de este calendario **sin esperar instrucción**.

## 2 · Calendario de cartas · H2 2026

| # | Fecha envío | Tema · fuente de reciclaje | Estado |
|---|---|---|---|
| 3 | **mar 16 jun 19:00** | «Necesitas que te miren para saber que vales» (hambre de mirada) · CTA lista espera Volver a Mí | **PROGRAMADA** (id 189878430782719669) · nota: retirado el bloque del directo del 7 jun (pasado) respecto al HTML del repo |
| 4 | mar 30 jun 19:00 | El cansancio que no se cura durmiendo · reciclar `te-escribo-cansancio-psiquico` + podcast E1 | Claude redacta semana del 22 jun |
| 5 | mar 14 jul 19:00 | Saberlo no te lo quita · reciclar `te-escribo-saberlo-no-te-lo-quita` | pendiente |
| 6 | mar 28 jul 19:00 | La autoexigencia (cierre ventana DDBEO) · reciclar podcast E6 | pendiente |
| 7 | mar 11 ago | (agosto: carta corta tipo «recado» · Daniel de vacaciones, cero implicación) | pendiente |
| 8+ | sep | Las cartas de septiembre arropan la pre-venta de Volver a Mí (3:1 valor/venta) | pendiente |

Los temas son propuesta editorial · Daniel puede reordenarlos con una línea. Lo inviolable es el ritmo, no el orden.

## 3 · Automatizaciones del ecosistema (estado real al 10 jun)

| Automation | Cubre | Estado |
|---|---|---|
| «Web - Newsletter Home» (Carta 1 D0 + Carta 2 D+10) | Bienvenida altas web · open 75 %/61 % | **Activa** · la «Bienvenida Te escribo» del plan x10 ya está cubierta por esta |
| «Reto 7 días» (17 pasos) · «Lectores Cap 3» (5 pasos) | Bienvenida por lead magnet | Activas |
| «Secuencia · Directo» + E2/E4 programadas | Embudo Directo 14 jun | Activa/programadas (10 jun) |
| **«Post-compra · Engranajes digital · reseña Amazon (D+7)»** · id 189878466140701979 | Circuito reseñas del libro | **CREADA 10 jun · INACTIVA** · Daniel: abrir panel, confirmar diseño del email y Activar (2-3 min) |

## 4 · Métricas del sistema (revisión quincenal, no diaria)

Open por carta ≥ 50 % (hoy 61-75 %) · bajas por carta < 1 % · y la de verdad: respuestas recibidas a las cartas (el canal es bidireccional por diseño). Si el open cae < 45 % dos cartas seguidas, revisar tema/asunto antes de revisar el ritmo.
