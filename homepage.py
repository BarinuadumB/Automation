from pageobjects.basepage import BasePage
from pageobjects.locators import HomePageLocator
from config.config import TestData
import time

class HomePage(BasePage):

    #constructor of home page class
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver.get(TestData.BASE_URL)
       
    global searchInput
    global searchButton
    global selectVehicleButton
    global selectVehicleText
    global garageVehicleSelection

    #Product search function
    def product_Search(self, searchText):
        loc = HomePageLocator()
        searchInput = loc.Search_Input 
        searchButton = loc.Search_Button  
        self.do_Send_Keys(searchInput, searchText)
        time.sleep(5)
        arr = 0
        self.do_Click(searchButton, arr)
        time.sleep(5)

    #Vehicle fitment search function
    def fitment_Search(self, param1, param2, param3, param4, param5):
        loc = HomePageLocator()
        selectVehicleButton = loc.select_vehicle_Button
        self.do_Click(selectVehicleButton, param1)
        time.sleep(5)
        garageVehicleSelection = loc.select_Garage_Vehicle_options
        self.do_Click(garageVehicleSelection, param2)
        time.sleep(5)
        self.do_Click(garageVehicleSelection, param3)
        time.sleep(5)
        self.do_Click(garageVehicleSelection, param4)
        time.sleep(5)
        self.do_Click(garageVehicleSelection, param4)
        time.sleep(10)
