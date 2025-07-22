import csv
from pathlib import Path


def read_csv_requests(root_dir: Path, filename: str) -> list[str]:
    filepath = root_dir / "data" / f"{filename}.csv"
    urls = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                urls.append(row[0])
    return urls
