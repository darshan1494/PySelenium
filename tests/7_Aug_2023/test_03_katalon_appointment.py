import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
from selenium.webdriver.support.select import Select
#from selenium.webdriver.support.ui import Select


@pytest.mark.negative
def test_katalon_appointment_negative():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    #LINK TEXT- Full match
    #PARTIAL LINK TEXT- Partial match
    driver.find_element(By.LINK_TEXT,"Make Appointment").click()

    username = driver.find_element(By.ID,"txt-username")
    username.send_keys("John Doe")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("John Doe")

    login_button = driver.find_element(By.ID, "btn-login")
    login_button.click()

    error_message = driver.find_element(By.CSS_SELECTOR, "p.lead.text-danger")
    assert "Login failed! Please ensure the username and password are valid." in error_message.text

@pytest.mark.positive
def test_katalon_appointment_positive():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    #LINK TEXT- Full match
    #PARTIAL LINK TEXT- Partial match
    driver.find_element(By.LINK_TEXT,"Make Appointment").click()

    username = driver.find_element(By.ID,"txt-username")
    username.send_keys("John Doe")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("ThisIsNotAPassword")

    login_button = driver.find_element(By.ID,"btn-login")
    login_button.click()

    dropdown = Select(driver.find_element(By.ID, "combo_facility"))
    dropdown.select_by_visible_text("Hongkong CURA Healthcare Center")

    time.sleep(5)

    driver.find_element(By.ID,"chk_hospotal_readmission").click()
    driver.find_element(By.NAME,"programs").click()

    driver.find_element(By.ID, "txt_visit_date").send_keys("01/01/2024")
    driver.find_element(By.NAME, "comment").send_keys("Need Doctor Appointment")
    driver.find_element(By.ID,"btn-book-appointment").click()

    heading_h2= driver.find_element(By.TAG_NAME, "h2")
    #LOGGER.info('title is-> ' + heading_h2)
    assert "Appointment Confirmation" in heading_h2.text








