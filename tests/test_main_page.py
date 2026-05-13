import pytest


@pytest.mark.main_page
class TestMainPage:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, main_page):
        main_page.open()
        main_page.should_be_login_link()

    @pytest.mark.smoke
    def test_guest_can_go_to_login_page(self, main_page, login_page):
        # Открытие главной страницы
        main_page.open()
        # Переход на login страницу
        main_page.go_to_login_page()
        # Проверка url == url login page
        login_page.should_be_login_url()
        # Проверка, что на странице есть элементы форм login, signup
        login_page.should_be_login_page()

    @pytest.mark.smoke
    def test_guest_cant_see_product_in_cart_opened_from_main_page(self, main_page, cart_page):
        main_page.open()
        main_page.go_to_cart_page()
        cart_page.should_be_cart_page_header()
        cart_page.should_be_continue_shopping_link()


