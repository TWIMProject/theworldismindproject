#!/usr/bin/env python3
"""
TWIM Project <-> NotebookLM Integration
========================================
Sincroniza el contenido de TWIM Project con Google NotebookLM y genera
múltiples artefactos: podcasts, vídeos, informes, quizzes, flashcards,
infografías, presentaciones, mapas mentales y chat interactivo.

Uso:
    # Login inicial (abre navegador)
    notebooklm login

    # Sincronizar fuentes + generar TODOS los artefactos
    python notebooklm/sync_twim.py --all

    # Solo sincronizar fuentes
    python notebooklm/sync_twim.py --sync-only

    # Generar artefactos individuales
    python notebooklm/sync_twim.py --audio
    python notebooklm/sync_twim.py --video
    python notebooklm/sync_twim.py --report
    python notebooklm/sync_twim.py --quiz
    python notebooklm/sync_twim.py --flashcards
    python notebooklm/sync_twim.py --infographic
    python notebooklm/sync_twim.py --slides
    python notebooklm/sync_twim.py --mindmap

    # Combinar varios
    python notebooklm/sync_twim.py --audio --report --quiz

    # Chat interactivo con el notebook
    python notebooklm/sync_twim.py --chat "¿Qué es el Método MindShift?"

    # Investigación web automática
    python notebooklm/sync_twim.py --research "burnout laboral España 2026"

    # Listar notebooks existentes
    python notebooklm/sync_twim.py --list
"""

import asyncio
import argparse
import os
import sys
from pathlib import Path
from datetime import datetime

try:
    from notebooklm import NotebookLMClient
    from notebooklm.types import (
        AudioFormat, AudioLength,
        ReportFormat,
        QuizDifficulty,
        InfographicStyle, InfographicOrientation, InfographicDetailLevel,
        SlideFormat, SlideLength,
    )
except ImportError:
    print("Error: notebooklm-py no está instalado.")
    print("Instala con: pip install 'notebooklm-py[browser]'")
    print("Luego:       playwright install chromium")
    sys.exit(1)

# ─── Configuración ──────────────────────────────────────────────

PROJECT_ROOT = Path(__file__).resolve().parent.parent
NOTEBOOK_TITLE = os.getenv("TWIM_NOTEBOOK_TITLE", "TWIM Project - Insights Psicología")
LANGUAGE = os.getenv("TWIM_LANGUAGE", "es")
OUTPUT_DIR = PROJECT_ROOT / "notebooklm" / "output"

# Instrucciones por tipo de artefacto
INSTRUCTIONS = {
    "audio": os.getenv("TWIM_AUDIO_INSTRUCTIONS", (
        "Genera una conversación en español entre dos presentadores sobre psicología aplicada, "
        "ansiedad laboral y bienestar emocional. El tono debe ser cercano, profesional y accesible. "
        "Usa ejemplos prácticos y referencia el trabajo de Daniel Orozco y el Método MindShift de TWIM Project."
    )),
    "video": os.getenv("TWIM_VIDEO_INSTRUCTIONS", (
        "Crea un vídeo explicativo en español sobre los conceptos clave de psicología del bienestar laboral. "
        "Incluye referencias al burnout, la ansiedad productiva y el Método MindShift."
    )),
    "report": os.getenv("TWIM_REPORT_INSTRUCTIONS", (
        "Elabora un informe profesional en español que sintetice los temas principales: "
        "ansiedad laboral, burnout, dependencia emocional, autoestima y gestión emocional. "
        "Incluye recomendaciones prácticas basadas en el enfoque de TWIM Project."
    )),
    "quiz": os.getenv("TWIM_QUIZ_INSTRUCTIONS", (
        "Genera preguntas en español sobre psicología del bienestar laboral, ansiedad, burnout "
        "y los conceptos del Método MindShift. Las preguntas deben ser prácticas y reflexivas."
    )),
    "flashcards": os.getenv("TWIM_FLASHCARDS_INSTRUCTIONS", (
        "Crea tarjetas de estudio en español con conceptos clave de psicología aplicada al trabajo: "
        "burnout, ansiedad, autoestima, dependencia emocional y técnicas del Método MindShift."
    )),
    "infographic": os.getenv("TWIM_INFOGRAPHIC_INSTRUCTIONS", (
        "Diseña una infografía en español sobre el Método MindShift y las señales de burnout laboral. "
        "Incluye estadísticas y recomendaciones prácticas."
    )),
    "slides": os.getenv("TWIM_SLIDES_INSTRUCTIONS", (
        "Crea una presentación profesional en español sobre el bienestar psicológico en el trabajo, "
        "el Método MindShift y las soluciones de TWIM Project para empresas."
    )),
}

