# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/12 14:00
# @Software       : PythonStudy
# @Python_verison : 3.7

# 1、详解
'''
import socket
ss = socket.socket()                # 创建socket对象
ss.bind(('127.0.0.1',9975))        # 给服务端绑定一个IP地址和端口号
ss.listen()                         # 监听
conn,addr = ss.accept()             # 接收客户端的链接、完成三次握手
while True:
    result = conn.recv(1024).decode('utf-8')            # 阻塞，只有等到client发送消息过来后才通顺
    if result == 'bye':
        conn.send(bytes('bye'.encode('utf-8')))
        break
    else:
        print(result)
    info= input('>>>服务端返回:')
    if info == 'bye':
        conn.send(bytes(info.encode('utf-8')))
        break
    else:
        conn.send(bytes(info.encode('utf-8')))     # 发送消息

conn.close()                                    # 关闭链接
ss.close()                                      # 关闭socket
'''

# 2、多个客户端请求
import socket
ss = socket.socket()                # 创建socket对象
ss.bind(('127.0.0.1',9975))        # 给服务端绑定一个IP地址和端口号
ss.listen()                         # 监听
while True:
    conn,addr = ss.accept()             # 接收客户端的链接、完成三次握手
    while True:
        result = conn.recv(1024).decode('utf-8')            # 阻塞，只有等到client发送消息过来后才通顺
        if result == 'bye':
            conn.send(bytes('bye'.encode('utf-8')))
            break
        else:
            print(result)
        info= input('>>>服务端返回:')
        if info == 'bye':
            conn.send(bytes(info.encode('utf-8')))
            break
        else:
            conn.send(bytes(info.encode('utf-8')))     # 发送消息

    conn.close()                                    # 关闭链接，但是可以使用其他链接，只要没有关闭socket


ss.close()                                      # 关闭socket

# 当用多个client链接server时，对于TCP协议，只有等到client1断开后，才可以传输信息,一个server不能同时跟两个client传输信息