# VL Module 2: Lab 2 - Creating a Bank Account Class

class Account:
    """A bank account class with an owner and a balance."""

    def __init__ (self, owner="", balance=0.0):
        """Initialize the account with an owner and a balance."""
        self.owner = owner
        self.balance = balance


    def __str__(self):
        """Return a string representation of the account."""
        return f"Owner: {self.owner}, Balance: ${self.balance:.2f}"