from abc import abstractmethod, ABC
from typing import Any, Sequence

from selenium.webdriver import Firefox, Chrome


class BrowserControllerInterface(ABC):
    def __init__(self, driver: Firefox | Chrome) -> None:
        self._driver = driver

    def __enter__(self) -> "BrowserControllerInterface":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.quit()

    def quit(self) -> None:
        self._driver.quit()

    @abstractmethod
    def get(self, url: str) -> None: ...

    @abstractmethod
    def find_element(self, by: Any, value: str) -> Any: ...

    @abstractmethod
    def find_elements(self, by: Any, value: str) -> Sequence[Any]: ...

    @abstractmethod
    def wait_until(self, condition, timeout: int) -> Any: ...
