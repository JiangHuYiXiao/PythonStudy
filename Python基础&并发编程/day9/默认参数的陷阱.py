# -*- coding:utf-8 -*-
# 1、默认参数的值是不可变数据类型

def func(a =1):
    return a

print(func())     # 1
print(func(2))    # 2


# 2、默认参数的值是可变数据类型
# 列表

def func(list = []):
    list.append(2)
    return list
#当实参没有传递值时，每次调用的时候都是用的默认参数的值，且是在公用同一个资源
print(func())          # [2]
print(func([1]))       # [1,2]
print(func())          # [2,2]
print(func())          # [2,2,2]
#当实参有传递值时，用传递的值
print(func([1]))       # [1,2]
print(func([1,3]))       # [1,3,2]

# 字典
def func(k,dic={}):
    print(k)
    dic[k] = 'v'
    return (dic)

print(func(1))    # {1: 'v'}
print(func(2))    # {1: 'v', 2: 'v'}
print(func(3))    # {1: 'v', 2: 'v', 3: 'v'}


