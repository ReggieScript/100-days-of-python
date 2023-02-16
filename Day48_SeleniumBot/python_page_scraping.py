from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

## --- SELENIUM INSTALLATION

chrome_driver = r"C:\Users\reegi\Documents\CODING\chromedriver"

service = Service(chrome_driver)
driver = webdriver.Chrome(service=service)
 
driver.get("https://www.python.org/")

list = driver.find_elements(By.XPATH, "/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li")

events = {}
key = 0
for item in list:
    events[f"{key}"] = {"time":item.find_element(By.TAG_NAME, "time").text, "name": item.find_element(By.TAG_NAME, "a").text}
    key+=1

print(events)

driver.quit()