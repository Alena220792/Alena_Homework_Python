from selenium.webdriver.common.by import By
import allure

class Cart_shopPage:
        
    def __init__(self, driver) -> None:
        """
        Конструктор класса Cart_shopPage.

        :param driver: WebDriver — объект драйвера Selenium.
        :return: None — инициализирует объект и ничего не возвращает.
        """
        with allure.step("Инициализация страницы корзины"):
            self._driver = driver
    
    @allure.step("Переход к оформлению заказа (нажатие Checkout)")
    def cart_shop(self) -> None:  
        """
        Выполняет переход к странице оформления заказа.
        
        :return: None — метод выполняет клик и ничего не возвращает.
        """ 
        with allure.step("Поиск и нажатие кнопки 'Checkout'"):
            self._driver.find_element(By.ID, "checkout").click()