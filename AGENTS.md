# Repository Guidelines

## Project Structure & Module Organization
- `Assignment3_plan.md` and `Assignment3_memo_outline.md` track the work plan and memo blueprint. Update these first when scope or data insights shift.
- `data/` contains derived datasets: `sec/` for XBRL extracts and summaries, `external/` for trends, social listening, press-release metrics, and market stats. Keep raw downloads (HTML/PDF) in `sources/` by origin (SEC, shareholder, external).
- `notes/` holds curated text excerpts such as `research_notes.md`; cite using `(notes/<file>:line)` when referencing elsewhere.
- `scripts/` provides automation (`process_press_releases.py`, `collect_additional_data.py`). Run them from the repo root.

## Build, Test, and Development Commands
- `python scripts/process_press_releases.py` – converts Ford media HTML to text and captures raw numbers.
- `python scripts/collect_additional_data.py` – pulls Google Trends, Twitter/X, and optional YouTube metadata (activate `data-venv` first).
- `python3 -m venv data-venv; source data-venv/bin/activate` – create/enter the virtual environment with pytrends, twarc, yt-dlp installed. Use `deactivate` when finished.

## Coding Style & Naming Conventions
- Markdown: ATX headings, wrap text ~100 characters, prefer bullet lists for tasks. Use present-tense, declarative sentences.
- Filenames: descriptive PascalCase with underscores (`Ford_2024_Form_10-K.txt`, `JD_Power_2024_Brand_Loyalty.pdf`). Avoid spaces in new files.
- Python scripts follow PEP 8 indentation (4 spaces) and keep configuration constants at the top for easy edits.

## Testing Guidelines
- No automated tests exist yet. When adding analytics notebooks or scripts, include usage examples and expected outputs. Place sample data in `data/` and document manual validation steps in the README or script docstring.

## Commit & Pull Request Guidelines
- Commit messages use sentence case summarizing the change (e.g., `Add automated data pulls and digital signal summaries`). Group related files (plan + notes + data) together.
- Before committing, run `git status` and `git diff` to confirm only intended changes—especially for large PDFs or CSVs.
- Pull requests should include: purpose summary, bullet list of key updates, links to relevant sources or datasets, and confirmation that scripts/notes were refreshed. Add screenshots or snippets only if they clarify a new figure or visualization.

## Security & Configuration Tips
- Keep API keys (Twitter/X bearer tokens) inside your local environment; never commit them. `collect_additional_data.py` expects credentials configured via `twarc2 configure` inside `data-venv`.
- When downloading new data, append URLs to the appropriate README in `sources/` for traceability and cite them in `notes/research_notes.md`.
## Role-Specific Instructions
- **Data Collectors:** Run automation scripts inside `data-venv` (`python scripts/collect_additional_data.py`) and log any new sources in `sources/external/README.md` and `data/external/market_stats.csv`. Capture PDFs or text extracts for reproducibility.
- **Analysts/Writers:** Update `notes/research_notes.md` with new insights (cite line references) before editing `Assignment3_memo_outline.md` or `Assignment3_plan.md`. Ensure figures trace back to `data/`.
- **Maintainers:** Review commits for large binaries, ensure scripts remain executable (`chmod +x scripts/*.py`), and keep virtual-environment dependencies documented (`data-venv/requirements.txt` if expanded).
