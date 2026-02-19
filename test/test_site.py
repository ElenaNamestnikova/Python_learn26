from selenium.webdriver.common.by import By
import time
from pages.homepage import Homepage
from pages.product import Product

def test_open_s6(driver):
    homepage = Homepage(driver)
    homepage.open_homepage()
    homepage.click()
    product = Product(driver)
    product.check_title("Samsung galaxy s6")
    #driver.get('https://demoblaze.com/')
    #galaxy_s6 = driver.find_element(By.LINK_TEXT, "Samsung galaxy s6")
    #galaxy_s6.click()
    #title = driver.find_element(By.CSS_SELECTOR, value="h2")
    #assert title.text == "Samsung galaxy s6"

def test_two_monitors(driver):
    homepage = Homepage(driver)
    homepage.open_homepage()
    homepage.click_monitor()
    #driver.get('https://demoblaze.com/')
    #monitor_link = driver.find_element(By.CSS_SELECTOR, value="[onclick=\"byCat('monitor')\"]")
    #monitor_link.click()
    time.sleep(5)
    homepage.check_count(2)
    #monitors = driver.find_elements(By.CSS_SELECTOR, value='.card')
    #assert len(monitors) == 2