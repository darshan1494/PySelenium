from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
from selenium.common.exceptions import (ElementNotSelectableException, ElementNotVisibleException)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_web_tables():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/webtable.html")

    #ROW
    #//table[contains(@id, "cust")]/tbody/tr
    row_elements = driver.find_elements(By.XPATH, "//table[contains(@id, 'cust')]/tbody/tr")
    row = len(row_elements)
    print(row)

    #COLUMN
    # //table[contains(@id, "cust")]/tbody/tr[2]/td
    col_elements = driver.find_elements(By.XPATH, "//table[contains(@id, 'cust')]/tbody/tr[2]/td")
    col = len(col_elements)
    print(col)

    '''
    # 2 for loops should be used:
    First_part= //table[contains(@id='cust')]/tbody/tr[
    4 - i(values vary from 2 to 7)
    Second_part=]/td[
    2 - j(values vary from1 to 3)
    Third_part=]
    '''

    first_part = "//table[contains(@id='cust')]/tbody/tr["
    second_part = "]/td["
    third_part = "]"

    '''
    Prints all the elements in the static table: Facing Error
      for i in range(2, row+1): # range in python(1,10) is considered as (1,9+1))
            for j in range(1, col+1):
                dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}" # Generating all the paths by using for loop & prints all elements.
                # print(dynamic_xpath) # Once dynamic path is done, we just need to get xpath out of it.
                data = driver.find_element(By.XPATH, dynamic_path) # Just want to find the element where dynamic_xpath exists & want to get text of it.
                print(data.text, end=" ")
    '''

    #Finding one element & it's following sibling using Xpath Axes : Facing Error
    #Find Helen Bennett's whuch country this person belongs to?
    #//table[@id="customers"]/tbody/tr[5]/td[2]/following-sibling::td
    for i in range(2, row + 1):  # range in python(1,10) is considered as (1,9+1))
        for j in range(1, col + 1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"  # Generating all the paths by using for loop & prints all elements.
            data = driver.find_element(By.XPATH , dynamic_path).text
            if "Helen Bennett" in data:
                country_path =  f"{dynamic_path}/following-sibling::td"
                country_text = driver.find_element(By.XPATH,country_path).text
                print(f"Helen Bennett	is in {country_text}")





