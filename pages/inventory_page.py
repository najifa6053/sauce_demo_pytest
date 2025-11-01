from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from helpers.utils import wait_for_visibility
from selenium.common.exceptions import NoSuchElementException

class InventoryPage(BasePage):
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_ICON = (By.ID, "shopping_cart_container")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        super().__init__(driver)
        
        wait_for_visibility(self.driver, *self.INVENTORY_CONTAINER)

    def find_item_element_by_name(self, item_name: str):
        items = self.driver.find_elements(*self.INVENTORY_ITEMS)
        for item in items:
            title = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if title.strip().lower() == item_name.strip().lower():
                return item
        raise NoSuchElementException(f"Item '{item_name}' not found")

    def add_item_to_cart_by_name(self, item_name: str):
        item = self.find_item_element_by_name(item_name)
        btn = item.find_element(By.TAG_NAME, "button")
        btn_text = btn.text.strip().lower()
        
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        btn.click()

    def remove_item_from_cart_by_name(self, item_name: str):
        try:
            item = self.find_item_element_by_name(item_name)
            btn = item.find_element(By.TAG_NAME, "button")
            btn.click()
            return True
        except Exception:
            return False

    def get_cart_count(self):
        try:
            badge = self.driver.find_element(*self.CART_BADGE)
            return int(badge.text)
        except Exception:
            return 0

    def go_to_cart(self):
        self.driver.find_element(*self.CART_ICON).click()
        from pages.cart_page import CartPage
        return CartPage(self.driver)

    def get_item_basic_info(self, item_name: str):
        
        item = self.find_item_element_by_name(item_name)
        name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
        desc = item.find_element(By.CLASS_NAME, "inventory_item_desc").text
        return {"name": name, "price": price, "description": desc}
