import pytest
from dessert import Order, Cookie, IceCream, Sundae


def test_set_payment_cash():
    order = Order()
    order.payment('CASH')
    assert order.payment() == 'CASH'


def test_set_payment_card():
    order = Order()
    order.payment('CARD')
    assert order.payment() == 'CARD'


def test_set_payment_phone():
    order = Order()
    order.payment('PHONE')
    assert order.payment() == 'PHONE'


def test_set_invalid_payment_raises():
    order = Order()
    with pytest.raises(ValueError):
        order.payment('BITCOIN')


def test_get_invalid_payment_raises():
    order = Order()
    # simulate corrupted/invalid stored value (bypass setter)
    order._payment._payment_method = 'BITCOIN'
    with pytest.raises(ValueError):
        _ = order.payment()

def test_order_sort():
    order = Order()

    item1 = Cookie("Chocolate Chip", 24, 12.0, "Box")  # Cost = $24.00
    item2 = IceCream("Vanilla", 2, 2.5, "Cone")  # Cost = $5.00
    item3 = Sundae("Strawberry", 2, 3.0, "Sprinkles", 2.0, "Boat")  # Cost = $6.00 + $2.00 = $8.00

    order.add(item1)
    order.add(item2)
    order.add(item3)

    order.sort()

    sorted_costs = [item.calculate_cost() for item in order.order]
    assert sorted_costs == [5.0, 8.0, 24.0]

def test_iter():
    order = Order()

    item1 = Cookie("Chocolate Chip", 24, 12.0, "Box")
    item2 = IceCream("Vanilla", 2, 2.5, "Cone")
    item3 = Sundae("Strawberry", 2, 3.0, "Sprinkles", 2.0, "Boat")

    order.add(item1)
    order.add(item2)
    order.add(item3)

    items = list(order)
    assert items == [item1, item2, item3]

def test_next():
    order = Order()

    item1 = Cookie("Chocolate Chip", 24, 12.0, "Box")
    item2 = IceCream("Vanilla", 2, 2.5, "Cone")

    order.add(item1)
    order.add(item2)

    iterator = iter(order)

    first_item = next(iterator)
    assert first_item == item1

    second_item = next(iterator)
    assert second_item == item2

    with pytest.raises(StopIteration):
        next(iterator)