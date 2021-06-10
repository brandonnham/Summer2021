import time

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/Brand/Desktop/Software/WebDrivers/chromedriver.exe')

driver.get('https://tracker.gg/valorant/profile/riot/chung%23yung/overview')
#driver.get('https://tracker.gg/valorant/profile/riot/skunkydude13%232495/overview')

content = driver.page_source
soup = BeautifulSoup(content)

results = []

gamemodes = []
#gamemodes.append('9D 17H 49M Play Time')
#gamemodes.append('5H 47M 50S Play Time')
#gamemodes.append('49M 36S Play Time')
#gamemodes.append('5H 43M 19S Play Time')
#gamemodes.append('2D 23H 00M Play Time')



gamemodes.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[3]/div[4]/div[1]/div/div/span[1]').text)

driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[2]/a[2]').click()
gamemodes.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[3]/div[3]/div[1]/div/div/span[1]').text)

driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[2]/a[3]').click()
gamemodes.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[3]/div[3]/div[1]/div/div/span[1]').text)

driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[2]/a[4]').click()
gamemodes.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[3]/div[4]/div[1]/div/div/span[1]').text)

driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[2]/a[5]').click()
gamemodes.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[3]/div[4]/div[1]/div/div/span[1]').text)

#print(gamemodes)

#do math
total_time = 0;
for element in gamemodes:
    total = [];
    parse_time = element.split(' ');

    if ('H' not in element):
        total.append(parse_time[0][0:len(parse_time[0]) - 1])
        total.append(parse_time[1][0:len(parse_time[1]) - 1])

        time = int(total[0])/ 60 + int(total[1])/3600
        total_time += time
        total = []

    if ('D' in element):
        #print('DAY')
        total.append(parse_time[0][0:len(parse_time[0])-1])
        total.append(parse_time[1][0:len(parse_time[1])-1])
        total.append(parse_time[2][0:len(parse_time[2])-1])

        time = 24*int(total[0]) + int(total[1]) + int(total[2])/60
        total_time += time
        #print(time)
        total = []

    #print(total)

    if ('S' in element and 'H' in element):
        #print('SEC')
        total.append(parse_time[0][0:len(parse_time[0]) - 1])
        total.append(parse_time[1][0:len(parse_time[1]) - 1])
        total.append(parse_time[2][0:len(parse_time[2]) - 1])

        time = int(total[0]) + int(total[1])/60 + int(total[2])/3600
        total_time += time

    print(str(total_time))

