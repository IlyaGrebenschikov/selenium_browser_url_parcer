from selenium.webdriver import Firefox, Chrome

from .base import DriverInterface
from .firefox import FirefoxDriver


def setup_driver(driver_instance: DriverInterface) -> Firefox | Chrome:
    driver_options = driver_instance.setup_options()
    driver = driver_instance.init_driver(driver_options)
    return driver


__all__ = (
    "DriverInterface",
    "FirefoxDriver",
)
