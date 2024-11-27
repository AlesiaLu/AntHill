#  basic class for every page in the project
#  methods of base page will be inherited by every child class (=any page of the website that extends BasePage)
# ! we should provide browser and URL as parameters when creating an instance of that class

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys  # package to use some keys from keyboard for inputs
from selenium.webdriver.support.ui import WebDriverWait as Wait


class BasePage:
    def __init__(self, browser, url, timeout=10):  # that is a class constructor
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # by that browser will implicitly spend 10 seconds to find every

    def open(self):
        self.browser.get(self.url)  # by that we open the specific website page that implements BasePage

    @staticmethod
    def clear_text_field(element):  # method to clear any text field that has autofill
        if element:
            while element.get_attribute("value") != "":
                element.send_keys(Keys.BACK_SPACE)

    def element_is_visible(self, locator, timeout=10):
        return Wait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
