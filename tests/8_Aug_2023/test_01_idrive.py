from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

def test_idrive():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.idrive360.com/enterprise/login")

    username = driver.find_element(By.ID,"username")
    username.send_keys("darshants.1494@gmail.com")

    password  = driver.find_element(By.ID, "password")
    password.send_keys("944833@Dtsasha")

    time.sleep(5)


    sign_in_button_ele = driver.find_element(By.ID, "frm - btn")
    sign_in_button_ele.click()

    time.sleep(20)
    add_button =driver.find_element(By.ID,"add-device-header-btn")
    add_button.click()
    time.sleep(3)

    download_btn = driver.find_element(By.XPATH, "//*[@id='id-card-bdy-backup-agent-win']/button")
    download_btn.click()