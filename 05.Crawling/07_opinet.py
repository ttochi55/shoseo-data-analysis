# 싼 주유소 찾기: 오피넷
# http://www.opinet.co.kr/

import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# conda install -c conda-forge tqdm
from tqdm import tqdm
from tqdm import tqdm_notebook

driver = webdriver.Chrome(
    'C:/Users/shoseo/AppData/Local/Programs/Python/chromedriver')
# driver.maximize_window()  # 윈도우 최대 화면
driver.switch_to.window(driver.window_handles[0])
driver.get('http://www.opinet.co.kr/')
time.sleep(1)  # 1초간 대기

# 지역별 싼 주유소 찾기
# 자주찾는 메뉴 > 싼 주유소 찾기
# http://www.opinet.co.kr/searRgSelect.do
driver.find_element_by_css_selector('#quick_ul li:nth-child(2)').click()
time.sleep(1)

# 지역선택
# gu_list_raw = driver.find_element_by_id('SIGUNGU_NM0')
gu_list_raw = driver.find_element_by_xpath('//*[@id="SIGUNGU_NM0"]')
gu_list = gu_list_raw.find_elements_by_tag_name('option')
gu_names = [option.get_attribute('value') for option in gu_list]
gu_names.remove('')
# gu_names = []
# for gu in gu_list:
#   gu_names.append(gu)
#   gu_names.remove('')
# print(gu_names)

# 엑셀저장
# gu_list_raw = driver.find_element_by_id('SIGUNGU_NM0')
# gu_list_raw.send_keys(gu_names[0])
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="glopopd_excel"]').click()

# print(gu_names)

# 25개 자치구에 대해서 엑셀 다운로드
for gu in gu_names:
    print(gu)
    region = driver.find_element_by_xpath('//*[@id="SIGUNGU_NM0"]')
    region.send_keys(gu)
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="glopopd_excel"]').click()
    time.sleep(2)

driver.close()
driver.quit()
