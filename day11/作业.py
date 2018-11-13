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

#-*- coding:utf-8 -*-
# 1、编写装饰器，为多个函数添加上认证的功能，
# 要求登录成功一次，后续函数都无需再输入用户名和密码
'''
flag = False
def wrapper(func):
    def inner(*args, **kwargs):
        global flag  # 声明一个全局变量这样在函数内部修改了flag后，会同步到全局，一般写函数头
        if flag:
            re = func(*args, **kwargs)
            return re
        else:
                name = input('请输入用户名:')
                pass_word = input('请输入密码:')
                if 'jianghu' == name and '123' == pass_word:
                    flag = True
                    re = func(*args,**kwargs)
                    return re
                else:
                    print('登录失败')
    return inner

@wrapper
def login():
    return '添加成功'
@wrapper
def delete():
    return '删除成功'


res = login()
print(res)
res1 = delete()
print(res1)
'''


# 2、编写装饰器，为多个函数加上记录调用功能，要求每次调用函数都将被调用函数的名称写入文件
'''
def log(func):
    def inner(*args,**kwargs):
        res = func(*args,**kwargs)   # 被装饰的函数
        with open('log',mode='a+',encoding='utf-8') as file:
            file.write(func.__name__ + '\n')   # 加上换行符，否则所有被调用的函数都在一行，
            print(file.read())
        return res
    return inner

@log
def add(*args,**kwargs):
    return ('添加物品')

@log
def delete(*args,**kwargs):
    return ('删除物品')


res = add(1)
print(res)

res1 = delete(2)
print(res1)
'''


# 3、进阶作业：
# 1、编写一个下载网页内容的函数，要求功能是，用户传入一个URL，函数返回下载页面的结果
# 2、为题目1编写装饰器，实现缓存网页内容的功能
# 具体：实现下载的页面，存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，否则就去下载
'''
# 1、
# 方法1
def get_url(url):
    from urllib.request import urlopen
    info = urlopen(url)
    with open('web_url',mode= 'w',encoding='utf-8')as file:
        file.write(str(info))
    return urlopen(url)

get_url('https://www.baidu.com/')

# 方法2
def get_url(url):
    from urllib.request import urlopen
    code = urlopen(url).read
    return code


res = get_url('http://www.baidu.com')
print(res)            # <bound method HTTPResponse.read of <http.client.HTTPResponse object at 0x0000000002ED70F0>>
'''

# 2、
def cache(*args,**kwargs):
    def inner(func):
        with open('cache',mode='wb+') as file:
            if file.__sizeof__() > 0:
                return file.read
            else:
                ret = get_url(func)
                file.write(ret)
                return ret
    return inner

@cache
def get_url(url):
    from urllib.request import urlopen
    code = urlopen(url).read
    return code


res = get_url('http://www.baidu.com')
print(res)            # <bound method HTTPResponse.read of <http.client.HTTPResponse object at 0x0000000002ED70F0>>