# Directorios y archivos de contenido para subir como fuentes
CONTENT_SOURCES = {
    "insights": {
        "path": PROJECT_ROOT / "insights",
        "glob": "*.html",
        "exclude": ["_template-insight.html", "index.html"],
    },
    "guides": {
        "path": PROJECT_ROOT,
        "files": [
            "BRIEFING-PROGRAMA-DEJADEBUSCARTE.md",
            "PLAN-TALLERES-ADOLESCENCIA.md",
            "GUIA-IMPLEMENTACION-SEO.md",
        ],
    },
    "pdfs": {
        "path": PROJECT_ROOT,
        "files": [
            "Grupo_Online_Info.pdf",
            "Programa_In-Company_Info.pdf",
            "guia-practica-anti-burnout.pdf",
        ],
    },
}

URL_SOURCES = [
    "https://twimproject.com",
    "https://twimproject.com/insights/",
]


# ─── Helpers ────────────────────────────────────────────────────

def timestamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def out_dir(artifact_type: str) -> Path:
    d = OUTPUT_DIR / artifact_type
    d.mkdir(parents=True, exist_ok=True)
    return d


def collect_files() -> list[Path]:
    """Recopila todos los archivos de contenido para subir."""
    files = []
    for config in CONTENT_SOURCES.values():
        base_path = config["path"]
        if "glob" in config:
            exclude = config.get("exclude", [])
            for f in sorted(base_path.glob(config["glob"])):
                if f.name not in exclude:
                    files.append(f)
        if "files" in config:
            for fname in config["files"]:
                fpath = base_path / fname
                if fpath.exists():
                    files.append(fpath)
                else:
                    print(f"  ⚠ No encontrado: {fpath}")
    return files


# ─── Notebook & Sources ────────────────────────────────────────

async def find_or_create_notebook(client: NotebookLMClient) -> str:
    """Busca el notebook de TWIM o crea uno nuevo."""
    notebooks = await client.notebooks.list()
    for nb in notebooks:
        if nb.title == NOTEBOOK_TITLE:
            print(f"  Notebook encontrado: {nb.title} ({nb.id})")
            return nb.id

    print(f"  Creando notebook: {NOTEBOOK_TITLE}")
    nb = await client.notebooks.create(NOTEBOOK_TITLE)
    print(f"  Notebook creado: {nb.id}")
    return nb.id


async def sync_sources(client: NotebookLMClient, notebook_id: str) -> list[str]:
    """Sincroniza archivos y URLs como fuentes en el notebook."""
    sources = await client.sources.list(notebook_id)
    existing = {s.title for s in sources}
    new_source_ids = []
    files = collect_files()

    print(f"\n📁 Archivos a sincronizar: {len(files)}")
    for f in files:
        title = f.stem
        if title in existing:
            print(f"  ✓ Ya existe: {title}")
            continue

        print(f"  ↑ Subiendo: {f.name} ...", end=" ", flush=True)
        try:
            source = await client.sources.add_file(notebook_id, str(f), wait=True, wait_timeout=120)
            new_source_ids.append(source.id)
            print(f"OK ({source.id})")
        except Exception as e:
            print(f"ERROR: {e}")

    print(f"\n🌐 URLs a sincronizar: {len(URL_SOURCES)}")
    for url in URL_SOURCES:
        title = url.replace("https://", "").replace("http://", "").rstrip("/")
        if title in existing:
            print(f"  ✓ Ya existe: {title}")
            continue

        print(f"  ↑ Añadiendo URL: {url} ...", end=" ", flush=True)
        try:
            source = await client.sources.add_url(notebook_id, url, wait=True, wait_timeout=120)
            new_source_ids.append(source.id)
            print(f"OK ({source.id})")
        except Exception as e:
            print(f"ERROR: {e}")

    return new_source_ids


