import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture()
def log_in():
    login, password = "standard_user", "secret_sauce"
    url = 'https://www.saucedemo.com/'
    driver = webdriver.Edge()
    driver.get(url=url)
    try:
        login_input = driver.find_element(By.ID, 'user-name')
        password_input = driver.find_element(By.ID, 'password')
        login_input.clear()
        password_input.clear()
        login_input.send_keys(login)
        time.sleep(0.4)
        password_input.send_keys(password)
        time.sleep(0.4)
        password_input.send_keys(Keys.ENTER)
        time.sleep(1)
    except Exception as ex:
        print(ex)
        driver.close()
        driver.quit()