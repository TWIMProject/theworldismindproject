# Checklist · Setup Meta Ads para captación de newsletter

> Documento operativo · 6 mayo 2026
> Implementa el Brief Meta Ads §4 de `contenido-rrss/te-escribo-newsletters/PLAN-CAPTACION-30D.md`.
> Audiencia: Daniel ahora; VA cuando entre (sept 2026).

---

## TL;DR

Meta Ads se activa como **gate condicional** el **21 mayo 2026** si el contador del grupo `newsletter-home` en MailerLite está por debajo de 150 suscriptoras. Presupuesto máximo 35 € (5 €/día × 7 días). Decisión cocida en `PLAN-CAPTACION-30D.md` §4 — no se relitiga, se ejecuta.

**Estado actual:**
- Meta Pixel ID `1447483376992558` configurado y funcionando en `reto-7-dias.html`.
- **Falta cargarlo en el resto del site** (index, landings SEO, /newsletter/).
- **Falta cablear el evento `Lead`** en cross-sell + exit-intent (newsletter_signup).

Tiempo total de setup técnico (código del repo): **2-3 horas**. Setup de la campaña en Meta Ads Manager: **1-2 horas**.

---

## 1 · Estado real del setup

### Lo que ya existe

| Componente | Estado | Ubicación |
|---|---|---|
| Meta Pixel ID `1447483376992558` | Activo | reto-7-dias.html (líneas 543-549) |
| Evento `Lead` para Reto 7 Días | Cableado | reto-7-dias.html línea 810-811 |
| GA4 evento `newsletter_signup` | Activo | assets/te-escribo-exit-intent.js + assets/te-escribo-cta.js |
| UTMs definidas | Sí | PLAN-CAPTACION-30D.md §4.2 y §4.3 |
| Audiencia + creatives + KPIs + stop-loss | Cocidos en plan | PLAN-CAPTACION-30D.md §4.1-§4.4 |

### Lo que falta antes del 21 mayo

| Tarea | Lado | Bloqueante para el ad |
|---|---|---|
| Cargar Meta Pixel en `index.html` | Código (yo lo puedo hacer en PR aparte) | Sí — sin píxel en home no se traquea retargeting |
| Cargar Meta Pixel en 7 landings SEO (`psicologo-*-valencia.html`, etc.) | Código (yo lo puedo hacer en PR aparte) | Recomendado — refuerza dataset del píxel |
| Cargar Meta Pixel en `/newsletter/` | Código (yo lo puedo hacer en PR aparte) | **Crítico** — es la URL de destino del ad |
| Cablear evento `fbq('track', 'Lead')` en cross-sell + exit-intent | Código (yo lo puedo hacer en PR aparte) | **Crítico** — sin esto las conversiones del ad no cuentan |
| Verificar Meta Pixel con la extensión "Meta Pixel Helper" | Manual Daniel | Sí — validación final |
| Configurar Custom Audiences (excluir suscriptoras + pacientes) | Manual Daniel en Ads Manager | Sí — evita gastar en gente ya convertida |
| Crear las 2 creatives (carrusel A + reel B) | Manual Daniel en Canva | Sí |
| Crear la campaña en Ads Manager | Manual Daniel | Sí |

---

## 2 · Pre-requisitos antes de empezar

- [ ] Acceso a **Meta Business Manager** (ya configurado tras setup MBS — ver `documentos-internos/checklist-meta-business-suite-setup.md`).
- [ ] **Cuenta publicitaria** "TWIM Project" (renombrada desde "The World Is Mind Project" cuando se haga la limpieza pendiente del System User).
- [ ] **Datos fiscales** del portfolio empresarial completos (Razón social Daniel Orozco Abia + dirección consulta + sitio web). Si Meta no los tiene, no factura ni cobra el ad. **Si están vacíos todavía, completarlos ANTES del 21 mayo.**
- [ ] **Método de pago** verificado en la cuenta publicitaria.
- [ ] **2FA** activado en Meta cuenta admin.

---

## 3 · Paso 1 · Cargar Meta Pixel en todo el site (código)

### Páginas que necesitan el píxel

