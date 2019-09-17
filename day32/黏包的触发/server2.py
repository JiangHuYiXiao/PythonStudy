# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/17 16:26
# @Software       : PythonStudy
# @Python_verison : 3.7
import socket
ss = socket.socket()
ss.bind(('127.0.0.1',8899))
ss.listen()
conn,addr = ss.accept()
res1 = conn.recv(12)
res2 = conn.recv(12)
print(res1,res2)

conn.close()
ss.close()

# 结果：b'helloegg'
# 产生了黏包，本质是因为两次send的数据太小，时间短

# 解决这种原因可以在send中间插入时间等待