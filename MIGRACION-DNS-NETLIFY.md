# Migración DNS: GitHub Pages → Netlify (twimproject.com)

> **Contexto:** Los formularios de captación (Reto 7 Días, Lead Magnet Dependencia Emocional) están rotos porque el dominio `twimproject.com` se sirve desde GitHub Pages, que no soporta Netlify Functions. La función backend (`/.netlify/functions/subscribe`) existe y funciona correctamente en `lighthearted-kitten-8aba94.netlify.app` con todas las env vars configuradas. Este documento es el playbook para migrar el dominio a Netlify.
>
> **Tiempo total:** 30 min de trabajo activo + 1-48h de propagación DNS.
>
> **Cuándo hacerlo:** En horario de baja actividad (madrugada, fin de semana). Durante la propagación el site puede servirse intermitentemente desde GitHub o Netlify, no es momento de tener anuncios pagados activos.

---

## Pre-flight (5 min)

Antes de tocar nada, recopila esto:

- [ ] **Acceso al panel de Netlify** (cuenta TWIMProject) — debes poder llegar al site `lighthearted-kitten-8aba94`.
- [ ] **Acceso al registrador de dominios** donde compraste `twimproject.com`. Para averiguar cuál es si no te acuerdas, ve a https://lookup.icann.org/ y busca `twimproject.com`. En el resultado, campo `Registrar`, aparece (típicamente Namecheap, GoDaddy, IONOS, Google Domains, Cloudflare, OVH, etc.).
- [ ] **Acceso al email asociado al dominio** (algunos registradores piden confirmación por email para cambios de DNS).
- [ ] **Saber qué emails usa el dominio**. Si tienes correo `@twimproject.com` (Google Workspace, Zoho, etc.), los registros MX apuntan a su servidor — NO los toques. Solo cambiamos los registros A y CNAME del web.

**Verificar configuración actual de DNS** (informativo, para tener constancia de qué cambia):

Abre Terminal en el ordenador y ejecuta:

```bash
dig twimproject.com +short
dig www.twimproject.com +short
dig MX twimproject.com +short
```

Apunta los valores devueltos. Los A records actuales deberían ser IPs de GitHub Pages: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`.

---

## Paso 1 · Añadir el dominio en Netlify (5 min)

1. Netlify → site `lighthearted-kitten-8aba94` → **Project navigation** → **Domain management** (también puede aparecer como "Domains" o "Custom domains").
2. **Add a domain you already own** (o "Add custom domain") → escribir `twimproject.com` → **Verify** → **Yes, add domain**.
3. Netlify detecta que el dominio no apunta a sus servidores y muestra un panel con los registros DNS que necesitas configurar. **Apunta exactamente los valores que te muestra** (pueden variar según la región y momento, no asumas IPs).
4. Repite para añadir `www.twimproject.com` como dominio secundario.
5. **Decide qué versión es la primaria:** apex (`twimproject.com`) o `www`. Recomendación: apex como primario, `www` redirige al apex (es la convención del site actual; mira los enlaces internos en `index.html`, todos usan apex sin `www`).
6. Netlify ofrecerá emitir un **certificado SSL Let's Encrypt** automáticamente cuando el DNS esté correctamente apuntando. Por ahora marca "Provision SSL" pero todavía no funcionará (falta el DNS).

---

## Paso 2 · Cambiar los registros DNS en el registrador (10 min)

Hay **dos caminos**, elige uno:

### Camino A · Netlify DNS (recomendado, más limpio a largo plazo)

Delegas el dominio entero a los nameservers de Netlify. A partir de ese momento gestionas todo el DNS desde Netlify.

1. En Netlify → Domain management → en `twimproject.com` clic en **Set up Netlify DNS** (o "Use Netlify DNS").
2. Netlify te dará 4 nameservers tipo:
   ```
   dns1.p01.nsone.net
   dns2.p01.nsone.net
   dns3.p01.nsone.net
   dns4.p01.nsone.net
   ```
   (los valores exactos pueden cambiar; copia los que te dé Netlify, no los de este documento).
3. Ve al panel de tu **registrador** → busca la sección **Nameservers** o "DNS" o "Servidores de nombres" del dominio `twimproject.com`.
4. Cambia de "Default nameservers" a "Custom nameservers" → pega los 4 que te dio Netlify → guardar.
5. **IMPORTANTE:** si tienes correo en este dominio (MX records), antes de cambiar los nameservers ve a Netlify DNS y añade manualmente los MX records que ya tenías. Si no, te quedas sin email durante la transición.

### Camino B · Solo cambiar registros A/CNAME (sin delegar)

Mantienes la gestión DNS en el registrador, solo cambias los registros del web.

1. En el panel del registrador → DNS records de `twimproject.com`.
2. **Borrar** los 4 A records que apuntan a GitHub Pages:
   - `@` → `185.199.108.153`
   - `@` → `185.199.109.153`
   - `@` → `185.199.110.153`
   - `@` → `185.199.111.153`
3. **Añadir** los nuevos A records que Netlify te indicó en el Paso 1 (típicamente apuntan a `75.2.60.5` o un único IP del load balancer de Netlify; consulta el valor exacto en el panel de Netlify, no copies de este documento).
4. **Modificar el CNAME de `www`**:
   - Borrar el actual: `www` → `twimproject.github.io` (o similar).
   - Añadir nuevo: `www` → `lighthearted-kitten-8aba94.netlify.app` (sin `https://`, sin barra final).
