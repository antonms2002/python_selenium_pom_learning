from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from pages.base_page import BasePage
import math

class ProductPage(BasePage):
    path = 'catalogue/the-shellcoders-handbook_209/?promo=newYear'

    # locators
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME_TEXT = (By.CSS_SELECTOR, "div.product_main > h1")
    DESCRIPTION_TITLE_TEXT = (By.ID, "product_description")
    ADD_TO_CART_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong")

    def open(self, path = None) -> None:
        if path is None:
            path = self.path
        super().open(path)

    def should_be_product_title(self) -> None:
        assert self.is_element_present(self.PRODUCT_NAME_TEXT), "Product name was not found."

    def add_to_cart(self) -> None:
        self.click_element(self.ADD_TO_CART_BUTTON)

    def get_product_title_text(self) -> str:
        return self.get_text(self.PRODUCT_NAME_TEXT)

    def get_add_to_cart_success_message_text(self) -> str:
        return self.get_text(self.ADD_TO_CART_SUCCESS_MESSAGE)

    def should_be_same_text_product_name_and_success_message(self) -> None:
        assert self.get_product_title_text() == self.get_add_to_cart_success_message_text(), \
            "Product name in success message is different than product name"

    # User needs to solve math expression to add product to cart
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


