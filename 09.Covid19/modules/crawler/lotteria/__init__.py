import sys
import numpy as np
import pandas as pd
import time
import json
import re

# A Fast, Extensible Progress Bar for Python and CLI
from tqdm import tqdm

# A simple, yet elegant HTTP library.
from urllib.request import urlopen
import urllib.request
import urllib.parse
import requests

# Unix style pathname pattern expansion
from glob import glob

# A browser automation framework and ecosystem.
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller

# from pyvirtualdisplay import Display

# Beautiful Soup is a library that makes it easy to scrape information from web pages.
from bs4 import BeautifulSoup

# WebDriver is an open source tool for automated testing of webapps across many browsers.
path = chromedriver_autoinstaller.install()
driver = webdriver.Chrome(path)

baseUrl = 'https://www.lotteria.com/Shop/Shop_Ajax.asp'
driver.switch_to.window(driver.window_handles[0])
driver.get(baseUrl)

wait = WebDriverWait(driver, 10)


def paging():

    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.paging_basic')))

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    element = soup.select_one('div.paging_basic a:last-child')
    href = element.get('href')
    page = re.compile(r"(\d+)").search(href).group(1)

    return page


def main():

    # max_page = paging()

    # print(max_page)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table.list')))

    # html = driver.page_source
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    html = session.get(baseUrl, headers=headers).content
    soup = BeautifulSoup(html, 'html.parser')

    rows = soup.select('table.list tbody tr.shopSearch')
    data = []

    for row in rows:
        col = row.select_one('td.first').get_text(strip=True)
        data.append(col)

    return data


# quit() is a webdriver command which calls the driver.dispose method, which in turn closes all the browser windows and terminates the WebDriver session. If we do not use quit() at the end of program, the WebDriver session will not be closed properly and the files will not be cleared off memory. This may result in memory leak errors.
driver.quit()

main()
