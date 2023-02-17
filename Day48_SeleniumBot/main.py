from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_experimental_option('detach', True)

## --- SELENIUM INSTALLATION

chrome_driver = r"C:\Users\reegi\Documents\CODING\chromedriver"

service = Service(chrome_driver)
driver = webdriver.Chrome(service=service, options=options)
 
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(3)

try:
    lang = driver.find_element(By.ID, "langSelect-EN") 
    lang.click() #click on the language
except:
    pass

time.sleep(3)

cookie = driver.find_element(By.ID, "bigCookie")

mins = time.time() + (60*5)
seconds = time.time() + 5

def store():
    items = driver.find_elements(By.CLASS_NAME, "product.unlocked.enabled")
    try:
        items.pop().click()
    except:
        pass
    return

while time.time() < mins:
    cookie.click()
    if time.time() >= seconds:
        store()
        seconds = time.time() + 5

print(driver.find_element(By.ID, "cookies").text)

driver.close()