# Plantillas de factura · Guía de uso

> Dos plantillas HTML reutilizables con marca Mind World Project / TWIM, conformes a normativa española de facturación profesional sanitaria.
>
> **Los datos de pacientes se rellenan SIEMPRE en local** — nunca en chat con IA, nunca en el repositorio.

---

## Las dos plantillas disponibles

### 1. `factura-mensual-paciente.html` — para facturación recurrente mensual

**Cuándo usarla:** los pacientes que te piden factura mes a mes (ej. Marcos Palau, Guillem Chinesta, Pablo Cantero).

**Estilo:** limpio, formal, fondo blanco, logo Mind World en esquina superior derecha. Tabla de profesional + tabla de servicios con fila adicional para listar las fechas de las sesiones del mes.

**Placeholders:** `{{NOMBRE_PACIENTE}}`, `{{DNI_PACIENTE}}`, `{{NUMERO_FACTURA}}`, `{{FECHA_EMISION}}`, `{{NUM_SESIONES}}`, `{{IMPORTE}}`, `{{MES}}`, `{{SESIONES_FECHAS}}`.

### 2. `factura-anual-renta.html` — para Renta / IRPF (ejercicio fiscal completo)

**Cuándo usarla:** los pacientes que te piden una factura agregada anual para declarar gastos sanitarios en su IRPF.

