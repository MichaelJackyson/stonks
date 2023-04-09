import datetime
from typing import List
import plotly.graph_objects as go

from utils import get_stock, get_date_list, get_stock_price_date


price_date = get_stock_price_date(target="ETH-USD", period="3y")
print(price_date)


def draw_graph(date_list: List[datetime.datetime], prices: List[float]) -> None:
    """
    Draw a graph of prices over time.

    Args:
    - date_list: A list of datetime.datetime objects representing dates for which prices are given.
    - prices: A list of float values representing the prices for the corresponding dates in date_list.

    Returns:
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


draw_graph(list(price_date.keys()), list(price_date.values()))
