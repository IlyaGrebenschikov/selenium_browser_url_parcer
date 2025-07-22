from src.common.drivers import DriverInterface
from src.parsers import GoogleSearchParser


class GoogleSearchHandler:
    def __init__(self, driver: DriverInterface, timeout: int = 60) -> None:
        self._driver = driver
        self._timeout = timeout
        self._parser = GoogleSearchParser(driver)

    def search_and_collect_links(self, query: str, pages: int = 1) -> set[str]:
        self._parser.open()
        self._parser.handle_consent_popup()
        self._parser.search(query, self._timeout)
        all_links = set()

        for _ in range(pages):
            all_links |= self._parser.get_result_links(self._timeout)

            if not self._parser.go_to_next_page(self._timeout):
                break

        return all_links
