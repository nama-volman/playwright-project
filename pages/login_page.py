from playwright.sync_api import Page
from pages.base_page import BasePage
from utilities import config

class LoginPage(BasePage):
    URL = config.GIMAIL_URL
    def __init__(self, page: Page):
        super().__init__(page)

    def click_sign_in(page: Page):
        with page.context.expect_page() as popup:
                signInButton.click()
            new_page = popup.value

    def signInButton(page: Page):
        signInButton = page.get_by_role("link", name="Sign into Gmail")



