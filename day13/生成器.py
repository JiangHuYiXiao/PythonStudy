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
def generator():  # 步骤1
    print(1)      # 步骤6
    yield 'a'     # 步骤7

res = generator()   # 没有返回值 右边：# 步骤2 左边：# 步骤3
print(res)   # <generator object generator at 0x00000000022B3750> # 步骤4
# 判断生成器函数generator()是否为迭代器
# from collections import Iterator
# from collections import Iterable
# print(isinstance(generator(),Iterator))    # True
# print(isinstance(generator(),Iterable))    # True
# 这样的函数内部包含yield关键字的都叫做生成器函数，这种函数调用需要通过迭代器去调用，而生成器函数的本质就是迭代器
# 所以可以直接调用生成器函数的__next__(）方法
print(res.__next__())   # 步骤5


