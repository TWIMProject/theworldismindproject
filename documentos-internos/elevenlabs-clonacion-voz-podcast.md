# ElevenLabs · Clonación de voz para TWIM Podcast

> Documento de referencia · 30 abril 2026
> Cuando Daniel pregunte sobre clonación de voz, ElevenLabs, o producción de audio del podcast, abrir este documento.
> Complementa: anexo CEO (stack audio+vídeo), sistema visual IG, automatización IG.

---

## TL;DR

- **Herramienta:** ElevenLabs (https://elevenlabs.io). Mejor calidad del mercado en clonación de voz al 2026.
- **Plan recomendado:** Creator (~22 €/mes) — suficiente para 4-5 episodios de 30 min/mes.
- **Workflow:** NotebookLM (estructura) → guion editorial Daniel → ElevenLabs (audio con voz Daniel clonada) → publicación YouTube + Spotify.
- **Disclosure obligatorio:** sí, en bio del podcast + descripción de cada episodio. No es opcional.
- **Backup obligatorio:** los 30-60 min de audio fuente quedan guardados en local + cloud cifrado para recrear el modelo si ElevenLabs cambia ToS o cierra.
- **Política con pacientes:** confirmada por Daniel — NUNCA se usa material clínico de pacientes ni en NotebookLM ni en ElevenLabs.

---

## 1 · Por qué ElevenLabs y no otro

| Herramienta | Veredicto | Motivo |
|---|---|---|
| **ElevenLabs** | ✅ Recomendado | Mejor calidad de clonación, naturalidad, prosodia. ToS claro para uso comercial. |
| Resemble.ai | ⚠️ Alternativa | Calidad sólida, plan empresarial, más caro a poco volumen. Útil como backup. |
| Play.ht | ⚠️ Alternativa | Bueno pero menos natural. Útil como backup. |
| Descript Overdub | ❌ Limitado | Solo edición sobre material grabado existente, no TTS desde texto puro. |
| Murf, Speechify, otros | ❌ No | Voces preconfiguradas, no clonación auténtica. |

ElevenLabs domina en 2026 por calidad y por compatibilidad con cualquier idioma (incluido el español ibérico, que es donde fallan otros).

---

## 2 · Setup paso a paso

### 2.1 · Plan a contratar

- **Creator (~22 €/mes):** 100.000 caracteres/mes ≈ 4-5 episodios de 30 min. Permite uso comercial. **Punto de partida correcto.**
- **Pro (~99 €/mes):** 500.000 caracteres/mes. Solo si pasas a 6+ episodios/mes.
- **Free (0 €):** NO sirve. ToS impide uso comercial. Cualquier ingreso por AdSense del YouTube invalida el uso free.

### 2.2 · Entrenamiento del modelo de voz

1. Grabar **30-60 minutos de audio limpio de Daniel** hablando con tono editorial natural (no script forzado, no entrevista emocional). Recomendado: leer en voz alta varios artículos del propio repo de TWIM o capítulos del libro.
2. Audio en formato WAV o MP3 320kbps, sin música ni reverb.
3. Subir a ElevenLabs en **Voice Lab** → "Add Voice" → "Instant Voice Cloning" (o Professional Voice Cloning si está disponible en plan, mejor calidad).
4. Nombrar la voz "Daniel Orozco · TWIM Podcast" para identificarla.
5. Probar generando 1-2 minutos de texto. Validar que la voz suena reconocible.

### 2.3 · Validación de calidad antes de publicar

Antes de publicar el primer episodio con voz clonada:

- **Test de alguien que conozca tu voz.** Pásale 2 audios cortos (uno tuyo real, uno clonado) sin decirle cuál es cuál. Si no distingue, la calidad es suficiente.
- **Test de frases largas.** ElevenLabs tiene "uncanny valley" en frases > 30 segundos sin pausa. Probar frases largas, ajustar puntuación si suena raro.
- **Test de términos clínicos.** "Psicoanálisis", "transferencia", "Heinz Kohut", "introyección". Validar que pronuncia bien o ajustar pronunciación con el editor de ElevenLabs.

---

## 3 · Workflow de producción de un episodio

```
PASO 1 · Curaduría editorial (Daniel · 30-45 min)
├─ Elegir tema del episodio según calendario editorial.
├─ Reunir fuentes: artículos propios del repo, fragmentos del libro, papers, notas editoriales.
└─ NUNCA fuentes clínicas de pacientes identificables.

PASO 2 · Estructuración con NotebookLM (Daniel · 30 min)
├─ Subir las fuentes a un notebook dedicado al episodio.
├─ Pedir a NotebookLM: esquema de 5-7 puntos, FAQ, párrafos de transición.
├─ NotebookLM como organizador, no como autor.
└─ Output: estructura clara del episodio.

PASO 3 · Redacción del guion (Daniel · 60-90 min)
├─ A partir del esquema, redactar guion en voz tuya editorial.
├─ Estilo: descriptivo del mecanismo, anti-coaching, lenguaje TWIM.
├─ Duración objetivo: 15-30 min hablados ≈ 2.500-5.000 palabras.
└─ Output: guion .txt o .md listo para audio.

PASO 4 · Generación de audio con ElevenLabs (~10 min)
├─ Pegar guion en ElevenLabs con la voz "Daniel Orozco · TWIM Podcast".
├─ Generar audio.
├─ Si hay frases que suenan mal, ajustar puntuación y regenerar la frase.
└─ Output: archivo MP3 del episodio completo.

PASO 5 · Edición rápida (~15 min)
├─ Revisar en Audacity o herramienta similar.
├─ Añadir intro/outro de marca (jingle corto + frase de bienvenida + disclosure).
├─ Normalizar volumen.
└─ Output: MP3 final listo para publicación.

PASO 6 · Publicación cruzada (~30 min)
├─ Subir audio a Spotify (vía Anchor, Buzzsprout, o plataforma de hosting).
├─ Generar vídeo simple para YouTube (cover estático + waveform animado).
├─ Subir cover, descripción con disclosure, tags.
└─ Output: episodio publicado en ambas plataformas.

TIEMPO TOTAL POR EPISODIO: ~3-4 horas de Daniel
(con asistente futura, baja a ~1.5-2 h de Daniel + asistente lo demás)
```

---

## 4 · Disclosure obligatorio

### 4.1 · Por qué es obligatorio

Tres razones:

- **Deontológica.** El oyente debe saber qué está escuchando. La promesa "TWIM = anti-coaching, voz auténtica clínica" se rompe si descubre por su cuenta que la voz es sintética.
- **Plataformas.** Spotify (2024) y Apple Podcasts (2025) requieren disclosure de TTS/AI. YouTube exige tag "AI-generated content" en metadata. No declararlo es riesgo de penalización.
- **Reputacional.** Cuando se descubra (y se descubre tarde o temprano), el daño narrativo es proporcional al ocultamiento. Mejor ser transparente desde el día 1.

### 4.2 · Texto base de disclosure

**En la bio del podcast (Spotify, YouTube, web):**

> *Este podcast utiliza tecnología de clonación de voz (ElevenLabs) sobre la voz original de Daniel Orozco Abia para optimizar el tiempo de producción. La voz que escuchas es la suya, sintetizada. Todos los contenidos son curados editorialmente por Daniel a partir de su material original (artículos, libro, notas editoriales propias) — nunca a partir de información clínica de pacientes.*

**En la descripción de cada episodio (versión corta):**

> *Audio generado con clonación de voz vía ElevenLabs a partir del material editorial de Daniel Orozco Abia · CV11515.*

**En el primer minuto del audio (intro):**

> *Esto es TWIM Podcast. La voz que escuchas es la de Daniel Orozco, sintetizada con clonación para liberar tiempo de producción. El contenido editorial es 100% suyo.*

### 4.3 · Lo que NO se hace en disclosure

- **No omitirlo "porque la calidad es buena".** El criterio no es "se nota o no se nota", es "el oyente tiene derecho a saberlo".
- **No esconderlo en letra pequeña al final de descripción de 500 palabras.** El disclosure va al principio o claramente visible.
- **No describirse como "podcast con la voz de Daniel" sin matizar.** Es la voz, sintetizada.

---

## 5 · Backup obligatorio del modelo

### 5.1 · Por qué

ElevenLabs puede:
- Cambiar Términos de Servicio (ya pasó con OpenAI varias veces).
- Subir precios.
- Cerrar el plan Creator.
- Tener un fallo técnico que invalide modelos antiguos.

Si pierdes el modelo de voz y no tienes los archivos fuente, **pierdes todo el activo de "voz clonada Daniel"** y tienes que volver a entrenar desde cero (con la dificultad de tener un volumen de podcast publicado bajo una voz que ya no se replicará exacto).

### 5.2 · Qué guardar

- **Los 30-60 minutos de audio original** que usaste para entrenar el modelo. Formato WAV sin compresión. Guardar en:
  - Local (ordenador Daniel) — copia primaria.
  - Drive cifrado (Cryptomator + Google Drive, o Proton Drive) — copia secundaria.
  - Disco externo — copia terciaria.
- **El JSON de configuración del modelo** si ElevenLabs lo permite exportar (depende del plan).
- **Lista de pronunciaciones personalizadas** (cómo dices "Heinz", "Recalcati", etc. si has hecho ajustes).

### 5.3 · Cuándo recrear el modelo

- Cada 12-18 meses, regenerar con audio nuevo y comparar. Tu voz humana evoluciona; conviene mantener el modelo "fresco".
- Si ElevenLabs lanza un nuevo modelo de mejor calidad, regenerar.
- Si cambias de proveedor (Resemble, Play.ht), entrenar con el mismo audio fuente.

---

## 6 · Riesgos y mitigación

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Calidad insuficiente del clonado en frases largas o emocionales | Media | Medio | Test inicial estricto. Ajustar puntuación. Regenerar frases mal sonadas individualmente. |
| Reconocimiento del oyente de "voz sintética" | Baja-Media (con calidad ElevenLabs Creator) | Bajo si hay disclosure | Disclosure cubre el riesgo reputacional. |
| Cambio de ToS de ElevenLabs (limitación de uso comercial, etc.) | Media a 24 meses | Alto si pasa sin backup | Backup audio fuente. Tener cuenta secundaria en Resemble.ai como respaldo. |
| Penalización de plataforma (Spotify/Apple/YouTube) por contenido IA sin disclosure | Baja con disclosure correcto, Alta sin él | Alto (reducción de alcance) | Disclosure desde día 1. Etiquetas "AI-assisted" en YouTube metadata. |
| Crítica pública de "Daniel usa IA para su podcast" | Media | Bajo si hay disclosure honesto | El disclosure transforma crítica potencial en posicionamiento honesto sobre uso de IA. |
| Daniel decide en 6 meses pasar a voz humana real | Posible | Bajo | El sistema lo permite. La voz clonada es transición, no destino. |
| Mal uso del modelo por terceros (deepfake, suplantación) si se filtra | Muy baja | Alto | No compartir credenciales. 2FA en ElevenLabs. No subir audios públicos largos sin proteger. |

---

## 7 · Coste real anual

| Concepto | Coste anual estimado |
|---|---|
| ElevenLabs Creator | ~264 €/año (22 €/mes) |
| Hosting podcast (Buzzsprout, Spotify for Podcasters gratis) | 0-150 €/año |
| Licencia música intro/outro (Epidemic Sound o similar) | 50-150 €/año |
| **Total stack audio** | **~300-550 €/año** |

Comparativa: para liberar 8-12 horas/mes de Daniel (lo que costaría grabar real cada episodio), 300-550 € es **el ROI más alto del mapa de TWIM**. El cálculo: 10 horas/mes × 12 meses = 120 horas. Si el tiempo de Daniel se valora a 50 €/hora (conservador), eso son 6.000 €/año de su tiempo liberado, contra 300-550 € de inversión.

---

## 8 · ToS de plataformas — situación al 2026

### 8.1 · Spotify

- Permite contenido generado con IA con disclosure.
- Permite TTS con voz propia clonada.
- Recomienda etiquetar en descripción.
- No penaliza activamente al 2026, pero la dirección es hacia exigir disclosure.

### 8.2 · Apple Podcasts

- Política explícita: contenido AI-generated debe ser declarado.
- TTS con voz propia clonada está permitido con disclosure.
- Penalización por incumplimiento: posible retirada del catálogo.

### 8.3 · YouTube

- Desde marzo 2024, exige etiqueta "AI-generated content" en metadata cuando aplica.
- TTS con voz propia se considera "AI-generated audio". Sí etiquetar.
- Si no se etiqueta y se detecta, riesgo de demonetización temporal.

### 8.4 · ElevenLabs

- Plan Creator y Pro permiten uso comercial.
- ToS prohíbe usar la herramienta para suplantar voces de terceros sin consentimiento (no aplica a Daniel, que clona la suya propia).
- Atribución a ElevenLabs no es obligatoria pero recomendada.

---

## 9 · Política de uso interno (no publicado)

ElevenLabs también puede usarse para audio interno NO publicado:

- **Audios de bienvenida personalizados** para suscriptores de programas.
- **Mensajes de voz a clientes B2B** (in-company) sin grabar.
- **Audiolibro de "Los engranajes de la mente"** — versión audio del libro publicado.
- **Audios cortos de presentación** para landings nuevas.

Para uso interno (no publicado), el disclosure deontológico es menos urgente pero la honestidad sigue siendo regla: si el receptor cree que es Daniel grabando, conviene aclarar.

**Excepción dura:** NUNCA usar la voz clonada para mensajes 1:1 a pacientes. Esto sería suplantación clínica. Para pacientes, solo voz humana directa.

---

## 10 · Decisiones a cerrar este mes

- [ ] **Crear cuenta ElevenLabs Creator** (~22 €/mes).
- [ ] **Grabar 30-60 min de audio fuente** de Daniel hablando con tono editorial.
- [ ] **Entrenar el modelo** "Daniel Orozco · TWIM Podcast" en Voice Lab.
- [ ] **Test de calidad** con alguien que conozca la voz de Daniel.
- [ ] **Backup del audio fuente** en local + Drive cifrado + disco externo.
- [ ] **Redactar disclosure** definitivo (versión bio podcast + descripción episodio + intro audio).
- [ ] **Actualizar bio de TWIM Podcast en Spotify, Apple, YouTube** con disclosure.
- [ ] **Republicar (o editar descripción de) los 4 episodios actuales** con disclosure añadido.
- [ ] **Testear el workflow completo** con un episodio piloto antes de adoptarlo como estándar.

---

## Cierre

ElevenLabs no es un atajo, es una **decisión estratégica** de cómo gestionar el activo "voz de Daniel" en el contexto donde el tiempo es el recurso escaso (doc CEO §6.4). Bien implementado, libera a Daniel de la grabación sin sacrificar coherencia de marca. Mal implementado (sin disclosure, sin backup, con calidad pobre), erosiona la marca más rápido de lo que la construye.

La diferencia entre las dos versiones es:

- Disclosure transparente.
- Backup del modelo.
- Test de calidad estricto antes de publicar.
- Disciplina para que el contenido editorial siga siendo curado por Daniel, no por la IA.

Si las cuatro cosas se hacen bien, el sistema es defendible y escalable. Si una falla, el sistema empieza a producir más daño que beneficio.

— Notas técnicas: documento generado el 30-04-2026. Cuando ElevenLabs cambie precios o políticas, actualizar §2 y §8. Si aparece nueva herramienta de mejor calidad (improbable a corto plazo), actualizar §1.
