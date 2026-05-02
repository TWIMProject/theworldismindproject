# GitHub hardening · Checklist para TWIM Project

> Documento de referencia · 1 mayo 2026
> Acciones que requieren UI de GitHub (Claude no puede ejecutarlas).
> Cuando Daniel pregunte sobre seguridad del repo, abrir este doc.

---

## TL;DR — qué hacer en orden de prioridad

| Prioridad | Acción | Tiempo | Donde |
|---|---|---|---|
| 🔴 Crítico | Activar Branch Protection en `main` | 5 min | Settings → Branches |
| 🔴 Crítico | Activar Secret Scanning + Push Protection | 2 min | Settings → Code security |
| 🔴 Crítico | Verificar 2FA en cuenta personal Daniel | 5 min | github.com/settings/security |
| 🟡 Alto | Activar Dependabot Alerts | 1 min | Settings → Code security |
| 🟡 Alto | Confirmar visibilidad del repo (privado recomendado) | 1 min | Settings → General |
| 🟢 Medio | Restringir GitHub Actions permissions | 3 min | Settings → Actions → General |
| 🟢 Medio | Limpiar branches mergeadas antiguas | 10 min | Branches |
| ⚪ Opcional | Purgar token Netlify del historial git | 30 min | Local (git filter-repo) |

---

## 1 · Branch Protection en `main` (CRÍTICO)

**Por qué importa:** sin esto, cualquiera con write access puede hacer push directo a `main`, force-push, o borrar la rama. El repo perdería control de calidad.

**Cómo:**

1. Ir a `https://github.com/TWIMProject/theworldismindproject/settings/branches`.
2. Click **"Add branch ruleset"** (o "Add classic branch protection rule" si prefieres modo simple).
3. Nombre: `main`.
4. Activar:
   - ✅ **Require a pull request before merging** (no push directo).
     - ✅ Require approvals: **1** (mínimo).
     - ✅ Dismiss stale pull request approvals when new commits are pushed.
     - ✅ Require review from Code Owners.
   - ✅ **Require status checks to pass before merging**.
     - Añadir: `Gitleaks` (cuando el workflow corra al menos una vez).
     - Añadir: `netlify/lighthearted-kitten-8aba94/deploy-preview` (cuando aparezca).
     - ✅ Require branches to be up to date before merging.
   - ✅ **Require conversation resolution before merging**.
   - ✅ **Require signed commits** (opcional, si configuras GPG).
   - ✅ **Require linear history** (opcional, evita merge commits).
   - ✅ **Do not allow bypassing the above settings** (importante: aplicar incluso a admins).
   - ✅ **Restrict who can push to matching branches**: solo Daniel.
   - ✅ **Allow force pushes**: NO.
   - ✅ **Allow deletions**: NO.
5. Save.

> **Nota práctica:** durante la fase actual (Daniel solo + Claude), "require 1 approval" puede frenar tu flow. Alternativa: dejarlo SIN require approval pero CON status checks obligatorios. Cuando entre la VA o Sergio, activar require approval.

---

## 2 · Secret Scanning + Push Protection (CRÍTICO)

**Por qué importa:** ya pasó una vez (token Netlify expuesto). Push protection bloquea automáticamente cualquier intento de pushear secretos detectados antes de que entren al repo.

**Cómo:**

1. Ir a `https://github.com/TWIMProject/theworldismindproject/settings/security_analysis`.
2. Activar:
   - ✅ **Secret scanning** → Enable.
   - ✅ **Push protection** → Enable.
   - ✅ **Dependency graph** → Enable.
3. Save.

A partir de ese momento: si intentas pushear un commit con un token detectable (Stripe, AWS, GitHub PAT, Netlify, etc.), GitHub lo bloquea **antes** de aceptar el push.

---

## 3 · 2FA en cuenta personal de Daniel (CRÍTICO)

**Por qué importa:** sin 2FA, una contraseña filtrada da acceso total al repo + organización + capacidad de borrar todo.

**Cómo:**

1. Ir a `https://github.com/settings/security`.
2. Si dice "Two-factor authentication: not enabled" → click **Enable two-factor authentication**.
3. Recomendado: app autenticadora (Authy, Google Authenticator, 1Password) — más seguro que SMS.
4. Guardar **códigos de recuperación** en gestor de contraseñas (no en notas, no en email).
5. Verificar que la org TWIMProject también tiene 2FA enforcement: `https://github.com/organizations/TWIMProject/settings/security` → "Require two-factor authentication" → enable.

---

## 4 · Dependabot Alerts (ALTO)

**Por qué importa:** notifica de vulnerabilidades en dependencias (Netlify Functions npm, GitHub Actions). Bajo costo, alto valor.

**Cómo:**

1. Ir a `https://github.com/TWIMProject/theworldismindproject/settings/security_analysis`.
2. Activar:
   - ✅ **Dependabot alerts** → Enable.
   - ✅ **Dependabot security updates** → Enable (PRs automáticos cuando detecta CVE).
   - ✅ **Dependabot version updates** → Ya configurado vía `.github/dependabot.yml` (este PR).

---

## 5 · Visibilidad del repositorio (ALTO)

**Por qué importa:** el repo contiene briefings estratégicos, documentos editoriales internos, plantillas de programa, decisiones de negocio. Si es público, todo es accesible.

