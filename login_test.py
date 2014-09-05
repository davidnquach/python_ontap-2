import unittest
from home_page_objects import HomePage
from nose_parameterized import parameterized
from nose.tools import assert_regexp_matches
from selenium import webdriver


class LoginTest(unittest.TestCase):
    #Setups browser before each test
    def setUp(self):
        self.browser = webdriver.Firefox()

    #Logs out and closes browser
    def tearDown(self):
        self.browser.close()

    #Iterates to each data and
    @parameterized.expand([
        ('david.quach', 'asdf'),
        ('company.admin', 'asdf'),
        ('kevin.monro', 'asdf')
    ])
    def test_user_can_login(self, username, password):
        home_page = HomePage(self.browser)
        home_page.navigate_to()
        login_form = home_page.get_login_form()
        login_form.submit_form_with(
            username,
            password
        )
        assert_regexp_matches(self.browser.current_url, ".*/calendar", "Page did not load")
        nav_links = HomePage(self.browser).get_nav_links()
        nav_links.logout()

    #User should not be able to login with bad credentials
    @parameterized.expand([
        ('John', 'asdf'),
        ('', 'asdf'),
        ('david.quach', '')
    ])
    def test_user_should_not_be_able_to_login(self, username, password):
        home_page = HomePage(self.browser)
        home_page.navigate_to()
        login_form = home_page.get_login_form()
        login_form.submit_form_with(
            username,
            password
        )
        assert home_page.has_error_message()