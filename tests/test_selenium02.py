import  pytest
from selenium import webdriver

@pytest.fixture() # marked as a fixture inorder to pass/send driver to the below function.
def driver():
    driver = webdriver.Chrome()
    yield driver # yield is almost similar to return keyword. But it will be available untill current function is running. After which it's not available. It is better for memory management. Instead of storing values, we can directly return them
    #return driver - Value will be stored permanently & also extra varaiable

def test_open_url_verify_title(driver):
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert "Login - VWO" == driver.title
    #Assertion= Verification Expected v/s Actual Result


