import pytest
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
    options = Options()
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe" 
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver  
    
    driver.quit()


def test_shop(driver):
    autoriz_page = AutorizPage(driver);
#внести данные пользователя
    autoriz_page.user_input()
#нажать кнопку
    autoriz_page.login_but()
#добавление товаров и переход в корзину    
    main_shop = MainshopPage(driver);
    main_shop.main_shop()
#корзина
    cartpage = Cart_shopPage(driver);
    cartpage.cart_shop()
#внести данные покупателя
    userpage = UserPage(driver);
    userpage.user()
#Прочитать со страницы итоговую стоимость
    total = userpage.total()
#Проверить  
    assert "$58.29" in total