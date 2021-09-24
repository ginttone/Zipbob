from selenium import webdriver
from multiprocessing.dummy import Pool as ThreadPool
import requests
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.10000recipe.com'
url_list = []

for i in range(1, 3):
    make_url = f'https://www.10000recipe.com/recipe/list.html?order=reco&page={i}'
    data = requests.get(make_url)

    soup = BeautifulSoup(data.content, 'html.parser')
    link = soup.find_all('a', class_="common_sp_link")

    for j in range(len(link)):
        url_list.append(url + link[j]['href'])

all_recipes = []

for page in url_list:
    datas = requests.get(page)
    soup = BeautifulSoup(datas.content, "html.parser")

    imgs = soup.select_one('img#main_thumbs')["src"]
    ids = soup.select('span.user_info2_name')[0].text.strip()
    title = soup.find('meta', property="kakao:title")["content"]
    ingredients = soup.find('div', class_="ready_ingre3").text.strip()

    recipe_list = []
    recipes = soup.select('div.view_step_cont.media')

    for recipe1 in recipes:
        recipe = recipe1.find('div', class_="media-body").text.strip()
        recipe_img = recipe1.find('img')["src"]
        if recipe_img != AttributeError:

        else:
            pass
        recipe_list.append([recipe, recipe_img])

    all_recipes.append([imgs, ids, title, ingredients, recipe_list])

print(all_recipes)
