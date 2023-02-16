from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

## --- SELENIUM INSTALLATION

chrome_driver = r"C:\Users\reegi\Documents\CODING\chromedriver"

service = Service(chrome_driver)
driver = webdriver.Chrome(service=service)
 
driver.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")

num_articles = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div[2]/p/b/a")

print(num_articles.text)