import time
import sys
import json
import csv
from time import sleep
import os.path
import re

from random import randint
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.common.exceptions import NoSuchElementException


#to use: python azlyrics_scraper.py input_file output_file
#input file is the file with one column of links to trailhead links
#output file is the file to write scrapped data to
#both files are to be in csv type


def urlify(s):
    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", ' ', s)
    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '+', s)
    return s

def remove_last_word(s):
    s = s.rsplit(' ', 1)[0]
    return s

if len(sys.argv) != 3:
    print()
    print("To use: python trailhead_scraper.py input_file output_file")
    print("input file is the file with links to trailhead links")
    print("output file is the file to write scrapped data to")
    print("both files are to be in csv type")
    sys.exit()


input_file = sys.argv[1]
output_file = sys.argv[2]

songs = []

#get links from csv
with open(input_file, 'r') as file:
    for line in file:
        if len(line.strip()) > 0:
            songs.append(line.strip())

#remove headers
songs = songs[1:]

driver = webdriver.Chrome('./chromedriver.exe')



driver.implicitly_wait(120)
driver.maximize_window()


all_lyrics = []
all_titles = []
all_artists = []


urls = []

for title in songs:
    
    driver.get("https://search.azlyrics.com/search.php?q=" + urlify(title))

    sleep(randint(1,2))
    size = len(driver.find_elements_by_xpath('/html/body/div[3]/div/div/div/table/tbody/tr'))
    
    print("=== Crawl ===")

    if (size == 0):
        url_song=""
    elif(size == 1):
        url_song = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/table/tbody/tr/td/a').get_attribute('href')
    elif(size >= 20):
        url_song = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/table/tbody/tr[2]/td/a').get_attribute('href')
    else:
        url_song = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/table/tbody/tr[1]/td/a').get_attribute('href')
        if(url_song.find("search")):
            url_song = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/table/tbody/tr[2]/td/a').get_attribute('href')
    print(url_song)

        

    urls.append(url_song)


print(urls)

count = 0

for song in urls:
    if count == 40:
        sleep(randint(30,60))

    if song != "":
        driver.get(song)

        sleep(randint(2,3))

        try:
            artist = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[3]/h2/b').text
            artist = remove_last_word(artist)
        except:
            artist = "none"

        try:
            title = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/b').text
            title = title.replace('"', '')
        except:
            title = "none"

        try:
            lyrics = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[5]').text
        except:
            lyrics = "none"

        print(title)
        print(artist)
        print(lyrics)

        all_titles.append(title)
        all_artists.append(artist)
        all_lyrics.append(lyrics)
    else:
        all_titles.append("none")
        all_artists.append("none")
        all_lyrics.append("none")
     
    print("Retrieval DONE!")
    count = count + 1


driver.quit()

with (open(output_file, 'w', newline='', encoding='utf-8')) as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'arist', 'lyrics'])

    for i in range(0,len(all_titles)):
        to_write = [all_titles[i], all_artists[i], all_lyrics[i]]
        writer.writerow(to_write)
