# Stock Market

# Calculate daily change from close - previous close

import yfinance as yf

stocks = []

#Asks the user the amount of stocks they want to compare
numOfStocks = int(input("How many stocks do you want to compare? \n")) 
#Loop that iterates for the number of stocks that the user wants to compare
for i in range(numOfStocks):
  print("List the stock ticker (ex: WMT) and then the name (ex: Walmart)")
  firstOne = input("Ticker: ")
  secondOne = input("Name: ")

  ticker = firstOne

  table = yf.download(ticker)
  
  print("")
  print("")
  print("")
  print("")
  print("Daily Change for " + secondOne)
  print("")
  print(table)

print(stocks)
