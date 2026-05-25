# Stripe · Copy editorial + portadas · 25 may 2026

> Documento operativo único para que Daniel pegue copy y suba portadas en el dashboard de Stripe. Cubre los 5 productos activos del catálogo + el setup del nuevo producto **Volver a Mí** (que sigue siendo PRODUCTO 1 + PRODUCTO 2 en `taller-volver-a-mi/stripe-setup-volver-a-mi.md`).
>
> Voz editorial · descriptiva, anti-positivismo, tuteo, sin slogans, info clínica concreta. Coherente con la regla inviolable de naming Stripe persistida en CLAUDE.md (separador `·`, comillas `«»`).

---

## 0 · Portadas generadas

5 imágenes 1080×1080 con paleta TWIM (fondo `#173D30`, beige `#C2A78B`, crema/blanco) generadas con `documentos-internos/plantillas/generar-portadas-stripe.py`. URLs públicas tras deploy:

| Producto | Archivo | URL pública (post-deploy) |
|---|---|---|
| Reserva Bachillerato | `assets/stripe-portadas/01-reserva-bachillerato.png` | `https://twimproject.com/assets/stripe-portadas/01-reserva-bachillerato.png` |
| Reserva TDAH | `assets/stripe-portadas/02-reserva-tdah.png` | `https://twimproject.com/assets/stripe-portadas/02-reserva-tdah.png` |
| Taller Bachillerato | `assets/stripe-portadas/03-taller-bachillerato.png` | `https://twimproject.com/assets/stripe-portadas/03-taller-bachillerato.png` |
| Taller TDAH | `assets/stripe-portadas/04-taller-tdah.png` | `https://twimproject.com/assets/stripe-portadas/04-taller-tdah.png` |
| Programa In-Company | `assets/stripe-portadas/05-programa-in-company.png` | `https://twimproject.com/assets/stripe-portadas/05-programa-in-company.png` |

**Cómo subirlas a Stripe:** dashboard → producto → `Más información` o sección «Imagen del producto» → `Cargar imagen` → seleccionar el archivo de tu disco (lo descargas del repo o del PR mergeado).

---

## 1 · Reserva · Entrevista informativa · Taller Bachillerato (40 €)

### Renombrar nombre

```
Reserva · Entrevista informativa · Taller Bachillerato
```

### Descripción (pegar verbatim)

```
Reserva de la entrevista informativa previa al «Taller Bachillerato · Encontrar el rumbo» — 90 min en directo con Daniel Orozco Abia (Psicólogo General Sanitario CV11515), presencial en Valencia o por videollamada.

La entrevista es gratuita en concepto. Si te presentas, la reserva se devuelve íntegra. Si no te presentas, no es reembolsable — compensa el tiempo bloqueado.

Pensada para padres con hijos en Bachillerato que no saben qué van a estudiar, han bajado el rendimiento sin explicación o están bloqueados en una decisión que se les ha vuelto demasiado grande. No es coaching ni sesiones motivacionales: es escucha clínica del momento concreto de tu hijo o hija.

Si tras la entrevista decides inscribirlo, el taller (720 €) se cobra aparte.
```

### Portada

`https://twimproject.com/assets/stripe-portadas/01-reserva-bachillerato.png`

---

## 2 · Reserva · Entrevista informativa · Taller TDAH adolescentes (40 €)

### Renombrar nombre

```
Reserva · Entrevista informativa · Taller TDAH adolescentes
```

### Descripción (pegar verbatim)

```
Reserva de la entrevista informativa previa al «Taller TDAH adolescentes · Más allá del TDAH» — 90 min en directo con Daniel Orozco Abia (Psicólogo General Sanitario CV11515), presencial en Valencia o por videollamada.

La entrevista es gratuita en concepto. Si te presentas, la reserva se devuelve íntegra. Si no te presentas, no es reembolsable — compensa el tiempo bloqueado.

Pensada para padres con hijos diagnosticados (o sospecha) de TDAH en 3º o 4º de ESO. Hablamos del momento concreto de tu hijo o hija, qué se confunde con el diagnóstico, qué se queda fuera del informe y qué necesita en esta etapa. No es psicoeducación genérica: es lectura clínica caso a caso.

Si tras la entrevista decides inscribirlo, el taller (720 €) se cobra aparte.
```

