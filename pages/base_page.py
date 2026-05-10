from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    base_url = "http://selenium1py.pythonanywhere.com/"

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    def open(self, path='') -> None:
        self.browser.get(f"{self.base_url}{path}")

    def find_element(self, locator) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def is_element_present(self, locator) -> bool:
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False