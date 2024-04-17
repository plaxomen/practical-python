# pcost.py
#
# Exercise 1.27
#
# Write a program to calculate the total cost of the holdings in portfolio.csv
import fileparse
import sys


def portfolio_cost_v2(filename):
    """A function to calculate the total cost of a portfolio in a file."""
    portfolio = fileparse.parse_csv(
        filename=filename, select=["name", "shares", "price"], types=[str, int, float]
    )
    cost = 0
    for position in portfolio:
        cost += position["shares"] * position["price"]
    return cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost_v2(filename)
print(f"Total cost of portfolio in '{filename}': ${cost:,.2f}")
