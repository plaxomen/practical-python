# pcost.py
#
# Exercise 1.27
#
# Write a program to calculate the total cost of the holdings in portfolio.csv

total = 0
with open("Data/portfolio.csv", "rt") as f:
    header = next(f)
    for line in f:
        row = line.split(",")
        nshares = int(row[1])
        price = float(row[2])
        cost = nshares * price
        total += cost

print(f"Total cost: ${total:,.2f}")
