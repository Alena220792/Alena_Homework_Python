from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/inputs")

search_locator = '[type="number"]'
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("Sky")
sleep(5)
search_input.clear() 
search_input.send_keys("Pro")


sleep(2)


driver.quit()