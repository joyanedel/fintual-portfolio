from datetime import date
from dataclasses import dataclass

from src.stock import Stock


@dataclass
class Portfolio:
    """
    Portfolio representation
    """
    stocks: dict[Stock, int] # stock, quantity

    def profit(self, start_date: date, end_date: date) -> float:
        """
        Returns the profit made between the period of time within `start_date` and `end_date`
        """
        stock_profits = [
            (stock.price(end_date) - stock.price(start_date)) * quantity
            for (stock, quantity) in self.stocks.items()
        ]
        
        return sum(stock_profits)
