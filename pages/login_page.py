from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from helpers.utils import wait_for_visibility

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_BANNER = (By.CSS_SELECTOR, "h3[data-test='error']")

    def load(self):
        self.driver.get(self.URL)

    def login(self, username: str, password: str):
      
        wait_for_visibility(self.driver, *self.USERNAME)
        self.driver.find_element(*self.USERNAME).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()
       