# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/20 9:15
# @Software       : Python_study
# @Python_verison : 3.7

'''
利用socket编写服务端，然后浏览器作为客户端链接服务器

import socket
ss = socket.socket()

ss.bind(('127.0.0.1',9958))
ss.listen()
while True:
    conn,addr = ss.accept()
    conn.recv(1024)
    conn.send(b'http/1.1 200 ok\r\n\r\nhello')   # 定义一个消息格式
    conn.close()
ss.close()
'''


import socket
ss = socket.socket()

ss.bind(('127.0.0.1',9958))
ss.listen()
while True:
    conn,addr = ss.accept()
    conn.recv(1024)
    conn.send(b'http/1.1 200 ok\r\n\r\n')   # 定义一个消息格式
    # 从文件中读取
    with open('网页1.html',mode='rb')as file:
        msg = file.read()
    conn.send(msg)
    conn.close()
ss.close()




# web框架的本质是：服务端、html、浏览器（客户端）


