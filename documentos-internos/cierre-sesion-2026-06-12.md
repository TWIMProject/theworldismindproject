# Cierre de sesión · 2026-06-12

Continuación de la sesión del 11 jun 2026 (app «Di lo que quieres decir», PRs #338 y #339 mergeados la noche del 11 jun 2026).

## Feedback de Daniel tras probar la app en producción (12 jun 2026, primera hora)

Daniel probó la app desde el móvil con un caso real (mensaje de WhatsApp a su pareja) y mandó 3 capturas con este veredicto verbatim: «Mira porque no me gusta. Lleva siempre a concretar hablarlo en persona y no recoge bien el mensaje y se basa en el mensaje realmente. Es demasiado genérico».

## Diagnóstico

**Lo que Daniel vio NO era el motor IA: era la plantilla fija del modo básico.** La prueba es concluyente: el texto del «después» de sus capturas es literalmente la plantilla hardcodeada de `reformulacionPorReglas()` en `app.js` («Quiero hablar contigo de algo que llevo tiempo callándome…»), con la emoción inferida por regex («me siento al límite», por el «me harta» de su texto) y la petición del mapa por objetivo. La IA no llegó a ejecutarse — o porque `ANTHROPIC_API_KEY` no está creada aún en Netlify, o porque se creó sin redeploy, o porque la llamada falló y se pulsó «Usar análisis básico». **Pendiente que Daniel confirme cuál.**

Hallazgos adicionales del repaso:
- **Byte NUL (`\x00`) en `app.js` de producción** (en `claveDeEntrada`, donde debía ir un espacio) — sin efecto funcional pero hacía que git/grep traten el fichero como binario. Corregido.
- El sandbox de esta sesión NO puede acceder a twimproject.com (la política de egress lo bloquea: «Host not in allowlist»). El «403 de Netlify contra bots» que se reportó el 11 jun era en realidad esto. No se puede verificar la clave ni probar la función desde aquí.
- Riesgo detectado: con volcados largos, `max_tokens: 3000` podía truncar el JSON y tirar al usuario al modo básico.

## Cambios aplicados (PR de hoy, rama `claude/twimproject-communication-app-i508h2`)

1. **System prompt v2 del motor** — el cambio de fondo que pide el feedback: el motor ahora distingue las 3 capas del volcado (meta-instrucciones a la herramienta · desahogo en tercera persona · frases directas), **obedece las meta-instrucciones** (canal WhatsApp, «sin que se sienta atacada», miedos declarados), convierte el desahogo en tercera persona en mensaje directo en segunda persona, y construye la reformulación **solo con material del texto** (prohibido el relleno genérico tipo «llevo tiempo callándome» salvo que sea palabra del usuario). Longitud proporcional al material. Frases ancla adaptadas al canal.
2. **Campo opcional «¿Cómo se lo quieres decir?»** en paso 2 (en persona / mensaje escrito / llamada) → va al motor; en modo básico adapta apertura y peticiones (nada de «hablarlo en persona» si es por escrito).
3. **Honestidad persistente del modo básico**: el aviso de plantilla ahora aparece también en pasos 4 y 5 (antes solo en el 3 y al avanzar se perdía — por eso el «después» parecía un resultado real siendo plantilla).
4. **Plantilla básica re-redactada** con gramática correcta («me siento que no me tienes en cuenta» → «siento que no me tienes en cuenta») y apertura por canal.
5. **`?diag=1`** en la función (patrón subscribe.js): `GET /.netlify/functions/traductor-interno?diag=1` → `{clave_configurada, modelo}` sin exponer valores. Para diagnosticar en 5 segundos desde el navegador.
6. **`max_tokens` 3000→4000** y byte NUL eliminado.

## Pendientes de Daniel

1. **Confirmar la clave**: Netlify → Environment variables → ¿existe `ANTHROPIC_API_KEY`? Si la creó: ¿hubo redeploy después? Tras mergear el PR de hoy, la URL `?diag=1` lo dice al instante.
2. **OK al PR de hoy** (toca `netlify/functions/` → regla infra → preview + OK explícito, no auto-merge).
3. Re-probar con su caso real **con la clave activa** — el preview del PR ya permite modo IA (origen de previews permitido desde el 11 jun).

## Estado emocional CEO al cierre

Frustración constructiva tras la prueba: reporta el problema con precisión clínica (3 capturas + diagnóstico en una frase) y espera iteración rápida. Patrón coherente con el perfil documentado: feedback directo, sin adornos, orientado a producto.
