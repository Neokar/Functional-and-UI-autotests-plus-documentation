from selenium.webdriver.common.by import By

AUTHORIZATION_PAGE_LEFT_SIDE = (By.ID, "page-left")
AUTHORIZATION_PAGE_RIGHT_SIDE = (By.ID, "page-right")
AUTHORIZATION_TAB_MENU = (By.XPATH, "//*[@id='page-right']/div/div/div/form/div[1]/div[1]")
AUTHORIZATION_PHONE_TAB = (By.ID, "t-btn-tab-phone")
AUTHORIZATION_MAIL_TAB = (By.ID, "t-btn-tab-mail")
AUTHORIZATION_LOGIN_TAB = (By.ID, "t-btn-tab-login")
AUTHORIZATION_LS_TAB = (By.ID, "t-btn-tab-ls")
AUTHORIZATION_LOGIN_FIELD = (By.ID, "username")
AUTHORIZATION_PASSWORD_FIELD = (By.ID, "password")
AUTHORIZATION_SLOGAN = (By.CLASS_NAME, "what-is__desc")
AUTHORIZATION_ENTER_BUTTON = (By.ID, "kc-login")
AUTHORIZATION_ERROR = (By.ID, "form-error-message")
AUTHORIZATION_FORGOT_PASSWORD_BUTTON = (By.ID, "forgot_password")
AUTHORIZATION_REGISTRATION_BUTTON = (By.ID, "kc-register")
AUTHORIZATION_LOGO = (By.CLASS_NAME, "what-is-container__logo-container")


RESTORE_PASS_CAPTCHA_FIELD = (By.ID, "captcha")
RESTORE_CONTINUE_BUTTON = (By.ID, "reset")
RESTORE_BACK_BUTTON = (By.ID, "reset-back")


REGISTRATION_FIRSTNAME_FIELD = (By.NAME, "firstName")
REGISTRATION_LASTNAME_FIELD = (By.NAME, "lastName")
REGISTRATION_REGION_CHOICE = (By.XPATH, "//*[@id='page-right']/div/div/div/form/div[2]/div/div/input")
REGISTRATION_EMAIL_OR_PHONE_FIELD = (By.ID, "address")
REGISTRATION_PASSWORD_FIELD = (By.ID, "password")
REGISTRATION_PASSWORD_CONFIRM_FIELD = (By.ID, "password-confirm")
REGISTRATION_REGISTRATION_BUTTON = (By.NAME, "register")
REGISTRATION_AGREEMENT_LINK = (By.LINK_TEXT, "пользовательского соглашения")
REGISTRATION_FIRSTNAME_FIELD_ERROR = (By.XPATH, "//*[@id='page-right']/div/div/div/form/div[1]/div[1]/span")
REGISTRATION_PASSWORD_ERROR = (By.XPATH, "//*[@id='page-right']/div/div/div/form/div[4]/div[1]/span")
REGISTRATION_PASSWORD_CONFIRM_ERROR = (By.XPATH, "//*[@id='page-right']/div/div/div/form/div[4]/div[2]/span")


CONFIRM_TITLE = (By.CLASS_NAME, "card-container__title")


ACCOUNT_EXISTS_TITLE = (By.CLASS_NAME, "card-modal__title")
ACCOUNT_EXISTS_ENTER_BUTTON = (By.NAME, "gotoLogin")
ACCOUNT_EXISTS_RESTORE_PASSWORD_BUTTON = (By.ID, "reg-err-reset-pass")


ACCOUNT_USER_LASTNAME = (By.CLASS_NAME, "user-name__last-name")