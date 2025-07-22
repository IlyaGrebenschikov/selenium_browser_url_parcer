from typing import Optional

from selenium.webdriver import Firefox, Chrome

from .base import DriverInterface
from .firefox import FirefoxDriver


def setup_driver(
    driver_instance: DriverInterface,
    user_agents: Optional[tuple[str]] = None,
    extentions: Optional[tuple[tuple[str, bool]]] = None,
) -> Firefox | Chrome:
    driver_options = driver_instance.setup_options(user_agents)
    driver = driver_instance.init_driver(driver_options, extentions)
    return driver


__all__ = (
    "DriverInterface",
    "FirefoxDriver",
    "setup_driver",
)
