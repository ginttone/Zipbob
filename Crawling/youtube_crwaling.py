import pandas as pd
import numpy as np
import sqlite3

from numpy import unicode

con = sqlite3.connect('../db.sqlite3')
cur = con.cursor()


df = pd.read_sql_query("select distinct itemnm from standard ; " ,con )

searchs = df.values.tolist()

# searchs = '감자'

import requests
import re
import time
import xml.etree.ElementTree as ET
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs


# 참조 : https://www.youtube.com/watch?v=ZFmTwbRQ0uc
# 참조 : https://www.youtube.com/watch?v=dDEESB4Iw8g&t=292s


# chrome_option = webdriver.ChromeOptions()
# chrome_option.add_argument('--headless')
# chrome_option.add_argument('--no-sandbox')
# chrome_option.add_argument('--disable-dev-shm-usage')

# driver = webdriver.Chrome('Crawling/chromedriver.exe',options=chrome_option)


for row in searchs:

    search = row[0]
    driver = webdriver.Chrome('chromedriver.exe')
    url = 'https://www.youtube.com/c/paikscuisine/search?query=' + search

    driver.get(url)

    contents = driver.find_elements_by_css_selector('#video-title > yt-formatted-string')

    cnt = 1
    key = ''

    max_page = 0

    body = driver.find_element_by_tag_name("body")

    while True:

        search_cnt = 0

        for content in contents:

            title = content.text

            print( search ,'/ ', title )
            if search in title:
                search_cnt += 1
                # print(title)

        print(len(contents) , search_cnt)

        if len(contents) > search_cnt:
            break
        else:
            if max_page != 0 and max_page == len(contents):
                print('끝' , max_page)
                break
            else:
                max_page = len(contents)

                body.send_keys(Keys.PAGE_DOWN)
                body.send_keys(Keys.PAGE_DOWN)
                body.send_keys(Keys.PAGE_DOWN)
                body.send_keys(Keys.PAGE_DOWN)
                body.send_keys(Keys.PAGE_DOWN)
                body.send_keys(Keys.PAGE_DOWN)
                body.send_keys(Keys.PAGE_DOWN)
                body.send_keys(Keys.PAGE_DOWN)
                body.send_keys(Keys.PAGE_DOWN)
                body.send_keys(Keys.PAGE_DOWN)
                body.send_keys(Keys.PAGE_DOWN)

                time.sleep(1)
                print('스크롤 완료')

                contents = driver.find_elements_by_css_selector('#video-title > yt-formatted-string')  # #video-title > yt-formatted-string


    for content in contents:

        title = content.text
        content.click()
        time.sleep(3)

        driver.find_element_by_css_selector('#more > yt-formatted-string').click()
        time.sleep(1)
        recipe = driver.find_elements_by_css_selector('div#description > yt-formatted-string > span.style-scope.yt-formatted-string')

        recipe_row = list()

        for row in recipe:

            if len(row.text) > 4:

                method = row.text

                if '[재료]' in method:
                    start = method.find('[재료]')
                else:
                    start = method.find(' 재료 ') -2

                if '[만드는 법]' in method:
                    mid = method.find('[만드는 법]')
                else:
                    mid = method.find(' 만드는 법 ') -2

                if '[Ingredients]' in method:
                    end  = method.find('[Ingredients]') -1
                else:
                    end = method.find(' Ingredients ') -2

                ingredients = method[start:mid].replace('\n\n\n\n','').replace('\n',' ').replace(',',' ')
                method = method[mid:end].replace('\n\n\n\n','').replace('\n',' ').replace(',',' ')

                recipe_row.append(search+'_'+str(cnt))
                recipe_row.append(title)
                recipe_row.append(ingredients)
                recipe_row.append(method)

        elem = driver.find_element_by_tag_name("body")
        last_height = driver.execute_script("return document.body.scrollHeight")

        max = 0
        print('댓글 스크롤 시작')
        while True:

            elem.send_keys(Keys.PAGE_DOWN)
            elem.send_keys(Keys.PAGE_DOWN)
            elem.send_keys(Keys.PAGE_DOWN)
            elem.send_keys(Keys.PAGE_DOWN)
            elem.send_keys(Keys.PAGE_DOWN)

            time.sleep(2)

            comments = driver.find_elements_by_css_selector('div > #content-text')
            comments_len = len(comments)

            if max == comments_len and max != 0 :
                print('댓글 스크롤 종료')
                break
            else:
                max = comments_len

        comment_list_list = list()

        for comment in comments:

            comment_list = list()
            cmt = comment.text.replace('\n',' ').replace(',','')

            if len(cmt) > 8:
                comment_list.append(search + '_' + str(cnt))
                comment_list.append(cmt)
                comment_list_list.append(comment_list)

                cur.execute('insert into recipe_comment_youtube (menu_key,comment) values(?,?)', (comment_list[0],comment_list[1]))
                con.commit()

        cnt += 1

        cur.execute('insert into recipe_info_youtube (menu_key,title,ingredients,method) values(?,?,?,?)',(recipe_row[0],recipe_row[1],recipe_row[2],recipe_row[3]))
        con.commit()

        driver.back()
        time.sleep(3)

driver.quit()