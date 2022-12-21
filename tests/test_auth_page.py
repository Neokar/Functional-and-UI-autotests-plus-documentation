import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import *



def test_auth_page_all_elements_are_visible():
    """Проверка, что все элементы видны на странице авторизации"""
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    assert wait.until(EC.visibility_of_element_located(AUTHORIZATION_PAGE_LEFT_SIDE))
    assert wait.until(EC.visibility_of_element_located(AUTHORIZATION_PAGE_RIGHT_SIDE))
    assert wait.until(EC.visibility_of_element_located(AUTHORIZATION_TAB_MENU))
    assert wait.until(EC.visibility_of_element_located(AUTHORIZATION_PHONE_TAB)).text == "Телефон"
    assert wait.until(EC.visibility_of_element_located(AUTHORIZATION_MAIL_TAB)).text == "Почта"
    assert wait.until(EC.visibility_of_element_located(AUTHORIZATION_LOGIN_TAB)).text == "Логин"
    assert wait.until(EC.visibility_of_element_located(AUTHORIZATION_LS_TAB)).text == "Лицевой счёт"
    assert wait.until(EC.visibility_of_element_located(AUTHORIZATION_LOGIN_FIELD))
    assert wait.until(EC.visibility_of_element_located(AUTHORIZATION_PASSWORD_FIELD))
    assert wait.until(EC.visibility_of_element_located(AUTHORIZATION_SLOGAN)).text == \
           "Персональный помощник в цифровом мире Ростелекома"
    driver.quit()


def test_tab_switch():
    """Проверка, что таб авторизации меняется автоматически"""
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    phone_tab = wait.until(EC.visibility_of_element_located(AUTHORIZATION_PHONE_TAB)).get_attribute("class")
    assert phone_tab == "rt-tab rt-tab--small rt-tab--active"
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_LOGIN_FIELD)).send_keys("test@mail.ru")
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_PASSWORD_FIELD)).click()
    email_tab = wait.until(EC.visibility_of_element_located(AUTHORIZATION_MAIL_TAB)).get_attribute("class")
    phone_tab = wait.until(EC.visibility_of_element_located(AUTHORIZATION_PHONE_TAB)).get_attribute("class")
    assert email_tab == "rt-tab rt-tab--small rt-tab--active"
    assert phone_tab != "rt-tab rt-tab--small rt-tab--active"
    driver.quit()


def test_successful_authorization():
    """Проверка, что пользователь может успешно авторизоваться с корректными данными"""
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_MAIL_TAB)).click()
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_LOGIN_FIELD)).click()
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_LOGIN_FIELD)).send_keys("wowoff95@yandex.ru")
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_PASSWORD_FIELD)).click()
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_PASSWORD_FIELD)).send_keys("h@U4dS7gKVAjPZ2")
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_ENTER_BUTTON)).click()
    time.sleep(5)
    assert wait.until(EC.visibility_of_element_located(ACCOUNT_USER_LASTNAME)).text == "Петров"
    driver.quit()


def test_failed_authorization_with_wrong_password():
    """Проверка, что пользователь не сможет авторизоваться с неверным паролем"""
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    grey_button = wait.until(EC.visibility_of_element_located(AUTHORIZATION_FORGOT_PASSWORD_BUTTON)).get_attribute(
        "class")
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_MAIL_TAB)).click()
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_LOGIN_FIELD)).send_keys("wowoff95@yandex.ru")
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_PASSWORD_FIELD)).send_keys("111111")
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_ENTER_BUTTON)).click()
    orange_button = wait.until(EC.visibility_of_element_located(AUTHORIZATION_FORGOT_PASSWORD_BUTTON)).get_attribute(
        "class")
    assert wait.until(EC.visibility_of_element_located(AUTHORIZATION_ERROR)).text == "Неверный логин или пароль"
    assert grey_button != orange_button
    driver.quit()


def test_failed_authorization_with_wrong_email():
    """Проверка, что пользователь не сможет авторизоваться с неверным email"""
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    grey_button = wait.until(EC.visibility_of_element_located(AUTHORIZATION_FORGOT_PASSWORD_BUTTON)).get_attribute(
        "class")
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_MAIL_TAB)).click()
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_LOGIN_FIELD)).send_keys("test1234@mail.ru")
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_PASSWORD_FIELD)).send_keys("h@U4dS7gKVAjPZ2")
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_ENTER_BUTTON)).click()
    orange_button = wait.until(EC.visibility_of_element_located(AUTHORIZATION_FORGOT_PASSWORD_BUTTON)).get_attribute(
        "class")
    assert wait.until(EC.visibility_of_element_located(AUTHORIZATION_ERROR)).text == "Неверный логин или пароль"
    assert grey_button != orange_button
    driver.quit()
