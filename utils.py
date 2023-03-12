import os
import datetime
from typing import List

import rich
import numpy as np
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

    if os.path.exists(os.path.join("data", "{}_{}.npy".format(target, period))):
        prices = np.load(os.path.join("data", "{}_{}.npy".format(target, period)))
        return prices

    stock = yf.Ticker(target)

    # rich.print(stock.info)

    hist = stock.history(period=period)
    # rich.print(hist)

    prices = hist["Close"].tolist()

    return prices


def get_date_list(target: str, period: str = "max") -> List[datetime.datetime]:
    """
    Generates a list of datetime objects based on the specified targeted stock and period.

    Args:
        target (str): A string that specifies the targeted stock for which date list is required.
        period (str, optional): A string that specifies the time period for which the date list 
                                should be generated. Defaults to "max".

    Returns:
        List[datetime.datetime]: A list of datetime objects representing the dates 
                                  based on the target and period parameters.
    """
    dates = yf.Ticker(target).history(period=period).index.tolist()
    date_list = [datetime.datetime.strptime(str(x).split()[0], "%Y-%m-%d") for x in dates]

    return date_list
