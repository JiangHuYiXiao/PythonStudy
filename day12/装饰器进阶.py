#-*- coding:utf-8 -*-
# 1、带参数的装饰器
# 现在有个需求想要删除被装饰函数的装饰器，可以一个一个删除，
# 但是更加高效的方法是给timer加个函数，传个参数给timer来判断是删除还是不删除装饰器

import time
flag = False
# flag = True
def outer(flag):
    def timer(func):
        def inner(*args,**kwargs):
            if flag:
                start = time.time()
                re = func(*args,**kwargs)
                end = time.time()
                print(end - start)
                return re
            else:
                re = func(*args, **kwargs)
                return re
        return inner
    return timer

# @outer相当于下面这两句
# timer = outer(timer)   先是调用outer返回timer，
# @timer  然后再@timer进行装饰,说到底outer函数只是传了个参数过来,所以叫做带参数的装饰器

@outer(flag)
def wahaha():
    time.sleep(0.01)
    print('wahahaha')

@outer(flag)
def jianghu():
    time.sleep(0.01)
    print('jianghuhu')


wahaha()
jianghu()


# 2、多个装饰器装饰一个函数
def wrapper1(func):
    def inner2():
        print('wrapper1 ,before func')      # 2
        func()
        print('wrapper1 ,after func')       # 3
    return inner2

def wrapper2(func):
    def inner2():
        print('wrapper2 ,before func')      #1
        func()
        print('wrapper2 ,after func')       # 4
    return inner2


@wrapper2
@wrapper1
def f():
    print('in f')

# 调用函数
f()

# wrapper2 ,before func
# wrapper1 ,before func
# in f
# wrapper1 ,after func
# wrapper2 ,after func


def wrapper1(func):
    def inner2():
        print('wrapper1 ,before func')      # 1
        func()
        print('wrapper1 ,after func')       # 4
    return inner2

def wrapper2(func):
    def inner2():
        print('wrapper2 ,before func')      # 2
        func()
        print('wrapper2 ,after func')       # 3
    return inner2


@wrapper1
@wrapper2
def f():
    print('in f')
#
# # 调用函数
# f()

# wrapper1 ,before func
# wrapper2 ,before func
# in f
# wrapper2 ,after func
# wrapper1 ,after func




def wrapper1(func):
    def inner2():
        print('wrapper1 ,before func')      # 1
        func()
        print('wrapper1 ,after func')       # 6
    return inner2

def wrapper2(func):
    def inner2():
        print('wrapper2 ,before func')      # 2
        func()
        print('wrapper2 ,after func')       # 5
    return inner2

def wrapper3(func):
    def inner3():
        print('wrapper3 ,before func')      # 3
        func()
        print('wrapper3 ,after func')       # 4
    return inner3


@wrapper1
@wrapper2
@wrapper3
def f():
    print('in f')

# 调用函数
f()

# wrapper1 ,before func  被装饰函数之前的所有功能执行顺序
# wrapper2 ,before func  被装饰函数之前的所有功能执行顺序
# wrapper3 ,before func  被装饰函数之前的所有功能执行顺序
# in f
# wrapper3 ,after func   被装饰函数之后的所有功能执行顺序
# wrapper2 ,after func   被装饰函数之后的所有功能执行顺序
# wrapper1 ,after func   被装饰函数之后的所有功能执行顺序


# 结论：
# 先写的那个装饰器先执行被装饰函数之前的那个功能，
# 然后执行另一个装饰的被装饰函数之前的那个功能，
# 后面被装饰函数之前的功能执行完了就接着这个装饰器去执行被装饰函数之后的功能

