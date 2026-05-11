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