from typing import List, Text
from urllib import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv

page = 'https://www.yad2.co.il/vehicles/commercial-cars?manufacturer=69&model=1664'
header = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.115' 

open_url = urlopen(page)
read_url = open_url.read()
html_soup = BeautifulSoup(read_url, 'html.parser')

item_grid = html_soup.find_all('div', class_="column_large")
item_row = item_grid.find('div', class_="feeditem table")

for item in item_grid:
     item = item.find('div', class_="feeditem table")

middle = item.find('div', class_="middle_col")
owners = middle.find_all('span', class_="data")
print(owners)

feed = item.find('div', class_='feed_list')
title = feed.find_all('span', class_= "title")
print(title)
