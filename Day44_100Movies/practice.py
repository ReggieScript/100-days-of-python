from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

response_soup = BeautifulSoup(response.text,"html.parser")

articles = response_soup.findAll(class_="titleline")

article_texts = []
article_links =[]

for text in response_soup.find_all(class_ = "titleline"):
    try:
        article_texts.append(text.get_text())
        article_links.append(text.find("a").get("href"))
    except:
        pass

article_score = [score.get_text() for score in response_soup.find_all(name = "span", class_="score")]

high_score = 0
for item in article_score:
    item_score = item.split(" ")
    if int(item_score[0]) > high_score:
        high_index = article_score.index(item)
        high_score = int(item_score[0])

print(article_texts[high_index])
print(article_links[high_index])
print(article_score[high_index])