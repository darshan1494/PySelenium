from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_idrive():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    #driver.implicitly_wait(20) # Tells Webdriver to wait for 20 seconds to load all the elements. If elements are loaded within 20 sec, then it's waste of time

    driver.maximize_window()
    driver.get("https://www.idrive360.com/enterprise/login")

    username = driver.find_element(By.ID,"username")
    username.send_keys("darshants.1494@gmail.com")

    password  = driver.find_element(By.ID, "password")
    password.send_keys("944833@Dtsasha")

    #time.sleep(5) # This basically stops python interpreter rather than Webdriver. This is not a good practice.

    #sign_in_button_ele = driver.find_element(By.ID, "frm - btn")
    #sign_in_button_ele = driver.find_element(By.CSS_SELECTOR, "#frm - btn")
    sign_in_button_ele = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#frm - btn')))
    sign_in_button_ele.click()

    #time.sleep(20)

    #add_button =driver.find_element(By.ID,"add-device-header-btn")
    #add_button = WebDriverWait(driver,15).until(EC.visibility_of_element_located(By.XPATH,"//span[normalize-space()='Add Devices']"))
    add_button = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//a[@id='add-device-header-btn']")))
    add_button.click()

    #time.sleep(3)

    download_btn = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='id-card-bdy-backup-agent-win']/button")))
    download_btn.click()

    time.sleep(100)  # Tells  Python Interpreter to halt the program for 100sec

    # We can download a file into Chrome directory
   # Install Software ->Call a bat file, sh linux.