from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locators import TestLocators


class TestConstructor:

    # test_012 - позитивный, переход к разделу Начинки
    def test_jumps_to_sections_of_constructor_fillings(self, driver):
        driver.find_element(*TestLocators.CHAPTER_FILLINGS).click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(TestLocators.LIST_FILLINGS))
        assert driver.find_element(*TestLocators.LIST_FILLINGS).is_displayed()

    # test_013 - позитивный, переход к разделу Булки
    def test_jumps_to_sections_of_constructor_buns(self, driver):
        driver.find_element(*TestLocators.CHAPTER_FILLINGS).click()
        driver.find_element(*TestLocators.CHAPTER_BUNS).click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(TestLocators.LIST_BUNS))
        assert driver.find_element(*TestLocators.LIST_BUNS).is_displayed()

    # test_014 - позитивный, переход к разделу Соусы
    def test_jumps_to_sections_of_constructor_sauces(self, driver):
        driver.find_element(*TestLocators.CHAPTER_SAUCES).click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(TestLocators.LIST_SAUCES))
        assert driver.find_element(*TestLocators.LIST_SAUCES).is_displayed()