# ─── Generadores de artefactos ─────────────────────────────────

async def generate_audio(client: NotebookLMClient, notebook_id: str):
    """Genera un podcast (audio overview) del notebook."""
    print("\n🎙️  Generando podcast...")
    status = await client.artifacts.generate_audio(
        notebook_id,
        language=LANGUAGE,
        instructions=INSTRUCTIONS["audio"],
        audio_format=AudioFormat.DEEP_DIVE,
        audio_length=AudioLength.DEFAULT,
    )
    print(f"  Task ID: {status.task_id}")
    print("  Esperando generación (puede tardar varios minutos)...")

    await client.artifacts.wait_for_completion(notebook_id, status.task_id, timeout=600)
    path = out_dir("audio") / f"twim_podcast_{timestamp()}.mp4"
    saved = await client.artifacts.download_audio(notebook_id, str(path))
    print(f"  ✅ Podcast guardado: {saved}")


async def generate_video(client: NotebookLMClient, notebook_id: str):
    """Genera un vídeo explicativo del notebook."""
    print("\n🎬 Generando vídeo...")
    status = await client.artifacts.generate_video(
        notebook_id,
        language=LANGUAGE,
        instructions=INSTRUCTIONS["video"],
    )
    print(f"  Task ID: {status.task_id}")
    print("  Esperando generación (puede tardar varios minutos)...")

    await client.artifacts.wait_for_completion(notebook_id, status.task_id, timeout=600)
    path = out_dir("video") / f"twim_video_{timestamp()}.mp4"
    saved = await client.artifacts.download_video(notebook_id, str(path))
    print(f"  ✅ Vídeo guardado: {saved}")


async def generate_report(client: NotebookLMClient, notebook_id: str):
    """Genera un informe/briefing en Markdown."""
    print("\n📄 Generando informe...")
    status = await client.artifacts.generate_report(
        notebook_id,
        report_format=ReportFormat.BRIEFING_DOC,
        language=LANGUAGE,
        extra_instructions=INSTRUCTIONS["report"],
    )
    print(f"  Task ID: {status.task_id}")
    print("  Esperando generación...")

    await client.artifacts.wait_for_completion(notebook_id, status.task_id, timeout=300)
    content = await client.artifacts.get_report_content(notebook_id)
    path = out_dir("reports") / f"twim_informe_{timestamp()}.md"
    path.write_text(content, encoding="utf-8")
    print(f"  ✅ Informe guardado: {path}")


async def generate_study_guide(client: NotebookLMClient, notebook_id: str):
    """Genera una guía de estudio."""
    print("\n📖 Generando guía de estudio...")
    status = await client.artifacts.generate_study_guide(
        notebook_id,
        language=LANGUAGE,
    )
    print(f"  Task ID: {status.task_id}")
    print("  Esperando generación...")

    await client.artifacts.wait_for_completion(notebook_id, status.task_id, timeout=300)
    content = await client.artifacts.get_report_content(notebook_id)
    path = out_dir("reports") / f"twim_guia_estudio_{timestamp()}.md"
    path.write_text(content, encoding="utf-8")
    print(f"  ✅ Guía de estudio guardada: {path}")


