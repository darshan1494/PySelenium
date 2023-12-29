from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
from selenium.common.exceptions import (ElementNotSelectableException, ElementNotVisibleException)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

def test_checkbox():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    checkboxes = driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")

    # click on checkbox-1 directly:
    # checkbox_first = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]")
    # checkbox_first.click()


    #Check the checkbox which is not selected:
    for c in checkboxes:
        if not c.is_selected():
            c.click()

    time.sleep(5)
