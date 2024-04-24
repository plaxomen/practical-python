#!/usr/bin/env python
# report.py
#
# Exercise 2.4

from fileparse import parse_csv
import sys
import stock


def read_portfolio(filename: str) -> list[stock.Stock]:
    """A function that returns a list of stocks of the holdings in a portfolio"""
    with open(filename, "rt") as f:
        portfolio = parse_csv(
            iterable=f,
            select=["name", "shares", "price"],
            types=[str, int, float],
        )
    stocks = [stock.Stock(s["name"], s["shares"], s["price"]) for s in portfolio]
    return stocks


def read_prices(filename: str) -> dict:
    """Returns a dictionary of stock prices (key=stock name, value=stock price)
    read from a file."""
    with open(filename, "rt") as f:
        prices = parse_csv(iterable=f, has_headers=False, types=[str, float])
    return dict(prices)


def make_report(portfolio: list[stock.Stock], prices: dict) -> list[tuple]:
    """Returns a list of tuples where each tuple is a summary of the
    performance of the stock."""
    report = []
    for stock in portfolio:
        if stock.name in prices:
            price = prices[stock.name]
            price_delta = price - float(stock.price)
        else:
            price = 0.0
            price_delta = 0.0
        report.append((stock.name, stock.shares, price, price_delta))
    return report


def print_report(report: list[tuple]):
    """Prints a formatted table of the stockes in report."""
    headers = ("Name", "Shares", "Price", "Change")
    print("%10s | %10s | %10s | %10s" % headers)
    print(f"{'':->10s} | {'':->10s} | {'':->10s} | {'':->10s}")
    for name, shares, price, change in report:
        price = f"${price:.2f}"
        if float(change) < 0:
            change = f"-${abs(change):.2f}"
        else:
            change = f"${change:.2f}"
        print(f"{name:>10s} | {int(shares):>10d} | {price:>10s} | {change:>10s}")


def portfolio_report(portfolio_filename: str, prices_filename: str):
    """Outputs a report of the current portfolio, its prices, and the change in price."""
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


def main(args):
    if len(args) != 3:
        raise SystemExit(
            f"Expected 3 arguments, but received {len(args)}.\nUsage: report.py portfolio.csv prices.csv"
        )
    portfolio_filename = args[1]
    prices_filename = args[2]
    portfolio_report(portfolio_filename, prices_filename)


if __name__ == "__main__":
    main(sys.argv)