async def generate_quiz(client: NotebookLMClient, notebook_id: str):
    """Genera un quiz de autoevaluación."""
    print("\n❓ Generando quiz...")
    status = await client.artifacts.generate_quiz(
        notebook_id,
        instructions=INSTRUCTIONS["quiz"],
        difficulty=QuizDifficulty.MEDIUM,
    )
    print(f"  Task ID: {status.task_id}")
    print("  Esperando generación...")

    await client.artifacts.wait_for_completion(notebook_id, status.task_id, timeout=300)
    quiz_data = await client.artifacts.get_quiz_content(notebook_id)

    path = out_dir("quizzes") / f"twim_quiz_{timestamp()}.md"
    lines = ["# Quiz TWIM - Bienestar Psicológico Laboral\n"]
    questions = quiz_data.get("questions", quiz_data) if isinstance(quiz_data, dict) else quiz_data
    if isinstance(questions, list):
        for i, q in enumerate(questions, 1):
            if isinstance(q, dict):
                lines.append(f"## Pregunta {i}\n")
                lines.append(f"{q.get('question', q.get('text', str(q)))}\n")
                for opt in q.get("options", []):
                    lines.append(f"- {opt}\n")
                answer = q.get("answer", q.get("correct_answer", ""))
                if answer:
                    lines.append(f"\n**Respuesta:** {answer}\n")
                lines.append("")
    else:
        lines.append(str(questions))

    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  ✅ Quiz guardado: {path}")


async def generate_flashcards(client: NotebookLMClient, notebook_id: str):
    """Genera flashcards de conceptos clave."""
    print("\n🃏 Generando flashcards...")
    status = await client.artifacts.generate_flashcards(
        notebook_id,
        instructions=INSTRUCTIONS["flashcards"],
    )
    print(f"  Task ID: {status.task_id}")
    print("  Esperando generación...")

    await client.artifacts.wait_for_completion(notebook_id, status.task_id, timeout=300)
    cards_data = await client.artifacts.get_flashcard_content(notebook_id)

    path = out_dir("flashcards") / f"twim_flashcards_{timestamp()}.md"
    lines = ["# Flashcards TWIM - Conceptos Clave\n"]
    cards = cards_data.get("cards", cards_data) if isinstance(cards_data, dict) else cards_data
    if isinstance(cards, list):
        for i, card in enumerate(cards, 1):
            if isinstance(card, dict):
                front = card.get("front", card.get("question", card.get("term", "")))
                back = card.get("back", card.get("answer", card.get("definition", "")))
                lines.append(f"## Tarjeta {i}\n")
                lines.append(f"**Pregunta:** {front}\n")
                lines.append(f"**Respuesta:** {back}\n")
    else:
        lines.append(str(cards))

    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  ✅ Flashcards guardadas: {path}")


async def generate_infographic(client: NotebookLMClient, notebook_id: str):
    """Genera una infografía visual."""
    print("\n🖼️  Generando infografía...")
    status = await client.artifacts.generate_infographic(
        notebook_id,
        orientation=InfographicOrientation.PORTRAIT,
        detail_level=InfographicDetailLevel.DETAILED,
        style=InfographicStyle.PROFESSIONAL,
    )
    print(f"  Task ID: {status.task_id}")
    print("  Esperando generación...")

    await client.artifacts.wait_for_completion(notebook_id, status.task_id, timeout=300)
    path = out_dir("infographics") / f"twim_infografia_{timestamp()}.png"
    saved = await client.artifacts.download_infographic(notebook_id, str(path))
    print(f"  ✅ Infografía guardada: {saved}")


async def generate_slides(client: NotebookLMClient, notebook_id: str):
    """Genera una presentación de diapositivas."""
    print("\n📊 Generando presentación...")
    status = await client.artifacts.generate_slide_deck(
        notebook_id,
        slide_format=SlideFormat.DETAILED_DECK,
        slide_length=SlideLength.DEFAULT,
    )
    print(f"  Task ID: {status.task_id}")
    print("  Esperando generación...")

    await client.artifacts.wait_for_completion(notebook_id, status.task_id, timeout=300)
    path = out_dir("slides") / f"twim_presentacion_{timestamp()}.pdf"
    saved = await client.artifacts.download_slide_deck(notebook_id, str(path))
    print(f"  ✅ Presentación guardada: {saved}")


async def generate_mindmap(client: NotebookLMClient, notebook_id: str):
    """Genera un mapa mental de los conceptos."""
    print("\n🧠 Generando mapa mental...")
    result = await client.artifacts.generate_mind_map(notebook_id)
    path = out_dir("mindmaps") / f"twim_mindmap_{timestamp()}.json"

    import json
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  ✅ Mapa mental guardado: {path}")


