# Repository Guidelines

## Project Structure & Module Organization
- `Assignment3_plan.md` and `Assignment3_memo_outline.md` hold the living work plan and memo blueprint. Update these first when scope or narrative shifts.
- `notes/` contains text extracts and research syntheses. Keep filenames descriptive (`Source_Topic.txt`) and cite line numbers when referencing elsewhere.
- `sources/` stores reference materials grouped by origin (`SEC/`, `shareholder/`, `external/`). Add URLs to the nested README each time a new document is saved.
- Class slides and proprietary course content remain outside the repo (`class notes/`). Reference insights in `notes/research_notes.md` without copying the files in.

## Build, Test, and Development Commands
- This project is primarily research and documentation. Standard git hygiene applies: `git status`, `git diff`, `git add`, `git commit`.
- Use `pdftotext <file.pdf> <out.txt>` or similar tooling to generate searchable extracts before summarizing in `notes/`.

## Coding Style & Naming Conventions
- Markdown: use ATX headings, wrap text near 100 characters, prefer bullet lists for action items. Insert inline citations with `(notes/<file>:line)`.
- Filenames: PascalCase words joined by underscores (`Ford_2024_Form_10-K.txt`). Avoid spaces.
- When embedding code snippets (rare), default to fenced blocks and two-space indentation.

## Testing Guidelines
- No automated tests are defined. If analysis scripts are introduced, include self-contained usage examples under a `tests/` or `examples/` directory and document expected outputs.

## Commit & Pull Request Guidelines
- Follow the existing sentence-case commit style (`Add industry intelligence sources and integrate insights`). Group related edits together and avoid mixing large binary updates with textual changes.
- Run `git status` and `git diff` before committing to ensure only intentional files are staged, especially large PDFs.
- Pull requests (if used) should summarize the objective, list key updates, link to relevant notes or sources, and mention any new documents placed under `sources/`.

## Security & Data Handling
- Do not commit sensitive course materials, personal data, or credentials. Keep class PDFs in `class notes/` (ignored by Git) and reference insights via summaries only.
- For files larger than 50 MB, enable Git LFS or share via alternative storage; GitHub warns on push for oversize assets.
