# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename: str) -> dict:
    """A function that returns a list of dictionaries of the holdings in a portfolio"""
    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for rownum, row in enumerate(rows, 2):
            try:
                record = dict(zip(header, row))
                portfolio.append(record)
            except ValueError as err:
                print(
                    f"Error processing row {rownum}. Missing or bad data: {row} > Message: {err}"
                )
    return portfolio


def read_prices(filename: str) -> dict:
    """Returns a dictionary of stock prices (key=stock name, value=stock price)
    read from a file."""
    prices = {}
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                prices[row[0]] = float(row[1])
    return prices


def make_report(portfolio: dict, prices: dict) -> list[tuple]:
    """Returns a list of tuples where each tuple is a summary of the
    performance of the stock."""
    report = []
    for stock in portfolio:
        name = stock["name"]
        if name in prices:
            price = prices[name]
            price_delta = price - float(stock["price"])
        else:
            price = 0.0
            price_delta = 0.0
        report.append((name, stock["shares"], price, price_delta))
    return report


def print_report(report: list[tuple]):
    """Prints a formatted table of the stockes in report."""
    headers = ("Name", "Shares", "Price", "Change")
    print("%10s | %10s | %10s | %10s" % headers)
    print(f"{'':->10s} | {'':->10s} | {'':->10s} | {'':->10s}")
    for name, shares, price, change in report:
        price = f"${price:.2f}"
        print(f"{name:>10s} | {int(shares):>10d} | {price:>10s} | {change:>10.2f}")


portfolio = read_portfolio("Data/portfoliodate.csv")
prices = read_prices("Data/prices.csv")
report = make_report(portfolio, prices)
print_report(report)
