# Google Ads · Campaña de captación de pacientes · build operativo

> Creado el 5 jun 2026 a petición de Daniel. Objetivo personal explícito · **liberar las tardes desde septiembre 2026** captando pacientes vía Google Ads y derivándolos a la red de psicólogos supervisada (modelo `modelo-captacion-supervisada-union-periodistas.md` + `twim-clinic-modelo-derivacion.md`). Daniel sigue atendiendo siempre su franja premium de mañana.
>
> Estado de la cuenta (5 jun 2026, verificado por captura de Daniel) · **activa**, no suspendida. Método de pago verificado y cargado. Saldo 8€. Una campaña previa tipo INTELIGENTE «Tu Mente Merece Bienestar» (5 clics / 832 impr / 0 conv / CTR 0,60%) · **pausar/archivar**.
>
> Cumplimiento · este build respeta `google-ads-cumplimiento-y-reactivacion.md` §1 (política salud) y §3 (estructura limpia).
>
> **✅ LANZADA 9 jun 2026.** Campaña «Búsqueda · Captación pacientes · Valencia + Online» publicada. Config final: tipo **Búsqueda manual**; redes **solo Búsqueda** (partners y Display OFF); geo **Valencia + radio** (presencia); ES; **presupuesto 8,5 €/día**; puja **Maximizar clics, CPC máx 1,80 €**; **horario lun-vie 8-22, sáb 8-14, dom 19-00** (domingo noche lo añadió Daniel: pico de ansiedad anticipatoria del lunes); grupo **Ansiedad** con 9 keywords (frase+exacta) → landing `/psicologo-ansiedad-valencia/`; RSA «Buena» eficacia; **6 sitelinks + callouts**; nombre **TWIM Project**; **IA Max OFF**. **Sin certificación de salud** (no requerida para terapia en España, ver corrección en `google-ads-cumplimiento-y-reactivacion.md`). **Conversión:** Daniel configuró el resultado como **Llamadas telefónicas** (las llamadas desde anuncios se miden solas, sin tag web). **Aviso de coherencia de embudo:** la landing empuja a **WhatsApp/email**, no a llamada (no hay `tel:` en la landing) → la conversión de llamada NO captura la vía real de contacto. Por eso se añade evento GA4 `generate_lead` en clics de WhatsApp/email de las landings vía `assets/twim-ads-conversion.js`. **Pendiente de Daniel:** marcar `generate_lead` como **evento clave en GA4** e **importarlo a Google Ads** para ver el embudo completo (llamadas + WhatsApp/email).

---

## 0 · Dos correcciones de rumbo

1. **Tipo de campaña · BÚSQUEDA manual, no INTELIGENTE.** Las campañas inteligentes auto-gestionan keywords y en nicho psicología con presupuesto bajo gastan en términos amplios irrelevantes. Búsqueda manual = control de keywords = CPL controlado.
2. **Crédito 400€ · NO perseguir.** Exige gastar 400€ antes del 19 jun (~28€/día) sobre embudo sin validar. Validar primero a 8-10€/día.

---

## 1 · Prerrequisito inviolable · transparencia del equipo (antes de escalar gasto)

Google (política salud) exige landing con About verificable, y la **deontología** exige que el paciente sepa que puede atenderle un psicólogo de la red supervisado por Daniel, no Daniel en persona.

**Acción previa:** añadir en la home y en las landings de captación una línea/sección tipo:

> «En TWIM Project somos un equipo de psicólogos sanitarios colegiados, cada uno especializado en un tipo de dificultad (dependencia emocional, ansiedad, autoexigencia, burnout). Daniel Orozco Abia (CV11515) dirige y supervisa clínicamente el trabajo del equipo. Según tu caso y disponibilidad, te atenderá el profesional más adecuado.»

- **Honestidad de tamaño** · «equipo de psicólogos» es correcto con ≥2 reales (Daniel + Sergio). No inflar a «amplio equipo» hasta que la red crezca.
- Sin nombres de los junior (como pidió Daniel) · evita que el paciente espere a uno concreto.

---

## 2 · Estructura de la campaña

