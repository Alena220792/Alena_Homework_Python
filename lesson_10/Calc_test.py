import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalcPage import CalcPage

@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    with allure.step("Запуск браузера Chrome"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(10)
        driver.maximize_window()
    yield driver  
    with allure.step("Закрытие браузера"):
        driver.quit()

@allure.epic("Калькулятор")
@allure.feature("Операции с задержкой")
@allure.story("Сложение чисел")
@allure.title("Проверка медленного сложения 7 + 8")
@allure.description("Тест устанавливает задержку в 45 " \
                    "секунд, выполняет сложение и проверяет результат")
@allure.severity("blocker")
def test_calc(driver) -> None:
    """Тест проверяет работу медленного калькулятора с операцией сложения.
    1. Устанавливается задержка (45 сек). 
    2. Поочередно нажимаются кнопки '7', '+', '8', '='. 
    3. Ожидается результат '15'. 
    4. Проверяется соответствие итогового значения на экране ожиданиям.
    
    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    :return: None ничего не возвращает
    """
    with allure.step("Инициализация страницы калькулятора"):
        calc_page = CalcPage(driver)
    with allure.step("Ввод задержки (45 секунд)"):  
        calc_page.delay_input("45")
    with allure.step("Выполнение математической операции (7 + 8)"):
        calc_page.click_num()
    with allure.step("Получение итогового результата"):
        result = calc_page.result()
    with allure.step(f"Проверка: ожидаемый результат '15', получили '{result}'"):  
        assert result == "15"
        print(f"Результат: {result}")