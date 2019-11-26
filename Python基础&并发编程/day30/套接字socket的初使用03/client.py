# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/11 9:33
# @Software       : PythonStudy
# @Python_verison : 3.7
'''
# 1、简单的socket通信
import socket
ss = socket.socket()            # 创建socket对象
ss.connect(('127.0.0.1',8996))          # 链接服务器
ss.send(b'hello')                   # 发送信息给服务端
res = ss.recv(1024)             # 接收服务端信息
print(res)
ss.close()                  # 关闭客户端套接字socket


# 2、谈话通过socket
import socket
ss = socket.socket()
ss.connect(('127.0.0.1',9991))
while True:
    ss.send(bytes('吃了午饭没'.encode('utf-8')))
    ret = ss.recv(1024)
    print(ret.decode('utf-8'))
    ss.send(bytes('不想吃饭也要意思下吃点'.encode('utf-8')))
    ret2 = ss.recv(1024)
    print(ret2.decode('utf-8'))
ss.close()
'''

# 3、输入
import socket
ss = socket.socket()
ss.connect(('127.0.0.1',9994))
while True:
    info = input('>>>').encode('utf-8')
    ss.send(bytes(info))
    ret =ss.recv(1024).decode('utf-8')
    print(ret)
    if ret == 'bye':
        ss.send(bytes('bye'.encode('utf-8')))
        break