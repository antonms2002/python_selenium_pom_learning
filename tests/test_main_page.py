def test_guest_should_see_login_link(main_page):
    main_page.open()
    main_page.should_be_login_link()

def test_guest_can_go_to_login_page(main_page, login_page):
    # Открытие главной страницы
    main_page.open()
    # Переход на login страницу
    main_page.go_to_login_page()
    # Проверка url == url login page
    login_page.should_be_login_url()
    # Проверка, что на странице есть элементы форм login, signup
    login_page.should_be_login_page()