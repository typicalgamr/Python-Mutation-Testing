import pytest
from inventory import Product, PerishableProduct
from datetime import date

def test_add_stock():
    product = Product("Laptop", 1000, 10)
    product.add_stock(5)
    assert product.quantity == 15

def test_remove_stock():
    product = Product("Laptop", 1000, 10)
    product.remove_stock(3)
    assert product.quantity == 7

def test_remove_stock_insufficient():
    product = Product("Laptop", 1000, 2)
    with pytest.raises(ValueError):
        product.remove_stock(5)

def test_get_stock_value():
    product = Product("Laptop", 1000, 10)
    assert product.get_stock_value() == 10000

def test_is_expired():
    perishable = PerishableProduct("Milk", 3, 50, expiration_date=date(2023, 10, 1))
    assert perishable.is_expired(date(2023, 10, 2)) is True
    assert perishable.is_expired(date(2023, 9, 30)) is False
