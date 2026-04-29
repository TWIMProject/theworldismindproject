# TWIM Project · Estado del proyecto — 29 abril 2026

Documento para trasladar el contexto a otro miembro del equipo.
Generado al final de la sesión de trabajo del 29-04-2026.

---

## 1. CONTEXTO GENERAL

- **Proyecto:** TWIM Project (The World Is Mind Project)
- **Titular:** Daniel Orozco Abia · Psicólogo General Sanitario CV11515 · Valencia
- **Web:** https://twimproject.com (alojada en Netlify)
- **Email marketing:** MailerLite
- **Automatizaciones Instagram:** ManyChat
- **Rama de trabajo activa:** `claude/check-manychat-instagram-EQalY`

---

## 2. COMPLETADO EN ESTA SESIÓN

### 2.1 ManyChat — Instagram (LISTO ✅)
Dos automatizaciones creadas y LIVE:

| Automatización | Trigger | Acción |
|---------------|---------|--------|
| DM keyword RETO | Alguien escribe "RETO" en DM | Respuesta automática con enlace al reto de 7 días |
| Comment trigger QUIERO | Alguien comenta "QUIERO" en publicaciones | Envío de DM con enlace al programa |

**Pendiente de diagnóstico:** El keyword RETO no respondió en prueba del cliente.
Causa probable: ManyChat no responde a cuentas propias (Instagram bloquea que te envíes DM a ti mismo). Solución: probar desde una cuenta de Instagram DIFERENTE a la de `@daniorozcopsicologo`.

Checklist de diagnóstico ya redactado en `taller-no-puedo-parar-setup.md`.

### 2.2 YouTube Banner (LISTO ✅)
- Archivo: `youtube-banner-twim.png` (2048×1152 px, 168 KB)
- Todo el contenido dentro del área segura 1235×338 (visible en todos los dispositivos)
- Generado con Python/Pillow, fuente Barlow Condensed, paleta verde/beige de marca
- Listo para subir a YouTube → Personalización → Arte del canal

### 2.3 SEO — Landings de posicionamiento (COMPLETADO ✅)
7 páginas HTML nuevas creadas para mejorar el posicionamiento en Google por términos de búsqueda relevantes. Cada página captura tráfico orgánico con keyword específica y convierte a primera consulta.

| # | Archivo | Keyword principal | Estado |
|---|---------|-------------------|--------|
| 1 | `daniel-orozco-abia.html` | "Daniel Orozco Abia psicólogo" | ✅ |
| 2 | `psicologo-ansiedad-valencia.html` | "psicólogo ansiedad Valencia" | ✅ |
| 3 | `psicologo-dependencia-emocional-valencia.html` | "psicólogo dependencia emocional Valencia" | ✅ |
| 4 | `psicologo-burnout-valencia.html` | "psicólogo burnout Valencia" | ✅ |
| 5 | `psicologo-adolescentes-valencia.html` | "psicólogo adolescentes Valencia" | ✅ |
| 6 | `terapia-pareja-valencia.html` | "terapia pareja Valencia" | ✅ |
| 7 | `psicologo-online.html` | "psicólogo online" en español (LATAM/EU/EE.UU.) | ✅ |

Cada landing incluye:
- Meta SEO completo (title, description, keywords, canonical, Open Graph, Twitter cards)
- 4 schemas JSON-LD: `MedicalBusiness` + `Service` + `BreadcrumbList` + `FAQPage`
- Contenido clínico específico del tema en voz editorial de Daniel
- Cross-linking con artículos relacionados del blog y programas
- CTA a primera consulta (email + WhatsApp)
- GA4 tracking integrado

**Trabajo adicional completado:**
- ✅ `sitemap.xml` actualizado con 7 URLs nuevas (40 URLs totales)
- ✅ Linking interno desde `index.html` (sección "Con quién trabajo" + bio de Daniel)
- ✅ Linking interno desde `dejadeobligarte.html` y `dejadebuscarteenotros.html`
- ✅ Auditoría automática pasada con **0 errores, 0 warnings** en las 7 landings
- ✅ Commits y pushes a `claude/check-manychat-instagram-EQalY`

**Próximos pasos manuales (cuando se desee):**
- Hacer merge de la rama a `main` para que las landings se desplieguen en producción
- Enviar el sitemap actualizado a Google Search Console
- Solicitar indexación manual de las 7 nuevas URLs en GSC

### 2.4 Scripts de auditoría (LISTOS ✅)
Creados en `scripts/`:
- `audit-mailerlite-netlify.sh` — para Mac / Linux (requiere bash + jq)
- `audit-mailerlite-netlify.ps1` — para Windows 11 (PowerShell)

Cómo usarlos:
1. Añadir credenciales al archivo `.env.audit` en la raíz del repo (gitignored, no se sube):
   ```
   NETLIFY_AUTH_TOKEN=nfp_xxxx
   MAILERLITE_API_KEY=eyJxxxx
   ```
2. Ejecutar el script correspondiente según sistema operativo
3. Pegar el output al equipo técnico para revisión

---

## 3. PENDIENTE / BLOQUEADO

### 3.1 Auditoría MailerLite (COMPLETADA ✅ via MCP)

Auditoría hecha el 29-04-2026 vía MailerLite MCP server. **Todo funcionando correctamente.**

