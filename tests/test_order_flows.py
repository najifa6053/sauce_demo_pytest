import pytest

@pytest.mark.dependency(name="order_confirm")
@pytest.mark.flaky
def test_order_confirmation(login):
    inv = login
    item = "Sauce Labs Backpack"
    inv.add_item_to_cart_by_name(item)
    assert inv.get_cart_count() == 1
    cart = inv.go_to_cart()
    
    info = cart.get_item_details_by_name(item)
    assert info["name"] == item
    assert info["price"].startswith("$")
    
    checkout = cart.proceed_to_checkout()
    checkout.fill_details_and_continue("Najifa", "Esha", "1207")
    checkout.finish_checkout()
    assert "THANK YOU FOR YOUR ORDER" in checkout.get_confirmation_text().upper()

@pytest.mark.dependency(depends=["order_confirm"])
@pytest.mark.skip(reason="Skipping cancellation test in CI; enable locally to test cancel flow")
def test_order_cancellation(login):
    inv = login
    item = "Sauce Labs Backpack"
    inv.add_item_to_cart_by_name(item)
    assert inv.get_cart_count() == 1
    cart = inv.go_to_cart()
    removed = cart.remove_item_by_name(item)
    assert removed is True
    inv2 = cart.continue_shopping()
    assert inv2.get_cart_count() == 0
