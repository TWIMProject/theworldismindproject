#!/usr/bin/env node
// TWIM Project · hook SessionStart
// Imprime los hitos del calendario operativo con su estado de urgencia
// y los devuelve como additionalContext para que Claude los lea al iniciar sesión.
//
// Patrón Claude Code: el hook recibe JSON por stdin (no se usa aquí),
// stdout debe ser JSON con hookSpecificOutput.additionalContext para
// inyectar texto al contexto del modelo.
//
// Cross-platform · Node está garantizado allí donde corre Claude Code
// (Windows nativo, WSL, macOS, Linux). No requiere bash ni Python.

const items = [
  ["2026-05-26", "crear doc métricas Carrusel #3 a 7 días"],
  ["2026-06-03", "carta promo Directo · verificar idioma a Español en panel MailerLite antes del envío 19:00 CEST"],
  ["2026-06-08", "Directo «La voz que te juzga» 19:00 CEST vía Meet"],
  ["2026-06-15", "inicio ventana grabación «Deja de Buscarte en Otros»"],
  ["2026-07-28", "cierre ventana grabación DDBEO (tope agosto)"],
  ["2026-09-01", "apertura pre-venta dura del taller «Volver a Mí» + Meta Ads"],
  ["2026-09-30", "S1 del taller «Volver a Mí» · 20:00 CEST"],
];

const now = new Date();
const todayUTC = Date.UTC(now.getFullYear(), now.getMonth(), now.getDate());
const isoToday = new Date(todayUTC).toISOString().slice(0, 10);
const MS_PER_DAY = 86400000;

const lines = [`[recordatorio hitos calendario TWIM al ${isoToday}]`];
for (const [fecha, desc] of items) {
  const [y, m, d] = fecha.split("-").map(Number);
  const targetUTC = Date.UTC(y, m - 1, d);
  const diff = Math.round((targetUTC - todayUTC) / MS_PER_DAY);
  let estado;
  if (diff < 0)        estado = `[vencido · hace ${-diff}d]`;
  else if (diff === 0) estado = "[HOY]";
  else if (diff <= 7)  estado = `[próximo · en ${diff}d]`;
  else if (diff <= 30) estado = `[<30d · en ${diff}d]`;
  else                 estado = `[futuro · en ${diff}d]`;
  lines.push(`  ${estado} ${fecha} · ${desc}`);
}

process.stdout.write(JSON.stringify({
  hookSpecificOutput: {
    hookEventName: "SessionStart",
    additionalContext: lines.join("\n"),
  },
}));
