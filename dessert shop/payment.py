from typing import Protocol, Literal

class Payable(Protocol):
    PayType: Literal["CASH", "CARD", "PHONE"]

    def get_pay_type(self) -> PayType:
        return self.PayType

    def set_pay_type(self, payment_method: PayType):
        self.PayType = payment_method



