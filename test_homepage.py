import pytest
from pageobjects.homepage import HomePage
from test.basetest import BaseTest
from config.config import TestData
import time

class TestHomePage(BaseTest):
   
    def test_ProductSearch_NoFitment(self):
        self.obj = HomePage(self.driver)
        self.TD = TestData()
        word = self.TD.SEARCH_KEY
        self.obj.product_Search(word)

    def test_Vehicle_Fitment(self):
        self.obj = HomePage(self.driver)
        arg1 = 0
        arg2 = 2
        arg3 = 3
        arg4 = 0
        arg5 = 2
        self.obj.fitment_Search(arg1, arg2, arg3, arg4, arg5)