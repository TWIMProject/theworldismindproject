# App «Di lo que quieres decir» · Principio de producto: el enfoque vínculo

> Declarado por Daniel el 12 jun 2026, tras validar el motor v2 con su caso real. Cita verbatim:
>
> «Que sea desde señalar lo bueno que es para el vínculo, de pareja, de padres hijos, de trabajo, de amistad, etc. Es un: "para el vínculo que tenemos, es importante que cuando hablemos estemos realmente el uno con el otro." Ese es el enfoque que de verdad va a ayudar a los usuarios y que ninguna app tiene.»

## El principio

La reformulación que entrega la app **no se enfoca desde quien manda el mensaje** (su déficit, su necesidad insatisfecha) **ni desde la conducta del receptor** (lo que hace mal, aunque se diga con suavidad). Se enfoca desde **el vínculo como sujeto**: lo que las dos personas tienen juntas y lo que ese nosotros necesita.

- ❌ Enfoque que señala (aunque suavice): «No es que seas una mala persona, es que necesito sentirme escuchado y ahora mismo no lo siento. Lo que pido es simple: que dejes el móvil cuando empezamos a hablar.»
- ✅ Enfoque vínculo: «Para el vínculo que tenemos, es importante que cuando hablemos estemos de verdad el uno con el otro. Por eso te pido que guardemos los móviles cuando hablemos de algo que nos importa.»

## Reglas operativas (implementadas en el system prompt v3 del motor y en el modo básico)

1. La necesidad y la petición se anclan en el «nosotros», con la palabra adaptada al tipo de vínculo: «lo nuestro» / «nuestra relación» (pareja), «nuestra relación de madre e hija» (familia), «nuestro equipo» (trabajo), «nuestra amistad».
2. La emoción en primera persona **se mantiene** (es la verdad de quien habla); lo que cambia es el ancla de la petición.
3. Petición como **acción conjunta** cuando tenga sentido: «que guardemos», «que nos demos un rato» — no orden unilateral («que dejes», «que hagas»).
4. **Prohibido** el patrón «no es que seas X, es que…»: la acusación negada sigue señalando.
5. Al menos una frase ancla ancla la conversación en el vínculo: «esto no va de quién tiene razón: va de cuidar lo que tenemos».

## Por qué es el diferencial

Las herramientas de comunicación al uso (y la CNV de manual) se quedan en el «mensaje-yo»: «yo siento, yo necesito, yo pido». Es mejor que el reproche, pero sigue siendo una transacción entre dos partes enfrentadas. El enfoque vínculo introduce el tercer elemento —la relación— como lo que ambos cuidan juntos: convierte la petición en una invitación a cuidar algo compartido en vez de una demanda de uno al otro. Coherente con la línea clínica de TWIM (hablar de un nosotros, no culpar al otro de las cosas de la relación).

Implementación: `netlify/functions/traductor-interno.js` (SYSTEM_PROMPT, sección REFORMULAR · «ENFOQUE VÍNCULO») y `di-lo-que-quieres-decir/app.js` (plantillas del modo básico).
