import logging

import  pytest
from selenium import webdriver

@pytest.fixture() # marked as a fixture inorder to pass/send driver to the below function.
def driver():
    driver = webdriver.Chrome()
    yield driver # yield is almost similar to return keyword. But it will be available untill current function is running. After which it's not available. It is better for memory management. Instead of storing values, we can directly return them
    #return driver - Value will be stored permanently & also extra varaiable

def test_open_url_verify_title(driver):
    LOGGER = logging.getLogger(__name__)
    driver.get("https://app.vwo.com")
    print(driver.title)
    LOGGER.info('This is information logs')
    LOGGER.warning('This is Warning logs')
    LOGGER.error('This is Error logs')
    LOGGER.critical('This is Critical logs')
    assert "Login - VWO" == driver.title
    #Assertion= Verification Expected v/s Actual Result


