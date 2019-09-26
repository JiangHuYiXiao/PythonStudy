# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/25 16:52
# @Software       : Python_study
# @Python_verison : 3.7
import socket
ss = socket.socket()
ss.connect(('127.0.0.1',9999))
while True:
    msg = input('>>>:')
    if msg == 'q':
        ss.close()
    ss.send(('client2:'+ msg).encode('utf-8'))
    result = ss.recv(1024)
    print(result.decode('utf-8'))
ss.close()