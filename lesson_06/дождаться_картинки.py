from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")


waiter = WebDriverWait(driver, 30)
all_image = waiter.until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#image-container img#landscape"))
)
all_images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
third_image = driver.find_element(By.CSS_SELECTOR, "#award")

src = third_image.get_attribute("src")

print(src)