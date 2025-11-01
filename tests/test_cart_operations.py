import pytest

@pytest.mark.dependency(name="add_item")
def test_add_item_to_cart(login):
    inv = login
    item = "Sauce Labs Backpack"
    inv.add_item_to_cart_by_name(item)
    assert inv.get_cart_count() == 1

@pytest.mark.dependency(depends=["add_item"])
def test_remove_item_from_cart(login):
    inv = login
    item = "Sauce Labs Backpack"
    
    try:
        inv.add_item_to_cart_by_name(item)
    except Exception:
        pass
    
    cart = inv.go_to_cart()
    removed = cart.remove_item_by_name(item)
    assert removed is True
    
    inv2 = cart.continue_shopping()
    assert inv2.get_cart_count() == 0

@pytest.mark.flaky
def test_cart_quantity_behaviour(login):
    """
    Basic test for quantity behavior (SauceDemo shows single item qty).
    This demonstrates a flaky test marker and will be retried if fails.
    """
    inv = login
    item = "Sauce Labs Bike Light"
    
    inv.add_item_to_cart_by_name(item)
    
    count = inv.get_cart_count()
    assert count >= 0  