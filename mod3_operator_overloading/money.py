class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
        self.normalize()

    def normalize(self):
        if self.cents >= 100:
            self.dollars += self.cents // 100
            self.cents = self.cents % 100

    def __str__(self):
        return f"${self.dollars}.{self.cents:02d}"
    
    def __add__(self, other):
        total_cents = self.cents + other.cents
        total_dollars = self.dollars + other.dollars
        total = Money(total_dollars, total_cents)
        total.normalize()
        return total
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            total_cents = self.cents * int(other)
            total_dollars = self.dollars * int(other)
            product = Money(total_dollars, total_cents)
            product.normalize()
            return product
        else:
            raise TypeError("Multiplication is only supported with int or float types.")
        
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            total_cents = self.cents * int(other)
            total_dollars = self.dollars * int(other)
            product = Money(total_dollars, total_cents)
            product.normalize()
            return product
        else:
            raise TypeError("Multiplication is only supported with int or float types.")
        
    def __eq__(self, other):
        return self.dollars == other.dollars and self.cents == other.cents

def main():
    m1 = Money(3, 50)
    m2 = Money(2, 75)

    print("m1:", m1)
    print("m2:", m2)

    m3 = m1 + m2
    print("m3:", m3)   # Expected: $6.25
    m4 = m1 * 2
    m5 = 3 * m2
    print("m4:", m4)   # Expected: $7.00
    print("m5:", m5)   # Expected: $8.25

    print(m1 == Money(2, 150))  # Expected: True
    print(m1 == Money(3, 49))   # Expected: False

if __name__ == "__main__":
    main()