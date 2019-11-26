# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/12 16:14
# @Software       : PythonStudy
# @Python_verison : 3.7
import socket
ss = socket.socket(type=socket.SOCK_DGRAM)    # 和tcp协议不同的是需要加上SOCK.DGRAM
ss.bind(('127.0.0.1',9962))                  # 绑定服务端的地址和端口
# 不需要监听
msg,addr = ss.recvfrom(1024)                    # 接收使用recvfrom,必须先接收，后发送,接收的是一个信息和一个地址
print(msg.decode('utf-8'))
ss.sendto(bytes('你好'.encode('utf-8')),addr)     # 不管是客户端还是服务端发送消息的时候必须指定地址信息
ss.close()
