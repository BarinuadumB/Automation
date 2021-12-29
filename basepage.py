#from selenium import webdriver
#from selenium.common.exceptions import ErrorInResponseException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_Click(self, by_locator, arr):  
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()
        except Exception as e:
            if (e == "ElementNotInteractableException"):
                javaScript = document.getElementByClassName(by_locator)[arr].click()
                self.driver.execute_script(javaScript)
            else:
                print(e)

    def do_Send_Keys(self, by_locator, text):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).send_keys(text)
        except Exception as e:
            if (e == "ElementNotInteractableException"):
                javaScript = document.getElementById(by_locator).value = text
                self.driver.execute_script(javaScript)
            else:
                print(e)
   
    def get_element_text(self, by_locator):
        element = BasePage.do_findElement(by_locator)
        return element.text

    def is_visible(self, by_locator):
        element = BasePage.do_findElement(by_locator)
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 15).until(EC.title_is(title))
        return self.driver.title 