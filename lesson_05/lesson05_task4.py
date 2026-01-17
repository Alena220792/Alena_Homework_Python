from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")

search_locator = '[id="username"]'
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("tomsmith")
sleep(2)

search_locator = '[id="password"]'
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("SuperSecretPassword!")
sleep(2)
search_locator = "button.radius"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator).click()

print("You logged into a secure area!")

sleep(4)
driver.quit()