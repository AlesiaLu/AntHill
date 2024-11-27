from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import SUBJECT, EMAIL_TEXT, NEW_TITLE
from locators.email_page_locators import EmailPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class EmailPage(BasePage):
    def open_new_email_card(self):
        compose_button = self.browser.find_element(*EmailPageLocators.COMPOSE_BUTTON)
        compose_button.click()
        try:
            new_email_creation_card = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(EmailPageLocators.NEW_EMAIL_CREATION_CARD))
            return new_email_creation_card
        except TimeoutException:
            raise TimeoutException("New email creation card did not appear in the expected time.")

    def select_spec_user_for_sending_email(self, starting_letters="сер", recipient_name="Сидоров Сергей Николаевич"):
        """
        Selects a user (by the name provided) as a recipient of the email.
        :param:
        - 'starting_letters' - starting letters to filter the dropdown list
        - 'recipient_name' - should be a string with a full name of the recipient (e.g., "LastName FirstName")"""
        try:
            email_input_field = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(EmailPageLocators.EMAIL_INPUT_FIELD))
            WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(EmailPageLocators.EMAIL_INPUT_FIELD))
            email_input_field.click()
            actions = ActionChains(self.browser)
            actions.click(email_input_field).send_keys(starting_letters).perform()

            dropdown_recipients = WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located(EmailPageLocators.EMAIL_RECIPIENT_USERNAME))

            for recipient in dropdown_recipients:
                if recipient.text.strip() == recipient_name:
                    recipient.click()
                    return recipient

                raise NoSuchElementException(f"Recipient '{recipient_name}' not found in the dropdown.")

        except TimeoutException:
            raise TimeoutException("Dropdown didn't populate in time.")

        except Exception as e:
            raise RuntimeError(f"An error occurred while selecting a recipient: {str(e)}")

    def go_to_subject_field(self):
        subject_input_field = self.browser.find_element(*EmailPageLocators.SUBJECT_INPUT_FIELD)
        subject_input_field.send_keys(SUBJECT)

    def type_email_message(self):
        """types a message (provided) in a massage field
        :param:
        - message - should be a string"""
        message_input_field = self.browser.find_element(*EmailPageLocators.MESSAGE_INPUT_FIELD)
        message_input_field.send_keys(EMAIL_TEXT)

    def go_to_send_email_button(self):
        send_email_button = self.browser.find_element(*EmailPageLocators.SEND_EMAIL_BUTTON)
        send_email_button.click()

    # def go_to_sent_emails_folder(self):
    #     # Check the Folder Panel on the left for the Sent folder
    #     sent_emails_folder = self.browser.find_element(*EmailPageLocators.SENT_EMAILS_FOLDER)
    #     sent_emails_folder.click()
    #
    # def open_the_sent_email(self):
    #     """finds and opens previously created mail in the Sent folder"""
    #     sent_email = self.browser.find_element(*EmailPageLocators.SENT_EMAIL)
    #     sent_email.click()
    #
    # def highlight_the_specific_part_of_message(self):
    #     """highlights the specific part of text, text selection menu appears automatically"""
    #     text_element = self.browser.find_element(*EmailPageLocators.MESSAGE_BODY)
    #     action = ActionChains(self.browser)
    #     action.move_to_element(text_element).click_and_hold().move_by_offset(100, 0).release().perform()
    #     try:
    #         text_selection_menu = WebDriverWait(self.browser, 10).until(
    #             EC.visibility_of_element_located(*EmailPageLocators.TEXT_SELECTION_MENU))
    #         if not text_selection_menu.is_displayed():
    #             raise ValueError("Text selection menu is not displayed.")
    #     except TimeoutException:
    #         raise TimeoutException("Text selection menu did not appear in the expected time.")
    #
    # def create_assignment_via_button(self):
    #     """creates an assignment via button in text selection menu"""
    #     create_assignment = self.browser.find_element(*EmailPageLocators.CREATE_ASSIGNMENT)
    #     create_assignment.click()
    #
    # def change_assignment_title(self):
    #     """changes the automatically created title to a new provided one"""
    #     assignment_title_input_field = self.browser.find_element(*EmailPageLocators.ASSIGNMENT_TITLE_INPUT_FIELD)
    #     assignment_title_input_field.clear()
    #     assignment_title_input_field.send_key(NEW_TITLE)
    #
    # def type_assignment_description(self, description_assignment_text):
    #     assignment_description_input_field = self.browser.find_element(
    #         *EmailPageLocators.ASSIGNMENT_DESCRIPTION_INPUT_FIELD)
    #     assignment_description_input_field.send_key(description_assignment_text)
    #
    # def change_assignment_status(self):
    #     status_dropdown = self.browser.find_element(*EmailPageLocators.STATUS_DROPDOWN)
    #     status_dropdown.click()
    #     selected_status = self.browser.find_element(*EmailPageLocators.SELECTED_STATUS)
    #     selected_status.submit()
    #
    # def clear_responsible_user_field(self):
    #     """clears field with an automatically assigned responsible user"""
    #     delete_assigned_user = self.browser.find_element(*EmailPageLocators.DELETE_ASSIGNED_RESPONSIBLE_USER)
    #     delete_assigned_user.click()

    # def select_responsible_user(self):
    #     responsible_user_dropdown = self.browser.find_element(*EmailPageLocators.RESPONSIBLE_USER_DROPDOWN)
    #     responsible_user_dropdown.click()
    #     select_responsible_user = WebDriverWait(self.browser, 10).until(
    #         EC.element_to_be_clickable(*EmailPageLocators.)
    #     )

    # def create_assignment_from_highlighted_text(self):
    #     """creates a new assignment with automatically filled by the system fields"""
    #     submit_button = self.browser.find_element(*EmailPageLocators.SUBMIT_BUTTON)
    #     submit_button.click()
