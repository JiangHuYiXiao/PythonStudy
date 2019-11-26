# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/13 10:41
# @Software       : PythonStudy
# @Python_verison : 3.7
import socket

ss = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1',9977)
time_format = input('>>>请输入客户端需要的时间格式：')
# time_format = '%Y-%m-%d %H:%M:%S'
ss.sendto(time_format.encode('utf-8'),ip_port)
result,addr = ss.recvfrom(1024)
print(result.decode('utf-8'))
ss.close()