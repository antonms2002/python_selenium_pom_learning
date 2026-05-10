from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    def should_be_login_link(self) -> bool:
        return self.is_element_present(self.LOGIN_LINK)

    def go_to_login_page(self) -> None:
        login_link = self.find_element(self.LOGIN_LINK)
        login_link.click()

