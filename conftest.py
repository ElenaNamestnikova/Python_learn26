import pytest
from selenium import webdriver

@pytest.fixture()
def driver(request):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver
    driver.close()