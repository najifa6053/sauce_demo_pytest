import pytest

@pytest.mark.parametrize("first,last,postal,expect_ok", [
    ("Najifa", "Esha", "1207", True),
    ("A", "B", "00000", True),
    ("", "Esha", "1207", False),  # missing first name - expected invalid
])
def test_checkout_details_verification(login, first, last, postal, expect_ok):
    inv = login
    item = "Sauce Labs Backpack"
    
    try:
        inv.remove_item_from_cart_by_name(item)
    except Exception:
        pass
    inv.add_item_to_cart_by_name(item)
    cart = inv.go_to_cart()
    
    details = cart.get_item_details_by_name(item)
    assert details["name"] == item
    assert details["price"].startswith("$")
    
    checkout = cart.proceed_to_checkout()
    checkout.fill_details_and_continue(first, last, postal)
    if expect_ok:
        checkout.finish_checkout()
        
        confirm = checkout.get_confirmation_text().upper()
        assert "THANK YOU FOR YOUR ORDER" in confirm
    else:
        
        pytest.xfail("Expected invalid input prevents continuation (known behavior).")
