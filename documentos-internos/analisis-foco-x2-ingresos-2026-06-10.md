# Análisis · Foco y camino al x2 de ingresos · 10 jun 2026

> Encargo de Daniel (10 jun 2026, verbatim): «Analiza el modelo "twimproject.com - Daniel Orozco" y busca la manera de encontrar el camino para mejorar la eficiencia y eficacia y no sea un modelo que se vaya dispersando. Tenemos el objetivo de aumentar los ingresos que ingresa ya Daniel Orozco en su consulta privada, x2, creando productos más allá de los pacientes que va tratando en consulta. Analiza la posibilidad de que aunque sea viable y bueno lo que ya está programado, Daniel por su cantidad de horas de trabajo, agotamiento por su función de padre y de marido puede provocar que no sean tan viables para acometer él psicológicamente por falta de energía.»
>
> Método: regla §1 de CLAUDE.md cumplida · análisis construido leyendo primero el repo completo (vista CEO v2, 9 cierres de sesión, inventario de catálogo, métricas de todos los canales, presupuesto 6 meses, modelo Unió) y contrastado con **datos vivos** de Stripe y MailerLite vía MCP el 10 jun 2026. Cada cifra cita su fuente.

---

## 0 · Veredicto en cinco líneas

1. **El x2 es alcanzable a 12 meses, pero no por el camino de «más productos».** Sale de **una** palanca que escala sin horas de Daniel (red supervisada) + **un** producto premium ya comprometido (Volver a Mí) + audiencia componiendo con Ads baratos. Todo lo demás es goteo o distracción.
2. **La verdad incómoda verificada hoy:** ingresos reales de producto fuera de consulta desde el 1 de mayo = **29,70 € brutos, y son compras de prueba de Daniel pendientes de reembolso** (Stripe en vivo, 10 jun). El producto aún no ha facturado un euro externo. Toda la capa de producto es, hoy, proyección.
3. **El cuello de botella no es el modelo ni las ideas: son las horas y la energía de Daniel.** El repo lo demuestra con datos: toda tarea que depende solo del cuerpo/voz/decisión de Daniel lleva 12-16 días atascada; toda tarea delegable a Claude se cierra el mismo día.
4. **El calendario H2 programado, tal cual está, no es psicológicamente viable** para un padre y marido con 25-30 sesiones/semana de consulta. Tiene tres picos de colisión (jun-jul, agosto, septiembre) que hay que desactivar recortando, no apretando.
5. **Recomendación central: pasar de 25+ frentes abiertos a 3.** Congelar el resto con fecha de revisión escrita (congelar no es renunciar: es decidir cuándo se decide).

---

## 1 · La matemática del x2 (sin autoengaño)

### 1.1 · Base verificada

| Concepto | Cifra | Fuente |
|---|---|---|
| Facturación consulta privada Daniel | **~54.000 €/año ≈ 4.500 €/mes** | `modelo-captacion-supervisada-union-periodistas.md` §4 |
| Objetivo x2 | **+4.500 €/mes adicionales sostenidos** fuera de la consulta actual | encargo 10 jun |
| Ingresos de producto reales acumulados (1 may → 10 jun) | **29,70 € · 3 pagos (2×9,90 + 1×8,90) del 3 jun · compras de prueba sin reembolsar** | Stripe MCP en vivo 10 jun · `cierre-sesion-2026-06-03.md` |
| Lista email MailerLite | **77 suscriptores** (63 el 17 may · +22 % en 3 semanas) | MailerLite MCP en vivo 10 jun · `metricas-newsletter-baseline-17-may-2026.md` |
| Open rate newsletter | 68 % (excepcional) | `metricas-newsletter-baseline-17-may-2026.md` |

### 1.2 · Por qué los productos digitales NO dan el x2 en 2026

Benchmark del propio repo (`ceo-vista-completa-v2-1-mayo-2026.md` §12.3): conversión email → compra de programa ≤100 € = 2-5 %. Con 77 suscriptores, eso son **2-4 ventas de DDBEO = 100-280 €, una sola vez**. Las proyecciones «realistas» del presupuesto (30 ventas DDBEO en 6 meses) exigen que compre el ~40 % de la lista actual — imposible. **La lista tiene que multiplicarse ×10-20 antes de que el producto digital sea una línea de ingresos relevante.** Eso es trabajo de 2026 para cosechar en 2027. No es razón para abandonar DDBEO (está al 80 % de producción y la ventana de grabación empieza el 15 jun): es razón para **no esperar de él el x2** y no construir más productos encima.

### 1.3 · Las vías, evaluadas contra el recurso escaso real (energía de Daniel)

