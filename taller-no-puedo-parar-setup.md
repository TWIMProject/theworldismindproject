# Taller 'No puedo parar' - Setup Completo
## 30 marzo 2026 - 19:30h (hora Espana)

---

## ESTADO ACTUAL - Lo que ya esta hecho

### STRIPE - COMPLETADO
- **Producto**: Taller 'No puedo parar' - 30 marzo 2026 (ID: prod_U8R9h2LaEoqIrb)
- **Precio**: 19 EUR, pago unico (ID: price_1TAAHmFW3OLCwM3HjO2q3NKt)
- **Enlace de pago**: https://buy.stripe.com/5kQ4gzdlw4OV58vdDG2sM07

### GOOGLE CALENDAR - COMPLETADO
- **Evento**: Taller 'No puedo parar' - EN VIVO
- **Fecha**: 30 marzo 2026, 19:30h - 21:00h (Europe/Madrid)
- **Google Meet**: Enlace generado automaticamente en el evento
- **Recordatorios**: 1 dia antes (email), 1 hora antes (popup), 15 min antes (popup)
- **Ver evento**: https://www.google.com/calendar/event?eid=NTA3ZWhxcWxrM3FmZHVzYTNjdW45dXZmbDQgZGFuaWVsb3JvemNvQHRoZXdvcmxkaXNtaW5kcHJvamVjdC5jb20

### PENDIENTE DE CONFIGURAR MANUALMENTE

#### En Stripe Dashboard:
1. **Mensaje post-pago**: Ve a Payment Links > tu enlace > After payment. Configura:
   > Reserva confirmada. El domingo 30 de marzo a las 19:30h recibiras un email con el enlace de Google Meet. Prepara papel y boli. Si tienes alguna duda, escribeme a danielorozco@theworldismindproject.com. Gracias por confiar. - Daniel
2. **Recoger emails**: Verifica que "Collect email addresses" esta activado en el payment link.

#### En Instagram:
- Pon el enlace de Stripe en tu bio: https://buy.stripe.com/5kQ4gzdlw4OV58vdDG2sM07

---

## MANYCHAT - CONFIGURACION MANUAL

ManyChat no se puede automatizar por API desde aqui. Sigue estos pasos:

### Paso previo: Verificar conexion
1. Abre https://app.manychat.com
2. Verifica que @daniorozcopsicologo esta conectado (tick verde)
3. Si no esta conectado: Settings > Instagram > Connect Instagram Account

### Automatizacion 1: Keyword TALLER (DM)
1. Automation > + New Automation > Start from scratch
2. Add Trigger > Instagram > DM con keyword
3. Keyword: **TALLER** | Coincidencia: **Contains**
4. Accion: Send Message > Texto:

```
Hola! Gracias por tu interes.

'No puedo parar' es un taller en vivo de 90 minutos para profesionales que se exigen demasiado y no consiguen desconectar.

Que vas a aprender:
- Por que no puedes parar aunque quieres (el mecanismo real, no teoria).
- Una tecnica de 120 segundos para intervenir en el momento exacto.
- Un plan de 7 dias para empezar a recuperar margen de eleccion.

Fecha: domingo 30 de marzo, 19:30h (hora Espana).
Formato: Google Meet en vivo (se graba).
Plazas: 20 maximo.
Precio de lanzamiento: 19 euros.

Reserva tu plaza aqui: https://buy.stripe.com/5kQ4gzdlw4OV58vdDG2sM07

Si tienes alguna duda, escribeme y te respondo personalmente. - Daniel
```

5. Publish/Activate

### Automatizacion 2: Keyword INFO (DM)
1. Automation > + New Automation > Start from scratch
2. Add Trigger > Instagram > DM con keyword
3. Keyword: **INFO** | Coincidencia: **Is** (exacto)
4. Accion: Send Message > Texto:

