import pytest
from dessert import Order


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
    # Add items with varying costs
    class DummyDessert:
        def __init__(self, cost):
            self._cost = cost
        def calculate_cost(self):
            return self._cost

    item1 = DummyDessert(5.0)
    item2 = DummyDessert(2.0)
    item3 = DummyDessert(8.0)

    order.add(item1)
    order.add(item2)
    order.add(item3)

    order.sort()

    sorted_costs = [item.calculate_cost() for item in order.order]
    assert sorted_costs == [2.0, 5.0, 8.0]