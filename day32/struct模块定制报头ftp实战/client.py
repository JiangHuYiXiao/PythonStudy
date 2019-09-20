# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/19 8:55
# @Software       : PythonStudy
# @Python_verison : 3.7
# client端读文件后发送文件
import os
import socket
import struct

ss = socket.socket()
ss.connect(('127.0.0.1',9907))
file_name = '01 python fullstack s9day33 复习.mp4'
path1 = 'E:\BaiduNetdiskDownload\Python\老男孩Python\day33'
file_path = os.path.join(path1,file_name)
file_size = os.path.getsize(file_path)
# 定义报头
head = {'file_name':'01 python fullstack s9day33 复习.mp4','file_size':file_size,'file_type':'mp4','file_path':file_path}
# 首先发送文件的大小
file_len_bytes = struct.pack('i',file_size)
ss.send(file_len_bytes)
# 读文件
while True:
    with open(file_path,mode='rb') as file:
        file.read()
        if file_size >= 1024:
            file_size = file_size -1024
        else:
            ss.send()


ss.send()
ss.close()
