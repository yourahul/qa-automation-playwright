import pytest
import os
from playwright.sync_api import sync_playwright

# ---------- BROWSER FIXTURE ----------
@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)# fixed
        context = browser.new_context()
        page = context.new_page()

        yield page

        browser.close()


# ---------- SCREENSHOT ON FAILURE ----------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            os.makedirs("reports/screenshots", exist_ok=True)
            file_path = f"reports/screenshots/{item.name}.png"
            page.screenshot(path=file_path)
            print(f"\n📸 Screenshot saved: {file_path}")
