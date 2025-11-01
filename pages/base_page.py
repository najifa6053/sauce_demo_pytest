from selenium.webdriver.common.by import By
from helpers.utils import wait_for_visibility, safe_click

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, by, locator, timeout=15):
        return wait_for_visibility(self.driver, by, locator, timeout=timeout)

    def click(self, by, locator, timeout=15):
        return safe_click(self.driver, by, locator, timeout=timeout)

    def get_text(self, by, locator, timeout=15):
        return wait_for_visibility(self.driver, by, locator, timeout=timeout).text

    def get_current_url(self):
        return self.driver.current_url
