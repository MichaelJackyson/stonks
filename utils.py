import os
import datetime
from typing import List, Dict
import plotly.graph_objects as go


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


def get_date_list(target: str, period: str = "10y") -> List[datetime.datetime]:
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


def get_stock_price_date(target: str, period="10y") -> Dict[datetime.datetime, float]:
    """it gets the stock prices and date at the same time

    Args:
        target (`str`): Stock call number required
        period (`str`): The time of the info asked

    >>> from utils import get_stock_price_date
    >>> price_date = get_stock_price_date(target="TSLA", period="1y")
    >>> print(price_date)
    {datetime.datetime(2023, 3, 20, 0, 0): 183.25, datetime.datetime(2023, 3, 21, 0, 0): 197.5800018310547, ...}
    """

    stock = yf.Ticker(target)
    hist = stock.history(period=period)

    prices = hist["Close"].tolist()
    date_list = [datetime.datetime.strptime(str(x).split()[0], "%Y-%m-%d") for x in hist.index.tolist()]

    return {k: v for k, v in zip(date_list, prices)}


def draw_graph(date_list: List[datetime.datetime], prices: List[float]) -> None:
    """
    Draw a graph of prices over time.

    Args:
    - date_list: A list of datetime.datetime objects representing dates for which prices are given.
    - prices: A list of float values representing the prices for the corresponding dates in date_list.

    Returns:u
    - None.

    This function draws a graph of the given data using a suitable graphing library. The graph can be used to visualize 
    trends, patterns or correlations in the data.
    """
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=date_list, y=prices,
            mode="lines",   
            name="abc",
            line=dict(width=2)
        )
    )

    fig.show()
