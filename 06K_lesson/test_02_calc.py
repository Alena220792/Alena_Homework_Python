import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver  
    
    driver.quit()

def test_data_calc_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
#внести данные в поля

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

        
#нажать кнопку
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()
    print("Кнопки нажаты успешно!")
    waiter = WebDriverWait(driver, 45)
    waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result == "15"
    print(f"Результат: {result}")