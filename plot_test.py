import datetime
from typing import List
import plotly.graph_objects as go

from utils import get_stock, get_date_list, get_stock_price_date


price_date = get_stock_price_date(target="TSLA", period="10d")
print(price_date)


def draw_graph(date_list: List[datetime.datetime], prices: List[float]) -> None:
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
