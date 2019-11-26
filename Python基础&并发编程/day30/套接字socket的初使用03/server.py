# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/11 9:32
# @Software       : PythonStudy
# @Python_verison : 3.7

# 基于TCP的socket：
# tcp是基于链接的，必须先启动服务端，然后再启动客户端去链接服务端

# 1、简单的socket通信
'''
import socket
ss = socket.socket()                # 创建socket对象
ss.bind(('127.0.0.1',8996))        # 绑定地址和ip
ss.listen()                         # 监听链接
conn,address = ss.accept()          # 接收客户端链接
print(conn,address)
res = conn.recv(1024)                 # 接收客户端信息，并且设置接收大小
print(res)
conn.send(b'hi')                    # 向客户端发送信息，必须是传bytes类型，因为网络传输都是用的bytes类型
conn.close()                        # 关闭客户端socket
ss.close()                          # 关闭服务端socket

# 一个发送send就有一个接收recv

# 2、谈话通过socket
import socket
ss = socket.socket()
# ss.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #重启server报错，后就在在bind前加
ss.bind(('127.0.0.1',9991))
ss.listen()
conn,addr = ss.accept()
while True:
    res = conn.recv(1024)
    print(res.decode('utf-8'))
    conn.send(bytes('不想吃饭'.encode('utf-8')))
    res1 = conn.recv(1024)
    print(res1.decode('utf-8'))
    conn.send(bytes('那我就勉为其难吃点吧。'.encode('utf-8')))
conn.close()
ss.close()
'''
# 3、输入
import socket
ss = socket.socket()
# ss.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #重启server报错，后就在在bind前加
ss.bind(('127.0.0.1',9994))
ss.listen()
conn,addr = ss.accept()
while True:
    res = conn.recv(1024).decode('utf-8')
    print(res)
    if res == 'bye':
        break
    conn.send(bytes(input('>>>').encode('utf-8')))
conn.close()
ss.close()

