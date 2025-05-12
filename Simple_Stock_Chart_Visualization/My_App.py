import yfinance as yf
import streamlit as st
from datetime import date

st.markdown(''' ## Simple Stock History Visualization
         Shows TataPower stock **closing price** and **volume**''')

# Corrected ticker for NSE
tickerSymbol = "TATAPOWER.NS"

# Use valid date range
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2021-04-01', end=str(date.today()))

st.write('''## Closing Price''')
st.line_chart(tickerDf['Close'])

st.write('''## Volume''')
st.line_chart(tickerDf['Volume'])
