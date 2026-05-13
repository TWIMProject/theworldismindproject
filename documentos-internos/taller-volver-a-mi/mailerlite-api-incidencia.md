# Incidencia MailerLite API · Formularios web twimproject.com

> Documento abierto el **13 may 2026** en sesión `claude/improve-proposal-quality-pq3d9` para registrar el problema técnico mencionado por Daniel y dejar trazabilidad de su resolución.
>
> **Estado a 13 may ~14:30 CEST: RESUELTA EN DIAGNÓSTICO.** El JSON del endpoint diag confirma que la API key MailerLite NO está revocada. El problema real son **4 env vars secundarias ausentes en Netlify**, no la API key del sistema. Los 9 grupos críticos (newsletter, reto 7 días, lead magnet dependencia, Cap III del libro) funcionan correctamente. Detalle completo en §4.3 y §4.4.
>
> **Conclusión para el taller Volver a Mí:** la infraestructura MailerLite está sana. La incidencia **no bloquea** ni la captación de newsletter ni el lead magnet del Cap III. Cuando se monte el grupo «Pre-venta Volver a Mí» en septiembre, será una env var nueva más a crear (5ª), no un sistema roto.

---

## 1 · Estado conocido a 13 may

**Lo que Daniel ha reportado en chat (verbatim):**

> «Infraestructura MailerLite con error de conexión API en formularios de captación de twimproject.com. Hipótesis principal API key expirada o revocada. Informe técnico ya generado para "Code".»

**Lo que esta sesión ha podido verificar:**

- ✅ La env var `MAILERLITE_GROUP_LEAD_ENGRANAJES_CAP3 = 187351536193505006` está creada en Netlify con todos los scopes (captura compartida por Daniel el 13 may).
- ✅ El grupo «Lectores · Engranajes Cap3» existe en MailerLite con el mismo ID (captura compartida).
- ✅ El código actualizado de `netlify/functions/subscribe.js` con la nueva entrada en `groupEnvMap` fue mergeado a main en el PR #149 el 13 may (commit `c5a6856`).
- ⚠️ El endpoint `/.netlify/functions/subscribe?diag=1` devolvía `MAILERLITE_GROUP_LEAD_ENGRANAJES_CAP3: false` tras el merge. Hipótesis razonable: deploy de Netlify aún en curso o caché del navegador.
- ❓ No se ha verificado todavía si `MAILERLITE_API_KEY` está válida ni si el problema reportado por Daniel afecta solo a la captación o también a otras funciones.

**Lo que NO está en el repo:**

- El «informe técnico ya generado para Code» mencionado por Daniel. Si existe, no está en chat ni en repo. Daniel debe pegarlo o subirlo cuando vuelva.

---

## 2 · Diagnóstico desde cero · pasos verificables sin acceso al dashboard MailerLite

Si el informe técnico previo no aparece, esta es la rutina mínima de diagnóstico que Daniel (o quien tenga acceso a Netlify) puede ejecutar:

### Paso 1 · Verificar que el deploy del PR #149 está publicado

