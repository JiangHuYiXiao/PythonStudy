# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/25 8:19
# @Software       : Python_study
# @Python_verison : 3.7
from gevent import monkey;monkey.patch_all()
import socket
import gevent
import time
ss = socket.socket()
ss.bind(('127.0.0.1',8868))
ss.listen()

def task(conn):
    while True:
        server_res = conn.recv(1024).decode('utf-8')
        print(server_res)
        conn.send(server_res.upper().encode('utf-8'))
    conn.close()

while True:
    conn, addrs = ss.accept()
    gevent.spawn(task,conn)

ss.close()

