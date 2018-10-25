# -*- coding:utf-8 -*-
# 元组：是只读列表，默认只能查询，不能增加、修改、删除
# 但是如果元组中包含了列表则可以对元组中的列表进行增删改查
tu = (1,2,3,'alex',[2,3,4,'taibai'],'egon')
'''
# 1、增加
#  元组本身不支持append、insert、extend进行增加
# 但是可以对元组中的列表进行增加操作
tu[4].append('luck')
print(tu)

tu[4].insert(0,1)
print(tu)

tu[4].extend('NB')
print(tu)

# 2、删除
# 元组本身可以使用通用删除，但是不能通过，remove和clear、pop
# tu1 = (12321,32432)
# del(tu1)
# print(tu1)
tu[4].remove(1)
print(tu)

tu[4].pop()
print(tu)

tu[4].pop(0)
print(tu)

tu[4].clear()
print(tu)
'''
#3、元组本身不可以修改
# tu[1] = 22    #元组不支持修改

tu[4][0] = 100
print(tu)
tu[4][1] = 'jiang'
print(tu)
tu[4][-1] = (tu[4][-1].upper())
print(tu)

# 4、元组的查询
# print(tu[1])      #2
# print(tu[1:4])    #(2, 3, 'alex')
# print(tu[0:4:2])  #(1, 3)


# 列表转换成字符串用join
# 补充join,是所有可迭代对象(字符串、列表、元组、字典)的操作方法，返回的数据类型为字符串
# join中所有的参数类型必须为str
tuple = (11,'jianghu',12,'abc')
s1 = ''.join('%s' %id for id in tuple)
print(s1)
