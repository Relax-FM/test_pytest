import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from contextlib import nullcontext as ex_not_raise
from block_5.src.main import ApiRequest


url = 'https://www.saucedemo.com/'
driver = webdriver.Firefox()


class Test_Saucedemo:
    url = 'https://www.saucedemo.com/'


    def driver(self):
        try:
            driver = webdriver.Firefox()
            driver.get(url=self.url)
            time.sleep(0.4)
            return driver
        except Exception as ex:
            print(ex)
            driver.close()
            driver.quit()

    def login(self, driver, login, password):
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


    @pytest.mark.parametrize(
        ["login", "password"],
        [
            ("standard_user", "secret_sauce"),
            ("locked_out_user", "secret_sauce"),
            ("problem_user", "secret_sauce"),
            ("performance_glitch_user", "secret_sauce"),
            ("error_user", "secret_sauce"),
            ("visual_user", "secret_sauce")
        ]
    )
    def test_login(self, login, password):
        try:
            driver = self.driver()
            self.login(driver, login, password)
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()


    def test_log(self, log_in):
        # try:
        #     driver = self.driver()
        #
        # except Exception as ex:
        #     print(ex)
        # finally:
        #     driver.close()
        #     driver.quit()
        assert 1 == 1