from selenium.webdriver.common.by import By


class EmailPageLocators:
    COMPOSE_BUTTON = (By.XPATH, '//*[@id="app"]/div/div[2]/div/main/div/div/nav[1]/div/div/div[1]/button/span[3]')
    NEW_EMAIL_CREATION_CARD = (By.XPATH, '//*[@id="app"]/div/div[2]/div/main/div/div/main/div[2]')
    EMAIL_INPUT_FIELD = (By.XPATH, '//*[@id="app"]/div/div[2]/div/main/div/div/main/div[2]/div[3]/div[1]/div['
                                   '1]/div/div[3]')
    EMAIL_RECIPIENT_USERNAME = (By.XPATH, "//li[contains(@class, 'search-result-item')]//div[contains(@class, "
                                          "'name') and text()='Сидоров Сергей Николаевич']")
    SUBJECT_INPUT_FIELD = [By.XPATH, '/html/body/div[1]/div/div[2]/div/main/div/div/main/div[2]/div[4]/div/div['
                                     '1]/div/div[4]/input']
    MESSAGE_INPUT_FIELD = (By.XPATH, '//*[@id="app"]/div/div[2]/div/main/div/div/main/div[2]/div[5]/div[2]/div/p')
    SEND_EMAIL_BUTTON = (By.XPATH, '//*[@id="app"]/div/div[2]/div/main/div/div/main/div[2]/div[6]/button[1]/span[3]')

    INBOX_EMAILS_FOLDER = (By.XPATH, "//*[@id='app']//li[contains(@class, 'email-filter-active')]")
    SENT_EMAILS_FOLDER = (By.XPATH, "//*[@href='/apps/email/filter/sent']")
    SENT_EMAIL = (By.CSS_SELECTOR, 'li.email-item')
    MESSAGE_BODY = (By.CSS_SELECTOR, '.mail-content-container')
    TEXT_SELECTION_MENU = (By.CLASS_NAME, 'text-selection-menu')
    CREATE_ASSIGNMENT = (By.XPATH, '//*[@id="app"]/div/div[2]/div/main/div/div/nav[2]/div/div[3]/div['
                                   '2]/button[1]')
    CREATE_TASK = (By.XPATH, '//*[@id="app"]/div/div[2]/div/main/div/div/nav[2]/div/div[3]/div[2]/button[2]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'document.querySelector("body > div.v-overlay-container > div.v-overlay--active '
                                      'button[type="submit"])')
    ASSIGNMENT_TITLE_INPUT_FIELD = (By.XPATH, '//*[@id="app-text-field-Наименование-m0ist"]')
    ASSIGNMENT_DESCRIPTION_INPUT_FIELD = (By.XPATH, "//div[contains(@class, '_editor_1kj3q_2') and contains(text(), "
                                                    "'Начните вводить текст...')]")
    STATUS_DROPDOWN = (By.CSS_SELECTOR, 'document.querySelector(".v-overlay__content._content_1jlho_1 ._body_1jlho_12 '
                                        'form div:nth-child(3) > div > div")')
    SELECTED_STATUS = (By.XPATH, "//div[@id='v-menu-123']//div[@class='v-list-item-title' and text()='На исполнении']")
    DELETE_ASSIGNED_RESPONSIBLE_USER = (By.XPATH, "//i[@aria-label='Clear']")
    RESPONSIBLE_USER_DROPDOWN = (By.CSS_SELECTOR, 'document.querySelector(".v-overlay--active form div:nth-child(5) '
                                                  '.v-input__control .v-field__append-inner > i")')

    DEADLINE_FIELD = (By.CSS_SELECTOR, 'document.querySelector("#input-133 > '
                                       'input.flat-picker-custom-style.h-100.w-100.form-control.input")')
    DEADLINE_CALENDAR = (By.CSS_SELECTOR, 'document.querySelector(".flatpickr-calendar.open .flatpickr-days '
                                          '.dayContainer")')
    FILE_UPLOADER = (By.XPATH, '//*[@id="input-133"]')
    SUBMIT_FILE_BUTTON = (By.CSS_SELECTOR, "//span[@class='v-btn__content' and text()='Выбрать']")
