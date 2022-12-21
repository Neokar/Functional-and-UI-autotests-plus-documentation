import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import *


def test_registration_page_all_elements_are_visible():
    """Проверка, что все элементы видны на странице регистрации"""
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_REGISTRATION_BUTTON)).click()
    assert wait.until(EC.visibility_of_element_located(AUTHORIZATION_PAGE_RIGHT_SIDE))
    assert wait.until(EC.visibility_of_element_located(AUTHORIZATION_PAGE_LEFT_SIDE))
    assert wait.until(EC.visibility_of_element_located(REGISTRATION_FIRSTNAME_FIELD))
    assert wait.until(EC.visibility_of_element_located(REGISTRATION_LASTNAME_FIELD))
    assert wait.until(EC.visibility_of_element_located(REGISTRATION_REGION_CHOICE))
    assert wait.until(EC.visibility_of_element_located(REGISTRATION_EMAIL_OR_PHONE_FIELD))
    assert wait.until(EC.visibility_of_element_located(REGISTRATION_PASSWORD_FIELD))
    assert wait.until(EC.visibility_of_element_located(REGISTRATION_PASSWORD_CONFIRM_FIELD))
    assert wait.until(EC.visibility_of_element_located(REGISTRATION_REGISTRATION_BUTTON))
    assert wait.until(EC.visibility_of_element_located(REGISTRATION_AGREEMENT_LINK))
    # try:
    #     assert wait.until(EC.visibility_of_element_located(AUTHORIZATION_SLOGAN))
    #     assert wait.until(EC.visibility_of_element_located(AUTHORIZATION_LOGO))
    # except TimeoutException:
    #     raise AssertionError("Elements are not found")
    # driver.quit()


def test_successful_redirection_to_email_confirm():
    """Проверка, что пользователь попадает на страницу подтверждения email"""
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_REGISTRATION_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(REGISTRATION_FIRSTNAME_FIELD)).send_keys("Петр")
    wait.until(EC.visibility_of_element_located(REGISTRATION_LASTNAME_FIELD)).send_keys("Петров")
    wait.until(EC.visibility_of_element_located(REGISTRATION_EMAIL_OR_PHONE_FIELD)).send_keys("test465783ab@mail.ru")
    wait.until(EC.visibility_of_element_located(REGISTRATION_PASSWORD_FIELD)).send_keys("Q123456q!!!")
    wait.until(EC.visibility_of_element_located(REGISTRATION_PASSWORD_CONFIRM_FIELD)).send_keys("Q123456q!!!")
    wait.until(EC.visibility_of_element_located(REGISTRATION_REGISTRATION_BUTTON)).click()
    assert wait.until(EC.visibility_of_element_located(CONFIRM_TITLE)).text == "Подтверждение email"
    driver.quit()


def test_failed_registration_with_same_email():
    """Проверка, что пользователь не сможет создать второй аккаунт на один email"""
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_REGISTRATION_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(REGISTRATION_FIRSTNAME_FIELD)).send_keys("Петр")
    wait.until(EC.visibility_of_element_located(REGISTRATION_LASTNAME_FIELD)).send_keys("Петров")
    wait.until(EC.visibility_of_element_located(REGISTRATION_EMAIL_OR_PHONE_FIELD)).send_keys("wowoff95@yandex.ru")
    wait.until(EC.visibility_of_element_located(REGISTRATION_PASSWORD_FIELD)).send_keys("Q123456q!!!")
    wait.until(EC.visibility_of_element_located(REGISTRATION_PASSWORD_CONFIRM_FIELD)).send_keys("Q123456q!!!")
    wait.until(EC.visibility_of_element_located(REGISTRATION_REGISTRATION_BUTTON)).click()
    assert wait.until(EC.visibility_of_element_located(ACCOUNT_EXISTS_TITLE)).text == "Учётная запись уже существует"
    driver.quit()


def test_account_exists_page_all_elements_are_visible():
    """Проверка, что все элементы видны на странице 'Учетная запись уже существует'"""
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_REGISTRATION_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(REGISTRATION_FIRSTNAME_FIELD)).send_keys("Петр")
    wait.until(EC.visibility_of_element_located(REGISTRATION_LASTNAME_FIELD)).send_keys("Петров")
    wait.until(EC.visibility_of_element_located(REGISTRATION_EMAIL_OR_PHONE_FIELD)).send_keys("wowoff95@yandex.ru")
    wait.until(EC.visibility_of_element_located(REGISTRATION_PASSWORD_FIELD)).send_keys("Q123456q!!!")
    wait.until(EC.visibility_of_element_located(REGISTRATION_PASSWORD_CONFIRM_FIELD)).send_keys("Q123456q!!!")
    wait.until(EC.visibility_of_element_located(REGISTRATION_REGISTRATION_BUTTON)).click()
    assert wait.until(EC.visibility_of_element_located(ACCOUNT_EXISTS_TITLE)).text == "Учётная запись уже существует"
    assert wait.until(EC.visibility_of_element_located(ACCOUNT_EXISTS_ENTER_BUTTON)).text == "Войти"
    assert wait.until(
        EC.visibility_of_element_located(ACCOUNT_EXISTS_RESTORE_PASSWORD_BUTTON)).text == "Восстановить пароль"
    driver.quit()