5. **NO toques los registros MX, TXT (SPF/DKIM/DMARC), ni ningún otro CNAME que no sea `www`.**

### Pistas según registrador

| Registrador | Ruta típica |
|-------------|-------------|
| Namecheap | Domain List → Manage → Advanced DNS |
| GoDaddy | My Products → Domain → DNS |
| IONOS | Dominios & SSL → Dominio → DNS |
| Google Domains / Squarespace | DNS → Custom records |
| Cloudflare | Websites → twimproject.com → DNS → Records |
| OVH | Web Cloud → Dominios → DNS |
| Hostinger | Domains → twimproject.com → DNS / Nameservers |

---

## Paso 3 · Esperar propagación (1-48h, normalmente <2h)

La propagación DNS no es instantánea. Mientras tanto:

- **NO modifiques nada más en DNS** durante esas horas.
- **NO desactives GitHub Pages todavía**. Si lo haces antes de que DNS propague, el site queda caído en los nodos que aún resuelven a GitHub.

Comprueba el progreso desde Terminal cada 15-30 min:

```bash
dig twimproject.com +short
```

Cuando veas que ya devuelve la IP de Netlify (no la de GitHub `185.199.x.x`), está propagado para ti. También puedes usar https://www.whatsmydns.net/ → introduce `twimproject.com` tipo `A` → te muestra cómo resuelve desde varios países. Cuando la mayoría aparezcan en verde con la IP de Netlify, ya es seguro.

---

## Paso 4 · Verificar que la web funciona desde Netlify

Una vez DNS propagado:

1. Abre `https://twimproject.com` en modo incógnito → debe cargar la home con el contenido habitual y un certificado SSL válido (candado verde, expedido por Let's Encrypt vía Netlify).
2. Abre `https://twimproject.com/.netlify/functions/subscribe?diag=1` → debe devolver el JSON con `"ok":true` y todas las env vars en `true`.
3. Abre `https://twimproject.com/reto-7-dias.html` → rellena el formulario con un email de prueba real → envía. Debe mostrar "¡Estás dentro! 🎉".
4. Comprueba en MailerLite → Subscribers → busca el email → debe aparecer en el grupo `Reto 7 Días - Inscritas` en menos de 1 minuto.
5. Comprueba en MailerLite → Automations → la cola debe haber incrementado en 1.

Si algo de esto falla, **NO sigas al paso 5**. Avísame y revisamos.

---

## Paso 5 · Limpiar GitHub Pages (5 min)

Solo cuando los pasos 1-4 estén verdes:

1. **Borrar el archivo `CNAME` del repo:**
   ```bash
   git checkout main
   git pull
   git rm CNAME
   git commit -m "chore: remove CNAME (dominio migrado a Netlify)"
   git push
   ```
   Mientras este archivo exista, GitHub Pages reclama el dominio. Borrarlo libera la reclamación.

2. **Desactivar GitHub Pages en el repo:**
   - GitHub → repo `theworldismindproject` → **Settings** → **Pages** → en "Source" cambiar a "None" (o "Deploy from a branch" → branch `gh-pages` que no exista).
   - El custom domain campo debería quedar vacío.

3. **Verificación final:** vuelve a abrir `https://twimproject.com` → sigue cargando (ahora 100% desde Netlify, sin posibilidad de servirse desde GitHub).

---

## Plan de rollback (si algo va catastróficamente mal)

Si tras propagar el DNS la web no carga o el email se rompe:

1. **Vuelve a poner los registros A originales en el registrador** (los de GitHub Pages: `185.199.108.153`, `.109.153`, `.110.153`, `.111.153`).
2. **Vuelve a poner el CNAME de `www`** apuntando a `twimproject.github.io`.
3. Si delegaste a Netlify DNS, vuelve a poner los nameservers originales del registrador (busca en su documentación cuáles son los suyos por defecto).
4. Espera de nuevo a que propague.

El estado original es totalmente recuperable mientras NO borres el archivo `CNAME` del repo.

---

## Resumen de qué cambia y qué no

| Pieza | Antes | Después |
|-------|-------|---------|
| Quién sirve `twimproject.com` | GitHub Pages | Netlify |
| Hosting de archivos estáticos | GH Pages desde `main` | Netlify desde `main` (ya estaba, solo no se usaba) |
| Netlify Functions (`/subscribe`) | No accesibles desde el dominio | Accesibles |
| Certificado SSL | GitHub Pages (Let's Encrypt) | Netlify (Let's Encrypt) |
| Email `@twimproject.com` | Sin cambios | Sin cambios (si conservas MX records) |
| Código del repo | Sin cambios | Solo se borra `CNAME` al final |
| Forms del Reto y Lead Magnet | Rotos (404 al backend) | Funcionando (backend conectado) |

---

## Si no quieres / no puedes hacer la migración DNS

Alternativa puente que funciona en GitHub Pages (sin tocar DNS):

- Crear formularios "Embedded" en el panel de MailerLite (uno para grupo Reto, uno para grupo Lead Magnet).
- MailerLite genera un snippet HTML+JS que hace POST directo a sus servidores desde el navegador.
- Reemplazar los `<form>` actuales en `reto-7-dias.html` y donde aplique con ese snippet.

Pierdes algo de control del diseño (los embeds de MailerLite tienen estilo propio, ajustable hasta cierto punto con CSS) pero captas leads ya, sin esperar propagación DNS. Si vas por aquí, dime y lo monto cuando me pases los snippets.
