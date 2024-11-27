#  file to collect all fixtures
import os
from dotenv import load_dotenv
from datetime import datetime
import pytest
from selenium import webdriver

import pages
from pages.login_page import LoginPage

load_dotenv()


@pytest.fixture(autouse=True)
def browser():
    """fixture to open Chrome browser before running tests, and to quit browser after that;
    automatically & implicitly started (by "autouse" parameter)
    for every test where this fixture is mentioned as a parameter of test"""
    browser = webdriver.Chrome()

    browser.maximize_window()
    # now = datetime.now()
    yield browser
    browser.quit()


@pytest.fixture()
def client_login(browser):
    """fixture to log in in with CLIENT TEST credentials;
       starts from opening login page and finishes on the Mail page (which is a homepage by default)"""
    login_page = pages.login_page.LoginPage(browser, os.environ["BASE_LOGIN_URL"])
    login_page.open()
    login_page.enter_email(os.environ["VALID_LOGIN_CLIENT"])
    login_page.enter_password(os.environ["VALID_LOGIN_PASSWORD"])
    login_page.submit_login()

# @pytest.fixture()
# def admin_login(browser):
#     """fixture to login in with ADMIN TEST credentials;
#        starts from opening login page and finishes on the Analytics page (which is a homepage by default)"""
#     login_page = LoginPage(browser, Links.login_page)
#     login_page.open()
#     login_page.login(TestData.valid_login_credentials_admin[0])
