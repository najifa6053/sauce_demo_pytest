from selenium.webdriver.common.by import By
from helpers.utils import wait_for_element

class CheckoutPage:
    _first_name = (By.ID, "first-name")
    _last_name = (By.ID, "last-name")
    _postal_code = (By.ID, "postal-code")
    _continue = (By.ID, "continue")
    _finish = (By.ID, "finish")
    _complete_header = (By.CLASS_NAME, "complete-header")
    _cancel = (By.ID, "cancel")

    def __init__(self, driver):
        self.driver = driver
       
    def fill_details_and_continue(self, first_name, last_name, postal_code):
        self.driver.find_element(*self._first_name).clear()
        self.driver.find_element(*self._first_name).send_keys(first_name)
        self.driver.find_element(*self._last_name).send_keys(last_name)
        self.driver.find_element(*self._postal_code).send_keys(postal_code)
        self.driver.find_element(*self._continue).click()

    def finish_checkout(self):
        self.driver.find_element(*self._finish).click()

    def get_confirmation_text(self):
        return self.driver.find_element(*self._complete_header).text

    def cancel_checkout(self):
        self.driver.find_element(*self._cancel).click()
