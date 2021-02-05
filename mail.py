# Stock Market

"""
@authors: Keenan, Nibodh, Shahil
@Date: Feb 2021

This program is designed to return 

Allows the user to recive an email when their desired stock reaches a target price
""" 
#Imports all the python libraries
# SMTPBLIB - SIMPLE MAIL TRANSFER PROTOCOL
import smtplib
from email.message import EmailMessage
import yfinance as yf
#Date time allows to check stock price at specifici time
import datetime as dt
# Pandas - reads data on json file
from pandas_datareader import data as pdr
import time


#The Email and password of the account sending the email
EMAIL_ADDRESS = 'stockmarketcsa@gmail.com'
EMAIL_PASSWORD = 'passwordtest'

msg = EmailMessage()

yf.pdr_override() 
start =dt.datetime(2020,12,1)
now = dt.datetime.now()

stock=""

#Checks to see if ticker (stock) has passed that price.
TargetPrice = 0

sendMail = False;

#User Input to collect email
input1 = input("Do you want to get email notifications for a certain stock? (yes/no) \n")

if (input1 == "yes"): 
  sendMail = True;
  stock = input("Please type the stock ticker. (ex: AAPL) \n")
  df = pdr.get_data_yahoo(stock, start, now)
  currentClose = df["Adj Close"][-1]
  message = "Current Price: "+ str(currentClose)
  print(message)
  TargetPrice = int(input("What is your target price? \n"))
  userEmail = input("Please type your email address. (ex: stockmarketcsa@gmail.com) \n")

  # Email Body
  msg['Subject'] = 'Requested Stock '+ stock+'!'
  msg['From'] = EMAIL_ADDRESS
  msg['To'] = userEmail

  print("You will recieve an email when " + stock + " reaches " + str(TargetPrice) + " dollars.")

alerted=False

while sendMail:
#Retrieves the stock data from yahoo finance
	df = pdr.get_data_yahoo(stock, start, now)
	currentClose=df["Adj Close"][-1]

	condition=currentClose>TargetPrice

  #If the price that the user selects meets the actual stock price then condition is set to true.
	if(condition and alerted==False):

		alerted=True

		message =stock +" has activated the alert price of "+ str(TargetPrice) +\
		 "\nCurrent Price: "+ str(currentClose)

		print(message)
		msg.set_content(message)

#Code needed to send the email. Uses SMTP (Simple Mail Tranfer Protocol). If there is no alerts, the code will still send one.
		with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
		    smtp.send_message(msg)

		    print("completed")
	else:
		print("No new alerts")
  
  # To prevent an infinite loop and pauses for 60 seconds.
	time.sleep(60)
  