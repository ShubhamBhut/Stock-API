from scraping import key_points
from plotly_chart import candlestick_maker
import streamlit as st

ticker = st.text_input("Enter the ticker: ", 'ITC')
st.plotly_chart(candlestick_maker(ticker))

key_points = key_points(ticker)

print(key_points)