# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/17 16:27
# @Software       : PythonStudy
# @Python_verison : 3.7

import socket
ss = socket.socket()
ss.connect(('127.0.0.1',8899))
ss.send(bytes('hello'.encode('utf-8')))
ss.send(bytes('egg'.encode('utf-8')))
ss.close()


# 解决黏包
import socket
import time
ss = socket.socket()
ss.connect(('127.0.0.1',8899))
ss.send(bytes('hello'.encode('utf-8')))
time.sleep(1)
ss.send(bytes('egg'.encode('utf-8')))
ss.close()