- **1 campaña:** `Búsqueda · Captación pacientes · Valencia + Online`
- **Grupos de anuncio (empezar con 2, los core TWIM):**

| Ad group | Landing destino | Geo |
|---|---|---|
| Dependencia emocional | `/psicologo-dependencia-emocional-valencia.html` | Valencia + área (radio) |
| Ansiedad | `/psicologo-ansiedad-valencia/` | Valencia + área (radio) |

> Ampliar después con Burnout (`/psicologo-burnout-valencia.html`) y Online-España (`/psicologo-online.html`) cuando los 2 primeros conviertan.

---

## 3 · Configuración

- **Objetivo:** Clientes potenciales (Leads).
- **Redes:** Solo Búsqueda. **Desactivar** «Red de Display» y «socios de búsqueda» (consumen presupuesto en baja calidad).
- **Geo:** Valencia ciudad + radio 20-25 km (área metropolitana). Para el futuro grupo Online · España.
  - Importante · elegir «Presencia: personas que están o visitan habitualmente» (no «interés»), para no pagar clics de fuera.
- **Idioma:** Español.
- **Presupuesto:** **8-10 €/día** las primeras 3-4 semanas.
- **Puja:** empezar en **«Maximizar clics» con un límite de CPC de 1,80 €** (recoge datos barato). Cuando haya ≥15-20 conversiones registradas, cambiar a «Maximizar conversiones».
- **Horario:** lun-vie 8:00-22:00, sáb 9:00-14:00. Pausar madrugadas.

---

## 4 · Palabras clave (concordancia de frase «…» y exacta [.…])

**Ad group Dependencia emocional:**
```
"psicologo dependencia emocional valencia"
"psicologo dependencia emocional"
"terapia dependencia emocional valencia"
"dependencia emocional ayuda profesional"
[psicologo dependencia emocional online]
```

**Ad group Ansiedad:**
```
"psicologo ansiedad valencia"
"terapia ansiedad valencia"
"psicologo para la ansiedad"
"tratamiento psicologico ansiedad valencia"
[psicologo ansiedad online]
```

> No usar concordancia amplia pura al inicio · trae basura. Frase y exacta dan control.

---

## 5 · Palabras clave negativas (a nivel campaña)

```
gratis
test
que es
significado
pdf
libro
frases
ejercicios
oposiciones
carrera
universidad
practicas
empleo
trabajo
sueldo
curso
casero
remedios
```

> Filtra a quien busca información/estudios/curiosidad, no a quien busca consulta.

---

## 6 · Anuncio adaptable de búsqueda (RSA) · copiar tal cual

Cumple política salud · sin diagnóstico, sin promesa de cura, sin apelar a vulnerabilidad extrema. Voz TWIM · clínica, sin coaching.

**Títulos (máx. 30 caracteres cada uno · pegar 12-15):**
```
Psicólogos en Valencia
Equipo TWIM Project
Dependencia Emocional
Ansiedad y Autoexigencia
Terapia Presencial y Online
Primera Sesión de Valoración
Supervisión Clínica CV11515
Psicología, no Coaching
Atención Profesional Real
Pide Cita en Valencia
Burnout y Cansancio Mental
Psicólogo Online en España
TWIM Project · Valencia
Reserva Tu Primera Cita
Psicólogos Colegiados
```

**Descripciones (máx. 90 caracteres cada una · pegar 4):**
```
Equipo de psicólogos sanitarios de TWIM Project. Terapia en Valencia y online.
Dependencia emocional, ansiedad y autoexigencia. Pide tu sesión de valoración.
Psicología profunda y aplicada, sin coaching ni promesas. Supervisión clínica.
Atención presencial en Valencia u online en toda España. Reserva tu primera cita.
```

**Rutas (path, opcional, máx. 15 cada una):** `valencia` / `psicologia`

> En el grupo de Ansiedad, cambiar el título 3 a «Ansiedad en Valencia» y el destino a la landing de ansiedad. Un RSA por ad group, apuntando a su landing.

---

## 7 · Extensiones (suben CTR y bajan CPC · ponerlas todas)

