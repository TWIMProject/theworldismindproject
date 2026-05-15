# Veredicto · Análisis externo de oportunidades de negocio

> Creado el **15 may 2026** en sesión `claude/improve-proposal-quality-pq3d9`.
>
> Daniel pegó en chat un análisis externo de «oportunidades de negocio» (no versionado en el repo) y pidió contrastarlo contra la verdad documentada. Este documento deja el veredicto escrito **para que ninguna sesión futura vuelva a litigar las mismas premisas falsas**.

---

## 0 · Procedencia y fiabilidad

El contraste se delegó primero a un sub-agente de exploración. Su transcripción **quedó contaminada por una confabulación interna** (narró una supuesta «orden crítica» del usuario que nunca se emitió). Un escaneo de firma de inyección sobre `*.md *.txt *.html *.json` del repo dio **limpio** — el repo no está envenenado; fue un fallo del agente, no un documento adversario.

Por esa razón, **todos los números de este veredicto los verifiqué yo leyendo los ficheros primarios**, no la transcripción del agente (que además tenía un error factual: dijo «79 €» cuando el repo dice 70 €). Cada afirmación de abajo cita el fichero exacto donde se puede re-verificar.

---

## 1 · Veredicto en una línea

El análisis externo es **investigación de mercado genérica correcta**, pero su recomendación estrella se apoya en una premisa que **el propio repo ya desmintió internamente el 12 may**. No es ejecutable tal cual.

---

## 2 · Las tres correcciones que impone el repo

### 2.1 · «~30k IG» no es un dato documentado en ningún sitio

`documentos-internos/metricas-audiencia-ig-baseline-12-may-2026.md` da solo porcentajes demográficos (60,1 % mujeres · cohorte 25-44 = 62,7 % · geografía dispersa, top 4 ciudades 11,3 %) y se refiere literalmente a *«una cuenta de este tamaño»*. `cierre-sesion-2026-05-15.md` §3.3 + PR #145: Carrusel #2 rindió **5-6× por debajo del benchmark**.

→ La tabla de ingresos del análisis (650 € → 2.900 € → 6.000 €) cuelga de un número de audiencia **inventado**. Inferir desde memoria contra dato contrario del repo es exactamente lo que la regla de método prohíbe.

### 2.2 · «Deja de Buscarte en Otros» no es un producto vivo con funnel que auditar

`documentos-internos/programa-deja-de-buscarte-en-otros/00-BRIEFING-DANIEL.md`, textual: *«el programa NO existe como producto entregable… Tu CEO doc lo daba por «listo». No lo estaba.»* Hoy solo están hechos Módulo 1 + Audio 1 + workbook + protocolo 21 días. Módulos 2-5 y Audios 2-3 son esqueletos. Stripe sin montar. Precio **70 €** (no 79 €). `cierre-sesion-2026-05-15.md` §1: por grabar **15 jun – 28 jul**, tope agosto.

→ El análisis dice «audita tu funnel actual, primer ingreso en 30-90 días». Repite **el mismo error que el repo ya cazó y corrigió**. El primer movimiento real no es montar embudo: es terminar de producir y grabar el programa.

### 2.3 · Migrar la newsletter a Substack/Beehiiv contradice infraestructura decidida

`cierre-sesion-2026-05-15.md` §3.3: la newsletter es **«Te escribo»** sobre MailerLite + función Netlify. Precedente relevante en el mismo §3.3: el equipo **ya rechazó explícitamente** el nombre de newsletter propuesto por un dossier externo de ChatGPT. Cambiar de plataforma rompe lo construido.

---

## 3 · Lo genuinamente aprovechable (que el repo NO contempla)

- **Mazo de cartas «Cartas para volver a ti»** — no hay línea de producto físico en el repo. El hueco que describe (rigor psicoanalítico frente a la avalancha de cartas-oráculo) es real. **Idea capturada como producto futuro candidato**, sin comprometer recursos hasta validar §4.1.
- **Programa de afiliados** — válido solo como multiplicador de fase 2, condición que el propio análisis reconoce («solo cuando el producto ancla funcione»).
- **Franqueza estructural** — «nada es pasivo los primeros 6 meses» y «cobra consulta en paralelo» coinciden con la realidad del repo: no hay ingresos del programa porque el programa no está construido.

---

## 4 · Orden de prioridad reconciliado (no sustituye al plan vivo, lo ordena)

1. **Terminar + grabar «Deja de Buscarte en Otros»** (Módulos 2-5 + Audios 2-3 + Stripe) — ventana 15 jun–28 jul ya documentada. Es el #1 verdadero.
2. **Libro «Tu valor…» + Cap III lead magnet + «Te escribo»** como motor de tráfico cualificado — ya en marcha; es la respuesta real al cuello de botella «tráfico al embudo».
3. **Mazo de cartas** — segundo movimiento, tras validar #1.
4. **Afiliados** — tercero.

---

## 5 · Inoculación para futuras sesiones

Si una sesión futura recibe un análisis externo que afirma cualquiera de estas dos cosas, **es falso y el repo manda**:

- ❌ «TWIM tiene ~30k seguidores en Instagram» → no documentado; cuenta pequeña, Carrusel #2 5-6× bajo benchmark.
- ❌ «"Deja de Buscarte en Otros" ya es un producto vendible con funnel» → no es entregable hasta verano 2026 (grabación 15 jun–28 jul).

Regla operativa confirmada: ante análisis de IA externos, contrastar SIEMPRE contra ficheros primarios del repo antes de aceptar premisas. Ya hay dos precedentes de dossiers externos con recomendaciones que el equipo tuvo que corregir (nombre de newsletter; este análisis).
