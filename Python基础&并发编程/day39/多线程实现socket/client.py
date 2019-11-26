# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/18 14:14
# @Software       : Python_study
# @Python_verison : 3.7
import socket
ss = socket.socket()
ss.connect(('127.0.0.1',9986))

print(ss.recv(1024).decode('utf-8'))
msg = input('请输入：')
ss.send(msg.encode('utf-8'))


ss.close()
