# Sistema visual del logo TWIM Project · Mayo 2026

> Documento creado el **23 may 2026** tras 3 reportes consecutivos de Daniel sobre el logo viéndose mal en headers verdes (PR #210, #213, #214 no resolvieron porque atacaron síntomas en vez de la causa raíz · contraste cromático).
>
> **Función · que la próxima sesión sepa exactamente qué versión del logo usar en cada contexto sin tener que iterar 3 veces sobre lo mismo.**

---

## 1 · Las 3 versiones del logo · qué es cada una

| Archivo | Color | Tamaño | Cuándo usarlo |
|---|---|---|---|
| `logo-mindworld.png` (raíz) | **Bicromo** · verde `#173D30` + beige `#C2A78B` sobre transparente | 745×448 RGBA | Favicon · OG image · Twitter card · contextos donde el fondo es claro o variable (pestaña del navegador, previews de redes sociales, capturas) |
| `assets/logo-mindworld-transparent.png` | **Bicromo** · idéntico al raíz | 745×448 RGBA | Headers crema/blancos de landings (DDBEO preventa, DDO preventa, lead-volver-a-mi, talleres/volver-a-mi, conferencias) |
| `assets/logo-mindworld-on-dark.png` | **Monocromo crema** `#FDFCFA` sobre transparente | 745×448 RGBA | Headers verde oscuro `#173D30` · todas las landings con `<header>` o `.site-header` o `.landing-header` con fondo `var(--green-dark)` |

Equivalentes `.webp` existen para los 3 (`.png` → `.webp`).

---

## 2 · Regla inviolable · qué versión usar según el contexto

### 2.1 · `<link rel="icon">` y `<link rel="apple-touch-icon">`

**Siempre** apuntar a `logo-mindworld.png` raíz (versión bicromo). El navegador renderiza el favicon sobre fondo claro/gris/oscuro variable según el tema del SO o el sitio anclado · la versión bicromo verde+beige se distingue en TODOS los contextos. La versión `on-dark` (crema) sería invisible sobre fondo blanco.

```html
<link rel="icon" href="logo-mindworld.png" type="image/png">
<link rel="apple-touch-icon" href="logo-mindworld.png">
```

### 2.2 · `og:image` / `twitter:image`

Igual · `logo-mindworld.png` raíz. Facebook, LinkedIn, Twitter renderizan previews sobre fondo claro.

```html
<meta property="og:image" content="https://twimproject.com/logo-mindworld.png">
```

### 2.3 · `<img>` dentro del header de la página

**Depende del color de fondo del header.** Antes de decidir, mira el CSS del header.

#### Si el header es verde oscuro · `assets/logo-mindworld-on-dark.png`

CSS típico que delata header verde:

```css
header { background: var(--green-dark); ... }
.site-header { background: var(--green-dark); ... }
.landing-header { background: #173D30; ... }
header { background: linear-gradient(...,#173D30...); }
```

Páginas conocidas con header verde · `index.html`, todas las `psicologo-*.html`, `daniel-orozco-abia.html`, `lead-burnout-5-senales.html`, `test-sindrome-impostora.html`, `nopuedoparar-taller.html`, `libro/capitulo-3/index.html`, `libro-engranajes-mente/index.html`, `talleres/index.html`, `talleres/gracias-reserva.html`, `talleres/tdah-adolescentes/index.html`, `talleres/bachillerato-motivacion/index.html`, `psicologo-ansiedad-valencia/index.html`, `soluciones/index.html`, `newsletter/index.html`, **todos los `insights/*.html`**.

#### Si el header es crema/blanco · `assets/logo-mindworld-transparent.png`

CSS típico que delata header crema:

```css
header.site { background: var(--cream); ... }
header.site { background: #FDFCFA; ... }
```

Páginas conocidas con header crema · `dejadebuscarteenotros-preventa.html`, `dejadeobligarte-preventa.html`, `lead-volver-a-mi-5-senales.html`, `talleres/volver-a-mi/index.html`, `conferencias/index.html`.

### 2.4 · Otros contextos visuales

- **Banners email masthead** (carta editorial, automation) · usar el logo recortado del template y recolorearlo si el fondo es oscuro (ver `email-templates/automations-listas-lead-21-may/banner-*.png` y `assets/email-header-A-logo-solo.png`).
- **PDFs sobre fondo verde** (header del PDF de factura, etc.) · `assets/logo-mindworld-on-dark.png`.
- **Carruseles IG** · `assets/logo-mindworld-transparent.png` salvo que el fondo sea verde.

---

## 3 · Protocolo de verificación visual ANTES de mergear cualquier cambio del logo

> Causa raíz de los 3 errores anteriores · no verifiqué visualmente cómo se renderiza el PNG en su contexto antes de declarar resuelto el bug.

**Verificación obligatoria · pasos:**

1. Abrir el PNG modificado con el tool `Read` para ver visualmente los colores reales del archivo.
2. Identificar el fondo del contexto donde se usa el logo (verde · crema · blanco).
3. **Mentalmente componer** logo + fondo · ¿hay contraste suficiente? Cualquier color del logo igual o casi igual al fondo se va a fundir.
4. Si hay duda, regenerar una variante con tono más alto contraste.
5. Solo después de pasar el test mental de contraste, commitear.

**Trampa típica · «el PNG es transparente»** no basta. Transparente significa que el fondo no estorba, pero los píxeles que SÍ tienen color tienen que contrastar con el fondo de la página. Verde sobre verde = invisible aunque el PNG sea transparente.

---

## 4 · Patrón anti-recurrencia (histórico de fallos para que la próxima sesión los reconozca)

| PR | Hipótesis equivocada | Causa real |
|---|---|---|
| #210 | «basta con transparentar el PNG» | Faltaba contraste cromático sobre verde |
| #213 | «el padding interno del PNG cuadrado parece recuadro» | Mismo: contraste cromático |
| #214 | «inconsistencia texto/logo entre páginas» | Mismo: contraste cromático del logo bicromo sobre verde |
| #217 | (correcto) sustituir el binario raíz por la versión on-dark | Causa raíz · pero introdujo bug NUEVO en favicon/og |
| **fix actual (24-may)** | Mantener raíz bicromo (favicon ok) + apuntar 50+ HTML con header verde a `on-dark` explícito | Estable a futuro |

---

## 5 · Si en el futuro hay que añadir una nueva página

1. Decidir el color de fondo del header (verde u otro).
2. **Si verde** · usar `<img src="<ruta>/assets/logo-mindworld-on-dark.png">` con su `.webp` source equivalente.
3. **Si crema/otro claro** · usar `<img src="<ruta>/assets/logo-mindworld-transparent.png">`.
4. Para favicon y og:image · apuntar al raíz `logo-mindworld.png` (bicromo) **siempre**.
5. Verificar visualmente con el protocolo §3 antes de mergear.

---

— Documento de referencia. Actualizar si la paleta TWIM cambia o si se introduce una 4ª versión del logo.
