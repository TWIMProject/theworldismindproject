# Briefing clic a clic · Meta Ads · calentamiento de lista (plan x10) · 10 jun 2026

> OK de Daniel al plan x10 dado el 10 jun («ADELANTE CON EL X10»). Este briefing es para publicar la campaña desde Ads Manager en ~30-40 min, mismo formato que el de Google Ads del 9 jun. Detalle estratégico en `plan-x10-lista-email-2026-06-10.md`.

## Antes de empezar (requisito)

- [ ] GA4 → Administrar → Eventos → marcar `generate_lead` como **evento clave**. Sin esto no se puede juzgar el CPL real.
- [ ] Verificar en GA4 «Tiempo real» que el evento salta al enviar el formulario de la landing destino.

## Campaña

1. **Ads Manager → Crear → Objetivo: «Tráfico»** (NUNCA «Combinación optimizada» — lección del anuncio del niño, 22 may).
2. Nombre campaña: `Lista · Calentamiento · 5 señales validación · jun 2026`.
3. **Presupuesto: 6 €/día** a nivel de campaña (CBO off, presupuesto en el conjunto si lo prefiere igual que en mayo).
4. Conjunto de anuncios:
   - Conversión: **Sitio web**.
   - Audiencia: mujeres · 25-50 · España · intereses psicología/bienestar emocional (la misma que validó el anuncio de mayo).
   - Ubicaciones: Advantage+ (automáticas).
5. Anuncio A (control · el validado):
   - Creativo: carrusel «5 señales de que buscas validación» (el de mayo · CTR 12,89 %).
   - Destino: la misma landing del test de mayo, **con UTM**: `?utm_source=meta&utm_medium=cpc&utm_campaign=lista-calentamiento-jun26&utm_content=5senales`.
6. Anuncio B (variante · mismo conjunto):
   - Creativo: cita visual A2 del hambre de mirada (reciclada del Carrusel #4).
   - Destino: `https://twimproject.com/libro/capitulo-3/?utm_source=meta&utm_medium=cpc&utm_campaign=lista-calentamiento-jun26&utm_content=cap3`.
7. Publicar. Meta lo tendrá «en revisión» unas horas.

## Compuertas (las revisa Claude cada lunes y reporta)

- Día 14 · CPL ≤ 4 € y ≥ 10 leads → seguir. CPL > 4 € → pausar el anuncio perdedor, mantener el ganador.
- Día 30 · CPL ≤ 2 € sostenido → proponer subida a 10-15 €/día (decisión de Daniel).
- En cualquier momento · CPL > 4 € dos semanas seguidas → pausar campaña y cambiar creativo. No insistir con dinero en un creativo agotado.

## Qué hace Claude sin que Daniel lo pida

Lunes: leer altas MailerLite de la semana + gasto (captura de Daniel o GA4 cuando esté el evento clave) → actualizar la fila del mes en `plan-x10-lista-email-2026-06-10.md` §5 → avisar solo si una compuerta salta.
