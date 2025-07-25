import random
from typing import Any, Optional

from selenium.webdriver import Firefox, FirefoxOptions

from .base import DriverInterface
from src.core.settings import FirefoxSettings


class FirefoxDriver(DriverInterface):
    def __init__(self, settings: FirefoxSettings) -> None:
        self._settings = settings

    def setup_options(
        self, user_agents: Optional[tuple[str]] = None, **kwargs: Any
    ) -> FirefoxOptions:
        options = FirefoxOptions(**kwargs)

        if user_agents:
            user_agent = random.choice(user_agents)
            options.add_argument(f"user-agent={user_agent}")

        if self._settings.headless:
            options.headless = True
            options.add_argument("--headless")

        if self._settings.binary_location:
            options.binary_location = self._settings.binary_location

        return options

    def init_driver(
        self,
        options: FirefoxOptions,
        extentions: Optional[tuple[tuple[str, bool]]] = None,
        **kwargs: Any,
    ) -> Firefox:
        driver = Firefox(options=options, **kwargs)

        if extentions:
            for extention in extentions:
                driver.install_addon(*extention)

        return driver
