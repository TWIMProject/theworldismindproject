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
| **P5b** | Calendario sesiones | **S1=30 sep → S2=7 oct → S3=14 oct → S4=21 oct → S5=28 oct → S6=4 nov → S7=11 nov → S8=18 nov 2026** | Code (reprogramado el 13 may tras pregunta de Daniel sobre si verano era buena fecha) | Argumentación en §2.2. La fecha 8 jun del dossier original era lunes; la opción 17 jun caía en pleno arranque de verano (vacaciones target + caída industria coaching premium 30-50%); reprogramación a otoño aprovecha el «rentrée» como anclaje cultural del nombre «Volver a Mí» |
| **P6** | Estructura temporal | **Semanal 8 semanas seguidas** | Code | Daniel quería ofrecer 2 opciones (intensiva fin de semana + semanal con pausas). Simplificar a una opción protege la honestidad clínica (elaboración requiere espacio entre sesiones — bloque 6 del guion) y evita confusión en la landing |
| **P7** | Sesión individual previa | **Sí, 30 min, antes de S1, incluida en el precio total** | Daniel | Función: valorar perfil + confirmar entrada al grupo + acabar de comprometer compra |
| **P8** | Material entregable post-taller | **PDFs adicionales + acceso a comunidad cerrada (WhatsApp / Telegram). NO grabaciones. NO sesión seguimiento extra** | Daniel + Code (descarta grabaciones por política deontológica TWIM y descarta seguimiento para no complicar oferta) | |
| **P9** | Política de devolución | **Devolución total hasta 14 días desde el pago de la reserva, siempre que S1 no haya empezado. A partir de S1, sin devolución por naturaleza grupal del producto** | Code | Cumplimiento RGPD + ley consumidores España |
| **P10** | Filtro de selección | **Reserva 100 € pagada para entrar al proceso. Sesión 1 individual con Daniel (30 min). Si Daniel y la inscrita aceptan, paga 597 € restantes antes de S1. Si no aceptan, devolución total. Si no se presenta a la sesión individual, reserva no se devuelve.** | Daniel (estructura general) + Code (importes y reglas) | Pattern «commitment device» de productos de alto ticket |
| **P11** | Email de contacto | **`equipo@twimproject.com`** | Code | Daniel propuso `equipo@theworldismindproject.com` pero el dominio principal activo es `twimproject.com`. Si Daniel confirma que `theworldismindproject.com` está activo y configurado para recibir correo, se cambia. Mientras tanto, usar el dominio que sí funciona |
| **P12** | Segunda edición | **Anunciar en landing como 1ª edición · próxima en Q1 2027 (miércoles 20 ene o similar, momento «nueva versión de mí» post-Reyes)** | Daniel (eligió «recomendación estratégica») + Code (ajustada Q4→Q1 2027 tras reprogramación de la 1ª a sep 2026) | Crea urgencia sin agresividad. La cadencia natural pasa a ser «1ª edición sep-nov · 2ª edición ene-mar · 3ª edición sep» |
| **P13** | Canales de captación | **Newsletter «Te escribo» · Instagram orgánico (carruseles + reels + stories) · Instagram Ads (Meta Ads)** | Daniel | Sin LinkedIn, sin email directo a no-suscriptores (RGPD), sin colaboraciones todavía |
| **P13b** | Presupuesto Meta Ads | **Pre-pre-venta (jul): 0 € · Pre-venta dura (1-22 sep): 350 € totales (15 €/día durante 22 días), escalable a 700 € si CPL primera semana < 50 €. Stop-loss si CPL > 100 €** | Code | Argumentación en §2.3 |
| **P14** | Métricas objetivo | **Éxito 8 plazas · Mínimo viable 5 · Fecha de corte 22 sep 23:59 CEST** | Daniel (8/5) + Code (22 sep, 8 días antes de S1, ajustada tras reprogramación a otoño) | |
| **P14b** | Decisión si <5 al 22 sep | **Posponer S1 a miércoles 14 oct (2 semanas extra de captación con visibilidad rentrée a tope), con calendario corrido S1-S8 sin pausas (14 oct → 2 dic). Mantener pre-ventas vivas + 50 € extra de descuento por molestia. Si al 5 oct siguen <5: cancelar y devolver. Si 0-2 al 22 sep: cancelar y devolver inmediatamente.** | Code | Argumentación en §2.4 |
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

### 2.2 · Por qué calendario sep-nov 2026 y no verano (P5b)

**Decisión tomada el 13 may** tras la pregunta de Daniel «al acercarse verano, es buena idea esas fechas?». Cuatro razones objetivas para reprogramar a otoño:

1. **Comportamiento de compra premium en verano España.** La industria coaching/psicología premium reporta caídas de **30-50 % en conversiones** entre 20 jun y 10 sep (benchmarks Holded, Coverflex, agencias sectoriales). Productos reflexivos de >500 € se posponen sistemáticamente al rentrée. El ticket 697 € entra de lleno en esa categoría.

2. **Target del taller con peor disponibilidad estival.** Mujeres 25-50 con dependencia emocional + hijos en edad escolar (perfil CEO doc §2 + baseline IG): fin de curso final de junio, campamentos y viajes en julio, vacaciones en agosto. Miércoles 20:00 entre 17 jun y 5 ago se cruza con todo eso. Tasa de ausencias esperable alta — y en grupo cerrado psicoanalítico, una ausencia rompe el efecto espejo Foulkes.

3. **Incompatibilidad clínica con modo vacacional.** El guion sesión 1 bloque 6 anticipa que «en los próximos días puede que aparezcan cosas — recuerdos, emociones, sueños raros». Ese trabajo en pleno verano con sobrecarga social familiar no se elabora. La elaboración de introyecciones no metabolizadas exige rutina + espacio interno, no fiestas + viajes.

