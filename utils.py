from typing import List

import rich
import yfinance as yf


def get_stock(target: str, period="max") -> List[float]:
    stock = yf.Ticker(target)

    # rich.print(stock.info)

    hist = stock.history(period=period)
    # rich.print(hist)

    prices = hist["Close"].tolist()

    return prices

