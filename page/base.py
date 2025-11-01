import allure
from config import BASE_URL
from utils.page_client import PageClient


class BasePage(PageClient):

    def __init__(self, page):
        super().__init__(page)
        self.url = BASE_URL

    def open(self):
        with allure.step(f"Open {self.url}"):
            self.PAGE.goto(url=self.url, wait_until="load")
            self.sleep(3)
        return self

    @property
    def current_url(self):
        return self.PAGE.evaluate("() => window.location.href")

    def assert_url_is(self, value):
        value = value if value.startswith("http") else BASE_URL + value
        assert value == self.current_url, (f"\nExpected: url is {value}"
                                           f"\nActual: url is {self.current_url}")

    def assert_error_text_is(self, expected, value):
        assert expected == value, (f"\nExpected: error text is {expected}"
                                   f"\nActual: error text is {value}")
