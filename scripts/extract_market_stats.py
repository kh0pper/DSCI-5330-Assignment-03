#!/usr/bin/env python3
"""Harvest key market statistics from sourced PDFs into a single CSV."""
from __future__ import annotations

import csv
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / "sources" / "external"
DATA_DIR = ROOT / "data" / "external"
OUTPUT_PATH = DATA_DIR / "market_stats.csv"


def _run_pdftotext(pdf_path: Path, txt_path: Path) -> None:
    txt_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run([
            "pdftotext",
            str(pdf_path),
            str(txt_path),
        ], check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        raise RuntimeError(f"pdftotext failed for {pdf_path}")


def _ensure_text(name: str) -> str:
    pdf_path = SOURCE_DIR / name
    if not pdf_path.exists():
        raise FileNotFoundError(f"Missing source PDF: {pdf_path}")

    txt_path = DATA_DIR / Path(name).with_suffix(".txt")
    if not txt_path.exists():
        _run_pdftotext(pdf_path, txt_path)
    return txt_path.read_text(encoding="utf-8", errors="ignore")


def _float_from_match(group: str) -> float:
    cleaned = group.replace(",", "").replace("€", "").replace("$", "")
    multiplier = 1.0
    if "billion" in group.lower():
        multiplier = 1_000_000_000
    elif "million" in group.lower():
        multiplier = 1_000_000
    return float(re.findall(r"[0-9]+(?:\.[0-9]+)?", cleaned)[0]) * multiplier


def collect_jd_power() -> list[dict[str, str]]:
    text = _ensure_text("JD_Power_2024_Brand_Loyalty.pdf")
    captures: list[tuple[str, str, str]] = [
        ("Ford truck loyalty rate", r"Ford ranks highest among truck owners .*?([0-9]+\.[0-9])%", "Highest loyalty rate in the study; Ford leads truck segment for the third consecutive year."),
        ("Honda SUV loyalty rate", r"Honda ranks highest among mass market brand SUV owners with a ([0-9]+\.[0-9])%", "Honda leads SUV loyalty while Subaru follows at 62.6%."),
        ("Toyota car loyalty rate", r"Toyota ranks highest among mass market brand car owners .*?([0-9]+\.[0-9])%", "Toyota repeats as mass-market car loyalty leader."),
        ("Lexus premium SUV loyalty rate", r"Lexus ranks highest among premium brand SUV owners with a ([0-9]+\.[0-9])%", "BMW is second at 55.8%."),
        ("Porsche premium car loyalty rate", r"Porsche ranks highest among premium brand car owners .*?([0-9]+\.[0-9])%", "Porsche holds the top premium car loyalty slot; Mercedes-Benz second at 49.0%."),
    ]

    rows = []
    for metric, pattern, context in captures:
        match = re.search(pattern, text, flags=re.DOTALL)
        if match:
            rows.append(
                {
                    "source": "J.D. Power U.S. Automotive Brand Loyalty Study",
                    "date": "2024-09-25",
                    "metric": metric,
                    "value": match.group(1),
                    "context": context,
                    "url": "https://www.jdpower.com/sites/default/files/file/2024-09/2024107%20U.S.%20Automotive%20Brand%20Loyalty.pdf",
                }
            )
    return rows


def collect_mckinsey_collectibles() -> list[dict[str, str]]:
    text = _ensure_text("McKinsey_Collectible_Cars.pdf")
    rows: list[dict[str, str]] = []

    stock_match = re.search(r"global value .*? to around (?:€|\$)([0-9,.]+)\s*billion", text, re.IGNORECASE | re.DOTALL)
    if stock_match:
        value = int(_float_from_match(stock_match.group(1) + " billion"))
        rows.append(
            {
                "source": "McKinsey – Collectible cars report",
                "date": "2025-02-04",
                "metric": "Global collectible car stock value",
                "value": value,
                "context": "Estimated value of global collectible car stock in 2024 (~€800B).",
                "url": "https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/collectible-cars-from-niche-market-to-growth-and-innovation-engine",
            }
        )

    auction_match = re.search(r"average transaction price is about (?:€|\$)([0-9,.]+) for auctions", text, re.IGNORECASE | re.DOTALL)
    if auction_match:
        rows.append(
            {
                "source": "McKinsey – Collectible cars report",
                "date": "2025-02-04",
                "metric": "Average collectible car auction price",
                "value": int(_float_from_match(auction_match.group(1))),
                "context": "Average auction transaction price for collectible cars (~€65k).",
                "url": "https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/collectible-cars-from-niche-market-to-growth-and-innovation-engine",
            }
        )

    listing_match = re.search(r"average transaction price is about .*? for auctions and (?:€|\$)([0-9,.]+) for public listings", text, re.IGNORECASE | re.DOTALL)
    if listing_match:
        rows.append(
            {
                "source": "McKinsey – Collectible cars report",
                "date": "2025-02-04",
                "metric": "Average collectible car listing price",
                "value": int(_float_from_match(listing_match.group(1))),
                "context": "Average public listing price highlights broader accessibility of the segment (~€56k).",
                "url": "https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/collectible-cars-from-niche-market-to-growth-and-innovation-engine",
            }
        )

    sale_match = re.search(r"sold for \$([0-9,.]+)\s+million\s+\(about €([0-9,.]+) million\)", text, re.IGNORECASE | re.DOTALL)
    if sale_match:
        rows.append(
            {
                "source": "McKinsey – Collectible cars report",
                "date": "2025-02-04",
                "metric": "Record 300 SLR Uhlenhaut sale",
                "value": int(float(sale_match.group(1).replace(",", ""))) * 1_000_000,
                "context": "Mercedes-Benz 300 SLR Uhlenhaut Coupé sold for $143M (≈€137M) at auction in 2022.",
                "url": "https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/collectible-cars-from-niche-market-to-growth-and-innovation-engine",
            }
        )

    return rows


def collect_mckinsey_interview() -> list[dict[str, str]]:
    text = _ensure_text("McKinsey_Ford_Transformation.pdf")
    quote_match = re.search(
        r"This industry has seen more changes in the past decade than perhaps in the prior hundred years",
        text,
    )

    rows: list[dict[str, str]] = []
    if quote_match:
        rows.append(
            {
                "source": "McKinsey – Ford’s evolving sense of self",
                "date": "2019-02-25",
                "metric": "Quote: Industry change pace",
                "value": "",
                "context": "Hau Thai-Tang underscores urgency for marketing transformation.",
                "url": "https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/fords-evolving-sense-of-self-an-interview-with-hau-thai-tang",
            }
        )
    return rows


def write_market_stats(rows: list[dict[str, str]]) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    fieldnames = ["source", "date", "metric", "value", "context", "url"]
    rows_sorted = sorted(rows, key=lambda r: (r["source"], r["metric"]))
    with OUTPUT_PATH.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows_sorted:
            writer.writerow(row)


def main() -> int:
    rows = []
    rows.extend(collect_jd_power())
    rows.extend(collect_mckinsey_collectibles())
    rows.extend(collect_mckinsey_interview())
    write_market_stats(rows)
    print(f"[OK] Extracted {len(rows)} market stats to {OUTPUT_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
