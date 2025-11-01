from page.login import LoginPage
from page.left_sidebar import LeftSidebar


class Application:
    def __init__(self, page):
        self.login = LoginPage(page)
        self.sidebar = LeftSidebar(page)
