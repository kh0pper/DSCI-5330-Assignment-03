#!/usr/bin/env python3
"""Aggregate YouTube metadata into tabular and memo-friendly outputs."""
from __future__ import annotations

import csv
import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
EXTERNAL_DIR = ROOT / "data" / "external"
OUTPUT_CSV = EXTERNAL_DIR / "youtube_metrics.csv"
OUTPUT_JSON = EXTERNAL_DIR / "youtube_metrics_summary.json"
OUTPUT_MD = ROOT / "notes" / "youtube_snapshot.md"


def _iter_json_objects(text: str):
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        try:
            yield json.loads(stripped)
        except json.JSONDecodeError:
            continue


def _parse_upload_date(raw: str | None) -> tuple[str, str]:
    if not raw:
        return "", ""
    try:
        dt = datetime.strptime(raw, "%Y%m%d")
    except ValueError:
        return raw, raw
    return raw, dt.date().isoformat()


def load_youtube_metadata() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for json_path in sorted(EXTERNAL_DIR.glob("youtube_*.json")):
        data = None
        for obj in _iter_json_objects(json_path.read_text()):
            data = obj
        if not data:
            continue

        raw_date, iso_date = _parse_upload_date(data.get("upload_date"))
        view_count = data.get("view_count")
        like_count = data.get("like_count")
        engagement = None
        if isinstance(view_count, int) and view_count > 0 and isinstance(like_count, int):
            engagement = round((like_count / view_count) * 100, 2)

        records.append(
            {
                "video_id": data.get("id", ""),
                "title": data.get("title", ""),
                "channel": data.get("channel", ""),
                "upload_date": raw_date,
                "upload_date_iso": iso_date,
                "duration_seconds": data.get("duration"),
                "view_count": view_count,
                "like_count": like_count,
                "engagement_pct": engagement,
                "category": ", ".join(data.get("categories", []) or []),
                "tags": ", ".join((data.get("tags") or [])[:5]),
                "watch_url": data.get("webpage_url") or f"https://www.youtube.com/watch?v={data.get('id', '')}",
            }
        )

    return records


def write_outputs(records: list[dict[str, object]]) -> None:
    if not records:
        print("[WARN] No YouTube metadata files found; skipping aggregation.")
        return

    fieldnames = [
        "video_id",
        "title",
        "channel",
        "upload_date_iso",
        "duration_seconds",
        "view_count",
        "like_count",
        "engagement_pct",
        "category",
        "tags",
        "watch_url",
    ]

    with OUTPUT_CSV.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in records:
            writer.writerow({key: row.get(key, "") for key in fieldnames})

    OUTPUT_JSON.write_text(json.dumps(records, indent=2))

    md_lines = ["# Ready Set Ford Video Snapshot", "", "| Video | Upload | Views | Likes | Engagement % |", "| --- | --- | ---: | ---: | ---: |"]
    for row in records:
        md_lines.append(
            f"| [{row['title']}]({row['watch_url']}) | {row['upload_date_iso']} | {row['view_count'] or ''} | {row['like_count'] or ''} | {row['engagement_pct'] or ''} |"
        )

    OUTPUT_MD.write_text("\n".join(md_lines) + "\n")

    print(f"[OK] Wrote YouTube metrics CSV to {OUTPUT_CSV.relative_to(ROOT)}")
    print(f"[OK] Wrote YouTube metrics JSON to {OUTPUT_JSON.relative_to(ROOT)}")
    print(f"[OK] Updated memo snapshot at {OUTPUT_MD.relative_to(ROOT)}")


def main() -> int:
    records = load_youtube_metadata()
    write_outputs(records)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
