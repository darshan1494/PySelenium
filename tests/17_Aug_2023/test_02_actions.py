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

def test_02_actions():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    clickable = driver.find_element(By.ID, "clickable")
    actions = ActionChains(driver)
    actions.click_and_hold(clickable).key_down(Keys.SHIFT).send_keys("darshan").key_up(Keys.SHIFT).perform()
    actions.click_and_hold(clickable).key_down(Keys.SHIFT).key_down("A").perform() #alternate way to enter text in textbox

    time.sleep(5)

