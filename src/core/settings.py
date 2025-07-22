from pathlib import Path
from typing import Any, Optional


class BaseSettings:
    def as_dict(self) -> dict[Any, Any]:
        return {
            key: value
            for key, value in vars(type(self)).items()
            if (not key.startswith("__") and not key.endswith("__"))
            and not callable(value)
        }


class ChromeSettings(BaseSettings):
    headless: bool = False
    version_main: Optional[str] = None
    use_subprocess: bool = False
    driver_executable_path: Optional[str] = None


class FirefoxSettings(BaseSettings):
    headless: bool = False
    binary_location: Optional[str] = None
    driver_executable_path: Optional[str] = None


class Settings:
    def __init__(
        self,
        base_dir: Path,
        root_dir: Path,
        chrome_settings: ChromeSettings,
        firefox_settings: FirefoxSettings,
    ) -> None:
        self._base_dir = base_dir
        self._root_dir = root_dir
        self._chrome_settings = chrome_settings
        self._firefox_settings = firefox_settings

    @property
    def base_dir(self) -> Path:
        return self._base_dir

    @property
    def root_dir(self) -> Path:
        return self._root_dir

    @property
    def chrome(self) -> ChromeSettings:
        return self._chrome_settings

    @property
    def firefox(self) -> FirefoxSettings:
        return self._firefox_settings


def load_base_dir() -> Path:
    return Path(__file__).parent.parent


def load_root_dir() -> Path:
    return Path(__file__).parent.parent.parent


def load_settings(
    base_dir: Optional[Path] = None,
    root_dir: Optional[Path] = None,
    chrome_settings: Optional[ChromeSettings] = None,
    firefox_settings: Optional[FirefoxSettings] = None,
) -> Settings:
    return Settings(
        base_dir or load_base_dir(),
        root_dir or load_root_dir(),
        chrome_settings or ChromeSettings(),
        firefox_settings or FirefoxSettings(),
    )
