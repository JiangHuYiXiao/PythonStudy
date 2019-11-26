# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/10/29 14:58
# @Software       : client
# @Python_verison : 3.7
'''
初始化链接和发送信息
'''
import socket
import json
# from  import setting
class SocketClient:
    def __init__(self):
        self.sk = socket.socket()
        self.sk.connect(('127.0.0.1',9956))
    def mysend(self,msg):
        # dict = {'username': 'alex', 'password': 'alex3714'}  # 字典的网络传输使用json模块进行序列化
        ret_json= json.dumps(msg)
        # json_encode = json_dict.encode('utf-8')  # 编码方式为utf-8
        self.sk.send(ret_json.encode('utf-8'))