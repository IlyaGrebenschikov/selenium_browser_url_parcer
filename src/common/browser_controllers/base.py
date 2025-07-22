from typing import Any, Sequence
from abc import abstractmethod, ABC


class BrowserControllerInterface(ABC):
    @abstractmethod
    def get(self, url: str) -> None: ...

    @abstractmethod
    def find_element(self, by: Any, value: str) -> Any: ...

    @abstractmethod
    def find_elements(self, by: Any, value: str) -> Sequence[Any]: ...

    @abstractmethod
    def wait_until(self, condition, timeout: int) -> Any: ...
