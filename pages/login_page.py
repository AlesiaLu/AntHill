#  method to create a Login-Page object
# contains all basic methods to run on this page
# ! we should provide browser and URL as parameters when creating an instance of that class
# import time

from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def enter_email(self, email):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        self.clear_text_field(email_field)
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        self.clear_text_field(password_field)
        password_field.send_keys(password)

    def submit_login(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).submit()

    # def login(self, login_credentials):
    #     email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
    #     password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
    #     time.sleep(2)
    #     for login in login_credentials.keys():  # method keys() is used to retrieve all keys from some dictionary
    #         #  where key - is email, and value - password for login
    #         self.clear_text_field(email_field)
    #         email_field.send_keys(login)  # to type key - email
    #         self.clear_text_field(password_field)
    #         password_field.send_keys(login_credentials[login])  # to type value of the key - password
    #         time.sleep(2)
    #     login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
    #     time.sleep(2)
    #     login_button.submit()

    # # navigate to...
    # def navigate_to_forgot_password(self):
    #     forgot_password_link = self.browser.find_element(*LoginPageLocators.FORGOT_PASSWORD_LINK)
    #     forgot_password_link.click()
    #     time.sleep(2)
    #
    # def navigate_to_create_account(self):
    #     create_account_link = self.browser.find_element(*LoginPageLocators.CREATE_ACCOUNT_LINK)
    #     create_account_link.click()
    #
    # def navigate_to_login_with_facebook(self):
    #     facebook_button = self.browser.find_element(*LoginPageLocators.LOG_BUTTON_WITH_FACEBOOK)
    #     facebook_button.click()
    #
    # def navigate_to_login_with_google(self):
    #     facebook_button = self.browser.find_element(*LoginPageLocators.LOG_BUTTON_WITH_GOOGLE)
    #     facebook_button.click()
    #
    # def navigate_to_login_with_twitter(self):
    #     twitter_button = self.browser.find_element(*LoginPageLocators.LOG_BUTTON_WITH_TWITTER)
    #     twitter_button.click()
    #
    # def login_error_message_shown(self):
    #     login_error_messages = self.browser.find_elements(*LoginPageLocators.LOGIN_ERROR_MESSAGE)
    #     return len(login_error_messages) == 1

    # some components of the page exist:
    # def login_button_exists(self):
    #     login_buttons = self.browser.find_elements(*LoginPageLocators.LOGIN_BUTTON)
    #     return len(login_buttons) == 1

    # def create_account_link_exists(self):
    #     links = self.browser.find_elements(*LoginPageLocators.CREATE_ACCOUNT_LINK)
    #     return len(links) == 1
    #
    # def forgot_password_link_exists(self):
    #     links = self.browser.find_elements(*LoginPageLocators.FORGOT_PASSWORD_LINK)
    #     return len(links) == 1
    #
    # def login_with_facebook_exists(self):
    #     facebook_buttons = self.browser.find_elements(*LoginPageLocators.LOG_BUTTON_WITH_FACEBOOK)
    #     return len(facebook_buttons) == 1
    #
    # def login_with_google_exists(self):
    #     google_buttons = self.browser.find_elements(*LoginPageLocators.LOG_BUTTON_WITH_GOOGLE)
    #     return len(google_buttons) == 1
    #
    # def login_with_twitter_exists(self):
    #     twitter_buttons = self.browser.find_elements(*LoginPageLocators.LOG_BUTTON_WITH_TWITTER)
    #     return len(twitter_buttons) == 1

    # def remember_me_checkbox_exists(self):
    #     checkbox_elements = self.browser.find_elements(*LoginPageLocators.REMEMBER_ME_CHECKBOX)
    #     return len(checkbox_elements) == 1
    #
    # def check_remember_me(self):
    #     checkbox = self.browser.find_element(*LoginPageLocators.REMEMBER_ME_CHECKBOX)
    #     checkbox.click()
    #
    # def remember_me_checked(self):
    #     checkbox = self.browser.find_element(*LoginPageLocators.REMEMBER_ME_CHECKBOX)
    #     return checkbox.is_selected()
    #
    # def remember_me_unchecked(self):
    #     checkbox = self.browser.find_element(*LoginPageLocators.REMEMBER_ME_CHECKBOX)
    #     return (checkbox.is_selected()) is False  # method to check whether this checkbox is selected
