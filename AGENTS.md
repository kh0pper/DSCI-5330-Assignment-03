# Repository Guidelines

## Project Structure & Module Organization
- Operate from `DSCI-5330-Assignment-03/`. Insights live in `notes/`, memo drafts in `memo/`, slide Markdown and imagery in `deck/`, and derived datasets in `data/` (`external/` for Google Trends/social/press metrics; `sec/` for XBRL extracts). Raw source files remain organized in `sources/` by origin.
- Automation scripts reside in `scripts/` and expect to run from the repo root. Common sequence: `python scripts/collect_additional_data.py`, `python scripts/summarize_youtube_metadata.py`, `python scripts/extract_market_stats.py`.

## Build, Test, and Development Commands
- Activate tooling: `source data-venv/bin/activate`.
- Refresh external data: `python scripts/collect_additional_data.py` (pulls Google Trends, Twitter/X, YouTube), followed by `python scripts/summarize_youtube_metadata.py` and `python scripts/extract_market_stats.py`.
- Regenerate deliverables: `pandoc --resource-path=deck deck/*.md -o deck/Ready_Set_Ford_deck.pptx`; export memo with `pandoc memo/memo_draft.md -o memo/memo_draft.docx`.

## Coding Style & Naming Conventions
- Python follows PEP 8 (4-space indentation). Markdown uses ATX headings with prose wrapped near 100 characters. Inline citations follow `(notes/<file>:line)`.
- Use descriptive snake_case or PascalCase filenames (e.g., `historic_campaigns.csv`, `slide_digital_pulse_trends.md`). Update Markdown before committing generated binaries.

## Testing Guidelines
- Manual validation only: inspect CSV diffs after script runs, confirm row counts, and review `notes/youtube_snapshot.md` plus visuals in `deck/visuals/`.
- Record ad hoc verification steps in script docstrings or `notes/research_notes.md` to maintain traceability.

## Commit & Pull Request Guidelines
- Commit messages use sentence case summarizing intent (“Add historic campaign benchmarks”). Group related changes (scripts + data + docs).
- Run `git status -sb` and `git diff` before committing to avoid unintended files or large binaries. PRs should state purpose, highlight key files, describe verification steps, and cite new data sources; include screenshots for slide/visual updates when helpful.

## Security & Configuration Tips
- Do not commit credentials. Configure Twitter/X access via `twarc2 configure` inside `data-venv`.
- Log new download URLs or derived datasets in the relevant README under `sources/` or `data/`.

## Role Notes
- **Project Coordinator:** Maintain `Assignment3_plan.md`, track QA checklist, ensure deliverable owners.
- **Data Collectors:** Run refresh scripts, archive raw inputs, update `data/external/` notes and READMEs.
- **Analysts/Writers:** Feed insights into `notes/research_notes.md`, align memo/deck copy, and leverage `data/external/historic_campaigns.csv` for historical comparisons.
- **Data Visualizers & Deck Steward:** Produce visuals, embed them in slide Markdown, and regenerate the PPTX via `pandoc` after content updates.
