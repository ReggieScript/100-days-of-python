import requests

api_key = ""
city = "Monterrey"


parameters = {
    "q": city,
    "appid": api_key,
    "units": "metric",
}

response = requests.get(url = "https://api.openweathermap.org/data/2.5/forecast?", params = parameters)

weather_data = response.json()

for item in weather_data["list"]:
    hour_weather = item["weather"][0]["main"]
    date = item["dt_txt"]
    print(date)
    print(hour_weather)