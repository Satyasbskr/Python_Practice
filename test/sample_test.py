import os
import pytest
from src.fixtures.pages_fixture import pages

@pytest.mark.usefixtures("pages")
def test_sample_home_page(pages):
    """Sample test: Go to home page and check Sign In button"""
    base_url = os.getenv("BASE_URL", "https://www.kroger.com/")
    pages["home"].go_to_home(base_url)
    pages["home"].click_sign_in_top_nav()
    assert pages["home"].welcome_sign_in_btn.is_visible(), "Welcome Sign In button should be visible"
    # ...additional checks or actions can be added here...
