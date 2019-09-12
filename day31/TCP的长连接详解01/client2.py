# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/12 14:00
# @Software       : PythonStudy
# @Python_verison : 3.7

import socket
ss = socket.socket()
ss.connect(('127.0.0.1',9975))
while True:
    info = input('>>>client2客户端请求:')
    if info == 'bye':
        ss.send(bytes(('client2' + 'bye').encode('utf-8')))
    else:
        ss.send(bytes(('client2'+ info).encode('utf-8')))
    result = ss.recv(1024).decode('utf-8')
    if result == 'bye':
        print(result)
        break
    else:
        print(result)

ss.close()
