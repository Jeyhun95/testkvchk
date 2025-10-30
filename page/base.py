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
            self.sleep(5)
        return self