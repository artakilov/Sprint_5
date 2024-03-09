from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locators import TestLocators
import random

class TestRegistration:

    # test_010 - позитивный, успешная регистрация с корректными данными
    def test_registration_successfully(self, driver):
        driver.find_element(*TestLocators.BUTTON_LOGIN_TO_ACCOUNT).click()
        driver.find_element(*TestLocators.LINK_REGISTRATION).click()
        driver.find_element(*TestLocators.FIELD_REGISTRATION_NAME).send_keys('artem')
        (driver.find_element(*TestLocators.FIELD_REGISTRATION_EMAIL).
         send_keys(f'artemakilov6{random.randint(100, 999)}@yandex.ru'))
        driver.find_element(*TestLocators.FIELD_REGISTRATION_PASSWORD).send_keys('AAs_6789')
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOGIN)), \
            'Регистрация не выполняется!'

    # test_011 - негативный, неуспешная регистрация из-за короткого пароля
    def test_registration_not_successfully_short_password(self, driver):
        driver.find_element(*TestLocators.BUTTON_LOGIN_TO_ACCOUNT).click()
        driver.find_element(*TestLocators.LINK_REGISTRATION).click()
        driver.find_element(*TestLocators.FIELD_REGISTRATION_NAME).send_keys('artem')
        (driver.find_element(*TestLocators.FIELD_REGISTRATION_EMAIL).
         send_keys(f'artemakilov6{random.randint(100, 999)}@yandex.ru'))
        driver.find_element(*TestLocators.FIELD_REGISTRATION_PASSWORD).send_keys('AAs')
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LABEL_INCORRECT_PASSWORD)), \
            'Регистрация выполняется с некорректным паролем!'
