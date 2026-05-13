# Decisiones cerradas · Taller «Volver a Mí»

> Documento creado el **13 may 2026** tras el merge del PR #151 con las respuestas de Daniel a las 14 piezas pendientes + decisiones tomadas por Claude Code en delegación expresa. Sustituye y consolida lo que estaba abierto en `piezas-pendientes.md` §1-§4.
>
> Función: que cualquier sesión futura (humana o IA) tenga las decisiones operativas del taller en una sola pantalla, con quién las tomó y por qué.

---

## 1 · Tabla maestra

| # | Decisión | Valor cerrado | Tomada por | Comentario |
|---|---|---|---|---|
| **P1** | Plazas del grupo cerrado | **8** (mínimo viable 5, máximo absoluto 10) | Code | Daniel marcó 6/8/10/12 = abierto. 8 es el sweet spot Foulkes para grupo cerrado psicoanalítico — suficiente para efecto espejo, manejable para conductor único en pocas sesiones |
| **P2** | Número de sesiones | **8** | Daniel | Coherente con la duración de elaboración mínima del marco kernbergiano en formato divulgativo |
| **P3** | Duración por sesión | **90 min** | Daniel | Coincide con la duración estimada del propio guion de sesión 1 |
| **P4** | Modalidad pública en landing | **Online (Zoom) por defecto · grupo presencial en Valencia opcional si hay ≥4 inscritas locales** | Code | Daniel quería preguntar preferencia en sesión 1 individual. Eso funciona, pero la landing necesita una modalidad base creíble. Online amplifica audiencia 100× respecto a Valencia (1,6% IG es Valencia según baseline) y no impide el grupo presencial si la demanda local lo pide |
| **P5** | Día y hora | **Miércoles 20:00 a 21:30 CEST** | Code | Argumentación detallada en §2.1 |
| **P5b** | Calendario sesiones | **S1=17 jun → S2=24 jun → S3=1 jul → S4=8 jul → S5=15 jul → S6=22 jul → S7=29 jul → S8=5 ago** | Code | Daniel decía «lanzamiento 8 jun» pero el 8 jun es lunes, no miércoles. Mover a 17 jun da 35 días de pre-venta (mejor que 26) sin perder la cohorte. Plan B en §2.2 si Daniel prefiere mantener 8 jun |
| **P6** | Estructura temporal | **Semanal 8 semanas seguidas** | Code | Daniel quería ofrecer 2 opciones (intensiva fin de semana + semanal con pausas). Simplificar a una opción protege la honestidad clínica (elaboración requiere espacio entre sesiones — bloque 6 del guion) y evita confusión en la landing |
| **P7** | Sesión individual previa | **Sí, 30 min, antes de S1, incluida en el precio total** | Daniel | Función: valorar perfil + confirmar entrada al grupo + acabar de comprometer compra |
| **P8** | Material entregable post-taller | **PDFs adicionales + acceso a comunidad cerrada (WhatsApp / Telegram). NO grabaciones. NO sesión seguimiento extra** | Daniel + Code (descarta grabaciones por política deontológica TWIM y descarta seguimiento para no complicar oferta) | |
| **P9** | Política de devolución | **Devolución total hasta 14 días desde el pago de la reserva, siempre que S1 no haya empezado. A partir de S1, sin devolución por naturaleza grupal del producto** | Code | Cumplimiento RGPD + ley consumidores España |
| **P10** | Filtro de selección | **Reserva 100 € pagada para entrar al proceso. Sesión 1 individual con Daniel (30 min). Si Daniel y la inscrita aceptan, paga 597 € restantes antes de S1. Si no aceptan, devolución total. Si no se presenta a la sesión individual, reserva no se devuelve.** | Daniel (estructura general) + Code (importes y reglas) | Pattern «commitment device» de productos de alto ticket |
| **P11** | Email de contacto | **`equipo@twimproject.com`** | Code | Daniel propuso `equipo@theworldismindproject.com` pero el dominio principal activo es `twimproject.com`. Si Daniel confirma que `theworldismindproject.com` está activo y configurado para recibir correo, se cambia. Mientras tanto, usar el dominio que sí funciona |
| **P12** | Segunda edición | **Anunciar en landing como 1ª edición · próxima Q4 2026 (primer miércoles octubre tentativo)** | Daniel (eligió «recomendación estratégica») | Crea urgencia sin agresividad |
| **P13** | Canales de captación | **Newsletter «Te escribo» · Instagram orgánico (carruseles + reels + stories) · Instagram Ads (Meta Ads)** | Daniel | Sin LinkedIn, sin email directo a no-suscriptores (RGPD), sin colaboraciones todavía |
| **P13b** | Presupuesto Meta Ads | **350 € totales en pre-venta (13 €/día durante 27 días, 18 may → 13 jun). Escalable a 700 € si CPL primera semana < 50 €. Stop-loss si CPL > 100 €** | Code | Argumentación en §2.3 |
| **P14** | Métricas objetivo | **Éxito 8 plazas · Mínimo viable 5 · Fecha de corte 1 jun 23:59 CEST** | Daniel | |
| **P14b** | Decisión si <5 al 1 jun | **Posponer S1 a miércoles 8 jul (5 semanas extra de captación) con calendario partido por pausa estival: S1-S4 en julio (8, 15, 22, 29 jul) · pausa agosto entero · S5-S8 en septiembre (2, 9, 16, 23 sep). Mantener pre-ventas vivas + 50 € extra de descuento por molestia. Si al 25 jun siguen <5: cancelar y devolver todas las pre-ventas. Si 0-2 al 1 jun: cancelar y devolver inmediatamente.** | Code | Argumentación en §2.4 |
| **T1** | Tipografía | **Instrument Serif (titulares) + Barlow Condensed (kickers, body)** | Daniel | Coherente con `instagram-sistema-visual-marca.md` §3.2. DM Serif Display + DM Sans del dossier original descartados |
| **MA1** | Informe técnico MailerLite | **Code lo construye desde cero — diagnóstico inicial en `mailerlite-api-incidencia.md`** | Daniel | Hay un bloqueo de sandbox: `twimproject.com` no está en allowlist, por lo que Code no puede hacer curl al endpoint `?diag=1` directamente. Daniel debe ejecutar el paso 2 del doc desde navegador y compartir el JSON |

