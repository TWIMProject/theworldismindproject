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

### 2.3 SEO — Landings de posicionamiento (EN CURSO ⚙️)
Se están creando 7 páginas HTML nuevas para mejorar el posicionamiento en Google por términos de búsqueda relevantes. El planteamiento es que cada página capture tráfico de búsqueda orgánica con keyword específica y convierta a primera consulta.

| # | Archivo | Keyword principal | Estado |
|---|---------|-------------------|--------|
| 1 | `daniel-orozco-abia.html` | "Daniel Orozco Abia psicólogo" | **Creada ✅** |
| 2 | `psicologo-ansiedad-valencia.html` | "psicólogo ansiedad Valencia" | En proceso ⚙️ |
| 3 | `psicologo-dependencia-emocional-valencia.html` | "psicólogo dependencia emocional Valencia" | Pendiente |
| 4 | `psicologo-burnout-valencia.html` | "psicólogo burnout Valencia" | Pendiente |
| 5 | `psicologo-adolescentes-valencia.html` | "psicólogo adolescentes Valencia" | Pendiente |
| 6 | `terapia-pareja-valencia.html` | "terapia pareja Valencia" | Pendiente |
| 7 | `psicologo-online.html` | "psicólogo online" | Pendiente |

Cada landing incluye:
- Meta SEO (title, description, keywords, canonical, OG, Twitter)
- Schema.org JSON-LD (MedicalBusiness / Service / BreadcrumbList / FAQPage)
- Contenido clínico específico del tema en voz de Daniel
- Enlace a artículos insights relacionados
- CTA a primera consulta (email + WhatsApp)

Pendiente tras crear las landings:
- Actualizar `sitemap.xml` con las 7 nuevas URLs
- Añadir links desde `index.html` e insights relevantes hacia las landings
- Commit + push a la rama activa

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

### 3.1 Auditoría MailerLite (pendiente de ejecutar localmente)
El sandbox de Claude no tiene acceso de red a `connect.mailerlite.com`. La auditoría hay que lanzarla en la máquina local de Daniel (Windows 11).

**Qué verificar cuando se lance el script:**
- [ ] Grupo `Reto 7 Días` existe con ID correcto → coincide con `MAILERLITE_GROUP_RETO` en Netlify
- [ ] Automatización `Reto 7 Días` está en estado **ACTIVE**
- [ ] Dominio `twimproject.com` autenticado con SPF + DKIM en verde
- [ ] Conteo de suscriptores en el grupo Reto
- [ ] No hay suscriptores atascados en la secuencia

**Cómo lanzar en Windows 11:**
```powershell
cd C:\...\theworldismindproject
powershell -ExecutionPolicy Bypass -File scripts\audit-mailerlite-netlify.ps1
```

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
