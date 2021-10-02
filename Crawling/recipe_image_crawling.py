import urllib.request
from urllib.error import URLError, HTTPError
import pandas as pd
import numpy as np
import sqlite3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


con = sqlite3.connect('../db.sqlite3')
cur = con.cursor()
df = pd.read_sql_query("select rcp_nm from recipe_api_info  ; " ,con )

df_list = df.values.tolist()

driver = webdriver.Chrome()

df_list = ['감자','배']

for df in df_list:
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")
    elem = driver.find_element_by_name("q")
    elem.send_keys(df)
    elem.send_keys(Keys.ENTER)

    driver.find_elements_by_css_selector("#islrg > div.islrc > div:nth-child(1) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img")[0].click()
    src = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute('src')

    try:
        urllib.request.urlretrieve(src, f'../static/image/standard/{df[0]}.jpg')
    except HTTPError as e:
        err = e.read()
        code = e.getcode()
        print('------------')
        print(code)  ## 404
        print('------------')

    # driver.back()