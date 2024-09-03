from datetime import date
from dataclasses import dataclass
from collections import defaultdict

from src.stock import Stock


@dataclass
class Portfolio:
    """
    Portfolio representation
    """

    stocks: dict[Stock, int]  # stock, quantity

    def profit(self, start_date: date, end_date: date) -> float:
        """
        Returns the profit made between the period of time within `start_date` and `end_date`
        """
        stock_profits = [
            (stock.price(end_date) - stock.price(start_date)) * quantity for (stock, quantity) in self.stocks.items()
        ]

        return sum(stock_profits)

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
