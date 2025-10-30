import inspect
from playwright.sync_api import Page
from utils.element import Element


class PageClient:

    def __init__(self, page):
        self.PAGE: Page = page

    def sleep(self, seconds):
        self.PAGE.wait_for_timeout(seconds * 1000)
        return self

    def element(self, locator) -> Element:
        stack = inspect.stack()
        the_class = stack[1][0].f_locals["self"].__class__.__name__
        the_method = stack[1][0].f_code.co_name
        return Element(self.PAGE, f"{the_class}.{the_method}", locator)