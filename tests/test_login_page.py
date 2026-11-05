import pytest
from pages.login_page import LoginPage
from pytest_playwright.pytest_playwright import Page


def test_sign_in_to_gmail(page: Page):
    signInPage = LoginPage(page)
    page.pause()
    signInPage.open()
    
    