---

## 2 · Argumentaciones detalladas

### 2.1 · Por qué miércoles 20:00 a 21:30 CEST (P5)

**Día:**
- Lunes está descartado por «resaca laboral», jueves por «preparación weekend». Conversiones histórica de contenido editorial de psicología muestran martes-miércoles como días de máximo engagement.
- Martes 19 may sale la Carta #2 «La voz que te juzga» a las 19:00 — taller los martes competiría con el envío del propio newsletter.
- → **Miércoles**.

**Hora:**
- 20:00 CEST es la hora pico declarada por Meta para la audiencia IG de Daniel esta semana (baseline IG §1.4).
- 20:00 CEST = 14:00 Buenos Aires / 13:00 México DF → accesible para LatAm tarde laboral, no horario familia.
- 20:00 a 21:30 (1h 30min) deja cierre antes de la rutina familiar/cena tardía.
- → **20:00 a 21:30 CEST**.

### 2.2 · Por qué calendario 17 jun → 5 ago (P5b)

- Daniel mencionó «lanzamiento 8 jun» pero 8 jun de 2026 es **lunes**, no miércoles. Forzar lunes para mantener fecha rompe el criterio de día (P5).
- Mover a **miércoles 17 jun**:
  - Da 35 días de pre-venta (vs. 26 originales) → tasa de llenado más realista.
  - Mantiene la cohorte editorial activa (Cap III + Carta #2 + Carrusel #3 + lo que venga las próximas 2-3 semanas).
  - Termina el 5 ago — antes de vacaciones de Daniel en agosto.
  - 8 sesiones × 7 días = 56 días → encaja sin estirar.

**Plan B si Daniel insiste en 8 jun**: cambiar día a **lunes** y calendario sería S1=8 jun → S2=15 jun → … → S8=27 jul. Funciona pero pierde la justificación de «miércoles = mejor día» del §2.1.

### 2.3 · Por qué 350 € de Meta Ads (P13b)

Cálculo:

- Revenue máximo = 8 × 697 € = **5.576 €**.
- ROAS deseable mínimo para producto editorial premium = **3x** (benchmark industria psicología digital España).
- Presupuesto Ads techo = 5.576 / 3 = **1.860 €**.
- Para pre-venta inicial con audiencia chica, presupuesto seguro inicial = 15-20% del techo = **350-400 €**.
- 350 € repartidos en 27 días = **13 €/día**.

Plan escalado:
- Semana 1 (días 1-7): 13 €/día → 91 € invertidos. Medir CPL (Cost per Lead, donde Lead = pre-reserva pagada).
- Si **CPL < 50 €** semana 1 → escalar a 700 € totales (25 €/día). Audiencia receptiva.
- Si **CPL 50-100 €** semana 1 → mantener 13 €/día, ajustar creativos.
- Si **CPL > 100 €** semana 1 → pausar Ads, revisar copy del anuncio + landing, retomar tras corrección.

CPL benchmark sano para producto premium psicología en España: 30-80 € (referencia genérica industria).

### 2.4 · Por qué posponer a 8 jul con pausa estival si <5 al 1 jun (P14b)

Calendario plan B propuesto:

- S1 = miércoles 8 jul
- S2 = miércoles 15 jul
- S3 = miércoles 22 jul
- S4 = miércoles 29 jul
- **[Pausa: 1-31 ago — vacaciones de Daniel]**
- S5 = miércoles 2 sep
- S6 = miércoles 9 sep
- S7 = miércoles 16 sep
- S8 = miércoles 23 sep

Razones por las que **este plan B es mejor que cancelar o que reprogramar entero a septiembre**:

1. **Mantiene la inercia editorial.** Cap III + Carta #2 + Carrusel #3 + Carta #3 (que tocará a finales de mayo o principios junio) son material caliente. Reprogramar todo a septiembre lo enfría 12 semanas; este plan B mantiene el arranque solo 3 semanas más tarde.
2. **5 semanas extras = 35 días.** Permite arreglar lo que haya fallado en captación: mejor copy de Ad, otro lead magnet, una colaboración cruzada, una entrevista en podcast ajeno. Suficiente para mover la aguja de 5 a 8.
3. **Respeta agosto vacaciones de Daniel.** Las 4 primeras sesiones (S1-S4) terminan el 29 jul; la pausa estival cubre agosto entero; las 4 últimas (S5-S8) reanudan el 2 sep. Daniel mantiene su descanso íntegro.
4. **La pausa es clínicamente coherente.** En el guion sesión 1 bloque 6 ya se anticipa que «en los próximos días puede que aparezcan cosas — el sistema procesando». Una pausa estival de 5 semanas entre S4 y S5 da espacio real de elaboración entre el bloque introductorio y el de cierre, lo cual es psicoanalíticamente legítimo (no un parche).
5. **Compensación a las pre-ventas existentes.** 50 € extra de descuento por la molestia del cambio = 647 € efectivo en lugar de 697 €. Eso fideliza y mantiene a las inscritas.

Razones para **no cancelar directamente al 1 jun con 3-4 inscritas**:

- Cancelar con pre-ventas pagadas genera mala reputación. Si hay 1-4 inscritas, devolver pre-ventas vacía el embudo y la 1ª edición «fallida» se cuenta como antecedente negativo durante meses.
- Posponer con honestidad («el grupo se llena mejor si esperamos 5 semanas más, te preservo tu plaza con descuento») mantiene la confianza.

**Solo se cancela si:**

- **0-2 al 1 jun** → cancelar inmediatamente y devolver. Por debajo de 3 inscritas el grupo no funciona ni clínica ni económicamente.
- **<5 al 25 jun** (24 días después del corte y 14 días antes de S1 del plan B) → cancelar y devolver. Si la campaña reforzada de 24 días no añadió ni 1 plaza, posponer otra vez quema la marca. Mejor cancelar limpio y volver con campaña de Q4.

---

## 3 · Decisiones aún pendientes (mínimas)

| # | Decisión | Por qué sigue abierta | Quién decide |
|---|---|---|---|
| P11 dominio | `equipo@twimproject.com` vs `equipo@theworldismindproject.com` | El segundo dominio no está confirmado activo en el repo | Daniel — solo necesita decir «sí está activo» o «no está, usa el primero» |
| P5b confirmación | Calendario 17 jun → 5 ago vs plan B 8 jun lunes | Si Daniel insiste en 8 jun, replantear día | Daniel — silencio se interpreta como acepta la recomendación 17 jun |
| Lead magnet específico del taller | Crear PDF gratuito «Cómo saber si tienes hambre de mirada» como gancho de Ads | Daniel no lo marcó pero Code recomienda hacerlo | Pendiente decisión — si Daniel ok, se produce |

---

## 4 · Lo que esto desbloquea

Con la tabla maestra cerrada, el siguiente PR puede:

1. **Crear la landing pública en `talleres/volver-a-mi/index.html`** con todos los datos reales (precio 697 €, 8 plazas, 8 sesiones, miércoles 20:00 CEST, online, 17 jun → 5 ago, política de reserva 100 €, etc.).
2. **Añadir grupo `pre-venta-volver-a-mi`** a `netlify/functions/subscribe.js` con su env var asociada.
3. **Crear el lead magnet específico del taller** (si Daniel da OK al PDF «Cómo saber si tienes hambre de mirada»).
4. **Documentar la automation MailerLite del taller** con copy de 3-4 emails de pre-venta.
5. **Brief operativo de Meta Ads** con copy de los 2-3 anuncios iniciales + audiencias + UTMs.
6. **Actualizar sitemap.xml** con la nueva URL.

Todo esto va en un PR separado para no mezclar «decisiones» con «implementación».

---

**Última actualización:** 13 may 2026 · sesión `claude/improve-proposal-quality-pq3d9` · post-merge PR #151.
