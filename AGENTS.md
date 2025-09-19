# Repository Guidelines

## Project Structure & Module Organization
- `Assignment3_plan.md` – task roadmap with open action items and status checkboxes.
- `Assignment3_memo_outline.md` – narrative flow for the executive memo and slide deck.
- `notes/` – plain-text extracts from filings and media sources; filenames use `Pascal_Case` and include the source (e.g., `Ford_2024_Form_10-K.txt`).
- `sources/` – canonical reference material grouped into `SEC/`, `shareholder/`, and `external/`; keep PDFs under 50 MB when possible.
- `AGENTS.md` (this file) and `README.md` – contributor guidance and quick orientation.

## Build, Test, and Development Commands
This project is research-focused; no build pipeline exists. Use standard shell utilities for maintenance:
- `git status` – review pending changes before staging.
- `textutil`/`pdftotext` – convert new documents into searchable text for the `notes/` directory.

## Coding Style & Naming Conventions
- Markdown files: wrap lines at ~100 characters, use ATX headings, and prefer bullet lists for task tracking.
- Text extracts: retain original capitalization; add citation markers `(notes/...:line)` when referencing in other docs.
- File naming: use descriptive titles with spaces replaced by underscores (e.g., `Introducing_Ready_Set_Ford.pdf`).

## Testing Guidelines
No automated tests are defined. When adding analysis scripts later, include runnable examples (`python script.py`) and sample output in a `tests/` or `examples/` section.

## Commit & Pull Request Guidelines
- Follow the existing “sentence case” commit pattern (`Initial research materials`). Keep commits scoped to one logical change (e.g., “Add Ready Set Ford article summary”).
- Before committing, run `git diff` to verify only intentional files are touched, especially large PDFs.
- Pull requests should include: purpose summary, bullet list of key changes, reference to relevant notes, and confirmation that sources were added under the correct subfolder.

## Security & Configuration Tips
- Do not commit personal API keys or credentials. Use `.env` files ignored by Git if scripts are added.
- Enable Git LFS before pushing assets larger than 50 MB.
