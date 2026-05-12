# Email Post-Pago Automático · Programa «Deja de Buscarte en Otros»

> Este email se envía automáticamente cuando alguien paga 70€ en Stripe.
> Configurar en Stripe: Productos → «Deja de Buscarte en Otros» → Configuración → **Email de confirmación personalizado**.
> O configurar webhook a MailerLite si quieres más control de plantilla (opcional, no necesario al inicio).

---

## ASUNTO

```
Aquí tienes tu acceso al programa
```

## PREVIEW TEXT

```
Te dejo el enlace, unas pocas instrucciones, y nada más.
```

## REMITENTE

```
Daniel Orozco · danielorozco@twimproject.com
```

---

## CUERPO DEL EMAIL (plain text · español)

```
Hola,

Acabas de comprar «Deja de Buscarte en Otros». Gracias por la confianza.

Aquí tienes el acceso al material:

[ENLACE_AL_DRIVE_O_VIMEO]

Encontrarás dentro:

— 5 vídeos (los 5 módulos del programa)
— Cuaderno de trabajo en PDF
— 3 audios guiados
— Protocolo de 21 días

El acceso es de por vida. Puedes verlo a tu ritmo, en el orden que prefieras, las veces que necesites.

Antes de empezar, tres notas:

1. Empieza por el Módulo 1 («El Mapa»). No te saltes el orden la primera vez. Los módulos descansan unos sobre otros.

2. Cada módulo tiene un ejercicio asociado en el cuaderno. Hazlo después de ver el módulo, no durante. Con café delante, sin prisa. La práctica es donde el material se mueve.

3. El protocolo de 21 días lo empiezas cuando hayas visto los 5 módulos. No antes. Si lo empiezas sin haber visto el material, los ejercicios se quedan en superficie.

Si necesitas resolver alguna duda sobre el contenido del programa, escríbeme a este mismo email. Si descubres que necesitas acompañamiento individual durante o después del programa, puedes consultar mis opciones en twimproject.com/daniel-orozco-abia.

Una última cosa. Este programa es psicoeducativo, no es terapia. Te va a ayudar a entender un mecanismo y a tener herramientas para intervenirlo. Si lo que sientes durante el material te paraliza o te impide funcionar, busca a alguien que pueda mirarlo contigo de cerca. Lo que vas a leer y escuchar no sustituye eso.

Te leo si lo necesitas.

— Daniel

—

Daniel Orozco Abia
Psicólogo General Sanitario · CV11515
twimproject.com
```

---

## NOTAS DE IMPLEMENTACIÓN

**Stripe Payment Link configuración:**

1. Producto: «Deja de Buscarte en Otros»
2. Precio: 70,00 EUR (one-time payment)
3. Confirmación post-pago: **email de confirmación personalizado** activado
4. URL del programa (custom URL después del pago): redirigir a `twimproject.com/gracias-compra-programa.html` (página de agradecimiento — opcional, podemos crearla después)
5. Idioma checkout: español
6. Métodos de pago: tarjeta, Bizum (si Stripe lo soporta en tu cuenta), Apple Pay, Google Pay
7. Recibos: activados, generan automáticamente
8. **NO activar suscripciones recurrentes.** Es un único pago.

**Antes de poner el Payment Link en producción:**

- Reemplazar `[ENLACE_AL_DRIVE_O_VIMEO]` por el link real al Drive privado o Vimeo
- Hacer una compra de prueba con tu propia tarjeta (puedes reembolsártela después en el dashboard de Stripe) para verificar:
  - Que el email llega
  - Que el link funciona
  - Que el recibo de Stripe llega aparte
  - Que no hay errores tipográficos

**Plantilla de email Stripe vs MailerLite:**

- **Opción A (más simple, recomendada al inicio):** plantilla nativa de Stripe. Configuras el texto en el dashboard de Stripe directamente. No requiere integración. Funciona desde el día 1.
- **Opción B (más control):** webhook Stripe → MailerLite. Permite seguir secuencias post-compra (ej: día +7 «¿cómo va el Módulo 1?», día +30 «¿has empezado el protocolo?»). Más trabajo de setup. Hacer cuando haya 5+ ventas y tenga sentido invertir en automation.

**Empieza con A.** B viene después.
