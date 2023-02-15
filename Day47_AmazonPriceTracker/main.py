import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

# VARIABLES

send_email = os.getenv("MAIL_SEND") 
recieve_email = os.getenv("MAIL_RECIEVE")
password = os.getenv("PASSWORD")

print(send_email, recieve_email, password)

HEADERS = (
    {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        'Accept-Language': "es-ES,es;q=0.9",
    }
)

item_url = "https://www.amazon.com.mx/SAMSUNG-Monitor-Smart-Experiencia-Dise%C3%B1o/dp/B09XVPDWSP/"

target_price = 14000

response = requests.get(url = item_url, headers = HEADERS)

soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(class_ = "a-price-whole").text
price = price.replace(".","")
price = int(price.replace(",", ""))

name = soup.find("h1",id ="title")

letter = f"Subject: Item in price range!\n\n The item {name} is on your requested price range at {price}. Go for it! {item_url}".encode("utf-8")

def send_mail():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(user=send_email, password=password)
        connection.sendmail(from_addr=send_email, to_addrs=recieve_email,msg=letter)
        connection.close()

if price < target_price:
    send_mail()
