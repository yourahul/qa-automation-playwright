from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_to_cart(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.add_item_to_cart()

    page.wait_for_timeout(2000)
    assert inventory.get_cart_count() == "1"
