# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/13 9:37
# @Software       : PythonStudy
# @Python_verison : 3.7
import socket
ss = socket.socket(type = socket.SOCK_DGRAM)
ss.bind(('127.0.0.1',9983))
while True:
    msg,addr = ss.recvfrom(1024)
    print(msg.decode('utf-8'),addr)
    info = input('>>>服务端输入：')
    info = ('\033[1;31m来自服务端的返回：%s'%info).encode('utf-8')
    ss.sendto(bytes(info),addr)

ss.close()