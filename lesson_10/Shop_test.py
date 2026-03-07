import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from AutorizPage import AutorizPage
from MainshopPage import MainshopPage
from Cart_shopPage import Cart_shopPage
from UserPage import UserPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    with allure.step("Запуск браузера Firefox"):
        options = Options()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe" 
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        driver.implicitly_wait(10)
        driver.maximize_window()
    yield driver  
    with allure.step("Закрытие браузера"):
        driver.quit()

@allure.epic("Интернет-магазин")
@allure.feature("Оформление заказа")
@allure.story("Покупка нескольких товаров")
@allure.title("Проверка полной цепочки покупки и итоговой суммы")
@allure.description("Тест проходит авторизацию, добавляет " \
                    "товары в корзину, заполняет данные и сверяет финальную стоимость")
@allure.severity("blocker")
def test_shop(driver) -> None:
    """
    Тест проверяет полный цикл оформления заказа в интернет-магазине.

    1. Авторизация под стандартным пользователем.
    2. Добавление трех товаров в корзину.
    3. Переход в корзину и заполнение данных покупателя.
    4. Проверка итоговой суммы заказа.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    :return: None — метод выполняет проверку и ничего не возвращает.
    """
    with allure.step("Авторизация в магазине"):
        autoriz_page = AutorizPage(driver)
        with allure.step("Ввод имени пользователя"):
            autoriz_page.user_input()
        with allure.step("Ввод пароля пользователя"):
            autoriz_page.login_but()
 
    with allure.step("Добавление товаров в корзину и переход в нее"):  
        main_shop = MainshopPage(driver)
        main_shop.main_shop()
    with allure.step("Переход к оформлению (Checkout)"):
        cartpage = Cart_shopPage(driver)
        cartpage.cart_shop()
    with allure.step("Ввод данных покупателя"):
        userpage = UserPage(driver)
        userpage.user()
    with allure.step("Считывание итоговой стоимости"):
        total = userpage.total()
    with allure.step(f"Проверка: ожидаемая сумма '$58.29', в корзине: '{total}'"): 
        assert "$58.29" in total