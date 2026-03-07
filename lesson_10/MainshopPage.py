from selenium.webdriver.common.by import By
import allure

class MainshopPage:

    def __init__(self, driver):
        with allure.step("Инициализация главной страницы магазина"):
            self._driver = driver
    
    @allure.step("Добавление товаров в корзину и переход к оформлению")
    def main_shop(self):
        with allure.step("Добавить в корзину 'Sauce Labs Backpack'"):
            self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        with allure.step("Добавить в корзину 'Sauce Labs Bolt T-Shirt'"):   
            self._driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        with allure.step("Добавить в корзину 'Sauce Labs Onesie'"):  
            self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        with allure.step("Нажать на иконку корзины"):
            self._driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()