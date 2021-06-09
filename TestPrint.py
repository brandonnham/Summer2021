import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/Brand/Desktop/Software/WebDrivers/chromedriver.exe')
driver.get('http://cnn.com')

results = []
content = driver.page_source
soup = BeautifulSoup(content)

for element in soup.findAll(attrs='cd__wrapper'):
    name = element.find('h3')
    if name not in results:
        results.append(name.text)
print(results)