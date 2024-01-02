import logging
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (ElementNotSelectableException, ElementNotVisibleException)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_01_actions():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/practice.html")

    first_name = driver.find_element(By.NAME,"firstname")
    # Before using Action class, we need to create an object of ActionChains class
    actions  = ActionChains(driver) # We need to pass "driver" into ActionChains & now instance is available
    #Send keys with Shift key
    actions\
        .key_down(Keys.SHIFT)\
        .send_keys_to_element(first_name,"the testing academy")\
        .key_up(Keys.SHIFT).perform() #Release SHIFT key up

    url = driver.find_element(By.XPATH, "//a[normalize-space()='Click here to Download File']")
    actions.context_click(url).perform()

    time.sleep(10)