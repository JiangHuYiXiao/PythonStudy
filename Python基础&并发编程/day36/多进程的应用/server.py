# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/4 9:13
# @Software       : Python_study
# @Python_verison : 3.7
import socket
from multiprocessing import Process
def talk(conn):
    conn.send(bytes('client 你好'.encode('utf-8')))
    res = conn.recv(1024)
    print(res.decode('utf-8'))

if __name__ == '__main__':
    ss = socket.socket()
    ss.bind(('127.0.0.1',8877))
    ss.listen()
    while True:
        conn,addr = ss.accept()
        p = Process(target=talk,args=(conn,))
        p.start()

    conn.close()
    ss.close()