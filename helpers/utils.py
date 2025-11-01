from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def wait_for_visibility(driver, by, locator, timeout=15):
    """Wait until element visible and return it."""
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, locator)))

def wait_for_clickable(driver, by, locator, timeout=15):
    """Wait until element clickable and return it."""
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, locator)))

def safe_click(driver, by, locator, timeout=15):
    el = wait_for_clickable(driver, by, locator, timeout=timeout)
    driver.execute_script("arguments[0].scrollIntoView(true);", el)
    el.click()

def element_text(driver, by, locator, timeout=15):
    el = wait_for_visibility(driver, by, locator, timeout=timeout)
    return el.text
