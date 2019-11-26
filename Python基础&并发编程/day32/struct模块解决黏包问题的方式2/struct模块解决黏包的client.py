# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/18 15:05
# @Software       : PythonStudy
# @Python_verison : 3.7
import socket
import struct
import subprocess

ss = socket.socket()
ss.connect(('127.0.0.1',9678))
while True:
    cmd = ss.recv(1024).decode('gbk')
    res = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    std_out = res.stdout.read()
    std_err = res.stderr.read()
    len_num = len(std_out)+len(std_err)
    num_bytes = struct.pack('i',len_num)
    ss.send(num_bytes)      # 4个字节
    ss.send(std_out)
    ss.send(std_err)
ss.close()