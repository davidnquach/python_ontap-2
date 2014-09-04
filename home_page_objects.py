#Contains page objects from the home page and other pages.
from base_page_object import BasePage
from login_page_objects import LoginPage


class HomePage(BasePage):
    url = "http://ontapstaging.herokuapp.com"

    #Login page object
    def get_login_form(self):
        return LoginPage(self.driver)