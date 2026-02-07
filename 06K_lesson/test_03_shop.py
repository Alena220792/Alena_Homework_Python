import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def driver():
    options = Options()
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe" # Укажи свой путь
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver  
    
    driver.quit()

def test_data_shop_form(driver):
    driver.get("https://www.saucedemo.com/")
#внести данные пользователя

    user_input = driver.find_element(By.ID, "user-name")
    user_input.send_keys("standard_user")
    pass_input = driver.find_element(By.ID, "password")
    pass_input.send_keys("secret_sauce")
    #нажать кнопку
    driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]').click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()
    driver.find_element(By.ID, "checkout").click()

    #внести данные покупателя

    first_input = driver.find_element(By.ID, "first-name")
    first_input.send_keys("Alena")
    last_input = driver.find_element(By.ID, "last-name")
    last_input.send_keys("Yarushina")
    zip_input = driver.find_element(By.ID, "postal-code")
    zip_input.send_keys("622588")

    #нажать кнопку
    driver.find_element(By.ID, "continue").click()

    print("Кнопки нажаты успешно!")

    waiter = WebDriverWait(driver, 10)
    total_element = waiter.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    
    total_text = total_element.text
    print(f"Прочитано со страницы: {total_text}")
    assert "$58.29" in total_text