Mínimo:
- [ ] `index.html`
- [ ] `newsletter/index.html`
- [ ] 7 landings SEO con bloque cross-sell (las del PR #94):
  - `psicologo-burnout-valencia.html`
  - `psicologo-ansiedad-valencia/`
  - `psicologo-adolescentes-valencia.html`
  - `psicologo-dependencia-emocional-valencia.html`
  - `terapia-pareja-valencia.html`
  - `psicologo-online.html`
  - `soluciones/index.html`
- [ ] `dejadeobligarte.html`
- [ ] `dejadebuscarteenotros.html`
- [ ] `nopuedoparar-taller.html`

### Snippet Meta Pixel a insertar

Antes del cierre del `</head>` en cada página:

```html
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '1447483376992558');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=1447483376992558&ev=PageView&noscript=1"/></noscript>
<!-- End Meta Pixel Code -->
```

### Validación tras carga

- Instalar la extensión [Meta Pixel Helper](https://chrome.google.com/webstore/detail/meta-pixel-helper) en Chrome.
- Visitar cada URL → la extensión debe mostrar "1 pixel found, 1 fired" con eventos `PageView`.

---

## 4 · Paso 2 · Cablear evento `Lead` en cross-sell + exit-intent

### Localización

- `assets/te-escribo-cta.js` (cross-sell de las 7 landings SEO).
- `assets/te-escribo-exit-intent.js` (exit-intent modal).

### Patrón a añadir

Donde hoy se dispara el evento `gtag('event', 'newsletter_signup', {...})`, añadir justo después:

```javascript
if (typeof fbq === 'function') {
  fbq('track', 'Lead', {
    content_name: 'Te escribo newsletter',
    source: source_value
  });
}
```

`source_value` es el mismo identificador que se pasa a GA4 (`'cross_sell_seo'` o `'exit_intent'`).

### Validación

- Suscribir un email de prueba desde una landing.
- Confirmar en Meta Pixel Helper que se dispara `Lead`.
- En Meta Ads Manager → Events Manager → Eventos → debe aparecer "Lead" con timestamp reciente.

---

## 5 · Paso 3 · Custom Audiences en Ads Manager (manual Daniel)

### 5.1 · Audience "Suscriptoras Newsletter Home" (a EXCLUIR)

1. Ads Manager → Audiences → Create Audience → Custom Audience → Customer List.
2. Subir lista de emails del grupo `newsletter-home` exportada desde MailerLite (CSV).
3. Nombrar: `EXCLUDE - Newsletter Home subs`.
4. Esperar 24-48h a que Meta haga el matching.

### 5.2 · Audience "Pacientes / contactos clínicos" (a EXCLUIR)

1. Misma vía: Custom Audience → Customer List.
2. Subir lista de emails de pacientes y contactos clínicos (de tu CRM o agenda Booking).
3. Nombrar: `EXCLUDE - Pacientes y contactos`.
4. **Política dura del CLAUDE.md aplicada:** esta lista NO se sube a NotebookLM ni a ElevenLabs ni a ningún otro sistema cloud salvo Meta Ads para exclusión. Es uso defensivo (no captarlos), no procesamiento clínico.

### 5.3 · Lookalike (diferido)

A activar **solo cuando haya ≥100 suscriptoras** en `newsletter-home`. Hoy 4. Probablemente no aplicable durante este test de 35 €.

---

## 6 · Paso 4 · Crear las 2 creatives (manual Daniel en Canva)

Las specs están completamente definidas en `PLAN-CAPTACION-30D.md` §4.2 y §4.3. Resumen ejecutivo:

### 6.1 · Creative A · carrusel 4 slides 1080×1350

- Slide 1: "duermo bien pero me levanto cansada" (reusa `slide-02.png` del carrusel cansancio psíquico).
- Slide 2: "El cuerpo se recupera con horas. La psique se recupera con honestidad." (reusa `slide-04.png`).
- Slide 3: "Reprimir cansa más que correr. Sostener una imagen cansa más que cargar peso." (reusa `slide-03.png`).
- Slide 4 (NUEVA): CTA con kicker "TE ESCRIBO" + H1 "Te lo escribo despacio, una carta cada tanto." + body editorial + footer twimproject.com/newsletter.

### 6.2 · Creative B · reel 9:16, 8-12 s

3 cards consecutivas (~3s cada una): "Has dormido 8 horas." → "Sigues cansada." → "Saber por qué cambia todo." → end-card logo TWIM + URL newsletter.

### 6.3 · Caption (común a A y B)

Ya redactado en PLAN-CAPTACION-30D.md §4.2. CTA del botón Meta: **"Saber más"** (no "Suscribirse" — rompe la promesa de carta editorial).

---

## 7 · Paso 5 · Crear la campaña en Ads Manager (manual Daniel)

### 7.1 · Setup base

- **Objetivo de campaña:** Leads (no Traffic — queremos optimización de conversión real).
- **Presupuesto:** 5 €/día × 7 días = 35 € total. CBO o ABO indistinto a este volumen.
- **Fechas:** del **21 mayo 00:00** al **27 mayo 23:59** (7 días).
- **Optimización:** Conversiones → evento `Lead`.

### 7.2 · Audiencia

Según `PLAN-CAPTACION-30D.md` §4.1:

- **Geo:** España.
- **Edad:** mujeres 28-45.
- **Idiomas:** Español.
- **Intereses:** psicología, mindfulness, autoconocimiento, terapia, *burnout*, ansiedad, libros de Brené Brown, Lori Gottlieb, Massimo Recalcati, Marian Rojas. NO usar intereses puramente comerciales tipo "marketing femenino".
- **Excluir:** las dos Custom Audiences del paso §5.

### 7.3 · Ad sets

Crear **2 ad sets paralelos** (split A vs B) para ver qué creative rinde mejor:

| Ad set | Creative | Presupuesto | UTM content |
|---|---|---|---|
| A | Carrusel | 2,50 €/día (la mitad) | `utm_content=carrusel-a` |
| B | Reel | 2,50 €/día (la mitad) | `utm_content=reel-b` |

URL destino base (igual ambas, cambia solo `utm_content`):
```
https://twimproject.com/newsletter/?utm_source=meta&utm_medium=cpc&utm_campaign=te-escribo-cansancio-w4&utm_content={A o B}
```

### 7.4 · Texto del ad

Caption según `PLAN-CAPTACION-30D.md` §4.2 (texto editorial sin coaching).

---

## 8 · Día del lanzamiento · 21 mayo 2026

Checklist secuencial mañana del 21 mayo:

- [ ] **08:00** Verificar contador `newsletter-home` en MailerLite.
  - Si **≥ 150** → cancelar test, plan orgánico funciona. Documentar y cerrar.
  - Si **100-149** → activar test con presupuesto reducido a 25 € (5 días).
  - Si **< 100** → activar test completo 35 € / 7 días.
- [ ] **09:00** Confirmar pixel y evento `Lead` con extensión Meta Pixel Helper en `/newsletter/`.
- [ ] **09:30** Lanzar la campaña. Estado: Active.
- [ ] **10:00** Verificar en Events Manager que llegan eventos `PageView` desde el ad.
- [ ] **18:00** Primera revisión del día. CPL provisional, CTR provisional. Si CPL > 5 € → pausar inmediatamente y revisar creative.

---

## 9 · Gestión durante los 7 días (revisión diaria 18:00)

### KPIs primarios

- **CPL (Cost per Lead):** €gastados / suscripciones a `newsletter-home` desde fuente Meta.
- **Cota objetivo:** ≤1,50 € España. ≤0,80 € si se amplía a LatAm en split posterior.

### Stop-loss

| Condición | Acción |
|---|---|
| Tras 15 € gastados, CPL > 3 € | **Pausar** la creative con peor CPL. Mantener la otra. |
| Las 2 creatives con CPL > 3 € | **Parar el test entero.** El problema es de copy/promesa, no de pujas. |
| CTR < 0,8 % | Considerar refresh de creative. |
| Frequency > 3 antes del día 5 | Audiencia muy pequeña, expandir intereses o ampliar geo. |

### KPIs secundarios

- CTR ≥ 1,5 %.
- Time on `/newsletter/` ≥ 30 s (GA4).
- Scroll depth ≥ 50 % (GA4).

---

## 10 · Post-test · análisis y decisión (28 mayo)

### Métricas a recopilar

| Métrica | Fuente |
|---|---|
| Total invertido | Meta Ads Manager |
| Suscriptoras netas atribuidas a Meta | MailerLite (filtro UTM) |
| CPL real | Cálculo |
| CTR | Meta Ads Manager |
| Time on landing | GA4 |
| Open rate de la primera carta que reciban (Carta #3 o automation bienvenida) | MailerLite |

### Decisiones a tomar el 28 mayo

- Si **CPL ≤ 1,50 € y captación neta ≥ 20** → **continuar Meta Ads** con presupuesto incremental (50-100 €/mes a partir de junio).
- Si **CPL 1,50-3 € o captación 10-20** → **iterar creatives** y volver a probar 35 € en julio.
- Si **CPL > 3 € o captación < 10** → **parar Meta Ads en T1**, replantear estrategia orgánica + autoridad externa (`SEO_ANALISIS_2026-03-20.md` §3).

---

## 11 · Riesgos y mitigación

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Meta rechaza el ad por contenido sensible (psicología, salud mental) | Media | Alto si pasa | Caption sin promesas terapéuticas. Sin frases tipo "te cura", "te transforma". Mantener tono editorial. Si rechazan, revisar política de Special Ad Categories ("Health"). |
| Cuenta publicitaria sin datos fiscales completos → Meta no factura | Media | Bloqueante | Completar datos antes del 18 mayo. |
| Píxel no instalado en `/newsletter/` el día del lanzamiento | Baja con este checklist | Bloqueante | Validación del paso §3 antes de activar. |
| Custom Audience de exclusión sin matching | Media (lleva 24-48h) | Medio (gastas en suscriptoras) | Subir las listas como muy tarde el 18 mayo (3 días antes del 21). |
| Comentarios negativos en el propio ad | Media | Bajo | Política de moderación: bloquear y reportar trolls, no responder. |
| Click rate alto pero conversión baja → coste alto sin captación | Media | Alto | Stop-loss del paso §9. La regla de 15 € es defensiva. |
| Daniel olvida revisar el día 21 | Baja | Alto si pasa | Recordatorio en agenda. La VA cuando entre lo ejecuta también. |

---

## 12 · Lo que NO se hace en este test

- **No retargeting con audiencias visitantes.** No tenemos suficiente tráfico para un retargeting útil. Diferido a Q3 2026 cuando haya >5.000 visitas/mes.
- **No vídeo testimonial.** Política deontológica: no testimonios de pacientes (`SEO_ANALISIS_2026-03-20.md` §6).
- **No ampliar a Google Ads en paralelo.** Hay tema pendiente de cumplimiento Google Ads (`documentos-internos/google-ads-cumplimiento-y-reactivacion.md`). Cerrar ese antes de tocar Google.
- **No promocionar programas de pago en este test.** El objetivo del test es **captar suscriptoras a newsletter, no vender programas**. Cuando el embudo madure (Q3-Q4 2026) se evalúa promo de pago para Deja de Obligarte / programa dependencia.

---

## 13 · Decisiones a cerrar antes del 21 mayo

- [ ] **Setup técnico del píxel + evento Lead** en código (PR aparte). **Lado yo.** Estimación: 30 min.
- [ ] **Completar datos fiscales** del portfolio empresarial Meta. **Lado Daniel.** Estimación: 15 min.
- [ ] **Subir Custom Audiences** de exclusión. **Lado Daniel.** Estimación: 30 min + 24-48h matching.
- [ ] **Diseñar las 2 creatives** en Canva. **Lado Daniel.** Estimación: 1-2 h.
- [ ] **Crear la campaña** en Ads Manager (sin lanzar). **Lado Daniel.** Estimación: 30 min.
- [ ] **Validación final** con Meta Pixel Helper en todas las URLs. **Lado Daniel.** Estimación: 15 min.

**Total tiempo Daniel pre-21-mayo: ~3 horas distribuidas en 2 semanas.**

---

## Refs

- Plan base cocido: `contenido-rrss/te-escribo-newsletters/PLAN-CAPTACION-30D.md` §4.
- Setup MBS pre-requisito: `documentos-internos/checklist-meta-business-suite-setup.md`.
- Sistema visual para creatives: `documentos-internos/instagram-sistema-visual-marca.md` (PR #94).
- Reglas de identidad editorial: `CLAUDE.md`.
- Métricas Carta #1 que justifican el gate: `contenido-rrss/te-escribo-newsletters/PLAN-LANZAMIENTO-5-MAYO.md` §Métricas reales.
