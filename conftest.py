import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose browser language")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def main_page(browser):
    return MainPage(browser)

@pytest.fixture(scope="function")
def login_page(browser):
    return LoginPage(browser)

@pytest.fixture(scope="function")
def product_page(browser):
    return ProductPage(browser)