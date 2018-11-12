# -*- coding:utf-8 -*-

# 1、语法糖 在被装饰的函数前面添加：@装饰器函数 等价于 func = time(func)
# V4
import time
def timer(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print(end - start)
    return inner

def func():
    print('你好我好大家好！')
    time.sleep(0.01)

# 调用func函数
func = timer(func)   # 等价于 @timer
func()   # 实际是inner

# 2、V5:使用语法糖后
import time
def timer(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print(end - start)
    return inner
@timer
def func():
    print('你好我好大家好！')
    time.sleep(0.01)

# 调用func函数
func()   # 实际是inner

# 3、V6:被装饰函数有返回值的装饰器
import time
def timer(f):
    def inner():
        start = time.time()
        re = f()
        end = time.time()
        print(end - start)
        return re
    return inner
@timer
def func():
    print('你好我好大家好！')
    time.sleep(0.01)
    return '新年好'

# 调用func函数
res = func()   # 实际是inner
print(res)

# 类似于要获取下面的字符串'inner'
def outer():
    def inner():
        return 'inner'
    re = inner()
    return re

# 调用outer

res = outer()
print(res)



# 4、V7:被装饰函数有参数的装饰器

import time
def timer(f):
    def inner(a):
        start = time.time()
        re = f(a)
        end = time.time()
        print(end - start)
        return re
    return inner
@timer
def func(a):
    print('你好我好大家好！',a)
    time.sleep(0.01)
    return '新年好'

# 调用func函数
res = func(1)   # 实际是inner
print(res)

# 5、V8:被装饰函数有多个按照位置传参的装饰器

import time
def timer(f):
    def inner(*args):
        start = time.time()
        re = f(args)
        end = time.time()
        print(end - start)
        return re
    return inner
@timer
def func(args):
    print('你好我好大家好！',args)
    time.sleep(0.01)
    return '新年好'

# 调用func函数
res = func(1,4)   # 实际是inner
print(res)

# 6、V9:被装饰函数有多个按照位置传参合按照关键字的装饰器

import time
def timer(f):
    def inner(*args,**kwargs):
        start = time.time()
        re = f(args,kwargs)
        end = time.time()
        print(end - start)
        return re
    return inner
@timer
def func(args,kwargs):
    print('你好我好大家好！',(args,kwargs))
    time.sleep(0.01)
    return '新年好'

# 调用func函数
res = func(1,4,b= 122131)   # 实际是inner
print(res)

# 二、装饰器的固定模式
def wrapper(func):        # 这里的func一定是被装饰的函数wahaha             # 装饰器函数
    def inner(*args,**kwargs):
            # '被装饰函数之前要做的事'
        res = func(*args,**kwargs)    # 被装饰的函数
            # '被装饰函数之后要做的事'
        return res
    return inner

@wrapper    # 等价于 wahaha = wrapper(wahaha)
def wahaha(*args,**kwargs):
    print('wahaha')
    return (args,kwargs)  #有返回值则需要加上

re = wahaha(1)  # 实际就是调用inner
print(re)

