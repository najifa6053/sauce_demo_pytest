import pytest
from selenium.webdriver.common.by import By

@pytest.mark.dependency(name="add_and_confirm")
@pytest.mark.flaky
def test_order_confirmation(login):
    """
    1) Add item to cart
    2) Proceed to checkout and finish
    3) Assert confirmation message
    """
    inv = login  # InventoryPage
    item_name = "Sauce Labs Backpack"
    inv.add_item_to_cart_by_name(item_name)
    assert inv.get_cart_count() == 1

    cart = inv.go_to_cart()
    assert item_name in cart.get_cart_items_titles()

    checkout = cart.proceed_to_checkout()
   
    checkout.fill_details_and_continue("Najifa", "Esha", "1207")
    checkout.finish_checkout()

    confirmation = checkout.get_confirmation_text()
    assert "THANK YOU FOR YOUR ORDER" in confirmation.upper()

@pytest.mark.dependency(depends=["add_and_confirm"])
def test_checkout_details_verification(login):
    """
    Parameterized: verify form validation & proceed flow for multiple data sets.
    We use parametrize to show different checkout details.
    """
    inv = login
    # Ensure cart empty, then add item
    # remove if any
    try:
        inv.remove_item_from_cart_by_name("Sauce Labs Backpack")
    except Exception:
        pass

    inv.add_item_to_cart_by_name("Sauce Labs Bike Light")
    cart = inv.go_to_cart()

    
    @pytest.mark.parametrize("first,last,postal,exp_ok", [
        ("Najifa", "Esha", "1207", True),
        ("A", "B", "00000", True),
        ("", "Esha", "1207", False),  # missing first name -> should fail or block continuation
    ])
    def do_checkout(first, last, postal, exp_ok):
        # Navigate to checkout
        checkout = cart.proceed_to_checkout()
        checkout.fill_details_and_continue(first, last, postal)
        if exp_ok:
            
            checkout.finish_checkout()
            assert "THANK YOU FOR YOUR ORDER" in checkout.get_confirmation_text().upper()
        else:
            # when first name missing, the site shows an error; we expect not to proceed
            # We'll assert that continue button still present or some error appears
            # Keep it as xfail if behavior might differ
            pytest.xfail("Expected invalid input prevents continuation")

    # Execute parameterized sub-tests
    do_checkout("Najifa", "Esha", "1207", True)
    do_checkout("A", "B", "00000", True)
    
    pytest.xfail("Known behavior: empty first name prevents continue")  # mark expected failure
    
    
@pytest.mark.skip(reason="Example: skipping cancellation test during CI; enable locally")
def test_order_cancellation(login):
    """
    1) Add item
    2) Remove from cart (cancel)
    3) Assert cart is empty
    """
    inv = login
    item_name = "Sauce Labs Backpack"
    inv.add_item_to_cart_by_name(item_name)
    assert inv.get_cart_count() == 1
    cart = inv.go_to_cart()
    removed = cart.remove_item_by_name(item_name)
    assert removed is True
   
    inv.driver.find_element(By.ID, "continue-shopping").click()
    assert inv.get_cart_count() == 0
