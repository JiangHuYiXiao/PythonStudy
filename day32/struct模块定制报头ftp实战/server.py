# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/19 8:55
# @Software       : PythonStudy
# @Python_verison : 3.7
# 需求：实现一个大文件的上传或者下载
# 配置文件 IP地址，端口号
# server端接收文件后写文件
import socket

ss = socket.socket()
ss.bind(('127.0.0.1',9907))
ss.listen()
conn,addr = ss.accept()
result = conn.recv(1024)


conn.close()
ss.close()