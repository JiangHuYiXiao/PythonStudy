# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/19 8:55
# @Software       : PythonStudy
# @Python_verison : 3.7
# 需求：实现一个大文件的上传或者下载
# 配置文件 IP地址，端口号
# server端接收文件后写文件

import json
import socket
import struct

ss = socket.socket()
ss.bind(('127.0.0.1',9907))
ss.listen()
conn,addr = ss.accept()
head_len = conn.recv(4)           # 接收报头的长度
print(head_len)
head_len = struct.unpack('i',head_len)[0]
print(head_len)
json_head = conn.recv(head_len).decode('utf-8')
head = json.loads(json_head)   # head字典
file_size = head['file_size']
# 先接收文件后写文件
with open(head['file_name'],mode='wb') as file:
    while file_size:
        if file_size >= 1024:
            content = conn.recv(1024)
            file.write(content)
            file_size = file_size - 1024
        else:
            content = conn.recv(file_size)
            file.write(content)
            break

conn.close()
ss.close()