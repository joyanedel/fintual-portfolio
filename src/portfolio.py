from datetime import date
from dataclasses import dataclass
from collections import defaultdict
from typing import TypedDict

from src.stock import Stock


@dataclass
class Portfolio:
    """
    Portfolio representation
    """

    class PortfolioDetails(TypedDict):
        annualized_return_percentage: float
        percent_return: float

    stocks: dict[Stock, int]  # stock, quantity

    def profit(self, start_date: date, end_date: date) -> tuple[float, PortfolioDetails]:
        """
        Returns the profit made between the period of time within `start_date` and `end_date`
        """
        stock_profits = [
            (stock.price(end_date) - stock.price(start_date)) * quantity for (stock, quantity) in self.stocks.items()
        ]
        final_profit = sum(stock_profits)

        final_outcome = sum([stock.price(end_date) * quantity for (stock, quantity) in self.stocks.items()])
        initial_investment = sum([stock.price(start_date) * quantity for (stock, quantity) in self.stocks.items()])

        time_period = (end_date - start_date).days / 365

        return final_profit, {
            "annualized_return_percentage": ((final_outcome / initial_investment) ** (1 / time_period)) - 1
            if time_period > 0
            else 1.0,
            "percent_return": final_outcome / initial_investment,
        }

    @classmethod
    def from_csv(cls, lines: list[str], quantities: dict[str, int]):
        """
        Load portfolio from csv lines and quantities dict with ticker as key and quantity as value
        """
        stocks = defaultdict(list)
        stock_lines = map(lambda x: x.split(","), lines)

        for [_date, ticker, company_name, price] in stock_lines:
            stocks[(ticker, company_name)].append((date.fromisoformat(_date), float(price)))

        stocks = {
            Stock(
                ticker=ticker, company_name=company_name, history={_date: price for (_date, price) in history}
            ): quantities[ticker]
            for ((ticker, company_name), history) in stocks.items()
        }
        return Portfolio(stocks=stocks)