### Portada

`https://twimproject.com/assets/stripe-portadas/02-reserva-tdah.png`

---

## 3 · Taller Bachillerato · Encontrar el rumbo (720 €)

### Renombrar nombre

```
Taller Bachillerato · Encontrar el rumbo
```

### Descripción (pegar verbatim)

```
Taller presencial en Valencia para adolescentes de Bachillerato. 16 sesiones, grupo cerrado de 6. Inicio: segunda quincena de septiembre de 2026.

Para hijos que llegan a este momento sin saber qué quieren, con rendimiento que baja sin explicación clara, o atascados en una decisión académica que se les ha vuelto demasiado grande. No es orientación vocacional ni clase de hábitos de estudio: es trabajo clínico semanal sobre el momento concreto en el que están, en compañía de otros adolescentes que también están ahí.

El taller incluye la guía «Padres Bachillerato» en PDF y una sesión de cierre con padres al final del proceso. La entrevista informativa previa (40 €, reembolsable si te presentas) es obligatoria para confirmar encaje antes de inscribir.

Conducido por Daniel Orozco Abia, Psicólogo General Sanitario CV11515 — formación psicoanalítica aplicada, sin coaching motivacional, sin slogans.
```

### Portada

`https://twimproject.com/assets/stripe-portadas/03-taller-bachillerato.png`

---

## 4 · Taller TDAH adolescentes · Más allá del TDAH (720 €)

### Renombrar nombre

```
Taller TDAH adolescentes · Más allá del TDAH
```

### Descripción (pegar verbatim)

```
Taller presencial en Valencia para adolescentes de 3º y 4º de ESO con diagnóstico (o sospecha) de TDAH. 16 sesiones, grupo cerrado de 6. Inicio: segunda quincena de septiembre de 2026.

El diagnóstico nombra parte del cuadro y deja parte fuera. Este taller trabaja lo que se queda fuera del informe — el cómo se ha colocado tu hijo o hija frente al diagnóstico, lo que se confunde con el TDAH y lo que está mezclado debajo. No es psicoeducación genérica ni reentrenamiento atencional: es trabajo clínico semanal en grupo, con otros adolescentes que también están en este punto.

El taller incluye la guía «Padres TDAH ESO» en PDF y una sesión de cierre con padres al final del proceso. La entrevista informativa previa (40 €, reembolsable si te presentas) es obligatoria para confirmar encaje antes de inscribir.

Conducido por Daniel Orozco Abia, Psicólogo General Sanitario CV11515 — formación psicoanalítica aplicada, sin coaching motivacional, sin slogans.
```

### Portada

`https://twimproject.com/assets/stripe-portadas/04-taller-tdah.png`

---

## 5 · Programa In-Company · Ansiedad Laboral · Ventaja Competitiva (2.450 €)

### Renombrar nombre

```
Programa In-Company · Ansiedad Laboral · Ventaja Competitiva
```

### Descripción (pegar verbatim)

```
Programa formativo para equipos y organizaciones. 6 sesiones de 90 min, modalidad presencial u online. Marco psicoanalítico aplicado a las dinámicas reales del equipo — sin coaching motivacional, sin slogans corporativos, sin ejercicios de team building.

Pensado para empresas que detectan ansiedad laboral creciente, autoexigencia tóxica difusa o conflictos que se reproducen sin explicación aparente. Trabajamos lo que el equipo aguanta sin decir, los pactos no escritos que sostienen la tensión y las dinámicas que cuestan productividad sin que se vean en ningún KPI.

El programa se adapta al tamaño y al sector de la empresa. Incluye sesión inicial de diagnóstico con dirección + RRHH, las 6 sesiones formativas con el equipo y un informe de cierre con observaciones y recomendaciones.

Conducido por Daniel Orozco Abia, Psicólogo General Sanitario CV11515. Contacto previo obligatorio en `equipo@theworldismindproject.com` para encajar fechas y alcance antes de comprar.
```

