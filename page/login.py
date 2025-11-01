from page.base import BasePage


class LoginPage(BasePage):

    def username_field(self):
        return self.element("#user-name")

    def password_field(self):
        return self.element("#password")

    def login_button(self):
        return self.element("#login-button")

    def pass_the_login(self, username="standard_user", password="secret_sauce"):
        self.username_field().fill(username)
        self.password_field().fill(password)
        self.login_button().click()

    def error_text(self):
        return self.element("h3[data-test='error']").get_text()

    def all_items(self):
        return self.element("#inventory_sidebar_link")
