# pcost.py
#
# Exercise 1.27
#
# Write a program to calculate the total cost of the holdings in portfolio.csv
import sys
import csv


def portfolio_cost(filename):
    "A function to calculate the total cost of a portfolio in a file."
    total = 0
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row_no, row in enumerate(rows, 2):
            record = dict(zip(header, row))
            try:
                nshares = int(record["shares"])
                price = float(record["price"])
                total += nshares * price
            except ValueError as err:
                print(
                    f"Error processing row[{row_no}]. Bad or missing data: {row} > Message: {err}"
                )
    return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print(f"Total cost of portfolio in '{filename}': ${cost:,.2f}")
