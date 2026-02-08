import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalcPage import CalcPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver  
    
    driver.quit()

def test_calc(driver):
    calc_page = CalcPage(driver);
 #внести данные в поля      
    calc_page.delay_input("45")
    calc_page.click_num()

    result = calc_page.result()
#Проверить    
    assert result == "15"
    print(f"Результат: {result}")