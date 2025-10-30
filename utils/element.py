from playwright.sync_api import Page


class Element:

    def __init__(self, page, name, locator):
        self.__page: Page = page
        self.__name = name
        self.__locator = locator