import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config.config import TestData


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def init_driver(request):
    service_chrome = Service(TestData.CHROME_EXECUTABLE_PATH)
    service_firefox = Service(TestData.FIREFOX_EXECUTABLE_PATH)
    if request.param == "chrome":
        driver = webdriver.Chrome(service = service_chrome)
    if request.param == "firefox":
        driver = webdriver.Firefox(service = service_firefox)
    request.cls.driver = driver
    driver.maximize_window()
   
    yield
    driver.close()