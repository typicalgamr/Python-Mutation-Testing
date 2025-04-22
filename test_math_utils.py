import pytest
from math_utils import add, subtract, is_even

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, 1) == -2

def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False
