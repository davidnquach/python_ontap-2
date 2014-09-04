#Contains the page objects for the login page
from base_page_object import BasePage


class LoginPage(BasePage):
    url = "http://ontapstaging.herokuapp.com"

    #Objects for the sign in form
    def set_username_to(self, username):
        self.fill_form_by_id('login_username', username)

    def set_password_to(self, password):
        self.fill_form_by_id('login_password', password)

    def submit(self):
        self.click_button_by_name('commit')