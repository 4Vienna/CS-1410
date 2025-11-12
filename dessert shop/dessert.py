from abc import ABC, abstractmethod
from packaging import Packaging
from payment import Payable


class DessertItem(ABC):
    """A base class for all dessert items"""
    def __init__(self, name = "", tax_percent = 7.25):
        self.name = name
        self.tax_percent = tax_percent

    @abstractmethod
    def calculate_cost(self) -> float:
        pass

    def calculate_tax(self) -> float:
        return round(self.calculate_cost() * (self.tax_percent / 100), 2)
    

class Candy(DessertItem, Packaging):
    def __init__(self,name = "", candy_weight = 0.0, price_per_pound = 0.0, packaging = "Bag"):
        super().__init__(name)
        self.weight = candy_weight
        self.price_per_pound = price_per_pound
        self.packaging = packaging

    def calculate_cost(self) -> float:
        return round(self.weight * self.price_per_pound, 2)
    
    def __str__(self):
        return f"{self.name} ({self.packaging})\n-\t{self.weight} lbs. @ ${self.price_per_pound}/lbs:, ${self.calculate_cost()}, [Tax: ${self.calculate_tax()}]"


class Cookie(DessertItem, Packaging):
    def __init__(self, name = "", number_of_cookies = 0, price_per_dozen = 0.0, packaging = "Box"):
        super().__init__(name)
        self.number_of_cookies = number_of_cookies
        self.price_per_dozen = price_per_dozen
        self.packaging = packaging

    def calculate_cost(self) -> float:
        return round((self.number_of_cookies / 12) * self.price_per_dozen, 2)
    
    def __str__(self):
        return f"{self.name} ({self.packaging})\n-\t{self.number_of_cookies} cookies. @ ${self.price_per_dozen}/dozen:, ${self.calculate_cost()}, [Tax: ${self.calculate_tax()}]"
    

class IceCream(DessertItem, Packaging):
    def __init__(self, name = "", scoop_count = 0, price_per_scoop = 0.0, packaging = "Bowl"):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.packaging = packaging

    def calculate_cost(self) -> float:
        return round(self.scoop_count * self.price_per_scoop, 2)
    
    def __str__(self):
        return f"{self.name} ({self.packaging})\n-\t{self.scoop_count} scoops. @ ${self.price_per_scoop}/scoop:, ${self.calculate_cost()}, [Tax: ${self.calculate_tax()}]"
    
    

class Sundae(IceCream, Packaging):
    """Sundae is a subclass of IceCream"""
    def __init__(self, name = "", scoop_count = 0, price_per_scoop = 0.0, topping_name = "", topping_price = 0.0, packaging = "Boat"):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
        self.packaging = packaging

    def calculate_cost(self) -> float:
        return round(super().calculate_cost() + self.topping_price, 2)
    
    def __str__(self):
        return f"{self.name} ({self.packaging})\n-\t{self.scoop_count} scoops. @ ${self.price_per_scoop}/scoop\n-\t{self.topping_name} @ ${self.topping_price}:, ${self.calculate_cost()}, [Tax: ${self.calculate_tax()}]"


class Order():
    """Order class works as a list holding DessertItem objects"""
    def __init__(self):
        self.order = []

    def __len__(self):
        return len(self.order)


    def add(self, item):
        self.order.append(item)


    def order_cost(self):
        total_cost = 0.0
        for item in self.order:
            total_cost += item.calculate_cost()
        return round(total_cost, 2)
    
    def order_tax(self):
        total_tax = 0.0
        for item in self.order:
            total_tax += item.calculate_tax()
        return round(total_tax, 2)
    
    def to_list(self):
        """Return a list of rows for tabulate.

        Each dessert item is represented as multiple rows so the first row contains
        the item name (with packaging) and the subsequent row(s) contain the
        description lines with cost and tax in the Cost/Tax columns. This makes
        the printed table match the requested multi-line layout.
        """
        rows = []
        for item in self.order:
            # Candy
            if isinstance(item, Candy) and not isinstance(item, Sundae):
                rows.append([f"{item.name} ({item.packaging})", "", ""])
                desc = f"-\t{item.weight} lbs. @ ${item.price_per_pound}/lb:"
                rows.append([desc, f"${item.calculate_cost():.2f}", f"[Tax: ${item.calculate_tax():.2f}]"])

            # Cookie
            elif isinstance(item, Cookie):
                rows.append([f"{item.name} Cookies ({item.packaging})", "", ""])
                desc = f"-\t{item.number_of_cookies} cookies. @ ${item.price_per_dozen}/dozen:"
                rows.append([desc, f"${item.calculate_cost():.2f}", f"[Tax: ${item.calculate_tax():.2f}]"])

            # Sundae (special -- has scoop line then topping line)
            elif isinstance(item, Sundae):
                rows.append([f"{item.topping_name} {item.name} Sundae ({item.packaging})", "", ""])
                scoop_line = f"-\t{item.scoop_count} scoops. @ ${item.price_per_scoop}/scoop"
                rows.append([scoop_line, "", ""])
                topping_line = f"-\t{item.topping_name} @ ${item.topping_price}:"
                rows.append([topping_line, f"${item.calculate_cost():.2f}", f"[Tax: ${item.calculate_tax():.2f}]"])

            # IceCream (not sundae)
            elif isinstance(item, IceCream):
                rows.append([f"{item.name} Ice Cream ({item.packaging})", "", ""])
                desc = f"-\t{item.scoop_count} scoops. @ ${item.price_per_scoop}/scoop:"
                rows.append([desc, f"${item.calculate_cost():.2f}", f"[Tax: ${item.calculate_tax():.2f}]"])

            # Fallback for any other DessertItem
            else:
                rows.append([f"{getattr(item, 'name', '')}", f"${item.calculate_cost():.2f}", f"[Tax: ${item.calculate_tax():.2f}]"])

        return rows


    def __str__(self):
        output = ""
        for item in self.order:
            if isinstance(item, Candy):
                output += f"{item.name}, {item.weight}, {item.price_per_pound}\n"
            elif isinstance(item, Cookie):
                output += f"{item.name}, {item.number_of_cookies}, {item.price_per_dozen}\n"
            elif isinstance(item, IceCream):
                output += f"{item.name}, {item.scoop_count}, {item.price_per_scoop}\n"
            elif isinstance(item, Sundae):
                output += f"{item.name}, {item.scoop_count}, {item.price_per_scoop}, {item.topping_name}, {item.topping_price}\n"
        return output
