import pytest
from dessert import Candy, DessertItem

#Unit tests for Candy
def test_Candy_default():
    candy = Candy()
    assert candy.name == ""
    assert candy.weight == 0.0
    assert candy.price_per_pound == 0.0

def test_Candy_custom():
    candy = Candy("Generic Candy", 2.0, 3.5)
    assert candy.name == "Generic Candy"
    assert candy.weight == 2.0
    assert candy.price_per_pound == 3.5

def test_Candy_update():
    candy = Candy("Test Candy", 3.0,5.0)
    candy.name = "Updated Candy"
    candy.weight = 1.5
    candy.price_per_pound = 4.0
    assert candy.name == "Updated Candy"
    assert candy.weight == 1.5
    assert candy.price_per_pound == 4.0

def test_Candy_calculate_cost():
    candy = Candy("Test Candy", 2.0, 3.0)
    assert candy.calculate_cost() == 6.0

def test_Candy_calculate_tax():
    candy = Candy("Candy Corn", 1.5, 0.25)
    assert candy.calculate_tax() == 0.03