def test_registration_firstname_field_positive_enter():
    """Проверка, что ошибка ввода в поле Имя НЕ появляется при вводе 2х символов"""
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_REGISTRATION_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(REGISTRATION_FIRSTNAME_FIELD)).send_keys("Ян")
    wait.until(EC.visibility_of_element_located(REGISTRATION_LASTNAME_FIELD)).click()
    assert wait.until_not(EC.visibility_of_element_located(REGISTRATION_FIRSTNAME_FIELD_ERROR))
    driver.quit()


@pytest.mark.parametrize("enter", ["П", "Ппппппппппппппппппппппппппппппп", "Sofia", 12], ids=["Less than 2 symbols",
                                                                                              "More than 30 symbols",
                                                                                              "Latin symbols",
                                                                                              "Numbers"])
def test_registration_firstname_field_negative_enter(enter):
    """Проверки, что появляется ошибка в поле ввода Имя при некорректном вводе"""
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_REGISTRATION_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(REGISTRATION_FIRSTNAME_FIELD)).send_keys(enter)
    wait.until(EC.visibility_of_element_located(REGISTRATION_LASTNAME_FIELD)).click()
    assert wait.until(EC.visibility_of_element_located(
        REGISTRATION_FIRSTNAME_FIELD_ERROR)).text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    driver.quit()


def test_registration_firstname_field_negative_enter_blank():
    """Проверка, что появляется ошибка при отправке пустого поля Имя"""
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_REGISTRATION_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(REGISTRATION_FIRSTNAME_FIELD)).send_keys("")
    wait.until(EC.visibility_of_element_located(REGISTRATION_REGISTRATION_BUTTON)).click()
    assert wait.until(EC.visibility_of_element_located(
        REGISTRATION_FIRSTNAME_FIELD_ERROR)).text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    driver.quit()


def test_registration_password_field_negative_enter_less_than_8_symbols():
    """Проверка, что появляется ошибка при вводе в поле Пароль менее 8 символов"""
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_REGISTRATION_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(REGISTRATION_PASSWORD_FIELD)).send_keys(1234567)
    wait.until(EC.visibility_of_element_located(REGISTRATION_PASSWORD_CONFIRM_FIELD)).click()
    assert wait.until(EC.visibility_of_element_located(
        REGISTRATION_PASSWORD_ERROR)).text == "Длина пароля должна быть не менее 8 символов"
    driver.quit()


def test_registration_password_field_negative_enter_without_capital_letters():
    """Проверка, что появляется ошибка при отсутствии ввода в поле Пароль заглавных букв"""
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_REGISTRATION_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(REGISTRATION_PASSWORD_FIELD)).send_keys(12345678)
    wait.until(EC.visibility_of_element_located(REGISTRATION_PASSWORD_CONFIRM_FIELD)).click()
    assert wait.until(EC.visibility_of_element_located(
        REGISTRATION_PASSWORD_ERROR)).text == "Пароль должен содержать хотя бы одну заглавную букву"
    driver.quit()


def test_registration_password_field_negative_enter_with_cyrillic_letters():
    """Проверка, что появляется ошибка при вводе в поле Пароль букв кириллицы"""
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_REGISTRATION_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(REGISTRATION_PASSWORD_FIELD)).send_keys("qwe12345п")
    wait.until(EC.visibility_of_element_located(REGISTRATION_PASSWORD_CONFIRM_FIELD)).click()
    assert wait.until(EC.visibility_of_element_located(
        REGISTRATION_PASSWORD_ERROR)).text == "Пароль должен содержать только латинские буквы"
    driver.quit()


def test_registration_passwords_are_not_equal():
    """Проверка, что появляется ошибка, если пароли не совпадают"""
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_REGISTRATION_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(REGISTRATION_PASSWORD_FIELD)).send_keys("QQaa12345")
    wait.until(EC.visibility_of_element_located(REGISTRATION_PASSWORD_CONFIRM_FIELD)).send_keys("QQaa1234")
    wait.until(EC.visibility_of_element_located(REGISTRATION_REGISTRATION_BUTTON)).click()
    assert wait.until(
        EC.visibility_of_element_located(REGISTRATION_PASSWORD_CONFIRM_ERROR)).text == "Пароли не совпадают"
    driver.quit()
