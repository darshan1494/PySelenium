import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.utils.JSUtil import JSUtils

'''
 Shadow DOM can be accessed only with the help of CSS Selector:
 If our target element is present inside #shadow-root(open) & if we find some element where shadowRoot is present just use "shadowRoot.querySelector"
 We should navigate through elements one by one as shown below step by step from parent element to target/child element using "document.querySelector" followed by ".shadowRoot.querySelector"
 
 document.querySelector("div.jackPart")
 <div id="userName" class="jackPart"></div>
 <div id="userName" class="jackPart" xpath="1"></div>
 Above 2 elements are same
 
document.querySelector("div.jackPart").shadowRoot.querySelector("a.learningHub");
<a class="learningHub" href="https://www.youtube.com/c/SelectorsHub?sub_confirmation=1" target="_blank" rel="noopener">Learning Hub</a>

document.querySelector("div.jackPart").shadowRoot.querySelector("div#app2");  We are finding 'div with classname=.jackPart' &  'div with ID=app2' using CSS Selector.
<div id="app2" qaid="country"></div>

document.querySelector("div.jackPart").shadowRoot.querySelector("div#app2").shadowRoot.querySelector("input#pizza");
<input type="text" id="pizza" placeholder="Enter pizza name">

'''

@pytest.fixture # Fixture is a method in which code can be executed and basically injects whatever it returns to the following test case functions
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver # yield can be used only in case of fixtures.
    driver.quit() # Once webdriver is done with its execution, yield helps to close the browser.
    # In Fixture we can Read a File, Read from DB, Create Webdriver, set data, configurations...

@pytest.mark.usefixtures("driver")
def test_js_execute(driver):
    URL = "https://selectorshub.com/xpath-practice-page/"
    driver.get(URL)
    div =  driver.find_element(By.XPATH, "//div[@class='jackPart']")
    driver.execute_script("arguments[0].scrollIntoView(true);", div)

    pizza = driver.execute_script("return document.querySelector('div.jackPart').shadowRoot.querySelector('div#app2').shadowRoot.querySelector('input#pizza');")
    pizza.send_keys("Farmhouse")
    # href = pizza.get_attribute("href")=To get this attribute, href="https://www.youtube.com/c/SelectorsHub?sub_confirmation=1"
    time.sleep(3)