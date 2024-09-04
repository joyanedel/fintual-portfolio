from __future__ import annotations
from datetime import date
from typing import Annotated
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from src.schemes import StatisticValue
from src.utils import generate_random_portfolio

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:3000"])


@app.get(
    "/",
    description="Compute statistics related to historical stock prices. For now it assumes that a person has bought 1 stock per ticker which are preloaded from a csv file. Available historical prices are from 2024-09-01 to 2024-09-10",
)
async def get_stock_statistics(
    start_date: date,
    end_date: date,
    includes: Annotated[
        list[StatisticValue], Query(title="Includes", description="Statistics to include in the result")
    ] = [StatisticValue.PROFIT],
):
    result = dict()
    portfolio = generate_random_portfolio()
    if "profit" in includes:
        result["profit"] = portfolio.profit(start_date, end_date)
    if "annualized_return" in includes:
        result["annualized_return"] = portfolio.annualized_return(start_date, end_date)
    if "percent_return" in includes:
        result["percent_return"] = portfolio.percent_return(start_date, end_date)
    return result
