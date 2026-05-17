# Métricas · Newsletter «Te escribo» · baseline 17 may 2026

> Documento de métrica datado · 17 may 2026 · sesión `claude/improve-proposal-quality-pq3d9`.
> Trigger: Daniel aportó captura del dashboard MailerLite corrigiendo la cifra de suscriptores que el doc CEO daba por «30». Se verifica contra fuente primaria viva y se deja escrito el mismo día (regla simétrica de `CLAUDE.md`).
> Convención: mismo patrón que `metricas-audiencia-ig-baseline-12-may-2026.md` y `metricas-gbp-daniel-orozco-q1-2026.md`.

---

## TL;DR

- **Suscriptores reales al 17-may-2026: 63 totales** (API) · **53 activos** (dashboard) · **+31 altas este mes** · 0 altas hoy.
- El `ceo-vista-completa-v2-1-mayo-2026.md` §1 (línea 60) dice `Suscriptores totales en MailerLite | **30**`. Esa cifra es del 1-may y está **desactualizada por más de 2×**. La cifra viva es esta, no la del doc CEO.
- Última campaña enviada: **«Te escribo · Recado 01 · Antes de ponerle nombre»** (11-may-2026) — 50 destinatarios, **68 % open**, **0 % click**.
- Lectura: crecimiento **relativo** fuerte de la palanca #1 (≈30 → 53 activos en ~16 días, orgánico). En **absoluto** sigue pequeño frente a las metas declaradas (200 netas mes 1 §3.3; 2.000 §7.3). 0 % click **no es alarma** (carta editorial pura sin CTA).
- No parchear el cuerpo del doc CEO v2-1 (es histórico fechado): este doc datado es la fuente viva. Alimenta la v3 del doc CEO cuando se genere.

---

## 1 · Datos y procedencia (doble verificación)

| Fuente | Qué dice | Cuándo |
|---|---|---|
| Captura dashboard MailerLite (app móvil, aportada por Daniel) | Total active subscribers **53** · New today **0** · New this month **31** · última campaña «Te escribo · Recado 01» 11/5/2026: 50 recipients, 68 % opened, 0 % clicked | 17-may-2026 ~12:15 |
| API MailerLite v3 vía MCP (`get_subscriber_count`) · cuenta `danielorozco@twimproject.com` · accountId `2232121` · prod | **63 total** | 17-may-2026 |

La diferencia 63 total vs 53 activos (~10) corresponde a estados no activos (baja / no confirmado / rebote): normal y esperable. Ambas cifras son reales; se reportan separadas, no se mezclan.

---

## 2 · Contraste con la verdad escrita

- `ceo-vista-completa-v2-1-mayo-2026.md` §1, línea 60: `| Suscriptores totales en MailerLite | **30** | Base mínima, todo está por construir |` — dato del 1-may-2026.
- Real al 17-may: **63 total / 53 activos**. Crecimiento neto ≈ +23 activos en ~16 días.
- No se edita la línea del doc CEO: ese documento se declara a sí mismo histórico-vivo y prevé **generar v3** ante dato nuevo importante (cierre del doc, §638), no parchearse in situ. Este doc datado es ahora la fuente primaria de la cifra.

---

## 3 · Lectura honesta (sin maquillar)

- **Relativo: bien.** La newsletter —palanca #1 del proyecto (CEO §7.3)— casi dobla base en ~2 semanas de forma **orgánica**, sin Ads ni herramientas de medición de pago. Es la evidencia de que lo que funciona es producir y captar, no medir.
- **Absoluto: aún chico.** 53 activos está **por debajo** de la meta de «200 netas en mes 1» (CEO §3.3) y muy lejos de los 2.000 que el §7.3 marca como la palanca real. Buen ritmo, base todavía mínima. No confundir crecimiento porcentual desde base baja con tracción consolidada.
- **68 % open: excepcional**, coherente con el histórico del doc CEO (51-70 % en grupo Reto). La gente que entra, lee.
- **0 % click: esperable, NO alarma.** «Recado 01 · Antes de ponerle nombre» es carta editorial pura, sin CTA ni enlace. El doc CEO §3.3 lo dice: las cartas *son* el producto; los emails de distribución son otra cosa. El click solo es señal a vigilar en cartas que **sí** lleven CTA (p. ej. las del kit del Directo / Cap III).

---

## 4 · Implicaciones

1. **Insumo para la v3 del doc CEO.** Dato nuevo importante de la palanca #1: entra junto al resto de triggers del §638 (Ahrefs, KPIs YouTube, primer mes Sergio) cuando se decida regenerar el doc CEO. No antes y no parcheando el v2-1.
2. **No cambia la recomendación sobre Ahrefs; la refuerza.** Que la palanca #1 crezca sin gastar en analítica de pago confirma que el dinero, en esta fase, va a ejecución (terminar el programa + motor newsletter/libro del `veredicto-15-may`), no a medición cara.
3. **Inoculación.** Si una sesión futura lee «30» en el doc CEO §1, está **desactualizado**. La cifra viva está aquí y es reconfirmable en segundos y gratis con `get_subscriber_count` (MCP MailerLite). Reconfirmar antes de citar cualquier cifra de suscriptores.

---

## 5 · Refs

- `ceo-vista-completa-v2-1-mayo-2026.md` §1 (línea 60, cifra desactualizada) y cierre §638 (trigger v3).
- `ceo-vista-completa-v2-1-mayo-2026.md` §3.3 (meta 200 mes 1, naturaleza editorial de «Te escribo») y §7.3 (palanca #1, meta 2.000).
- `contenido-rrss/te-escribo-newsletters/` (PLAN-CAPTACION-30D.md, PLAN-LANZAMIENTO-5-MAYO.md, recado-01-antes-de-ponerle-nombre.txt).
- `CLAUDE.md` (regla simétrica: actualizar la verdad escrita el mismo día).

---

— Nota de trazabilidad: generado el 17-05-2026 en sesión `claude/improve-proposal-quality-pq3d9`. Verificado contra API MailerLite v3 (cuenta `2232121`, prod). Próxima revisión: cuando se genere la v3 del doc CEO o cuando la cifra cruce un umbral relevante (200 / 1.000 / 2.000).
