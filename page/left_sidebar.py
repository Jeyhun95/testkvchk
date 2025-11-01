from page.base import BasePage


class LeftSidebar(BasePage):

    def burger_menu(self):
        return self.element("#react-burger-menu-btn")

    def all_items_button(self):
        return self.element("#inventory_sidebar_link")

    def about_button(self):
        return self.element("#about_sidebar_link")

    def logout_button(self):
        return self.element("#logout_sidebar_link")

    def reset_app_button(self):
        return self.element("#reset_sidebar_link")

    def logout(self):
        self.burger_menu().click()
        self.logout_button().click()
