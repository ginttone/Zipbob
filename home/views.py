import sqlite3
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from ip.functions import home_process
import json

## 챗봇 테스트 ---------------------------------------
import ML.chatmodel ## 챗봇코드를 넣은 .py파일에 맞게 경로를 지정합니다

from django.http import HttpResponse

# Create your views here.
def home(request):
    result={}
    return render(request, 'home.html', context=result)

def index(request):
    home_class = home_process()

    this_week = home_class.this_week()
    recipe_table = home_class.recipe_table()
    recipe_recommend = home_class.recipe_recommend()

    print(this_week)

    result = {'this_week': this_week, 'recipe_table':recipe_table , 'recipe_recommend' : recipe_recommend}

    return render(request, 'index.html', context=result)

def test(request):
    result={}
    return render(request, 'test.html', context=result)

def premium(request):
    result = dict()
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row  # for getting columns
    curs = conn.cursor()
    # economics
    curs.execute('select * from recipe_tot_youtube')
    data = curs.fetchall()
    for row in data:
        print(row['title'], ' : ', row['method'])
    paginator = Paginator(data, 5)
    result = dict()
    result['paginator'] = paginator
    # request.GET['page']
    page_number = request.GET.get('page', 1)
    result['page_obj'] = paginator.get_page(page_number)
    return render(request, 'premium.html', context=result)

def frame_test(request):
    result = dict()
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row  # for getting columns
    curs = conn.cursor()
    # economics
    curs.execute('select * from recipe_tot_youtube')
    data = curs.fetchall()
    for row in data:
        print(row['title'], ' : ', row['method'])
    paginator = Paginator(data, 5)
    result = dict()
    result['paginator'] = paginator
    # request.GET['page']
    page_number = request.GET.get('page', 1)
    result['page_obj'] = paginator.get_page(page_number)
    return render(request, 'frame_test.html', context=result)



def chatbottest(request):
    a = request.GET['a']
    result = ML.chatmodel.chat(a)
    # print("chat함수 성공")
    return HttpResponse(json.dumps(result), content_type='application/json')

