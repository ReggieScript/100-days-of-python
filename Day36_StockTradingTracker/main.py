import requests
import datetime
import smtplib
from newsapi import NewsApiClient
import pandas
import os

stock_key = ""
news_api = NewsApiClient(api_key="")

letter = f""

test_email = "" #Fill this with your email
pwd_email = "" #Email password

parameters_stock = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "AAPL",
    "apikey": stock_key,
}

news = news_api.get_top_headlines(q = "Apple", category = "business")

response = requests.get(url="https://www.alphavantage.co/query?", params= parameters_stock)

stock_data = response.json()
keys = list(stock_data["Time Series (Daily)"].keys()) #Instead of looking for the correct date, instead we grab the first two entries from the response.

yesturday_data = stock_data["Time Series (Daily)"][keys[0]]["4. close"]
yesturday2_data = stock_data["Time Series (Daily)"][keys[1]]["4. close"]

difference = float(yesturday_data)-float(yesturday2_data)

