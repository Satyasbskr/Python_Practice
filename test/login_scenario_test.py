import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from src.fixtures.pages_fixture import pages

@pytest.mark.positive
@pytest.mark.login
@pytest.mark.usefixtures("pages")
def test_successful_login(pages):
    """UI-001 - Successful login with valid credentials"""
    base_url = os.getenv("BASE_URL", "https://www.kroger.com/")
    username = os.getenv("USERNAME", "your_prod_username")
    password = os.getenv("PASSWORD", "your_prod_password")
    pages["home"].go_to_home(base_url)
    pages["home"].click_sign_in_top_nav()
    pages["home"].click_welcome_sign_in()
    pages["signin"].fill_email(username)
    pages["signin"].fill_password(password)
    pages["signin"].ensure_remember_me_selected()
    pages["signin"].click_sign_in()
    # Add assertions for successful login here

@pytest.mark.negative
@pytest.mark.login
@pytest.mark.usefixtures("pages")
def test_unsuccessful_login(pages):
    """UI-002 - Unsuccessful login with incorrect password"""
    base_url = os.getenv("BASE_URL", "https://www.kroger.com/")
    username = os.getenv("USERNAME", "your_prod_username")
    password = os.getenv("INCORRECT_PASSWORD", "wrong_password")
    pages["home"].go_to_home(base_url)
    pages["home"].click_sign_in_top_nav()
    pages["home"].click_welcome_sign_in()
    pages["signin"].fill_email(username)
    pages["signin"].fill_password(password)
    pages["signin"].ensure_remember_me_selected()
    pages["signin"].click_sign_in()
    # Add assertions for failed login here
