# Métricas Carrusel #2 «Saberlo no te lo quita» · 12 may 2026

> Documento de revisión de rendimiento creado el **13 may 2026 ~10:00 CEST** (≈15-16 h después de la publicación). Sucede a las capturas de Meta Business Suite compartidas por Daniel en sesión `claude/improve-proposal-quality-pq3d9`.
>
> Función: dejar por escrito qué pasó con el Carrusel #2, contra qué se compara, cuáles son las causas más probables del rendimiento por debajo de lo esperado, y qué cambia en el Carrusel #3 a partir de esto. Para que la próxima sesión opere sobre datos reales y no sobre intuición.
>
> Pieza analizada: distribución multicanal documentada en `contenido-rrss/te-escribo-newsletters/PLAN-CAPTACION-30D.md` §6 (12 may 2026 · IG + FB · 19:00 CEST).

---

## 1 · Datos crudos a 24 h (lectura del 13 may ~10:00 CEST)

### 1.1 · Instagram

| Métrica | Valor |
|---|---|
| Visualizaciones | **1.207** |
| Alcance | **625** |
| Interacciones totales | **19** |
| Me gusta y reacciones | 12 |
| Comentarios | **0** |
| Veces compartida | 2 |
| Veces guardada | 5 |
| Seguidores nuevos atribuibles | **0** |

**Curva de visualizaciones** (gráfico Meta Business Suite):
- Línea «esta publicación» (azul): de 0 a ~1.200 entre 0 h y 1 d 6 h.
- Línea «habitual de tu publicación» (gris): de 0 a ~3.000 en 7 días.
- Lectura: a 24 h estamos en ~40-50 % de la curva habitual de tu cuenta. La proyección a 7 días apunta a ~1.500-2.000, es decir ~50-67 % del rendimiento habitual del feed.

### 1.2 · Facebook

| Métrica | Valor |
|---|---|
| Visualizaciones | **3** |
| Espectadores | 3 |
| Interacciones | 1 (1 share, 0 likes, 0 comentarios, 0 saves) |
| Clics en enlaces | — |
| Seguidores nuevos | 0 |

**Lectura:** 3 views no es «bajo rendimiento orgánico», es **fallo técnico o de configuración** del cross-post automático Meta Business Suite → Página FB. La página de Facebook de TWIM no está recibiendo distribución real, o el formato carrusel no se está publicando como tal en FB. Acción: verificar antes de programar Carrusel #3 (§6.6).

### 1.3 · Audiencia (Instagram)

| Dimensión | Valor | Comparativa baseline orgánico 12 may |
|---|---|---|
| Mujeres | **81,6 %** | 60,1 % |
| Hombres | **18,4 %** | 39,9 % |
| 25-34 | ~27 % | 38,0 % |
| 35-44 | ~35 % | 24,7 % |
| 45-54 | ~8 % | 17,7 % |
| 55-64 | ~6 % | 8,9 % |
| 18-24 + 65+ | ~3 % | ~10,7 % |

**Sesgo principal:** la audiencia que vio el carrusel está **+21 puntos por encima en mujeres** y **+10 puntos por encima en franja 35-44** respecto a la base orgánica de la cuenta. El algoritmo no distribuyó al perfil orgánico real, sino al subconjunto «mujer 35-44 emocional». Este sesgo contradice la implicación operativa §3 del baseline (`metricas-audiencia-ig-baseline-12-may-2026.md`): *«No caricaturizar copy hacia "mujer 45 con dependencia emocional". La audiencia es más amplia. Voz editorial transversal.»*

---

## 2 · Comparativa contra benchmark declarado (instagram-sistema-visual §13.1)

| Métrica | Real Carrusel #2 | Cota mes 3 declarada | Cota mes 12 declarada | Brecha |
|---|---|---|---|---|
| Save rate (saves / impresiones) | 5/1.207 = **0,41 %** | **>2 %** en carruseles A | >4 % | **5× por debajo del mes 3** |
| Share rate | 2/1.207 = **0,17 %** | **>1 %** | >2 % | **6× por debajo del mes 3** |
| Conversión visitante perfil → click bio | 0 (sin attribución) | >5 % | >10 % | No medible este post |
| Suscriptores newsletter atribuibles a IG | 0 (sin UTM separable de stories) | +20/mes | +100/mes | No medible este post |
| % contenido en marca (capa A1) | 100 % (pieza en marca) | >90 % | 100 % | ✅ cumple |

**Único KPI que cumple:** el de marca (la pieza ES sistema A1). Todos los KPIs de **rendimiento** están por debajo, los dos críticos (save/share) por **5-6× la cota objetivo de mes 3**.

---

## 3 · Comparativa contra Reel del 9 may (mismo embudo, pieza inmediata anterior)

