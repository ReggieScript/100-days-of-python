import requests
from datetime import datetime
import smtplib
import time

my_lat = 0 #fill with your lat
my_lon = 0 #fill wwith your long
your_city = "" #fill with your city

letter = f"Subject: Look up!\n\nThe International Space Station is right above {your_city}, look up!"

list_mails = () #fill with a list of emails you would like to send to the notifications

test_email = "" #Fill this with your email
pwd_email = "" #Email password

#obtaining ISS data

def iss_loc_api():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    response.raise_for_status()

    data = response.json()["iss_position"]

    latitude = float(data["latitude"])
    longitude = float(data["longitude"])

    return latitude,longitude

def send():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=test_email, password=pwd_email)
        for mail in list_mails:
            connection.sendmail(from_addr=test_email, to_addrs=mail,
                            msg=letter)
        connection.close()

#Obtaining time nighttime data

parameters = {
    "lat": my_lat,
    "lng": my_lon,
    "formatted": 0,
}


response = requests.get(url = "https://api.sunrisesunset.io/json?", params = parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data['results']['sunrise'].split(':')[0])
sunset = int(data['results']['sunset'].split(':')[0]) + 12 # To set it to 24 hour time

time_now = datetime.now()

while time_now.hour >= sunset or time_now.hour <= sunrise:
    time.sleep(120)
    iss_loc = iss_loc_api()
    latitude = iss_loc[0]
    longitude = iss_loc[1]
    if (latitude > my_lat - 5 and latitude < my_lat + 5) and (longitude > my_lon - 5 and longitude < my_lon + 5):
        send()
    time_now = datetime.now()