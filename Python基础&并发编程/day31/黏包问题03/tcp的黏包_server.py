# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/13 15:58
# @Software       : PythonStudy
# @Python_verison : 3.7
# 需求：基于tcp远程执行命令
# server发送命令
# client接收命令并且执行命令

import socket

ss = socket.socket()
ss.bind(('127.0.0.1',9988))
ss.listen()
conn,add = ss.accept()
# subprocess.Popen('dir',shell=True,stdout=)
while True:
    cmd = input('>>>:')
    conn.send(bytes(cmd.encode('utf-8')))
    result1 = conn.recv(1024).decode('gbk')
    result2 = conn.recv(1024).decode('gbk')
    print(result1,result2)
conn.close()
ss.close()