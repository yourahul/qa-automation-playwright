from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # login first
        login_page = LoginPage(page)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # inventory actions
        inventory_page = InventoryPage(page)
        inventory_page.add_item_to_cart()
        inventory_page.open_cart()

        page.wait_for_timeout(3000)

        assert "cart" in page.url

        browser.close()
