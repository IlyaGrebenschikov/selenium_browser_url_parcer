from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from common.browser_controllers import BrowserControllerInterface


class GoogleSearchPage:
    SEARCH_BOX = (By.NAME, "q")
    SEARCH_RESULTS = (By.ID, "search")
    NEXT_BUTTON = (By.ID, "pnnext")
    RESULT_LINKS_XPATH = (
        "//a[@href and (ancestor::div[@class='g'] or ancestor::div[@data-snhf='0'])]"
    )

    def __init__(self, driver: BrowserControllerInterface) -> None:
        self.driver = driver

    def open(self) -> None:
        self.driver.get("https://www.google.com")

    def search(self, query: str, timeout: int) -> None:
        search_box = self.driver.wait_until(
            lambda d: d.find_element(*self.SEARCH_BOX), timeout
        )
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        self.driver.wait_until(lambda d: d.find_element(*self.SEARCH_RESULTS), timeout)

    def get_result_links(self, timeout: int) -> set[str]:
        self.driver.wait_until(
            lambda d: d.find_element(By.XPATH, self.RESULT_LINKS_XPATH), timeout
        )
        links = self.driver.find_elements(By.XPATH, self.RESULT_LINKS_XPATH)
        return {
            link.get_attribute("href") for link in links if link.get_attribute("href")
        }

    def go_to_next_page(self, timeout: int) -> bool:
        try:
            self._close_location_popup(timeout)
            next_button = self.driver.wait_until(
                lambda d: d.find_element(*self.NEXT_BUTTON), timeout
            )
            next_url = next_button.get_attribute("href")
            if next_url:
                self.driver.get(next_url)
                self.driver.wait_until(
                    lambda d: d.find_element(*self.SEARCH_RESULTS), timeout
                )
                return True
            return False
        except Exception:
            return False

    def handle_consent_popup(self, timeout: int = 10) -> None:
        try:
            accept_button = self.driver.wait_until(
                lambda d: d.find_element(By.ID, "L2AGLb"), timeout
            )
            accept_button.click()
        except Exception:
            pass

    def _close_location_popup(self, timeout: int = 15) -> None:
        try:
            popup_xpath = (
                "//button[normalize-space()='Не сейчас' or normalize-space()='Not now'] | "
                "//span[normalize-space()='Не сейчас' or normalize-space()='Not now'] | "
                "//div[normalize-space()='Не сейчас' or normalize-space()='Not now']"
            )
            popup_button = self.driver.wait_until(
                lambda d: d.find_element(By.XPATH, popup_xpath), timeout
            )
            popup_button.click()
        except Exception:
            pass
