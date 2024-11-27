import time
from pages.login_page import LoginPage
from pages.email_page import EmailPage
import allure
from allure_commons.types import AttachmentType


def test_send_email(browser, client_login):
    link = 'https://demo.anthill.su/'
    page = LoginPage(browser, link)
    page.open()
    link = 'https://demo.anthill.su/apps/email'
    page = EmailPage(browser, link)
    page.open_new_email_card()
    page.select_spec_user_for_sending_email()
    page.go_to_subject_field()
    page.type_email_message()
    page.go_to_send_email_button()
    time.sleep(3)
    browser.save_screenshot('email_successful_sent.png')
