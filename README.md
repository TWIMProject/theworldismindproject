<div align="center">

# 🌎 The World Is Mind Project

### Transformando la ansiedad laboral en ventaja competitiva

[![Website](https://img.shields.io/badge/web-twimproject.com-D74A2B?style=for-the-badge&logo=google-chrome&logoColor=white)](https://twimproject.com)
[![License](https://img.shields.io/badge/license-CC%20BY--NC--ND%204.0-B2361B?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/status-production-00ff88?style=for-the-badge)]()

**Sitio web oficial del proyecto de divulgación y bienestar psicológico**  
Impulsado por **Daniel Orozco Abia** | Psicólogo General Sanitario CV11515

[🌐 Ver Sitio Web](https://twimproject.com) • [📧 Contacto](mailto:danielorozco@twimproject.com) • [📚 Libro](https://amzn.eu/d/38Veu6F)

---

</div>

## 📋 Tabla de Contenidos

- [Sobre el Proyecto](#-sobre-el-proyecto)
- [Características](#-características)
- [Demo en Vivo](#-demo-en-vivo)
- [Tecnologías](#-tecnologías)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Instalación y Desarrollo](#-instalación-y-desarrollo)
- [Despliegue](#-despliegue)
- [SEO y Performance](#-seo-y-performance)
- [Contribución](#-contribución)
- [Licencia](#-licencia)
- [Contacto](#-contacto)

---

## 🎯 Sobre el Proyecto

**The World Is Mind Project (TWIM)** es una plataforma de divulgación y servicios profesionales enfocada en transformar la ansiedad laboral y el burnout en rendimiento sostenible mediante:

- 🏢 **Método MindShift** para empresas
- 🧠 **Workshops experienciales** anti-burnout
- 👥 **Mentoring ejecutivo** para líderes
- 📊 **Diagnósticos 360º** organizacionales
- 📚 **Contenido educativo** basado en psicoanálisis aplicado

### Misión

> Convertir la ansiedad laboral en ventaja competitiva mediante ciencia psicológica, narrativa estratégica y formación experiencial. Ayudar a personas y equipos a reestructurar su mente para rendir sin romperse.

### Impacto

- ✅ +12 años de experiencia profesional
- ✅ Colaboraciones con Nike, FC Barcelona, Amazon
- ✅ -25% reducción de estrés en 30 días (workshops)
- ✅ Cientos de personas y equipos transformados

---

## ✨ Características

### 🎨 Diseño y UX
- ✅ Diseño responsive mobile-first
- ✅ Interfaz limpia y minimalista
- ✅ Navegación intuitiva con smooth scroll
- ✅ Accesibilidad WCAG 2.1 nivel AA
- ✅ Dark mode friendly

### ⚡ Performance
- ✅ Lighthouse Score: 90+ (Performance)
- ✅ First Contentful Paint: <1.5s
- ✅ Lazy loading en imágenes e iframes
- ✅ CSS y JavaScript optimizados
- ✅ Recursos precargados (preload/preconnect)

### 🔍 SEO Optimizado
- ✅ Meta tags completos (Open Graph + Twitter Cards)
- ✅ Structured Data (Schema.org):
  - Organization/ProfessionalService
  - Person (con credenciales)
  - Service (Método MindShift)
  - Book (Los engranajes de la mente)
  - FAQPage
  - BreadcrumbList
- ✅ Sitemap.xml y robots.txt
- ✅ Canonical URLs
- ✅ Rich Snippets ready
- ✅ SEO Score: 92/100

### 🛡️ Seguridad
- ✅ HTTPS nativo (GitHub Pages)
- ✅ Honeypot anti-spam en formularios
- ✅ rel="noopener noreferrer" en enlaces externos
- ✅ CSP headers configurables

### 📱 Funcionalidades
- ✅ Integración con Stripe (pagos)
- ✅ Formulario de contacto (Formspree)
- ✅ Tienda Spreadshop integrada
- ✅ Modals para PDFs informativos
- ✅ Video embeds (YouTube, LinkedIn)
- ✅ Social media links

---

## 🚀 Demo en Vivo

🌐 **Producción:** [https://twimproject.com](https://twimproject.com)

> El sitio se actualiza automáticamente con cada `push` a la rama `main` gracias a GitHub Pages.

**Vista previa de secciones:**
- [Inicio](https://twimproject.com/#home)
- [Sobre Mí](https://twimproject.com/#about)
- [Soluciones](https://twimproject.com/#solutions)
- [Programas](https://twimproject.com/#programs)
- [Libro](https://twimproject.com/#libros)
- [Contacto](https://twimproject.com/#contacto)

---

## 🛠 Tecnologías

<div align="center">

| Categoría | Tecnologías |
|-----------|-------------|
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla) |
| **Tipografía** | Barlow Condensed (Google Fonts) |
| **Iconos** | Font Awesome 6.5 |
| **Analytics** | Google Analytics 4 (opcional) |
| **Formularios** | Formspree |
| **Pagos** | Stripe |
| **E-commerce** | Spreadshop |
| **Hosting** | GitHub Pages |
| **CI/CD** | GitHub Actions |
| **SEO** | Schema.org JSON-LD, Sitemap XML |

</div>

### Por qué estas tecnologías

- **Sin frameworks** → Carga ultrarrápida (<500ms FCP)
- **HTML/CSS vanilla** → Mantenimiento simple, sin dependencias
- **GitHub Pages** → Hosting gratuito, HTTPS automático, CDN global
- **Servicios SaaS** → Stripe, Formspree, Spreadshop (sin backend propio)

---

## 📂 Estructura del Proyecto

```
theworldismindproject/
│
├── index.html                      # Página principal (landing page)
├── robots.txt                      # Configuración para crawlers
├── sitemap.xml                     # Mapa del sitio para SEO
├── privacy.html                    # Política de privacidad
│
├── assets/
│   ├── images/
│   │   ├── LOGO.png               # Logo principal TWIM
│   │   ├── BUSTO.png              # Imagen hero background
│   │   ├── twimp.jpg              # Foto conferencia
│   │   ├── imagen amazon.jpeg     # Portada libro
│   │   └── ...
│   │
│   ├── css/                        # (Opcional) Estilos externos
│   │   └── main.css
│   │
│   └── js/                         # (Opcional) Scripts externos
│       └── main.js
│
├── docs/
│   ├── Grupo_Online_Info.pdf      # Info programa online
│   └── Programa_In-Company_Info.pdf
│
├── README.md                       # Este archivo
├── LICENSE                         # CC BY-NC-ND 4.0
└── .gitignore                      # Archivos ignorados por git
```

---

## 💻 Instalación y Desarrollo

### Prerequisitos

- Git instalado
- Editor de código (VS Code recomendado)
- Navegador web moderno

### Clonar el repositorio

```bash
git clone https://github.com/tuUsuario/theworldismindproject.git
cd theworldismindproject
```

### Desarrollo Local

**Opción 1: Abrir directamente**
```bash
# Simplemente abre index.html en tu navegador
open index.html  # macOS
start index.html # Windows
xdg-open index.html # Linux
```

**Opción 2: Servidor local (recomendado)**
```bash
# Con Python 3
python -m http.server 8000

# Con Node.js (npx)
npx http-server -p 8000

# Con PHP
php -S localhost:8000
```

Luego visita: `http://localhost:8000`

### Editar contenido

1. **Textos:** Edita directamente en `index.html`
2. **Estilos:** Modifica la sección `<style>` en el `<head>`
3. **Imágenes:** Reemplaza archivos en `/assets/images/`
4. **Schema.org:** Edita los bloques `<script type="application/ld+json">`

---

## 🚀 Despliegue

### GitHub Pages (Automático)

1. **Configurar GitHub Pages:**
   ```bash
   # En tu repositorio de GitHub
   Settings → Pages → Source: main branch
   ```

2. **Hacer cambios:**
   ```bash
   git add .
   git commit -m "Descripción de cambios"
   git push origin main
   ```

3. **Esperar despliegue:** 1-2 minutos
4. **Ver en vivo:** `https://tuUsuario.github.io/theworldismindproject`

### Dominio personalizado

1. En `Settings → Pages → Custom domain` añade: `twimproject.com`
2. Configura DNS en tu proveedor:
   ```
   A     @       185.199.108.153
   A     @       185.199.109.153
   A     @       185.199.110.153
   A     @       185.199.111.153
   CNAME www     tuUsuario.github.io
   ```
3. Espera propagación DNS (24-48h)

---

## 🔍 SEO y Performance

### Verificar SEO

**Rich Results Test:**
```bash
https://search.google.com/test/rich-results?url=https://twimproject.com
```

**PageSpeed Insights:**
```bash
https://pagespeed.web.dev/analysis?url=https://twimproject.com
```

**Mobile-Friendly Test:**
```bash
https://search.google.com/test/mobile-friendly?url=https://twimproject.com
```

### Google Search Console

1. Verificar propiedad: https://search.google.com/search-console
2. Enviar sitemap: `https://twimproject.com/sitemap.xml`
3. Solicitar indexación de páginas principales

### Analytics (Opcional)

Para añadir Google Analytics 4:

```html
<!-- Añadir antes del </head> -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

---

## 🤝 Contribución

Las contribuciones son bienvenidas, especialmente en:

- 🐛 Reportar bugs
- 💡 Sugerir mejoras
- 📝 Mejorar documentación
- ♿ Accesibilidad
- 🌐 Traducciones

### Cómo contribuir

1. Fork el proyecto
2. Crea una rama: `git checkout -b feature/nueva-caracteristica`
3. Commit cambios: `git commit -m 'Añade nueva característica'`
4. Push a la rama: `git push origin feature/nueva-caracteristica`
5. Abre un Pull Request

### Estándares de código

- HTML válido (W3C Validator)
- Accesibilidad WCAG 2.1 AA
- Performance: Lighthouse >85
- SEO: Meta tags completos
- Comentarios en código complejo

---

## 📄 Licencia

Este proyecto está licenciado bajo **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)**.

### ¿Qué significa?

- ✅ **Puedes:** Ver el código, aprender de él, usarlo como referencia
- ❌ **No puedes:** Usarlo comercialmente, modificarlo para redistribuir, crear derivados

Para usos comerciales o académicos, contacta: [danielorozco@twimproject.com](mailto:danielorozco@twimproject.com)

**Lectura completa:** [LICENSE](LICENSE)

---

## 📞 Contacto

<div align="center">

### Daniel Orozco Abia
**Psicólogo General Sanitario · CV11515**

[![Email](https://img.shields.io/badge/Email-danielorozco%40twimproject.com-D74A2B?style=for-the-badge&logo=gmail&logoColor=white)](mailto:danielorozco@twimproject.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Dani%20Orozco-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dani-orozco-abia-1a0a90115/)
[![Instagram](https://img.shields.io/badge/Instagram-%40daniorozcopsicologo-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/daniorozcopsicologo)
[![YouTube](https://img.shields.io/badge/YouTube-Daniel%20Orozco-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/@daniorozcopsicologo)

</div>

---

## 🌟 Agradecimientos

- A todas las personas y equipos que han confiado en el Método MindShift
- A la comunidad open-source por las herramientas utilizadas
- A los colaboradores que hacen posible este proyecto

---

<div align="center">

**[⬆ Volver arriba](#-the-world-is-mind-project)**

Hecho con 🧠 y ❤️ por [Daniel Orozco](https://twimproject.com)

© 2025 The World Is Mind Project. Todos los derechos reservados.

</div>
