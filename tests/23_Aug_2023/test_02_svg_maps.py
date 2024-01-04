import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture  # Fixture is a method in which code can be executed and basically injects whatever it returns to the following test case functions
def driver():
    driver = webdriver.Chrome()
    yield driver  # yield can be used only in case of fixtures.
    driver.quit()  # Once webdriver is done with its execution, yield helps to close the browser.
    # In Fixture we can Read a File, Read from DB, Create Webdriver, set data, configurations...


@pytest.mark.usefixtures("driver")
def test_svg_maps_execute(driver):
    URL = "https://www.amcharts.com/svg-maps/?map=india"
    driver.get(URL)
    driver.maximize_window()
    time.sleep(5)
    actions = ActionChains(driver)

    path_states = driver.find_elements(By.XPATH, "//*[local-name()='svg']/*[local-name()='g'][7]/*[local-name()='g']/*[local-name()='g']/*[local-name()='path']")

    # Iterating over the list using for loop:
    for state in path_states:
        state_name = state.get_attribute('aria-label')
        print(state_name)
        if state_name == "Karnataka  ":
            actions.move_to_element(state).click().perform()
            break
    time.sleep(10)







