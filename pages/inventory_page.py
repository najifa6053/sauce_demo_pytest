# pages/inventory_page.py
from selenium.webdriver.common.by import By
from helpers.utils import wait_for_element

class InventoryPage:
    # Locators
    _inventory_items = (By.CLASS_NAME, "inventory_item")
    _add_to_cart_btn = (By.XPATH, ".//button[contains(@id,'add-to-cart')]")
    _remove_btn = (By.XPATH, ".//button[contains(@id,'remove')]")
    _cart_icon = (By.ID, "shopping_cart_container")
    _cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver
        # ensure page loaded
        wait_for_element(self.driver, *self._inventory_items)

    def add_item_to_cart_by_name(self, item_name):
        items = self.driver.find_elements(*self._inventory_items)
        for item in items:
            title = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if title.strip().lower() == item_name.strip().lower():
                add_btn = item.find_element(*self._add_to_cart_btn)
                add_btn.click()
                return True
        raise ValueError(f"Item '{item_name}' not found on inventory page")

    def remove_item_from_cart_by_name(self, item_name):
        items = self.driver.find_elements(*self._inventory_items)
        for item in items:
            title = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if title.strip().lower() == item_name.strip().lower():
                rem_btn = item.find_element(*self._remove_btn)
                rem_btn.click()
                return True
        return False

    def go_to_cart(self):
        self.driver.find_element(*self._cart_icon).click()
        from pages.cart_page import CartPage
        return CartPage(self.driver)

    def get_cart_count(self):
        try:
            badge = self.driver.find_element(*self._cart_badge)
            return int(badge.text)
        except Exception:
            return 0
