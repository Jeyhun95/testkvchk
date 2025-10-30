from page.base import BasePage
from page.login import LoginPage
from utils.page_client import PageClient


class Application:
    def __init__(self):
        self.login = LoginPage(BasePage)
