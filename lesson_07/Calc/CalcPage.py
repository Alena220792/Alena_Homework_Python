from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def delay_input(self, term):
    
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(term)

    def click_num(self):
    #нажать кнопку
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()
        print("Кнопки нажаты успешно!")
        waiter = WebDriverWait(self.driver, 45)
        waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

   
    def result(self):
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return result