# -*- coding:utf-8 -*-
# 1、命名空间
# a、内置命名空间
#      作用时间：在启动python解释器的时候就加载到内存中。
#      包含：if，print，while，for，def 等内置函数
# b、全局命名空间
#       作用时间：是在程序从上到下被执行的过程加载到内存里面
#       包含:函数外部定义的变量名，函数名，等
# c、局部命名空间
#       作用时间：在函数内部定义的变量，当函数调用的时候加载到内存里，随着函数的调用结束而结束。
#       包含:函数内部定义的变量名，函数名，等

# a = 1  #全局命名空间包含  a，func
# def func(b):
#     b = b + 2 #局部命名空间  b
#     return b
# print(func(1))

# 他们三者从大到小范围是内置命名空间，全局命名空间，局部命名空间，小范围的底层的可以使用上层的，直到找到最近的第一个为止
# 局部命名空间可以使用局部命名空间和内置命名空间和全局命名空间的变量，先使用局部的
# 全局命名空间可以使用全局命名空间和内置命名空间的变量，先使用全局的
# 内置命名空间只可以使用内置空间的变量

# 1、局部命名空间使用内置命名空间和全局命名空间的变量
# a = 1
# def func(b):
#     return max(a,b)   #使用内置命名空间max，和全局命名空间a
#
# print(func(2))

# 2、局部命名空间使用局部命名空间的变量
# a = 1
# def func(b):
#     c = 3
#     return max(a,b,c)     #使用局部命名空间c
#
# print(func(2))

# 3、全局命名空间不能使用局部命名空间的变量
# a = 1
# def func(b):
#     c = 3
#     return max(a,b,c)
# print(c)      #不能使用局部命名空间c
# print(func(2))

# 4、全局命名空间使用全局命名空间的变量
# a = 1
# def func(b):
#     c = 3
#     return max(a,b,c)
# print(a)      #使用全局命名空间a
# print(func(2))

# 5、全局命名空间使用内置命名空间的变量
# a = 1
# def func(b):
#     c = 3
# print(max(a,2))      #使用内置命名空间max
# print(func(2))

# 6、如果在局部命名空间里面没有该变量则找该局部命名空间上一层的最近的第一个为止。
# a = 1
# def outer(b):
#     a = 2
#     def inner1():
#         print(a)
#     inner1()
# print(outer(2))   # 2

# a = 1
# def outer(b):
#     def inner1():
#         print(a)
#     inner1()
# print(outer(2))   # 1

# 7、全局命名空间可以使用全局命名空间的变量和内置命名空间的变量，不过先使用全局命名空间的，如果全局找不到再去找内置命名空间的

# def input():
#     print('my_input')
# input()    # my_input

# def input1():
#     print('my_input')
# input()    # 提示输入，使用内置命名空间的input

# 8、局部命名空间可以使用局部命名空间的变量和全局的，以及内置的，但是先使用局部命名空间的变量
# a = 1
# def max(a,b):
#     a = 200
#     print(a)
# max(1,2)     # 200

def input():
    print('in put now')
def func():
    input()
func()   # in put now   j局部的input先找局部没有找到则找全局的，全局找到了则不会再往上找内置的
