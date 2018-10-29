#-*- coding:utf-8 -*-
'''
# 1、有如下变量：tu ，请实现要求的功能
tu = ('alex',[11,22,{'k1':'v1','k2':['age','name'],'k3':[11,22,33]},44])
# a、讲述元组的特性
# b、请问tu变量的第一个元素alex是否可以被修改，
# c、请问tu变量的k2对应的值数据类型为，是否可以被修改，如果可以请在其中添加一个元素’Seven‘
# d、请问tu变量的k3对应的值数据类型为，是否可以被修改，如果可以请在其中添加一个元素’Seven‘

# a、元组本身是只读列表，不可增加，删除、修改，只能够进行查找，但是如何元组里面包含了可变数据类型（列表、字典、集合）则可以修改、增加、删除
# b、不可修改
# c、

print(type(tu[1][2]['k2']))
tu[1][2]['k2'].append('Seven')
print(tu)

print(type(tu[1][2]['k3']))
tu[1][2]['k3'].append('Seven')
print(tu)

# 2、字典，dic dic = {'k1':'v1','k2':'v2','k3':[11,22,33]}
# a、请循环输出所有的key
# b、请循环输出所有的value
# c、请循环输出所有的key和value
# d、请在字典中添加一个键值对，k4：v4，并输出添加后的字典
# e、请修改字典中的k1值为‘alex’并输出修改后的字典
# f、请在k3对应的值中添加一个元素44，并输出修改后的字典
# g、请在k3对应的值中的第一个位置，添加一个元素18，并输出修改后的字典
dic = {'k1':'v1','k2':'v2','k3':[11,22,33]}
# a
for i in dic.keys():
    print(i)
# b
for i in dic.values():
    print(i)
# c
for i in dic.items():
    print(i)

# d
# 方法1：
dic['k4'] = 'v4'
print(dic)

# 方法2：
dic.setdefault('k4','v4')
print(dic)

e、
# 方法1
dic['k1'] = 'alex'
print(dic)

# 方法2
dic1 = {'k1':'alex'}
dic.update(dic1)
print(dic)
f、
dic['k3'].append(44)
print(dic)

g、
dic['k3'].insert(0,18)
print(dic)
'''

# 3、元素分类，有如下值li = [11,22,33,44,55,66,77,88,99,90],
# 将所有的大于66的值，保存到字典的第一个key下面，将小于66值，保存至第二个，key值中
#即：{'k1':'大于66值的所有列表','k2':'小于66的所有值列表'}
# dic = {}
# new1_li =[]
# new2_li =[]
# li =[11,22,33,44,55,66,77,88,99,90]
# for i in li:
#     if i > 66:
#         new1_li.append(i)
#     if i < 66:
#         new2_li.append(i)
# dic['k1'] = new1_li
# dic['k2'] = new2_li
# print(dic)

# 4、输出商品列表，用户输入序号，显示用户输入的商品，
# li = ['手机','电脑','鼠标垫','游艇']
# 要求：
# 1、页面显示序号+商品名称，如：
# 1 手机
# 2 电脑
# ...
# 2、用户输入选择的商品序号，然后打印商品名称。
# 3、如果用户输入的商品序号有错误，则提示输入有误，请重新输入。
# 4、用户输入q或者Q退出程序。

li = ['手机', '电脑', '鼠标垫', '游艇']
cart = []
while 1:
    for i,f in enumerate(li):
        print(i+1,f)
    shopping = input('请输入商品序号/输入q或者Q退出循环:')
    if shopping.isdigit():
        if 0 < int(shopping) and int(shopping) <= len(li):
            cart.append(li[int(shopping) - 1])
            print(cart)
        else:
            print('你输入的商品序号不存在，请重新输入')
    elif shopping.upper() == 'Q':
        break
    else:
        print('你输入的商品序号不存在，请重新输入')
