# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/25 8:26
# @Software       : Python_study
# @Python_verison : 3.7
import socket
import os
import hmac

secret_key = b'jianghu'
ss = socket.socket()
ss.bind(('127.0.0.1',9963))
ss.listen()
def check_conn(conn):
    msg = os.urandom(32)
    conn.send(msg)
    h = hmac.new(secret_key,msg)
    server_digest = h.digest()
    client_digest = conn.recv(1024)
    return hmac.compare_digest(server_digest,client_digest)
conn,addr = ss.accept()
result = check_conn(conn)
if result:
    print('合法的客户端')
    conn.close()
else:
    print('不合法的客户端')
    conn.close()
ss.close()