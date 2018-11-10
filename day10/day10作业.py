# -*- coding:utf-8 -*-
# 1、写函数，接收n个数字，求这些参数数字的和。
def cal_sum(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print(cal_sum(1,3,554,333,443,554))


# 2、读代码，回答，代码中打印出来的a,b,c,分别是什么，为啥？
a = 10
b = 20
def test5(a,b):
    print(a,b)

c = test5(b,a)   # 调用函数test5
print(c)

# res:a = 20,b = 10,c = None
# 3、读代码，回答，代码中打印出来的a,b,c,分别是什么，为啥？
a = 10
b = 20
def test5(a,b):
    a = 3
    b = 5
    print(a,b)

c = test5(b,a)    # 调用函数test5
print(c)

# res:a = 3,b = 5,c = None

# 4、用面向函数的思想完成购物车作业
# 函数1：实现三次登录功能
# 函数2：实现新用户注册功能
# 函数3：购物功能
# 进阶：将购物功能拆分成多个函数

# 函数1、新用户注册函数
def register(name,password):
    # name = input('请输入你的注册的用户名：')
    # password = input('请输入你的密码：')
    with open('注册信息',mode='w+',encoding='utf-8') as file:
        file.write('{}\n{}'.format(name,password))
        file.read()

# 调用注册函数
register('jianghu',123)


# 函数2、登录函数
def three_login(login_name,login_password):
    # login_name = input('请输入用户名：')
    # login_password = input('请输入密码：')

    i = 0
    while i < 3:
        with open('注册信息', mode='r+', encoding='utf-8') as file1:
            for line in file1:
                if line[0] == login_name and line[1] == login_password:
                    print('登录成功')
                    break
                else:
                    print('用户名或者密码错误，请重新登录。')
    i += 1

# 调用登录函数
three_login('jianghu',123)



# 函数3：购物功能

def shopping(goods_num):
    list = [{'name': '香蕉', 'price': 10},
            {'name': '苹果', 'price': 4},
            {'name': '橘子', 'price': 5},
            {'name': '哈密瓜', 'price': 20},
            {'name': '火龙果','price':8}]
    shopping_cart = {}
    your_money = input('请输入你的资产：')
    if int(your_money) <= 4:
        print('你的资金不够，欢迎下次光临')
        return
    else:
        while 1:
            if goods_num in range(len(list)):
                if list[goods_num]['name'] not in shopping_cart:
                    shopping_cart[list[goods_num]['name']] = 1
                else:
                    shopping_cart[list[goods_num]['name']] = shopping_cart[list[goods_num]['name']] + 1
                print(shopping_cart[list[goods_num]['name']])
            remain_money = int(your_money) - shopping_cart[list[goods_num]['name']] * list[goods_num]['price']
            if remain_money < 0:
                print('你的资金不够，欢迎下次光临')
            return shopping_cart

# 调用函数
for i in range(3):
    res = shopping(i)
    print(res)