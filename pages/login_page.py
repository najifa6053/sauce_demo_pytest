from selenium.webdriver.common.by import By
from helpers.utils import wait_for_element

class LoginPage:
    URL = "https://www.saucedemo.com/"

    _username = (By.ID, "user-name")
    _password = (By.ID, "password")
    _login_btn = (By.ID, "login-button")

    def __init__(self, driver, base_url=None):
        self.driver = driver
        self.base_url = base_url or self.URL

    def load(self):
        self.driver.get(self.base_url)

    def login(self, username, password):
        wait_for_element(self.driver, *self._username)
        self.driver.find_element(*self._username).clear()
        self.driver.find_element(*self._username).send_keys(username)
        self.driver.find_element(*self._password).send_keys(password)
        self.driver.find_element(*self._login_btn).click()
