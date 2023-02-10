import requests
from bs4 import BeautifulSoup
import random
 
response = requests.get(url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

movies = [item.get_text() for item in soup.find_all("h3", class_="title")]
movies.reverse()

with open("Day44_100Movies/100_movies.txt", "w", encoding= "utf-8") as file:
    for movie in movies:
        file.write(movie+"\n")

print(f"You should watch: {random.choice(movies)}")