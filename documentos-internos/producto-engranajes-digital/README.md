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
| Entrega segura (vía rápida v1) | ✅ PDF con hash + `noindex` + página de gracias con hash · **falta el redirect en panel Stripe** |
| Landing de venta | ✅ sección «Edición digital» en `libros-firmados.html` (rama `claude/blissful-lovelace-VPbaj`, sin mergear) |

## Entrega vía rápida v1 · estado operativo (3 jun 2026)

Decisión de especialista (Daniel delegó: «la que recomiendes como especialista»): **vender ya con la vía rápida**, blindar después (token+Blobs) cuando haya volumen. La vía rápida es: pago → Stripe redirige a una **página de gracias con nombre no adivinable** → botón de descarga del **PDF con hash** (`noindex`, no enlazado en ningún sitio).

### Piezas (en la rama, sin mergear)
| Pieza | Ruta |
|---|---|
| PDF libro (producto de pago) | `descargas/los-engranajes-edicion-digital-c3ff84e018.pdf` |
| PDF cuaderno (producto de pago) | `descargas/la-mirada-del-otro-5447778151.pdf` |
| Página de gracias libro | `descargas/gracias-engranajes-c69e607cf2.html` |
| Página de gracias cuaderno | `descargas/gracias-mirada-07b0f6aade.html` |
| `noindex` + no-cache para `/descargas/*` | `_headers` |
| Portadas públicas (marketing) | `portada-engranajes-digital.jpg`, `portada-cuaderno-la-mirada.jpg` |
| Sección de venta | `libros-firmados.html` → `#edicion-digital` |

### Redirects que faltan (los pone Daniel en el panel de Stripe — la API MCP no puede)
> **Por qué a mano:** `stripe_api_execute` de este MCP no serializa parámetros de tipo objeto anidado (falla con «Invalid object» en `after_completion`, y «Metadata must be a single object» en `metadata`). No es un problema de config: es un límite de la herramienta. Para una operación de dinero, además, ponerlo en el panel es lo más seguro y visible (regla §2).

En cada Payment Link → «After payment» → «Redirect customers to your website» → pegar:

| Payment Link | Redirect URL |
|---|---|
| Libro `plink_1Te9giFW3OLCwM3HYrm5mI4r` (`buy.stripe.com/dRmfZh2GS2GNgRdbvy2sM0i`) | `https://twimproject.com/descargas/gracias-engranajes-c69e607cf2.html?utm_source=stripe` |
| Cuaderno `plink_1Te9grFW3OLCwM3HQdHNjQyN` (`buy.stripe.com/14A00jchs95bbwT9nq2sM0j`) | `https://twimproject.com/descargas/gracias-mirada-07b0f6aade.html?utm_source=stripe` |

### Secuencia de salida a producción (regla cirujano · no cobrar sin haber entregado una vez)
1. Daniel pone los 2 redirects (tabla de arriba) en el panel de Stripe.
2. Mergear el PR (deja en producción las páginas de gracias + los PDF + la sección de venta).
3. **Compra de prueba reembolsable** de cada producto: pagar → comprobar que el redirect lleva a la página de gracias → que el PDF se descarga. Reembolsar las 2.
4. Solo si las 2 pruebas pasan, **anunciar/promocionar** la edición digital.

Hasta el paso 4, la sección existe pero no se difunde. Si se merge antes de poner los redirects, un comprador caería en la confirmación por defecto de Stripe sin enlace de descarga (recuperable a mano, pero a evitar).

## Regla crítica · el PDF NO se commitea

El PDF ensamblado es el **producto de pago**. Si se sube al repo, Netlify lo serviría público (gratis). Por eso:

- El PDF se **genera fuera del repo** (`/tmp/LEDLM-edicion-digital.pdf`) ejecutando `scripts/montar-pdf-engranajes-digital.py`. Reproducible siempre.
- **Nunca** añadir el PDF (ni el `LEDLM.pdf` interior como producto) a una ruta pública servida por Netlify.
- Pendiente con OK de Daniel: mover también el extra HTML y el cuaderno fuera de `documentos-internos/` público, o bloquearlos, al montar la entrega.

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
