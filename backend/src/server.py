from typing import Annotated
from enum import StrEnum
from fastapi import FastAPI, Query

app = FastAPI()


class StatisticValue(StrEnum):
    PROFIT = "profit"
    ANNUALIZED_RETURN = "annualized_return"
    PERCENT_RETURN = "percent_return"


@app.get("/")
async def get_stock_statistics(
    includes: Annotated[
        list[StatisticValue], Query(title="Includes", description="Statistics to include in the result")
    ] = [StatisticValue.PROFIT],
):
    result = dict()
    if "profit" in includes:
        result["profit"] = 123.4
    if "annualized_return" in includes:
        result["annualized_return"] = 1.0
    if "percent_return" in includes:
        result["percent_return"] = 1.0
    return result
