from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        page.wait_for_timeout(3000)

        assert "inventory" in page.url

        browser.close()