- **Enlaces de sitio (4):** «Dependencia emocional» → su landing · «Ansiedad» → su landing · «Burnout» → su landing · «Cómo trabajamos» → home/about.
- **Textos destacados (callouts):** `Psicólogos colegiados` · `Presencial y online` · `Primera valoración` · `Supervisión clínica`.
- **Fragmentos estructurados** (tipo «Servicios»): Terapia individual · Terapia online · Dependencia emocional · Ansiedad · Burnout.
- **Llamada:** teléfono de la consulta (si quieres recibir llamadas directas).

---

## 8 · Seguimiento de conversiones (CRÍTICO · ahora estás a ciegas)

Sin esto, 0 conversiones medidas = no se puede optimizar. Configurar **al menos una**:

1. **Envío de formulario** en la landing (lead) · la más valiosa.
2. **Clic en botón WhatsApp / «Pedir cita»** como conversión secundaria.
3. **Llamada desde el anuncio** (si activas extensión de llamada).

Vía · Google Ads → Objetivos → Conversiones → Nueva acción → Sitio web (con etiqueta en la landing) o importar desde GA4 `G-VMMZ1TKWZ0` (ya instalado).

---

## 9 · Calendario y umbrales de decisión

- **Semana 1-2:** dejar correr sin tocar. Recoger datos (mínimo 50-100 clics antes de juzgar).
- **Revisar:** CTR (objetivo >4% en search), CPC medio, y sobre todo **CPL (coste por lead)**.
- **Umbral de éxito:** CPL ≤ 15-20 € para que la economía de derivación funcione (margen supervisión 20-30 €/sesión × varias sesiones por paciente cubre de sobra un CPL de 15-20 €).
- **Si CPL > 30 €** sostenido a las 3 semanas · pausar el ad group, revisar keywords/landing, no subir presupuesto.
- **Si convierte:** subir a 15-25 €/día y añadir los ad groups de Burnout + Online.

---

## 10 · Riesgos específicos

| Riesgo | Mitigación |
|---|---|
| Capacidad insuficiente (solo Daniel + Sergio) para absorber leads | Empezar presupuesto bajo · escalar Ads al ritmo que crece la red de junior, no antes |
| Anuncio rechazado por wording clínico | Copy §6 ya cumple · si rechazan, quitar la palabra señalada y reenviar |
| Pagar clics de fuera de Valencia | Geo «presencia», no «interés» (§3) |
| Gastar sin medir | No lanzar hasta tener §8 (conversiones) configurado |
| Expectativa «quiero a Daniel» | Encuadre del equipo §1 en la landing |

---

## 11 · Orden de ejecución (checklist para Daniel)

```
[ ] 1. Añadir sección «equipo TWIM supervisado por Daniel» en home + 2 landings (§1).
[ ] 2. Configurar 1 conversión (formulario o clic cita) (§8).
[ ] 3. Crear campaña Búsqueda (no Inteligente), objetivo Leads, solo Búsqueda (§3).
[ ] 4. Geo Valencia+radio, presencia, ES, 8-10€/día, Max clics CPC máx 1,80€ (§3).
[ ] 5. Ad group Dependencia + keywords (§4) + RSA (§6) → su landing.
[ ] 6. Ad group Ansiedad + keywords (§4) + RSA (§6) → su landing.
[ ] 7. Negativas a nivel campaña (§5).
[ ] 8. Extensiones (§7).
[ ] 9. Publicar. Dejar 2 semanas sin tocar.
[ ] 10. Revisar CPL y decidir (§9).
```

---

**Pendiente de afinar con datos reales** · tarifas de derivación cerradas, capacidad real de la red, CPL real del nicho en Valencia. Revisar este doc cuando haya 2 semanas de datos.

---

## Seguimiento · 10 jun 2026 (48 h de campaña) · HALLAZGO + datos + plan corrector

> Capturas de Daniel del panel (10 jun). Registrado por Claude.

### Hallazgo principal · la campaña activa es INTELIGENTE (Smart/Express), no la Búsqueda manual diseñada

