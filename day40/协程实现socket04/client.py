# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/25 8:21
# @Software       : Python_study
# @Python_verison : 3.7
import socket
import time
ss = socket.socket()
ss.connect(('127.0.0.1',8868))
while True:
    ss.send(bytes('hi'.encode('utf-8')))
    client_res = ss.recv(1024).decode('utf-8')
    print(client_res)
    time.sleep(1)
ss.close()