**Estilo:** header con banda verde TWIM (#173D30), logo Mind World blanco invertido, dos cajas (emisor / receptor), tabla con período + sesiones + importe, total destacado en caja verde, declaración IRPF y firma.

**Placeholders:** `{{NOMBRE_PACIENTE}}`, `{{DNI_PACIENTE}}`, `{{DIRECCION_PACIENTE_LINEA1}}`, `{{DIRECCION_PACIENTE_LINEA2}}`, `{{NUMERO_FACTURA}}`, `{{FECHA_EMISION}}`, `{{ANIO}}`, `{{PERIODO}}`, `{{NUM_SESIONES}}`, `{{IMPORTE}}`.

> El año del ejercicio fiscal va en `{{ANIO}}`. Reemplazas con el año correspondiente cada vez (2025, 2026, 2027…).

---

## Logo

`logo-mindworld.png` está en la misma carpeta que las plantillas. Las dos plantillas lo referencian con ruta relativa (`logo-mindworld.png`).

**Cuando copies una plantilla a otra carpeta para rellenar, copia también `logo-mindworld.png`** en la misma carpeta. Si no, el logo no aparecerá al imprimir.

---

## Cómo rellenar (local, sin IA)

### Opción A — Con tu navegador (más rápido)

1. Abre la plantilla en local: doble click en `factura-mensual-paciente.html` (o `factura-anual-renta.html`). Se abre en el navegador.
2. Click derecho → **Inspeccionar** (o pulsa `F12`). Se abre DevTools.
3. En la pestaña **Elements**, busca cada `{{PLACEHOLDER}}` y edítalo con el valor real del paciente.
4. Cuando esté completa: click derecho → **Imprimir** → **Guardar como PDF**.
5. Guarda el PDF en tu carpeta local cifrada de facturas.
6. Cierra el navegador. Los cambios en DevTools no se guardan en el archivo original — la plantilla queda intacta para la siguiente factura.

### Opción B — Con tu editor de texto (más limpio)

1. Crea una carpeta local cifrada (ej: `~/Documents/facturas-pacientes/2026-04/`).
2. Copia ahí: la plantilla HTML que vayas a usar **+ `logo-mindworld.png`**.
3. Renombra la copia: `factura-{{NUMERO}}-{{NOMBRE_PACIENTE}}.html` (ej: `factura-F-2026-049-marcos-palau.html`).
4. Ábrela con TextEdit / Notepad / VS Code.
5. Busca y reemplaza cada `{{PLACEHOLDER}}` con el valor real (Cmd+F → "Replace").
6. Guarda.
7. Abre en navegador → Imprimir → **Guardar como PDF**.
8. **Borra el .html con datos rellenados** una vez tengas el PDF (no es necesario conservar el HTML; el PDF queda como factura definitiva).

---

## Tabla de placeholders

### Plantilla mensual (`factura-mensual-paciente.html`)

| Placeholder | Qué pones | Ejemplo |
|---|---|---|
| `{{NUMERO_FACTURA}}` | Numerador correlativo de tu serie. | `F-2026-049` |
| `{{FECHA_EMISION}}` | Fecha de emisión. | `1 de mayo de 2026` |
| `{{NOMBRE_PACIENTE}}` | Nombre y apellidos del paciente. | (nombre completo) |
| `{{DNI_PACIENTE}}` | DNI con letra. | (DNI) |
| `{{NUM_SESIONES}}` | Número total de sesiones del mes. | `4` |
| `{{IMPORTE}}` | Importe total con moneda. **Aparece dos veces** (fila de servicio + fila de total). | `260,00 €` |
| `{{MES}}` | Nombre del mes facturado. | `abril` |
| `{{SESIONES_FECHAS}}` | Días concretos de las sesiones. | `2, 9, 16 y 23` |

### Plantilla anual Renta (`factura-anual-renta.html`)

| Placeholder | Qué pones | Ejemplo |
|---|---|---|
| `{{NUMERO_FACTURA}}` | Numerador correlativo. | `F-2026-001` |
| `{{FECHA_EMISION}}` | Fecha de emisión. | `29 de abril de 2026` |
| `{{ANIO}}` | Año del ejercicio fiscal facturado. | `2025` |
| `{{NOMBRE_PACIENTE}}` | Nombre y apellidos. | (nombre completo) |
| `{{DNI_PACIENTE}}` | DNI con letra. | (DNI) |
| `{{DIRECCION_PACIENTE_LINEA1}}` | Calle, número, piso. | (dirección) |
| `{{DIRECCION_PACIENTE_LINEA2}}` | CP + ciudad. | (CP ciudad) |
| `{{PERIODO}}` | Período facturado. | `Ene–Oct 2025` |
| `{{NUM_SESIONES}}` | Total de sesiones del año. | `23` |
| `{{IMPORTE}}` | Importe total. **Aparece dos veces** (tabla + caja Total). | `1.150,00 €` |

> Importante: en ambas plantillas, `{{IMPORTE}}` aparece **dos veces**. Asegúrate de reemplazar las dos ocurrencias.

---

## Reglas obligatorias por normativa española

- **Numeración correlativa** sin saltos. Mantén una serie única (ej: `F-2026-001`, `F-2026-002`…). Si emites mensual + anual, no mezcles series.
- **Fecha de emisión** real (no antedatada).
- **Datos completos del emisor**: nombre, NIF, dirección. Pre-rellenados en ambas plantillas.
- **Datos completos del receptor**: nombre, NIF/DNI. Dirección obligatoria solo en la anual de Renta.
- **Descripción del servicio** lo bastante específica.
- **Mención de exención de IVA** con base legal (art. 20.1.3º Ley 37/1992). Pre-incluida en ambas.
- **Importe total** claramente identificable.
- **Conservación**: copia de cada factura **mínimo 6 años** (art. 30 Código de Comercio + LGT).

---

## Política de protección de datos clínicos

Las facturas a pacientes contienen **datos de categoría especial** (art. 9 RGPD: salud).

### SÍ:
- Guardar los PDFs en **disco local con cifrado activo** (FileVault macOS, BitLocker Windows).
- Copia de seguridad cifrada en servicio con DPA firmado.
- Estructura predecible: `~/facturas-pacientes/AAAA/AAAA-MM/`.
- Conservar tu sistema de numeración aparte para no romper la serie.

### NO:
- ❌ Subir HTMLs ni PDFs con datos a chats con IA (Claude, ChatGPT, NotebookLM…).
- ❌ Email sin cifrar a terceros (al propio paciente sí, con TLS estándar es suficiente).
- ❌ Capturas en redes sociales.
- ❌ Commitear al repositorio. El `.gitignore` ya bloquea `factura-F-*.pdf`, `factura-2*.pdf` y `facturas-pacientes/`.

---

## Cuándo migrar a software profesional

Señales claras:

- Facturas mensuales a >5 pacientes recurrentes.
- Próxima entrada en vigor de factura electrónica obligatoria (Ley Crea y Crece, 2026 para algunos rangos).
- Pacientes que piden formato Facturae XML.
- Daniel quiere delegar facturación a VA o gestor.

Recomendaciones:

| Software | Coste | Pro |
|---|---|---|
| **FacturaDirecta** | 9 €/mes | Español, simple, autónomos |
| **Anfix** | 15-25 €/mes | Conecta con gestoría, AEAT-ready |
| **Quaderno** | 19 €/mes | Multi-país, buena UX |
| **Holded** | 12-30 €/mes | Más completo, contabilidad incluida |

Cualquiera de ellos lleva numeración automática, custodia con DPA RGPD-compliant, exporta a tu gestor fiscal y cumple Facturae cuando entre en vigor para tu rango.

---

## Cierre

Las dos plantillas resuelven el caso "facturar a 3-10 pacientes/mes con buen diseño y sin romper protección de datos". Para >10 facturas/mes o cumplimiento Facturae automático: software profesional.

— Documento generado el 1-05-2026. Si la AEAT cambia los requisitos formales o entra en vigor la obligación de Facturae para tu rango, revisar este README y las plantillas.