**Cuenta:**
- Email autenticado: `danielorozco@twimproject.com` · Account ID: 2232121 · Entorno: producción
- 30 suscriptores totales en la cuenta

**Grupo `Reto 7 Dias - Inscritas`:**
- ID: `183364554663659208` ✅ coincide con env var `MAILERLITE_GROUP_RETO` en Netlify
- 5 suscriptores activos en el grupo (en distintas fases del reto)
- Open rate del grupo: 51.85%

**Automatización `Reto 7 días`:**
- ID: `184902133394442190`
- Estado: **ENABLED ✅**
- 17 pasos (8 emails + 7 delays + 2 acciones post-secuencia)
- 5 personas en cola **progresando sin fallos**
- 0 errores en el log de actividad

**Stats reales de los emails (al 29-04-2026):**
| Email | Enviados | Open rate | Notas |
|-------|----------|-----------|-------|
| D4 "Cuerpo" | 24 | 62.5% | 1 hard bounce |
| D5 "Máscara" | 22 | 68.18% | 100% delivery |
| D7 "Revisión + CTA" | 20 | **70%** · 20% CTR | 1 unsubscribe |

**Otras automatizaciones activas (todas enabled):**
- Secuencia Anti-Test Dependencia Emocional (15 pasos)
- Taller TDAH · Nurturing guía (7 pasos)
- Web - Newsletter Home (3 pasos)

**Conclusión:** El flujo MailerLite está sólido. La conversión Email 7 → CTA programa "Deja de Buscarte en Otros" es del 20% (excelente). No hay nada que arreglar. La acción que produce más impacto ahora es **escalar tráfico** a `reto-7-dias.html` (vía Instagram Ads / contenido orgánico) para llenar la parte alta del embudo.

### 3.2 Netlify — Variables de entorno (verificado via MCP ✅)
En sesión anterior se auditaron con Netlify MCP. Las 8 variables críticas estaban presentes:
- `MAILERLITE_API_KEY` ✅
- `MAILERLITE_GROUP_RETO` ✅ (ID: 183364554663659208)
- `MAILERLITE_GROUP_GENERAL` ✅
- `MAILERLITE_GROUP_LEAD_MAGNET` ✅
- `MAILERLITE_GROUP_PADRES_TDAH` ✅
- `MAILERLITE_GROUP_PADRES_BACH` ✅
- `MAILERLITE_GROUP_PADRES_TALLERES` ✅

**Pendiente en Netlify:** activar MFA (2FA) — actualmente desactivado. Riesgo de seguridad bajo pero recomendado.

### 3.3 Seguridad — Tokens expuestos en chat (ACCIÓN REQUERIDA)
Durante la sesión aparecieron en el chat dos credenciales que **deben rotarse**:

| Credencial | Estado |
|-----------|--------|
| Netlify token `nfp_Fe7FsD3Uv9UtsLmz9broLYSad2PKqh9E4d2e` | ⚠️ Pendiente de revocar y regenerar |
| Token MailerLite "Auditoría Claude" | ✅ Ya eliminado por Daniel |

Para revocar el token Netlify: `https://app.netlify.com/user/applications` → Personal access tokens → revocar el actual → crear uno nuevo → actualizar `.env.audit`.

---

## 4. ESTRUCTURA DE ARCHIVOS RELEVANTES

```
theworldismindproject/
├── index.html                          ← Home (1.493 líneas, pendiente añadir links)
├── daniel-orozco-abia.html             ← Landing SEO marca personal ✅ nueva
├── psicologo-ansiedad-valencia.html    ← Landing SEO ⚙️ en proceso
├── sitemap.xml                         ← Pendiente actualizar con 7 nuevas URLs
├── netlify/functions/subscribe.js      ← Función de suscripción MailerLite ✅ ok
├── email-templates/reto-7-dias/        ← 8 emails HTML (D0–D7) ✅ ok
├── scripts/
│   ├── audit-mailerlite-netlify.sh     ← Script auditoría Mac/Linux ✅ nuevo
│   └── audit-mailerlite-netlify.ps1    ← Script auditoría Windows ✅ nuevo
└── .env.audit                          ← Credenciales locales (gitignored)
```

---

## 5. FLUJO DE CONVERSIÓN ACTUAL

```
Instagram Ad / Post
        ↓
ManyChat → DM automático con enlace
        ↓
twimproject.com/reto-7-dias.html
        ↓
Formulario → Netlify Function subscribe.js
        ↓
MailerLite API → suscriptor en grupo "Reto 7 Días"
        ↓
Automatización MailerLite → 8 emails durante 7 días
        ↓
Email 7 → CTA al programa "Deja de Buscarte en Otros"
```

**Estado del flujo:** Web y función OK. Automatización MailerLite pendiente de verificar en panel.

---

## 6. RAMA DE TRABAJO

```bash
git branch:  claude/check-manychat-instagram-EQalY
git remote:  origin → github.com/twimproject/theworldismindproject
```

Cuando se complete el bloque SEO, se hará commit + push de todo a esta rama. Pendiente PR o merge a main según flujo de despliegue habitual.

---

*Documento generado el 2026-04-29. Para preguntas técnicas, revisar el historial de la sesión Claude Code o contactar al equipo de desarrollo.*
