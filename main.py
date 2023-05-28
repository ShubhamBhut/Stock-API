from scraping import key_points
from stock_data import get_data
import streamlit as st

ticker = input("Enter the ticker: ")

key_points = key_points(ticker)

print(key_points)