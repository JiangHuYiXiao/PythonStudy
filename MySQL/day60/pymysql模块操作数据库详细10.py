# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/11 16:13
# @Software       : Python_study
# @Python_verison : 3.7
'''
# 1、增加
import pymysql
conn = pymysql.connect(host='127.0.0.1',user='root',password='',database='db1')
cursor = conn.cursor()
sql = "insert into t_user_info(password,user_name) values(123456,'jinaghu1');"
cursor.execute(sql)
conn.commit()           # 提交
conn.close()
cursor.close()

# 2、删除
import pymysql
conn = pymysql.connect(host='127.0.0.1',user='root',password='',database='db1')
cursor = conn.cursor()
sql = "delete from t_user_info where id=13;"
cursor.execute(sql)
conn.commit()
conn.close()
cursor.close()


# 3、改
import pymysql
conn = pymysql.connect(host='127.0.0.1',user='root',password='',database='db1')
cursor = conn.cursor()
sql = "update t_user_info set user_name='jiangxi'where id=10;"
cursor.execute(sql)
conn.commit()           # 提交
conn.close()
cursor.close()

# 4、变量增加
user_name='long'
password=123
import pymysql
conn = pymysql.connect(host='127.0.0.1',user='root',password='',database='db1')
cursor = conn.cursor()
sql = "insert into t_user_info(password,user_name) values(%s,%s);"
cursor.execute(sql,[password,user_name])
conn.commit()           # 提交
conn.close()
cursor.close()


# 5、批量插入

import pymysql
conn = pymysql.connect(host='127.0.0.1',user='root',password='',database='db1')
cursor = conn.cursor()
sql = "insert into t_user_info(password,user_name) values(%s,%s);"
r= cursor.executemany(sql,[(123,'nimei'),(123456,'1232')])          # 受影响的行数
print(r)
conn.commit()           # 提交
conn.close()
cursor.close()
'''
# 6、查找
import pymysql
conn = pymysql.connect(host='127.0.0.1',user='root',password='',database='db1')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)   # 这样设置的话，取出来的数据是字典形式，有列名
sql = "select * from t_user_info;"
cursor.execute(sql)
# res= cursor.fetchone()          # 取一个
res=cursor.fetchmany(3)          # 取三个
# res= cursor.fetchall()          # 取所有
print(res)
conn.close()
cursor.close()