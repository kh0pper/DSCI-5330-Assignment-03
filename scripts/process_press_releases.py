#!/usr/bin/env python3
import re
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parent.parent  # DSCI-5330/Assignment 03
DATA_DIR = ROOT / "DSCI-5330-Assignment-03" / "data" / "external"
HTML_FILES = {
    "ford_servicetitan": DATA_DIR / "ford_servicetitan.html",
    "ford_managed_charging": DATA_DIR / "ford_managed_charging.html",
}

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        data = data.strip()
        if data:
            self.parts.append(data)

    def get_text(self):
        return "\n".join(self.parts)

def html_to_text(src: Path) -> str:
    parser = TextExtractor()
    parser.feed(src.read_text(encoding="utf-8", errors="ignore"))
    return parser.get_text()

def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    metrics_rows = []

    for key, html_path in HTML_FILES.items():
        if not html_path.exists():
            print(f"[WARN] Missing HTML file: {html_path}")
            continue

        text = html_to_text(html_path)
        text_path = html_path.with_suffix(".txt")
        text_path.write_text(text, encoding="utf-8")
        print(f"[OK] Wrote text to {text_path.relative_to(ROOT)}")

        numbers = re.findall(r"\b\d[\d,\.]*\b", text)
        metrics_rows.append(f"{key},{'; '.join(numbers)}")

    metrics_csv = DATA_DIR / "ford_press_metrics.csv"
    metrics_csv.write_text("source,raw_numbers\n" + "\n".join(metrics_rows), encoding="utf-8")
    print(f"[OK] Wrote metrics summary to {metrics_csv.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
