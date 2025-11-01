from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from helpers.utils import wait_for_visibility
from selenium.common.exceptions import NoSuchElementException

class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BTN = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def __init__(self, driver):
        super().__init__(driver)
        wait_for_visibility(self.driver, *self.CART_ITEMS, timeout=10)

    def get_cart_items(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        results = []
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
            
            results.append({"name": name, "price": price, "element": item})
        return results

    def get_item_details_by_name(self, name):
        items = self.get_cart_items()
        for i in items:
            if i["name"].strip().lower() == name.strip().lower():
                return i
        raise NoSuchElementException(f"Cart item '{name}' not found")

    def remove_item_by_name(self, name):
        items = self.driver.find_elements(*self.CART_ITEMS)
        for item in items:
            title = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if title.strip().lower() == name.strip().lower():
                item.find_element(By.TAG_NAME, "button").click()
                return True
        return False

    def proceed_to_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BTN).click()
        from pages.checkout_page import CheckoutPage
        return CheckoutPage(self.driver)

    def continue_shopping(self):
        self.driver.find_element(*self.CONTINUE_SHOPPING).click()
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)
