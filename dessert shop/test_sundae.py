import pytest
from dessert import Sundae, IceCream, DessertItem

#Unit tests for Sundae
def test_Sundae_default():
    sundae = Sundae()
    assert sundae.name == ""
    assert sundae.scoop_count == 0.0
    assert sundae.price_per_scoop == 0.0
    assert sundae.topping_name == ""
    assert sundae.topping_price == 0.0
    assert sundae.packaging == "Boat"

def test_Sundae_custom():
    sundae = Sundae("Generic Sundae", 12, 10.0, "Hot Fudge", 2.0, "Cup")
    assert sundae.name == "Generic Sundae"
    assert sundae.scoop_count == 12
    assert sundae.price_per_scoop == 10.0
    assert sundae.topping_name == "Hot Fudge"
    assert sundae.topping_price == 2.0
    assert sundae.packaging == "Cup"

def test_Sundae_update():
    sundae = Sundae("Test Sundae", 6,5.0, "Sprinkles", 1.0)
    sundae.name = "Updated Sundae"
    sundae.scoop_count = 1.5
    sundae.price_per_scoop = 4.0
    sundae.topping_name = "Caramel"
    sundae.topping_price = 0.25
    sundae.packaging = "Dish"
    assert sundae.name == "Updated Sundae"
    assert sundae.scoop_count == 1.5
    assert sundae.price_per_scoop == 4.0
    assert sundae.topping_name == "Caramel"
    assert sundae.topping_price == 0.25
    assert sundae.packaging == "Dish"

def test_Sundae_calculate_cost():
    sundae = Sundae("Test Sundae", 3, 2.5, "Hot Fudge", 1.5)
    assert sundae.calculate_cost() == 9.00


def test_Sundae_calculate_tax():
    sundae = Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
    assert sundae.calculate_tax() == 0.24