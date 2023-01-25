import datetime as dt
import smtplib
import random

test_email="" #Your gmail here
pwd_email="" #Your password here
real_email="" #The email you want to send to

now=dt.datetime.now()
with open("Day32_Mail SMTP\quotes.txt", "r") as quotes:
    quotes_lines=quotes.read().splitlines()
    if now.weekday() == 0:
        random_quote= random.choice(quotes_lines)
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
         connection.starttls()
         connection.login(user=test_email,password=pwd_email)
         connection.sendmail(from_addr=test_email, to_addrs=real_email, msg=f"Subject: Quote of the day...\n\n{random_quote}\n\nHave a great Monday!")
