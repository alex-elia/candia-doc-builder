# Satellite Presentation & Demo Builder

Tools for generating presentations, demo videos, and shareable assets for the **Embedded AI for Satellites** initiative.

## What's inside

- **Presentation generators** powered by `python-pptx`
- **Video & screen recording helpers** for demo capture
- **Pitch automation scripts** (PowerShell + Bash)
- **Templates & sample assets** (`Templates/`, `images/`, `examples`)

## Quick start

```bash
python -m venv .venv
. .venv/bin/activate  # Windows PowerShell: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Generate the premium Thales deck
python generate_thales_presentation.py
```

The scripts assume the current working directory is the repository root so that relative paths to `Templates/` and `images/` resolve automatically.

## Repository layout

```
candia-doc-builder/
 README.md
 requirements.txt
 *.py / *.ps1 / *.sh          # automation scripts
 Templates/                   # base PowerPoint templates
 images/                      # sample imagery used in decks
 docs & guides                # how-to content (see *.md files)
```

## Common scripts

| Script | Purpose |
| --- | --- |
| `generate_thales_presentation.py` | Build the default Thales Alenia deck |
| `generate_with_template_correct.py` | Use a provided PPTX template with placeholders |
| `generate_demo_video.py` | Storyboard a narrated video from demo steps |
| `automated_screen_recording.py` | Automate capture of a scripted run |
| `build_pitch.sh / .ps1` | Compile the LaTeX pitch into PDF |

Each script contains inline options for tailoring content (titles, metrics, imagery). When sharing outputs publicly, edit the contact details at the bottom of each deck.

## Requirements

- Python 3.11+
- LaTeX toolchain (for `build_pitch.*` scripts, e.g., TeX Live or MikTeX)
- FFMPEG (optional) for video helpers

Install Python dependencies via `requirements.txt`. Templates reference fonts commonly available on Windows/macOS; adjust the styles if you're on Linux.

## Sanitizing before publishing

- Replace personal contact information in slide generators before sharing
- Store API keys (e.g., search/video services) in environment variables
- Use royalty-free or public-domain imagery in `images/`

## Roadmap ideas

- Package modules under a `doc_builder` namespace with CLI entrypoints
- Ship containerized workflows for reproducible decks
- Add CI to lint scripts and validate template integrity

---

Maintained alongside the `satellite-ai-prototype` demo. Fork and adapt to your own embedded-AI storytelling needs.
