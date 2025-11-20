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


def test_comparisions():
    candy1 = Candy("Candy1", 1.0, 2.0)  # Cost = 2.0
    candy2 = Candy("Candy2", 2.0, 1.5)  # Cost = 3.0
    candy3 = Candy("Candy3", 1.0, 2.0)  # Cost = 2.0

    assert candy1 == candy3
    assert candy1 != candy2
    assert candy1 < candy2
    assert candy2 > candy1
    assert candy1 <= candy3
    assert candy2 >= candy1



