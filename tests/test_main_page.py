def test_guest_should_see_login_link(main_page):
    main_page.open()
    assert main_page.should_be_login_link(), "Login link is not presented."

def test_guest_can_go_to_login_page(main_page):
    main_page.open()
    main_page.go_to_login_page()