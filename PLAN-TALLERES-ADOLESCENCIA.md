# Plan de acción: Llenar los dos talleres de adolescencia

**Fecha:** 20 de marzo de 2026
**Objetivo:** 12 plazas totales (6 + 6) para septiembre 2026
**Tiempo disponible:** ~6 meses

---

## Diagnóstico actual

### Lo que ya está bien hecho
- Las dos landing pages tienen copy de altísima calidad, psicológicamente sofisticado y orientado a padres
- SEO técnico correcto: Schema.org (Course, FAQPage), meta tags, canonical URLs, sitemap
- Estructura clara: cada taller tiene su propia página dedicada
- Cross-linking entre los dos talleres
- Presencia en homepage con sección destacada y barra de anuncio
- FAQ bien pensadas que abordan objeciones reales de los padres
- Formulario de contacto con opciones específicas para cada taller

### Problemas críticos detectados

#### 1. FUNNEL DE CONVERSIÓN ROTO
- **El único CTA es un mailto:** tanto en hero como en el CTA final, el usuario debe abrir su cliente de correo. Esto genera una fricción enorme, especialmente en móvil (donde muchos no tienen configurado el mailto)
- **No hay formulario de contacto en las landing pages de los talleres.** El formulario Formspree solo está en la homepage
- **No hay sistema de reserva/lista de espera.** Sin manera de "apartar" plaza con baja fricción
- **El PDF de información de talleres es un fake:** el formulario de email en la homepage no envía el email a ningún sitio (el `submit` solo oculta el form y muestra un link de descarga a `Grupo_Online_Info.pdf`, que además parece ser un PDF de otro programa, no de los talleres)

#### 2. ZERO PRUEBA SOCIAL
- No hay ni un solo testimonio de padres o adolescentes
- No hay datos de ediciones anteriores (aunque sea la primera, se puede referenciar experiencia clínica con adolescentes)
- No hay contador de plazas reservadas/disponibles
- No hay logos de colegios, asociaciones TDAH o colaboradores

#### 3. ZERO CONTENIDO DE ATRACCIÓN PARA EL PÚBLICO OBJETIVO
- Los 20+ artículos del blog están 100% orientados a adultos (burnout, trabajo, autoexigencia, dependencia emocional)
- **No existe ni un solo artículo sobre adolescencia, TDAH, motivación escolar o crianza**
- Esto significa que no hay tráfico orgánico de padres buscando ayuda para sus hijos adolescentes

#### 4. SIN CAPTURA DE LEADS
- No hay newsletter
- No hay lead magnet real para padres (guía, checklist, vídeo)
- No hay pixel de remarketing configurado (solo GA4 básico)
- No hay seguimiento de conversiones específico para los talleres

#### 5. URGENCIA Y ESCASEZ MAL COMUNICADAS
- Se menciona "Solo 6 plazas" pero sin indicar cuántas quedan
- No hay fecha límite de inscripción
- No hay "early bird" ni incentivo temporal

#### 6. ERRORES TÉCNICOS EN EL SITEMAP
- El sitemap.xml tiene XML malformado: dos `<urlset>` abiertos, URLs duplicadas (`elegir-es-perder`, `sindrome-del-impostor`, `privacy.html`), `<loc>` tags dentro de otros `<url>` sin cerrar correctamente
- Esto puede afectar la indexación en Google

---

## Plan de acción por prioridad

### FASE 1 — URGENTE (semanas 1-2): Reparar el funnel de conversión

#### 1.1 Añadir formulario Formspree en cada landing page de taller
- Reemplazar el bloque CTA final (`cta-box`) que tiene solo un mailto por un formulario embebido
- Campos: Nombre del padre/madre, Email, Nombre y edad del hijo/a, Mensaje opcional
- Mantener el mailto como alternativa secundaria
- **Archivo:** `talleres/tdah-adolescentes/index.html` (líneas 269-276)
- **Archivo:** `talleres/bachillerato-motivacion/index.html` (líneas 272-279)

