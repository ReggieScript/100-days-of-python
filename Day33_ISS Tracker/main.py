import requests
from datetime import datetime

my_lat = 25.6866130
my_lon = -100.3161160

#obtaining ISS data

response = requests.get(url="http://api.open-notify.org/iss-now.json")

response.raise_for_status()

data = response.json()["iss_position"]

latitude = data["latitude"]
longitude = data["longitude"]



#Obtaining time nighttime data

parameters = {
    "lat": my_lat,
    "lng": my_lon,
    "formatted": 0,
}

response = requests.get(url = "https://api.sunrisesunset.io/json?", params = parameters)
response.raise_for_status()
data = response.json()

print(data)
# sunrise = data["results"]["sunrise"].split("T")[1]
# sunset = data["results"]["sunset"].split("T")[1]

# print(sunrise)
# print(sunset)

time_now = datetime.now()