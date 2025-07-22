from .core import load_settings
from .common.browser_controllers import FirefoxController
from .common.drivers import FirefoxDriver, setup_driver
from .handlers import GoogleSearchHandler
from .services import GoogleSearchService
from .utils.csv_utils import read_csv_requests


def main() -> None:
    settings = load_settings()
    user_agents = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
    )
    extentions = (
        (
            settings.base_dir / "utils" / "browser" / "extentions" / "noptcha.xpi",
            True,
        ),
    )
    driver = setup_driver(FirefoxDriver(settings.firefox), user_agents, extentions)

    with FirefoxController(driver) as controller:
        handler = GoogleSearchHandler(controller, 60)
        service = GoogleSearchService(handler, settings.root_dir)

        try:
            requests = read_csv_requests(settings.root_dir, "requests")
            service.collect_links_for_queries(requests, "urls", 2)
        finally:
            controller.quit()


if __name__ == "__main__":
    main()
