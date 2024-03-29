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
            assert "https://www.saucedemo.com/inventory.html" in driver.current_url
        except Exception as ex:
            print(ex)
            driver.close()
            driver.quit()

    def logout(self, driver):
        try:
            driver.find_element(By.ID, 'react-burger-menu-btn').click()
            time.sleep(0.4)
            driver.find_element(By.ID, 'logout_sidebar_link').click()
            time.sleep(1)
            assert "https://www.saucedemo.com" in driver.current_url
        except Exception as ex:
            print(ex)
            driver.close()
            driver.quit()

    @pytest.mark.parametrize(
        ["login", "password"],
        [
            ("standard_user", "secret_sauce"),
            ("problem_user", "secret_sauce"),
            ("performance_glitch_user", "secret_sauce"),
            ("error_user", "secret_sauce"),
            ("visual_user", "secret_sauce")
        ]
    )
    def test_login_logout(self, login, password):
        try:
            driver = self.driver()
            self.login(driver, login, password)
            self.logout(driver)
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()

    def buy(self, driver, id):
        try:
            driver.find_element(By.ID, id).click()
            time.sleep(0.4)
            driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
            time.sleep(0.4)
            driver.find_element(By.ID, 'checkout').click()
            element = driver.find_element(By.ID, 'first-name')
            element.send_keys("Relax")
            time.sleep(0.4)
            element = driver.find_element(By.ID, 'last-name')
            element.send_keys("Fm")
            time.sleep(0.4)
            element = driver.find_element(By.ID, 'postal-code')
            element.send_keys("1234")
            time.sleep(0.4)
            driver.find_element(By.ID, 'continue').click()
            time.sleep(0.4)
            driver.find_element(By.ID, 'finish').click()
            time.sleep(0.4)
            assert "https://www.saucedemo.com/checkout-complete.html" in driver.current_url
        except Exception as ex:
            print(ex)
            driver.close()
            driver.quit()

    @pytest.mark.parametrize(
        "id",
        [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bike-light",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-fleece-jacket",
            "add-to-cart-sauce-labs-onesie",
            "add-to-cart-test.allthethings()-t-shirt-(red)",
        ]
    )
    def test_buy(self, id):
        try:
            driver = self.driver()
            self.login(driver, "standard_user", "secret_sauce")
            self.buy(driver, id)
            self.logout(driver)
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()