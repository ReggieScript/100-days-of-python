from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()

username_link = os.getenv("USERNAME_LINK")
password = os.getenv("PASSWORD")


options = Options()
options.add_experimental_option('detach', True)

## --- SELENIUM INSTALLATION

chrome_driver = r"C:\Users\reegi\Documents\CODING\chromedriver"

service = Service(chrome_driver)
driver = webdriver.Chrome(service=service, options=options)
 
driver.get("https://www.linkedin.com/jobs/")

us =driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form/div[2]/div[1]/input")
us.send_keys(username_link)

ps = driver.find_element(By.XPATH,"/html/body/main/section[1]/div/div/form/div[2]/div[2]/input")
ps.send_keys(password)

driver.find_element(By.XPATH,'//*[@id="main-content"]/section[1]/div/div/form/button').click()

time.sleep(5)

# driver.find_element(By.CLASS_NAME, "mercado-match").click()

# time.sleep(3)

job_search = driver.find_element(By.ID, "jobs-search-box-keyword-id-ember23")
job_search.send_keys("junior python developer")
time.sleep(1)
loc = driver.find_element(By.XPATH, '')
job_search.send_keys(Keys.ENTER)