### Portada

`https://twimproject.com/assets/stripe-portadas/05-programa-in-company.png`

---

## 6 · Volver a Mí · 2 productos (pendiente de crear)

Setup completo paso a paso ya documentado en `documentos-internos/taller-volver-a-mi/stripe-setup-volver-a-mi.md`. Resumen:

### 6.1 · Reserva · Volver a Mí · Grupo cerrado otoño 2026 (100 €)

**Descripción editorial (verbatim, lista para pegar):**

```
Reserva de plaza en «Volver a Mí», grupo cerrado de 8 personas conducido por Daniel Orozco Abia (Psicólogo General Sanitario CV11515). 8 sesiones online semanales de 90 min — miércoles de 20:00 a 21:30 hora Madrid, del 30 sept al 18 nov de 2026.

La reserva incluye una sesión individual previa de 30 min con Daniel. Su función es confirmar el encaje mutuo antes de entrar al grupo: si Daniel acepta y tú también, se cobra el resto del taller (597 €) y se confirma la plaza. Si Daniel no acepta el encaje o tú decides no continuar, la reserva se devuelve íntegra. Si no te presentas a la sesión individual, la reserva no se devuelve.

Para mujeres adultas que llevan años sosteniéndose en la mirada del otro y quieren empezar a hacerlo en otra parte. No es coaching ni grupo de apoyo: es trabajo clínico semanal en grupo cerrado, con marco psicoanalítico aplicado.
```

**Portada:** generar cuando esté lista la identidad visual del taller (pendiente). Mientras tanto, se puede usar `logo-mindworld.png` o subir la portada Reserva genérica como placeholder.

### 6.2 · Resto · Volver a Mí · Grupo cerrado otoño 2026 (597 €)

**Descripción editorial (verbatim):**

```
Pago del resto del taller «Volver a Mí» (597 €). Este enlace se envía privadamente tras la sesión individual previa, una vez confirmado el encaje mutuo.

Cubre las 8 sesiones grupales online de 90 min (miércoles 20:00 a 21:30 hora Madrid, del 30 sept al 18 nov de 2026), el material PDF complementario y el acceso a la comunidad cerrada del grupo durante el proceso. La reserva previa de 100 € ya está cobrada por separado.

Política de cancelación: refund total hasta 7 días antes de la S1. Refund 50 % entre 7 días antes y la S1. Sin refund una vez iniciado el taller.

Daniel Orozco Abia, Psicólogo General Sanitario CV11515.
```

---

## 7 · Checklist final para Daniel (después de subir todo)

- [ ] 4 productos activos renombrados según naming TWIM (separador `·`, comillas `«»`)
- [ ] 5 portadas subidas a Stripe (1 por producto)
- [ ] 5 descripciones editoriales pegadas en su producto correspondiente
- [ ] Categorías consolidadas:
  - Reservas + Talleres adolescentes → `Talleres en vivo`
  - In-Company → `Servicios profesionales`
- [ ] Metadata obligatoria añadida en cada producto:
  - `taller_id` (ej. `bachillerato-2026`, `tdah-2026`, `in-company`)
  - `edicion` (ej. `septiembre-2026`)
  - `funcion` (`reserva`, `taller`, `programa`)
- [ ] Productos de «Volver a Mí» creados antes del 31 jul 2026 (Reserva 100 € + Resto 597 €)

---

**Última actualización:** 25 may 2026 · Claude (sesión `claude/social-media-link-naming-tcIUA`).
