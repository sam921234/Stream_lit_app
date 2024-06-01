import pandas as pd
import numpy as np
import streamlit as st
import yfinance as yf
import datetime


st.title('Stock Price Analyser')

# Ticker symbo input from end user
ticker_symbol  = st.text_input("Enter Ticker Symbol", "MSFT")
st.write("The current stock is for : ", ticker_symbol)

# start and end period input from the user with proper layout
### keeping start and end date in 1row in 2 diff columns
col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Start Date", datetime.date(2019, 1, 1))
    st.write("Start date of analysis:", start_date)

with col2:
    end_date = st.date_input("Start Date", datetime.date(2024, 5, 31))
    st.write("End date of analysis:", end_date)

# Displaying the data
data  = yf.Ticker(ticker_symbol)
df = data.history(period="1d",
                  start = start_date,
                  end = end_date)
st.dataframe(df)

# line chart displaying trend of daily closing price
st.subheader('Daily Closing Price', divider='rainbow')
st.line_chart(df.Close)

# line chart displaying volume of stocks traded daily
st.subheader('Daily Stocks Traded Volumne', divider='rainbow')
st.line_chart(df.Volume)

