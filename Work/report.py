# report.py
#
# Exercise 2.4

import csv


def read_portfolio_tuple(filename):
    """A function that returns a list of tuples of the holdings in a portfolio"""
    portfolio = []
    with open(filename, "rt") as f:
        data = csv.reader(f)
        header = next(data)
        for row in data:
            portfolio.append((row[0], int(row[1]), float(row[2])))
    return portfolio


def read_portfolio(filename):
    """A function that returns a list of dictionaries of the holdings in a portfolio"""
    portfolio = []
    with open(filename, "rt") as f:
        data = csv.reader(f)
        header = next(data)
        for row in data:
            portfolio.append(
                {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            )
    return portfolio


def read_prices(filename):
    """Returns a dictionary of stock prices (key=stock name, value=stock price)
    read from a file."""
    prices = {}
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            if row:
                prices[row[0]] = float(row[1])
    return prices


def make_report(portfolio, prices):
    """Returns a list of tuples where each tuple is a summary of the
    performance of the stock."""
    report = []
    for stock in portfolio:
        name = stock["name"]
        if name in prices:
            price = prices[name]
            price_delta = f"{price - stock["price"]:.2f}"
        else:
            price = None
            price_delta = None
        report.append((name, stock["shares"], price, price_delta))
    return report


def compute_portfolio_cost(portfolio):
    """Returns the cost of the entire portfolio."""
    total = 0.0
    for stock in portfolio:
        total += stock["shares"] * stock["price"]
    return total


def compute_portfolio_value(portfolio, prices):
    total = 0.0
    for stock in portfolio:
        name = stock["name"]
        if name in prices:
            total += stock["shares"] * prices[name]
    return total


def compute_portfolio_pnl(portfolio, prices):
    cost = compute_portfolio_cost(portfolio)
    current_value = compute_portfolio_value(portfolio, prices)
    return current_value - cost


def compute_holding_pnl(portfolio, prices):
    """Returns a dictionary of the pnl for each holding in the portfolio."""
    pnl = {}
    for stock in portfolio:
        name = stock["name"]
        if name in prices:
            cost = stock["shares"] * stock["price"]
            curr_value = stock["shares"] * prices[name]
            pl = round(curr_value - cost, 2)
            if name in pnl:
                pnl[name] += pl
            else:
                pnl[name] = pl
        else:
            pnl[name] = None
    return pnl


portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")
report = make_report(portfolio, prices)

# print(f"Portfolio Cost: ${compute_portfolio_cost(portfolio):,.2f}")
# print(f"Portfolio Value: ${compute_portfolio_value(portfolio, prices):,.2f}")
# print(f"Portfolio PNL: ${compute_portfolio_pnl(portfolio, prices):,.2f}")
