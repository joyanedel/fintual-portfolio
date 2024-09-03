import pytest
from pathlib import Path
from datetime import date

from src.portfolio import Portfolio

STOCK_FIXTURE_PATH = Path(__file__).parent / "stock_fixtures.csv"


@pytest.fixture
def stock_file_lines():
    with open(STOCK_FIXTURE_PATH, "r") as f:
        return f.readlines()


@pytest.fixture
def portfolio_fixture(stock_file_lines):
    return Portfolio.from_csv(stock_file_lines[1:], {"AAPL": 8, "MSFT": 4, "GOOGL": 2, "FNTL": 1})


@pytest.mark.parametrize(
    "start_date, end_date, expected_profit, expected_annualized_return_percentage",
    [
        (date(2024, 9, 1), date(2024, 9, 1), 0.0, 1.0),
        (date(2024, 9, 1), date(2024, 9, 2), 19.25, 1.3),
        (date(2024, 9, 1), date(2024, 9, 3), 13.55, 0.34),
        (date(2024, 9, 3), date(2024, 9, 9), 111.4, 1.23),
        (date(2024, 9, 1), date(2024, 9, 10), 143.25, 0.98),
    ],
)
def test_portfolio_profit(
    portfolio_fixture, start_date, end_date, expected_profit, expected_annualized_return_percentage
):
    (result, details) = portfolio_fixture.profit(start_date, end_date)

    assert round(result, 2) == expected_profit
    assert round(details["annualized_return_percentage"], 2) == expected_annualized_return_percentage
