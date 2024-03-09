from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locators import TestLocators


class TestLogin:

    # test_006 - позитивный, вход по кнопке «Войти в аккаунт» на главной странице
    def test_login_by_using_button_login_to_account(self, driver):
        driver.find_element(*TestLocators.BUTTON_LOGIN_TO_ACCOUNT).click()
        driver.find_element(*TestLocators.FIELD_LOGIN_EMAIL).send_keys('artemakilov6789@yandex.ru')
        driver.find_element(*TestLocators.FIELD_LOGIN_PASSWORD).send_keys('AAs_6789')
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_CHECKOUT))
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_PROFILE))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile', \
            'Вход по кнопке «Войти в аккаунт» не выполняется!'

    # test_007 - позитивный, переход на страницу "Вход" через "Личный кабинет"
    # (авторизация проверяется в test_006)
    def test_login_by_using_link_login_in_personal_account(self, driver):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOGIN))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', \
            'Переход на страницу "Вход" через "Личный кабинет" не выполняется!'

    # test_008 - позитивный, переход на страницу "Вход" через ссылку на странице регистрации
    # (авторизация проверяется в test_006)
    def test_login_by_using_link_login_in_registration(self, driver):
        driver.find_element(*TestLocators.BUTTON_LOGIN_TO_ACCOUNT).click()
        driver.find_element(*TestLocators.LINK_REGISTRATION).click()
        driver.find_element(*TestLocators.LINK_LOGIN_IN_REGISTRATION).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOGIN))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', \
            'Переход на страницу "Вход" через ссылку на странице регистрации не выполняется!'

    # test_009 - позитивный, переход на страницу "Вход" через ссылку на странице восстановления пароля
    # (авторизация проверяется в test_006)
    def test_login_by_using_link_login_in_restore_password(self, driver):
        driver.find_element(*TestLocators.BUTTON_LOGIN_TO_ACCOUNT).click()
        driver.find_element(*TestLocators.LINK_RESTORE_PASSWORD).click()
        driver.find_element(*TestLocators.LINK_LOGIN_IN_RESTORE_PASSWORD).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOGIN))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', \
            'Переход на страницу "Вход" через ссылку на странице восстановления пароля не выполняется!'
