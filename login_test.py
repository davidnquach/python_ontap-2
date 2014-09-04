import re
import unittest
from home_page_objects import HomePage
from nose.tools import assert_true
from selenium import webdriver


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.good_data = [
            {'username': 'david.quach', 'password': 'asdf'}
        ]

        self.bad_data = [
            {'username': 'John', 'password': 'asdf'},
            {'username': '', 'password': '1234'},
            {'username': 'John.Smith', 'password': ''}
        ]
        self.browser = webdriver.Firefox()

    def test_user_can_login(self):
        home_page = HomePage(self.browser)
        home_page.navigate_to()
        login_form = home_page.get_login_form()
        login_form.set_username_to(self.good_data[0]['username'])
        login_form.set_password_to(self.good_data[0]['password'])
        login_form.submit()
        assert_true(re.match(".*/calendar", self.browser.current_url), "page did not load")

    def tearDown(self):
        self.browser.close()
