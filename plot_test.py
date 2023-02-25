import plotly.graph_objects as go

from utils import get_stock, get_date_list


prices = get_stock("AMZN")

date_list = get_date_list("AMZN")

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
