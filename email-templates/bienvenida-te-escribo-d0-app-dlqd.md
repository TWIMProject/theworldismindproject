# Bienvenida «Te escribo» · D0 · con código de la app DLQD

> Pieza 3 del doc de captación del 4 jun y §3 del plan x10, redactada el 12 jun 2026 para construirla en MailerLite en cuanto Daniel autorice el conector. Es el email D0 de la automation «Bienvenida Te escribo» (disparador: alta en el grupo de newsletter). Incluye el código personal de la app vía campo personalizado `dlqd_codigo` (la función `traductor-interno` lo escribe en el perfil del suscriptor al emitirlo; si el alta llega por otra vía y el campo está vacío, el bloque del código se condiciona o se omite — decidir al construir según soporte de bloques condicionales).
>
> Reglas aplicadas: promesa pública sin cadencia (re-encuadre) · tuteo · sin emojis · sin positivismo tóxico · claridad de un vistazo · concreción.

**Asunto:** Tu código de la app (y por qué no te escribiré cada semana)

**Cuerpo:**

Hola,

soy Daniel Orozco, psicólogo. Acabas de entrar en «Te escribo», y antes de nada quiero contarte cómo funciona esto, porque no es una newsletter al uso:

no te escribiré cada semana. Te escribo cuando algo merece tu tiempo. A veces pasarán semanas en silencio; cuando llegue una carta, será porque tiene algo dentro.

**Tu código de la app: {$dlqd_codigo}**

Con él puedes usar «Di lo que quieres decir» en cualquier dispositivo: entras, pones tu email y tu código, y listo. Es la herramienta con la que preparas esa conversación que te da miedo estropear — escribes lo que te sale, sin filtro, y te devuelve el mensaje que el otro puede escuchar. Sin reproches. Cuidando lo que de verdad importa: el vínculo que tenéis.

https://twimproject.com/di-lo-que-quieres-decir/

Una cosa más, porque sé que pesa: nada de lo que escribas en la herramienta se guarda. Ni yo lo leo, ni se almacena. Lo que pones ahí desaparece cuando cierras la página.

Si la usas y te sirve, pásasela a quien la necesite. Casi todos llevamos encima una conversación pendiente.

Un abrazo,
Daniel

Daniel Orozco Abia · Psicólogo General Sanitario CV11515
The World Is Mind Project — twimproject.com

---

## Notas de construcción (para la sesión que monte la automation)

- **Disparador:** alta en grupo `Web - Newsletter Home` (185936045160793620) — o el grupo dedicado «Lead · App DLQD» si ya se ha creado y migrado el slug.
- **Requiere:** campo personalizado `dlqd_codigo` creado en MailerLite ANTES de que la función pueda escribirlo (la función ya lo intenta en mejor esfuerzo desde el 12 jun; sin campo creado, MailerLite lo ignora).
- **Idioma de la automation/email: es-ES** (arista conocida: verificar idioma en el panel; incidente del 12 jun con campaña en inglés por defecto).
- **D3 y D7** (mejor carta histórica · Cap III) quedan según el plan x10 §3 — construir después de validar el D0.
- **Activación:** si el conector no permite activar la automation, queda en borrador y Daniel la activa en el panel de escritorio (arista conocida del 15 may).
