from bs4 import BeautifulSoup
import requests
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

date = input("What year do you want to travel to? Type the date in YYYY-MM-DD format: ")

OAUTH_AUTHORIZE_URL= 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL= 'https://accounts.spotify.com/api/token'

response = requests.get(url = f"https://www.billboard.com/charts/hot-100/{date}")

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.select("h3.c-title.a-no-trucate.a-font-primary-bold-s.u-letter-spacing-0021")

authors = soup.select("span.c-label.a-no-trucate.a-font-primary-s")

CLIENT = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SCT = os.getenv("SPOTIPY_CLIENT_SECRET")
USER = os.getenv("USERID")

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",redirect_uri="http://localhost:8080/",client_id=CLIENT,client_secret=CLIENT_SCT,show_dialog=True,cache_path="token.txt"))

playlist = []
playlist_URI = []

for i in range(0,len(titles)):
    song = titles[i].get_text().strip()
    author = authors[i].get_text().strip()
    playlist.append(song)
    try:
        playlist_URI.append(spotify.search(q = f"{song} {author}",limit = 1, type = "track")["tracks"]["items"][0]["uri"])
    except:
        pass

playlist_final = spotify.user_playlist_create(user=spotify.current_user()["id"], name = f"Time Machine: {date}", public=False, collaborative=False, description="Billboard's Hot 100 back in time.")
spotify.playlist_add_items(playlist_id = playlist_final["id"], items = playlist_URI)