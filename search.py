# Calculate daily change from close - previous close

# Stock Market

import numpy as np
import pandas as pd
import yfinance as yf
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


stocks = []

numOfStocks = int(input("How many stocks do you want to compare? \n")) 

for i in range(numOfStocks):
  print ("List the stock ticker (ex: WMT) and then the name (ex: Walmart)")
  firstOne = input("Ticker: ")
  secondOne = input("Name: ")

  ticker = firstOne

  table = yf.download(ticker)

  print(table)

print(stocks)


