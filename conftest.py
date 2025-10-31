import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

SAUCE_URL = "https://www.saucedemo.com/"

@pytest.fixture(scope="session")
def browser():
    options = Options()
    if os.environ.get("HEADLESS", "false").lower() == "true":
        options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login(browser):
    from pages.login_page import LoginPage
    from pages.inventory_page import InventoryPage
    lp = LoginPage(browser, SAUCE_URL)
    lp.load()
    lp.login("standard_user", "secret_sauce")
    return InventoryPage(browser)
