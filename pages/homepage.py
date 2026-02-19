from selenium.webdriver.common.by import By

class Homepage:

    def __init__(self, driver):
        self.driver = driver

    def open_homepage(self):
        self.driver.get('https://demoblaze.com/')

    def click(self ):
        galaxy_s6 = self.driver.find_element(By.LINK_TEXT, "Samsung galaxy s6")
        galaxy_s6.click()

    def click_monitor(self):
        monitor_link = self.driver.find_element(By.CSS_SELECTOR, value="[onclick=\"byCat('monitor')\"]")
        monitor_link.click()

    def check_count(self, count):
        monitors = self.driver.find_elements(By.CSS_SELECTOR, value='.card')
        assert len(monitors) == count
