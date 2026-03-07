from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class UserPage:

    def __init__(self, driver) -> None:
        """
        Инициализация страницы данных пользователя.
        :param driver: WebDriver - объект драйвера Selenium.
        :return: None ничего не возвращает
        """
        with allure.step("Инициализация страницы данных пользователя"):
            self._driver = driver

    @allure.step("Заполнение формы данных покупателя")
    def user(self) -> None:
        """
        Заполняет имя, фамилию и почтовый индекс, затем нажимает Continue.
        :return: None ничего не возвращает
        """
        with allure.step("Ввести имя 'Alena'"):
            first_input = self._driver.find_element(By.ID, "first-name")
            first_input.send_keys("Alena")
        with allure.step("Ввести фамилию 'Yarushina'"):
            last_input = self._driver.find_element(By.ID, "last-name")
            last_input.send_keys("Yarushina")
        with allure.step("Ввести почтовый индекс '622588'"):
            zip_input = self._driver.find_element(By.ID, "postal-code")
            zip_input.send_keys("622588")
        with allure.step("Нажать кнопку 'Continue'"):
            self._driver.find_element(By.ID, "continue").click()

        print("Кнопки нажаты успешно!")

        
    @allure.step("Получение итоговой стоимости заказа")
    def total(self)  -> str:
        """
        Ожидает появления итоговой суммы и возвращает её текст.
        :return: str - строка с итоговой ценой заказа.
        """
        with allure.step("Ожидание появления элемента с итоговой суммой"):
            waiter = WebDriverWait(self._driver, 10)
            total_element = waiter.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        with allure.step("Считать текст итоговой стоимости с экрана"):
            total_text = total_element.text
            allure.attach(total_text, "Итоговая сумма на странице", allure.attachment_type.TEXT)
        print(f"Прочитано со страницы: {total_text}")

        return total_text