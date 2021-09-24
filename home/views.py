import sqlite3
from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    result={}
    return render(request, 'home.html', context=result)

def index(request):
    result={}
    return render(request, 'index.html', context=result)

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




