
class DessertItem:
    """A base class for all dessert items"""
    def __init__(self, name = ""):
        self.name = name


class Candy(DessertItem):
    def __init__(self,name, candy_weight = 0.0, price_per_pound = 0.0):
        super().__init__(name)
        self.weight = candy_weight
        self.price_per_pound = price_per_pound

class Cookie(DessertItem):
    def __init__(self, name, number_of_cookies = 0, price_per_dozen = 0.0):
        super().__init__(name)
        self.number_of_cookies = number_of_cookies
        self.price_per_dozen = price_per_dozen

class IceCream(DessertItem):
    def __init__(self, name, scoop_count = 0, price_per_scoop = 0.0):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

class Sundae(IceCream):
    """Sundae is a subclass of IceCream"""
    def __init__(self, name, scoop_count = 0, price_per_scoop = 0.0, topping_name = "", topping_price = 0.0):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price