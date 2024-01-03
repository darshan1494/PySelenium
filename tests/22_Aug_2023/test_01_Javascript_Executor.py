import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture # Fixture is a method in which code can be executed and basically injects whatever it returns to the following test case functions
def driver():
    driver = webdriver.Chrome()
    yield driver # yield can be used only in case of fixtures.
    driver.quit() # Once webdriver is done with its execution, yield helps to close the browser.
    # In Fixture we can Read a File, Read from DB, Create Webdriver, set data, configurations...

@pytest.mark.usefixtures("driver")
def test_js_execute(driver):
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"
    driver.get(URL)
    js_ex = driver.execute_script
    element = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
    element.click() # This is executed by selenium webdriver.
    time.sleep(2)
    js_ex("arguments[0].click()", element) # This code is executed by Javascript executor & it is equivalent/same as below JS code. 'arguments[0]' is replaced by element found by selenium webdriver.
    #document.querySelector("button[onclick='addElement()']").click();

    btn_add = driver.find_elements(By.CLASS_NAME, "added-manually")
    print(len(btn_add))

    title = js_ex("return document.title") # This code is executed by Javascript executor & returns document name = The Internet
    print(title)

    js_ex("window.scrollBy(0,100)") # JS executor scrolls window by 100 pixels.
   # js_ex("window.scrollTo(0,document.body..scrollHeight)") # We can perform scroll to particular  height

    # btn_add = driver.find_element(By.CLASS_NAME,"added-manually")
    # time.sleep(2)

    driver.get("https://thetestingacademy.com/")
    js_ex("window.scrollBy(0,600)") # JS executor scrolls window by 600 pixels.
    time.sleep(3)