from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
from selenium.common.exceptions import (ElementNotSelectableException, ElementNotVisibleException)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic_web_table():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/webtable1.html")
    #Get the table
    table = driver.find_element(By.XPATH,"//table[@summary='Sample Table']/tbody")
    row_table = table.find_elements(By.TAG_NAME,"tr") #We can use this also as an alternative option. TR is within the table. So we can use table.findelements() . This is called findelement chaining concept = //table[@summary="Sample Table"]/tbody/tr[4]/td

    for row in row_table:
        cols = row.find_elements(By.TAG_NAME, "td")
        for e in cols:
            print(e.text)