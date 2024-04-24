# stock.py
#
# Exercise 4.1: Objects as Data Structures


class Stock:
    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name = name
        self.shares = shares
        self.price = price
