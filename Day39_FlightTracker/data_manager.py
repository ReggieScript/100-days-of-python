import requests

sheety_url = "https://api.sheety.co/cd7eaf60ce68ea180b72c2883cd73550/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.response = requests.get(url = sheety_url)
        self.response_data = self.response.json()