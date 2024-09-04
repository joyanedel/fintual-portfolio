from datetime import date
import pytest

from src.models import Portfolio, Stock
from src.files import read_lines_from_file
from src.constants import STATIC_FILES_PATH


@pytest.fixture(scope="session")
def portfolio_fixture():
    def __parse_stock_line(line: str):
        _date, _, _, price = line.split(",")
        return (date.fromisoformat(_date), float(price))

    aapl_fixture = map(__parse_stock_line, read_lines_from_file(STATIC_FILES_PATH / "aapl_fixture.csv")[1:])
    fntl_fixture = map(__parse_stock_line, read_lines_from_file(STATIC_FILES_PATH / "fntl_fixture.csv")[1:])
    googl_fixture = map(__parse_stock_line, read_lines_from_file(STATIC_FILES_PATH / "googl_fixture.csv")[1:])
    msft_fixture = map(__parse_stock_line, read_lines_from_file(STATIC_FILES_PATH / "msft_fixture.csv")[1:])

    aapl_stock = Stock(ticker="AAPL", history=dict(aapl_fixture))
    fntl_stock = Stock(ticker="FNTL", history=dict(fntl_fixture))
    googl_stock = Stock(ticker="GOOGL", history=dict(googl_fixture))
    msft_stock = Stock(ticker="MSFT", history=dict(msft_fixture))

    portfolio = Portfolio(stocks=[(aapl_stock, 8), (fntl_stock, 1), (msft_stock, 4), (googl_stock, 2)])

    return portfolio


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
def test_portfolio_profit(portfolio_fixture, start_date, end_date, expected_profit):
    result = portfolio_fixture.profit(start_date, end_date)

    assert round(result, 2) == expected_profit


@pytest.mark.parametrize(
    "start_date, end_date, expected_annualized_return",
    [
        (date(2024, 9, 1), date(2024, 9, 1), 0.0),
        (date(2024, 9, 1), date(2024, 9, 2), 1.3),
        (date(2024, 9, 1), date(2024, 9, 3), 0.34),
        (date(2024, 9, 3), date(2024, 9, 9), 1.23),
        (date(2024, 9, 1), date(2024, 9, 10), 0.98),
    ],
)
def test_portfolio_annualized_return(portfolio_fixture, start_date, end_date, expected_annualized_return):
    result = portfolio_fixture.annualized_return(start_date, end_date)

    assert round(result, 2) == expected_annualized_return


@pytest.mark.parametrize(
    "start_date, end_date, expected_percent_return",
    [
        (date(2024, 9, 1), date(2024, 9, 1), 0.0),
        (date(2024, 9, 1), date(2024, 9, 2), 0.0),
        (date(2024, 9, 1), date(2024, 9, 3), 0.0),
        (date(2024, 9, 3), date(2024, 9, 9), 0.01),
        (date(2024, 9, 1), date(2024, 9, 10), 0.02),
    ],
)
def test_portfolio_percent_return(portfolio_fixture, start_date, end_date, expected_percent_return):
    result = portfolio_fixture.percent_return(start_date, end_date)

    assert round(result, 2) == expected_percent_return
