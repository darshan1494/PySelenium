from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

def test_vwologin():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()  # This function also maximize window as above function.
    driver.get("https://app.vwo.com")  # driver.navigate.To() is not available in Python like as it is in Java.

    # LINK TEXT- Full match
    # PARTIAL LINK TEXT- Partial match
    link  = driver.find_element(By.LINK_TEXT,"Start a free trial")
    link1  = driver.find_element(By.PARTIAL_LINK_TEXT,"free trial")
    link1.click()

    '''
    Use locators in the following preference order while performing automation. 
        ID, NAME, CLASS NAME, TAGNAME, LINKTEXT, PARTIAL LINKTEXT, CSS SELECTOR, XPATH.
        Many people say CSS SELECTOR is faster than XPATH. This statement is both TRUE/FALSE.
        This speed of execution depends on which OS & Browser is being used(Before 2GB & now min 8GB RAM is available).
        CSS SELECTOR & XPATH has thin line of difference.
        We can use any locator whichever we are comfortable with.
    '''

'''
    class By:
        Set of supported locator strategies.

        ID = "id"
        XPATH = "xpath"
        LINK_TEXT = "link text"
        PARTIAL_LINK_TEXT = "partial link text"
        NAME = "name"
        TAG_NAME = "tag name"
        CLASS_NAME = "class name"
        CSS_SELECTOR = "css selector"
'''

'''
What is XPATH and CSS SELECTOR?
->XPATH: Query language to find a tag in HTML
->CSS SELECTOR: Way to find element in HTML using CSS properties.

ID, NAME, CLASSNAME- These are Attributes
Tags - HTML based Web Elements
Link & Partial - Text of the Anchors
'''

'''
Locators Strategy:
  It should be Unique in nature.
  It should be Stable in nature and they shouldn't change every often.
  Avoid dynamic locators or class="123_6Aug2023" . This class name is getting changed day by day. 
  Based on the Browser resolution class name changes.
  Find the stable, unique locators which will survive automation scripts for the longer run.
  Stable means a Locator with only 1 webelement should be available & we are sure 100% that they will not change. 
'''