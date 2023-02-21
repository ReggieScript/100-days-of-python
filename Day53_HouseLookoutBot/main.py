from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option('detach', True)

chrome_driver = r"C:\Users\reegi\Documents\CODING\chromedriver"

service = Service(chrome_driver)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://forms.gle/jWHGM4i2nzqaHkND7")

HEADERS = (
    {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        'Accept-Language': "es-ES,es;q=0.9",
    }
)

# Send the data from zillow
response = requests.get('https://www.zillow.com/austin-tx/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Austin%2C%20TX%22%2C%22mapBounds%22%3A%7B%22west%22%3A-98.18007511914062%2C%22east%22%3A-97.45223088085937%2C%22south%22%3A30.036288609064826%2C%22north%22%3A30.550910202155425%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A10221%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A601150%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D', headers = HEADERS)

soup = BeautifulSoup(response.content, "html.parser")

data = soup.select(selector = "div.StyledPropertyCardDataWrapper-c11n-8-84-2__sc-1omp4c3-0.jIcpOJ.property-card-data")

def send_form(input_data):
    form_address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_send = driver.find_element(By.CLASS_NAME, "NPEfkd.RveJvd.snByac")
    
    form_address.send_keys(input_data[0])
    form_price.send_keys(input_data[1])
    form_link.send_keys(input_data[2])

    form_send.click()
    driver.back() #Reload the page
    time.sleep(1)

full_data = []

for item in data:
    address = item.find(name = "address").text
    price = item.find("span").text.split("+")[0]
    link = "https://www.zillow.com/" + item.find("a")['href']
    full_data.append([address, price, link])

for item in full_data:
    send_form(item)
