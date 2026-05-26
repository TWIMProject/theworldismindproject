# Briefing Meta Ads · Carrusel #4 «Hambre de mirada» → lista espera Volver a Mí

> Documento operativo creado el **26 may 2026 22:15 hora Madrid**. Función · dejar por escrito todo el setup del próximo anuncio Meta Ads para que su lanzamiento sea reproducible, su medición sea verificable y la decisión de escalar/cortar sea binaria.
>
> Decisión origen · Daniel verbatim 26 may 22:00 «Estoy convencido» (sobre aplicar el aprendizaje del post viral del niño con objetivo correcto). Destino confirmado · landing taller Volver a Mí + lista espera.

---

## 1 · Compuerta declarada · excepción acotada

### 1.1 · Regla persistida

Cita textual de `metricas-meta-ads-anuncio-nino-22-may-2026.md` §5 punto 6:

> **Compuerta del CEO doc §7 Decisión 2** · nada de Meta Ads hasta que el orgánico demuestre que el registro convierte. Este anuncio refuerza esa regla · el embudo de captación por email debe estar afinado antes de pagar tráfico.

### 1.2 · Evolución acordada el 26-may

La compuerta **se mantiene como regla general** y se levanta solo para esta excepción acotada · **Ad de calentamiento de lista**, no de venta. Criterios que justifican la excepción:

