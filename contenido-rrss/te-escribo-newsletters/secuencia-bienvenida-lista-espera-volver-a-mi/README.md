# Secuencia bienvenida · Lista espera Volver a Mí

> Creado 26 may 2026 por Claude bajo libertad de acción explícita («tenemos que hacer envío a mujeres por email y demás opciones de que es twimproject, quien es daniel orozco abia y por qué el taller Volver a Mi es la mejor opción que tienen»). Daniel autorizó pegar en MailerLite vía MCP.

---

## 1 · Estado a 26 may 2026

| Email | Cuándo | Estado en MailerLite | Estado en repo |
|---|---|---|---|
| E1 · Estás dentro · TWIM Project | D+0 (inmediato) | ✅ **Pegado vía MCP** (versión corta · ~1.000 chars) en automation `188015660948784728` paso 0. `subject: «Estás dentro · esto es lo que te he prometido (y lo que NO)»` | ✅ versión completa en `E1-estas-dentro-d0.txt` (~2.900 chars) |
| E2 · Quién soy y por qué este trabajo | D+3 | ⏳ Pendiente · automation solo tiene 1 paso · Daniel añade en panel | ✅ `E2-quien-soy-d3.txt` |
| E3 · Por qué Volver a Mí encaja contigo | D+7 | ⏳ Pendiente · idem | ✅ `E3-por-que-volver-a-mi-d7.txt` |

---

## 2 · Qué falta · acción manual Daniel en MailerLite

### A · Verificar trigger group de la automation
El automation `188015660948784728` se llama «Secuencia · Lead magnet 5 señales hambre de mirada + lista taller». Confirmar en panel que su **trigger group** sea `Lead · Pre-venta Volver a Mí` (ID `188015567896052961`). Si no es, asignar.

### B · Añadir 2 emails más a la automation
Limitación MCP · solo se puede actualizar el email existente, no añadir nuevos pasos. Daniel añade en panel:

1. **Delay 3 días** después del E1
2. **Email 2** · pegar contenido de `E2-quien-soy-d3.txt` · asunto: `Quién soy · y por qué hago esto`
3. **Delay 4 días** después del E2 (D+7 desde E1)
4. **Email 3** · pegar contenido de `E3-por-que-volver-a-mi-d7.txt` · asunto: `Por qué Volver a Mí encaja con lo que llevas dentro`

Tiempo estimado: 15-20 min en panel MailerLite.

### C · Reemplazar E1 corto por versión larga (opcional)
Si Daniel quiere el copy completo en E1 (más rico editorialmente · ~2.900 chars en vez de 1.000), reemplazar el plain_text actual con el cuerpo entero de `E1-estas-dentro-d0.txt`. La versión corta es funcional pero menos editorial.

### D · Verificar idioma a Español
Las automations creadas vía MCP nacen en `language_id: 4` (en-US) · arista del conector. Cambiar a Español en panel antes de que se dispare la automation. Crítico antes de los primeros suscriptores reales.

---

## 3 · Voz editorial · resumen

Los 3 emails siguen la voz Te escribo · descriptivos, anti-positivismo, sin presión, sin venta dura, tuteo. Estructura narrativa:

- **E1** · contención + expectativa + diferenciación anti-spam. NO vender taller aquí.
- **E2** · biografía clínica + autoridad sobria + referentes (Recalcati, González, Gottlieb). Construye confianza.
- **E3** · 4 frentes operativos (qué se hace · por qué grupo · por qué no curso grabado · qué pasa si no encaja). Cierre persuasivo suave. PD al Directo del 7 jun.

---

## 4 · Cuándo activar / desactivar la automation

- **Activar** · cuando los 3 emails estén en panel + idioma Español verificado.
- **Modificar PD del E3** · borrar el PD del Directo 7 jun cuando llegue 8 jun (pasada la fecha).
- **Desactivar / pausar** · a partir del 1 sept 2026 (apertura pre-venta dura) · la secuencia de bienvenida deja paso a la secuencia de pre-venta que es otra automation.

---

**Última actualización:** 26 may 2026 · sesión `claude/social-media-link-naming-tcIUA`.