async def generate_data_table(client: NotebookLMClient, notebook_id: str):
    """Genera una tabla de datos estructurada."""
    print("\n📋 Generando tabla de datos...")
    status = await client.artifacts.generate_data_table(
        notebook_id,
        instructions="Organiza los conceptos principales de psicología laboral con sus definiciones y técnicas asociadas.",
        language=LANGUAGE,
    )
    print(f"  Task ID: {status.task_id}")
    print("  Esperando generación...")

    await client.artifacts.wait_for_completion(notebook_id, status.task_id, timeout=300)
    table_data = await client.artifacts.get_data_table_content(notebook_id)

    path = out_dir("tables") / f"twim_tabla_{timestamp()}.md"
    lines = ["# Tabla de Datos TWIM\n"]

    if isinstance(table_data, dict):
        headers = table_data.get("headers", [])
        rows = table_data.get("rows", [])
        if headers:
            lines.append("| " + " | ".join(str(h) for h in headers) + " |")
            lines.append("| " + " | ".join("---" for _ in headers) + " |")
            for row in rows:
                cells = row if isinstance(row, list) else [row]
                lines.append("| " + " | ".join(str(c) for c in cells) + " |")
    else:
        lines.append(str(table_data))

    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  ✅ Tabla guardada: {path}")


# ─── Chat interactivo ──────────────────────────────────────────

async def chat_ask(client: NotebookLMClient, notebook_id: str, question: str):
    """Hace una pregunta al notebook y muestra la respuesta."""
    print(f"\n💬 Pregunta: {question}")
    print("  Consultando...")

    result = await client.chat.ask(notebook_id, question)
    print(f"\n  📝 Respuesta:\n")
    print(f"  {result.answer}")

    if hasattr(result, "references") and result.references:
        print(f"\n  📚 Referencias: {len(result.references)} fuentes citadas")

    return result


# ─── Investigación web ──────────────────────────────────────────

async def research_web(client: NotebookLMClient, notebook_id: str, query: str):
    """Investiga en la web e importa fuentes al notebook."""
    print(f"\n🔍 Investigando: {query}")
    task = await client.research.start(notebook_id, query, source="web", mode="deep")
    print(f"  Task iniciado, esperando resultados...")

    for _ in range(60):
        result = await client.research.poll(notebook_id)
        status = result.get("status", "")
        if status == "completed":
            sources_found = result.get("sources", [])
            summary = result.get("summary", "")
            print(f"\n  📊 Resultados: {len(sources_found)} fuentes encontradas")
            if summary:
                print(f"  📝 Resumen: {summary[:200]}...")

            if sources_found:
                to_import = sources_found[:5]
                print(f"  ↑ Importando {len(to_import)} fuentes al notebook...")
                imported = await client.research.import_sources(
                    notebook_id, task.get("task_id", ""), to_import
                )
                print(f"  ✅ {len(imported)} fuentes importadas")
            return
        elif status == "failed":
            print(f"  ❌ Investigación fallida")
            return
        await asyncio.sleep(5)

    print("  ⏰ Timeout - la investigación tardó demasiado")


# ─── Listado de notebooks ──────────────────────────────────────

async def list_notebooks(client: NotebookLMClient):
    """Lista todos los notebooks existentes con detalles."""
    notebooks = await client.notebooks.list()
    if not notebooks:
        print("No hay notebooks.")
        return
    print(f"\n📓 Notebooks ({len(notebooks)}):")
    for nb in notebooks:
        print(f"  - {nb.title} ({nb.id})")


# ─── Main ──────────────────────────────────────────────────────

