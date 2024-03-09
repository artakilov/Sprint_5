from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locators import TestLocators


class TestPersonalAccount:

    # test_001 - позитивный, переход в личный кабинет по клику на «Личный кабинет» (вход пользователя выполнен)
    def test_go_to_personal_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*TestLocators.FIELD_LOGIN_EMAIL).send_keys('artemakilov6789@yandex.ru')
        driver.find_element(*TestLocators.FIELD_LOGIN_PASSWORD).send_keys('AAs_6789')
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_PROFILE))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile', \
            'Переход по клику на «Личный кабинет» не выполняется!'

    # test_002 - негативный, переход в личный кабинет по клику на «Личный кабинет» (вход пользователя не выполнен)
    def test_go_to_personal_account_without_login(self, driver):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOGIN))
        assert not driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile', \
            'Переход по клику на «Личный кабинет» выполняется, даже если пользователь не выполнил вход!'

    # test_003 - позитивный, переход из личного кабинета в конструктор по клику на логотип Stellar Burgers
    def test_go_to_constructor_by_using_logo(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*TestLocators.FIELD_LOGIN_EMAIL).send_keys('artemakilov6789@yandex.ru')
        driver.find_element(*TestLocators.FIELD_LOGIN_PASSWORD).send_keys('AAs_6789')
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_PROFILE))
        driver.find_element(*TestLocators.LINK_LOGO).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', \
            'По клику на логотип Stellar Burgers переход из личного кабинета в конструтор не выполняется!'

    # test_004 - позитивный, переход из личного кабинета в конструктор по клику на "Конструктор"
    def test_go_to_constructor_by_using_constructor(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*TestLocators.FIELD_LOGIN_EMAIL).send_keys('artemakilov6789@yandex.ru')
        driver.find_element(*TestLocators.FIELD_LOGIN_PASSWORD).send_keys('AAs_6789')
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_PROFILE))
        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', \
            'По клику на "Конструктор" переход из личного кабинета в конструтор не выполняется!'

    # test_005 - позитивный, выход из личного кабинета по клику на кнопку "Выйти"
    def test_logout_by_using_button_logout(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*TestLocators.FIELD_LOGIN_EMAIL).send_keys('artemakilov6789@yandex.ru')
        driver.find_element(*TestLocators.FIELD_LOGIN_PASSWORD).send_keys('AAs_6789')
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_PROFILE))
        driver.find_element(*TestLocators.BUTTON_LOGOUT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOGIN))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', \
            'По клику на кнопку "Выйти" выход из личного кабинета не выполняется!'
