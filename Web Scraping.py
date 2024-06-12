from selenium import webdriver
import urllib.request
import selenium
import time
from bs4 import BeautifulSoup
import pandas as pd
import requests
import cfscrape
from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://money18.on.cc/info/hk/liveinfo_quote_02382.html')
r.html.render()
soup = BeautifulSoup(r.html.html, 'html.parser')
filter = soup.find("div", class_="text-right stock-price")
filter2= filter.find("span", class_="value")
print(filter)
print(filter2)
result = "" + filter2.get_text()
print(result)

