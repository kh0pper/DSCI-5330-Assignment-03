#!/usr/bin/env python3
"""Generate deck slides summarizing Google Trends and Twitter activity."""
from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
EXTERNAL = ROOT / "data" / "external"
TRENDS_CSV = EXTERNAL / "google_trends_readysetford_us.csv"
TWITTER_JSONL = EXTERNAL / "twitter_readysetford.jsonl"

TREND_SLIDE = ROOT / "deck" / "slide_digital_pulse_trends.md"
SOCIAL_SLIDE = ROOT / "deck" / "slide_social_listening.md"


def load_trends() -> list[dict[str, object]]:
    rows = []
    with TRENDS_CSV.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                date = datetime.strptime(row["date"], "%Y-%m-%d").date()
            except ValueError:
                continue
            ready = int(row["Ready Set Ford"])
            pro = int(row["Ford Pro"])
            rows.append({"date": date, "ready": ready, "pro": pro})
    return rows


def compute_trend_stats(rows: list[dict[str, object]]) -> dict[str, object]:
    if not rows:
        return {}

    rows_sorted = sorted(rows, key=lambda r: r["date"])
    latest_date = rows_sorted[-1]["date"]
    window_start = latest_date - timedelta(days=90)

    def summarize(series_key: str) -> dict[str, object]:
        peak_row = max(rows_sorted, key=lambda r: r[series_key])
        trailing_values = [r[series_key] for r in rows_sorted if r["date"] >= window_start]
        trailing_avg = sum(trailing_values) / len(trailing_values) if trailing_values else 0
        return {
            "peak_value": peak_row[series_key],
            "peak_date": peak_row["date"].isoformat(),
            "trailing_avg": round(trailing_avg, 1),
        }

    ready_stats = summarize("ready")
    pro_stats = summarize("pro")
    delta = ready_stats["trailing_avg"] - pro_stats["trailing_avg"]

    return {
        "latest": latest_date.isoformat(),
        "ready": ready_stats,
        "pro": pro_stats,
        "delta": round(delta, 1),
    }


def write_trend_slide(stats: dict[str, object]) -> None:
    if not stats:
        TREND_SLIDE.write_text("# Digital Pulse – Google Trends\n\n_No Google Trends data available._\n")
        return

    content = f"""# Digital Pulse – Google Trends (US)

| Term | Peak Weekly Interest | Peak Week | Trailing 90-Day Avg | Trend vs. Ford Pro |
| --- | ---: | --- | ---: | ---: |
| Ready Set Ford | {stats['ready']['peak_value']} | {stats['ready']['peak_date']} | {stats['ready']['trailing_avg']} | {stats['delta']} |
| Ford Pro | {stats['pro']['peak_value']} | {stats['pro']['peak_date']} | {stats['pro']['trailing_avg']} | 0.0 |

- Ready Set Ford searches peaked the week of {stats['ready']['peak_date']} with an index of {stats['ready']['peak_value']}.
- Over the past 90 days (ending {stats['latest']}), Ready Set Ford averaged {stats['ready']['trailing_avg']} vs. Ford Pro at {stats['pro']['trailing_avg']} (delta {stats['delta']:+}).
- Use this slide alongside campaign milestones to explain spikes tied to video drops or press coverage.

*Source: `google_trends_readysetford_us.csv` generated via `scripts/collect_additional_data.py`.*
"""
    TREND_SLIDE.write_text(content)


def load_twitter() -> list[dict[str, object]]:
    if not TWITTER_JSONL.exists():
        return []

    posts = []
    with TWITTER_JSONL.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                posts.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return posts


def compute_twitter_stats(posts: list[dict[str, object]]) -> dict[str, object]:
    if not posts:
        return {}

    hashtag_counter: Counter[str] = Counter()
    top_examples: list[str] = []
    for post in posts:
        entities = post.get("entities") or {}
        hashtags = entities.get("hashtags") or []
        for tag in hashtags:
            tag_text = tag.get("tag") or tag.get("text") or ""
            if tag_text:
                hashtag_counter[tag_text.lower()] += 1

        if len(top_examples) < 3:
            text = (post.get("text") or "").strip().replace("\n", " ")
            if text:
                top_examples.append(text[:120])

    top_hashtags = hashtag_counter.most_common(5)
    return {
        "count": len(posts),
        "top_hashtags": top_hashtags,
        "examples": top_examples,
    }


def write_social_slide(stats: dict[str, object]) -> None:
    if not stats:
        SOCIAL_SLIDE.write_text("# Digital Pulse – Twitter Listening\n\n_No Twitter data captured for Ready Set Ford._\n")
        return

    table_rows = ["| Rank | Hashtag | Mentions |", "| ---: | --- | ---: |"]
    if stats["top_hashtags"]:
        for idx, (tag, count) in enumerate(stats["top_hashtags"]):
            table_rows.append(f"| {idx + 1} | #{tag} | {count} |")
    else:
        table_rows.append("| - | (no hashtags captured) | - |")
    hashtag_table = "\n".join(table_rows)

    filtered_examples = [text for text in stats["examples"] if text]
    if filtered_examples:
        examples_md = "\n".join(f"- \"{text}...\"" for text in filtered_examples)
    else:
        examples_md = "- \"No representative tweets captured.\""

    content = f"""# Digital Pulse – Twitter Listening (Ready Set Ford)

Total captured tweets: **{stats['count']}** (limit 200, 6-day window).

{hashtag_table}

Representative posts:
{examples_md}

*Source: `twitter_readysetford.jsonl` via `scripts/collect_additional_data.py` (twarc2 search).* 
"""
    SOCIAL_SLIDE.write_text(content)


def main() -> int:
    trend_rows = load_trends()
    trend_stats = compute_trend_stats(trend_rows)
    write_trend_slide(trend_stats)

    posts = load_twitter()
    twitter_stats = compute_twitter_stats(posts)
    write_social_slide(twitter_stats)
    print("[OK] Generated digital pulse slides in deck/ directory")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