#### 1.2 Añadir botón de WhatsApp como canal alternativo
- Muchos padres prefieren WhatsApp al email
- Añadir como segundo CTA junto al "Quiero información"
- Formato: `https://wa.me/34625231297?text=...`

#### 1.3 Crear un lead magnet real para padres
- Ejemplo: "5 señales de que tu hijo adolescente necesita más que clases de repaso" (PDF breve)
- O: "Guía para padres: cómo hablar con tu adolescente cuando sientes que no te escucha"
- Integrarlo con captura de email real (Formspree o Mailchimp)
- El formulario actual del homepage (`workshops-info-form`) no hace nada con el email: hay que conectarlo

#### 1.4 Corregir el sitemap.xml
- Eliminar XML duplicado y malformado
- Asegurar que cada URL aparece una sola vez con formato correcto

---

### FASE 2 — ALTA PRIORIDAD (semanas 2-4): Contenido de atracción para padres

#### 2.1 Crear cluster de artículos sobre adolescencia y TDAH (mínimo 4-6)
El blog actual no tiene NADA dirigido a padres de adolescentes. Artículos propuestos:

**Para el taller TDAH:**
1. "TDAH en adolescentes: por qué la medicación sola no es suficiente"
2. "Autoestima y TDAH: cómo reconstruir lo que las notas han destruido"
3. "Mi hijo con TDAH no quiere estudiar: lo que realmente está pasando"

**Para el taller Bachillerato:**
4. "Mi hijo de bachillerato no sabe qué estudiar: por qué presionarle es peor"
5. "Apatía adolescente: cuando 'no me importa nada' esconde algo más profundo"
6. "Qué hacer cuando tu hijo adolescente se desconecta de todo"

**Cada artículo debe:**
- Incluir CTA al taller correspondiente al final
- Tener Schema.org Article
- Estar optimizado para las keywords que buscan los padres
- Enlazar a la landing page del taller

#### 2.2 Crear una página intermedia "Talleres para adolescentes"
- URL: `/talleres/` (index)
- Página puente que presente ambos talleres juntos
- Útil para compartir un solo link en redes sociales

---

### FASE 3 — PRIORIDAD MEDIA (semanas 3-6): Prueba social y confianza

#### 3.1 Añadir testimonios o casos (anonimizados)
- Si no hay testimonios de talleres anteriores (primera edición), usar:
  - Testimonios de padres de pacientes adolescentes en consulta individual (anonimizados)
  - Citas de investigación que avalen el formato grupal
  - Fragmentos de reseñas de los libros en Amazon
- Ubicación: entre la sección "Lo que un grupo puede hacer..." y el bloque de detalles

#### 3.2 Añadir sección "Por qué un grupo y no terapia individual"
- Explicar las ventajas específicas del formato grupal con referencias
- Esto diferencia el servicio y justifica el precio

#### 3.3 Añadir foto de Daniel o del espacio
- Las landing pages de talleres no tienen ni una sola imagen
- Una foto del profesional o del espacio donde se realizará el taller genera confianza
- Las imágenes OG (`og:image`) tampoco están definidas en las landing pages de talleres

---

### FASE 4 — PRIORIDAD MEDIA (semanas 4-8): Estrategia de captación activa

#### 4.1 Contenido en redes sociales (Instagram/YouTube)
- Crear serie de reels/vídeos cortos dirigidos a padres:
  - "3 cosas que puedes hacer esta noche si tu hijo tiene TDAH" (ya está en la web, convertir a vídeo)
  - "Por qué tu hijo de bachillerato dice que no le importa nada"
  - "Lo que la medicación no puede hacer por tu hijo con TDAH"
- Cada vídeo con CTA a la landing page del taller

