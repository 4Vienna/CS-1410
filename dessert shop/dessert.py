from abc import ABC, abstractmethod
from packaging import Packaging
from payment import Payment
from combine import Combinable


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
    
    def __eq__(self, value):
        return self.calculate_cost() == value.calculate_cost()
    
    def __ne__(self, value):
        return self.calculate_cost() != value.calculate_cost()
    
    def __lt__(self, value):
        return self.calculate_cost() < value.calculate_cost()
    
    def __le__(self, value):
        return self.calculate_cost() <= value.calculate_cost()
    
    def __gt__(self, value):
        return self.calculate_cost() > value.calculate_cost()
    
    def __ge__(self, value):
        return self.calculate_cost() >= value.calculate_cost() 
    
    

class Candy(DessertItem, Packaging):
    def __init__(self,name = "", candy_weight = 0.0, price_per_pound = 0.0, packaging = "Bag"):
        super().__init__(name)
        self.weight = candy_weight
        self.price_per_pound = price_per_pound
        self.packaging = packaging

    def calculate_cost(self) -> float:
        return round(self.weight * self.price_per_pound, 2)
    
    def can_combine(self, other: "Candy") -> bool:
        if isinstance(other, Candy) and self.name == other.name and self.price_per_pound == other.price_per_pound:
            return True
        else:
            return False
        
    def combine(self, other: "Candy") -> "Candy":
        if not self.can_combine(other):
            raise ValueError("Cannot combine these two Candy items.")
        self.weight += other.weight
        return self
    
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
    
    def can_combine(self, other: "Cookie") -> bool:
        if isinstance(other, Cookie) and self.name == other.name and self.price_per_dozen == other.price_per_dozen:
            return True
        else:
            return False
        
    def combine(self, other: "Cookie") -> "Cookie":
        if not self.can_combine(other):
            raise ValueError("Cannot combine these two Cookie items.")
        self.number_of_cookies += other.number_of_cookies
        return self
    
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
        # use the Payment implementation to track/validate payment method
        self._payment = Payment()

    def __len__(self):
        return len(self.order)


    def __iter__(self):
        self._iter_index = 0
        return self


    def __next__(self):
        if self._iter_index >= len(self.order):
            raise StopIteration
        item = self.order[self._iter_index]
        self._iter_index += 1
        return item


    def add(self, item):
        # Try to combine with an existing item if possible. If the incoming
        # item does not implement `can_combine` (e.g. a test dummy), treat it
        # as non-combinable and simply append it.
        for existing_item in self.order:
            can_combine = getattr(item, "can_combine", None)
            if callable(can_combine) and item.can_combine(existing_item):
                existing_item.combine(item)
                return
        # No existing item could combine with `item` — append to order.
        self.order.append(item)
            
        

    def payment(self, payment_method: str | None = None) -> str:
        if payment_method is None:
            return self._payment.get_pay_type()
        self._payment.set_pay_type(payment_method)
        return self._payment.get_pay_type()


    def sort(self):
        self.order.sort(key=lambda item: item.calculate_cost())


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
                # avoid using tab characters (\t) — tabs expand inconsistently
                desc = f"-    {item.weight} lbs. @ ${item.price_per_pound}/lb:"
                rows.append([desc, f"${item.calculate_cost():.2f}", f"[Tax: ${item.calculate_tax():.2f}]"])

            # Cookie
            elif isinstance(item, Cookie):
                rows.append([f"{item.name} Cookies ({item.packaging})", "", ""])
                desc = f"-    {item.number_of_cookies} cookies. @ ${item.price_per_dozen}/dozen:"
                rows.append([desc, f"${item.calculate_cost():.2f}", f"[Tax: ${item.calculate_tax():.2f}]"])

            # Sundae (special -- has scoop line then topping line)
            elif isinstance(item, Sundae):
                rows.append([f"{item.topping_name} {item.name} Sundae ({item.packaging})", "", ""])
                scoop_line = f"-    {item.scoop_count} scoops. @ ${item.price_per_scoop}/scoop"
                rows.append([scoop_line, "", ""])
                topping_line = f"-    {item.topping_name} @ ${item.topping_price}:"
                rows.append([topping_line, f"${item.calculate_cost():.2f}", f"[Tax: ${item.calculate_tax():.2f}]"])

            # IceCream (not sundae)
                    # include payment method at end of order string
            elif isinstance(item, IceCream):
                rows.append([f"{item.name} Ice Cream ({item.packaging})", "", ""])
                desc = f"-    {item.scoop_count} scoops. @ ${item.price_per_scoop}/scoop:"
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


        try:
            pay = self.payment()
        except ValueError:
            pay = "Invalid"
        output += f"Payment Method: {pay}\n"
        return output
