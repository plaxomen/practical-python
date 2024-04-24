#!/usr/bin/env python
# report.py
#
# Exercise 2.4

from fileparse import parse_csv
import sys
import stock
import tableformat


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


def print_report(reportdata, formatter):
    """Prints a formatted table from a list of (name, shares, price, change) tuples."""
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:,.2f}", f"{change:,.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfolio_filename: str, prices_filename: str):
    """Outputs a report of the current portfolio, its prices, and the change in price."""

    # Read data files.
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # Create the report data.
    reportdata = make_report(portfolio, prices)

    # Print out the report data.
    formatter = tableformat.TableFormatter()
    print_report(reportdata, formatter)


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
