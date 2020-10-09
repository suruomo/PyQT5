# -*- coding: utf-8 -*-
__author__ = 'suruomo'
__date__ = '2020/10/9 13:03'

import sqlite3

# 连接数据库，创建表和加入数据
conn = sqlite3.connect("student.db")
cursor = conn.cursor()
sql="create table student(name Text,phone Text,address Text)"
cursor.execute(sql)

sql="insert into student values('zhangsan','1231231242','beijing'),"\
    "('lisi','1231242412','shanghai')"

cursor.execute(sql)
conn.commit()
