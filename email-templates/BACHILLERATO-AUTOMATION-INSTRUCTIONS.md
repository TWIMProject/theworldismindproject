# Automatización Bachillerato — Instrucciones MailerLite

## Configuración de la automatización

**Nombre:** `Nurture Guía Bachillerato`
**Disparador:** `Se une a grupo(s)` → `padres-talleres-bachillerato`
**Condiciones:** ninguna

---

## Flujo (secuencia exacta)

| Paso | Tipo   | Contenido                                            | Delay     |
|------|--------|------------------------------------------------------|-----------|
| 1    | Email  | `bachillerato-email-1-bienvenida.html`               | Inmediato |
| 2    | Delay  | 2 días                                               | —         |
| 3    | Email  | `bachillerato-email-2-no-es-vago.html`               | —         |
| 4    | Delay  | 3 días                                               | —         |
| 5    | Email  | `bachillerato-email-3-caso-pablo.html`               | —         |
| 6    | Delay  | 4 días                                               | —         |
| 7    | Email  | `bachillerato-email-4-taller.html`                   | —         |

---

## Asuntos y previews

### Email 1 — Día 0 (inmediato)
- **Asunto:** `Tu guía de Bachillerato está aquí (+ algo personal)`
- **Preview:** `Lo que he aprendido en trece años con adolescentes`
- **Archivo:** `bachillerato-email-1-bienvenida.html`

### Email 2 — Día +2
- **Asunto:** `Tu hijo no es vago`
- **Preview:** `Lo que tú ves como vagancia, por dentro es otra cosa`
- **Archivo:** `bachillerato-email-2-no-es-vago.html`

### Email 3 — Día +5
- **Asunto:** `Lo que pasó con "Pablo" (17 años, 2º Bachillerato)`
- **Preview:** `Un caso real. Cambio el nombre, pero lo demás es tal cual`
- **Archivo:** `bachillerato-email-3-caso-pablo.html`

### Email 4 — Día +9
- **Asunto:** `Por si lo de Pablo resuena en tu casa`
- **Preview:** `Un taller muy concreto que empieza en septiembre`
- **Archivo:** `bachillerato-email-4-taller.html`

---

## Checklist antes de activar

- [ ] Grupo `padres-talleres-bachillerato` existe en MailerLite
- [ ] Los 4 emails pegados en HTML personalizado (NO plain text)
- [ ] Delays de 2, 3 y 4 días entre emails
- [ ] Merge tag `{$name}` en todos los saludos
- [ ] Merge tag `{$unsubscribe}` en footer de los 4 emails
- [ ] Imagen del avatar cargada (`twimproject.com/yoacolor.png`)
- [ ] Link a `twimproject.com/guia-padres-bachillerato.pdf` comprobado (Email 1)
- [ ] Link a `/talleres/bachillerato-motivacion/#cta-final` comprobado (Email 4)
- [ ] WhatsApp `wa.me/34625231297` comprobado (Email 4)
- [ ] Test con email propio (recuerda: en modo test llegan los 4 seguidos, eso es normal)
- [ ] Activar

---

# Google Business Profile — contenido listo

## Nombre del negocio (exactamente así)
```
TWIM Project · Daniel Orozco Abia | Psicólogo Adolescentes Valencia
```

## Categoría principal
```
Psicólogo
```

## Categorías secundarias (añadir hasta 9)
1. Consulta psicológica
2. Psicoterapeuta
3. Centro de psicología
4. Servicio de salud mental
5. Consultor psicológico
6. Terapeuta

## Descripción corta (750 caracteres máx — esta tiene 738)

```
Consulta de psicología en Valencia dirigida por Daniel Orozco Abia, Psicólogo General Sanitario de orientación psicoanalítica (Col. CV11515) con más de 13 años de experiencia. Atención a adolescentes y adultos jóvenes con TDAH, apatía académica, confusión vocacional, ansiedad, síndrome del impostor, dependencia emocional y burnout. Consulta privada individual y talleres psicoeducativos grupales presenciales para adolescentes de 3º y 4º ESO (TDAH) y 1º y 2º de Bachillerato (motivación y orientación vocacional). CEO de The World Is Mind Project y autor de «Los Engranajes de la Mente» y «Burnout: El libro para no petar». Primera consulta sin compromiso.
```

## Servicios (añadir uno a uno)
1. Terapia psicológica individual adolescentes
2. Terapia psicológica individual adultos
3. Taller grupal TDAH adolescentes (3º y 4º ESO)
4. Taller grupal motivación Bachillerato
5. Evaluación psicológica adolescentes
6. Acompañamiento a padres
7. Terapia online (consultar)
8. Primera consulta informativa

## Horario
Confirma el horario actual de consulta (ej. L-V 10:00–20:00). No lo dejes vacío.

