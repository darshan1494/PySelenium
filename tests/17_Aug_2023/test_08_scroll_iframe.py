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

def test_08_actions():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")

    # Scroll the page using Action_class & make sure to find iframe.
    iframe = driver.find_element(By.TAG_NAME, "iframe") # There is only 1 frame & we are using Tagname-iframe
    scroll_origin = ScrollOrigin.from_element(iframe)
   #  ActionChains(driver).scroll_to_element(iframe).perform()
    # This piece of code scrolls main page's scrollabar

    # Scroll from element with offset x,y(0, 200) co-ordinates:
    # From the iframe to 200 pixel we achieved scrolling inside iframe
    ActionChains(driver).scroll_from_origin(scroll_origin,0,200).perform()

    time.sleep(5)
