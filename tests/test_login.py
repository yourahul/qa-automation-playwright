from pages.login_page import LoginPage

def test_login(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    page.wait_for_timeout(2000)
    assert "inventory" in page.url
