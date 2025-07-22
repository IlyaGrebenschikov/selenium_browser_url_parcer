import csv
from pathlib import Path


def write_csv_urls(root_dir: Path, filename: str, urls: set[str]) -> None:
    filepath = root_dir / "data" / f"{filename}.csv"
    with open(filepath, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for url in urls:
            writer.writerow([url])
