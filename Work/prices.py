# report.py
#
# Exercise 2.6
import csv


def read_prices(filename):
    """Returns a dictionary of stock prices (key=stock name, value=stock price)
    read from a file."""
    prices = {}
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            if row:
                prices[row[0]] = float(row[1])
    return prices
