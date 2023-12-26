'''
Selenium handles only automation part:
Selenium is not a testing framework and it can automate only browsers.

Test case Steps:
Open the Browser
Navigate to URL
Find the Email Web-element & enter  email id= "abc@gmail.com"
Find the Password input box & enter the password=123
Click on Sign-in Button
'''


'''
Verification part/Assertion part is taken care by Pytest testing framework.
1.Verify that the dashboard is completely loaded.
2.Create a report to share with QA team , QA lead, QA Manager with the help of HTML/Allure reporting mechanism.
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

def test_vwologin():
    # Selenium API- Create Session & Creating an instance of ChromeOptions to maximize window size.

    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--start-maximized")
    # driver = webdriver.Chrome(options=chrome_options)
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window() # This function does the same thing as above function
    driver.get("https://app.vwo.com") # driver.navigate.To() is not available in Python like as it is in Java.
    email_address_ele=driver.find_element(By.ID,"login-username")
    password_ele=driver.find_element(By.NAME,"password")
    sign_in_button_ele=driver.find_element(By.ID,"js-login-btn")

    email_address_ele.send_keys("darshants.1494@gmail.com")
    password_ele.send_keys("Admin@123")
    sign_in_button_ele.click()
    #There is delay for about 2-3 seconds
    time.sleep(4)
    LOGGER.info('title is -> ' +  driver.title)
    assert "Dashboard" in driver.title

    driver.refresh()
    driver.get("https://sdet.live")
    driver.back()
    driver.forward()


'''
Email input box attributes:
<input type="email" 
class="text-input W(100%)" 
name="username" 
id="login-username" 
data-qa="hocewoqisi"> - Custom attribute-Custom controls. Custom element is created in ReactJS. It is JS library for building UI

'''

'''
How to find the elements in Selenium?
🔎 Locators in Selenium
A locator is a way of identifying an element on a web page so that it can be interacted with.
There are several different types of locators that can be used, including:
● ID: This locator type uses the unique ID attribute of an element to locate it on the
page.
● Name: This locator type uses the name attribute of an element to locate it on the
page.
● Class name: This locator type uses the class attribute of an element to locate it on
the page.
● Tag name: This locator type uses the HTML tag name of an element to locate it on
the page.
● Link text: This locator type uses the text of a link to locate it on the page.
● Partial link text: This locator type uses part of the text of a link to locate it on the
page.
● CSS selector: This locator type uses a CSS selector to locate an element on the
page.
● Xpath: This locator type uses an XPath expression to locate an element on the page.
● When writing test scripts with Selenium, you can use a combination of these locator
types to accurately and reliably locate elements on the page.


● find_element_by_id: Finds an element by its unique id attribute.
● find_element_by_name: Finds an element by its name attribute.
● find_element_by_xpath: Finds an element using an XPath expression.
● find_element_by_link_text: Finds an anchor element (a) by its visible text.
● find_element_by_partial_link_text: Finds an anchor element (a) by a partial match of
its visible text.
● find_element_by_tag_name: Finds an element by its HTML tag name (e.g., "div",
"input", "a", etc.).
● find_element_by_class_name: Finds an element by its CSS class name.
● find_element_by_css_selector: Finds an element using a CSS selector.

For multiple elements, you can use the plural versions of these functions.
● (e.g., find_elements_by_id, find_elements_by_name, etc.), which will return a list of
matching WebElement objects.
'''