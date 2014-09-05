#Contains page objects from the home page and other pages.
from base_page_object import BasePage
from login_page_objects import LoginPage
from nav_page_objects import NavPage


class HomePage(BasePage):
    url = "http://ontapstaging.herokuapp.com"

    #Login page object
    def get_login_form(self):
        return LoginPage(self.driver)

    def get_nav_links(self):
        return NavPage(self.driver)

    def has_error_message(self):
        if len(self.get_errors_by_class('alert-danger')) > 0:
            return True
        else:
            return False