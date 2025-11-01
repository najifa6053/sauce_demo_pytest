from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from helpers.utils import wait_for_visibility

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    SUMMARY_ITEMS = (By.CLASS_NAME, "cart_list")  # container
    CANCEL = (By.ID, "cancel")

    def __init__(self, driver):
        super().__init__(driver)
        
        wait_for_visibility(self.driver, *self.FIRST_NAME, timeout=10)

    def fill_details_and_continue(self, first: str, last: str, postal: str):
        self.driver.find_element(*self.FIRST_NAME).clear()
        self.driver.find_element(*self.FIRST_NAME).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.POSTAL).send_keys(postal)
        self.driver.find_element(*self.CONTINUE).click()

    def finish_checkout(self):
        self.driver.find_element(*self.FINISH).click()

    def get_confirmation_text(self):
        return self.driver.find_element(*self.COMPLETE_HEADER).text

    def cancel_checkout(self):
        self.driver.find_element(*self.CANCEL).click()

    def get_summary_products(self):
        
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        out = []
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
            out.append({"name": name, "price": price})
        return out