## Fotos (mínimo necesario)
- **Portada:** tu foto profesional (la del sillón ya está en el sitio)
- **Logo:** `logo-mindworld.png`
- **Interior:** 1-2 fotos del espacio de consulta (sin pacientes)
- **Exterior:** fachada / entrada del edificio (útil para que te encuentren)

## Atributos destacables
- Acepta nuevos pacientes
- Cita previa requerida
- Accesible en silla de ruedas (si aplica)
- LGBTQ+ friendly (si te representa)

---

# Plantilla WhatsApp — pedir reseñas al círculo profesional

> **Importante:** nunca a pacientes ni ex-pacientes. Este mensaje es para colegas psicólogos, médicos, profesores, exalumnos de máster, compañeros de colegio, supervisores, editores, podcasters con los que hayas colaborado.

## Versión A — contactos profesionales cercanos

```
Hola [Nombre], ¿qué tal?

Te escribo con un pequeño favor. Estoy dando empuje al perfil de Google
Business del proyecto (TWIM Project) de cara a los talleres que arranco
en septiembre para adolescentes, y me ayudaría mucho tener reseñas
honestas de personas que me conozcan en lo profesional.

Por ética no pido reseñas a pacientes, así que me apoyo en el círculo de
colegas y personas con las que he colaborado.

Si te parece bien y me conoces lo suficiente como para hablar de cómo
trabajo, de los libros, de la divulgación o del trato humano, ¿te
animarías a dejarme una reseña breve?

Te paso el enlace directo: [LINK_GOOGLE_RESENA]

Cualquier ángulo que te salga natural vale: rigor clínico, forma de
explicar, divulgación, trato con adolescentes o con padres, lo que tú
veas. Honestidad mejor que amabilidad.

Mil gracias de verdad.
Un abrazo,
Daniel
```

## Versión B — contactos más informales (exalumnos, compañeros de promoción)

```
Hola [Nombre], una cosa rápida.

Estoy dando empuje al perfil de Google del proyecto de cara a septiembre
(arranco talleres para adolescentes con TDAH y de Bachillerato) y
necesito reseñas de gente que me conozca profesionalmente. A pacientes
no les pido por ética.

¿Te animas a dejarme una? No hace falta que sea larga. Lo que te salga
sobre cómo trabajo, los libros, la divulgación o el trato.

Link: [LINK_GOOGLE_RESENA]

Gracias un montón.
Daniel
```

## 6 ángulos de reseña (mándaselos como sugerencia si te los piden)

1. **Rigor clínico y formación.** «Conozco a Daniel desde [año/contexto]. Su formación psicoanalítica y su rigor a la hora de devolver algo técnico se notan en cuanto hablas con él cinco minutos.»

2. **Trato con adolescentes.** «He visto a Daniel trabajar con adolescentes (o hablar de su trabajo con ellos) y lo que más destaca es su capacidad para no forzar, no juzgar y sostener silencios incómodos sin rellenarlos. Algo poco habitual.»

3. **Capacidad de divulgación.** «Lo sigo como divulgador (Instagram, YouTube, libros) y lo que le diferencia es que no reduce la psicología a etiquetas. Explica cosas complejas sin simplificarlas. Eso se agradece.»

4. **Trato humano.** «Daniel es una persona que cuida los detalles, escucha de verdad y no va con el piloto automático del profesional. Se nota que lo que hace le importa.»

5. **Honestidad profesional.** «Si no puede ayudar en algo, lo dice. Si cree que alguien necesita otro tipo de atención, lo deriva. Eso, en este sector, no es tan común como debería.»

6. **Compromiso con la adolescencia como etapa.** «Lleva años apostando por un trabajo serio con adolescentes en un momento en el que la salud mental juvenil está en crisis. Haber montado talleres grupales específicos para TDAH y Bachillerato es exactamente lo que hace falta.»

## Cómo conseguir el link directo a dejar reseña en Google

1. Entra en tu perfil de Google Business Profile (desde la app o desde google.com/business).
2. Pulsa `Solicitar reseñas` o `Compartir perfil`.
3. Copia el link corto tipo `g.page/r/xxxxx/review` o `maps.google.com/?cid=...`
4. Pégalo en `[LINK_GOOGLE_RESENA]` del mensaje de arriba.

## A quién priorizar (empieza por los 6 más probables de responder hoy)

- [ ] Compañero/a psicólogo/a de promoción o máster
- [ ] Supervisor/a clínico/a actual o pasado
- [ ] Colega con el que hayas colaborado en podcast, charla o formación
- [ ] Editor/a de los libros
- [ ] Profesor/a universitario de la carrera o máster
- [ ] Orientador/a de colegio o instituto que conoces profesionalmente

**Objetivo:** 6 reseñas en 2 semanas. No más. Mejor pocas y reales que muchas y genéricas.
