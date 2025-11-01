from config import BASE_URL, INVENTORY
from utils.error import invalid_credentials, locked_user


class TestLogin:

    def test_login_with_valid_credentials(self, browser, app, logout):
        app.login.open()
        app.login.pass_the_login()
        app.login.assert_url_is(BASE_URL + INVENTORY)

    def test_login_with_invalid_username(self, app):
        app.login.open()
        app.login.pass_the_login(username="autotest")
        app.login.assert_url_is(BASE_URL)
        app.login.assert_error_text_is(invalid_credentials, app.login.error_text())

    def test_login_with_invalid_password(self, app):
        app.login.open()
        app.login.pass_the_login(password="autotest")
        app.login.assert_url_is(BASE_URL)
        app.login.assert_error_text_is(invalid_credentials, app.login.error_text())

    def test_login_as_locked_user(self, app):
        app.login.open()
        app.login.pass_the_login(username="locked_out_user")
        app.login.assert_url_is(BASE_URL)
        app.login.assert_error_text_is(locked_user, app.login.error_text())

    def test(self, app):
        app.login.all_items().click()
