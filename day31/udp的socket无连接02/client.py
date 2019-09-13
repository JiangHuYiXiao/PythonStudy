# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/12 16:14
# @Software       : PythonStudy
# @Python_verison : 3.7
import socket
ss = socket.socket(type = socket.SOCK_DGRAM)
ip_port = ('127.0.0.1',9962)
ss.sendto(bytes('你好呀'.encode('utf-8')),ip_port)
msg,addr = ss.recvfrom(1024)
print(msg.decode('utf-8'))
ss.close()