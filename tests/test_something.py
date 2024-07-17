from playwright.sync_api import Page


def test_foo():
    pass


def test_some_playwright(page: Page):
    page.goto('https://example.com')
