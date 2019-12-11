
# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/11 16:54
# @Software       : Python_study
# @Python_verison : 3.7
import pymysql
conn = pymysql.connect(host='127.0.0.1',user='root',password='',database='db1')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)   # 这样设置的话，取出来的数据是字典形式，有列名
sql = "insert into t_user_info(password,user_name) values(123456,'keke');"
r=cursor.execute(sql)
conn.commit()
print(cursor.lastrowid)               # 获取插入数据的自增id
print(r)
conn.close()
cursor.close()