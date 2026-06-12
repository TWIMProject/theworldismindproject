# Di lo que quieres decir

Herramienta web de The World Is Mind Project que ayuda a preparar una conversación importante (pareja, familia, trabajo): separa el mensaje nuclear del ruido defensivo (reproches, ataques, anticipación defensiva, mensajes escondidos) y propone una versión depurada que conserva la voz de la persona.

## Decisión de stack y justificación

**HTML/CSS/JS vanilla, sin build step**, más una **Netlify Function** como proxy de la API de Anthropic.

- El resto del sitio twimproject.com es estático sin bundler; añadir React+Vite habría introducido un paso de build en un repo que se despliega tal cual a Netlify, para una app de 5 pantallas con estado lineal. Una máquina de estados de ~400 líneas de JS plano lo cubre sin dependencias, sin tiempo de build y sin superficie extra de fallos.
- La clave de la API **no puede vivir en el navegador** (sería visible para cualquiera). Por eso el análisis pasa por `netlify/functions/traductor-interno.js`: un proxy sin estado que lee `ANTHROPIC_API_KEY` de las variables de entorno de Netlify, llama a la API y devuelve el JSON. No loguea ni almacena el texto.

## Privacidad

- Todo el estado vive en memoria de la pestaña. **No hay localStorage, ni cookies, ni base de datos, ni registro de usuarios.**
- El texto del usuario solo sale del navegador en el momento de pulsar «Analizar mi texto», con destino único la función serverless → API de Anthropic.
- Si no hay clave configurada (o la API falla), la app funciona en **modo degradado**: detección por reglas (regex en español) ejecutada íntegramente en el navegador, avisando al usuario de que el análisis es básico.

## Estructura

```
di-lo-que-quieres-decir/
├── index.html    # las 5 pantallas del recorrido
├── app.css       # paleta TWIM app + DM Serif Display / DM Sans, mobile-first
├── app.js        # máquina de estados, llamada al motor, modo degradado por reglas
└── README.md
netlify/functions/
└── traductor-interno.js   # proxy a la API de Anthropic (system prompt + JSON estricto)
```

## Instalación y desarrollo local

Requisitos: Node 20+ y la CLI de Netlify.

```bash
npm install -g netlify-cli
# desde la raíz del repo:
netlify dev
# abre http://localhost:8888/di-lo-que-quieres-decir/
```

Para probar el motor con IA en local, crea un fichero `.env` en la raíz (gitignored) o exporta la variable antes de arrancar:

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
netlify dev
```

Sin la clave, la app arranca igualmente en modo degradado.

## Configuración de la clave API (producción)

1. Netlify → Site configuration → Environment variables.
2. Añadir `ANTHROPIC_API_KEY` con la clave (scope: Functions). **Nunca en el código fuente ni en el repo.**
3. (Opcional) `TRADUCTOR_INTERNO_MODEL` para cambiar el modelo sin tocar código. Por defecto: `claude-haiku-4-5-20251001` (mejor coste/latencia para esta tarea). La constante vive en `netlify/functions/traductor-interno.js` (`MODELO_POR_DEFECTO`).
4. Redeploy para que la función recoja la variable.

## Despliegue

El repo ya despliega en Netlify (publish `.`, functions `netlify/functions` según `netlify.toml`). No hace falta nada más: al mergear a `main`, la app queda en `https://twimproject.com/di-lo-que-quieres-decir/` y la función en `/.netlify/functions/traductor-interno`.

## Motor de análisis

Una sola llamada por sesión de análisis. La función envía a la API:

- `system` (v4, 12 jun): **enfoque vínculo** — sello de la herramienta declarado por Daniel: la necesidad y la petición se formulan desde el cuidado del «nosotros» («para el vínculo que tenemos, es importante que…»), nunca señalando al otro ni desde el déficit propio; petición conjunta cuando se pueda; prohibida la acusación negada en todas sus variantes; concordancia del nosotros (la frase del vínculo en plural de principio a fin, sin recentrar el yo); una sola idea central por mensaje; mutualidad indirecta (el emisor incluido en el cuidado del vínculo). Detalle en `documentos-internos/app-dlqd-principio-vinculo.md`. Además, el motor distingue las tres capas de un volcado en crudo — meta-instrucciones a la herramienta («quiero mandárselo por WhatsApp», «sin que se sienta atacada»: requisitos a obedecer, no ruido), desahogo en tercera persona (donde está el ruido y el material real) y frases directas al destinatario. Detecta los 4 tipos de ruido (fragmentos literales para resaltarlos), reformula **construyendo solo con el material del texto** (prohibido el relleno genérico de manual), respeta el medio elegido (si es mensaje escrito, redacta el mensaje listo para enviar y nunca propone «hablarlo en persona») y genera 3 frases ancla adaptadas al objetivo y al canal. Prohibido moralizar, diagnosticar o usar tecnicismos.
- `medio` (opcional, del paso 2): «en persona», «por mensaje escrito» o «por llamada».
- `output_config.format` con JSON Schema estricto → la respuesta es siempre JSON válido con `{ruidos[], reformulacion, frases_ancla[]}`.

Diagnóstico rápido sin exponer secretos: `GET /.netlify/functions/traductor-interno?diag=1` devuelve si la clave está configurada y qué modelo se usa.

Manejo de errores: 429/5xx de la API → mensaje amable + botón «Reintentar»; fallo no reintentable o sin red → opción de «Usar análisis básico»; sin clave → modo degradado automático con aviso honesto.

Nota conocida: si el modelo devolviera un fragmento no literal (no encontrado con `indexOf` en el texto original), ese fragmento no se resalta ni se lista; el esquema y el prompt lo instruyen como literal precisamente para evitarlo.

## Criterios de aceptación (estado)

1. Flujo de 5 pasos completo sin errores de consola ✔ (sintaxis verificada con `node --check`; flujo probado en preview).
2. Con API: texto con reproches genera ≥2 tipos de ruido resaltados ✔ (el modo reglas ya detecta los 4 tipos en el caso de prueba; el modo IA es estrictamente superior).
3. La reformulación conserva la intención (caso «nunca me escuchas / móvil») ✔ vía system prompt; verificar en preview con clave configurada.
4. Sin API la app es usable y lo comunica con honestidad ✔ (aviso visible de análisis básico).
5. Sin clave en el código fuente ✔; ningún dato sale salvo la llamada a Anthropic al pulsar analizar ✔.
6. Lighthouse mobile accesibilidad >90: HTML semántico, labels en todos los campos, `aria-live` en resultados, foco gestionado entre pasos, contraste verificado sobre crema.
