# Instrucciones Stripe · Setup paso a paso para el Programa «Deja de Buscarte en Otros»

> Para Daniel. Si nunca has usado Stripe, este documento te lleva de cero a Payment Link funcionando en ~20 minutos.
> Si ya tienes cuenta Stripe, salta al paso 4.

---

## Paso 0 · Antes de empezar, ten a mano

- DNI español o pasaporte
- IBAN de la cuenta donde quieres recibir los cobros (puede ser tu cuenta personal o empresarial)
- Dirección fiscal completa
- Número de teléfono móvil para verificación SMS
- 20 minutos sin interrupciones (es el tiempo total del setup completo)

---

## Paso 1 · Crear cuenta Stripe (5 min)

1. Ve a **https://dashboard.stripe.com/register**
2. Email → contraseña → país: **España**
3. Verifica tu email
4. **Activa la cuenta** rellenando los datos legales que Stripe te pide:
   - Tipo de empresa: probablemente «Particular / Autónomo» (a menos que tengas SL)
   - Sector: «Servicios profesionales» o «Educación»
   - Descripción del negocio: «Programa digital de psicoeducación. Material en vídeo, audio y PDF sobre dependencia emocional, dirigido a adultos.»
   - URL del negocio: `https://twimproject.com`
   - Dirección y datos fiscales: los tuyos
   - IBAN: el tuyo para los payouts
5. Verifica el SMS
6. Espera la confirmación (suele tardar segundos, a veces minutos)

**Stripe pedirá un documento de identidad subido en algún momento.** Súbelo. Es trámite normal.

---

## Paso 2 · Configurar marca de cuenta (3 min)

1. En el dashboard, ve a **Configuración → Marca**
2. Sube tu logo (`logo-mindworld.png`)
3. Color de marca: **#173D30** (verde TWIM)
4. Color de fondo: **#FDFCFA** (crema)
5. Nombre comercial: **TWIM Project**
6. Email de soporte: **danielorozco@twimproject.com**

Esto hace que el checkout y los emails de Stripe se vean con tu marca.

---

## Paso 3 · Configurar idioma y moneda (1 min)

1. **Configuración → Configuración de la cuenta**
2. Idioma por defecto: **Español**
3. Moneda por defecto: **EUR**
4. Zona horaria: **Europe/Madrid**

---

## Paso 4 · Crear el producto (3 min)

1. En el dashboard, ve a **Productos → Añadir producto**
2. Datos del producto:
   - **Nombre:** Deja de Buscarte en Otros
   - **Descripción:** Programa de dependencia emocional. 5 módulos en vídeo + cuaderno de trabajo PDF + 3 audios guiados + protocolo de 21 días. Acceso de por vida.
   - **Imagen del producto:** sube `logo-mindworld.png` o una imagen sobria del programa (puedes generar una pieza vertical con título en Canva si quieres)
3. Datos de precio:
   - **Modelo de precio:** Tarifa única
   - **Precio:** 70,00 EUR
   - **NO marcar «Recurrente»**
   - Tipo de impuesto: dejar por defecto (Stripe gestiona IVA automático si lo activas, ver paso 7)
4. Guardar producto

---

## Paso 5 · Crear el Payment Link (3 min)

1. Una vez creado el producto, en la página del producto pulsa **«Crear Payment Link»** (o ve a **Payment Links → Crear**)
2. Selecciona el producto «Deja de Buscarte en Otros»
3. **Configuración del enlace:**
   - URL después del pago: redirigir a una URL personalizada → `https://twimproject.com/gracias-compra-programa.html` (esa página la creamos después, por ahora puedes dejar la URL de éxito por defecto de Stripe)
   - Recopilación de información: solo email (lo demás no hace falta)
   - Restricciones de país: España + UE + LATAM (mercado natural del programa)
   - Cantidad ajustable: NO
   - Permitir promocodes: SÍ (te servirá si en el futuro quieres ofrecer código «LANZAMIENTO» a 49€ para lista cálida)
4. **Idioma del checkout:** Español
5. **Métodos de pago:** marcar todos los disponibles (tarjeta, Bizum si aparece, Apple Pay, Google Pay, Klarna si te ofrecen). Bizum es importante para España.
6. Guardar Payment Link
7. **Copiar la URL** que te da Stripe. Se ve algo así como `https://buy.stripe.com/test_xxxx`

**ESA URL es la que va a ir en el botón «Quiero el programa» de la landing.**

---

## Paso 6 · Personalizar email post-pago (5 min)

