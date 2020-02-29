import time
import csv
import pandas as pd
from time import sleep
import os.path
from random import randint
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import selenium.common.exceptions as selexcept
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
# available since 2.26.0
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


url="https://open.spotify.com/search"
file = open(r'C:\Users\Li Yiyao\Desktop\Codes\DM_Music\songnames.csv','r')
driver = webdriver.Chrome(r'C:\Users\Li Yiyao\Desktop\Codes\Chrome79\chromedriver.exe')
driver.implicitly_wait(120)
driver.get(url)
driver.maximize_window()

# temp = []
final = []
# try:
#     csv_reader = csv.reader(file,delimiter = ',')
#     next(csv_reader)
#     for row in csv_reader:
#         # element = driver.find_element_by_xpath('/html/body/div[3]/div/div[4]/div[1]/header/div[3]/div/label/input')
#         element = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/header/div[3]/div/label/input')
#         print(row[0])
#         # input_str = row[1] + ' ' + row[2]
#         element.send_keys(row[0])
#         # input_str = ""
#         sleep(randint(2,3))
#         # driver.find_element_by_xpath('/html/body/div[3]/div/div[4]/div[4]/div[1]/div/div[2]/div/div/div/section[1]/div/div[2]/div/div/div/div[4]').click()
#         # driver.find_element_by_xpath('/html/body/div[3]/div/div[4]/div[4]/div[1]/div/div[2]/div/div/div/section[2]/div/div[1]/div/div/div[3]/a').click()
#         driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/div/div/div/section[2]/div/div[1]/div/div/div[3]/a').click()
#         sleep(randint(2,3))
#         print(driver.current_url.split(":")[3])
#         temp = [row[0],driver.current_url.split(":")[3]]
#         driver.get(url)
#         # sleep(randint(2,3))
#         final.append(temp)
#         temp = []
#         print("go next")
#     df = pd.DataFrame(final,columns = ['Song Name','Spotify Id'])
#     df.to_csv("spotify_Song_Ids_1.csv")
#     # element = driver.find_element_by_xpath('/html/body/div[3]/div/div[4]/div[1]/header/div[3]/div/label/input')
#     # element.send_keys("night of the hunter")
#     # sleep(randint(2,3))
#     # # driver.find_element_by_xpath('/html/body/div[3]/div/div[4]/div[4]/div[1]/div/div[2]/div/div/div/section[1]/div/div[2]/div/div/div/div[4]').click()
#     # driver.find_element_by_xpath('/html/body/div[3]/div/div[4]/div[4]/div[1]/div/div[2]/div/div/div/section[2]/div/div[1]/div/div/div[3]/a').click()
#     # sleep(randint(2,3))
#     # print(driver.current_url.split(":")[3])

# except Exception as e:
#     print(e)
# finally:
#     driver.quit()
link_array = []
temp = []
try:
    csv_reader = csv.reader(file,delimiter = ',')
    next(csv_reader)
    for row in csv_reader:
        driver.implicitly_wait(120)
        element = driver.find_element(By.TAG_NAME,'input')
        element.send_keys(row[0])
        sleep(randint(2,3))
        links = driver.find_elements(By.TAG_NAME,"a")
        # print(links[13].get_attribute('href').split("track/")[1])
        for link in links:
            if "track/" in link.get_attribute('href'):
                link_array.append(link.get_attribute('href'))
        print(row[0]  +' ' +link_array[0].split("track/")[1])
        temp = [row[0],link_array[0].split("track/")[1]]
        final.append(temp)
        link_array = []
        temp = []
        sleep(randint(2,3))
        driver.get(url)
    df = pd.DataFrame(final,columns = ['Song Name','Spotify Id'])
    df.to_csv("spotify_Song_Ids_1.csv")
except Exception as e:
    print(e)
# finally:
#     driver.quit()

# try:

#     element = driver.find_element(By.TAG_NAME,'input')
#     element.send_keys("Whole Heart Hillsong United")
#     sleep(randint(2,3))
#     links = driver.find_elements(By.TAG_NAME,"a")
#         # print(links[13].get_attribute('href').split("track/")[1])
#     for link in links:
#         if "track/" in link.get_attribute('href'):
#             link_array.append(link.get_attribute('href'))
#     print(link_array[0].split("track/")[1])
# #         temp = [row[0],link_array[0].split("track/")[1]]
# #         final.append(temp)
# #         link_array = []
# #         temp = []
# #         sleep(randint(2,3))
# #         driver.get(url)
# #     df = pd.DataFrame(final,columns = ['Song Name','Spotify Id'])
# #     df.to_csv("spotify_Song_Ids_1.csv")
# except Exception as e:
#     print(e)