**Cómo verificar:**

1. Ir a `https://github.com/TWIMProject/theworldismindproject/settings`.
2. Buscar sección "Danger Zone" → ver visibilidad actual.
3. **Recomendación:** Privado (a menos que haya una razón específica para que sea público — open source, marketing, transparencia).
4. Si está público y quieres pasar a privado: botón "Change visibility" → Private.

> **Aviso:** si el repo ha sido público en algún momento, asume que su contenido completo está indexado/cacheado en otros sitios (archive.org, search caches). Pasar a privado **ahora** evita futura exposición pero no borra el pasado.

---

## 6 · Restringir GitHub Actions permissions (MEDIO)

**Por qué importa:** evita que workflows maliciosos (vía PR de fork) puedan acceder a secretos del repo o modificar releases.

**Cómo:**

1. Ir a `https://github.com/TWIMProject/theworldismindproject/settings/actions`.
2. **Actions permissions:**
   - Recomendado: "Allow [TWIMProject], and select non-[TWIMProject], actions and reusable workflows".
   - Marketplace: solo verificados por GitHub.
3. **Workflow permissions:**
   - Default: "Read repository contents and packages permissions".
   - ❌ NO "Read and write permissions" como default.
   - Cada workflow declara sus permisos explícitamente (el secret-scan.yml ya lo hace).
4. ✅ **Require approval for first-time contributors** → Enable.

---

## 7 · Cleanup de branches antiguas (MEDIO)

**Estado actual:** 30+ branches `claude/*` activas. Muchas ya mergeadas, otras abandonadas. Acumulación reduce visibilidad.

**Cómo:**

1. Ir a `https://github.com/TWIMProject/theworldismindproject/branches`.
2. Filtrar por "Stale" o "Merged".
3. Borrar las ya mergeadas (botón papelera).
4. Las que tienen trabajo no mergeado: revisar antes de borrar (puede haber código útil).

> **Automatizable a futuro:** activar "Automatically delete head branches" en Settings → General → Pull Requests. Cada PR mergeado borra automáticamente su branch.

---

## 8 · Purgar token Netlify del historial (OPCIONAL)

**Estado:** el token literal aparece en 6 commits del historial git (commits `846a807`, `d1d2a51`, `d0c21a7`, `3f43a28`, `8e37f1f`, `95b975a`).

**Riesgo actual:** BAJO. El token ya está revocado (1 mayo 2026), por lo que no es operativo. Pero la presencia de secretos en historial es mala práctica defensiva.

**Cuándo purgar:**
- Si el repo es PÚBLICO o tiene colaboradores externos: **purgar ya**.
- Si el repo es PRIVADO con solo Daniel + Anthropic + bots: opcional.

**Cómo (si decides hacerlo):**

```bash
# 1. Backup completo del repo antes de tocar nada
cp -r theworldismindproject theworldismindproject.backup

# 2. Instalar git-filter-repo (recomendado por GitHub)
brew install git-filter-repo  # macOS
# o: pip install git-filter-repo

# 3. Purgar el token del historial completo
cd theworldismindproject
git filter-repo --replace-text <(echo "nfp_Fe7FsD3Uv9UtsLmz9broLYSad2PKqh9E4d2e==>nfp_***REDACTED***")

# 4. Force-push a remoto (REESCRIBE HISTORIAL — coordina con colaboradores antes)
git push --force --all
git push --force --tags

# 5. Pedir a GitHub que limpie cachés:
#    https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
```

> **Aviso:** force-push reescribe historial. Si hay PRs abiertos, se rompen. Si hay otros colaboradores, deben re-clonar. **Coordinar antes de ejecutar.**

---

## 9 · Notificaciones de seguridad

Asegurarte de que recibes alertas:

1. `https://github.com/settings/notifications` → activar "Vulnerability alerts" por email.
2. `https://github.com/TWIMProject/theworldismindproject/settings/security_analysis` → "Email notifications" → tu email.

---

## 10 · Revisión periódica

| Frecuencia | Acción |
|---|---|
| Mensual | Revisar Dependabot alerts (5 min). |
| Mensual | Revisar branches activas y limpiar mergeadas. |
| Trimestral | Auditar permisos de la org TWIMProject (¿quién tiene acceso?, ¿sigue activo?). |
| Trimestral | Revisar Acceso de OAuth Apps autorizadas (`github.com/settings/applications`). |
| Anual | Rotar Personal Access Tokens incluso sin sospecha de exposición. |
| Anual | Revisar política de seguridad `/.github/SECURITY.md`. |

---

## Cierre

GitHub está bien diseñado: sus protecciones por defecto son razonables, pero **muchas requieren activación explícita**. Las acciones de §1, §2, §3 son las críticas — sin ellas, una credencial filtrada o un colaborador comprometido pueden destruir el repo. Las demás son defensa en profundidad.

Cuando termines este checklist, el repo TWIMProject queda al nivel de hardening que cualquier auditoría profesional consideraría aceptable para un negocio con datos clínicos detrás.

— Notas técnicas: documento generado el 1-05-2026. Si GitHub cambia UI o introduce nuevas funcionalidades de seguridad, revisar §1, §2, §6.
