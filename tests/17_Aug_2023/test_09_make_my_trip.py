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

def test_09_actions():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.makemytrip.com/")

    time.sleep(6)
    fromCity = driver.find_element(By.ID, "fromCity")
    actions = ActionChains(driver)
    actions.move_to_element(fromCity).click().send_keys("New Delhi").perform()