| Vía | €/mes potencial a 12 meses | Coste en horas/energía de Daniel | Veredicto |
|---|---|---|---|
| **A · Red supervisada** (Sergio + convenio Unió + derivación desde Google Ads) | **~2.500 €/mes** a mes 12 (`twim-clinic-modelo-derivacion.md` §5.5 vía CEO §11.5) · escenario régimen Unió: 34.500 €/año (`modelo-captacion-...` §4) | **Bajo** · ~1 h/semana de supervisión por asociado · no toca tardes | **MOTOR PRINCIPAL del x2.** Única línea cuyo techo no son las horas de Daniel. Coincide con su objetivo declarado: «liberarme desde septiembre ya, de tardes» (5 jun) |
| **B1 · Taller Volver a Mí** (697 €/plaza · 5-8 plazas · 2 ediciones/año) | ~580-930 €/mes prorrateado (realista 5 plazas = 3.485 €/edición, `presupuesto-6-meses-consultor-24-may-2026.html` §3) | Alto pero **acotado en el tiempo** (preventa 22 días + 8 sesiones) | **SEGUNDA PIEZA.** Ya comprometido, ticket alto, valida el modelo grupal. Se mantiene |
| **B2 · DDBEO evergreen** (49-70 €) | ~300 €/mes realista a 6 meses · compone con la lista | **Alto una sola vez** (grabación jun-jul ya bloqueada) · luego pasivo | **TERMINAR Y CERRAR.** Se graba porque está al 80 % y la ventana existe — no porque dé el x2 en 2026 |
| **B3 · Libros + cuaderno + audiolibros + tienda firmados** | 50-150 €/mes goteo | Medio y recurrente (maquetar, grabar voz, empaquetar) | **AUTOMATIZAR Y DEJAR EN GOTEO.** No son palanca; son marca y puerta de entrada |
| **C · B2B In-Company / conferencias** (2.450 €/contrato) | 0 hoy · cero pipeline declarado (`ceo-vista-completa` §4.1) | Alto (venta activa + entrega presencial) | **CONGELAR salvo inbound.** Un contrato vale mucho pero la prospección consume la energía que no hay |

### 1.4 · La suma que sí cuadra (horizonte 12 meses, jun 2027)

```
A  · Red supervisada (4-5 asociados vía Unió + Ads)   ≈ 2.500 €/mes
B1 · Volver a Mí (2 ediciones/año, 5-7 plazas)        ≈   800 €/mes
B2 · DDBEO evergreen (lista ya ×5-10 por Ads)         ≈   400 €/mes
B3 · Libros + digital en goteo automatizado           ≈   150 €/mes
Opt· Consulta: tarifa +5-10 € y agenda llena vía Ads  ≈   650 €/mes
                                                      ─────────────
                                                      ≈ 4.500 €/mes  → x2
```

Cada sumando tiene fuente documental o dato vivo detrás; ninguno requiere que Daniel trabaje más tardes — al contrario, A las libera. **El x2 no se consigue añadiendo: se consigue concentrando.**

---

## 2 · Diagnóstico de dispersión (cuantificado, no impresionista)

