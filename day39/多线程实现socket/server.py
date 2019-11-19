# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/18 14:11
# @Software       : Python_study
# @Python_verison : 3.7

# 多线程实现socket通信
import threading
from threading import Thread
import socket
ss = socket.socket()
ss.bind(('127.0.0.1',9986))
ss.listen()


def func(conn):
    conn.send(bytes('hello'.encode('utf-8')))
    res = conn.recv(1024).decode('utf-8')
    print(res)
    conn.close()            # 每次开启一个线程时候就应该关闭，如果放外面那么最后只能关闭最后一个线程

while True:         # 服务端需要一直开着，然后客户端可以开启多个，所以客户端不需要写多线程，和循环
    conn,addr = ss.accept()
    t = Thread(target=func,args=(conn,))
    t.start()


ss.close()
