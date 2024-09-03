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
    "start_date, end_date, expected_profit",
    [
        (date(2024, 9, 1), date(2024, 9, 1), 0.0),
        (date(2024, 9, 1), date(2024, 9, 2), 19.25),
        (date(2024, 9, 1), date(2024, 9, 3), 13.55),
        (date(2024, 9, 3), date(2024, 9, 9), 111.4),
        (date(2024, 9, 1), date(2024, 9, 10), 143.25),
    ],
)
def test_portfolio(portfolio_fixture, start_date, end_date, expected_profit):
    result = portfolio_fixture.profit(start_date, end_date)

    assert round(result, 2) == expected_profit
