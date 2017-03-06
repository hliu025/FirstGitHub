#coding=utf-8
import pymysql.cursors
#import MySQLdb
import time
#connect to teh database
import pymysql
conn = pymysql.connect(host='127.0.0.1',port=3309,
                       user='root', passwd='123456', db='netbar')
cur = conn.cursor()
#cur.execute("USE scraping")
cur.execute("SELECT * FROM ap_group WHERE store_id=103")
#cur.execute("UPDATE ap_group set name='interface' WHERE store_id=103")
print(cur.fetchone())
#conn.commit()
#conn.close()
try:

    with conn.cursor() as cursor:
        #create a new record
        sql='UPDATE ap_group set name="interface" WHERE store_id=103'

        cursor.execute(sql)
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        conn.commit()
    with conn.cursor() as cursor:
        # Read a single record
        sql="SELECT * FROM ap_group WHERE store_id=103"
        cursor.execute(sql)
        result=cursor.fetchone()
        print(result)
finally:
    conn.close()
