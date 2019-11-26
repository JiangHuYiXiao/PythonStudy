# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/13 9:37
# @Software       : PythonStudy
# @Python_verison : 3.7
import socket
ss = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1',9983)
while True:
    input_msg = input('>>>客户端1输入：')
    info = ('\033[1;31m来自client1的消息：%s'%input_msg).encode('utf-8')
    ss.sendto(info,ip_port)
    msg,addr = ss.recvfrom(1024)
    print(msg.decode('utf-8'))
ss.close()