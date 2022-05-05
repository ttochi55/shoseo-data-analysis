# http://200.1.220.254:3000
# username: djy
# password: 1234

import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome(
    'C:/Users/shoseo/AppData/Local/Programs/Python/chromedriver')
# driver.maximize_window()  # 윈도우 최대 화면
driver.get('http://200.1.220.254:3000')
time.sleep(1)  # 1초간 대기

# login
driver.find_element_by_id('uid').send_keys('djy')
driver.find_element_by_css_selector('#pwd').send_keys('1234')
driver.find_element_by_class_name('btn.btn-primary').click()

# paging
ul = driver.find_element_by_css_selector('.pagination')
lis = ul.find_elements_by_tag_name('li')
total_pages = len(lis) - 2
