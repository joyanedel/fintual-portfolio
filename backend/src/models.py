from __future__ import annotations
from datetime import date
from pydantic.dataclasses import dataclass


@dataclass
class Portfolio:
    stocks: list[tuple[Stock, int]]

    def profit(self, start_date: date, end_date: date) -> float:
        """
        Returns the profit generated between a period determined by `start_date` and `end_date`
        """
        stock_profits = sum(
            [(stock.price(end_date) - stock.price(start_date)) * quantity for stock, quantity in self.stocks]
        )

        return stock_profits

    def annualized_return(self, start_date: date, end_date: date) -> float:
        """
        Returns the annualized return between a period of time
        """
        delta_period_in_years = (end_date - start_date).days / 365
        if delta_period_in_years == 0:
            return 0.0

        initial_investment = sum([stock.price(start_date) * quantity for stock, quantity in self.stocks])
        final_outcome = sum([stock.price(end_date) * quantity for stock, quantity in self.stocks])

        return (final_outcome / initial_investment) ** (1 / delta_period_in_years) - 1

    def percent_return(self, start_date: date, end_date: date):
        """
        Returns the percent return between a period of time
        """
        initial_investment = sum([stock.price(start_date) * quantity for stock, quantity in self.stocks])
        final_outcome = sum([stock.price(end_date) * quantity for stock, quantity in self.stocks])

        return (final_outcome / initial_investment) - 1


@dataclass
class Stock:
    ticker: str

    history: dict[date, float]
    company_name: str | None = None

    def add_history_entry(self, _date: date, price: float):
        self.history[_date] = price

    def price(self, lookup_date: date):
        return self.history[lookup_date]

    def __hash__(self) -> int:
        return hash(self.ticker)
