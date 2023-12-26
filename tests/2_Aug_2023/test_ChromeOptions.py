import logging
import  pytest
from selenium import webdriver

# ChromeOptions - Chrome with Extension, Window Size, Proxy, JavaScript Disabled

def test_login():
    # Creating an instance of ChromeOptions to maximize window size
    chrome_options = webdriver.ChromeOptions()

    #extension_path= "/Users/darsh/Downloads/adblocker.crx"
    chrome_options.add_argument("--start-maximized")
    #chrome_options.add_extension(extension_path)
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument("--headless=new")


    driver = webdriver.Chrome(options=chrome_options)
    # driver.maximize_window() # This function does the same thing as above function
    driver.get("https://app.vwo.com")

