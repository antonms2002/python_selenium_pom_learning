from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    base_url = "http://selenium1py.pythonanywhere.com/"

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CHECK_CART_BUTTON = (By.CSS_SELECTOR, ".basket-mini > .btn-group > a.btn")


    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 5)

    # Methods for main page
    def should_be_login_link(self) -> None:
        assert self.is_element_present(self.LOGIN_LINK), "Login link is not presented."

    def go_to_login_page(self) -> None:
        login_link = self.find_element(self.LOGIN_LINK)
        login_link.click()

    def go_to_cart_page(self) -> None:
        self.click_element(self.CHECK_CART_BUTTON)

    # Common methods for other pages
    def open(self, path = "") -> None:
        self.browser.get(f"{self.base_url}{path}")

    def get_url(self) -> str:
        return self.browser.current_url

    def find_element(self, locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_text(self, locator) -> str:
        element = self.find_element(locator)
        return element.text

    def is_element_present(self, locator) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    # Method to check that element is NOT appearing on page during timeout(3s)
    def is_not_element_present(self, locator, timeout=3) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
            return False
        except TimeoutException:
            return True

    # visibility_of_element_located - is element visible
    # presence_of_element_located  - is element in DOM
    # Method to check that element disappearing from page
    def is_element_disappeared(self, locator, timeout=3) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    '''
    WebDriverWait(driver, timeout, poll_frequency: float = 0.5, ignored_exceptions: tuple)
        
      - ignored_exceptions: Iterable (tuple in python) structure of exception classes ignored
        during calls. By default, it contains NoSuchElementException only.
        
    Explict wait list: https://selenium-python.readthedocs.io/waits.html 
    
    .until(method): 
    Ожидает, пока предоставленный method вернет что-либо, кроме False.
    Т.е. ждет, когда EC вернет True 
    Если method продолжает возвращать False до истечения времени ожидания, 
    будет вызвано исключение TimeoutException.

    .until_not(method): 
    Ожидает, пока предоставленный method не вернет False. 
     Т.е. ждет, когда EC вернет False
    Если метод не вернет False до истечения времени ожидания, 
    будет вызвано исключение TimeoutException.
    
    К слову, судя по всему явные ожадания из EC (e.g visibility_of_element_located
    это НЕ метод. Это класс с магическим методом __call__.
    __call__() позволяет вызывать экземпляр класса как функцию.
    ПРИ ЭТОМ ЭКЗЕМЛЯР КЛАССА ПЕРЕДАЕТСЯ В метод until, где вызывается как ФУНКЦИЯ.
    Т.е. если создавать класс с __call__, нужно сначала создать экземпляр этого класса. 
    При этом в __call__(self, some_params) можно передавать параметры 
    при вызове через экземпляр класса. - проверить
     '''

    # def is_disappeared(self, how, what, timeout=4):
    #     try:
    #         WebDriverWait(self.browser, timeout, 1, TimeoutException). \
    #             until_not(EC.presence_of_element_located((how, what)))
    #     except TimeoutException:
    #         return False
    #
    #     return True