> Datos del Reel del 9 may sacados de `contenido-rrss/te-escribo-newsletters/REACCION-9-MAYO.md` §2.1. Solo parte orgánica IG (no incluye lo que aportaron los ads concurrentes).

| Métrica | Reel 9-may IG | Carrusel #2 12-may IG | Lectura |
|---|---|---|---|
| Visualizaciones | 1.686 | 1.207 | Reel +40 % |
| Alcance | 1.148 | 625 | Reel +84 % |
| Likes | 47 | 12 | Reel +291 % |
| Comentarios | 4 | **0** | Reel mejor |
| Shares | 1 | 2 | Carrusel +1 |
| Saves | 1 | **5** | **Carrusel +400 %** ← única ventaja |
| Follows atribuibles | n/d (combinado con ads) | **0** | — |

**Lectura cruzada:** el carrusel rinde mejor donde un carrusel **debe** rendir mejor (saves: contenido archivable). Pero rinde peor donde un carrusel también debería competir contra reel (alcance, likes, comentarios). Como métrica primaria de los carruseles A1 declarada en `instagram-sistema-visual §13.2` es **saves+shares, no likes**, el carrusel #2 supera al reel en saves pero solo lo iguala en shares — y sigue 5× por debajo del benchmark propio en saves.

**Conclusión honesta:** comparado con el reel anterior, el carrusel #2 no es desastre absoluto, es **infrarrendimiento del formato carrusel respecto a su techo declarado**. El problema no es que «los carruseles no funcionen», es que esta pieza concreta no activó la palanca específica del carrusel (saves a tope) ni la de reel (alcance/likes).

---

## 4 · Causas probables (contraste con docs del repo, no opinión)

### 4.1 · Hook abstracto-conceptual en lugar de diagnóstico/lista/escena

Slide 1 actual: **«El insight no cura. Lo que cura es vivir lo que entiendes.»**

Patrón hook de los carruseles A1 que sí performan en tu propio feed (referenciados en `instagram-sistema-visual-marca.md` §1.1):

| Carrusel | Tipo de hook |
|---|---|
| «Tu cansancio no es físico» | Diagnóstico desmentido («X no es Y») |
| «5 señales de que buscas validación» | Lista numerada |
| «Si alguna vez has sentido un vacío» | Escena identificable |

**El aforismo es buen cierre, mal hook en IG.** La función del slide 1 a 1,5 segundos de scroll no es resumir tu tesis editorial, es plantear un dolor identificable. «El insight no cura» es perfecta como **slide pivote** o **slide final**, no como entrada.

### 4.2 · Caption IG sin pregunta de cierre ni CTA explícita

Comparativa entre los tres canales del mismo carrusel:

| Canal | ¿Pregunta abierta de cierre? | ¿CTA a `/newsletter/`? | ¿Hashtags? |
|---|---|---|---|
| LinkedIn (caption-linkedin.txt) | ✅ «¿Te has visto en este punto alguna vez — sabiendo perfectamente lo que te pasa y aun así repitiendo el patrón?» | ❌ implícito en bio | 5 |
| X (thread-x.txt, tweet 7) | ✅ + PD a newsletter explícita | ✅ `twimproject.com/newsletter` en PD | n/a |
| **Instagram (caption-instagram.txt)** | ❌ cierra con «Vivirlo, no leerlo. — Daniel» | ❌ ningún link a newsletter | **14** (demasiados) |

**La caption IG está infra-utilizada respecto al material del que ya disponías.** El thread X y el LinkedIn cierran con pregunta + CTA; la caption IG no. Resultado coherente con la métrica: 0 comentarios y 0 follows.

### 4.3 · Cero warm-up de Stories del carrusel antes de las 19:00

Según `PLAN-CAPTACION-30D.md` §6: la Story «Recado 01» publicada a las 14:30 CEST apuntaba al **link de la newsletter** (`/newsletter/`), no al carrusel del feed. El carrusel se publicó «en frío» a las 19:00 sin teaser previo en stories propias.

El alcance inicial de un carrusel depende mucho del share del propio creador en stories en las primeras 2 h post-publicación: sin esa señal, el algoritmo solo prueba el feed y el techo de distribución se queda en el «alcance habitual» de la cuenta menos un buffer. Esto es consistente con que el alcance esté en ~50 % de la curva habitual.

### 4.4 · Horario 19:00 CEST cuando el pico documentado es 20:00 CEST

