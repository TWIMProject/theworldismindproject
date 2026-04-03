#!/usr/bin/env python3
"""
TWIM Project <-> NotebookLM Integration
========================================
Sincroniza el contenido de TWIM Project con Google NotebookLM
para generar podcasts/audio overviews automáticos.

Uso:
    # Login inicial (abre navegador)
    notebooklm login

    # Sincronizar contenido y generar audio
    python notebooklm/sync_twim.py

    # Solo sincronizar fuentes (sin generar audio)
    python notebooklm/sync_twim.py --sync-only

    # Generar audio de un notebook existente
    python notebooklm/sync_twim.py --audio-only

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
    from notebooklm.types import AudioFormat, AudioLength
except ImportError:
    print("Error: notebooklm-py no está instalado.")
    print("Instala con: pip install 'notebooklm-py[browser]'")
    print("Luego:       playwright install chromium")
    sys.exit(1)

# --- Configuración ---

PROJECT_ROOT = Path(__file__).resolve().parent.parent
NOTEBOOK_TITLE = os.getenv("TWIM_NOTEBOOK_TITLE", "TWIM Project - Insights Psicología")
AUDIO_LANGUAGE = os.getenv("TWIM_AUDIO_LANGUAGE", "es")
AUDIO_OUTPUT_DIR = PROJECT_ROOT / "notebooklm" / "audio"

# Instrucciones para el audio generado por NotebookLM
AUDIO_INSTRUCTIONS = os.getenv("TWIM_AUDIO_INSTRUCTIONS", (
    "Genera una conversación en español entre dos presentadores sobre psicología aplicada, "
    "ansiedad laboral y bienestar emocional. El tono debe ser cercano, profesional y accesible. "
    "Usa ejemplos prácticos y referencia el trabajo de Daniel Orozco y el Método MindShift de TWIM Project."
))

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
            "GuíaPrácticaAntiBurnout.pdf",
        ],
    },
}

# URLs del sitio web para añadir como fuentes
URL_SOURCES = [
    "https://twimproject.com",
    "https://twimproject.com/insights/",
]


def collect_files() -> list[Path]:
    """Recopila todos los archivos de contenido para subir."""
    files = []
    for source_name, config in CONTENT_SOURCES.items():
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


async def find_or_create_notebook(client: NotebookLMClient) -> str:
    """Busca el notebook de TWIM o crea uno nuevo. Devuelve el notebook_id."""
    notebooks = await client.notebooks.list()
    for nb in notebooks:
        if nb.title == NOTEBOOK_TITLE:
            print(f"  Notebook encontrado: {nb.title} ({nb.id})")
            return nb.id

    print(f"  Creando notebook: {NOTEBOOK_TITLE}")
    nb = await client.notebooks.create(NOTEBOOK_TITLE)
    print(f"  Notebook creado: {nb.id}")
    return nb.id


async def get_existing_source_titles(client: NotebookLMClient, notebook_id: str) -> set[str]:
    """Obtiene los títulos de fuentes ya subidas."""
    sources = await client.sources.list(notebook_id)
    return {s.title for s in sources}


async def sync_sources(client: NotebookLMClient, notebook_id: str) -> list[str]:
    """Sincroniza archivos y URLs como fuentes en el notebook. Devuelve source_ids nuevos."""
    existing = await get_existing_source_titles(client, notebook_id)
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
        # Usar dominio como título aproximado
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


async def generate_audio(client: NotebookLMClient, notebook_id: str):
    """Genera un audio overview (podcast) del notebook."""
    print("\n🎙️  Generando audio overview...")
    print(f"  Idioma: {AUDIO_LANGUAGE}")
    print(f"  Instrucciones: {AUDIO_INSTRUCTIONS[:80]}...")

    try:
        status = await client.artifacts.generate_audio(
            notebook_id,
            language=AUDIO_LANGUAGE,
            instructions=AUDIO_INSTRUCTIONS,
        )
        print(f"  Task ID: {status.task_id}")

        # Esperar a que el audio esté listo
        print("  Esperando generación (puede tardar varios minutos)...")
        result = await client.artifacts.wait_for_completion(
            notebook_id, status.task_id, timeout=600
        )
        print(f"  ✅ Audio generado correctamente")

        # Descargar audio
        AUDIO_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = AUDIO_OUTPUT_DIR / f"twim_podcast_{timestamp}.mp4"

        saved_path = await client.artifacts.download_audio(notebook_id, str(output_path))
        print(f"  💾 Guardado en: {saved_path}")

    except Exception as e:
        print(f"  ❌ Error generando audio: {e}")
        print("  Puedes generar el audio manualmente desde notebooklm.google.com")


async def list_notebooks(client: NotebookLMClient):
    """Lista todos los notebooks existentes."""
    notebooks = await client.notebooks.list()
    if not notebooks:
        print("No hay notebooks.")
        return
    print(f"\n📓 Notebooks ({len(notebooks)}):")
    for nb in notebooks:
        print(f"  - {nb.title} ({nb.id})")


async def main():
    parser = argparse.ArgumentParser(description="TWIM Project <-> NotebookLM sync")
    parser.add_argument("--sync-only", action="store_true", help="Solo sincronizar fuentes, sin generar audio")
    parser.add_argument("--audio-only", action="store_true", help="Solo generar audio del notebook existente")
    parser.add_argument("--list", action="store_true", help="Listar notebooks existentes")
    args = parser.parse_args()

    print("=" * 50)
    print("🧠 TWIM Project <-> NotebookLM Integration")
    print("=" * 50)

    async with await NotebookLMClient.from_storage() as client:
        if args.list:
            await list_notebooks(client)
            return

        notebook_id = await find_or_create_notebook(client)

        if not args.audio_only:
            new_ids = await sync_sources(client, notebook_id)
            print(f"\n📊 Resumen: {len(new_ids)} fuentes nuevas añadidas")

        if not args.sync_only:
            await generate_audio(client, notebook_id)

    print("\n✅ Proceso completado.")
    print("   Visita https://notebooklm.google.com para ver el resultado.")


if __name__ == "__main__":
    asyncio.run(main())
