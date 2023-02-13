from bs4 import BeautifulSoup
import requests
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

# date = input("What year do you want to travel to? Type the date in YYYY-MM-DD format: ")

date = "2000-03-22"

response = requests.get(url = f"https://www.billboard.com/charts/hot-100/{date}")

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.select("h3.c-title.a-no-trucate.a-font-primary-bold-s.u-letter-spacing-0021")

authors = soup.select("span.c-label.a-no-trucate.a-font-primary-s")

CLIENT = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SCT = os.getenv("SPOTIPY_CLIENT_SECRET")
USER = os.getenv("USERID")

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

playlist = []
playlist_URI = []

print(CLIENT, CLIENT_SCT)

for i in range(0,len(titles)):
    song = titles[i].get_text().strip()
    playlist.append(song)
    try:
        playlist_URI.append(spotify.search(q = song,limit = 1, type = "track")["tracks"]["items"][0]["uri"])
    except:
        pass

playlist_final = spotify.user_playlist_create(user=spotify.current_user()["id"], name = f"Time Machine: {date}", public=False, collaborative=False, description="Billboard's Hot 100 back in time.")

spotify.playlist_add_items(id = playlist_final["id"], items = playlist_URI)
