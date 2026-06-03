# Producto · «Los engranajes de la mente» · edición digital

> Venta directa digital del libro (en paralelo a Amazon). Decidido y construido el 2 jun 2026, sesión `claude/blissful-lovelace-VPbaj`, con libertad de acción de Daniel.

## Qué es y por qué

Edición digital **ampliada** del libro (que en Amazon está a 7,68 €). Se vende directa desde la web con más margen y se diferencia de Amazon por un **extra exclusivo**. No canibaliza Amazon (allí están las reseñas 5★); es otra edición.

## Estado (2 jun 2026)

| Pieza | Estado |
|---|---|
| Portada digital TWIM (de cero, aprobada por Daniel «así genial») | ✅ `portada-edicion-digital-twim.jpg` · script `scripts/generar-portada-engranajes-digital.py` |
| Extra exclusivo «De los engranajes a tu día» (validado «ahora sí») | ✅ `extra-de-los-engranajes-a-tu-dia.html` |
| PDF completo ensamblado (portada + 186 interior + extra 10 págs + contraportada) | ✅ 198 págs · script `scripts/montar-pdf-engranajes-digital.py` |
| Precio | **9,90 €** (edición ampliada; +2 € sobre Amazon por el extra + compra directa) |
| Producto + Payment Link Stripe | ✅ creados (Live) · ver IDs abajo |
| Entrega de doble canal | ✅ Canal 1 redirect (hecho) + Canal 2 email (construido) · ver abajo |
| Landing de venta | ✅ sección «Edición digital» en `libros-firmados.html` (rama `claude/blissful-lovelace-VPbaj`, sin mergear) |

## Entrega de DOBLE CANAL · estado operativo (3 jun 2026)

> Endurecido tras un fallo real: Daniel hizo una compra de prueba y no pudo ni descargar ni recibir el PDF (el redirect no estaba puesto y la ficha prometía un email que no existía). Lección: **un solo canal = un solo punto de fallo.** Ahora hay dos canales independientes.

**Canal 1 · Descarga inmediata (redirect Stripe → página de gracias):** garantiza el PDF en el segundo 0, pase lo que pase con el email.
**Canal 2 · Email (webhook → grupo MailerLite → automation):** copia duradera en la bandeja del comprador. Si el email falla (spam, opt-in, typo), el canal 1 ya entregó.

### Piezas (en la rama, sin mergear salvo donde se indique)
| Pieza | Ruta / ID |
|---|---|
| PDF libro / cuaderno (producto de pago) | `descargas/los-engranajes-edicion-digital-c3ff84e018.pdf` · `descargas/la-mirada-del-otro-5447778151.pdf` |
| Páginas de gracias (con hash) | `descargas/gracias-engranajes-c69e607cf2.html` · `descargas/gracias-mirada-07b0f6aade.html` |
| `noindex` + no-cache `/descargas/*` | `_headers` |
| Portadas públicas | `portada-engranajes-digital.jpg` · `portada-cuaderno-la-mirada.jpg` |
| Sección de venta | `libros-firmados.html` → `#edicion-digital` |
| **Redirect Stripe (Canal 1)** | ✅ **YA PUESTO por API** (bracket-notation `after_completion[redirect][url]`) en los 2 Payment Links |
| Grupos MailerLite comprador (Canal 2) | Libro `189245231853471319` · Cuaderno `189245232345252997` |
| Automations de entrega (Canal 2) | Libro `189245270546974092` · Cuaderno `189245281082017289` |
| Webhook que enruta precio→grupo | `netlify/functions/stripe-webhook.js` (precios digitales añadidos con `groupId` fijo) |

### Nota técnica · el redirect SÍ se pudo por API
La clave fue la **codificación con brackets**: `after_completion[type]=redirect` + `after_completion[redirect][url]=...`. El MCP `stripe_api_execute` falla con dot-notation y con objeto anidado, pero acepta brackets. (Los IDs de grupo van fijos en el webhook a propósito: no son secretos y así el Canal 2 no depende de configurar env vars nuevas.)

### Lo que falta (panel + merge) — la API no puede «diseñar/activar» automations
1. **MailerLite (panel):** abrir cada automation (`189245270546974092` y `189245281082017289`) → abrir el email → **guardarlo en el editor visual** (queda «designed») → **activar** la automation. El contenido HTML y el texto ya están metidos por API; solo falta el guardado+activación, que la API no permite (`send_test` da «Emails not designed»).
2. **Mergear el PR** → deja en producción: páginas de gracias, PDFs, sección de venta y el **webhook actualizado** (sin esto, el Canal 2 no enruta).
3. **Compra de prueba reembolsable** de cada producto: pagar → (Canal 1) cae en la página de gracias y descarga → (Canal 2) llega el email con el enlace. Reembolsar las 2.
4. Solo si pasan, **anunciar/promocionar**.

**Importante:** el Canal 1 (descarga inmediata) funciona en cuanto se mergea, aunque las automations aún no estén activadas. Es decir, el merge ya garantiza entrega; el email es el refuerzo. La ficha de Stripe puede seguir diciendo «entrega por email» porque será cierto en cuanto se active el Canal 2; mientras, el comprador igualmente descarga al instante.

## Sobre commitear el PDF (decisión v1 vs blindaje v2)

> Histórico: el plan original era NO commitear el PDF (servirlo desde Blobs privado con token). En v1 se decidió lo contrario, a conciencia.

