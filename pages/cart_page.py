from selenium.webdriver.common.by import By
from helpers.utils import wait_for_element

class CartPage:
    _checkout_btn = (By.ID, "checkout")
    _cart_items = (By.CLASS_NAME, "cart_item")
    _remove_button = (By.XPATH, ".//button[contains(@id,'remove')]")
    _continue_shopping = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver
        wait_for_element(self.driver, *self._cart_items)

    def get_cart_items_titles(self):
        items = self.driver.find_elements(*self._cart_items)
        titles = [i.find_element(By.CLASS_NAME, "inventory_item_name").text for i in items]
        return titles

    def remove_item_by_name(self, name):
        items = self.driver.find_elements(*self._cart_items)
        for item in items:
            title = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if title.strip().lower() == name.strip().lower():
                item.find_element(*self._remove_button).click()
                return True
        return False

    def proceed_to_checkout(self):
        self.driver.find_element(*self._checkout_btn).click()
        from pages.checkout_page import CheckoutPage
        return CheckoutPage(self.driver)
