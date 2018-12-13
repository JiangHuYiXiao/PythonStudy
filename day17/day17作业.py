# -*- coding:utf-8 -*-
# 1、斐波那契 ，问第n个斐波那契数是多少？
# 1,1,2,3,5,8
# 用递归解决问题，一般都是从最后一个数往前面推导
# fib(5) fib(4) + fib(3)
# fib(4) fib(3) + fib(2)
# fib(3) fib(2) + fib(1)
# fib(2)=1
# fib(1)=1

# def fib(3):
#     if n == 1 or n == 2:       # 结束条件
#         return 1               # 需要返回值
#     return (fib(3-1) + fib(3-2))     # 需要返回值
#
# def fib(2):
#     if n == 1 or n == 2:       # 结束条件
#         return 1               # 需要返回值 ，返回给了fib（2）和fib（1）
#     return (fib(n-1) + fib(n-2))     # 需要返回值

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n -2)    # 如果一个函数里面有两次递归，那么查询效率很慢，

print(fib(10))

# 2、推到出阶乘的函数，使用递归
# fac(4) = 4*3*2*1
# fac(3) = 3*2*1
# fac(2) = 2*1
# fac(1) = 1

def fac(n):
    if n ==1:
        return 1
    else:
        return n*fac(n-1)

print(fac(6))



