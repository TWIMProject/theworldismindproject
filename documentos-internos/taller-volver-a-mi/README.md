# Taller «Volver a Mí» · carpeta operativa interna

> Carpeta creada el **13 may 2026** en sesión `claude/improve-proposal-quality-pq3d9` a partir del dossier que Daniel pegó en chat el mismo día. Su función es **dejar la verdad operativa del taller en el repo** según la regla inviolable del CLAUDE.md, para que ninguna sesión futura (humana o IA) opere desde memoria de chat.
>
> Estado del taller: producción avanzada · lanzamiento previsto **8 jun 2026** · precio **697 €** · 12 piezas operativas pendientes de Daniel (ver §3).

---

## 1 · Mapa de archivos

| Archivo | Contenido | Estado |
|---|---|---|
| `README.md` | Este índice | ✅ |
| `dossier-completo.md` | Dossier verbatim que Daniel pegó en chat (identificación, marco conceptual, posicionamiento, audiencia, producción, identidad visual, normas) | ✅ |
| `guion-sesion-01.md` | Guion narrativo verbatim de la primera sesión (75-90 min) generado por ChatGPT con base en Kernberg, con anexos sobre manejo de situaciones, honestidades, investigación de contexto | ✅ |
| `marco-conceptual.md` | Los tres conceptos propios (hambre de mirada, self hambriento, Juez Interno) con cruce a libro `Tu valor no está en su mirada` y a manuscrito del libro `Los Engranajes de la Mente` | ✅ |
| `normas-inviolables.md` | Reglas profesionales y editoriales que cualquier entregable del taller debe cumplir | ✅ |
| `piezas-pendientes.md` | Las 12 decisiones operativas que Daniel necesita confirmar antes de publicar landing y abrir pre-venta | ⚠️ esperando input Daniel |
| `mailerlite-api-incidencia.md` | Documentación del problema técnico que bloquea la captación vía formularios web | ⚠️ esperando datos del informe técnico de ChatGPT |

---

## 2 · Lo que NO está aquí todavía (se sube cuando Daniel lo pase)

Estos artefactos los tiene Daniel pero aún no están en el repo:

- **Landing HTML completa** del taller (mencionada en el dossier §6).
- **3 PDFs preparatorios** con diseño de marca, organizados por bloques temáticos.
- **Logo Mind World Project procesado** para fondos claros y oscuros (.svg).
- **Análisis comparativo asíncrono vs sincrónico** para dependencia emocional.
- **Benchmarks de precio** en mercado español.
- **Proyecciones de conversión** para el lanzamiento.
- **Informe técnico** sobre la incidencia MailerLite API (Daniel dice que existe).

Cuando Daniel los pase (o los vuelque desde otro espacio), van a:

```
documentos-internos/taller-volver-a-mi/
  ├── analisis-comparativo-asincronico-sincronico.md
  ├── benchmark-precios-mercado-espanol.md
  ├── proyecciones-conversion.md
  └── mailerlite-api-incidencia.md  ← se completa con datos del informe técnico

talleres/volver-a-mi/                ← landing pública (no se crea hasta tener §3 cerrado)
  ├── index.html
  └── assets/
      ├── logos/
      └── pdfs-preparatorios/
```

La landing pública en `/talleres/volver-a-mi/` **no se crea hasta que Daniel confirme las 12 piezas pendientes del §3**, para evitar publicar una landing con placeholders falsos (plazas, fechas, modalidad indeterminada — eso sería peor que no tener landing).

---

## 3 · Las 12 decisiones operativas que bloquean el lanzamiento

Detalle completo en `piezas-pendientes.md`. Resumen para ojeada rápida:

1. Plazas del grupo cerrado (recomendado 6-10 para sincrónico).
2. Número total de sesiones.
3. Duración de cada sesión.
4. Modalidad: presencial Valencia · online · mixto.
5. Día y hora de las sesiones.
6. Estructura: semanal · quincenal · intensiva fin de semana.
7. ¿Sesión individual incluida en el precio?
8. Material entregable post-taller (grabaciones · PDFs adicionales · comunidad).
9. Política de devolución.
10. ¿Selección o filtrado previo de participantes?
11. Email de contacto específico o canalizado por el general.
12. ¿Segunda edición prevista y cuándo?

