from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
from selenium.common.exceptions import (ElementNotSelectableException, ElementNotVisibleException)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_vwologin():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    #driver.implicitly_wait(20) # Tells Webdriver to wait for 20 seconds to load all the elements. If elements are loaded within 20 sec, then it's waste of time

    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")

    email_address_ele = driver.find_element(By.ID, "login-username")
    password_ele = driver.find_element(By.NAME, "password")
    sign_in_button_ele = driver.find_element(By.ID, "js-login-btn")

    email_address_ele.send_keys("darshants.1494@gmail.com")
    password_ele.send_keys("Admin@123")
    sign_in_button_ele.click()

    #time.sleep(5) # This basically stops python interpreter rather than Webdriver. This is not a good practice.

    # For Explicit wait -until(EC.visibility_of_element_located) pass ((By.CSS_SELECTOR,".page-heading")) as a tuple to avoid error!!!
    # page_heading_element1 = WebDriverWait(driver ,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".page-heading"),"Dashboard"))

    page_heading_element = WebDriverWait(driver ,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".page-heading")))
    assert 'Dashboard' in page_heading_element.text

    # Fluent Wait: Worked
    # ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
    # fluent_wait = WebDriverWait(driver, timeout=30, poll_frequency=5, ignored_exceptions=ignore_list)
    # element = EC.presence_of_element_located((By.CSS_SELECTOR, ".page-heading"))
    # driver.quit()
    # assert 'Dashboard' in element.text
