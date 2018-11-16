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

