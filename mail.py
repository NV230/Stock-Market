#imports all the python libraries
import smtplib
from email.message import EmailMessage
import yfinance as yf
import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr
import time


#The Email and password of the account sending the email
EMAIL_ADDRESS = 'stockmarketcsa@gmail.com'
EMAIL_PASSWORD = 'passwordtest'

msg = EmailMessage()

yf.pdr_override() 
start =dt.datetime(2020,12,1)
now = dt.datetime.now()

stock="AAPL"
#Checks to see if ticker (stock) has passed that price.
TargetPrice=50

msg['Subject'] = 'Alert on '+ stock+'!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'stockmarketcsa@gmail.com'

alerted=False

while 1:
#Gets the stock data from yahoo finance
	df = pdr.get_data_yahoo(stock, start, now)
	currentClose=df["Adj Close"][-1]

	condition=currentClose>TargetPrice

#If the price that the user selects meets the actual stock price then condition is set to true.
	if(condition and alerted==False):

		alerted=True

		message=stock +" Has activated the alert price of "+ str(TargetPrice) +\
		 "\nCurrent Price: "+ str(currentClose)

		print(message)
		msg.set_content(message)

#Code needed to send the email. Uses SMTP. If there is no alerts, the code will still send one.
		with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
		    smtp.send_message(msg)

		    print("completed")
	else:
		print("No new alerts")
  
  # To prevent an infinite loop and pauses for 60 seconds.
	time.sleep(60)
  