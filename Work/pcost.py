# pcost.py
#
# Exercise 1.27
#
# Write a program to calculate the total cost of the holdings in portfolio.csv
import report
import sys


def portfolio_cost(filename):
    """A function to calculate the total cost of a portfolio in a file."""
    portfolio = report.read_portfolio(filename)
    cost = 0
    for position in portfolio:
        cost += position["shares"] * position["price"]
    return cost


def main(args):
    if len(args) != 2:
        raise SystemExit(
            f"Expected 2 arguments but received {len(args)}.\n\tUsage: pcost.py 'Data/portoflio.csv'"
        )

    filename = args[1]
    cost = portfolio_cost(filename)
    print(f"Total cost of {filename}: ${cost:,.2f}")


if __name__ == "__main__":
    main(sys.argv)
