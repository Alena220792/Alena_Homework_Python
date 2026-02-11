from selenium.webdriver.common.by import By

class MainshopPage:

    def __init__(self, driver):
        self._driver = driver

    def main_shop(self):
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        self._driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()