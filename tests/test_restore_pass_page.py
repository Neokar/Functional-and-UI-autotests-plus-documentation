from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import *


def test_restore_password_page_all_elements_are_visible():
    """Проверка, что видны все элементы на странице восстановления пароля"""
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_FORGOT_PASSWORD_BUTTON)).click()
    assert wait.until(EC.visibility_of_element_located(AUTHORIZATION_PHONE_TAB)).text == "Телефон"
    assert wait.until(EC.visibility_of_element_located(AUTHORIZATION_MAIL_TAB)).text == "Почта"
    assert wait.until(EC.visibility_of_element_located(AUTHORIZATION_LOGIN_TAB)).text == "Логин"
    assert wait.until(EC.visibility_of_element_located(AUTHORIZATION_LS_TAB)).text == "Лицевой счёт"
    assert wait.until(EC.visibility_of_element_located(AUTHORIZATION_LOGIN_FIELD))
    assert wait.until(EC.visibility_of_element_located(RESTORE_PASS_CAPTCHA_FIELD))
    assert wait.until(EC.visibility_of_element_located(RESTORE_CONTINUE_BUTTON)).text == "Продолжить"
    assert wait.until(EC.visibility_of_element_located(RESTORE_BACK_BUTTON)).text == "Вернуться назад"
    driver.quit()


def test_restore_password_without_captcha_enter():
    """Проверка, что пользователь не сможет восстановить пароль без ввода капчи"""
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_FORGOT_PASSWORD_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_MAIL_TAB)).click()
    wait.until(EC.visibility_of_element_located(AUTHORIZATION_LOGIN_FIELD)).send_keys("wowoff95@yandex.ru")
    wait.until(EC.visibility_of_element_located(RESTORE_CONTINUE_BUTTON)).click()
    assert wait.until(
        EC.visibility_of_element_located(AUTHORIZATION_ERROR)).text == "Неверный логин или текст с картинки"
    driver.quit()
