from scraping import key_points
from plotly_chart import candlestick_maker
import streamlit as st

ticker = input("Enter the ticker: ")

key_points = key_points(ticker)

print(key_points)