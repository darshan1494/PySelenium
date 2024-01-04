import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture # Fixture is a method in which code can be executed and basically injects whatever it returns to the following test case functions
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver # yield can be used only in case of fixtures.
    driver.quit() # Once webdriver is done with its execution, yield helps to close the browser.
    # In Fixture we can Read a File, Read from DB, Create Webdriver, set data, configurations...

@pytest.mark.usefixtures("driver")
def test_svg_execute(driver):
    URL = "https://www.flipkart.com/"
    driver.get(URL)
    time.sleep(5)

    '''
    Run this script whenever SignUp form's close button is available soon after Homepage is loaded:
    
    cross_button_close = driver.find_element(By.XPATH, "//span[@role='button']")
    #cross_button_close.click() # If it doesn't work, then use ActionChain class.
    actions = ActionChains(driver)
    actions.move_to_element(cross_button_close).click().perform()
    '''


    search_input = driver.find_element(By.NAME, "q")
    search_input.send_keys("AC")

    '''
    This is how SVG's are created and element lies in the Path
    # SVG->g->Path
    # SVG->g->g->g->Path
    '''

    search_svg_icon = driver.find_element(By.XPATH, "//*[local-name()='svg']/*[local-name()='path'] ")
    #search_svg_icon.click() # Sometimes we are not able to click on svg element directly. In this case , we should use ActionChain class
    actions = ActionChains(driver)
    actions.move_to_element(search_svg_icon).click().perform() # This is the good practice to handle SVGs.
    time.sleep(5)