from dataclasses import dataclass
from datetime import date


@dataclass
class Stock:
    """
    Stock representation
    """

    ticker: str
    company_name: str
    history: dict[date, float]

    def price(self, lookup_date: date) -> float:
        """
        Returns the price of the lookup date

        Raises an error if lookup date doesn't exist in the history
        """
        price = self.history.get(lookup_date, None)

        if price is None:
            raise KeyError(f"Date {lookup_date} has no registered price")

        return price

    def __hash__(self) -> int:
        return hash(self.ticker)

    def __str__(self) -> str:
        return f"{self.company_name} ({self.ticker})"

    def __repr__(self) -> str:
        return self.__str__()