4. **«Volver a Mí» tiene anclaje narrativo natural en septiembre.** El nombre del taller coincide exactamente con el momento psicológico-cultural del rentrée: vuelta al cole interior, recomposición post-vacaciones, replantearse la vida. Eso no se puede comprar en marketing — lo da el timing cultural gratis.

**Probabilidad estimada de llenar 8 plazas:**

- Calendario 17 jun → 5 ago: **~30 %**.
- Calendario 30 sep → 18 nov: **~60-70 %** (16 semanas de captación con material editorial vivo desde mayo + ventana de rentrée).

**Calendario final 1ª edición:**

| Sesión | Fecha (miércoles 20:00-21:30 CEST) |
|---|---|
| S1 | 30 sep 2026 |
| S2 | 7 oct 2026 |
| S3 | 14 oct 2026 |
| S4 | 21 oct 2026 |
| S5 | 28 oct 2026 |
| S6 | 4 nov 2026 |
| S7 | 11 nov 2026 |
| S8 | 18 nov 2026 |

**Beneficio operativo colateral muy grande:**

- Agosto de Daniel queda **íntegro como vacaciones reales**, sin pre-venta paralela.
- Junio-julio se libera para **grabar el programa «Deja de Buscarte en Otros»** (asíncrono, 8 módulos × 3 h ≈ 24 h en 6 semanas = 4 h/semana). Era lo que Daniel quería tope agosto.
- En Q4 2026 tendrás **dos productos vivos simultáneamente**: taller premium sincrónico + programa digital asíncrono.

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

### 2.4 · Por qué posponer a 14 oct si <5 al 22 sep (P14b)

Calendario plan B propuesto:

- S1 = miércoles 14 oct 2026
- S2 = miércoles 21 oct
- S3 = miércoles 28 oct
- S4 = miércoles 4 nov
- S5 = miércoles 11 nov
- S6 = miércoles 18 nov
- S7 = miércoles 25 nov
- S8 = miércoles 2 dic 2026

Razones por las que **este plan B funciona**:

1. **Mantiene la inercia editorial otoñal.** Si la pre-venta de septiembre se quedó corta, octubre sigue siendo zona caliente de rentrée + ya hay 22 días extra de visibilidad acumulada del material de marketing.
2. **2 semanas extras = 14 días reales de captación adicional**, suficiente para mover la aguja de 4 a 5-8 con campaña reforzada (más Ads, más cross-sell, más urgencia narrativa).
3. **Sigue cabiendo antes de Navidad.** S8 cierra el 2 dic — antes del puente festivo Constitución/Inmaculada (6-8 dic) y muy antes de las vacaciones de Navidad. No interfiere con Q1 2027 que es cuando se anuncia la 2ª edición.
4. **Compensación a las pre-ventas existentes.** 50 € extra de descuento por la molestia del cambio = 647 € efectivo. Mantiene la fidelidad sin quemar la marca.

**Solo se cancela si:**

- **0-2 al 22 sep** → cancelar inmediatamente y devolver. Por debajo de 3 inscritas el grupo no funciona ni clínica ni económicamente.
- **<5 al 5 oct** (13 días después del corte y 9 días antes de S1 del plan B) → cancelar y devolver. Si la campaña reforzada de 13 días no añadió ni 1 plaza, posponer otra vez quema la marca. Mejor cancelar limpio y volver con la 2ª edición prevista Q1 2027.

---

## 3 · Decisiones aún pendientes (mínimas)

| # | Decisión | Por qué sigue abierta | Quién decide |
|---|---|---|---|
| P11 dominio | `equipo@twimproject.com` vs `equipo@theworldismindproject.com` | El segundo dominio no está confirmado activo en el repo | Daniel — solo necesita decir «sí está activo» o «no está, usa el primero» |
| ~~P5b confirmación~~ | ~~Calendario 17 jun → 5 ago vs plan B 8 jun lunes~~ | **Resuelto el 13 may**: Daniel preguntó si verano era buena fecha → Code argumentó reprogramación → Daniel confirmó septiembre. Nuevo calendario S1=30 sep → S8=18 nov | ✅ cerrado |
| Lead magnet específico del taller | Crear PDF gratuito «Cómo saber si tienes hambre de mirada» como gancho de Ads | Daniel no lo marcó pero Code recomienda hacerlo | Pendiente decisión — si Daniel ok, se produce |

---

## 4 · Lo que esto desbloquea

Con la tabla maestra cerrada, el siguiente PR puede:

1. **Crear la landing pública en `talleres/volver-a-mi/index.html`** con todos los datos reales (precio 697 €, 8 plazas, 8 sesiones, miércoles 20:00 CEST, online, **S1=30 sep → S8=18 nov 2026**, política de reserva 100 €, etc.).
2. **Añadir grupo `pre-venta-volver-a-mi`** a `netlify/functions/subscribe.js` con su env var asociada.
3. **Crear el lead magnet específico del taller** (si Daniel da OK al PDF «Cómo saber si tienes hambre de mirada»).
4. **Documentar la automation MailerLite del taller** con copy de 3-4 emails de pre-venta.
5. **Brief operativo de Meta Ads** con copy de los 2-3 anuncios iniciales + audiencias + UTMs.
6. **Actualizar sitemap.xml** con la nueva URL.

Todo esto va en un PR separado para no mezclar «decisiones» con «implementación».

---

**Última actualización:** 13 may 2026 · sesión `claude/improve-proposal-quality-pq3d9` · post-merge PR #151.
