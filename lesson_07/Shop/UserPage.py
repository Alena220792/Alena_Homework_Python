from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserPage:

    def __init__(self, driver):
        self._driver = driver

    def user(self):
        first_input = self._driver.find_element(By.ID, "first-name")
        first_input.send_keys("Alena")
        last_input = self._driver.find_element(By.ID, "last-name")
        last_input.send_keys("Yarushina")
        zip_input = self._driver.find_element(By.ID, "postal-code")
        zip_input.send_keys("622588")
        self._driver.find_element(By.ID, "continue").click()

        print("Кнопки нажаты успешно!")

        
    
    def total(self):
        waiter = WebDriverWait(self._driver, 10)
        total_element = waiter.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
        total_text = total_element.text
        print(f"Прочитано со страницы: {total_text}")

        return total_text