- **25+ frentes abiertos** a 10 jun (inventario completo en cierres de sesión 15 may → 9 jun): 22 productos/líneas en catálogo, 9 proyectos editoriales activos, 5 de captación, 4 de infraestructura.
- **15 tareas llevan más de 14 días vencidas o arrastrándose**, y comparten un patrón: todas dependen **solo de Daniel** (grabar podcast E5 · 14 días; imprimir tarjetas · 12 días; activar Bizum/PayPal en Stripe · 16 días; métricas Carrusel #3 · 15 días; subir fotos hero · 14 días). Las tareas delegables a Claude se cierran el mismo día.
- **Las 3 decisiones de la hoja del fin de semana (30 abr-4 may) acabaron pivotadas o sin ejecutar:** concentración→pivotó a captación+red (5 jun); Meta Ads 6 €/día→pivotó a Google Ads (9 jun); VA en junio→no contratada. No es indisciplina: es que el plan se escribió por encima de la capacidad real de ejecución.
- **Lectura honesta:** la capacidad de *planificar* del sistema (Claude produce docs, landings, embudos a demanda) es ~10× la capacidad de *ejecutar* de Daniel (1-2 h/día fuera de consulta, con familia). Cada plan nuevo que se escribe sin retirar otro **aumenta la deuda**, no el ingreso. La dispersión no es un defecto de carácter: es el resultado aritmético de un embudo de planes más ancho que el embudo de horas.

---

## 3 · Viabilidad psicológica del calendario H2 (la pregunta de Daniel)

El plan programado es bueno sobre el papel. Sobre el cuerpo de un padre y marido con 25-30 sesiones/semana, tiene **tres picos de colisión**:

### Pico 1 · 15 jun – 28 jul · grabación DDBEO
Sobre la misma ventana caen hoy: grabar 8 módulos + 3 audios, Directo 14 jun, terminar maquetación del libro «Tu valor», vigilar Google Ads, grabar vídeo YouTube ansiedad, podcast E5, carruseles. **Es el triple de lo que cabe.**
→ **Descarga:** en esa ventana **solo se graba DDBEO**. El vídeo de ansiedad y el E5 se difieren a la era de voz clonada (agosto+) o se cancelan sin culpa. La maquetación del libro se cede (Claude prepara + freelance Fiverr remata, 80-150 €). Carruseles: solo reciclaje, nada nuevo.

### Pico 2 · Agosto · las «vacaciones inviolables» invadidas
El propio repo declara agosto como vacaciones inviolables (`presupuesto-6-meses`), pero el roadmap de libros le ha metido dentro: grabar 30-60 min de voz, audiolibro Engranajes, tapas KDP, maquetación (`roadmap-libros-audiolibro-y-tapa-2026.md`).
→ **Descarga:** agosto queda con **una sola tarea de Daniel: grabar los 30-60 min de voz fuente** (un día, desbloquea audiolibro + podcast T2 + futuros). Audiolibro y tapas pasan a **octubre-noviembre**. Que el psicólogo del burnout se queme en sus vacaciones no es solo un riesgo personal: es un riesgo de marca.

### Pico 3 · Septiembre · el mes imposible
Hoy septiembre acumula: lanzamiento libro nuevo + pre-venta dura Volver a Mí (22 días con Meta Ads) + sesión individual de 30 min con **cada** inscrita + S1 del taller (30 sep) + ElevenLabs T2 + talleres adolescencia en el calendario viejo + arranque red Unió.
→ **Descarga:** septiembre se queda con **Volver a Mí como único lanzamiento activo** (es el de mayor ticket y ya tiene plan de captación). El libro se publica en KDP **sin campaña** (la campaña del libro se hace en octubre, después del cierre de preventa). ElevenLabs T2 arranca cuando la preventa cierre (23 sep+). La red Unió la arranca **Sergio**, no Daniel — Daniel solo supervisa.

### El principio que ordena todo
**Regla 1-2-3 (propuesta para persistir si Daniel da OK):**
- **1** sola pieza de producción que requiera el cuerpo/voz de Daniel a la vez (ahora: DDBEO; nada más se graba hasta el 28 jul).
- **2** horas/día máximo de TWIM fuera de consulta, con presupuesto semanal explícito (~10-12 h/sem); si una semana se excede, la siguiente se recorta. La familia no es lo que queda cuando TWIM termina: es una restricción de diseño del modelo.
- **3** frentes activos máximo: (1) consulta de mañanas, (2) la pieza de producción única, (3) la línea delegada de crecimiento (red supervisada + Ads, que operan Sergio y Claude).

---

## 4 · Qué se congela (con fecha de revisión, no a la basura)

| Frente | Estado | Revisión |
|---|---|---|
| Podcast E5 «Autoexigencia» (grabar con voz propia) | CONGELADO → se hará con voz clonada | sep 2026 (post-grabación voz agosto) |
| Vídeo YouTube ansiedad (formato A, guion listo) | CONGELADO → guion no caduca | sep 2026 |
| X/Twitter + LinkedIn activos | GOTEO de reciclaje automatizable, cero piezas nuevas | oct 2026 |
| «Rompe el TENGO QUE» + «Deja de obligarte» | YA CERRADOS (decisión 20 may) · sin cambios | 2027 |
| Producto B2B psicólogos «Consulta en Orden» | FASE 0 documental · sin horas | Q1 2027 (como ya estaba) |
| Mazo de cartas físico | IDEA CAPTURADA · sin recursos | tras validar DDBEO (como ya estaba) |
| Audiolibros + tapa KDP Engranajes | MOVIDO a oct-nov (solo voz fuente en agosto) | oct 2026 |
| Talleres adolescencia (TDAH + bachillerato) | Según decisión 18 may (descartada la vía Sergio co-facilitador) · landing en SEO pasivo | dic 2026 |
| In-Company / conferencias | Solo inbound · cero prospección activa | dic 2026 |
| Tienda libros firmados | PASIVA tras imprimir tarjetas (única acción física pendiente) | — |

Lo que **no** se congela: DDBEO (grabación 15 jun-28 jul) · Volver a Mí (calendario intacto) · newsletter «Te escribo» (cadencia «cuando hay algo», como siempre) · Google Ads captación + derivación · negociación Unió (la lleva la otra parte) · Directo 14 jun (ya convocado).

---

## 5 · Hallazgos de auditoría en vivo (10 jun) · requieren acción

1. **Patrón compatible con card-testing en Stripe.** ~90 intentos de cobro de **75,00 €** consecutivos en minutos, el ~2 jun, **todos fallidos, ninguno capturado** (verificado: cero cargos de 75 € exitosos). Es el patrón típico de bots probando tarjetas robadas contra un Payment Link público. No ha entrado dinero fraudulento, pero conviene actuar: **revisar Radar en el dashboard y activar reglas anti card-testing (3DS/CAPTCHA en Payment Links)**. *Identificado el mismo 10 jun (segunda tanda de la sesión):* el precio de 75 € es el del producto `prod_UbE1eMyz4kOIGq` · «Libro · Edición especial · "Los engranajes de la mente" · tapa blanda · papel grueso a color · pieza única» (tienda de libros firmados, `/libros-firmados.html`). El link no se desactiva (venta viva con stock real) · se blinda desde el panel. 10 minutos.
2. **Compras de prueba del 3 jun sin reembolsar** (2×9,90 € + 8,90 €). Tarea ya anotada el 3 jun, sigue pendiente. Mientras no se reembolsen, contaminan cualquier métrica de ventas.
3. **MailerLite a 77 suscriptores** · crecimiento orgánico sano (+22 % en 3 semanas) pero a este ritmo la lista tarda ~10 meses en llegar a 500. El Ads de calentamiento de lista (excepción acotada del 26 may) es la vía para acelerar sin romper compuertas.
4. **Hitos del calendario vencidos** al 10 jun: doc métricas Carrusel #3 (15 días), verificación idioma MailerLite pre-Directo (el Directo se movió al 14 jun · verificar idioma E4 sigue pendiente), evento Google Calendar aún en fecha vieja.

---

## 6 · Qué cambia mañana por la mañana (resumen operativo)

1. **Daniel decide sobre la regla 1-2-3** (§3). Si OK, se persiste en CLAUDE.md como regla de foco.
2. **15 jun → 28 jul: solo DDBEO.** Todo lo demás que pida su voz/cuerpo, congelado según §4.
3. **La red supervisada es el proyecto estrella del x2** — y es de Sergio y de Claude en lo operativo, de Daniel solo en supervisión y criterio clínico. Cerrar convenio Unió cuando responda; mientras, Claude prepara el kit de arranque del primer asociado.
4. **Stripe: 10 minutos de panel** — Radar/3DS + reembolsos de prueba + identificar el link de 75 €.
5. **Agosto sagrado salvo 1 día de grabación de voz.**
6. **Septiembre = solo Volver a Mí.** Libro sale sin campaña; su campaña, en octubre.

---

*Generado el 10 jun 2026 · sesión `claude/practical-hypatia-3dmulg` · fuentes: repo completo al 10 jun + Stripe MCP + MailerLite MCP en vivo. Sustituye a ningún documento: ordena los existentes bajo el criterio de energía como recurso escaso. Si Daniel valida §3 y §4, persistir la regla 1-2-3 en CLAUDE.md y actualizar los planes afectados (roadmap libros, calendario H2).*

---

## Apéndice · Correcciones de Daniel tras la lectura (10 jun, misma tarde)

Daniel leyó el análisis y corrigió cuatro puntos · el repo iba por detrás de la realidad. Quedan registrados para que el análisis no se cite con datos viejos:

1. **Reembolsos hechos.** Las 3 compras de prueba (29,70 €) ya están reembolsadas. El contador de ingresos de producto queda limpio en 0 € reales — punto de partida correcto del §1.1.
2. **Podcast E5 y E6 ya publicados** (hace ~4 semanas y ~13 días respectivamente). La fila «Podcast E5 · CONGELADO» del §4 y la mención del §2 a «grabar E5 · 14 días atascado» quedan **anuladas**: ese frente ya estaba cerrado y el repo no lo reflejaba. La congelación del §4 aplica solo al vídeo YouTube de ansiedad pendiente de grabar (si sigue pendiente).
3. **Red supervisada · estado real:** Google Ads ya invierte en recibir llamadas (campaña 9 jun) · Unió de Periodistes sin cerrar, falta su feedback final · Sergio a la espera de derivaciones. El motor A del §1.3 está encendido en fase de arranque, no en idea.
4. **«Libros que trabajan solos»** · Daniel pregunta el mecanismo («¿cómo van a trabajar solos para ser vistos y comprados?»). Respuesta concreta en el plan x10 (`plan-x10-lista-email-2026-06-10.md`) y en el resumen de sesión: trabajan solos **solo si** los 4 circuitos están montados (Cap III → automation D0/D3/D7 ya activa · email post-compra pidiendo reseña Amazon · superficies fijas con un solo CTA · SEO de la landing del libro) **y** el motor x10 les pasa tráfico. Sin tráfico, los circuitos convierten poco · por eso la lista precede al libro (§1.2).