A esos 12 yo añadiría dos más críticos por estrategia (ver `piezas-pendientes.md` §2):

13. **Estrategia de captación** (canales): newsletter + IG + Meta Ads + colaboraciones · qué priorizamos en los 26 días previos al 8 jun.
14. **Métrica de éxito vs mínimo viable**: cuántas plazas se necesitan para considerar lanzamiento exitoso vs cuándo se posterga.

---

## 4 · Relación con otros activos del repo

- **Libro en desarrollo**: `documentos-internos/libro-tu-valor-no-esta-en-su-mirada/` (manuscrito limpio del 11 may + revisión temario) trabaja exactamente el mismo cuadro psíquico que el taller. Pueden venderse juntos o cross-sellearse.
- **Programa «Deja de Buscarte en Otros»**: `documentos-internos/programa-deja-de-buscarte-en-otros/` está estructurado (briefing, currículo, módulos, workbook, protocolo 21 días, stripe, email confirmación). Es el producto digital asíncrono del mismo eje. Decisión estratégica de Daniel del 13 may: priorizar Volver a Mí ahora, grabar Deja de Buscarte como tope agosto.
- **Lead magnet activo del libro Engranajes**: `libro/capitulo-3/` + automation MailerLite «Lectores · Engranajes Cap3» (PR #149 mergeado el 13 may). Su Cap III es sobre el Juez Interno = mismo concepto central del taller. **El lead magnet del libro es el primer escalón natural del embudo del taller.**
- **Sprint editorial activo semana 19 may**: Carta #2 «La voz que te juzga» (`contenido-rrss/te-escribo-newsletters/carta-02-la-voz-que-te-juzga.html`) + Carrusel #3 «5 frases del juez interno» (`contenido-rrss/te-escribo-voz-que-te-juzga/`). **Toda esa publicación es ya regado del terreno para el taller.**

---

## 5 · Inconsistencias detectadas entre el dossier de chat y el repo

> Marcadas para que la próxima sesión no las propague.

| Dossier ChatGPT dice | Repo dice (verdad operativa) | Acción |
|---|---|---|
| Newsletter TWIM «Cartas desde el diván» | Newsletter «Te escribo» (`contenido-rrss/te-escribo-newsletters/`) | Usar **Te escribo** en cualquier entregable del taller |
| Daniel «especialista en psicoanálisis…» | Mismo en CLAUDE.md + landing libro | ✅ consistente |
| Logo «Mind World Project» | Logo `logo-mindworld.png` en root del repo | ✅ consistente |
| Tipografía DM Serif Display + DM Sans | `instagram-sistema-visual-marca.md` §3.2: **Instrument Serif + Barlow Condensed** | **Discrepancia importante** — resolverla con Daniel antes de maquetar la landing pública (ver §3 piezas-pendientes) |
| Paleta cromática «exacta de twimproject.com, variables CSS documentadas» | `CLAUDE.md` + `instagram-sistema-visual-marca.md` §3.1: `#173D30 / #265C4B / #C2A78B / #FDFCFA` | ✅ consistente (asumiendo que la twim-styles.css usa esos tokens) |

---

## 6 · Próximos pasos sugeridos (cuando Daniel vuelva de pacientes)

1. Pasar los 7 artefactos faltantes del §2 (PDFs, landing HTML existente, logos, análisis, benchmarks, proyecciones, informe técnico MailerLite).
2. Contestar las 14 preguntas de `piezas-pendientes.md`.
3. Resolver la incidencia MailerLite (probablemente regenerar `MAILERLITE_API_KEY` y actualizar en Netlify).
4. Resolver la discrepancia tipográfica del §5.
5. Decisión estratégica clave: ¿lanzamiento 8 jun confirmado o pre-venta con criterio de validación al 1 jun? (Recomendación de la sesión: pre-venta. Detalle en el chat del 13 may.)

Cuando tengamos 1-5 resueltos, se crea la landing pública en `talleres/volver-a-mi/` con datos reales, se programa la campaña de captación de los días restantes y se activa pre-venta.

---

**Última actualización:** 13 may 2026 · sesión `claude/improve-proposal-quality-pq3d9` · pendiente de input de Daniel para completar §2 y §3.
