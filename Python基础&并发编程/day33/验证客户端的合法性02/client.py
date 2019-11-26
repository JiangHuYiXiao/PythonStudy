# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/25 8:26
# @Software       : Python_study
# @Python_verison : 3.7
import socket
import hmac
secret_key = b'jianghu'
ss = socket.socket()
ss.connect(('127.0.0.1',9963))
msg = ss.recv(1024)
h = hmac.new(secret_key,msg)
client_digest = h.digest()
ss.send(client_digest)
ss.close()