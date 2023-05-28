import plotly.graph_objects as go
import pandas as pd
from stock_data import get_data

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv"
)

fig = go.Figure(
    data=[
        go.Candlestick(
            x=df["Date"],
            open=df["AAPL.Open"],
            high=df["AAPL.High"],
            low=df["AAPL.Low"],
            close=df["AAPL.Close"],
        )
    ]
)

ticker = "ITC"
fig = go.Figure(
    data = [
        go.Candlestick(
            x = get_data(ticker)['date'],
            open = get_data(ticker)['open'],
            close = get_data(ticker)['close'],
            high = get_data(ticker)['high'],
            low = get_data(ticker)['low']
        )
    ]
)

fig.update_layout(xaxis_rangeslider_visible=False)
fig.show()