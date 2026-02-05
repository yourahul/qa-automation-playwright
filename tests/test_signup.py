from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.signup_page import SignupPage

def test_signup_flow(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    # add item first
    inventory = InventoryPage(page)
    inventory.add_item_to_cart()

    page.click(".shopping_cart_link")
    page.click("#checkout")

    signup = SignupPage(page)
    signup.fill_details("Rahul", "Test", "575001")
    signup.click_continue()

    page.wait_for_timeout(2000)

    assert "checkout-step-two" in page.url
