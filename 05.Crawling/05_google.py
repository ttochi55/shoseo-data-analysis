import pandas as pd
import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(
    'C:/Users/shoseo/AppData/Local/Programs/Python/chromedriver')
driver.maximize_window()  # 윈도우 최대 화면
driver.get('http://www.google.com')
time.sleep(1)  # 1초간 대기

search_box = driver.find_element_by_name('q')  # element name
search_box.send_keys('ChromeDriver')  # 키워드 입력
search_box.submit()
time.sleep(2)  # 2초간 대기

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Use Single Selector
# divs = soup.select('.g')
# title_list = []; content_list = []
# for div in divs:
#     title = div.select_one('.LC20lb.DKV0Md').get_text()
#     content = div.select_one('.aCOpRe').get_text()
#     title_list.append(title)
#     content_list.append(content)

# Use Plural Selector
divs = driver.find_elements_by_css_selector('.g')
title_list = []
content_list = []

for div in divs:
    title = div.find_elements_by_css_selector('.LC20lb.DKV0Md').text()
    content = div.find_elements_by_css_selector('.aCOpRe').text()
    title_list.append(title)
    content_list.append(content)

df = pd.DataFrame({
    'title': title_list,
    'content': content_list,
})

df.to_csv('google.csv', sep='|', encoding='utf8')
