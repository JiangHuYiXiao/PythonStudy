# -*- coding:utf-8 -*-
# 嵌套列表
list = [1,'江湖一笑',2,3,[12,13,14,15,'tao'],'jianghu','taibai']
# 1、输出‘湖’
print(list[1][1])
# 2、输出12
print(list[4][0])
# 3、将list中的jianghu的首字母大写
list[-2] = (list[-2].capitalize())
print(list)
# 4、将list中的‘江湖一笑’改成‘江湖险恶’(字符串中没有修改这个功能，所以只能替换)
# 方法1
list[1] = list[1].replace('一笑','险恶')
print(list)
# 方法2----间接的对列表进行修改
list[1] = '江湖险恶'
print(list)

# 5、将tao全部变成大写
list[4][-1] = list[4][-1].upper()
print(list)
# 6、将15全部变成150
list[4][-2] = 150
print(list)