import pytest
from dessert import Candy, DessertItem, Cookie

#Unit tests for Candy
def test_Candy_default():
    candy = Candy()
    assert candy.name == ""
    assert candy.weight == 0.0
    assert candy.price_per_pound == 0.0
    assert candy.packaging == "Bag"

def test_Candy_custom():
    candy = Candy("Generic Candy", 2.0, 3.5, "Paper Bag")
    assert candy.name == "Generic Candy"
    assert candy.weight == 2.0
    assert candy.price_per_pound == 3.5
    assert candy.packaging == "Paper Bag"

def test_Candy_update():
    candy = Candy("Test Candy", 3.0,5.0)
    candy.name = "Updated Candy"
    candy.weight = 1.5
    candy.price_per_pound = 4.0
    candy.packaging = "Clear Bag"
    assert candy.name == "Updated Candy"
    assert candy.weight == 1.5
    assert candy.price_per_pound == 4.0
    assert candy.packaging == "Clear Bag"

def test_Candy_calculate_cost():
    candy = Candy("Test Candy", 2.0, 3.0)
    assert candy.calculate_cost() == 6.0

def test_Candy_calculate_tax():
    candy = Candy("Candy Corn", 1.5, 0.25)
    assert candy.calculate_tax() == 0.03


def test_Candy_can_combine():
    candy1 = Candy("Lollipop", 1.0, 2.0)
    candy2 = Candy("Lollipop", 2.0, 2.0)
    candy3 = Candy("Lollipop", 1.0, 3.0)
    candy4 = Candy("Gummy Bears", 1.0, 2.0)
    cookie = Cookie("Chocolate Chip", 12, 1.5)
    assert candy1.can_combine(candy2) == True
    assert candy1.can_combine(candy3) == False
    assert candy1.can_combine(candy4) == False
    assert candy1.can_combine(cookie) == False

def test_Candy_combine():
    candy1 = Candy("Lollipop", 1.0, 2.0)
    candy2 = Candy("Lollipop", 2.0, 2.0)
    combined_candy = candy1.combine(candy2)
    assert combined_candy.weight == 3.0
    assert combined_candy.name == "Lollipop"
    assert combined_candy.price_per_pound == 2.0

    candy3 = Candy("Lollipop", 1.0, 3.0)
    with pytest.raises(ValueError):
        candy1.combine(candy3)

    cookie = Cookie("Chocolate Chip", 12, 1.5)
    with pytest.raises(ValueError):
        candy1.combine(cookie)