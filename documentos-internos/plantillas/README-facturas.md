# Plantilla de factura de honorarios · Guía de uso

> Plantilla HTML reutilizable con diseño Mind World Project / TWIM, conforme a normativa española de facturación profesional sanitaria. **Los datos de pacientes se rellenan SIEMPRE en local** — nunca en chat con IA.

---

## Cuándo usar esta plantilla

- Facturación mensual a pacientes que la solicitan (renta IRPF, justificación de gastos sanitarios).
- Facturación puntual a pacientes que cierran un período de tratamiento.

## Cuándo NO usarla

- Si vas a facturar más de 5-10 facturas/mes de forma estable: **migra a un software de facturación profesional** (FacturaDirecta, Anfix, Quaderno o Holded). Ver `documentos-internos/google-ads-cumplimiento-y-reactivacion.md` para las recomendaciones por coste.
- A partir de **2026 la factura electrónica entre profesionales será obligatoria** en España (Ley Crea y Crece). El software dedicado lo cumple automáticamente; esta plantilla HTML/PDF sí es válida hoy pero no cumplirá el formato Facturae cuando la obligación entre en vigor para tu rango de facturación.

---

## Cómo rellenar la plantilla (local, sin IA)

### Opción A — Con tu navegador (más rápido)

1. Abre la plantilla en local: doble click en `factura-honorarios-paciente.html`. Se abre en Chrome/Safari/Firefox.
2. Click derecho → **Inspeccionar** (o pulsa `F12`). Se abre DevTools.
3. En la pestaña **Elements**, busca cada `{{PLACEHOLDER}}` y edítalo en línea con el valor real del paciente.
4. Cuando esté completa: click derecho en la página → **Imprimir** → "Guardar como PDF".
5. Guardar el PDF en tu carpeta local de facturas (cifrada o en disco con FileVault/BitLocker).
6. Cerrar el navegador. Los cambios en DevTools no se guardan en el archivo original.

### Opción B — Con tu editor de texto (más limpio)

1. Copia `factura-honorarios-paciente.html` a una carpeta **local cifrada** (ej: `~/Documents/facturas-pacientes/2026-04/`).
2. Renombra la copia: `factura-{{NUMERO}}-{{NOMBRE_PACIENTE}}.html` (ej: `factura-F-2026-049-marcos-palau.html`).
3. Ábrela con TextEdit / Notepad / VS Code.
4. Busca y reemplaza cada `{{PLACEHOLDER}}` con el valor real (Cmd+F → "Replace").
5. Guarda.
6. Abre en navegador → Imprimir → Guardar como PDF.
7. **Borra el .html con datos rellenados** una vez tengas el PDF (no es necesario conservar el HTML; el PDF queda como factura definitiva).

---

## Lista de placeholders a rellenar

| Placeholder | Qué pones | Ejemplo |
|---|---|---|
| `{{NUMERO_FACTURA}}` | Numerador correlativo. Sigue tu serie. | `F-2026-049` |
| `{{FECHA_EMISION}}` | Fecha de emisión en formato largo. | `1 de mayo de 2026` |
| `{{SUBTITULO}}` | Concepto general del período. | `Honorarios por tratamiento psicológico · Abril 2026` |
| `{{NOMBRE_PACIENTE}}` | Nombre y apellidos del paciente. | (nombre completo) |
| `{{DNI_PACIENTE}}` | DNI con letra. | (DNI) |
| `{{DIRECCION_PACIENTE_LINEA1}}` | Calle, número, piso. | (dirección) |
| `{{DIRECCION_PACIENTE_LINEA2}}` | CP + ciudad (+ provincia). | (CP ciudad) |
| `{{DESCRIPCION_SERVICIO}}` | Descripción corta. | `Honorarios por tratamiento psicológico` |
| `{{PERIODO}}` | Período facturado. | `Abril 2026` |
| `{{NUM_SESIONES}}` | Número total de sesiones del período. | `4` |
| `{{IMPORTE}}` | Importe total con moneda. Aparece en dos sitios: tabla + caja Total. | `260,00 €` |
| `{{SESIONES_FECHAS}}` | Fechas concretas de las sesiones. | `2, 9, 16 y 23 de abril de 2026` |

