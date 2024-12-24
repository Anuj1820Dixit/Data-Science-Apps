import streamlit as st
import pandas as pd
import yfinance as yf
st.write("""
# SIMPLE STOCK PRICE APP

Shown are the STOCK closing price and Volume OF google

""")

tickersymbol = 'GooGL'
tickerdata= yf.Ticker(tickersymbol)
tickerdf = tickerdata.history(period='id', start= '2009-1-28', end= '2023-05-04')
st.line_chart(tickerdf.Close)
st.line_chart(tickerdf.Volume)