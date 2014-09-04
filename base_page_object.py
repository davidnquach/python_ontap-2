class BasePage(object):

    #intialization of BasePage object
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.timeout = timeout

    #actions
    def navigate_to(self, url=False):
        url = url or self.url
        self.driver.get(url)

    def go_back(self):
        self.driver.back()

    def go_forward(self):
        self.driver.forward()

    #lower level object actions
    def fill_form_by_id(self, form_id, value):
        elem = self.driver.find_element_by_id(form_id)
        elem.send_keys(value)

    def click_button_by_name(self, name):
        elem = self.driver.find_element_by_name(name)
        elem.click()