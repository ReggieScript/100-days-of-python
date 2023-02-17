from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


options = Options()
options.add_experimental_option('detach', True)

## --- SELENIUM INSTALLATION

chrome_driver = r"C:\Users\reegi\Documents\CODING\chromedriver"

service = Service(chrome_driver)
driver = webdriver.Chrome(service=service, options=options)
 
driver.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")

# num_articles = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div[2]/p/b/a")
# num_articles.click() # funct to click on an element
# welcome = driver.find_element(By.LINK_TEXT,"Bienvenidos")
# welcome.click()
# print(num_articles.text)

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

print(driver.find_element(By.CLASS_NAME, "mw-page-title-main").text)

driver.quit()