`metricas-audiencia-ig-baseline-12-may-2026.md` §1.4 documentó el 12 may a las ~12:00 CEST que la hora pico declarada por Meta para tus seguidores esta semana es **20:00**. La decisión de mantener 19:00 fue consciente (`PLAN-CAPTACION-30D.md` §6, *«mantener 19:00 por comparabilidad con Carrusel #1»*) y la hipótesis del cambio a 20:00 quedó aparcada para el Carrusel #3. Esto sigue siendo una decisión correcta editorialmente para tener serie comparable, pero **es una causa contributiva** al techo de alcance.

---

## 5 · Lo que NO se concluye

- **No** «el contenido es malo». El concepto «comprender ≠ elaborar» es de los más sólidos del repertorio editorial. La pieza es buena editorialmente, mal envasada para IG.
- **No** «los carruseles no funcionan». La métrica primaria del carrusel A1 (saves) supera al reel del 9 may, aunque siga lejos del benchmark propio.
- **No** «hay que cambiar la voz editorial». La voz funciona y está fija en CLAUDE.md y CEO §2. Lo que falla es el *packaging IG*: hook + caption + CTA + warm-up. Tres piezas operativas, no la voz.
- **No** «hay que abandonar el sistema visual A1». El sistema visual cumple. La pieza está 100 % en marca. El problema no está en cómo se ve, está en qué dice el slide 1 y qué dice la caption.

---

## 6 · Plan operativo para Carrusel #3 (semana 18-25 may)

Cada acción de esta sección está pensada como **variable aislada** para que el Carrusel #3 sirva como test contra el #2. No se cambia todo a la vez sin criterio: se cambian las palancas que el diagnóstico §4 señala como causas, se mantiene el resto.

### 6.1 · Hook diagnóstico/escena en slide 1

Patrón obligatorio para slide 1 del Carrusel #3:

- Diagnóstico desmentido: *«X no es Y, es Z.»*
- Lista numerada: *«N señales de…»*
- Escena identificable: *«Si alguna vez te ha pasado…»*

Aforismos editoriales («el insight no cura») se reservan al **slide pivote** (slide 3-4) o al **slide de cierre antes del CTA**.

### 6.2 · Caption IG con estructura completa

Plantilla obligatoria para la caption del Carrusel #3:

```
[Hook · 1 frase, repite o reformula el slide 1]

[Cuerpo · 4-6 frases, mismo cuerpo del LinkedIn adaptado]

[Pregunta abierta · 1 frase, copia literal de la pregunta del LinkedIn]

[CTA · 1 frase con URL completa]
→ twimproject.com/newsletter

— Daniel

[6-8 hashtags max, no 14]
```

La pregunta de cierre de LinkedIn y la PD del thread X **se reusan literalmente** en la caption IG. No se reescribe lo que ya funciona.

### 6.3 · Slide CTA visible con URL

Slide final del Carrusel #3 incluye:

- Kicker beige: «TE ESCRIBO».
- Frase central Instrument Serif: cierre aforístico (aquí sí, aforismo encaja).
- URL destacada Barlow Condensed Bold beige: `twimproject.com/newsletter`.
- Footer estándar: `@daniorozcopsicologo · twimproject.com`.

Hoy el slide final del #2 cierra con «Comprender no es lo mismo que elaborar» sin URL al newsletter en la propia imagen — solo el handle. Pasa desapercibido.

### 6.4 · 2 stories de teaser + 1 story de share post-publicación

- **24 h antes** (lunes 18 may por la tarde): story con frase del slide pivote del Carrusel #3 + sticker «mañana 20:00».
- **2 h antes** (martes 19 may ~18:00): story con slide 1 del Carrusel #3 + sticker recordatorio.
- **30-60 min después de publicar**: story re-share del propio post con frase de invitación a comentar.

Las 3 stories tienen sticker link a `/newsletter/` con UTMs separados (`utm_campaign=teaser-d-1`, `teaser-d0-pre`, `share-d0-post`).

### 6.5 · Test horario 20:00 CEST (cumplir hipótesis baseline §4)

Programar Carrusel #3 a las **20:00 CEST** del martes 19 may (no 19:00). Esto cumple la hipótesis pendiente del baseline §4 y da serie de tres puntos:

| Pieza | Hora | Día semana |
|---|---|---|
| Carrusel #1 «Saberlo no te lo quita» | 19:00 | Martes |
| Carrusel #2 (12 may) | 19:00 | Martes |
| **Carrusel #3 (19 may)** | **20:00** | **Martes** |

Si el Carrusel #3 mejora >20 % en alcance respecto al promedio #1+#2 con todo lo demás también cambiando, no podremos atribuir el delta solo al horario — pero sí podremos descartar la hipótesis si el alcance NO mejora pese a tener mejor hook + caption + warm-up.

### 6.6 · Verificar cross-post FB manualmente

Antes de programar el #3 en Meta Business Suite:

- Entrar a la Página FB de TWIM y comprobar visibilidad del Carrusel #2 (3 views es síntoma, no causa). Posibles causas: la página tiene 0 alcance orgánico estable, el carrusel se publicó como foto única en lugar de álbum, o el cross-post está marcado como «no recomendado» por FB.
- Si la causa es la página dormida: aceptar que FB no es canal de tracción y dejar de cross-postear (no malgasta esfuerzo, simplemente se retira de la métrica).
- Si la causa es el formato álbum: programar IG y FB **por separado** desde MBS (publicación nativa cada uno), no usar el cross-post automático.

### 6.7 · Auditoría de métricas a 7 días, no a 24 h

El save rate de carruseles A1 es métrica de cola larga: el lector guarda cuando vuelve, no en la primera pasada. La revisión final del Carrusel #2 se hace el **lunes 19 may por la mañana** (7 días vivo) y se anota en §7 de este mismo documento. La decisión sobre si la pauta de mejoras §6.1-§6.6 funciona se toma con datos de 7 días del #2 vs datos de 7 días del #3 (no antes).

---

## 7 · Revisión a 7 días · placeholder (rellenar 19 may ~10:00 CEST)

```
Fecha de captura: __________
Visualizaciones IG a 7 días: __________
Alcance IG a 7 días: __________
Saves a 7 días: __________ (save rate: ____ %)
Shares a 7 días: __________ (share rate: ____ %)
Likes a 7 días: __________
Comentarios a 7 días: __________
Follows atribuibles a 7 días: __________
Visualizaciones FB a 7 días: __________ (¿se confirma fallo técnico?)

Lectura honesta a 7 días:
__________

Decisión sobre §6.1-§6.7 (mantener / ajustar / revertir):
__________
```

---

## 8 · Hipótesis a validar con el Carrusel #3

Si el Carrusel #3 con las 7 acciones de §6 aplicadas:

- **Supera 30 % al #2** en saves+shares combinados a 7 días → confirmamos que la causa principal del bajo rendimiento del #2 era el packaging (hook + caption + warm-up + horario), no el contenido.
- **No supera al #2** o lo iguala → la causa es estructural (algoritmo IG decodifica el formato verde como nicho femenino emocional saturado, o la cuenta tiene techo orgánico actual ~600-1.200 alcance por carrusel sin Ads). En ese caso, replantear: o se acepta el techo y se compensa con cadencia (3 carruseles/semana en lugar de 1) o se introduce Meta Ads sobre el carrusel a 5 €/día.

Esa decisión se toma el **lunes 26 may** con datos de 7 días del Carrusel #3 sobre la mesa.

---

## 9 · Acciones derivadas inmediatas

- [ ] **13 may:** Daniel añade entrada en `PLAN-CAPTACION-30D.md` §6 con resumen de 24 h del Carrusel #2 + link a este doc. (Hecho en este mismo PR.)
- [ ] **14-17 may:** producir Carrusel #3 con plantilla §6 — hook diagnóstico/escena, caption con pregunta + CTA, slide CTA con URL, 2 stories teaser planificadas.
- [ ] **18 may por la tarde:** publicar story teaser día -1.
- [ ] **19 may ~10:00:** rellenar §7 de este doc con datos a 7 días del Carrusel #2.
- [ ] **19 may ~18:00:** publicar story teaser pre-publicación.
- [ ] **19 may 20:00:** publicar Carrusel #3 a las 20:00 CEST (test horario).
- [ ] **19 may ~21:00:** publicar story re-share post-publicación.
- [ ] **20 may ~10:00:** captura de métricas a 14 h del Carrusel #3 (referencia rápida vs el #2 a 14 h).
- [ ] **26 may ~10:00:** crear `metricas-carrusel-3-[slug]-19-may-2026.md` con datos a 7 días + decisión sobre §6 según hipótesis §8.

---

## 10 · Cómo se capturó

- Daniel comparte el 13 may ~10:00 CEST cuatro capturas de Meta Business Suite (`business.facebook.com/latest/insights/object_insights/`) del Carrusel #2 publicado el 12 may 19:00 CEST. Tres capturas son del post Instagram (asset_id `1113734008481690`, content_id `18092296088350404`), una del post Facebook (content_id `122106561110692022`).
- Audiencia baseline contrastada con `documentos-internos/metricas-audiencia-ig-baseline-12-may-2026.md` (capturado el mismo día 12 may ~12:00).
- Comparativa Reel 9-may extraída de `contenido-rrss/te-escribo-newsletters/REACCION-9-MAYO.md` §2.1.
- Benchmarks contrastados con `documentos-internos/instagram-sistema-visual-marca.md` §13.1 (cotas mes 3 y mes 12).
- Sin acceso vía API a Meta Business Suite (host bloqueado en sandbox según CLAUDE.md): toda la lectura se hace sobre las capturas + repo.

---

**Última actualización:** 13 may 2026 ~10:00 CEST · sesión `claude/improve-proposal-quality-pq3d9` · revisión a 7 días pendiente para 19 may.
