import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture
def driver():
    edge_driver_path = r"C:\Users\Windows\Desktop\edgedriver_win64\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver  
    
    driver.quit()

def test_data_types_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
#внести данные в поля

    driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")
    driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').send_keys("") 
#нажать кнопку
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    print("Кнопка нажата успешно!")

    waiter = WebDriverWait(driver, 20)
    zip_field = waiter.until(lambda d: d.find_element(By.ID, "zip-code") 
                             if "alert-danger" in d.find_element(By.ID, "zip-code").get_attribute("class") 
                             else False)
    
    assert "alert-danger" in zip_field.get_attribute("class")

    
    green_fields = [
        "first-name", "last-name", "address", "city", 
        "country", "e-mail", "phone", "job-position", "company"
    ]

    for field_id in green_fields:
        field = waiter.until(EC.presence_of_element_located((By.ID, field_id)))
               
        assert "alert-success" in field.get_attribute("class"), f"Поле {field_id} не зеленое"