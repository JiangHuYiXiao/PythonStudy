# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/17 9:35
# @Software       : PythonStudy
# @Python_verison : 3.7
# 需求：基于udp远程执行命令
# 服务端：发送命令
import socket
ss = socket.socket(type=socket.SOCK_DGRAM)
ss.bind(('127.0.0.1',9987))
conn,addr = ss.recvfrom(1024)
while True:
    cmd = input('>>>:')
    ss.sendto(bytes(cmd.encode('utf-8')),addr)
    result1,addr = ss.recvfrom(1024)
    result2,addr = ss.recvfrom(1024)
    print(result1.decode('utf-8'),result2.decode('utf-8'))
ss.close()

# udp没有黏包现象，没有发完就不发了