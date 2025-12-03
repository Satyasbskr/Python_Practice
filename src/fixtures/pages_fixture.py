import os
from playwright.sync_api import sync_playwright
from src.pages.home_page import HomePage
from src.pages.signin_page import SignInPage

import pytest

@pytest.fixture(scope="function")
def pages():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        home = HomePage(page)
        signin = SignInPage(page)
        yield {
            "page": page,
            "home": home,
            "signin": signin
        }
        browser.close()
