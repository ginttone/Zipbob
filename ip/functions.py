import sqlite3
import pandas as pd
import json
import random
import datetime
import numpy as np
from django.shortcuts import render
from django.http import HttpResponse

from datetime import date
from datetime import datetime
from datetime import datetime , timedelta

from django.core.paginator import Paginator

global cur , con

con = sqlite3.connect('./db.sqlite3',check_same_thread=False)
cur = con.cursor()

now = datetime.now()
today = date.today()

yesterday = now - timedelta(days=3)

next_today = today + timedelta(days=7)
last_today = today - timedelta(days=7)

now = str(now)[0:10]
yesterday = str(yesterday)[0:10]


dict = {0:'월요일', 1:'화요일', 2:'수요일', 3:'목요일', 4:'금요일', 5:'토요일', 6:'일요일'}

# 이번주
if today.weekday() == 0:
    monday = today
    # print( '이번주 월요일', monday, '입니다.' )
else:
    monday = today - timedelta(days=today.weekday())
    # print( '이번주 월요일은', monday, '입니다.' )

if today.weekday() == 4:
    friday = today
    # print( '이번주 금요일', friday, '입니다.' )
else:
    friday = today - timedelta(days=today.weekday())
    # print( '이번주 금요일은', friday, '입니다.' )

# 다음주
if next_today.weekday() == 0:
    next_monday = next_today
    # print( '다음주 오늘은 월요일', next_monday, '입니다.' )
else:
    next_monday = next_today - timedelta(days=next_today.weekday())
    # print( '다음주 월요일은', next_monday, '입니다.' )

if next_today.weekday() == 4:
    next_friday = next_today
    # print( '다음주 금요일은', next_friday, '입니다.' )
else:
    next_friday = next_today - timedelta(days=next_today.weekday())
    # print( '다음주 금요일은', next_friday, '입니다.' )

#지난주
if last_today.weekday() == 0:
    last_monday = last_today
    # print( '지난주 오늘은 월요일', last_monday, '입니다.' )
else:
    last_monday = last_today - timedelta(days=last_today.weekday())
    # print( '지난주 월요일은', last_monday, '입니다.' )

if last_today.weekday() == 4:
    last_friday = last_today
    # print( '지난주 금요일은', last_friday, '입니다.' )
else:
    last_friday = last_today - timedelta(days=last_today.weekday())
    # print( '지난주 금요일은', last_friday, '입니다.' )

