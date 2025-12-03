from playwright.sync_api import Page, Locator

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.sign_in_top_nav: Locator = page.locator('#WelcomeButton-A11Y-FOCUS-ID')
        self.welcome_sign_in_btn: Locator = page.get_by_test_id('WelcomeMenuButtonSignIn')

    def go_to_home(self, base_url: str):
        self.page.goto(base_url)

    def click_sign_in_top_nav(self):
        self.sign_in_top_nav.click()

    def click_welcome_sign_in(self):
        assert self.welcome_sign_in_btn.is_visible(), "Welcome Sign In button not visible"
        self.welcome_sign_in_btn.click()
