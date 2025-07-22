import random
from typing import Any

from selenium.webdriver import Firefox, FirefoxOptions

from .base import DriverInterface
from src.core.settings import FirefoxSettings

class FirefoxDriver(DriverInterface):
    def __init__(self, settings: FirefoxSettings) -> None:
        super().__init__(settings)

    def setup_options(self, **kwargs: Any) -> FirefoxOptions:
        options = FirefoxOptions(**kwargs)
        USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
        ]
        user_agent = random.choice(USER_AGENTS)
        options.add_argument(f"user-agent={user_agent}")

        if self._settings.headless:
            options.headless = True
            options.add_argument("--headless")

        if self._settings.binary_location:
            options.binary_location = self._settings.binary_location

        return options

    def init_driver_firefox(
        options: FirefoxOptions,
        extentions: tuple[tuple[str, bool]],
        **kwargs: Any
    ) -> Firefox:
        driver = Firefox(
            options=options,
            **kwargs
            )

        for extention in extentions:
            driver.install_addon(*extention)

        return driver
