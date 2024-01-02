import logging
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder  import ActionBuilder
from selenium.common.exceptions import (ElementNotSelectableException, ElementNotVisibleException)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_03_actions():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    '''
    Click -Normal click and Action will be performed
    Click & Hold-Click but it will not release the element
    '''
    clickable = driver.find_element(By.ID, "click")
    actions = ActionChains(driver)
    actions\
        .click_and_hold(clickable)\
        .perform()

    assert "mouse_interaction.html" in driver.current_url
    time.sleep(5)



