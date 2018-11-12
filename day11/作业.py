# -*- coding:utf-8 -*-
# 1、编写装饰器，为多个函数加上认证的功能（用户的账号和密码来源于文件）
# 要求登录成功一次，后续的函数都无需再输入用户名和密码

def login_wrapper(func):
    def inner(name,password):
        with open('登录信息',mode='r+',encoding='utf-8') as file1:
            f = file1.read()
            for line in f:
                login_name= line[0]
                login_password = line[1]
        ret = func(name,password)
        if login_name == name and login_password == password:
            print('恭喜你，通过认证！')
        return ret
    return inner

@login_wrapper    # login = login_wrapper(login)
def login(name,password):
    # name = input('请输入你的账号：')
    # password = input('请输入你的密码：')
    with open('登录信息',mode= 'w+',encoding='utf-8') as file:
        file.write('{}\n{}'.format(name,password))
    return name,password

res = login(1,2)
print(res)
# 2、编写装饰器，为多个函数加上记录调用的功能，要求每次调用函数都将被调用函数名称写入文件