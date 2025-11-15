from typing import Protocol, Literal, get_args

# Define PayType whose only legal values are "CASH", "CARD", "PHONE"
PayType = Literal["CASH", "CARD", "PHONE"]

# A runtime set of valid payment values extracted from the Literal
VALID_PAYMENT_TYPES = set(get_args(PayType))


class Payable(Protocol):
    def get_pay_type(self) -> PayType:
        ...

    def set_pay_type(self, payment_method: PayType) -> None:
        ...


class Payment(Payable):
    """Concrete implementation of Payable.
    Validates values on set and get. Default payment is CASH.
    """

    def __init__(self, payment_method: PayType = "CASH") -> None:
        # store as plain string; validate via setter
        self._payment_method = None
        self.set_pay_type(payment_method)

    def get_pay_type(self) -> PayType:
        if self._payment_method not in VALID_PAYMENT_TYPES:
            raise ValueError(f"Invalid payment method stored: {self._payment_method}. Valid options: {VALID_PAYMENT_TYPES}")
        return self._payment_method  # type: ignore[return-value]

    def set_pay_type(self, payment_method: PayType) -> None:
        if payment_method not in VALID_PAYMENT_TYPES:
            raise ValueError(f"Invalid payment method: {payment_method}. Valid options: {VALID_PAYMENT_TYPES}")
        self._payment_method = payment_method





