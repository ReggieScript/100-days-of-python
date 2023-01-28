import requests
import datetime
import smtplib

api_key = ""
city = "" #Fill this with your city

letter = f"Subject: Cloudy Day\n\nBring an umbrella with you. Today is going to be a rainy day!"

test_email = "" #Fill this with your email
pwd_email = "" #Email password

parameters = {
    "q": city,
    "appid": api_key,
    "units": "metric",
}


response = requests.get(url = "https://api.openweathermap.org/data/2.5/forecast?", params = parameters)

weather_data = response.json()
tomorrow = datetime.date.today() + datetime.timedelta(days=1)

def send_mail():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=test_email, password=pwd_email)

        connection.sendmail(from_addr=test_email, to_addrs="regina.crespo.018@gmail.com",
                        msg=letter)
        connection.close()


for item in weather_data["list"]:
    date_month = "".join(item["dt_txt"][5:7])
    date_day = "".join(item["dt_txt"][8:10])
    if int(date_day) == tomorrow.day and int(date_month) == tomorrow.month:
        hour_weather = item["weather"][0]["main"]
        if hour_weather == "Rain":
            send_mail()
            break