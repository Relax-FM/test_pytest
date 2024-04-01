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

    def login(self, driver, login="standard_user", password="secret_sauce"):
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
            self.login(driver)
            self.buy(driver, id)
            self.logout(driver)
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()

    def add_delete(self, driver, id):
        try:
            driver.find_element(By.ID, id).click()
            basket = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
            assert int(basket) == 1
            time.sleep(0.4)
            rid = id.replace('add-to-cart', 'remove')
            driver.find_element(By.ID, rid).click()
            time.sleep(0.4)
            basket = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
            count_in_basket = basket.find_elements(By.CLASS_NAME, 'shopping_cart_badge')
            assert count_in_basket == []
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
    def test_basket_count(self, id):
        try:
            driver = self.driver()
            self.login(driver)
            self.add_delete(driver, id)
            self.logout(driver)
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()

    def sorts(self, driver, id) -> dict:
        try:
            sort_btn = driver.find_element(By.CLASS_NAME, 'product_sort_container')
            sort_btn.click()
            time.sleep(0.4)
            selected_option =sort_btn.find_element(By.CSS_SELECTOR, f'option[value=\"{id}\"]')
            selected_option.click()
            time.sleep(0.4)
            res = []
            if id in ['hilo', 'lohi']:
                items_price = []
                items_prices = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')

                for item in items_prices:
                    res.append(item.text)

            elif id in ['az', 'za']:
                items_name = []
                items_names = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')

                for item in items_names:
                    res.append(item.text)
            return res

        except Exception as ex:
            print('Проблемки :')
            print(ex)
            driver.close()
            driver.quit()

    def create_dict(self, driver, id) -> dict:
        try:
            res = []
            if id in ['hilo', 'lohi']:
                items_price = []
                items_prices = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')

                for item in items_prices:
                    res.append(item.text)

            elif id in ['az', 'za']:
                items_name = []
                items_names = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')

                for item in items_names:
                    res.append(item.text)

            if id in ['lohi', 'az']:
                res.sort()

            elif id in ['hilo', 'za']:
                res.sort(reverse=True)

        except Exception as ex:
            print(ex)
            driver.close()
            driver.quit()



    @pytest.mark.parametrize(
        "id",
        [
            "az",
            "za",
            "lohi",
            "hilo",
        ]
    )
    def test_sorts(self, id):
        try:
            driver = self.driver()
            self.login(driver)
            my_dict: dict = self.create_dict(driver, id)
            site_dict: dict = self.sorts(driver, id)
            self.logout(driver)
            for i in range(len(my_dict)):
                assert my_dict[i] == site_dict[i]
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()

    def test_locked_out_user(self):
        try:
            driver = self.driver()
            login_input = driver.find_element(By.ID, 'user-name')
            password_input = driver.find_element(By.ID, 'password')
            login_input.clear()
            password_input.clear()
            login_input.send_keys('locked_out_user')
            time.sleep(0.4)
            password_input.send_keys('secret_sauce')
            time.sleep(0.4)
            password_input.send_keys(Keys.ENTER)
            time.sleep(1)
            error = driver.find_element(By.CLASS_NAME,'error-button').text
            assert error == "Epic sadface: Sorry, this user has been locked out."
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()
