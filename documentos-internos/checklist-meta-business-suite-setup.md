# Checklist · Setup Meta Business Suite para distribución TWIM

> Documento operativo · 4 mayo 2026
> Paso 2/3 del checklist post-docs (§10 del doc #5).
> Implementa el setup descrito en doc #5 `reciclaje-contenido-pipeline.md` §6.2.
> Audiencia: Daniel ahora; VA cuando entre (sept 2026).

---

## TL;DR

Meta Business Suite (gratis, nativo Meta) es la consola de programación elegida para distribuir las piezas derivadas del podcast (carrusel A1, cita A2, Reels) en IG + FB durante T1 (mayo-agosto 2026). Cubre ~80% de los derivados sin coste. LinkedIn y newsletter se gestionan aparte.

Tiempo estimado total del setup: **45-90 min** una sola vez.

---

## Pre-requisitos antes de empezar

- [ ] Acceso administrador a la cuenta de IG `@daniorozcopsicologo`.
- [ ] Acceso administrador a la página de FB de TWIM (si no existe la página, crearla antes — Meta Business Suite exige página FB vinculada).
- [ ] Cuenta de Meta Business (gratis · `business.facebook.com`). Si Daniel no la tiene, crearla con cuenta de Meta primaria.
- [ ] Logo TWIM y cover en formatos correctos (ya disponibles en repo).
- [ ] Decisión sobre titularidad de la cuenta Business: ¿personal de Daniel o cuenta corporativa TWIM? (recomendado corporativa cuando se formalice; mientras tanto, personal).
- [ ] **Credenciales gestionadas en gestor de contraseñas** (1Password, Bitwarden o equivalente). Usuario, contraseña y **códigos de recuperación 2FA** se guardan ahí. Coherente con `documentos-internos/github-hardening-checklist.md`. **No** se guardan credenciales en notas, email, mensajes ni en el repo.

---

## Paso 1 · Clasificar IG como cuenta Profesional

**Por qué:** sin esto, Meta Business Suite no puede programar publicaciones a IG. La cuenta Personal no tiene permisos de API.

1. Abrir IG móvil → perfil `@daniorozcopsicologo`.
2. Menú (≡) → Configuración y privacidad → Tipo de cuenta y herramientas.
3. Cambiar a **Cuenta profesional** → seleccionar "Empresa" (no "Creador").
4. Categoría sugerida: "Servicios psicológicos" o "Consultor de salud mental".
5. Vincular a página de FB de TWIM cuando lo pida.
6. Guardar.

**Validación:** volver al perfil → debe aparecer botón "Insights / Estadísticas" (solo aparece en cuentas profesionales).

---

## Paso 2 · Conectar página FB + IG en Meta Business

1. Ir a `business.facebook.com` con la cuenta de Daniel.
2. Menú izquierda → **Configuración del negocio** → **Cuentas**.
3. **Páginas** → "Añadir" → seleccionar la página de TWIM en FB. Si la página no aparece, asegurarse de que Daniel es admin de esa página desde su cuenta personal de FB.
4. **Cuentas de Instagram** → "Añadir" → conectar `@daniorozcopsicologo`. Confirmar con código de IG.
5. Asegurar que ambas (FB + IG) aparecen bajo el **mismo Business Manager**.

**Validación:** en el dashboard de Business Manager, ver ambos activos listados como "Conectados".

---

## Paso 3 · Abrir Meta Business Suite

1. Ir a `business.facebook.com/latest/home`.
2. En el selector superior izquierdo, asegurarse de que está seleccionado el Business Manager correcto y la página de TWIM.
3. Confirmar que en la barra superior aparecen los iconos de FB e IG vinculados (debería verse "Página + IG").

---

## Paso 4 · Configurar zona horaria y roles

### 4.1 · Zona horaria

1. Configuración del negocio → **Información del negocio** → **Zona horaria**.
2. Establecer **Europa / Madrid**.
3. Confirmar que el calendario de programación se muestra en hora local correcta.

### 4.2 · Roles iniciales

| Persona | Rol Business Manager | Rol página FB | Rol IG |
|---|---|---|---|
| Daniel Orozco | Admin | Admin | Admin |
| VA (cuando entre) | Empleado | Editor | Editor |
| Backup emergencia (persona de confianza) | Admin (segunda cuenta) | Admin | Admin |

**Por qué backup:** si Daniel pierde acceso a su cuenta personal Meta, el negocio no debe quedar bloqueado. Tener una segunda cuenta admin (familiar de confianza, gestor) evita ese riesgo. **El backup necesita rol Admin también en IG**, no solo en FB y Business Manager — sin acceso al asset de Instagram, en un incidente no podría recuperar la vinculación IG/MBS ni operar la cuenta de IG.

### 4.3 · Asignar al backup acceso al asset de IG

1. Configuración del negocio → **Cuentas** → **Cuentas de Instagram** → seleccionar `@daniorozcopsicologo`.
2. Pestaña **Personas** → "Añadir personas" → invitar la segunda cuenta del backup → asignar rol **Admin de Instagram**.
3. Confirmar invitación desde la cuenta del backup.
4. Validar que el backup puede acceder a IG desde Business Manager con su segunda cuenta.

> No dar rol Admin a la VA. Solo Editor — basta para programar y responder, no permite cambios estructurales.

---

## Paso 5 · Crear plantilla de calendario semanal

Meta Business Suite permite arrastrar piezas a slots fijos. La plantilla TWIM:

| Día | Slot | Pieza típica del pipeline |
|---|---|---|
| Lunes | 19:00 | Episodio nuevo en YouTube/Spotify (no se programa desde MBS, pero se ancla aquí) |
| Martes | 09:00 | Newsletter "Te escribo" (no MBS; ancla calendario) |
| Miércoles | 19:00 | Carrusel A1 IG (Pieza #4) |
| Jueves | 19:00 | Reel #1 (Pieza #3) |
| Viernes | 12:00 | Cita visual A2 IG (Pieza #5) |
| Sábado | 11:00 | Reel #2 (Pieza #3) |
| Domingo | 19:00 | Reel #3 o stories del episodio |

> Estos horarios son hipótesis razonables para audiencia España (mujer 25-50). Ajustar tras 4-6 semanas con datos de Insights de IG.

**Cómo crear la plantilla en MBS:**

1. Planificador → Calendario → vista semanal.
2. Por cada slot, crear una publicación borrador con etiqueta `[PILOTO]` y fecha-hora del slot.
3. Guardar como borradores. Cuando entre el episodio E5, se rellenan estos borradores con piezas reales.

---

## Paso 6 · Validar programación de Reels

**Riesgo conocido:** algunas cuentas reportan limitaciones programando Reels desde Meta Business Suite (la API de Reels ha tenido bugs intermitentes 2024-2026).

### Test de validación

1. Crear un Reel corto de prueba (10-15 s, contenido neutro tipo "Próximamente: TWIM Podcast E5").
2. **Subir un cover branded** (no dejar que IG use frame automático) según el sistema visual del PR #94 — ver `documentos-internos/instagram-sistema-visual-marca.md` sobre "Cover obligatorio". El cover branded es el estándar TWIM y el test debe validar específicamente que la programación lo respeta.
3. Programar para 2 horas más tarde desde Meta Business Suite.
4. Esperar la hora programada.
5. Verificar:
   - Que aparece publicado en IG.
   - Que el cover branded subido se mantiene **sin sustituirse por un frame automático**. Si MBS sustituye el cover, es un fallo bloqueante — activa Plan B.
6. Borrar el Reel de prueba tras validar.

### Si la programación de Reels falla

Plan B documentado en doc #5 §6.2:

- Programar el Reel desde **IG nativa** (app móvil) usando la opción "Programar" del propio IG.
- Coordinar manualmente desde calendario externo (Notion / Google Calendar) hasta que Meta arregle la API.
- Si el problema persiste 2+ meses, escalar la evaluación de Metricool antes de los 4-5 meses originales (doc #5 §6.3).

---

## Paso 7 · Chequeos finales

- [ ] Página FB y cuenta IG vinculadas y visibles en MBS.
- [ ] Zona horaria Europa/Madrid configurada.
- [ ] Daniel con rol Admin, backup admin con segunda cuenta.
- [ ] Plantilla de calendario semanal creada con borradores en cada slot.
- [ ] Test de programación de Reels superado (o Plan B documentado si falla).
- [ ] Notificaciones de MBS configuradas (alertas a email Daniel cuando una publicación falla al publicar).
- [ ] Inbox unificado de IG + FB activado en MBS para responder DMs y comentarios desde una sola consola.
- [ ] 2FA activado en cuenta Meta de Daniel y en cuenta backup.

---

## Notas para el handoff a la VA (sept 2026)

Cuando la VA entre, este documento se le entrega como referencia operativa. Antes:

- Revisar que la VA ya ha sido añadida con rol Editor (paso 4.2).
- Sesión de onboarding de 60 min con la VA repasando los 7 pasos en pantalla compartida.
- Acordar protocolo de aprobación antes de programar: ninguna pieza se publica sin "ok Daniel" durante el primer mes de delegación (ver doc #5 §7.4 política de revisión).

---

## Lo que NO se hace desde Meta Business Suite

- Publicar en YouTube. YouTube se gestiona desde YouTube Studio (no hay MBS para vídeo largo).
- Publicar en LinkedIn. LinkedIn se gestiona desde LinkedIn nativo o, si entra Metricool a 4-5 meses, desde ahí.
- Enviar newsletter. MailerLite es la consola de newsletter, no MBS.
- Responder DMs sobre temas clínicos delicados sin revisión Daniel. Política de moderación humana (doc #3 §11).

---

## Riesgos y mitigaciones del setup

| Riesgo | Mitigación |
|---|---|
| Meta cambia API y la plantilla de calendario se rompe | Mantener calendario maestro en Notion o Google Sheets como fuente de verdad. MBS es ejecutor, no archivo. |
| Daniel pierde acceso a cuenta Meta personal | Backup admin con segunda cuenta (paso 4.2). |
| VA programa pieza con error tonal | Política de aprobación previa primer mes (doc #5 §7.4). |
| Reels siguen fallando al programar | Plan B IG nativa, escalado a Metricool (paso 6). |
| Audiencia no responde a horarios elegidos | Revisar Insights tras 4-6 semanas y ajustar horarios. |

---

## Después del setup

Cuando los 7 pasos estén tachados:

1. Marcar como completada la línea correspondiente del checklist §10 del doc #5.
2. Continuar al paso 3 del flujo: hoja de cronometraje del episodio piloto E5.
3. Programar primera revisión del setup tras 4 semanas (junio 2026) para ajustar horarios con datos reales.

---

## Refs

- `documentos-internos/reciclaje-contenido-pipeline.md` §6 (distribución técnica) y §7 (delegación VA).
- `documentos-internos/youtube-podcast-estrategia-canal.md` §11 (riesgos) y §12 (decisiones).
- Identidad editorial: `CLAUDE.md`.
