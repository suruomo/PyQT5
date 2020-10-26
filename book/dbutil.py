# -*- coding: utf-8 -*-
__author__ = 'suruomo'
__date__ = '2020/10/20 14:02'

import pymysql as mysql_conn


# 获取连接
def get_conn():
    try:
        conn = mysql_conn.connect(host='localhost',
                                  database='library',
                                  user='root',
                                  password='suruomo')
        return conn
    except mysql_conn.Error:
        print("数据库连接异常")


# 关闭连接
def close_conn(conn, cursor):
    try:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    except mysql_conn.Error:
        print("数据库关闭异常")
    finally:
        cursor.close()
        # conn.close()


print(get_conn())

