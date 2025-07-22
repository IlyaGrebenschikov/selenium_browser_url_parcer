from .core import load_settings
from .common.browser_controllers import FirefoxController
from .common.drivers import FirefoxDriver, setup_driver
from .handlers import GoogleSearchHandler
from .services import GoogleSearchService
from .utils.csv_utils import read_csv_requests


def main() -> None:
    settings = load_settings()
    driver = setup_driver(FirefoxDriver(settings.firefox))

    with FirefoxController(driver) as controller:
        handler = GoogleSearchHandler(controller)
        service = GoogleSearchService(handler, settings.root_dir)

        try:
            requests = read_csv_requests(settings.root_dir, "requests")
            service.collect_links_for_queries(requests, "urls", 2)
        finally:
            controller.quit()


if __name__ == "__main__":
    main()
