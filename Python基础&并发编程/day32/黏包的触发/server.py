# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/17 16:02
# @Software       : PythonStudy
# @Python_verison : 3.7
import socket
ss = socket.socket()
ss.bind(('127.0.0.1',8899))
ss.listen()
conn,addr = ss.accept()
res1 = conn.recv(2)
res2 = conn.recv(8)
print(res1)
print(res2)
conn.close()
ss.close()

# 结果：
# b'he'
# b'llo,egg'

# 这个例子，产生了黏包现象，本质是不知道客户端发送的数据的长度