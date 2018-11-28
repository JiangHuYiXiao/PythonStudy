# -*- coding:utf-8 -*-
'''
生成器：的本质就是迭代器
生成器的生成方式：
    1、就是我们自己写的生成器函数
    2、生成器表达式
'''
# 1、生成器函数
'''   # 普通函数
# 函数定义
def generator():
    print(1)
    return 'a'

# 函数调用
res = generator()
print(res)
'''
# 生成器函数
# yield必须在函数内部，且一个函数里面不能同时含有yield和return
# 生成器函数执行后，会返回一个生成器作为返回值
# yield也可以返回函数值，但是yield之后不会结束函数，return会结束函数
'''
def generator():  # 步骤1
    print(1)      # 步骤6
    yield 'a'     # 步骤7

res = generator()   # 返回一个生成器 右边：# 步骤2 左边：# 步骤3
print(res)   # <generator object generator at 0x00000000022B3750> # 步骤4
# 判断生成器函数generator()是否为迭代器
# from collections import Iterator
# from collections import Iterable
# print(isinstance(generator(),Iterator))    # True
# print(isinstance(generator(),Iterable))    # True
# 这样的函数内部包含yield关键字的都叫做生成器函数，这种函数调用需要通过迭代器去调用，而生成器函数的本质就是迭代器
# 所以可以直接调用生成器函数的__next__(）方法
print(res.__next__())   # 步骤5
'''
# 连续取生成器函数的值，可以通过__next__和for循环

# 1、__next__
# def generator():
#     print(1)
#     yield 'a'
#     print(2)
#     yield 'b'
#     print(3)
#     yield 'c'
#
# res = generator()
# print(res.__next__()) # 1,a
# print(res.__next__()) # 2,b
# print(res.__next__()) # 3,c
# print(res.__next__()) # StopIteration

# yield就不会结束函数，会继续取值


# 2、for循环
# for循环取全部生成器函数的值
# def generator():
#     print(1)
#     yield 'a'
#     print(2)
#     yield 'b'
#     print(3)
#     yield 'c'
# res = generator()
# for i in res:
#     print(i)  #1,a,2,b,3,c


# 需求，生成wahaha+序列（200000）
# def func():    # 生成器函数
#     for i in range(200001):
#         yield 'wahaha%s'%i
#
# res = func()   # 生成器
# for i in res:
#     print(i)


# 只想要取得50个
# def func():    # 生成器函数
#
#     for i in range(200001):
#         yield 'wahaha%s'%i
#
# res = func()   # 生成器
# count = 0
# for i in res:
#     count += 1
#     print(i)
#     if count > 50:
#         break
#
# # 还可以接着取值
# print('****',res.__next__())
#
# # 还可以接着取值
# for i in res:
#     count += 1
#     print(i)
#     if count > 100:
#         break


# 迭代器和可迭代的关于for循环的差异
#迭代器：针对于同一个迭代器是不会重新取值的，只有针对于不同迭代器就会重新取值
def generator():
    for i in range(500):
     yield 'wahaha%s'%i

g = generator()
g1 = generator()
count = 0
for i in g:
    count += 1
    print(i)
    if count > 50:
        break           # 到wahaha50
print(g.__next__())     # wahaha51

print(g1.__next__())    # wahaha0

# 可迭代的:会重新开始取值
# list = [11,12,14]
# for i in list:
#     print(i)
#     if i == 12:
#         break
# # result:11,12
#
# for i in list:
#     print(i)

# result:11,12,14


