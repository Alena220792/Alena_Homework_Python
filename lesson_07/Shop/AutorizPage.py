from selenium.webdriver.common.by import By


class AutorizPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    
    def user_input(self):
        user_input = self.driver.find_element(By.ID, "user-name")
        user_input.send_keys("standard_user")
        pass_input = self.driver.find_element(By.ID, "password")
        pass_input.send_keys("secret_sauce")

    def login_but(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]').click()