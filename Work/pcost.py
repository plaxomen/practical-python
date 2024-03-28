# pcost.py
#
# Exercise 1.27
#
# Write a program to calculate the total cost of the holdings in portfolio.csv


def portfolio_cost(filename):
    "A function to calculate the total cost of a portfolio in a file."
    total = 0
    with open(filename, "rt") as f:
        header = next(f)
        for line in f:
            row = line.split(",")
            nshares = int(row[1])
            price = float(row[2])
            total += nshares * price
    return total


cost = portfolio_cost("Data/portfolio.csv")
print(f"Total cost: ${cost:,.2f}")
