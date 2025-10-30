from page.base import BasePage


class LoginPage(BasePage):

    def username_field(self):
        return self.element("[name='username']")

    def password_field(self):
        return self.element("[name='password']")

    def login_button(self):
        return self.element("[type='submit']")

    def pass_the_login(self):
        self.username_field().fill("Admin")
        self.password_field().fill("admin123")
        self.login_button().click()