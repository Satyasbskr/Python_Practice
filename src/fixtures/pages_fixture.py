import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from playwright.sync_api import sync_playwright
from src.pages.home_page import HomePage
from src.pages.signin_page import SignInPage

import pytest

@pytest.fixture(scope="function")
def pages():
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless=False, args=["--disable-http2"])
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()
        home = HomePage(page) 
        signin = SignInPage(page)
        yield {
            "page": page,
            "home": home,
            "signin": signin
        }
        browser.close()
