#!/usr/bin/env python3
"""Helper script to collect additional marketing intelligence datasets.

This script is designed to run locally (with network access). It performs the following:
1. Google Trends export via pytrends (if the library is installed).
2. Initializes a market research stats template for manual/automated entries.
3. Optionally runs a twarc2 search for Twitter/X mentions (requires twarc2 CLI + credentials).
4. Optionally captures YouTube metadata via yt-dlp (requires yt-dlp installed).

Edit the configuration variables below to adjust keywords, file names, or API settings.
"""
from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration – adjust to taste
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "DSCI-5330-Assignment-03" / "data"
EXTERNAL_DIR = DATA_DIR / "external"

GOOGLE_TRENDS_TERMS = [
    "Ready Set Ford",
    "Ford Pro",
]
GOOGLE_TRENDS_TIMEFRAME = "today 5-y"  # See pytrends docs for syntax
GOOGLE_TRENDS_GEO = "US"

TWITTER_OUTPUT = EXTERNAL_DIR / "twitter_readysetford.jsonl"
TWARC_QUERY = "Ready Set Ford lang:en -is:retweet"
TWARC_LIMIT = "200"  # string to pass to CLI

YOUTUBE_URLS = [
    # e.g. "https://www.youtube.com/watch?v=VIDEO_ID"
]

MARKET_STATS_CSV = EXTERNAL_DIR / "market_stats.csv"

# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------
def ensure_directories() -> None:
    EXTERNAL_DIR.mkdir(parents=True, exist_ok=True)
    (DATA_DIR / "sec").mkdir(parents=True, exist_ok=True)


def download_google_trends() -> None:
    try:
        from pytrends.request import TrendReq
    except ImportError:  # pragma: no cover - optional dependency
        print("[WARN] pytrends not installed. Skipping Google Trends export.")
        print("       Install with: pip install pytrends pandas")
        return

    pytrends = TrendReq(hl="en-US", tz=360)
    print(f"[INFO] Requesting Google Trends data for {GOOGLE_TRENDS_TERMS}")
    pytrends.build_payload(
        kw_list=GOOGLE_TRENDS_TERMS,
        timeframe=GOOGLE_TRENDS_TIMEFRAME,
        geo=GOOGLE_TRENDS_GEO,
    )

    df = pytrends.interest_over_time()
    out_path = EXTERNAL_DIR / "google_trends_readysetford_us.csv"
    df.to_csv(out_path)
    print(f"[OK] Saved Google Trends CSV to {out_path.relative_to(ROOT)}")


def initialize_market_stats_template() -> None:
    if MARKET_STATS_CSV.exists():
        print(f"[INFO] Market stats CSV already exists: {MARKET_STATS_CSV.relative_to(ROOT)}")
        return

    header = ["source", "date", "metric", "value", "context", "url"]
    rows = [
        [
            "J.D. Power Brand Loyalty Study",
            "2025-07-10",
            "Ford loyalty rate",
            "",
            "Add summary of the headline stat",
            "https://www.jdpower.com/...",
        ],
        [
            "McKinsey Automotive Marketing Report",
            "2025-05-15",
            "EV consideration uplift",
            "",
            "Record headline metric",
            "https://www.mckinsey.com/...",
        ],
    ]

    with MARKET_STATS_CSV.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    print(f"[OK] Wrote market stats template to {MARKET_STATS_CSV.relative_to(ROOT)}")


def run_twarc_search() -> None:
    if TWARC_QUERY == "":
        print("[INFO] TWARC_QUERY empty; skipping Twitter scrape.")
        return

    if TWITTER_OUTPUT.exists():
        print(f"[INFO] Twitter output already present: {TWITTER_OUTPUT.relative_to(ROOT)}")
        return

    cmd = [
        "twarc2",
        "search",
        TWARC_QUERY,
        "--limit",
        TWARC_LIMIT,
        str(TWITTER_OUTPUT),
    ]
    print("[INFO] Running twarc2 search:", " ".join(cmd))
    try:
        subprocess.run(cmd, check=True)
        print(f"[OK] Saved Twitter data to {TWITTER_OUTPUT.relative_to(ROOT)}")
    except FileNotFoundError:
        print("[WARN] twarc2 CLI not found. Install via `pip install twarc`. Skipping.")
    except subprocess.CalledProcessError as exc:
        print(f"[WARN] twarc2 search failed: {exc}")


def fetch_youtube_metadata() -> None:
    if not YOUTUBE_URLS:
        print("[INFO] No YouTube URLs configured. Skipping.")
        return

    for url in YOUTUBE_URLS:
        video_id = url.split("v=")[-1]
        out_path = EXTERNAL_DIR / f"youtube_{video_id}.json"
        cmd = [
            "yt-dlp",
            "--skip-download",
            "--print-json",
            url,
        ]
        print("[INFO] Fetching YouTube metadata:", url)
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            out_path.write_text(result.stdout)
            print(f"[OK] Saved YouTube metadata to {out_path.relative_to(ROOT)}")
        except FileNotFoundError:
            print("[WARN] yt-dlp not found. Install via `pip install yt-dlp`. Skipping.")
            break
        except subprocess.CalledProcessError as exc:
            print(f"[WARN] yt-dlp failed for {url}: {exc}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main() -> int:
    ensure_directories()
    download_google_trends()
    initialize_market_stats_template()
    run_twarc_search()
    fetch_youtube_metadata()
    print("[DONE] Additional data pull workflow complete. Review outputs under", EXTERNAL_DIR.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
