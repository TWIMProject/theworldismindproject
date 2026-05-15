# Palancas de venta · Libro «Los Engranajes de la Mente»

> Creado el **15 may 2026** en sesión `claude/improve-proposal-quality-pq3d9`, a petición de Daniel: dejar por escrito qué palancas mueven la venta del libro **sin improvisar**, qué autoriza el repo y qué no.
>
> Fuente de verdad: `ceo-vista-completa-v2-1-mayo-2026.md` (§3.4, §6.3 palanca 3, §8, §9.4) + `mailerlite-automation-lectores-engranajes-cap3.md` (§1-§5). Toda afirmación de abajo cita el sitio re-verificable. Nada propuesto de memoria.

---

## 0 · Encuadre (no negociable)

El repo **no define el libro como producto de venta directa en Amazon**. Lo define como **activo dormido / puerta inversa al ecosistema** (`ceo-vista-completa` §3.4: *«activo dormido»*, §6.3 palanca 3: *«activar el libro como puerta inversa»*). La estrategia escrita es: libro → capítulo gratis → email → newsletter «Te escribo».

Traducción operativa: **«vender más» = meter tráfico cualificado al capítulo gratis**, no trucos Amazon. El motor de conversión a compra ya está diseñado y es el Email D7 de la automation Cap III (`mailerlite-automation-lectores-engranajes-cap3.md` §3.3), que enlaza el libro real en `https://www.amazon.es/dp/B0FR8PSQT3`.

---

## 1 · Estado verificado a 15 may 2026

