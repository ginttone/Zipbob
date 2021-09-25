import urllib.request
from urllib.error import URLError, HTTPError
import pandas as pd
import numpy as np
import math
import sqlite3
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os
import shutil

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--headless')
chrome_option.add_argument('--no-sandbox')
chrome_option.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome('./chromedriver.exe',options=chrome_option)
# driver = webdriver.Chrome()

con = sqlite3.connect('../db.sqlite3')
cur = con.cursor()
df = pd.read_sql_query("select distinct itemnm from standard order by 1  ; " ,con )
df_list = df.values.tolist()

# df_list = [['귀리']]

try:

    for df in df_list:

        url_df = 'https://www.10000recipe.com/recipe/list.html?q='+ df[0]

        driver.get(url_df)
        # print(df[0])
        cnt = int(driver.find_element_by_css_selector("#contents_area_full > ul > div > b").text.replace(',',''))
        # print(cnt)
        contents_df = len(driver.find_elements_by_xpath("//*[@id='contents_area_full']/ul/ul/li"))
        # print(contents_df)
        page = math.ceil(cnt/contents_df)+1
        # print(page)

        for i in range(1,6):
            url = 'https://www.10000recipe.com/recipe/list.html?q=' + df[0] + '&order=reco&page=' + str(i)
            driver.get(url)
            print(url)
            contents = int(len(driver.find_elements_by_xpath("//*[@id='contents_area_full']/ul/ul/li"))) +1

            for j in range( 1 , contents ):

                content = driver.find_element_by_xpath(f"//*[@id='contents_area_full']/ul/ul/li[{j}]")
                title = content.text
                # title_spt = title.split('\n')[0].replace('"','').replace('/','_')
                title_spt = title.split('\n')[0]

                title_spt = re.sub(r"[^a-zA-Z가-힣 ]", "", title_spt)
                title_spt = title_spt.replace(' ','_')

                print( j , title_spt)

                con_elem = content
                driver.execute_script("arguments[0].click();", con_elem)

                content.click()

                ingredients = driver.find_elements_by_css_selector("#divConfirmedMaterialArea > ul")

                ing_list = list()

                if len(ingredients) == 0:

                    while True:

                        page_url = driver.current_url

                        if 'page' in page_url:
                            print('요소없음')
                            break
                        else:
                            driver.back()
                            time.sleep(1)
                else:

                    for ingredient in ingredients:
                        ingredient_row = ingredient.text.split('\n')

                        cnt = 0
                        row_ing = ''

                        for row in ingredient_row:

                            if '[' not in row or ']' not in row:
                                cnt += 1

                            if cnt % 2 == 1 or cnt == 0:
                                row_ing += row
                            else:
                                row_ing += row + ','

                        ing_list.append( row_ing[:-1] )

                    ing_list_final = ' '.join(ing_list)

                    # print(ing_list_final)

                    cur.execute('insert or replace into recipe_10000 (agricultural,title,ingredients) values(?,?,?)',(df[0],title_spt,ing_list_final))
                    con.commit()

                    main_img = driver.find_element_by_css_selector("#main_thumbs").get_attribute('src')

                    # 이미지 저장 부분
                    try:
                        urllib.request.urlretrieve(main_img, f'./img/recipe/{title_spt}.jpg')
                    except HTTPError as e:
                        err = e.read()
                        code = e.getcode()
                        print('------------')
                        print(code)  ## 404
                        print('------------')

                    methods = driver.find_elements_by_css_selector("div.view_step_cont.media")

                    mt_cnt = 0
                    img_cnt = 0

                    method_list = list()

                    method_list.append(title_spt)

                    for method in methods:
                        mt_cnt += 1
                        # print(mt_cnt , method.text )
                        method_list.append(method.text)

                    while True:

                        if len(method_list) == 31:
                            break
                        else:
                            method_list.append('')

                    cur.execute(
                        'insert or replace into recipe_10000_detail (title,rcp1,rcp2,rcp3,rcp4,rcp5,rcp6,rcp7,rcp8,rcp9,rcp10,rcp11,rcp12,rcp13,rcp14,rcp15,rcp16,rcp17,rcp18,rcp19,rcp20,rcp21,rcp22,rcp23,rcp24,rcp25,rcp26,rcp27,rcp28,rcp29,rcp30) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
                        , (method_list[0], method_list[1], method_list[2], method_list[3], method_list[4], method_list[5], method_list[6], method_list[7], method_list[8], method_list[9], method_list[10],
                           method_list[11], method_list[12], method_list[13], method_list[14], method_list[15], method_list[16], method_list[17], method_list[18], method_list[19], method_list[20],
                           method_list[21], method_list[22], method_list[23], method_list[24], method_list[25], method_list[26], method_list[27], method_list[28], method_list[29], method_list[30]))
                    con.commit()

                    imgs = driver.find_elements_by_css_selector("div.view_step_cont.media > div > img")

                    for img in imgs:
                        img_src = img.get_attribute('src')
                        img_cnt += 1
                        # print( img_cnt ,  img_src )

                        # 이미지 저장 부분
                        try:
                            urllib.request.urlretrieve(img_src, f'./img/method/{title_spt}_{img_cnt}.jpg')
                        except HTTPError as e:
                            err = e.read()
                            code = e.getcode()
                            print('------------')
                            print(code)  ## 404
                            print('------------')

                    try:

                        # driver.find_element_by_css_selector("div > #btnMoreReviews").click() # 리뷰 전체 보기

                        review_click = driver.find_element_by_css_selector("div > #btnMoreReviews")

                        driver.execute_script("arguments[0].click();", review_click)

                    except NoSuchElementException:
                        pass

                    try:

                        # driver.find_element_by_css_selector("div > #btnMoreComments").click() # 댓글 전체 보기

                        comment_click = driver.find_element_by_css_selector("div > #btnMoreComments")

                        driver.execute_script("arguments[0].click();", comment_click)

                    except NoSuchElementException:
                        pass

                    comments = driver.find_elements_by_css_selector("#contents_area > div.view_reply > div > div.media.reply_list")

                    comment_cnt = 0

                    commnet_list_final = list()

                    if len(comments) != 0:

                        for comment in comments:
                            comment_row = comment.text.split('\n')

                            commnet_list = list()

                            for row in comment_row:
                                comment_cnt += 1
                                if comment_cnt % 2 == 0:
                                    commnet_list.append(df[0])
                                    commnet_list.append(title_spt)
                                    commnet_list.append(row)
                                    # print(commnet_list)
                                    cur.execute('insert or replace into recipe_10000_comment (agricultural,title,comment) values(?,?,?)',
                                                (commnet_list[0], commnet_list[1],commnet_list[2]))
                                    con.commit()
                    while True:

                        page_url = driver.current_url

                        if 'page' in page_url:
                            break
                        else:
                            driver.back()
                            time.sleep(1)
    driver.quit()

except Exception as error:
    driver.quit()
    error.message

