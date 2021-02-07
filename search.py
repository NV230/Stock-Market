# Stock Market
"""
@authors: Keenan, Nibodh, Shahil
@Date: Feb 2021
@Version: 2.2

This program is designed to return the prices of stocks 

Allows the user to input the number stocks they want to compare and asks for the ticker for each stock.
""" 
# Calculate daily change from close - previous close

# yahoo finance library is where we get stock market information.
import yfinance as yf

# Creates an array to hold the inputted tickers 
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
