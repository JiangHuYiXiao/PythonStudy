# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/10/29 10:05
# @Software       : client
# @Python_verison : 3.7
'''
认证：登录、注册、退出的方法
'''
import json
from core.socket_client import SocketClient
class Auth:
    # 设置单例模式避免每次登录或者注册的时候要创建对象和链接
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            obj = object.__new__(cls)
            cls.__instance = obj
        return cls.__instance
    # 初始化的时候进立链接
    def __init__(self):
        self.socket = SocketClient()
        self.username = None
    def login(self):
        username = input('username:')
        password = input('password:')
        if username.strip() and password.strip():
            # send
            self.socket.mysend({'username': username, 'password': password,'operation':'login'})
        ret = self.socket.sk.recv(1024)
    def register(self):
        username = input('username:')
        password1 = input('password1:')
        password2 = input('password2:')
        if username.strip() and password1.strip() and password1==password2:
            self.socket.mysend({'username': username, 'password': password1,'operation':'register'})
        ret = self.socket.sk.recv(1024)
'''
class A:
    __instance = False
    def __init__(self,name):
        self.name = name
    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance
        else:
            cls.__instance = object.__new__(cls)
            return cls.__instance

a1 = A('egon')
a2 = A('son')
print(a1)           # <__main__.A object at 0x0000000001F05780>

print(a2)           # <__main__.A object at 0x0000000001F05780>

print(a1.name)          # son
print(a2.name)          # son  证明了每次都是用的同一个对象，单实例

'''
