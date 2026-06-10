# Plan x10 · Lista email · 77 → 770+ · 10 jun 2026

> Encargo de Daniel (10 jun, tras leer `analisis-foco-x2-ingresos-2026-06-10.md`): «PLAN REAL EFECTIVO PARA MULTIPLICAR LA LISTA EMAIL POR 10». Este doc concreta el mini-plan «captación sin cadencia» de `captacion-email-doc-externo-comparacion-2026-06-04.md` §3 con números, presupuesto y compuertas. No contradice ninguna decisión tomada: respeta el modelo sin cadencia, usa MailerLite, y opera dentro de la excepción acotada de Ads de calentamiento de lista (26 may, 6 criterios).

---

## 0 · La matemática primero (por qué hace falta motor de pago)

- Lista hoy: **77** (MailerLite en vivo, 10 jun). Crecimiento orgánico real: ~25-30 netas/mes.
- **A ritmo orgánico, el x10 tarda ~24-28 meses.** No llega a tiempo para DDBEO (agosto) ni para la preventa de Volver a Mí (septiembre).
- El motor de pago ya está **validado con datos propios**: anuncio «5 señales de que buscas validación» (18-25 may) → 7.172 visitas a la landing por 139,93 € = **0,02 €/visita**, CTR 12,89 % (`metricas-meta-ads-carrusel-validacion-25-may-2026.md`). Con conversión visitante→lead del 5-15 % (benchmark repo), el CPL queda en **0,39-1,94 €**.
- **Coste del x10:** +700 suscriptoras a CPL 1,5 € ≈ **1.050 € totales** repartidos en ~6 meses (≈175 €/mes · 6 €/día). A CPL 0,75 €, la mitad. Es la decisión de gasto que esto requiere de Daniel — todo lo demás es ejecutable sin él.

## 1 · Paso 0 · Medición (bloquea todo · esta semana)

Sin conocer la conversión real de la landing, no se cumple el criterio 1 de la excepción de Ads (embudo verificado) y no se puede juzgar el CPL.

- Daniel · marcar `generate_lead` como **evento clave en GA4** + importar a Google Ads (pendiente desde el 9 jun · 5 min de panel).
- Claude · verificar que el evento dispara en las landings de captación y cuadrar altas MailerLite vs visitas del periodo del anuncio de mayo para estimar el CR real retroactivo.

## 2 · El motor · Meta Ads de calentamiento always-on

- **Creativo:** el ya validado («5 señales», CTR 12,89 %) + 1 variante nueva por mes (Claude la produce reciclando carruseles existentes · cero horas de Daniel).
- **Destino:** la landing ya validada del anuncio de mayo como control; variante B = `/libro/capitulo-3/` (Cap III · capta email con intercambio de valor, sin prometer cadencia). La que gane en CR a 3 semanas se queda con todo el tráfico.
- **Presupuesto:** arrancar **6 €/día**. Compuertas (de la hoja de decisiones, ya escritas): si a 14 días CPL ≤ 4 € y ≥10 leads → mantener; si CPL ≤ 2 € sostenido 30 días → subir a 10-15 €/día; si CPL > 4 € dos semanas → pausar y cambiar creativo, no insistir.
- **Quién:** Daniel publica la campaña una vez con briefing clic a clic (mismo formato que la de Google Ads del 9 jun · 30-40 min). Claude prepara briefing, copy, audiencias y revisa métricas cada lunes.
- **Convivencia con Google Ads de pacientes:** son presupuestos y objetivos distintos (Google = llamadas consulta/derivación · Meta = lista). No compiten entre sí.

## 3 · La red de seguridad · bienvenida automática

Sin cadencia, la suscriptora nueva quedaría en silencio semanas. La **automation «Bienvenida Te escribo»** (pieza 3 del doc del 4 jun, aún no construida) lo resuelve: D0 carta de bienvenida con el re-encuadre («no te escribo cada semana · te escribo cuando algo merece tu tiempo») + D3 mejor carta histórica + D7 Cap III si no lo tiene. Claude la construye y deja lista para que Daniel la active (la activación de automations requiere panel de escritorio · verificado 15 may).

## 4 · El orgánico apunta al mismo embudo (cero piezas nuevas)

- **Regla de un solo CTA:** cada pieza existente (carruseles reciclados, directos, YouTube E5/E6 ya publicados, descripciones de podcast, bio IG) apunta a UNA misma landing de captación. Nada de repartir el tráfico entre 5 destinos.
- **Directo 14 jun** ya funciona como evento de captación (grupo Lead Directo → lista).
- **Rotación de promo IG 4 semanas** (doc 4 jun §3.4): gancho · prueba social · adelanto de carta · llamada directa con el re-encuadre sin cadencia. Solo reciclaje, sin producción nueva (regla foco: 15 jun-28 jul se graba DDBEO y nada más).

## 5 · Hitos y compuertas

| Mes | Lista (objetivo) | Gate |
|---|---|---|
| jul 2026 | 200 | CPL ≤ 4 € · CR landing ≥ 5 % · si no, cambiar creativo/destino |
| ago 2026 | 350 | open bienvenida ≥ 40 % (calidad del tráfico) |
| sep 2026 | 500 | la preventa Volver a Mí se apoya en esta lista |
| oct 2026 | 600 | lanzamiento DDBEO evergreen a lista ya caliente |
| dic 2026 | **770+** | x10 cumplido · revisar si se mantiene o se sube inversión |

Limpieza: doble opt-in activo y poda de inactivas trimestral para proteger el open rate (hoy 68 %).

## 6 · Decisión que requiere a Daniel

Una sola: **el presupuesto** (~175 €/mes durante 6 meses, con compuertas de salida semanales). Todo lo demás —briefing, creativos, automation de bienvenida, métricas— lo opera Claude.

---

*Refs: `captacion-email-doc-externo-comparacion-2026-06-04.md` (mini-plan base y líneas rojas) · `metricas-meta-ads-carrusel-validacion-25-may-2026.md` (motor validado) · `metricas-newsletter-baseline-17-may-2026.md` · excepción Ads de calentamiento 26 may (perfil §11) · `analisis-foco-x2-ingresos-2026-06-10.md` §1.2 (por qué la lista precede al producto).*
