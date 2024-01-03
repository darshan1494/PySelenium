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
    URL = "https://selectorshub.com/xpath-practice-page/"
    driver.get(URL)
    #element = driver.find_element(By.CSS_SELECTOR, "#shub71") # This is normal HTML element & we can directly interact.
    element = driver.find_element(By.ID, "pizza") # Shadow DOM is basically called as Encapsulation.This is how developer hides certain elements. They will be present on the webpage but couldn't interact with them. This element is inside Shadow DOM and for such elements XPath won't support.Alert: This element is inside shadow dom which can't be accessed through XPath, use cssSelector for it.
    js_utils = JSUtils(driver)
    js_utils.scroll_into_view(element)
    element.send_keys("Hello This is Darshan")
    time.sleep(3)