1. Ve a **Configuración → Recibos por email**
2. **Activa los recibos** (Stripe envía automáticamente un recibo al cliente)
3. Ve a **Configuración → Eventos → Customer emails**
4. Activa la opción **«Enviar email personalizado tras pago exitoso»** (si está disponible en tu plan)
5. Asunto: `Aquí tienes tu acceso al programa`
6. Cuerpo: copia y pega **íntegro** el contenido de `email-confirmacion-compra.md` (ya está redactado)
7. **Reemplaza el placeholder** `[ENLACE_AL_DRIVE_O_VIMEO]` por el link real al Drive cuando tengas el contenido subido. **No actives el Payment Link en producción hasta que este placeholder esté reemplazado por el link real.**

**Si tu plan Stripe no permite email post-pago personalizado** (planes muy básicos a veces no): solución alternativa via webhook → MailerLite. Pero esto lo dejamos para más adelante; por ahora la mayoría de cuentas Stripe nuevas sí permiten email personalizado.

---

## Paso 7 · Activar gestión automática de IVA (opcional pero recomendado)

Si vas a vender más de unos pocos productos al año a clientes UE, tienes obligación de cobrar IVA del país del comprador (One-Stop Shop, OSS).

1. **Configuración → Impuestos → Stripe Tax**
2. Activar Stripe Tax (es un servicio de Stripe que calcula el IVA automático según el país del comprador)
3. Coste: ~0.5% sobre las transacciones donde calcule IVA. A cambio, te ahorra el quebradero de cabeza de la fiscalidad UE.

**Consulta esto con tu gestor antes de activarlo.** Es una decisión fiscal, no técnica. Si tu volumen actual es <100 ventas/año, hay umbrales que te eximen.

---

## Paso 8 · Hacer una compra de prueba (3 min)

**ANTES de poner el Payment Link en la landing pública:**

1. Activa **modo Test** en Stripe (toggle arriba a la derecha)
2. Vuelve a tu Payment Link en modo test
3. Haz una compra con **tarjeta de prueba Stripe**: `4242 4242 4242 4242` · cualquier fecha futura · cualquier CVC · cualquier código postal
4. Verifica:
   - ✅ El checkout aparece en español
   - ✅ El logo + colores son los tuyos
   - ✅ Te llega el email de confirmación
   - ✅ El link al Drive funciona
   - ✅ El recibo Stripe llega aparte

5. Si todo bien, **vuelve a modo Live** y copia la URL del Payment Link de modo Live (es distinta a la de modo Test). **Esa URL es la que va a la landing.**

---

## Paso 9 · Poner el Payment Link en la landing (2 min)

1. Abre `dejadebuscarteenotros.html`
2. Busca: `STRIPE_PAYMENT_LINK_AQUI`
3. Reemplaza por la URL real del Payment Link de Stripe (modo Live)
4. Guardar
5. Commit + push a main → Netlify despliega automáticamente
6. Verifica en producción que el botón funciona

---

## Paso 10 · Hacer una compra real con tu propia tarjeta (5 min)

Una vez en producción, **hazte tú mismo una compra real**. Sí, paga 70 €. Después te lo reembolsas en el dashboard.

¿Por qué? Porque solo así verificas el flujo completo: pago → email → link al Drive → acceso al material. Si algo falla, prefieres que falle contigo, no con el primer comprador real.

Tras la prueba, en el dashboard Stripe **Reembolsar** la transacción. Tarda 5-10 días en aparecer en tu cuenta de vuelta.

---

## Webhook MailerLite (opcional, hacer después)

Cuando tengas 5+ ventas y quieras montar secuencia post-compra automática (día +7 «¿qué tal el módulo 1?», día +21 «¿has empezado el protocolo?»):

1. En MailerLite, crea grupo «Compradores Programa DDBEO»
2. Stripe → Webhooks → añadir endpoint apuntando a MailerLite
3. Evento a escuchar: `payment_intent.succeeded`
4. Cada vez que alguien compre, MailerLite los añade automáticamente a ese grupo
5. Configurar secuencia post-compra en MailerLite

**No hagas esto hoy.** Hoy lo importante es que el flujo básico funcione. Webhooks vienen cuando haya volumen.

---

## Resumen del paso a paso

1. ✅ Crear cuenta Stripe
2. ✅ Configurar marca (logo, colores)
3. ✅ Idioma + moneda + zona horaria
4. ✅ Crear producto «Deja de Buscarte en Otros» a 70€
5. ✅ Crear Payment Link
6. ✅ Personalizar email post-pago
7. ✅ (Opcional) Activar Stripe Tax
8. ✅ Compra de prueba en modo Test
9. ✅ Poner Payment Link en landing
10. ✅ Compra real propia + reembolso

**Tiempo total real:** 20-30 min si no tienes complicaciones. Hasta 60 min si la verificación de identidad de Stripe tarda.

**Cuando termines, dímelo y completo lo que falta (página de gracias post-compra, ajustes en landing, lo que sea).**
