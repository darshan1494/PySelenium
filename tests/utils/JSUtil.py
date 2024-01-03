import logging
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (ElementNotSelectableException, ElementNotVisibleException)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

'''
JSUtil is a normal function & reusable component. Rather than writing some set of code again & again 
we can create utilities so that we can use it in other functions.
'''
class JSUtils:
    #Constructor
    def __init__(self,driver): # self is basically used in class to initialise class variables.
        self.driver = driver # whenever  something is basically present inside classes, then first argument would be self.

#Utility: We can resuse these functions
    def make_alert(self,msg):
        js= self.driver.execute_script
        js("alert('"+msg+"')")

    def click_element_by_js(self,element):
        try:
            executor = self.driver.execute_script
            executor("arguments[0].click()", element)
        except Exception as e:
            raise AssertionError("Test failed with exception--->" + str(e))

    def refresh_browser_by_js(driver):
        js = driver.execute_script
        js("history.go(0)")

    def wait_for_page_load(self):
        def page_load_condition(driver):
            return self.driver.execute_script("return document.readyState") == "complete"
        wait =WebDriverWait(self.driver,5000)
        wait.until(page_load_condition)
        print("Page loaded successfully")

    def wait_for_alert(self):
        WebDriverWait(self.driver,10).until(EC.alert_is_present())

    def scroll_into_view(element , driver):
        js=driver.execute_script
        js("arguments[0].scrollIntoView(true)", element)
