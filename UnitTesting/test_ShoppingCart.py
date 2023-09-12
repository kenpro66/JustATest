from unittest.mock import Mock

import pytest
from ShoppingCart import ShoppingCart
from Item_Database import ItemDatabase


@pytest.fixture
def cart():
    cart = ShoppingCart(5)
    cart.add('Apple')
    cart.add('Orange')
    cart.add('Banana')

    return cart

def test_can_add_item_to_cart(cart):
    assert cart.size() == 3

def test_item_exists_in_list(cart):
    assert 'Apple' in cart.get_items()

def test_add_more_than_max_items(cart):
    cart.add('Apple')
    cart.add('Apple')

    with pytest.raises(OverflowError):
        cart.add('Apple')

def test_can_get_total_price(cart):
    item_database = ItemDatabase()

    def mock_get_item(item: str):
        if item == 'Apple':
            return 1.0
        if item == 'Banana':
            return 1.5
        if item == 'Orange':
            return 2.0
    
    item_database.get = Mock(side_effect=mock_get_item)

    assert cart.get_total_price(item_database) == 4.5
