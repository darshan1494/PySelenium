from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
from selenium.common.exceptions import (ElementNotSelectableException, ElementNotVisibleException)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

def test_alerts_testing():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    button = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']")
    button.click()
    time.sleep(5)
    wait  = WebDriverWait(driver,10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(3)

    result = driver.find_element(By.XPATH, "//p[@id='result']")
    print(result.text)

