from base_page_object import BasePage


class NavPage(BasePage):

    def logout(self):
        self.click_link_by_name('Logout')