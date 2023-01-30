import requests
import smtplib
from newsapi import NewsApiClient


stock_key = ""
news_api = NewsApiClient(api_key="")
symbol = "AAPL"
stock_name= "Apple"

test_email = "" #Fill this with your email
pwd_email = "" #Email password


parameters_stock = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": symbol,
    "apikey": stock_key,
}

news = news_api.get_top_headlines(q = stock_name, language="en")

title = news["articles"][0]["title"]
brief = news["articles"][0]["content"]
url = news["articles"][0]["url"]

response = requests.get(url="https://www.alphavantage.co/query?", params= parameters_stock)

stock_data = response.json()
keys = list(stock_data["Time Series (Daily)"].keys()) #Instead of looking for the correct date, instead we grab the first two entries from the response.

yesturday_data = stock_data["Time Series (Daily)"][keys[0]]["4. close"]
yesturday2_data = stock_data["Time Series (Daily)"][keys[1]]["4. close"]

def check_difference(dif):
    if dif < 0 :
        return "DOWN"
    else:
        return "UP"

def percentage(dif):
    per = abs(dif/float(yesturday2_data))*100
    return per

difference = float(yesturday_data) - float(yesturday2_data)
behaviour = check_difference(difference)
stock_per = percentage(difference)

letter = f"Subject: {stock_name} Stock Update!\n\n{symbol} {behaviour} {round(stock_per)}%\n\nHeadline:{title} \nBrief: {brief}\n\nLearn More: {url}"

def send_mail():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=test_email, password=pwd_email)
        try:
            connection.sendmail(from_addr=test_email, to_addrs="regina.crespo.018@gmail.com",
                        msg=letter)
        except:
            connection.sendmail(from_addr=test_email, to_addrs="regina.crespo.018@gmail.com",
                        msg=letter.replace("…", "..."))
        connection.close()

send_mail()