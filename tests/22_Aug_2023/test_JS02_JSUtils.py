import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.utils.JSUtil import JSUtils

@pytest.fixture # Fixture is a method in which code can be executed and basically injects whatever it returns to the following test case functions
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver # yield can be used only in case of fixtures.
    driver.quit() # Once webdriver is done with its execution, yield helps to close the browser.
    # In Fixture we can Read a File, Read from DB, Create Webdriver, set data, configurations...

@pytest.mark.usefixtures("driver")
def test_js_execute(driver):
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"
    driver.get(URL)
    js_utils = JSUtils(driver)
    js_utils.make_alert("Hello")

    element = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
    js_utils.click_element_by_js(element)


    time.sleep(5)