El panel es `ads.google.com/aw/express/` y los textos hablan de «campañas inteligentes». Nombre visible: «Psicólogos Expertos en Ansiedad». Implicaciones: sin keywords exactas/negativas reales (solo «temas»), Google decide dónde mostrar (incluye Maps), y el copy del anuncio lo generó Google. El presupuesto coincide (8,5 €/día · máx 258 €/mes) y el horario personalizado se mantuvo.

### Datos 9-10 jun

| Métrica | Valor | Lectura |
|---|---|---|
| Inversión | 13,19 € | en línea con 8,5 €/día |
| Impresiones | 5.191 (96 % móvil · 909 a 25-34) | volumen alto por mezcla smart |
| Clics | 18 → **CPC medio 0,73 €** | bueno (máx era 1,80) |
| Origen clics | 9 Búsqueda · **9 Maps** · 0 YouTube/Gmail | la mitad va a la ficha GBP |
| Llamadas / acciones locales / conversiones | **0 / 0 / 0** | sin `generate_lead` como conversión, la campaña optimiza a ciegas |
| Términos | «psicologos en burjassot» 2 · «erea» 2 (1,16 €) · «emdr valencia» 1 (1,01 €) · «catarroja» 1 · «psicología cerca de mí» 1 | **fuga ~16-24 %**: «erea» es ruido y «emdr» es una técnica que Daniel no ofrece · en smart no hay negativas reales |
| Tendencia | impresiones 3,8k→1,5k · clics 14→4 | normal en día 2 (calibración) · no alarmante aún |

### Copy del anuncio generado por Google · rompe la voz TWIM

«Contamos con el Respaldo de Psicólogos Expertos, Siempre Dispuestos a Brindarte Apoyo» — genérico, Title Case, voz corporativa. Sustituir (botón Editar) por: **«Psicólogo para ansiedad en Valencia. Daniel Orozco Abia, colegiado CV11515, en consulta desde 2012. Presencial en Valencia u online. Primera respuesta en 48 h.»** (concreto, con credencial, sin promesa vacía).

### Plan corrector (decidido 10 jun)

1. **NO apagar todavía.** 48 h no es muestra. El gate sigue siendo el del doc: revisión 23 jun, CPL objetivo ≤15-20 € por lead real.
2. **Daniel (5 min, lo más urgente):** marcar `generate_lead` evento clave en GA4 + vincular a Ads. Con 0 conversiones registradas, la smart campaign no puede aprender NI podemos juzgarla.
3. **Daniel (3 min):** editar el texto del anuncio con el copy de arriba · revisar «temas de palabras clave» y quitar los que no encajen (si EMDR aparece como tema, fuera).
4. **Decisión del 23 jun:** si con conversiones midiendo el CPL real no cumple, **migrar a la campaña de Búsqueda manual de este doc** (estructura ya definida arriba: keywords frase/exacta, negativas, RSA propia). Una smart campaign nunca dará el control que el plan exige; se le da su ventana de prueba porque ya está pagada y calibrando.

### Verificación E2E del evento de conversión · 10 jun 2026 · OK

Test real ejecutado por Daniel (móvil → landing ansiedad → botón WhatsApp) y verificado en GA4 Tiempo real por captura: **`generate_lead · 1` registrado** (junto a page_view 3, session_start 2, form_start 1). El circuito botón → gtag → GA4 funciona de punta a punta. «Eventos clave» aún sin datos = esperado (falta la estrella).

Pasos restantes (Daniel):
1. **Mañana 11 jun** · GA4 → Administrar → Visualización de datos → Eventos → pestaña «Eventos recientes» → estrella en `generate_lead` (Google tarda hasta 24 h en listarlo tras el primer disparo). Aprovechar y poner estrella también a `sign_up`, `cap3_lead_capture` y `directo_reservar_plaza` (leads reales ya con datos).
2. Después · Google Ads → llave inglesa → Conversiones → «+ Nueva acción de conversión» → Importar → Propiedades GA4 → Web → `generate_lead` → Importar. (Si el panel express no lo muestra: ⋮ → «Cambiar al modo experto», no afecta a la campaña.)
3. Nota: el test de hoy contará como 1 conversión falsa cuando se importe · irrelevante a efectos de optimización, no requiere acción.