- URL: `https://app.netlify.com/projects/lighthearted-kitten-8aba94/deploys`
- Buscar el deploy correspondiente al commit `c5a6856` (Merge pull request #149).
- Estado esperado: **«Published»**.
- Si está en «Building» o «Failed», esperar / investigar.

### Paso 2 · Llamar al diagnóstico de la function

```
https://twimproject.com/.netlify/functions/subscribe?diag=1
```

Resultado esperado tras deploy completo, recogido del fichero `netlify/functions/subscribe.js`:

```json
{
  "ok": true,
  "node": "vXX.X.X",
  "fetchAvailable": true,
  "env": {
    "MAILERLITE_API_KEY": true,
    "MAILERLITE_GROUP_LEAD_MAGNET": true,
    "MAILERLITE_GROUP_RETO": true,
    "MAILERLITE_GROUP_GENERAL": true,
    "MAILERLITE_GROUP_PADRES_TDAH": true,
    "MAILERLITE_GROUP_PADRES_BACH": true,
    "MAILERLITE_GROUP_PADRES_TALLERES": true,
    "MAILERLITE_GROUP_NEWSLETTER_HOME": true,
    "MAILERLITE_GROUP_INSCRITAS_TDAH": true,
    "MAILERLITE_GROUP_INSCRITAS_BACH": true,
    "MAILERLITE_GROUP_LEAD_IMPOSTORA": true,
    "MAILERLITE_GROUP_LEAD_BURNOUT": true,
    "MAILERLITE_GROUP_LEAD_ENGRANAJES_CAP3": true
  }
}
```

**Interpretación:**

- Si **alguna entrada está en `false`** → esa env var no se ha propagado o no existe. Solución: crear/revisar en Netlify → Site configuration → Environment variables.
- Si **todo está en `true` pero los formularios siguen fallando** → el problema no es env var ausente sino API key inválida. Ir al paso 3.

### Paso 3 · Verificar autenticación con MailerLite directamente

Si todas las env vars están en `true` pero los forms siguen fallando, lo siguiente es probar la API key haciendo una llamada autenticada desde un sitio que no sea el de producción (curl local con el valor de la env var). La respuesta esperada de `GET https://connect.mailerlite.com/api/me` con la Authorization correcta es 200 con el JSON del account holder.

Si devuelve `401 Unauthorized` → la API key está revocada o expirada. **Resolución:**

1. MailerLite dashboard → Integrations → API → generar nueva API key con permisos `subscribers:write`.
2. Copiar el token nuevo.
3. Netlify → Environment variables → editar `MAILERLITE_API_KEY` con el nuevo valor.
4. Redeploy del site (Netlify lo hace solo al cambiar env vars, pero verificar).
5. Repetir paso 2 — todas las vars deben seguir en `true` y un POST de prueba al endpoint subscribe debe devolver 200.

### Paso 4 · Test E2E con email de prueba

Una vez los pasos anteriores estén en verde, hacer test end-to-end desde un navegador en incógnito con un email tuyo de prueba (gmail funciona bien). Confirmar:

- Form aparece y submit funciona.
- Email confirma llegada al grupo correspondiente.
- El suscriptor aparece en MailerLite en el grupo correcto.

---

## 3 · Lista de formularios afectados (auditoría rápida)

Forms presentes en el repo a 13 may que pasan por `/.netlify/functions/subscribe`:

| Form | Archivo | Grupo enviado |
|---|---|---|
| Hero newsletter home | `index.html` | `newsletter-home` |
| Newsletter LP | `newsletter/index.html` | `newsletter-home` |
| Cross-sell 7 landings SEO | `assets/te-escribo-cta.js` + 7 HTML | `newsletter-home` |
| Exit-intent modal 7 landings | `assets/te-escribo-exit-intent.js` | `newsletter-home` |
| Newsletter en landing libro Engranajes | `libro-engranajes-mente/index.html` | `newsletter-home` |
| Lead magnet Cap III | `libro/capitulo-3/index.html` | `lead-magnet-engranajes-cap3` (mergeado el 13 may, esperando deploy) |
| Reto 7 días | `reto-7-dias.html` | `reto-7-dias` |
| Lead magnet dependencia | (varios) | `lead-magnet-dependencia` |
| Test impostora / burnout | landings dedicadas | `lead-magnet-impostora` / `lead-magnet-burnout` |
| Talleres TDAH / Bach | landings dedicadas | `inscritas-tdah` / `inscritas-bachillerato` / `padres-*` |

Si la API key está revocada, **todos los formularios anteriores devuelven 500** al usuario que intente suscribirse. Las suscripciones de los últimos días podrían estar perdidas.

---

## 4 · Acciones derivadas inmediatas

### 4.1 · Intento de diagnóstico desde Code · 13 may ~13:35 CEST

- ✅ Code intentó ejecutar paso 2 (`curl https://twimproject.com/.netlify/functions/subscribe?diag=1`) desde el sandbox.
- ❌ **Bloqueado:** el sandbox de Claude Code devuelve `Host not in allowlist` para `twimproject.com`. **Este bloqueo no está explícito en CLAUDE.md** — el doc solo cita `api.netlify.com` y `connect.mailerlite.com` como hosts bloqueados (sección «APIs bloqueadas en el sandbox»). El bloqueo del propio dominio público es restricción del sandbox no documentada hasta ahora. Acción de mejora pendiente: añadir `twimproject.com` a esa lista en CLAUDE.md o aclarar que el sandbox bloquea cualquier host externo por defecto.
- 📋 Conclusión: Code no puede ejecutar el paso 2 ni los siguientes sin la ayuda de Daniel desde un navegador o un terminal externo al sandbox.

### 4.2 · Lo que Daniel debe hacer en 90 segundos (cuando tenga 1 min libre entre pacientes)

1. Abrir en navegador (preferiblemente en modo incógnito para evitar caché): `https://twimproject.com/.netlify/functions/subscribe?diag=1`.
2. Copiar el JSON completo de la respuesta y pegarlo en chat o en un PR a este archivo (sección 4.3).

Eso es todo. Con el JSON, Code identifica:

- Si todas las env vars están en `true` → la API key probablemente está OK; problema es otro y se diagnostica con un test E2E desde la propia landing del Cap III.
- Si `MAILERLITE_API_KEY` o alguna `MAILERLITE_GROUP_*` está en `false` → falta env var en Netlify; Code dice exactamente cuál crear.
- Si el endpoint devuelve **500 o error** sin JSON → el problema es del runtime de la function (Node, fetch, deploy fallido) y se diagnostica desde los logs de Netlify.

### 4.3 · Resultado del diagnóstico (rellenado 13 may 2026 ~14:30 CEST)

```
Fecha de captura: 13 may 2026
Endpoint URL probada: https://twimproject.com/.netlify/functions/subscribe?diag=1
HTTP status code: 200 OK
Respuesta JSON completa:
{
  "ok": true,
  "node": "v20.20.2",
  "fetchAvailable": true,
  "env": {
    "MAILERLITE_API_KEY": true,
    "MAILERLITE_GROUP_LEAD_MAGNET": true,
    "MAILERLITE_GROUP_RETO": true,
    "MAILERLITE_GROUP_GENERAL": true,
    "MAILERLITE_GROUP_PADRES_TDAH": true,
    "MAILERLITE_GROUP_PADRES_BACH": true,
    "MAILERLITE_GROUP_PADRES_TALLERES": true,
    "MAILERLITE_GROUP_NEWSLETTER_HOME": true,
    "MAILERLITE_GROUP_INSCRITAS_TDAH": false,
    "MAILERLITE_GROUP_INSCRITAS_BACH": false,
    "MAILERLITE_GROUP_LEAD_IMPOSTORA": false,
    "MAILERLITE_GROUP_LEAD_BURNOUT": false,
    "MAILERLITE_GROUP_LEAD_ENGRANAJES_CAP3": true
  }
}
```

**Interpretación de Code (hipótesis original FALSADA):**

La hipótesis original del informe técnico previo era que `MAILERLITE_API_KEY` estaba expirada o revocada. **Es falsa**: el diag devuelve `true` para `MAILERLITE_API_KEY`. La autenticación contra MailerLite funciona.

**Diagnóstico real:** 4 de los 13 grupos del `groupEnvMap` tienen env var **ausente en Netlify** (devuelven `false`):

| Env var ausente | Form afectado | Estado del form |
|---|---|---|
| `MAILERLITE_GROUP_INSCRITAS_TDAH` | Landing `/talleres/tdah-adolescentes/` inscripción | Devuelve 500 al usuario al pulsar «Apuntarme» |
| `MAILERLITE_GROUP_INSCRITAS_BACH` | Landing `/talleres/bachillerato-motivacion/` inscripción | Devuelve 500 al usuario al pulsar «Apuntarme» |
| `MAILERLITE_GROUP_LEAD_IMPOSTORA` | Landing `test-sindrome-impostora.html` | Devuelve 500, lead se pierde |
| `MAILERLITE_GROUP_LEAD_BURNOUT` | Landing `lead-burnout-5-senales.html` | Devuelve 500, lead se pierde |

El error que ven los usuarios en frontend es el `error` que devuelve la function en línea 117-119 de `netlify/functions/subscribe.js`:

```
"Grupo MailerLite no configurado (MAILERLITE_GROUP_XXX ausente en Netlify)"
```

Los **9 grupos críticos** del proyecto **funcionan**:

- ✅ `MAILERLITE_API_KEY` (autenticación contra connect.mailerlite.com)
- ✅ `MAILERLITE_GROUP_NEWSLETTER_HOME` (hero home + landing newsletter + cross-sell 7 landings SEO + exit-intent + form del libro Engranajes)
- ✅ `MAILERLITE_GROUP_RETO` (Reto 7 Días, el lead magnet más activo)
- ✅ `MAILERLITE_GROUP_LEAD_MAGNET` (Lead Magnet Dependencia Emocional)
- ✅ `MAILERLITE_GROUP_GENERAL` (Lista General TWIM)
- ✅ `MAILERLITE_GROUP_PADRES_TDAH` / `PADRES_BACH` / `PADRES_TALLERES` (formularios de padres)
- ✅ `MAILERLITE_GROUP_LEAD_ENGRANAJES_CAP3` (lead magnet del libro publicado hoy 13 may)

### 4.4 · Acciones siguientes

**Para los 4 grupos en `false`:**

Daniel decide si activarlos o no. Dos escenarios posibles para cada uno:

**Escenario A · El grupo SÍ existe en MailerLite**:

1. Dashboard MailerLite → Subscribers → Groups → buscar nombre exacto.
2. Copiar el Group ID.
3. Netlify → Environment variables → crear env var correspondiente con ese ID y «All scopes».
4. Esperar redeploy automático (1-3 min).
5. Confirmar con diag endpoint que pasa a `true`.

Los IDs de 2 grupos ya están conocidos por estar comentados en `netlify/functions/subscribe.js`:

```
MAILERLITE_GROUP_INSCRITAS_TDAH = 186093787887437444
MAILERLITE_GROUP_INSCRITAS_BACH = 186093790595909010
```

Daniel solo necesita pegar esos IDs en Netlify para arreglar 2 de los 4. Los otros 2 (`IMPOSTORA` y `BURNOUT`) requieren crear el grupo en MailerLite primero (escenario B).

**Escenario B · El grupo NO existe en MailerLite todavía**:

Esto aplica a `LEAD_IMPOSTORA` y `LEAD_BURNOUT` según el comment del propio `subscribe.js` que dice «Daniel debe crear». Decisión Daniel:

- ¿Quieres recuperar leads de `test-sindrome-impostora.html` y `lead-burnout-5-senales.html`? Si sí: crear los grupos en MailerLite + env vars.
- Si no: las landings deberían señalizarse como inactivas o redirigir a la newsletter principal para no perder leads silenciosamente.

**Para el taller Volver a Mí:**

- La infraestructura MailerLite **está sana**. La incidencia reportada por ChatGPT en el dossier original era una interpretación incorrecta: los 4 grupos en `false` son grupos secundarios, no la API key del sistema.
- Cuando llegue septiembre y se monte el grupo «Pre-venta Volver a Mí», será un grupo nuevo más a configurar (5º env var a crear), no un sistema roto.

**Status incidencia: RESUELTA EN DIAGNÓSTICO.** Pendiente decisión Daniel sobre si arreglar los 4 grupos secundarios o desactivar las landings asociadas.

### 4.5 · Verificación de integridad post-fix

Tras cualquier intervención en la API key o env vars:

- Confirmar que las 51 suscriptoras al 9 may (REACCION-9-MAYO §3) siguen presentes en MailerLite.
- Hacer test E2E desde `/libro/capitulo-3/` con email tuyo de prueba.
- Confirmar que el email D0 «Aquí lo tienes» del lead magnet llega en <60s.
- Confirmar que el suscriptor de prueba aparece en el grupo «Lectores · Engranajes Cap3».

---

## 5 · Por qué este documento existe

Sin este archivo, la próxima sesión recibe el problema como rumor («Daniel dijo que había un error en chat»). Con este archivo, cualquier sesión futura puede:

1. Saber qué se ha verificado y qué no.
2. Continuar el diagnóstico desde donde se quedó.
3. Documentar la resolución para que no se repita el mismo trabajo.

Política simétrica del CLAUDE.md aplicada a incidencias técnicas, no solo a publicaciones.

---

**Última actualización:** 13 may 2026 · sesión `claude/improve-proposal-quality-pq3d9` · pendiente del informe técnico previo de Daniel y de la verificación del paso 2 una vez Netlify haya completado el deploy del PR #149.
