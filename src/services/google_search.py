from typing import Sequence
from pathlib import Path

from src.handlers.google_search import GoogleSearchHandler
from src.utils.csv_utils import write_csv_urls


class GoogleSearchService:
    def __init__(self, handler: GoogleSearchHandler, root_dir: Path) -> None:
        self._handler = handler
        self._root_dir = root_dir

    def collect_links_for_queries(
        self, queries: Sequence[str], output_file_name: str, pages: int = 1
    ) -> None:
        for query in queries:
            result = self._handler.search_and_collect_links(query, pages)
            write_csv_urls(self._root_dir, output_file_name, result)
