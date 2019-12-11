# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/11 10:02
# @Software       : Python_study
# @Python_verison : 3.7
# python中使用mysql是通过模块 pymysql
'''

# 1、使用pymysql实现用户登录
name = input('请输入用户名：')
pwd = input('请输入密码：')

# 导入模块
import pymysql
# 创建连接
conn = pymysql.connect(host='127.0.0.1',user='root',password='',database='db1')
cursor = conn.cursor()
# 编写sql
SQL = "select * from t_user_info where user_name='%s' and password='%s';" %(name,pwd)
print(SQL)
# 执行sql
cursor.execute(SQL)
# 获取所有的结果
# res = cursor.fetchall()
# 获取一个结果
res = cursor.fetchone()
if res:
    print('登录成功')
else:
    print('登录失败')

cursor.close()
conn.close()



# 2、pymysql中的sql注入
name = input('请输入用户名：')
pwd = input('请输入密码：')
import pymysql
# 创建连接
conn = pymysql.connect(host='127.0.0.1',user='root',password='',database='db1')
cursor = conn.cursor()
# 编写sql
SQL = "select * from t_user_info where user_name='%s' and password='%s';" %(name,pwd)
print(SQL)
# 执行sql
cursor.execute(SQL)
# 获取所有的结果
# res = cursor.fetchall()
# 获取一个结果
res = cursor.fetchone()
if res:
    print('登录成功')
else:
    print('登录失败')

cursor.close()
conn.close()
# SQL注入样式1：
    # 小明' -- 后面加空格
# select * from t_user_info where user_name='小明' -- ' and password='';

    # aa' or 1=1 --
# select * from t_user_info where user_name='aa' or 1=1 -- ' and password='';
'''

# 3、pymysql中的防止sql注入的方式就是不要自己拼接参数，通过excute（添加参数）
name = input('请输入用户名：')
pwd = input('请输入密码：')
import pymysql
# 创建连接
conn = pymysql.connect(host='127.0.0.1',user='root',password='',database='db1')
cursor = conn.cursor()
# 编写sql
SQL = "select * from t_user_info where user_name=%s and password=%s"
print(SQL)
# 执行sql
cursor.execute(SQL,[name,pwd])
# cursor.execute(SQL,{'u':name,'p':pwd})
# 获取所有的结果
# res = cursor.fetchall()
# 获取一个结果
res = cursor.fetchone()
if res:
    print('登录成功')
else:
    print('登录失败')

cursor.close()
conn.close()