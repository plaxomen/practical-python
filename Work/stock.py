# stock.py
#
# Exercise 4.1: Objects as Data Structures


class Stock:
    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        """Returns the number of shares multiplied by the current price."""
        return self.shares * self.price

    def sell(self, shares_to_sell: int):
        self.shares -= shares_to_sell
        return self.shares