| Elemento | Estado | Fuente |
|---|---|---|
| Libro publicado en Amazon (`B0FR8PSQT3`) | ✅ vivo | `…engranajes-cap3.md` §3.3 |
| PDF lead magnet Cap III (23 págs) | ✅ en repo | §5 |
| Landing `/libro/capitulo-3/` + función Netlify + GA4 `cap3_lead_capture` | ✅ desplegado (PR #149) | §5 · cierre §2 |
| Copy de los 3 emails (D0/D3/D7) | ✅ escrito **verbatim** en el repo | §3.1-§3.3 |
| Grupo MailerLite | ✅ creado y renombrado `Lead · Libro Engranajes · Cap 3 gratis` (id `187351536193505006`) | MCP 15 may |
| Automation 3 emails (`Secuencia · Lectores Cap 3 Engranajes`, id `187569220715808525`) | ✅ creada vía MCP, copy dentro · `enabled: false` | MCP 15 may |
| **Activación + env var Netlify** | ❌ pendiente solo de Daniel (1 clic Activar + env var) | — |

**Consecuencia:** la automation ya existe con todo el copy dentro, pero `enabled: false`. Hasta que Daniel pulse **Activar** y la env var Netlify apunte al id del grupo, **el motor sigue apagado**: quien descarga el Cap III no recibe el D7 que vende el libro. Por eso la Palanca 0 precede a todo.

---

## 2 · Palanca 0 · Encender el motor (bloquea todo lo demás)

La automation `Secuencia · Lectores Cap 3 Engranajes` (id `187569220715808525`) ya está **creada vía MCP con los 3 emails dentro** (D0 inmediato · +3 d · D3 · +4 d · D7, copy verbatim, D7 con 2 caminos). Falta solo, y **solo desde ordenador** (MailerLite bloquea edición móvil app+navegador; MCP/API no puede activar ni marcar completo — verificado 15 may, no reintentar por API): (1) marcar los 3 emails como **Hecho** en el editor y pulsar **Activar**; (2) env var Netlify `MAILERLITE_GROUP_LEAD_ENGRANAJES_CAP3` = `187351536193505006` (esto sí desde móvil); (3) test E2E (`…engranajes-cap3.md` §2.4). Lo demás verificado OK por dry_run; el toggle Status es 2 min en escritorio.

Hasta que el test E2E (§2.4) dé verde —email D0 en <60 s, suscriptor en el grupo, evento GA4— **no escalar tráfico**.

---

## 3 · Palancas documentadas · ejecutables desde el móvil (en orden)

Solo después de Palanca 0:

1. **Comparte el capítulo gratis, no el link de Amazon.** En bio Instagram, «destacado», Featured de LinkedIn, comentario fijado + descripción de YouTube (mayor audiencia: 10,1K, `ceo-vista-completa` §1). URL: `twimproject.com/libro/capitulo-3/`. Capta email *y* vende vía D7 = «puerta inversa» (`ceo-vista-completa` §6.3 palanca 3).
2. **Nota corta a la lista actual** desde la app MailerLite. Quien ya te lee es el mejor comprador (lógica `ceo-vista-completa` §3.3). Pieza breve → al capítulo gratis (no Amazon directo).
3. **Recicla un carrusel del juez interno** con CTA al Cap III. El repo autoriza reciclar carruseles; **prohíbe explícitamente vídeo largo de YouTube** (`ceo-vista-completa` §8). Mantente en ese carril.
4. **Descripciones de podcast** (plantilla en `documentos-internos/plantillas/podcast/descripcion-youtube-spotify.md`): incluir el link del capítulo gratis como superficie estable ya existente.

### Métricas a vigilar (lunes, no a diario) — cotas del repo §4

| Métrica | Cota mes 1 | Cota mes 3 |
|---|---|---|
| Open rate D0 | ≥60 % | ≥70 % |
| Click D0 → PDF | ≥50 % | ≥65 % |
| Click D7 → newsletter/programa | ≥8 % | ≥15 % |
| Conversión visitante → lead (`cap3_lead_capture`) | ≥15 % | ≥25 % |
| **Compras del libro en Amazon atribuibles** | **≥2/mes** | **≥10/mes** |

El repo trata el libro como puerta de audiencia, no como fuente de ingresos: la cota temprana es solo ≥2 ventas/mes. No medirlo como si fuera el producto estrella.

---

## 4 · Lo que el repo NO autoriza · silencio documentado

**No existe en el repo ningún plan Amazon-nativo.** No hay nada escrito sobre:

- Amazon Ads (Sponsored Products).
- Promociones de precio / Kindle Countdown Deals / gratis temporal.
- Estrategia de generación de reseñas.
- A+ Content / Author Central / página de autor.
- KDP Select / Kindle Unlimited.

Son palancas estándar de KDP, pero la **regla de método prohíbe improvisarlas**. No se ejecuta ninguna sin decidirla y escribirla antes (regla simétrica del `CLAUDE.md`).

---

## 5 · Decisión pendiente para Daniel

> ¿Se abre una línea de trabajo **Amazon-nativa** (Ads + reseñas + Author Central + precio), o el libro se mantiene estrictamente como puerta inversa al ecosistema durante los próximos 6 meses?

- **Mantener puerta inversa** (coherente con `ceo-vista-completa` §6.3 y §8: disciplina sobre dispersión). Recomendación por defecto del repo.
- **Abrir Amazon-nativo**: decisión nueva. Requiere doc propio con presupuesto, antes de tocar nada.

Hasta que Daniel decida, **solo Palancas 0-3**. Esta sección queda abierta a propósito: no se rellena con intuición.

---

## 6 · Refs

- `documentos-internos/mailerlite-automation-lectores-engranajes-cap3.md` · §1 (3 pasos manuales), §2 (setup + test E2E), §3.1-§3.3 (copy verbatim D0/D3/D7), §4 (métricas), §5 (PDF/landing/función/GA4).
- `documentos-internos/ceo-vista-completa-v2-1-mayo-2026.md` · §3.3 (newsletter como eje), §3.4 (libro activo dormido), §6.3 palanca 3 (puerta inversa), §8 (prohibido vídeo largo YT), §9.4 (sin página rica del libro).
- `documentos-internos/cierre-sesion-2026-05-15.md` · §2 PR #149 (Cap III en producción).
- ASIN libro: `B0FR8PSQT3` → `https://www.amazon.es/dp/B0FR8PSQT3`.
