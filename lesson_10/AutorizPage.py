from selenium.webdriver.common.by import By
import allure


class AutorizPage:

    def __init__(self, driver):
        with allure.step("Открытие страницы авторизации и настройка"):
            self.driver = driver
            self.driver.get("https://www.saucedemo.com/")
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

    @allure.step("Ввод учетных данных пользователя")
    def user_input(self):
        with allure.step("Ввести логин 'standard_user'"):
            user_input = self.driver.find_element(By.ID, "user-name")
            user_input.send_keys("standard_user")
        with allure.step("Ввести пароль 'secret_sauce'"):
            pass_input = self.driver.find_element(By.ID, "password")
            pass_input.send_keys("secret_sauce")

    @allure.step("Нажатие кнопки входа (Login)")
    def login_but(self):
        with allure.step("Нажать на кнопку 'Login'"):
            self.driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]').click()