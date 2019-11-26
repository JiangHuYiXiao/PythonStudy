# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/19 8:55
# @Software       : PythonStudy
# @Python_verison : 3.7
# client端读文件后发送文件

import json
import os
import socket
import struct

ss = socket.socket()
ss.connect(('127.0.0.1',9907))
file_name = r'01 python fullstack s9day33 复习.mp4'
path1 = r'E:\BaiduNetdiskDownload\Python\老男孩Python\day33'
file_path = os.path.join(path1,file_name)

# 定义报头
head = {'file_name':file_name,'file_size':None,'file_type':'mp4','file_path':file_path}
# 要发送的文件的大小
file_size = os.path.getsize(file_path)
head['file_size'] = file_size
# 将报头转成字符串进行网络传输
json_head = json.dumps(head)
# 字符串转bytes
bytes_head = json_head.encode('utf-8')
# 计算head的长度
head_len = len(bytes_head)
print(head_len)
# 使用stuct模块将报头长度转换成4个字节
pack_len = struct.pack('i',head_len)
# 发送报头长度
ss.send(pack_len)
# 发送报头
ss.send(bytes_head)
# 读文件并且发送文件
with open(file_path,mode='rb') as file:
    while file_size:
        if file_size >= 1024:
            content = ss.send(file.read(1024))
            file_size = file_size - 1024
            ss.send(bytes(content))
        else:
            content = file.read(file_size)
            ss.send(bytes(content))
            break

ss.close()