#### 4.2 Colaboraciones estratégicas
- Contactar asociaciones TDAH en Valencia (APADAH, APNADAH Valencia)
- Contactar colegios e institutos de Valencia para presentar los talleres
- Contactar orientadores escolares como canal de derivación
- Contactar pediatras y psiquiatras infanto-juveniles de Valencia

#### 4.3 Google Ads (micro-presupuesto)
- Campañas de búsqueda para:
  - "psicólogo TDAH adolescentes Valencia"
  - "taller adolescentes Valencia"
  - "mi hijo no quiere estudiar ayuda Valencia"
- Landing pages ya optimizadas, solo falta el formulario embebido (Fase 1)

---

### FASE 5 — OPTIMIZACIÓN CONTINUA (semanas 6-24): Seguimiento y ajuste

#### 5.1 Implementar tracking de conversiones en GA4
- Eventos personalizados para:
  - Click en "Quiero información" (mailto)
  - Envío de formulario de contacto
  - Click en WhatsApp
  - Descarga de PDF
- Esto permite medir qué canal convierte mejor

#### 5.2 Añadir indicador de plazas disponibles
- Mostrar "X de 6 plazas reservadas" dinámicamente
- Genera urgencia real y prueba social implícita
- Puede ser manual (actualizado en HTML cuando se reserve una plaza)

#### 5.3 Implementar secuencia de email post-contacto
- Cuando un padre pide información, responder con:
  1. Email inmediato con información del taller (PDF real)
  2. A los 3 días: email con un artículo relevante del blog
  3. A los 7 días: email recordatorio con "quedan X plazas"
- Esto requiere una herramienta de email marketing (Mailchimp, ConvertKit, o similar)

#### 5.4 Página de agradecimiento post-formulario
- Redirigir tras envío de formulario a una página de "Gracias" con:
  - Confirmación de que recibirán respuesta en 24h
  - Link al PDF de información
  - CTA secundario a los artículos del blog sobre adolescencia

---

## Resumen de impacto esperado

| Acción | Esfuerzo | Impacto en conversión |
|--------|----------|-----------------------|
| Formulario en landing pages | Bajo | Alto |
| WhatsApp como canal | Bajo | Alto |
| Lead magnet para padres | Medio | Alto |
| Artículos de blog sobre adolescencia | Alto | Alto (tráfico orgánico) |
| Testimonios/prueba social | Medio | Alto |
| Foto de Daniel en landings | Bajo | Medio |
| Redes sociales (reels para padres) | Alto | Medio-Alto |
| Colaboraciones (colegios, asociaciones) | Medio | Muy Alto |
| Google Ads | Medio | Alto (tráfico inmediato) |
| Contador de plazas | Bajo | Medio |
| Corregir sitemap.xml | Bajo | Bajo-Medio |
| Secuencia de email | Medio | Medio |
| Tracking GA4 | Bajo | Bajo (pero necesario para medir) |

---

## Orden de ejecución recomendado

1. **Esta semana:** Formularios en landings + WhatsApp + corregir sitemap
2. **Semana 2:** Lead magnet + OG images en landings de talleres
3. **Semanas 2-4:** Escribir y publicar 4-6 artículos sobre adolescencia/TDAH
4. **Semanas 3-5:** Testimonios + foto en landings + página índice de talleres
5. **Semana 4 en adelante:** Contenido en redes + colaboraciones + Google Ads
6. **Continuo:** Tracking + secuencia email + contador de plazas

---

## Notas técnicas adicionales

- El `index.html` tiene un error de HTML en la sección FAQ: falta cerrar un `</details>` y hay un `<summary>` suelto (líneas 1278-1281)
- Las landing de talleres no tienen Google Analytics (falta el script gtag.js)
- Las landing de talleres no tienen `og:image`, lo que limita cómo se ven al compartir en redes
- El archivo CSS compartido `twim-styles.css` se usa en las landings pero las variables CSS están definidas solo en `index.html`, lo que puede causar problemas de estilo
