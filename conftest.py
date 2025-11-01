import os
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

SAUCE_URL = "https://www.saucedemo.com/"

@pytest.fixture(scope="session")
def browser():
    options = Options()
    
    if os.environ.get("HEADLESS", "false").lower() == "true":
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)  
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login(browser):
    
    from pages.login_page import LoginPage
    from pages.inventory_page import InventoryPage
    lp = LoginPage(browser)
    lp.load()
    lp.login("standard_user", "secret_sauce")
    
    return InventoryPage(browser)

@pytest.fixture
def add_product_to_cart(login):
    
    default_item = "Sauce Labs Backpack"
    inv = login
    inv.add_item_to_cart_by_name(default_item)
    return inv.get_item_basic_info(default_item)

@pytest.fixture(autouse=False)
def clean_cart(browser):
    
    yield
    
    try:
        from pages.inventory_page import InventoryPage
        inv = InventoryPage(browser)
        
        items = browser.find_elements(By.CLASS_NAME, "inventory_item")
        for item in items:
            btn = item.find_element(By.TAG_NAME, "button")
            if btn.text.strip().lower() == "remove":
                btn.click()
    except Exception:
        pass


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browser")
        if driver:
            screenshot_path = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_path, exist_ok=True)
            file = os.path.join(screenshot_path, f"{item.name}.png")
            driver.save_screenshot(file)
            
            try:
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.image(file))
                rep.extra = extra
            except Exception:
                pass
