from src.common.browser_controllers import BrowserControllerInterface
from src.parsers import GoogleSearchParser


class GoogleSearchHandler:
    def __init__(
        self, controller: BrowserControllerInterface, timeout: int = 30
    ) -> None:
        self._controller = controller
        self._timeout = timeout
        self._parser = GoogleSearchParser(self._controller)

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
