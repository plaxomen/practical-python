# report.py
#
# Exercise 2.4

import sys
import csv


def read_portfolio_tuple(filename):
    """A function that returns a list of tuples of the holdings in a portfolio"""
    portfolio = []
    with open(filename, "rt") as f:
        data = csv.reader(f)
        header = next(data)
        for row in data:
            portfolio.append((row[0], int(row[1]), float(row[2])))
    return portfolio


def read_portfolio_dict(filename):
    """A function that returns a list of dictionaries of the holdings in a portfolio"""
    portfolio = []
    with open(filename, "rt") as f:
        data = csv.reader(f)
        header = next(data)
        for row in data:
            portfolio.append(
                {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            )
    return portfolio
