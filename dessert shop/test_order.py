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
