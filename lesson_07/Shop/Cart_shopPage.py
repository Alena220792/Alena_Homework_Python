from selenium.webdriver.common.by import By

class Cart_shopPage:

    def __init__(self, driver):
        self._driver = driver

    def cart_shop(self):   
        self._driver.find_element(By.ID, "checkout").click()