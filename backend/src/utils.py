from datetime import date, timedelta
from random import random

from src.models import Stock, Portfolio
from functools import cache


@cache
def generate_random_portfolio():
    """
    Generate a portfolio with random prices set for AAPL, GOOGL, MSFT and FNTL tickers
    """
    dates_from_2021_to_now = generate_dates(date(2021, 1, 1), date.today())
    dates_length = len(dates_from_2021_to_now)

    aapl_stock = Stock(
        ticker="AAPL", history=dict(zip(dates_from_2021_to_now, generate_random_values(dates_length, 0, 2000.0)))
    )
    fntl_stock = Stock(
        ticker="AAPL", history=dict(zip(dates_from_2021_to_now, generate_random_values(dates_length, 0, 2000.0)))
    )
    msft_stock = Stock(
        ticker="AAPL", history=dict(zip(dates_from_2021_to_now, generate_random_values(dates_length, 0, 2000.0)))
    )
    googl_stock = Stock(
        ticker="AAPL", history=dict(zip(dates_from_2021_to_now, generate_random_values(dates_length, 0, 2000.0)))
    )

    portfolio = Portfolio(stocks=[(aapl_stock, 1), (fntl_stock, 1), (msft_stock, 1), (googl_stock, 1)])

    return portfolio


def generate_random_values(n: int, min_value: float, max_value: float):
    return [min_value + (max_value - min_value) * random() for _ in range(n)]


def generate_dates(start_date: date, end_date: date):
    return [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]
