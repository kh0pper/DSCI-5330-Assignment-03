# Assignment 3 – Marketing Analysis Plan

## Deliverables
- Executive memo (8–10 pages, 1.5 spacing) synthesizing Ford’s marketing strategy, campaign assessment, marketing intelligence recommendations, and BI roadmap.
- Presentation deck (~12 slides) highlighting key findings, data visuals, and decision-ready recommendations.

## Research Assets On Hand
- 2024 Form 10-K (Ford) – `sources/SEC/Ford_2024_Form_10-K.pdf`
- 2024 Annual Report – `sources/shareholder/Ford_2024_Annual_Report.pdf`
- 2025 DEF 14A – `sources/shareholder/Ford_2025_DEF14A.html`
- External campaign coverage (USA Today, Ford newsroom, Detroit News) – see `sources/external/README.md`
- Class readings: “Marketing Intelligence” (Harvard), Session 6 decks on marketing strategy/intelligence (kept outside repo)
- Transcribed notes and analysis log (`notes/` directory)

## Analysis Workstreams
1. **Marketing Strategy Baseline**
   - Reaffirm Ford+ positioning, segment responsibilities, and Ready Set Ford objectives.
   - Document marketing intelligence frameworks from class materials to anchor analysis (problem definition → research design → data synthesis).
2. **Performance Diagnostics**
   - Compare 2023 vs 2024 segment metrics, highlighting volume/margin shifts and marketing implications.
   - Assess incentives, pricing, and product mix effectiveness using 10-K causal factor disclosures.
3. **Marketing Intelligence Assessment**
   - Map available secondary data (SEC filings, syndicated sources) vs primary data gaps (customer perception, campaign resonance).
   - Identify potential research techniques (conjoint, perceptual mapping, qualitative exploration) informed by class readings.
4. **Business Intelligence & Data Integration**
   - Inventory Ford’s digital data streams (Ford Pro telematics, FordPass, EV telemetry) and align with intelligence needs.
   - Define KPIs for Build/Thrill/Adventure lifestyle pillars and propose dashboards.
5. **Recommendations & Storytelling**
   - Memo structure: Executive Summary, Strategic Context, Marketing Intelligence Assessment, Segment Diagnostics, BI Opportunities, Action Plan, Appendix.
   - Slides: emphasize lifestyle storytelling, intelligence roadmap, quick wins/long-term roadmap.

## Immediate Next Actions (Week of 22 Sep 2025)
- [x] Extract key frameworks/examples from class notes into `notes/research_notes.md` (Marketing Intelligence section).
- [x] Deepen secondary research on marketing intelligence applications in automotive (e.g., competitor case studies, syndicated data references).
- [x] Outline primary research recommendations (qual vs quant) to validate Ready Set Ford positioning. **Owner:** Analysts/Writers. **Artifacts:** `memo/memo_draft_sections.md`, `notes/research_notes.md`. **Due:** 23 Sep.
- [x] Begin drafting memo sections with new structure; expand slide outline accordingly. **Owner:** Analysts/Writers with Deck Steward. **Artifacts:** `memo/memo_draft.md`, `deck/deck_outline.md`. **Due:** 24 Sep.
- [x] Build campaign visuals (financial trends, Google Trends, social listening highlights) for slide deck. **Owner:** Data Visualizers. **Artifacts:** `deck/visuals/`, `deck/slide_ready_set_ford_*`. **Due:** 24 Sep.

### Agent Kickoff Checklist
- **Project Coordinator:**
  - Schedule daily 15-minute async stand-up in `Assignment3_plan.md` with status updates beginning 22 Sep.
  - Confirm each owner acknowledges deliverables; log dependencies or blockers in the plan file.
  - **Status 22 Sep:** Stand-up posted below; Analysts/Writers, Data Visualizers, Data Collectors acknowledged deliverables via plan updates.
- **Data Collectors:**
  - Refresh datasets by running `python scripts/collect_additional_data.py`, `python scripts/summarize_youtube_metadata.py`, and `python scripts/extract_market_stats.py` from repo root (activate `data-venv` first). Record notable diffs in `notes/research_notes.md`.
  - Update `data/external/market_stats.csv` snapshot notes if row counts or sources change; capture any new URLs in `sources/external/README.md`.
  - **Status 22 Sep:** Scripts executed; see `notes/research_notes.md` for refresh log.
- **Analysts/Writers:**
  - Draft Ready Set Ford primary research roadmap (qual + quant) and plug into memo Section 3. Work off existing outline, cite sources `(notes/<file>:line)` style.
  - Begin Executive Summary and Strategic Context paragraphs in `memo/memo_draft.md`, aligning KPIs with loyalty + campaign narratives.
  - **Status 22 Sep:** Roadmap drafted in `memo/memo_draft_sections.md`; Sections 4–6 refreshed with digital pulse citations.
- **Data Visualizers:**
  - Prototype refreshed Google Trends and social listening visuals; store outputs in `deck/visuals/` with rendering notes.
  - Coordinate with Deck Steward on layout needs; ensure scripts or notebooks have usage comments.
  - **Status 22 Sep:** Google Trends, hashtag bar chart, and financial trend visuals exported (`deck/visuals/`).
- **Deck Steward Agent:**
  - Integrate new visuals and research bullets into slide Markdown modules; update `deck/deck_outline.md` change log.
  - Plan to regenerate PPTX after Analysts deliver revised narrative (target 25 Sep) using `pandoc deck/*.md -o deck/Ready_Set_Ford_deck.pptx`.
  - **Status 22 Sep:** Slides now reference `deck/visuals/` PNGs; `pandoc deck/*.md -o deck/Ready_Set_Ford_deck.pptx` rerun after visual refresh.
- **Maintainers:**
  - Run `git status` and check for large binaries or permission drifts after data refresh. Document hygiene notes in `Assignment3_plan.md` or `notes/research_notes.md` as needed.

### Stand-up Log
- **22 Sep (async, 09:30 CT):** Focus on primary research outline, memo drafting kickoff, visual prototypes. Owners: Analysts/Writers (research + memo), Data Visualizers (Google Trends/social), Data Collectors (data refresh status). Blockers: awaiting confirmation on access to class readings for citations. Responses logged 22 Sep 14:00 CT.
- **22 Sep (15:30 CT follow-up):** Coordinator pinged Analysts/Writers to confirm citation access for class readings; Analysts confirmed class summaries in `notes/research_notes.md` are sufficient for interim citations.
