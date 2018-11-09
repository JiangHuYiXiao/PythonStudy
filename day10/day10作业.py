# -*- coding:utf-8 -*-
# 1、写函数，接收n个数字，求这些参数数字的和。
# def cal_sum(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     return sum
# print(cal_sum(1,3,554,333,443,554))


# 2、读代码，回答，代码中打印出来的a,b,c,分别是什么，为啥？
# a = 10
# b = 20
# def test5(a,b):
#     print(a,b)
#
# c = test5(b,a)   # 调用函数test5
# print(c)

# res:a = 20,b = 10,c = None
# 3、读代码，回答，代码中打印出来的a,b,c,分别是什么，为啥？
# a = 10
# b = 20
# def test5(a,b):
#     a = 3
#     b = 5
#     print(a,b)
#
# c = test5(b,a)    # 调用函数test5
# print(c)

# res:a = 3,b = 5,c = None

# 4、用面向函数的思想完成购物车作业
# 函数1：实现三次登录功能
# 函数2：实现新用户注册功能
# 函数3：购物功能
# 进阶：将购物功能拆分成多个函数

def register(name,password):
    with open('注册信息',mode='w+',encoding='utf-8') as file:
        file.write('{}\n{}'.format(name,password)



def three_login(login_name,login_password):
    with open()
    i = 0
    for i in range(3):
        if



