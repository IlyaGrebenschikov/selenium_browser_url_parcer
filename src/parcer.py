from .common.drivers import DriverInterface
from .common.page_objects import GoogleSearchPage


class Parser:
    def __init__(self, driver: DriverInterface, timeout: int = 60) -> None:
        self._driver = driver
        self._timeout = timeout
        self._google_page = GoogleSearchPage(driver)

    def search_and_collect_links(self, query: str, pages: int = 1) -> set[str]:
        self._google_page.open()
        self._google_page.handle_consent_popup()
        self._google_page.search(query, self._timeout)
        all_links = set()

        for _ in range(pages):
            all_links |= self._google_page.get_result_links(self._timeout)

            if not self._google_page.go_to_next_page(self._timeout):
                break

        return all_links
