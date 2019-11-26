#-*- coding:utf-8 -*-
# 1、函数：
# 函数定义：
# def func():
#     '函数体'
#
# # 函数调用
# func()

# 2、函数返回值
# 没有返回值

# def func():
#     print('函数体')
#     a = 1   #没有return
#
# def func():
#     print('函数体')
#     a = 1   #有return 返回空
#     return
#
# def func():
#     print('函数体')
#     a = 1   #有return 返回None
#     return None


# 一个返回值，用一个参数接收
# def func():
#     print('函数体')
#     a = 1
#     return a
#
#
# re = func()
# print(re)

# 多个返回值用一个接收，结果为元组
# def func():
#     print('函数体')
#     a = 1
#     b = 2
#     return a,b
#
# re= func()
# print(re)   # (1, 2)

# 多个返回值用相同的多个接收

# def func():
#     print('函数体')
#     a = 1
#     b = 2
#     return a,b
#
# re1,re2= func()
# print(re1,re2)   # 1 2

# 3、函数的参数
'''
站在形参（就是函数定义的时候）的角度：
    位置参数
    动态参数（多个位置参数）
    默认参数
    动态参数（多个默认参数）

# 站在实参（就是函数调用的时候）的角度
    按照位置传参
    按照关键字传参

def func(*args):  # 站在形参的角度就是将传过来的参数组合
    print(args)

func(1,3,4,5)
L = [1,3,4,5]
func(*L)     # 站在实参的角度，给L加上*就是按照顺序打散这个序列
'''
# 4、命名空间
# 顺序从大到小（内置--->全局--->局部），
# 小范围可以使用大范围的变量，大范围不能使用小范围的，
# 如果自己命名空间没有，则一层一层往上找，如果还没找到，就报错
# 4.1内置命名空间：
    # 是python解释器，cpython内置的一些if,for等，在启动cpython时就加载到内存中
# 4.2全局命名空间
    # 函数定义时的函数名，变量等，在程序执行时，按照从上至下一步一步加载到内存中
# 4.3局部命名空间
    # 函数内部定义的变量，函数名等，在函数调用结束而结束
    # 每个函数都有自己的局部命名空间，互相之间不共用

# 5、作用域
# 全局作用域：就是全局命名空间的，全局命名的变量在全局可以使用
# 局部作用域：局部命名空间的就是局部作用域，默认只可以在局部使用

# 6、global
# 如果想让局部命名空间的变量可以作用于全局，可以使用global在变量前来修饰变量
# a = 10
#
# def inner():
#     global a
#     a = 20
#     print(a)
# print(a)
# inner()
# print(a)


# 7、nonlocal
# 如果想在内部改变外部变量的值，可以使用nonlocal进行修饰变量
# def outer():
#     a  = 1
#     def inner():
#         nonlocal a
#         a = 2
#         print('inner',a)
#     inner()
#     print('outer',a)
# outer()

# 8、locals(),globals()分别返回函数的局部变量和全局变量
# def outer():
#     c = 100
#     def inner():
#         a = 12
#         b = 20
#         print(locals())
#         print(globals())
#     inner()
# outer()
# print(globals())
# print(locals())   #放在全局返回全局变量


# 9、函数调用实质是内存地址（）只是因为内存地址是16进制，解释器帮我们转换为str


# 10、函数的嵌套
# 嵌套定义
# def func1():
#     a = 1
#     func1()
#     b = 2


# 嵌套调用
# def func1():
# #     a = 2
# #     def func2():
# #         func1()  # 嵌套调用func1


# 11、函数名
#     1、其实就是函数的内存地址
#     2、可以作为返回值
#     3、可以作为参数传递
#     4、可以作为容器
#     5、可以赋值

# 12、闭包
# 闭包必须是函数嵌套，且内部函数有使用外部函数的变量
# def outer():
#     a = 10
#     def inner():
#         b = a + 10
#         print('b:',b)
#     inner()
#     print(inner.__closure__)   # 判断函数是否为闭包函数
#     print('a:',a)
#
# outer()


# 13、函数外部使用内部函数变量，两种方法
#   1、内部函数使用global
#   2、内部函数返回函数名
# def outer():
#     print('outerfunction')
#     def inner():
#         a = 10
#         print('innerfunction')
#         return a
#     return inner
#
#
# res = outer()  # 此时res就是inner函数名，所以可以直接res()
# result = res()
# print(result)

# 14、闭包函数的应用，---装饰器
# 固定格式

# def wrapper(func):
#
#     '被装饰函数之前可以添加的功能'
#     def inner(*args,**kwargs):
#         '被装饰函数之后可以添加的功能'
#         res = func(args,kwargs)
#         return res
#     return inner
#
# @wrapper
# def func(*args, **kwargs):
#     print('你们好')
#
# # 调用
# # func = wrapper(func)
# func()





# def wrapper(func):
#     # '被装饰函数之前可以添加的功能'
#     def inner(*args, **kwargs):
#         # '被装饰函数之后可以添加的功能'
#         print('大家好')
#         res = func(args, kwargs)
#         return res
#     return inner
#
# @wrapper
# def func(*args, **kwargs):
#     print('你们好')
#
# # func = wrapper(func)
# func()


# 14、装饰器遵循一个原则：开放封闭原则
    # 对扩展是开放的
    # 对修改是封闭的

# 15、带参数的装饰器
import time
# flag = False
# flag = True
# def outer(flag):
#     def timer(func):
#         def inner(*args,**kwargs):
#             if flag:
#                 start = time.time()
#                 re = func(*args,**kwargs)
#                 end = time.time()
#                 print(end - start)
#                 return re
#             else:
#                 re = func(*args, **kwargs)
#                 return re
#         return inner
#     return timer

# @outer相当于下面这两句
# timer = outer(timer)   先是调用outer返回timer，
# @timer  然后再@timer进行装饰,说到底outer函数只是传了个参数过来,所以叫做带参数的装饰器

# @outer(flag)
# def wahaha():
#     time.sleep(0.01)
#     print('wahahaha')
#
# @outer(flag)
# def jianghu():
#     time.sleep(0.01)
#     print('jianghuhu')
#
#
# wahaha()
# jianghu()


# 16、多个装饰器装饰一个函数

# def wrapper1(func):
#     def inner2():
#         print('wrapper1 ,before func')      # 1
#         func()
#         print('wrapper1 ,after func')       # 7
#     return inner2
#
# def wrapper2(func):
#     def inner2():
#         print('wrapper2 ,before func')      # 2
#         func()
#         print('wrapper2 ,after func')       # 6
#     return inner2
#
# def wrapper3(func):
#     def inner3():
#         print('wrapper3 ,before func')      # 3
#         func()
#         print('wrapper3 ,after func')       # 5
#     return inner3
#
#
# @wrapper1
# @wrapper2
# @wrapper3
# def f():
#     print('in f')   # 4
#
# f()


# 17、想要获取被装饰函数的注释，名称，内置函数，使用wraps
from functools import wraps
def wrapper(func):
    # '被装饰函数之前可以添加的功能'
    @wraps(func)
    def inner(*args, **kwargs):
        '''这个是inner函数'''
        # '被装饰函数之后可以添加的功能'
        print('大家好')
        res = func(args, kwargs)
        return res
    return inner

@wrapper
def func(*args, **kwargs):
    '''这个是函数'''
    print('你们好')

print(func.__name__)
print(func.__doc__)


func()