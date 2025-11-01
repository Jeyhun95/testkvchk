import pytest
from playwright.sync_api import Browser, sync_playwright
from model.application import Application


@pytest.fixture()
def browser() -> Browser:
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=300, args=["--ignore-certificate-errors"])
    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture()
def app(browser):
    page = browser.new_page()
    app = Application(page)
    yield app


@pytest.fixture()
def logout(app):
    yield
    app.sidebar.logout()
