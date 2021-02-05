# Calculate daily change from close - previous close

# Stock Market

import pandas as pd
import yfinance as yf
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

#Creats a list of stocks for the program to use.
stocks = [
    {
        'ticker': 'AAPL',
        'name': 'Apple'
    },
    {
        'ticker': 'AMZN',
        'name': 'Amazon'
    },
    {
        'ticker': 'WMT',
        'name': 'Walmart'
    }
]


def create_plot(stocks):
  # Create an empty dataframe
  data = pd.DataFrame()
  for stock in stocks: 
    # Create a column for the adjusted close of each stock
    # Here we use the DataReader library to get the data.
    data[stock['ticker']] = wb.DataReader(stock['ticker'], data_source='yahoo', start='2007-1-1')['Adj Close']

  # Calculate the returns for all the days
  returns = data.apply(lambda x: (x / x[0] * 100))

  plt.figure(figsize=(8, 4))

# Plot the returns
  for stock in stocks: 
    plt.plot(returns[stock['ticker']], label=stock['name'])

  # We need to call .legend() to show the legend.
  plt.legend()
  # Give the axes labels
  plt.ylabel('Cumulative Returns %')
  plt.xlabel('Time')
  plt.show()

#Creates the final graph of all the stocks
create_plot(stocks)
