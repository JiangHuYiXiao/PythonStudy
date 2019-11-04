# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/4 9:13
# @Software       : Python_study
# @Python_verison : 3.7
import socket
ss = socket.socket()
ss.connect(('127.0.0.1',8877))
res = ss.recv(1024)
print(res.decode('utf-8'))
ss.send(bytes(input('请输入：').encode('utf-8')))
ss.close()