from abc import abstractmethod
from typing import Protocol, Any, Optional

class DriverInterface(Protocol):
    def __init__(self, settings: Any) -> None:
        self._settings = settings

    @abstractmethod
    def setup_options(
        self,
        user_agents: Optional[tuple[str]] = None,
        **kwargs: Any
        ) -> Any: ...

    @abstractmethod
    def init_driver(self, **kwargs: Any) -> Any: ...