| Criterio | Estado |
|---|---|
| El embudo de email está afinado (form → MailerLite → secuencia bienvenida) | ✅ verificado · `/.netlify/functions/subscribe` → grupo `pre-venta-volver-a-mi` (`188015567896052961`) |
| El creativo nuevo (Carrusel #4 A2 + foto IA) ya rompe expectativa del algoritmo | ✅ publicación orgánica miércoles/jueves esta semana |
| El destino es coherente con el creativo (taller → landing taller) | ✅ no hay bait-and-switch (lección §5.3 doc niño) |
| El presupuesto es bajo (cap experimental) | ✅ 50 € total / 5 días / 10 €/día |
| El KPI es de captación, no de venta | ✅ leads a lista espera, no compras |
| Hay fecha de revisión binaria escalar/pausar | ✅ 3-5 días, ver §7 |

### 1.3 · Lo que esta excepción NO autoriza

- Lanzar anuncios sin objetivo de tráfico definido (regla §5 punto 1 doc niño).
- Anuncios con destino «Perfil» o «Combinación optimizada» (regla §5 punto 1).
- Escalar presupuesto sin revisión a 3 días.
- Lanzar Ads de venta del taller antes de la apertura de pre-venta dura del **1 sep 2026** (calendario inviolable).
- Ignorar las 6 lecciones del §5 del doc del niño.

---

## 2 · Configuración del anuncio

| Variable | Valor |
|---|---|
| **Objetivo de campaña** | **Tráfico** (no «Combinación optimizada» · regla §5.1 doc niño) |
| **Destino** | **Sitio web** (no «Perfil») |
| **URL destino** | `https://twimproject.com/talleres/volver-a-mi/?utm_source=meta&utm_medium=cpc&utm_campaign=hambre-mirada-cal&utm_content=carrusel-4` |
| **Botón CTA** | «Más información» |
| **Formato creativo** | Carrusel (8 slides) |
| **Creativo** | Carrusel #4 «Hambre de mirada» · sistema A2 crema + foto IA · `carrusel-hambre-de-mirada/slide-1-hook.png` a `slide-8-newsletter.png` |
| **Presupuesto total** | **50 €** (cap experimental) |
| **Duración** | 5 días (10 €/día) |
| **Pujas** | Automáticas |
| **Pacing** | Estándar (no acelerado) |
| **Ubicaciones** | Facebook Feed + Instagram Feed + Instagram Explore (excluir Reels, Stories y Audience Network) |

### 2.1 · Audiencia (acotada)

| Variable | Valor | Razón |
|---|---|---|
| Sexo | **Mujer** | Audiencia objetivo del taller. Hombre = -90 % conversión esperada. |
| Edad | **28-52** | Lección §5.4 doc niño (audiencia 55+ se llevó 33 % del gasto sin ser público objetivo). |
| Ubicación | **España** + (opcional) Argentina + México | España = 95,6 % alcance del post viral del niño · ya validado |
| Idioma | Español | — |
| Intereses (selección por orden de afinidad) | Psicología · Autoestima · Dependencia emocional · Mindfulness · Salud mental · Recalcati · Lacan · Anabel González · Carl Jung | Acotar para evitar dispersión |
| Excluir | Públicos compradores del libro (si Meta Pixel los identifica) | Evitar pagar por audiencia que ya es lead |

### 2.2 · Copy del anuncio (primary text)

Versión A (recomendada · tono Te escribo):

> No es inseguridad.
>
> Es haber aprendido a leer caras antes de hablar. A pedir perdón sin haber hecho nada. A releer un mensaje tres veces antes de enviarlo.
>
> Hay un mecanismo detrás · se montó cuando eras niña, y hoy sigue funcionando solo.
>
> Lo trabajamos en grupo cerrado de 8 mujeres · 8 miércoles · 30 sep a 18 nov 2026.
>
> Apúntate a la lista de espera. Sin pago. Sin compromiso. Solo para saber primero.

Versión B (más directo · si A no rinde):

> Si alguna vez te has dicho «soy demasiado sensible» pero por dentro sabías que no era eso · esto es para ti.
>
> El taller «Volver a Mí» es un grupo cerrado de 8 mujeres con dependencia emocional. Ocho miércoles. Online. 30 sep a 18 nov 2026.
>
> Apúntate a la lista de espera · sin pago, sin compromiso.

### 2.3 · Caption corto / headline

«Hambre de mirada · 3 escenas que no habrás nombrado»

### 2.4 · Description (texto inferior del CTA)

«Lista de espera · sin pago, sin compromiso · twimproject.com»

---

## 3 · Verificación pre-lanzamiento (checklist)

Antes de pulsar Publicar, verificar **todos** los puntos. Si alguno falla · NO lanzar.

- [ ] Carrusel #4 publicado orgánicamente al menos 1 día antes (medir performance orgánica como baseline).
- [ ] Las 8 slides existen en `carrusel-hambre-de-mirada/` y se ven bien en preview de Meta Ads Manager.
- [ ] Landing `https://twimproject.com/talleres/volver-a-mi/` carga sin errores (probar en móvil y desktop · regla §2 inviolable infraestructura).
- [ ] Form de la landing envía email + nombre y devuelve respuesta 200 (probar manualmente con email burner).
- [ ] El email burner aparece en MailerLite grupo `Lead · Pre-venta Volver a Mí` (`188015567896052961`) en < 60 s.
- [ ] La URL de destino incluye los 4 UTM (source / medium / campaign / content) · verificar en GA4 Realtime.
- [ ] Meta Pixel disparando `Lead` event tras submit del form (verificar con Pixel Helper de Chrome).
- [ ] Presupuesto 50 €, duración 5 días, audiencia 28-52 mujer España, objetivo Tráfico, destino sitio web · confirmados en pantalla de revisión.
- [ ] Daniel da OK explícito antes de publicar (regla §2 cambios infraestructurales).

---

## 4 · KPIs y umbrales de decisión

### 4.1 · KPI principal · leads a lista espera

| Métrica | Umbral de éxito | Umbral de pausa |
|---|---|---|
| **Leads totales al grupo MailerLite** (5 días) | ≥ 10 leads = **5 €/lead** o menos | < 5 leads en 3 días = pausar |
| **CPL (coste por lead)** | < 5 € | > 10 € = pausar |
| **CTR (click-through rate)** | > 1 % | < 0,5 % = revisar creativo |
| **CPC (coste por click)** | < 0,50 € | > 1 € = pausar o reajustar audiencia |
| **Tasa form (visitas landing → submit form)** | > 8 % | < 3 % = problema de landing, no de creativo |

### 4.2 · Lectura del anuncio anterior (niño · referencia)

- CPM 3,60 € · razonable
- CPC ≈ 0,12 € · muy bajo
- Toques enlace externo · **2** (problema del objetivo, no del creativo)

Si este anuncio mantiene CPC < 0,50 € y consigue ≥ 10 leads, el rediseño objetivo+destino habrá quedado validado.

---

## 5 · Plan de medición y decisión binaria

| Día | Acción |
|---|---|
| Día 0 (publicación orgánica + lanzamiento Ad) | Marcar inicio. Capturar baseline orgánica del Carrusel #4 a las primeras 12 h (impresiones IG orgánico, sin pagar). |
| Día 1 | Revisar Pixel · ¿se dispara `Lead` event? Si no, debug ANTES de gastar más presupuesto. |
| Día 3 | Auditoría · leads totales, CPC, CTR, CPL. **Si menos de 5 leads · pausar.** Si va bien, dejar correr 2 días más. |
| Día 5 | Cierre del anuncio. Documentar resultados en `metricas-meta-ads-carrusel-4-hambre-mirada-XX-may-2026.md` (estructura paralela al doc del niño). |
| Día 5+ | Decisión binaria · escalar (subir a 30 €/día) si CPL < 5 € · OR · documentar lecciones y no relanzar hasta tener nuevo creativo. |

---

## 6 · Comparativa con anuncio del niño (qué NO repetir)

| Variable | Anuncio del niño (mal) | Anuncio Carrusel #4 (corregido) |
|---|---|---|
| Objetivo de campaña | Combinación optimizada | **Tráfico** |
| Destino | Perfil | **Sitio web** (landing taller) |
| URL destino | (n/a · perfil) | URL con 4 UTMs |
| CTA caption | «Está en Amazon y enlazado en mi bio» | «Apúntate a la lista de espera» |
| Edad audiencia | Abierta (incluía 55+) | **28-52** |
| Resultado de tráfico externo | 2 toques enlace en 13.361 vis | (esperamos) > 10 leads en ~10.000 vis |
| Coherencia creativo→destino | Carrusel «niño» → bio → Amazon | Carrusel «hambre de mirada» → landing taller |
| Gasto | 48,05 € / 75 € (cancelado) | 50 € cap experimental |

---

## 7 · Actualización de la regla en el doc del niño

Tras este lanzamiento, **actualizar** `metricas-meta-ads-anuncio-nino-22-may-2026.md` §5 punto 6 con:

> **Actualización 26-may 2026** · La compuerta se mantiene como regla general (no Meta Ads sin orgánico que convierta). Se abre excepción acotada para **Ads de calentamiento de lista** cuando se cumplen los 6 criterios del §1.2 del doc `setup-meta-ads-carrusel-4-hambre-de-mirada.md`. Esta excepción NO autoriza Ads de venta antes de la pre-venta dura del 1 sep 2026.

---

## 8 · Riesgos identificados y mitigación

| Riesgo | Probabilidad | Mitigación |
|---|---|---|
| Pixel no dispara `Lead` event correctamente | Media | Verificar día 1 con Pixel Helper antes de gastar más |
| Audiencia 28-52 es demasiado amplia y el CPM se dispara | Baja | Acotar más a 32-48 si CPM > 6 € |
| Landing carga lenta en móvil → CR baja | Media | Probar en pre-lanzamiento desde móvil real con 4G |
| Form falla por error Netlify function | Baja | Probar 24 h antes con email burner |
| El creativo A2 + foto IA no resuena en frío (sin contexto orgánico) | Media | Por eso se publica orgánicamente 1 día antes · sirve de prueba |
| Se generan leads pero no se convierten luego en venta de pre-venta | Alta | Es lead frío. Lo trabaja la secuencia bienvenida automation. Si tasa lead→venta < 3 % se replantea el funnel post 1-sept. |

---

## 9 · Próximos pasos (en orden)

1. **Mié 27 o jue 28 may 20:00 hora Madrid** · publicar Carrusel #4 orgánicamente en IG (caption con aforismo + URL canónica · sin Boost).
2. **Mismo día +12 h** · capturar baseline orgánica (impresiones, alcance, saves).
3. **Día siguiente · 09:00** · armar el anuncio en Meta Ads Manager siguiendo §2.
4. **Verificar checklist §3 completo** antes de pulsar Publicar.
5. **Pedir OK explícito a Daniel** antes de pulsar Publicar (regla §2 inviolable infraestructura).
6. **Día +3** · auditoría intermedia. Decisión pausar o seguir.
7. **Día +5** · cierre. Documentar resultados.

---

— Documento operativo. Si el lanzamiento se ejecuta, este doc queda como referencia histórica. Si se descarta, archivar con razón documentada.
