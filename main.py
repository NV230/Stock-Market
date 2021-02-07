"""
@authors: Keenan, Nibodh, Shahil
@Date: Feb 2021
@Version: 2.3

This program is designed to return the cumulative returns of stocks.
 
""" 
# Stock Market

# Calculate daily change from close - previous close

import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

#Creats an array of stocks for the program to use.
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

# create_graph is our function to create the chart 
def create_graph(stocks):
  # Create an empty dataframe
  data = pd.DataFrame()
  for stock in stocks: 
    # Create a column for the adjusted close of each stock
    # Here we use the DataReader library to get the data.
    data[stock['ticker']] = wb.DataReader(stock['ticker'], data_source='yahoo', start='2016-1-1')['Adj Close']

  # Calculate the returns for all the days
  # lambda allows the function to be defined without using "def"
  # the lambda stores the value of each stock (which is the input) 
  returns = data.apply(lambda x: (x / x[0] * 100))

  plt.figure(figsize=(8, 4))

# Plot the returns
  for stock in stocks: 
    plt.plot(returns[stock['ticker']], label=stock['name'])

  # We need to call .legend() to show the legend.
  plt.legend()
  # Give the axes labels
  plt.ylabel('Cumulative Returns %')
  plt.xlabel('Time (Year)')
  plt.show()

#Creates the final graph of all the stocks
create_graph(stocks)