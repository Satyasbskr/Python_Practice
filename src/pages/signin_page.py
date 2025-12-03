from playwright.sync_api import Page, Locator

class SignInPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input: Locator = page.locator('#signInName')
        self.password_input: Locator = page.locator('#forgotPassword')
        self.remember_me_checkbox: Locator = page.locator('#kr_remember_me_adi_true')
        self.sign_in_btn: Locator = page.locator('#continue')

    def fill_email(self, username: str):
        self.email_input.click()
        self.email_input.fill(username)

    def fill_password(self, password: str):
        self.password_input.click()
        self.password_input.fill(password)

    def ensure_remember_me_selected(self):
        if not self.remember_me_checkbox.is_checked():
            self.remember_me_checkbox.check()

    def click_sign_in(self):
        self.sign_in_btn.click()
