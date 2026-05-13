import pytest


@pytest.mark.parametrize(
    "path",
    ["catalogue/coders-at-work_207/?promo=offer0",
     "catalogue/coders-at-work_207/?promo=offer1",
     "catalogue/coders-at-work_207/?promo=offer2",
     "catalogue/coders-at-work_207/?promo=offer3",
     "catalogue/coders-at-work_207/?promo=offer4",
     "catalogue/coders-at-work_207/?promo=offer5",
     "catalogue/coders-at-work_207/?promo=offer6",
     pytest.param("catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
     "catalogue/coders-at-work_207/?promo=offer8",
     "catalogue/coders-at-work_207/?promo=offer9"],
    ids = ["offer0", "offer1", "offer2", "offer3", "offer4",
           "offer5", "offer6", "offer7", "offer8", "offer9"])
def test_guest_can_add_product_to_basket(product_page, path):
    # Open product page
    product_page.open(path)
    # Check that product tittle is present
    product_page.should_be_product_title()
    # Click add to cart
    product_page.add_to_cart()
    # Solve quiz
    product_page.solve_quiz_and_get_code()
    # Check that product tittle present in success message
    product_page.should_be_same_text_product_name_and_success_message()

def test_guest_should_see_login_link_on_product_page(product_page):
    product_page.open()
    product_page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(product_page, login_page):
    product_page.open()
    product_page.go_to_login_page()
    login_page.should_be_login_form()

def test_unavailable_good(product_page):
    product_page.open(path="catalogue/hackers-painters_185/")
    product_page.should_be_product_title()
    product_page.should_be_unavailability_message()
    product_page.should_not_be_add_to_cart()

def test_guest_cant_see_success_message_without_adding_to_cart(product_page):
    product_page.open()
    product_page.should_not_be_success_message()

def test_guest_cant_see_product_in_basket_opened_from_product_page(product_page, cart_page):
    product_page.open()
    product_page.go_to_cart_page()
    cart_page.should_be_cart_page_header()
    cart_page.should_be_continue_shopping_link()

@pytest.mark.skip(reason="Not valid test. Made for page methods debug")
def test_guest_cant_see_success_message_after_adding_product_to_basket(product_page):
    product_page.open()
    product_page.add_to_cart()
    # Next step will be failed.
    product_page.should_not_be_success_message()

@pytest.mark.skip(reason="Not valid test. Made for page methods debug")
def test_message_disappeared_after_adding_product_to_basket(product_page):
    product_page.open()
    product_page.add_to_cart()
    # Next step will be failed
    product_page.should_disappear_success_message()