```
Hola! Te cuento.

El 30 de marzo a las 19:30h hago un taller en vivo de 90 minutos. Se llama 'No puedo parar' y esta pensado para profesionales que:

- Saben que deberian parar pero no pueden.
- Sienten culpa o inquietud cuando descansan.
- Funcionan bien por fuera pero por dentro estan en deuda permanente con la idea de 'estar a la altura'.

No es motivacion ni autoayuda. Es ver el mecanismo que te empuja y aprender a no obedecerlo en el primer segundo.

Tienes alguna duda concreta? Preguntame lo que necesites.
```

5. Publish/Activate
6. **NOTA**: Este mensaje NO incluye enlace a proposito. Cuando la persona responda, enviale manualmente: https://buy.stripe.com/5kQ4gzdlw4OV58vdDG2sM07

### Automatizacion 3: Comment trigger en posts
1. Automation > + New Automation > Start from scratch
2. Trigger: Instagram > Comment on Post
3. Seleccionar el post de anuncio del taller (hacerlo DESPUES de publicar el post, entre el 17-24 marzo)
4. Comment contains: dejar vacio (cualquier comentario) o poner "QUIERO"
5. Respuesta publica al comentario: **"Te envio info por DM!"**
6. DM automatico: copiar el mismo texto de la Automatizacion 1 (el completo con enlace)
7. Activar cuando publiques el post de anuncio

---

## DMs MANUALES - COPIAR Y PEGAR

### DM 1: Para quienes respondieron 'Si' en encuestas de Stories
**Enviar entre 17-24 marzo**

```
Hola [nombre],

vi que respondiste a mi encuesta sobre autoexigencia. Queria contarte que estoy preparando un taller en vivo sobre exactamente eso: por que no podemos parar aunque queremos y que hacer con ello.

Es el 30 de marzo a las 19:30h, 90 minutos por Google Meet. 19 euros. 20 plazas.

Te interesa que te cuente mas o prefieres que te envie directamente el enlace?
```

### DM 2: Para quienes interactuaron pero no compraron
**Enviar entre 25-29 marzo**

```
Hola [nombre],

he visto que te ha interesado el contenido sobre autoexigencia. El taller es este domingo a las 19:30h y quedan pocas plazas.

Tienes alguna duda? Preguntame lo que necesites. Si ya lo tienes claro, aqui va el enlace: https://buy.stripe.com/5kQ4gzdlw4OV58vdDG2sM07
```

### DM 3: Seguimiento a quien pregunto pero no compro
**Enviar 28-29 marzo**

```
Hola [nombre],

te escribo porque el otro dia me preguntaste por el taller. Es este domingo y quedan [X] plazas.

No quiero presionarte. Solo quiero que sepas que si al final decides entrar, aqui esta el enlace: https://buy.stripe.com/5kQ4gzdlw4OV58vdDG2sM07

Y si no es el momento, sin problema. El contenido del blog sigue ahi.
```

**IMPORTANTE**: Personaliza siempre el [nombre]. Un DM con nombre convierte 3x mas que uno generico.

---

## CHECKLIST

### STRIPE
- [x] Enlace de pago creado (19 EUR, pago unico)
- [ ] Mensaje de confirmacion post-pago configurado (manual en Stripe Dashboard)
- [x] Enlace copiado y guardado
- [ ] Enlace puesto en bio de Instagram

### MANYCHAT
- [ ] Instagram conectado a ManyChat
- [ ] Automatizacion 1: keyword TALLER con mensaje + enlace de pago
- [ ] Automatizacion 2: keyword INFO con mensaje sin enlace
- [ ] Automatizacion 3: comment trigger preparada
- [ ] Probado desde otra cuenta

### GOOGLE
- [x] Evento en Google Calendar creado con Google Meet
- [ ] Google Forms de testimonios creado (3 preguntas)

### CONTENIDO
- [ ] Presentacion 'taller-no-puedo-parar.pptx' descargada y revisada
- [ ] Calendario de contenidos leido (documento plan-lanzamiento)
- [ ] Primera Story publicada
