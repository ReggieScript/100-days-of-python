from bs4 import BeautifulSoup
import requests
from pprint import pprint
import spotipy

# date = input("What year do you want to travel to? Type the date in YYYY-MM-DD format: ")

date = "2000-03-22"

response = requests.get(url = f"https://www.billboard.com/charts/hot-100/{date}")

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.select("h3.c-title.a-no-trucate.a-font-primary-bold-s.u-letter-spacing-0021")

authors = soup.select("span.c-label.a-no-trucate.a-font-primary-s")

playlist = []
for i in range(0,len(titles)):
    playlist.append((titles[i].get_text().strip(),authors[i].get_text().strip()))

pprint(playlist[20])