# App «Di lo que quieres decir» · Principio de producto: el enfoque vínculo

> Declarado por Daniel el 12 jun 2026, tras validar el motor v2 con su caso real. Cita verbatim:
>
> «Que sea desde señalar lo bueno que es para el vínculo, de pareja, de padres hijos, de trabajo, de amistad, etc. Es un: "para el vínculo que tenemos, es importante que cuando hablemos estemos realmente el uno con el otro." Ese es el enfoque que de verdad va a ayudar a los usuarios y que ninguna app tiene.»

## El principio

La reformulación que entrega la app **no se enfoca desde quien manda el mensaje** (su déficit, su necesidad insatisfecha) **ni desde la conducta del receptor** (lo que hace mal, aunque se diga con suavidad). Se enfoca desde **el vínculo como sujeto**: lo que las dos personas tienen juntas y lo que ese nosotros necesita.

- ❌ Enfoque que señala (aunque suavice): «No es que seas una mala persona, es que necesito sentirme escuchado y ahora mismo no lo siento. Lo que pido es simple: que dejes el móvil cuando empezamos a hablar.»
- ✅ Enfoque vínculo: «Para el vínculo que tenemos, es importante que cuando hablemos estemos de verdad el uno con el otro. Por eso te pido que guardemos los móviles cuando hablemos de algo que nos importa.»

## Declaración ampliada (12 jun 2026, segunda iteración, verbatim)

> «Lo que buscamos con esta App es lo que el ser humano necesita, construir mensajes que ayuden a hacer entender a un otro, lo que de verdad importa en los vínculos en las relaciones sociales, transmitir sin atacar, transmitir cuidando lo más importante para las personas, el vínculo que les une, centrar lo importante del mensaje para no irse por las ramas, que eso es lo que sucede si les damos mensajes donde se señalen errores directamente a la persona. Para que las conversaciones no se dispersen o acaben peor de lo que empiezan es importante en los vínculos sociales que no se desvíe la atención de los participantes a algo que no sea lo que la persona quiere señalar del otro y también es importante mejorar la comunicación hablando de un nosotros; al usuario que use nuestra app le hagamos ver indirectamente que él también suele ser ese otro que descuida el vínculo o puede llegar a hacerlo, sea en vínculos de amistad, de pareja, de trabajo, de parentalidad.»

## Reglas operativas (implementadas en el system prompt v4 del motor y en el modo básico)

1. La necesidad y la petición se anclan en el «nosotros», con la palabra adaptada al tipo de vínculo: «lo nuestro» / «nuestra relación» (pareja), «nuestra relación de madre e hija» (familia), «nuestro equipo» (trabajo), «nuestra amistad».
2. La emoción en primera persona **se mantiene** (es la verdad de quien habla); lo que cambia es el ancla de la petición.
3. Petición como **acción conjunta** cuando tenga sentido: «que guardemos», «que nos demos un rato» — no orden unilateral («que dejes», «que hagas»).
4. **Prohibida la acusación negada en todas sus variantes**: «no es que seas X, es que…», «no es que no te importe…», «no digo que tú…». Nombrar la acusación negándola sigue señalando.
5. **Concordancia del nosotros** (detectado por Daniel en la prueba del 12 jun): la frase anclada en el vínculo se mantiene en plural de principio a fin. Errores reales del motor que motivaron la regla: «para que de verdad nos entienda» (debe ser «nos entendamos») y «para el vínculo que tenemos, esto es importante para mí» (recentra el yo; debe ser «para el vínculo que tenemos, esto importa»). La primera persona va en su propia frase, nunca incrustada en la frase del nosotros.
6. **Una idea central**: el mensaje se centra en la única cosa que la persona quiere señalar y en lo que pide. Cada reproche o ejemplo secundario extra es una puerta a que la conversación se disperse y acabe peor de lo que empezó.
7. **Mutualidad indirecta**: el mensaje incluye a quien lo envía en el cuidado del vínculo (peticiones en plural, «los dos» cuando fluya). El usuario también es a veces ese otro que descuida el vínculo; el mensaje lo asume **sin decírselo y sin sermonear**.
8. Al menos una frase ancla ancla la conversación en el vínculo: «esto no va de quién tiene razón: va de cuidar lo que tenemos».

## Por qué es el diferencial

Las herramientas de comunicación al uso (y la CNV de manual) se quedan en el «mensaje-yo»: «yo siento, yo necesito, yo pido». Es mejor que el reproche, pero sigue siendo una transacción entre dos partes enfrentadas. El enfoque vínculo introduce el tercer elemento —la relación— como lo que ambos cuidan juntos: convierte la petición en una invitación a cuidar algo compartido en vez de una demanda de uno al otro. Coherente con la línea clínica de TWIM (hablar de un nosotros, no culpar al otro de las cosas de la relación).

Implementación: `netlify/functions/traductor-interno.js` (SYSTEM_PROMPT, sección REFORMULAR · «ENFOQUE VÍNCULO») y `di-lo-que-quieres-decir/app.js` (plantillas del modo básico).
