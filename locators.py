from selenium.webdriver.common.by import By

class HomePageLocator(object):
    Search_Input = (By.CLASS_NAME, 'form-control utility-bar__search-input')
    Search_Button = (By.CLASS_NAME, 'input-group-btn')
    select_vehicle_Button = (By.CLASS_NAME, 'utility-bar__select-vehicle-button')
    select_Vehicle_text = (By.CLASS_NAME, 'utility-bar__select-vehicle-text')
    garage_Vehicle_Selection = (By.CLASS_NAME, 'garage garage-vehicle-selection')
    select_Garage_Vehicle_options = (By.CLASS_NAME, 'garage__select-vehicle-link')
    #Select_Garage_Vehicle_Links = (By.CLASS_NAME, 'btn btn-default garage__select-vehicle-link')
   
class AccessoriesPageLocator(object):
    pass

class ProductDetailsPageLocator(object):
    pass