import datetime
from typing import List
import plotly.graph_objects as go

from utils import get_stock, get_date_list


prices = get_stock("AMZN")

date_list = get_date_list("AMZN")

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


draw_graph(date_list, prices)
