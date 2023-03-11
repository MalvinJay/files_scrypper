import pandas as pd;
import os, re, requests, urllib 
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime, data, timedelta
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
import datetime
from dateparser.search import search_dates
from bs4 import BeautifulSoup
import glob as glob
from time import sleep

records = []

for count in range(1, 5):
    data = {}
    for i in range(1, 10):
        label = driver.find_element(By.XPATH, f'/html/body/div/table[4]/tr/th[{str(i)}]/a').text
        value = driver.find_element(By.XPATH, f'/html/body/div/table[4]/tr/th[{str(count)}]/td[{str(i)}]').text
        data.update({label:value})
    records.append({data})