async def main():
    parser = argparse.ArgumentParser(
        description="TWIM Project <-> NotebookLM: sincronización y generación de artefactos",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # Modo general
    parser.add_argument("--list", action="store_true", help="Listar notebooks existentes")
    parser.add_argument("--sync-only", action="store_true", help="Solo sincronizar fuentes")
    parser.add_argument("--all", action="store_true", help="Generar TODOS los artefactos")

    # Artefactos individuales
    gen = parser.add_argument_group("Artefactos (se pueden combinar)")
    gen.add_argument("--audio", action="store_true", help="Generar podcast (audio deep dive)")
    gen.add_argument("--video", action="store_true", help="Generar vídeo explicativo")
    gen.add_argument("--report", action="store_true", help="Generar informe/briefing")
    gen.add_argument("--study-guide", action="store_true", help="Generar guía de estudio")
    gen.add_argument("--quiz", action="store_true", help="Generar quiz de autoevaluación")
    gen.add_argument("--flashcards", action="store_true", help="Generar flashcards")
    gen.add_argument("--infographic", action="store_true", help="Generar infografía")
    gen.add_argument("--slides", action="store_true", help="Generar presentación")
    gen.add_argument("--mindmap", action="store_true", help="Generar mapa mental")
    gen.add_argument("--table", action="store_true", help="Generar tabla de datos")

    # Interactivo
    inter = parser.add_argument_group("Interactivo")
    inter.add_argument("--chat", type=str, metavar="PREGUNTA", help="Preguntar al notebook")
    inter.add_argument("--research", type=str, metavar="QUERY", help="Investigar en web e importar fuentes")

    # Opciones
    parser.add_argument("--no-sync", action="store_true", help="No sincronizar fuentes antes de generar")

    args = parser.parse_args()

    print("=" * 55)
    print("  🧠 TWIM Project <-> NotebookLM Integration")
    print("=" * 55)

    async with await NotebookLMClient.from_storage() as client:
        if args.list:
            await list_notebooks(client)
            return

        notebook_id = await find_or_create_notebook(client)

        # Sincronizar fuentes (a menos que se pida no hacerlo)
        if not args.no_sync:
            new_ids = await sync_sources(client, notebook_id)
            print(f"\n📊 Resumen: {len(new_ids)} fuentes nuevas añadidas")

        if args.sync_only:
            print("\n✅ Sincronización completada.")
            return

        # Chat interactivo
        if args.chat:
            await chat_ask(client, notebook_id, args.chat)
            return

        # Investigación web
        if args.research:
            await research_web(client, notebook_id, args.research)
            return

        # Determinar qué artefactos generar
        generators = []
        if args.all or args.audio:
            generators.append(("Podcast", generate_audio))
        if args.all or args.video:
            generators.append(("Vídeo", generate_video))
        if args.all or args.report:
            generators.append(("Informe", generate_report))
        if args.all or args.study_guide:
            generators.append(("Guía de estudio", generate_study_guide))
        if args.all or args.quiz:
            generators.append(("Quiz", generate_quiz))
        if args.all or args.flashcards:
            generators.append(("Flashcards", generate_flashcards))
        if args.all or args.infographic:
            generators.append(("Infografía", generate_infographic))
        if args.all or args.slides:
            generators.append(("Presentación", generate_slides))
        if args.all or args.mindmap:
            generators.append(("Mapa mental", generate_mindmap))
        if args.all or args.table:
            generators.append(("Tabla de datos", generate_data_table))

        # Si no se eligió nada, generar audio por defecto
        if not generators:
            generators.append(("Podcast", generate_audio))

        print(f"\n🚀 Artefactos a generar: {', '.join(name for name, _ in generators)}")

        errors = []
        for name, gen_fn in generators:
            try:
                await gen_fn(client, notebook_id)
            except Exception as e:
                print(f"  ❌ Error en {name}: {e}")
                errors.append(name)

        print(f"\n{'=' * 55}")
        total = len(generators)
        ok = total - len(errors)
        print(f"  ✅ Completado: {ok}/{total} artefactos generados")
        if errors:
            print(f"  ⚠  Errores en: {', '.join(errors)}")
        print(f"  📂 Output: {OUTPUT_DIR}")
        print(f"  🌐 https://notebooklm.google.com")


if __name__ == "__main__":
    asyncio.run(main())
