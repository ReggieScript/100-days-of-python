import smtplib
import datetime as dt
import pandas
import random

templates = ["Day32_Mail SMTP\letter_templates\letter_1.txt",
             "Day32_Mail SMTP\letter_templates\letter_2.txt", "Day32_Mail SMTP\letter_templates\letter_3.txt"]
test_email = "" #Fill this with your email
pwd_email = "" #Email password

def send(letter, mail):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=test_email, password=pwd_email)
        connection.sendmail(from_addr=test_email, to_addrs=mail,
                            msg=letter)
        connection.close()


def bday_letter(name):
    with open(random.choice(templates), "r") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", name)
        return letter


birthdays = pandas.read_csv(
    r"Day32_Mail SMTP\birthdays.csv").to_dict(orient='index')
now = dt.datetime.now()

print(birthdays)

for key in birthdays:
    bday_name = birthdays[key]['name']
    bday_email = birthdays[key]['email']
    bday_month = birthdays[key]['month']
    bday_day = birthdays[key]['day']
    if bday_day == now.day and bday_month == now.month:
        new_letter = bday_letter(bday_name)
        send(new_letter,bday_email)
