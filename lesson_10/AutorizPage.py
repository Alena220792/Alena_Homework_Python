from selenium.webdriver.common.by import By
import allure


class AutorizPage:
    
    def __init__(self, driver) -> None:
        """
        Инициализация страницы авторизации.

        :param driver: WebDriver — объект драйвера Selenium.
        :return: None — инициализирует объект и ничего не возвращает.
        """
        with allure.step("Открытие страницы авторизации и настройка"):
            self.driver = driver
            self.driver.get("https://www.saucedemo.com/")
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

    @allure.step("Ввод учетных данных пользователя")
    def user_input(self) -> None:
        """
        Вводит стандартные логин и пароль в соответствующие поля.
        :return: None ничего не возвращает
        """
        with allure.step("Ввести логин 'standard_user'"):
            user_input = self.driver.find_element(By.ID, "user-name")
            user_input.send_keys("standard_user")
        with allure.step("Ввести пароль 'secret_sauce'"):
            pass_input = self.driver.find_element(By.ID, "password")
            pass_input.send_keys("secret_sauce")

    @allure.step("Нажатие кнопки входа (Login)")
    def login_but(self) -> None:
        """
        Выполняет нажатие на кнопку входа в систему.
        :return: None ничего не возвращает
        """
        with allure.step("Нажать на кнопку 'Login'"):
            self.driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]').click()