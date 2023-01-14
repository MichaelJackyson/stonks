from typing import List

import rich
import yfinance as yf


def get_stock(target: str, period="max") -> List[float]:
    """it gets the stock prices

    Args:
        target (`str`): Stock call number required
        period (`str`): The time of the info asked

    >>> from utils import get_stock
    >>> prices = get_stock("AMZN")
    >>> len(prices)
    6460
    """
    stock = yf.Ticker(target)

    # rich.print(stock.info)

    hist = stock.history(period=period)
    # rich.print(hist)

    prices = hist["Close"].tolist()

    return prices

