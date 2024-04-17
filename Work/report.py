# report.py
#
# Exercise 2.4

from fileparse import parse_csv


def read_portfolio(filename: str) -> dict:
    """A function that returns a list of dictionaries of the holdings in a portfolio"""
    portfolio = parse_csv(
        filename=filename,
        select=["name", "shares", "price"],
        types=[str, int, float],
    )
    return portfolio


def read_prices(filename: str) -> dict:
    """Returns a dictionary of stock prices (key=stock name, value=stock price)
    read from a file."""
    prices = parse_csv(filename=filename, has_headers=False, types=[str, float])
    return dict(prices)


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


# portfolio_report("Data/portfolio.csv", "Data/prices.csv")
