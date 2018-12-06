#-*- coding:utf-8 -*-
# 函数名 = lambda 参数:函数体   （只能写一行）
# 匿名函数可以有名字
# 比如：calc = lambda n:n**n，函数名为calc，
'''
calc = lambda n:n**n
print(calc(10))

# 练习1：把下面的函数改成匿名函数
def add(x,y):
    return x+y
print(add(2,3))

add = lambda x,y:x+y
print(add(12,21))

# 需求1：筛选出字典中value值最大的key值
dict = {'k1':11,'k2':210,'k3':20}
def func(key):
    return dict[key]
print(max(dict,key=func))

# 使用匿名函数
print(max(dict,key=lambda key:dict[key]))
'''

# 练习2：筛选列表中大于10的数[5,8,11,9,15]
# def func(num):
#     if num>10:
#         return num
# res = filter(func,[5,8,11,9,15])
# print(res)
# for i in res:
#     print(i)

# 使用匿名函数

res = filter(lambda num:(num > 10),[5,8,11,9,15])
for i in res:
    print(i)


