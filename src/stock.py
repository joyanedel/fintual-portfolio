from dataclasses import dataclass
from datetime import date


@dataclass
class Stock:
    """
    Stock representation
    """
    name: str
    history: dict[date, float]

    def __hash__(self) -> int:
        return hash(self.name)

    def price(self, lookup_date: date) -> float:
        """
        Returns the price of the lookup date

        Raises an error if lookup date doesn't exist in the history
        """
        price = self.history.get(lookup_date, None)

        if price is None:
            raise KeyError(f"Date {lookup_date} has no registered price")
