from playwright.sync_api import Page


class Element:

    def __init__(self, page, name, locator):
        self.page: Page = page
        self.name = name
        self.locator = locator

    def fill(self, value):
        self.page.fill(self.locator, value)

    def click(self):
        self.page.click(self.locator)

    def get_text(self):
        return self.page.text_content(self.locator)
