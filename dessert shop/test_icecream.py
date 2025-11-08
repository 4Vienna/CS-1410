import pytest
from dessert import IceCream, DessertItem

#Unit tests for IceCream
def test_IceCream_default():
    icecream = IceCream()
    assert icecream.name == ""
    assert icecream.scoop_count == 0.0
    assert icecream.price_per_scoop == 0.0
    assert icecream.packaging == "Bowl"

def test_IceCream_custom():
    icecream = IceCream("Generic IceCream", 12, 10.0, "Cone")
    assert icecream.name == "Generic IceCream"
    assert icecream.scoop_count == 12
    assert icecream.price_per_scoop == 10.0
    assert icecream.packaging == "Cone"

def test_IceCream_update():
    icecream = IceCream("Test IceCream", 6,5.0)
    icecream.name = "Updated IceCream"
    icecream.scoop_count = 1.5
    icecream.price_per_scoop = 4.0
    icecream.packaging = "Cup"
    assert icecream.name == "Updated IceCream"
    assert icecream.scoop_count == 1.5
    assert icecream.price_per_scoop == 4.0
    assert icecream.packaging == "Cup"

def test_IceCream_calculate_cost():
    icecream = IceCream("Test IceCream", 3, 2.5)
    assert icecream.calculate_cost() == 7.50

def test_IceCream_calculate_tax():
    iceCream = IceCream("Pistachio", 2, .79)
    assert iceCream.calculate_tax() == 0.11