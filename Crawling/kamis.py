import urllib.request
from urllib.request import urlopen


from urllib.error import URLError, HTTPError
import pandas as pd
import sqlite3
import time
from bs4 import BeautifulSoup
import urllib.request as MyURL
from lxml import etree
import xml.etree.ElementTree as ET


con = sqlite3.connect('../db.sqlite3')
cur = con.cursor()
# df = pd.read_sql_query(''' select distinct a.itemcd , a.itemnm
# , c.mx
#
# from standard a left outer join  (  select b.itemnm , max(b.regdate) as mx
# 									from kamis_price_api b
# 									group by b.itemnm   ) c
# 				on a.itemnm = c.itemnm
#
# order by 1 ''' ,con )

df = pd.read_sql_query(''' select distinct a.itemcd , a.itemnm  from standard a order by 1 ''' ,con )
df_list = df.values.tolist()

# df_list = [['211','배추','2021-09-01']]

print(df_list)

end = 2022
id = '1980'
key = '5fb47fa6-43cf-4bf0-abf8-4eea3e61ef13'


for df in df_list:

    srch = df[0]

    # if df[2] == None:
    #     start = 1996
    # else:
    #     start = int(df[2][0:4])

    start = 2021

    for i in range( start , end ):

        url = 'http://www.kamis.or.kr/service/price/xml.do?action=periodProductList&p_startday='+str(i)+'-09-01'+ '&p_endday=' + str(i) +'-12-31' + '&p_itemcode=' + df[0] + '&p_countrycode=1101' + '&p_cert_key=' + key + '&p_cert_id=' + key + '&p_returntype=xml&p_convert_kg_yn=Y'
        print(url)

        try:
            response = MyURL.urlopen(url)

            soup = BeautifulSoup(response,"lxml")

            for data in soup.find_all('item'):
                items = data.text

                # print(data)
                row_list = list()

                if df[1] in items:
                    items_list = items.split('\n')
                    for item in items_list:
                        row_list.append(item)
                if len(row_list) != 0:
                    # print(row_list)
                    itemnm = row_list[1]
                    kindnm = row_list[2]
                    regdate = row_list[5] + '-' + row_list[6].replace('/','-')
                    price = row_list[7]

                    print(itemnm,kindnm,regdate,price)

                    cur.execute('insert or replace into kamis_price_api (itemnm,kindnm,regdate,price) values(?,?,?,?)',(itemnm,kindnm,regdate,price))
                    con.commit()
        except:
            continue