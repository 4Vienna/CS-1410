import pytest
from dessert import Cookie,DessertItem, Candy

#Unit tests for Cookie
def test_Cookie_default():
    cookie = Cookie()
    assert cookie.name == ""
    assert cookie.number_of_cookies == 0.0
    assert cookie.price_per_dozen == 0.0
    assert cookie.packaging == "Box"

def test_Cookie_custom():
    cookie = Cookie("Generic Cookie", 12, 10.0, "Bag")
    assert cookie.name == "Generic Cookie"
    assert cookie.number_of_cookies == 12
    assert cookie.price_per_dozen == 10.0
    assert cookie.packaging == "Bag"

def test_Cookie_update():
    cookie = Cookie("Test Cookie", 6,5.0)
    cookie.name = "Updated Cookie"
    cookie.number_of_cookies = 1.5
    cookie.price_per_dozen = 4.0
    cookie.packaging = "Wrapper"
    assert cookie.name == "Updated Cookie"
    assert cookie.number_of_cookies == 1.5
    assert cookie.price_per_dozen == 4.0
    assert cookie.packaging == "Wrapper"

def test_Cookie_calculate_cost():
    cookie = Cookie("Chocolate Chip", 6, 3.99)
    assert cookie.calculate_cost() == 2.00

def test_Cookie_calculate_tax():
    cookie = Cookie("Chocolate Chip", 6, 3.99)
    assert cookie.calculate_tax() == 0.14


def test_can_combine():
    cookie1 = Cookie("Chocolate Chip", 6, 3.99)
    cookie2 = Cookie("Chocolate Chip", 12, 3.99)
    cookie3 = Cookie("Chocolate Chip", 6, 5.99)
    cookie4 = Cookie("Oatmeal Raisin", 6, 3.99)
    candy = Candy("Chocolate Chip", 1.0, 3.99)
    assert cookie1.can_combine(cookie2) == True
    assert cookie1.can_combine(cookie3) == False
    assert cookie1.can_combine(cookie4) == False
    assert cookie1.can_combine(candy) == False


def test_combine():
    cookie1 = Cookie("Chocolate Chip", 6, 3.99)
    cookie2 = Cookie("Chocolate Chip", 12, 3.99)
    combined_cookie = cookie1.combine(cookie2)
    assert combined_cookie.number_of_cookies == 18

    candy = Candy("Gummy Bears", 1.0, 2.0)
    with pytest.raises(ValueError):
        cookie1.combine(candy)