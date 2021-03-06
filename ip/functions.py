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

    global item_4_final , item_4  , item_all , list_4 , item_high, item_low , items_4

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

    # print('len - ', len(item_4_df_list))

    if len(item_4_df_list) == 0:
        item_4_df = pd.read_sql_query(f' select itemnm , round(pred_price) as price , pred_date as regdate '
                                      f' from kamis_price_pred '
                                      f' where pred_date >= "{monday}" '
                                      f' and pred_price != "-" '
                                      f' and pred_price > 99 '
                                      f' group by  pred_date , itemnm '
                                      f' order by 1 ,3 ;', con)
        item_4_df_list = item_4_df.values.tolist()

    # print(item_4_df_list)
    list_4 = list()

    max_dict = {}

    high_rate_list = list()
    low_rate_list = list()


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

            high_rate = round(100-(price_min/price_max*100))
            low_rate = round(100 - (price_max / price_min  * 100))
            # print(row,price_max,price_max_date)
            # print(row,price_min,price_min_date)
            high_final_data = (row,high_rate)
            low_final_data = (row,low_rate)
            # print(final_data)
            high_rate_list.append(high_final_data)
            low_rate_list.append(low_final_data)


    high_rate_list_sort = sorted(high_rate_list, key=lambda rate: rate[1] ,reverse=True )
    low_rate_list_sort = sorted(low_rate_list, key=lambda rate: rate[1], reverse=True)

    # print(rate_list_sort)

    items_4 = list()
    item_high = list()
    item_low = list()

    for rate_4_item in high_rate_list_sort:
        items_4.append(rate_4_item[0])

        if len(items_4) > 3:
            break

    for rate_2_high in high_rate_list_sort:
        item_high.append(rate_2_high[0])

        if len(item_high) > 1:
            break

    for rate_2_low in low_rate_list_sort:
        item_low.append(rate_2_low[0])

        if len(item_low) > 1:
            break

    item_4_final = items_4
    item_4 = ','.join(item_4_final)
    item_4 =  '("' +item_4.replace(',','","') + '")'

    items_all = list()

    for rate_all_item in high_rate_list_sort:
        items_all.append(rate_all_item[0])

        if len(items_all) > 10:
            break

    item_all_final = items_all
    item_all = ','.join(item_all_final)
    item_all = '("' + item_all.replace(',', '","') + '")'


    def this_week(self):

        # df = pd.read_sql_query(f' select itemnm , kindnm , price , regdate '
        #                         f' from kamis_price_api '
        #                         f' where regdate >= "{monday}" '
        #                         f' and price != "-" '
        #                         f' and kindnm != "깐마늘(남도)(1kg)" '
        #                         f' and itemnm in {item_all} '
        #
        #                         f' group by itemnm , kindnm , price , regdate '
        #                         f' order by 1 ,3 '
        #
        #                         f';', con)
        #
        # df_list = df.values.tolist()
        #
        # if len(df_list) == 0:

        df = pd.read_sql_query(f' select a.itemnm , a.itemkind ,  round(pred_price) as price , pred_date as regdate '
                                      f' from kamis_price_pred a , standard b '
                                      f' where pred_date >= "{monday}" '
                                      f' and pred_price != "-" '
                                      f' and a.itemnm in {item_all} '
                                      f' and pred_price > 99 '
                                      f' and a.itemkind in ( select itemnm||"-"||kindnm '
                                                           f'from kamis_price_api '
                                                           f'where itemnm in {item_all} '
                                                           f'and price > 100  and price != "-" '
                                                           f'and regdate >= "{last_monday}"  '
                                                           f'group by kindnm   '
                                                           f' )  '
                                      f' and a.itemkind = b.itemnm || "-" || b.breednm ||"(1kg)"  '
                                      f' group by a.itemnm , itemkind , pred_price , pred_date '
                                      f' order by 1 ,3 ;', con)
        df_list = df.values.tolist()

        # print(df_list)
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

        print( df_date_list )

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

        print(df_list)

        # print(item_4_final)
        # print(item_high)
        # print(item_low)

        result = { 'item_4': item_4_final , 'th':datetime_list_final ,'tr':data_final , 'high': item_high , 'low' : item_low }

        return result


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

        # print(email , pwd )

        df = pd.read_sql_query( f'select name from user where email = "{email}" and password = "{pwd}" ; ', con)

        df_list = df.values.tolist()

        if len(df_list) >  0:
            name = df_list[0][0]
            print(name)
            data = {'data': f"{name}" " 님 환영합니다."}
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
        # print(data)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def next_week_pred(request):

        cnt = 0

        result = {}

        result_data = []

        df_item_list = item_4_final

        line_list = ['ShortDashDot','Dash','ShortDash']
        df_list = list()
        df_list_final = list()

        print(df_list_final)

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
                                            f'select pred.itemnm  as itemnm , pred.pred_date as date , round(pred.pred_price) as price '
                                            f'from  kamis_price_pred pred '
                                            f'where pred.pred_date >= "{now}" '
                                            f'and pred.pred_date <= "{next_friday}" '
                                            f'and pred_price != "-" '
                                            f'and pred_price > 99 '
                                            f'and pred.itemnm = "{data_item}" '
                                            f') tot '
                                   f'group by date '
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

            result_data.append(item_dict)


        # print(result_data)

        df_list_final = set(df_list_final)
        df_list_final = list(df_list_final)

        datetime_list = list()
        datetime_list_final = list()

        for j in df_list_final:

            datetime_list.append(datetime.strptime(j,'%Y-%m-%d'))

        datetime_list = sorted(datetime_list)

        for k in datetime_list:
            str_date = str(k)
            datetime_list_final.append(str_date[0:10])

        print(result_data)
        print(datetime_list_final)


        result = { 'data': result_data , 'date' : datetime_list_final }

        return HttpResponse(json.dumps(result), content_type='application/json')


    def recipe_recommend(request):

        recipe_final = list()

        df = pd.read_sql_query(f'select agricultural , title '
                               f'from recipe_10000 '
                               f'where agricultural in {item_4} '
                               f'group by agricultural ' , con)

        df.dropna(axis=0)
        # print(df)

        recipe_final = df.values.tolist()
        recipe_title_list = df['title'].values.tolist()



        rcp1_list = list()
        rcp2_list = list()
        rcp3_list = list()
        rcp4_list = list()

        cnt = 0

        recipe_4 = '","'.join(recipe_title_list)


        df2 = pd.read_sql_query(f'select a.agricultural,  a.title , a.ingredients , '
                                f'rcp1||rcp2||rcp3||rcp4||rcp5||rcp6||rcp7||rcp8||rcp9||rcp10|| '
                                f'rcp11||rcp12||rcp13||rcp14||rcp15||rcp16||rcp17||rcp18||rcp19||rcp20|| '
                                f'rcp21||rcp22||rcp23||rcp24||rcp25||rcp26||rcp27||rcp28||rcp29||rcp30|| '
                                f'rcp41||rcp42||rcp43||rcp44||rcp45||rcp46||rcp47||rcp48||rcp49||rcp50|| '
                                f'rcp51||rcp52||rcp53||rcp54||rcp55||rcp56||rcp57||rcp58||rcp59||rcp60 as method '
                                f'from recipe_10000 a , recipe_10000_detail b  '
                                f'where a.title = b.title and  a.title in ("{recipe_4}") '
                                f'group by a.title '
                                f' ', con)


        df_list_all = df2.values.tolist()


        all_row_list = []

        for row in df_list_all:

            row_list = {}
            row_list['agricultural'] = row[0]
            row_list['title'] = row[1]
            row_list['ingredients'] = row[2]
            # row_list['method'] = row[3]

            df3 = pd.read_sql_query(f''' 
                                    
                                    select rcp1,rcp2,rcp3,rcp4,rcp5,rcp6,rcp7,rcp8,rcp9,rcp10, 
                                    rcp11,rcp12,rcp13,rcp14,rcp15,rcp16,rcp17,rcp18,rcp19,rcp20, 
                                    rcp21,rcp22,rcp23,rcp24,rcp25,rcp26,rcp27,rcp28,rcp29,rcp30, 
                                    rcp41,rcp42,rcp43,rcp44,rcp45,rcp46,rcp47,rcp48,rcp49,rcp50, 
                                    rcp51,rcp52,rcp53,rcp54,rcp55,rcp56,rcp57,rcp58,rcp59,rcp60 
                                    from recipe_10000 a , recipe_10000_detail b
                                    where a.title = b.title
                                    and a.title = '{row[1]}' 
                                    group by a.title
                                    
                                    ''', con)


            df3_list = df3.transpose().values.tolist()
            df3_list_list = {}
            df3_list_final = list()
            method_cnt = 0

            tot = 0

            for row in df3_list:
                if len(row[0]) != 0:
                    tot += 1
            print(tot)
            for row in df3_list:
                if len(row[0]) != 0:
                    method_cnt += 1
                    df3_list_list =  { 'cnt':method_cnt ,'method': row[0] , 'tot': tot  }
                    df3_list_final.append(df3_list_list)

            row_list['method'] = df3_list_final

            print(row_list['method'])

            all_row_list.append(row_list)



        result = { 'all' : all_row_list , 'title': recipe_title_list  }

        return result

    def recipe_table(request):

        recipe_final = list()

        df = pd.read_sql_query(f'select title , ingredients  , case when middle == "" then "중급"  when low == "" then "고급"  else "초급" end as lvl '
                               f'from ( '  
                               f'select a.agricultural , a.title , a.ingredients , '
                               f' rcp1||rcp2||rcp3||rcp4||rcp5||rcp6||rcp7||rcp8||rcp9||rcp10 as low, '
                               f' rcp11||rcp12||rcp13||rcp14||rcp15||rcp16||rcp17||rcp18||rcp19||rcp20 as middle, '
                               f' rcp21||rcp22||rcp23||rcp24||rcp25||rcp26||rcp27||rcp28||rcp29||rcp30 as high '
                               f'from recipe_10000 a '
                               f', recipe_10000_detail b '
                               f'where a.title = b.title '
                               f'and  a.agricultural in {item_all} '
                               f') '
                               f' limit 20 ; ', con)
        df.dropna(axis=0)
        # print(df)

        recipe_final = df.values.tolist()
        recipe_title_list = df[['title','ingredients', 'lvl']].values.tolist()
        recipe_ingredients_list = df['ingredients'].values.tolist()

        # print(recipe_title_list)
        print('*****************************')
        print(items_4)

        result = { 'data': recipe_final , 'title': recipe_title_list , 'ingredients' : recipe_ingredients_list  }

        return result
