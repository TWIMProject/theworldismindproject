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
//
// Mantenimiento 10-jun-2026 (sesión claude/practical-hypatia-3dmulg):
// retirados 3 hitos cumplidos/obsoletos (métricas Carrusel #3 · doc existe
// desde el 19-27 may; idioma carta promo · hecho 3 jun; Directo 7 jun ·
// reprogramado al 14 jun 21:30). Añadidos hitos del Directo 14 jun,
// revisión CPL Google Ads y agosto sagrado (analisis-foco-x2 §3).

const items = [
  ["2026-06-13", "E2 víspera Directo sale 19:00 CEST automático (MailerLite, programada 10 jun) · solo verificar"],
  ["2026-06-14", "Directo «La voz que te juzga» 21:30 CEST vía Meet · E4 «en 1 hora» sale 20:30 automático · después: programar E5 con URL de grabación"],
  ["2026-06-15", "inicio ventana grabación «Deja de Buscarte en Otros» · regla foco: nada más se graba hasta el 28 jul"],
  ["2026-06-23", "revisar CPL campaña Google Ads (lanzada 9 jun) · objetivo ≤15-20 € · si convierte, ampliar ad groups"],
  ["2026-07-28", "cierre ventana grabación DDBEO (tope agosto)"],
  ["2026-08-03", "agosto sagrado (vacaciones) · única tarea Daniel: grabar 30-60 min de voz fuente (1 día) · audiolibro y tapas a oct-nov"],
  ["2026-09-01", "apertura pre-venta dura del taller «Volver a Mí» + Meta Ads · único lanzamiento de septiembre (libro sale sin campaña)"],
  ["2026-09-30", "S1 del taller «Volver a Mí» · 20:00 CEST"],
];

const now = new Date();
const todayUTC = Date.UTC(now.getFullYear(), now.getMonth(), now.getDate());
const isoToday = new Date(todayUTC).toISOString().slice(0, 10);
const MS_PER_DAY = 86400000;

// Hito recurrente (idea #7, aprobada por Daniel el 10-jun-2026):
// cada lunes · dashboard semanal de métricas para Daniel + triaje de inbox.
// Se calcula el próximo lunes (o hoy si es lunes) y se inyecta como hito.
const dow = new Date(todayUTC).getUTCDay(); // 0=domingo · 1=lunes
const daysToMonday = (8 - dow) % 7; // 0 si hoy es lunes
const mondayISO = new Date(todayUTC + daysToMonday * MS_PER_DAY).toISOString().slice(0, 10);
items.push([mondayISO, "LUNES · generar dashboard semanal TWIM (panel HTML, regla §5) + triaje inbox con borradores Gmail y enviarlo a Daniel con el enlace · idea #7 · si la sesión arranca en lunes, hacerlo SIN esperar instrucción"]);
items.sort((a, b) => a[0].localeCompare(b[0]));

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
