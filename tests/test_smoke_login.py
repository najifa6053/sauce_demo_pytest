import pytest

@pytest.mark.smoke
def test_login_success(login):
    """
    Verify that login works and inventory page loads.
    """
    inv = login
    
    assert "inventory" in inv.get_current_url()
    
    assert inv.get_cart_count() == 0