> **Nota:** `{{IMPORTE}}` aparece **dos veces** en el HTML (en la tabla y en la caja "Total a abonar"). Asegúrate de reemplazar las dos.

---

## Reglas obligatorias por normativa española

- **Numeración correlativa** sin saltos. La AEAT lo verifica si te audita.
- **Fecha de emisión** real (no antedatada).
- **Datos completos del emisor**: nombre, NIF, dirección. Ya pre-rellenados en la plantilla.
- **Datos completos del receptor**: nombre, NIF/DNI, dirección.
- **Descripción del servicio** lo bastante específica para que sea reconocible. "Tratamiento psicológico" + período sirve.
- **Mención de exención de IVA** con base legal (art. 20.1.3º Ley 37/1992). Ya incluida en la plantilla.
- **Importe total** claramente identificable.
- **Conservación**: el emisor (Daniel) debe conservar copia de cada factura **mínimo 6 años** (art. 30 Código de Comercio + LGT).

---

## Política de protección de datos clínicos

Las facturas a pacientes contienen **datos de categoría especial** (art. 9 RGPD: salud). Manejarlas correctamente:

### SÍ:
- Guardar los PDFs en **disco local con cifrado de disco activo** (FileVault en macOS, BitLocker en Windows).
- Mantener una **copia de seguridad cifrada** en un servicio que tengas declarado como encargado de tratamiento (Drive empresarial con DPA, NAS personal, disco externo cifrado).
- Conservar el archivo `.numerador.txt` o tu sistema de numeración aparte para no romper la serie.
- **Archivar** las facturas en estructura predecible: `~/facturas-pacientes/AAAA/AAAA-MM/`.

### NO:
- ❌ No subir HTMLs ni PDFs con datos rellenados a chats con IA (Claude, ChatGPT, etc.) ni a NotebookLM.
- ❌ No enviar por email sin cifrado al paciente — usar email con TLS estándar es suficiente para envío puntual al propio paciente, pero NUNCA reenviar a terceros (tu gestor SÍ es destinatario legítimo).
- ❌ No publicar capturas en redes sociales, ni siquiera anonimizadas parciales.
- ❌ No commitear PDFs de facturas al repositorio git (el `.gitignore` debería incluir `**/facturas/`, ver §siguiente).

### Añadir al `.gitignore` del repo

Para evitar que por error subas alguna vez una factura al repo:

```gitignore
# Facturas de pacientes — datos clínicos, fuera del repo
facturas/
facturas-pacientes/
**/factura-*.pdf
**/factura-*.html
```

Esta línea ya está añadida al .gitignore principal de TWIM Project.

---

## Cuándo migrar a software profesional

Señales claras:

- Facturas mensuales a >5 pacientes recurrentes (tiempo manual sale caro).
- Próxima entrada en vigor de factura electrónica obligatoria (2026 para algunos rangos).
- Pacientes que piden la factura en formato estándar (Facturae XML).
- Daniel quiere delegar facturación a VA o gestor.

En cualquiera de esos casos: dar de alta **FacturaDirecta** (~9 €/mes) o **Anfix** (~15 €/mes) y migrar la numeración. La plantilla HTML queda como respaldo histórico.

---

## Cierre

Esta plantilla resuelve el caso "tengo que facturar a 3-5 pacientes este mes y quiero que se vea bien" sin romper protección de datos. No resuelve el caso "tengo 30 facturas/mes y necesito numeración automática + DPA + Facturae". Para eso, software profesional.

— Documento generado el 1-05-2026. Si la AEAT cambia los requisitos formales o entra en vigor la obligación de Facturae para tu rango, revisar este README.
