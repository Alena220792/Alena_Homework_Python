from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CalcPage:

    def __init__(self, driver):
        """
        Конструктор класса CalcPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        with allure.step("Открытие страницы калькулятора и настройка"):
            self.driver = driver
            self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
            self.driver.implicitly_wait(4)
            self.driver.maximize_window()

    @allure.step("Установка задержки {term} секунд")
    def delay_input(self, term):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param term: int — время задержки в секундах.
        """
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(term)

    @allure.step("Нажатие кнопок '7 + 8 =' и ожидание результата")
    def click_num(self):
        """
        Нажимает на несколько кнопок калькулятора по очереди.
        :param: str — текст на кнопке ( '7', '+', '=').,
        которые нужно нажать).
        """
        with allure.step("Нажатие кнопки '7'"):
            self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        with allure.step("Нажатие кнопки '+'"):
            self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        with allure.step("Нажатие кнопки '8'"):
            self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        with allure.step("Нажатие кнопки '='"):   
            self.driver.find_element(By.XPATH, "//span[text()='=']").click()
        print("Кнопки нажаты успешно!")
        with allure.step("Ожидание появления числа 15 на экране (до 45 сек)"):
            waiter = WebDriverWait(self.driver, 45)
            waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    @allure.step("Получение итогового результата с экрана")
    def result(self):
        
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return result