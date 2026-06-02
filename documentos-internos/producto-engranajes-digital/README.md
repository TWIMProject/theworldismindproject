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
| Producto + Payment Link Stripe | ⏳ pendiente |
| Entrega segura | ⏳ **pendiente · requiere OK de Daniel (infraestructura)** |
| Landing de venta | ⏳ pendiente |

## Regla crítica · el PDF NO se commitea

El PDF ensamblado es el **producto de pago**. Si se sube al repo, Netlify lo serviría público (gratis). Por eso:

- El PDF se **genera fuera del repo** (`/tmp/LEDLM-edicion-digital.pdf`) ejecutando `scripts/montar-pdf-engranajes-digital.py`. Reproducible siempre.
- **Nunca** añadir el PDF (ni el `LEDLM.pdf` interior como producto) a una ruta pública servida por Netlify.
- Pendiente con OK de Daniel: mover también el extra HTML y el cuaderno fuera de `documentos-internos/` público, o bloquearlos, al montar la entrega.

## Plan de entrega segura (para ejecutar CON OK de Daniel · toca `netlify/functions` = infraestructura, regla §2)

1. **Producto Stripe** «Infoproducto · Los engranajes de la mente · Edición digital ampliada», 9,90 €, Stripe Checkout (no Payment Link estático).
2. **Webhook** (`netlify/functions/stripe-webhook.js`, ya existe): al evento `checkout.session.completed`, generar un **token de descarga firmado** (JWT con caducidad ~72 h y nº de descargas limitado) y enviarlo al email del comprador.
3. **Función de descarga** (`netlify/functions/descarga-libro.js`, nueva): valida el token y sirve el PDF desde una ubicación **no pública** (bundle de la función o storage privado). Sin token válido → 403.
4. **Marca de agua** con el email del comprador en cada PDF entregado (disuade el reenvío). Se aplica al vuelo en la función o pre-generando por compra.
5. Verificar en deploy preview antes de mergear. **No mergear a producción sin OK explícito de Daniel** (precedente PR #133).

Límite honesto asumido: un PDF, una vez descargado, es reenviable; sin DRM (no compensa a 9,90 €). Se blinda el **acceso** (solo el comprador recibe el enlace único) y se disuade con marca de agua. Esto cumple el «solo el comprador, si no nada» que pidió Daniel.

## Reproducir

```
python3 scripts/generar-portada-engranajes-digital.py   # portada
python3 scripts/montar-pdf-engranajes-digital.py         # PDF completo -> /tmp/LEDLM-edicion-digital.pdf
```
Requiere: Pillow, PyMuPDF, weasyprint (pip) + Instrument Serif TTF.
