# pcost.py
#
# Exercise 1.27
#
# Write a program to calculate the total cost of the holdings in portfolio.csv
import csv


def portfolio_cost(filename):
    "A function to calculate the total cost of a portfolio in a file."
    total = 0
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row_no, row in enumerate(rows, 2):
            try:
                nshares = int(row[1])
                price = float(row[2])
                total += nshares * price
            except Exception as e:
                print(f"Error processing row[{row_no}]. {e}")
    return total


cost = portfolio_cost("Data/portfolio.csv")
print(f"Total cost: ${cost:,.2f}")
