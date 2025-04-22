import pytest
from utils import categorize_age

def test_categorize_age():
    assert categorize_age(10) == "Child"
    assert categorize_age(15) == "Teen"
    assert categorize_age(30) == "Adult"
    assert categorize_age(70) == "Senior"
