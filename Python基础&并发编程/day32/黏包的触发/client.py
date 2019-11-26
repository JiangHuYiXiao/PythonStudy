# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/17 16:02
# @Software       : PythonStudy
# @Python_verison : 3.7
import socket
ss = socket.socket()
ss.connect(('127.0.0.1',8899))
ss.send(bytes('hello,egg'.encode('utf-8')))
ss.close()