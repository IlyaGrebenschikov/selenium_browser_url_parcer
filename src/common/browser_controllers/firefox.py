from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from .base import BrowserControllerInterface


class FirefoxController(BrowserControllerInterface):
    def __init__(self, driver: Firefox):
        self._driver = driver

    def get(self, url: str) -> None:
        self._driver.get(url)

    def find_element(self, by, value: str):
        return self._driver.find_element(by, value)

    def find_elements(self, by, value: str):
        return self._driver.find_elements(by, value)

    def wait_until(self, condition, timeout: int):
        return WebDriverWait(self._driver, timeout).until(condition)
