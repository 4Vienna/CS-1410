import pytest
from dessert import DessertItem, Candy

#Unit tests for DessertItem
def test_DessertItem_default():
    dessert = Candy()
    assert dessert.name == ""

def test_DessertItem_custom():
    dessert = Candy("Generic Dessert")
    assert dessert.name == "Generic Dessert"

def test_DessertItem_update():
    dessert = Candy("Test Dessert")
    dessert.name = "Updated Dessert"
    assert dessert.name == "Updated Dessert"

def test_DessertItem_tax_percent():
    dessert = Candy()
    assert dessert.tax_percent == 7.25






