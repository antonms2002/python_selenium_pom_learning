import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class Navbar:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CHECK_CART_BUTTON = (By.CSS_SELECTOR, ".basket-mini > .btn-group > a.btn")

    def __init__(self, browser):
        self.wait = WebDriverWait(browser, 5)

    def is_element_present(self, locator) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Check login link is present")
    def should_be_login_link(self) -> None:
        assert self.is_element_present(self.LOGIN_LINK), "Login link is not presented."

    @allure.step("Go to login page")
    def go_to_login_page(self) -> None:
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_LINK)).click()

    @allure.step("Go to cart page")
    def go_to_cart_page(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.CHECK_CART_BUTTON)).click()