- **v1 (actual):** los PDFs SÍ se commitean en `descargas/` con **nombre-hash no adivinable** + `noindex`/no-cache (`_headers`) + no enlazados en ningún sitio público. Seguridad por oscuridad del hash, proporcionada a 8,90–9,90 €. Es lo que permite la entrega por redirect/email sin infra extra. Reproducible: `scripts/montar-pdf-engranajes-digital.py`.
- **Límite honesto:** un PDF descargado es reenviable; sin DRM (no compensa al precio). Se blinda el acceso (hash + páginas con hash), no la copia.
- **v2 (blindaje, cuando haya volumen):** mover los PDFs a Netlify Blobs privado + token HMAC caducable (`_lib-token.js` y `descarga-libro.js` ya están, inertes) y quitarlos del repo. Marca de agua con el email del comprador como disuasor.

## Entrega segura · arquitectura y estado (regla §2 · cobro = dinero, máximo cuidado)

### IDs Stripe (Live · creados 3 jun 2026 vía MCP)
| Producto | product_id | price_id | Payment Link |
|---|---|---|---|
| Los engranajes · edición digital ampliada · 9,90 € | `prod_UdQU34NRH5DfIO` | `price_1Te9ezFW3OLCwM3Hk5dRzXQd` | https://buy.stripe.com/dRmfZh2GS2GNgRdbvy2sM0i |
| La mirada del otro · cuaderno · 8,90 € | `prod_UdQWdU02qcOBar` | `price_1Te9giFW3OLCwM3HTwtYsBEu` | https://buy.stripe.com/14A00jchs95bbwT9nq2sM0j |

Cuenta: `acct_1Rbl1IFW3OLCwM3H` (TWIMProject). Estos `price_id` son los que el webhook debe mapear a cada PDF en la entrega.


**Diseño:** Stripe Checkout (pago) → `stripe-webhook.js` (ya verifica firma) detecta el price del libro → firma un **token HMAC caducable** → mete al comprador en MailerLite con el enlace de descarga en un campo → una automation le envía el email → la función `descarga-libro.js` valida el token y sirve el PDF desde **Netlify Blobs (privado)**. El PDF nunca está en una ruta pública.

### Ya construido en la rama (inerte hasta activar · no rompe nada existente)
- ✅ `netlify/functions/_lib-token.js` — firma/verifica token HMAC (caducidad). Compartido.
- ✅ `netlify/functions/descarga-libro.js` — sirve el PDF desde Blobs solo con token válido (403 si no). `noindex`.
- ✅ `netlify/functions/package.json` — dependencia `@netlify/blobs`.

### Falta (ejecutar con OK + verificación · en este orden)
0. **Proteger `documentos-internos/` del acceso público** (HALLAZGO verificado 2 jun: no hay regla y `publish="."` → hoy el extra/cuaderno serían accesibles por URL, aunque con `noindex`). Antes de mergear el material de pago, añadir en `_redirects` una regla tipo `/documentos-internos/* /404.html 404` (o equivalente) y **verificar en el deploy preview con un navegador real** (el bot de WebFetch recibe 403 de Netlify y no sirve para comprobarlo). Es cambio de routing = infraestructura §2.
1. **Verificar el deploy preview del PR**: que el build de funciones pasa con el nuevo `package.json` y que **el webhook de talleres (cobra 720 € reales) sigue intacto**. Crítico antes de cualquier merge.
2. **Extender `stripe-webhook.js`** (cirugía mínima, sin tocar la rama de talleres): si un line item coincide con `PRICE_LIBRO_DIGITAL`, firmar token (`signDownloadToken`, ttl 7 días, productKey `engranajes-digital`), construir `https://twimproject.com/.netlify/functions/descarga-libro?t=<token>` y dar de alta al comprador en MailerLite con el campo `download_url` + grupo comprador. La lógica de talleres queda igual.
3. **Subir el PDF a Netlify Blobs** (store `productos`, clave `engranajes-edicion-digital.pdf`) con un script o la CLI de Netlify. El PDF se genera con `scripts/montar-pdf-engranajes-digital.py`. NO al repo.
4. **Env vars Netlify** (nuevas): `DOWNLOAD_TOKEN_SECRET` (aleatorio largo), `PRICE_LIBRO_DIGITAL` (price_id del producto), `MAILERLITE_GROUP_COMPRADORES_LIBRO` (id del grupo).
5. **Stripe**: crear producto «Infoproducto · Los engranajes de la mente · Edición digital ampliada» a 9,90 € + Payment Link. (Sin MCP de Stripe en esta sesión → lo crea Daniel en panel, o vía API con la secret key.)
6. **MailerLite**: crear campo `download_url`, grupo comprador y automation de entrega (email con `{{download_url}}`, voz «Te escribo»).
7. **PRUEBA EN MODO TEST de Stripe end-to-end** (pago de prueba → llega email → descarga funciona → token caduca) **antes de pasar a live**. No se cobra de verdad hasta que la prueba pase.
8. Solo entonces, con OK de Daniel, mergear a producción.

**Marca de agua** con el email del comprador en el PDF · mejora v2 (disuade reenvío). v1 sale sin ella: el token caducable + Blobs privado ya cumple «solo el comprador» en el acceso.

Límite honesto: un PDF descargado es reenviable; sin DRM (no compensa a 9,90 €). Se blinda el acceso, no la copia. La marca de agua (v2) es el disuasor proporcional.

## Reproducir

```
python3 scripts/generar-portada-engranajes-digital.py   # portada
python3 scripts/montar-pdf-engranajes-digital.py         # PDF completo -> /tmp/LEDLM-edicion-digital.pdf
```
Requiere: Pillow, PyMuPDF, weasyprint (pip) + Instrument Serif TTF.
