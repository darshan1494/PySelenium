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

def test_05_actions():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    clickable = driver.find_element(By.ID, "clickable")
    ActionChains(driver)\
        .double_click(clickable)\
        .perform()

    time.sleep(5)