class home_process:

    global item_4_final , item_4  , item_all

    item_4_final = list()

    # item_4 = ('갈치', '감자', '건고추', '건멸치')

    item_4_df = pd.read_sql_query(f' select itemnm , price , regdate '
                                  f' from kamis_price_api '
                                  f' where regdate >= "{monday}" '
                                  f' and price != "-" '
                                  f' and price > 99 '
                                  f' group by  regdate , itemnm '
                                  f' order by 1 ,3 ;' , con)

    # print(item_4_df)

    item_4_df_list = item_4_df.values.tolist()

    list_4 = list()

    max_dict = {}

    rate_list = list()


    for item in item_4_df_list:
        # print(item)
        if item[0] not in list_4:
            list_4.append(item[0])


    for row in list_4:

        price_max = 0
        price_min = 10000000
        price_max_date = ""
        price_min_date = ""

        for price in item_4_df_list:
            row_price = price[1]

            if isinstance(row_price, str):
                row_price = int(row_price.replace(',',''))

            # print(price)
            if price[0] == row:

                if price_max < row_price:
                    price_max = row_price
                    price_max_date = price[2]
                if price_min > row_price:
                    price_min = row_price
                    price_min_date = price[2]

        # print(now ,yesterday )
        if ( price_max_date != price_min_date ) and (  yesterday < price_min_date ) :

            rate = round(100-(price_min/price_max*100))
            # print(row,price_max,price_max_date)
            # print(row,price_min,price_min_date)
            final_data = (row,rate)
            # print(final_data)
            rate_list.append(final_data)

    rate_list_sort =sorted(rate_list, key=lambda rate: rate[1] ,reverse=True )

    # print(rate_list_sort)

    items_4 = list()

    for rate_4_item in rate_list_sort:
        items_4.append(rate_4_item[0])

        if len(items_4) > 3:
            break

    item_4_final = items_4
    item_4 = ','.join(item_4_final)
    item_4 =  '("' +item_4.replace(',','","') + '")'

    items_all = list()

    for rate_all_item in rate_list_sort:
        items_all.append(rate_all_item[0])

        if len(items_all) > 10:
            break

    item_all_final = items_all
    item_all = ','.join(item_all_final)
    item_all = '("' + item_all.replace(',', '","') + '")'



    def this_week(self):

        df = pd.read_sql_query(f' select itemnm , kindnm , price , regdate '
                                f' from kamis_price_api '
                                f' where regdate >= "{monday}" '
                                f' and price != "-" '
                                f' and kindnm != "깐마늘(남도)(1kg)" '
                                f' and itemnm in {item_all} '
                                
                                f' group by itemnm , kindnm , price , regdate '
                                f' order by 1 ,3 '
                                
                                f';', con)

        df_list = df.values.tolist()

        item_list = []

        for data in df_list:
            test = (data[0], data[1])
            if test not in item_list:

                item_list.append(test)

        data_final = list()

        for item in item_list:

            df_item = df['itemnm'] == item[0]
            df_data = df[df_item]['price']
            df_data = df_data.values.tolist()
            # print(df_data)
            df_data.reverse()

            list_itme = list(item)

            new_list = list_itme + df_data

            data_final.append(new_list)

        df_date_list = df['regdate'].values.tolist()
        df_list = list()
        df_list_final = list()

        for i in df_date_list:
            if i not in df_list:
                df_list.append(i)



        if len(df_list) >= len(df_list_final):
            df_list_final = df_list

        datetime_list = list()
        datetime_list_final = list()

        for j in df_list_final:

            datetime_list.append(datetime.strptime(j,'%Y-%m-%d'))

        datetime_list = sorted(datetime_list)

        for k in datetime_list:
            str_date = str(k)
            datetime_list_final.append(str_date[0:10])

        datetime_list_final.insert(0,'품목')
        datetime_list_final.insert(1, '기준')

        print(item_4_final)

        result = { 'item_4': item_4_final , 'th':datetime_list_final ,'tr':data_final }

        return result;


    def next_week(self):
        # 시계열 피클 사용 https://wikidocs.net/141381
        result = []
        return result;

    def what_next(self):
        # 시계열 피클 사용 https://wikidocs.net/141381
        result = []
        return result;

    def graph(self):
        result = []
        return result;

    def recipe_table(self):
        result = []
        return result;


    def emailchk(request):

        email = request.GET['email']

        df = pd.read_sql_query( f'select * from user where email = "{email}" ; ', con)

        df_list = df.values.tolist()

        if len(df_list) >  0:
            data = {'data': "이미 사용중인 E-mail 입니다.", 'color': "Red"}
        else:
            data = {'data': "사용 가능한 E-mail 입니다.", 'color': "Green"}

        return HttpResponse(json.dumps(data), content_type='application/json')

    def login(request):
        print('------------------');

        email = request.GET['email']
        pwd = request.GET['pwd']

        print(email , pwd )

        df = pd.read_sql_query( f'select name from user where email = "{email}" and password = "{pwd}" ; ', con)

        df_list = df.values.tolist()
        name = df_list[0][0]

        print(name)

        if len(df_list) >  0:
            data = { 'data': f"{name}" " 님 환영합니다." }
        else:
            data = {'data': "메일 또는 비밀번호를 다시 확인하세요."}

        return HttpResponse(json.dumps(data), content_type='application/json')

    def regi_view(request):

        email = request.GET['email']
        name = request.GET['name']
        pwd = request.GET['pwd']

        cur.execute('insert into user (email,name,password) values(?,?,?)',
                    (email, name, pwd))
        con.commit()
        data = '정상적으로 가입 되었습니다. 로그인 하세요.'
        print(data)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def next_week_pred(request):

        cnt = 0

        result = {}

        result_data = []

        df_item_list = item_4_final

        line_list = ['ShortDashDot','Dash','ShortDash']
        df_list = list()
        df_list_final = list()

        for item in df_item_list:

            item_dict = {}

            data_item = item

            df = pd.read_sql_query(f'select round(price) as price , date '
                                   f'from ( select api.itemnm as itemnm , api.regdate as date , replace(api.price,",","") as price '
                                            f'from kamis_price_api api '
                                            f'where api.regdate < "{now}" '
                                            f'and api.regdate >= "{last_monday}" '
                                            f'and api.itemnm = "{data_item}" '
                                            f'union '
                                            f'select pred.itemnm  as itemnm , pred.pred_date as date , pred.pred_price as price '
                                            f'from  kamis_price_pred pred '
                                            f'where pred.pred_date >= "{now}" '
                                            f'and pred.pred_date <= "{next_friday}" '
                                            f'and pred.itemnm = "{data_item}" '
                                            f') tot '
                                   f'where tot.itemnm in {item_4} '
                                   f'group by price ,date '
                                   f'order by 2 ;', con)

            df.columns = ['price', 'date']

            df_price_list = df['price'].values.tolist()
            df_date_list = df['date'].values.tolist()

            for i in df_date_list:
                df_list.append(i)

            if len(df_list) >= len(df_list_final):
                df_list_final = df_list

            cnt += 1

            color = list()
            color_value = 'color[' + str(cnt) + ']'
            color.append(color_value)

            item_dict['name'] = data_item
            item_dict['data'] = df_price_list
            item_dict['dashStyle'] = [random.choice(line_list) for i in range(1)][0]
            item_dict['color'] = color[0]


            result_data.append(item_dict)


        # print(result_data)
        # print(df_list_final)

        result = { 'data': result_data , 'date' : df_list_final }

        return HttpResponse(json.dumps(result), content_type='application/json')