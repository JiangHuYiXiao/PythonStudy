# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/13 15:59
# @Software       : PythonStudy
# @Python_verison : 3.7
import socket
import subprocess
ss = socket.socket()
ss.connect(('127.0.0.1',9988))
while True:
    cmd = ss.recv(1024)
    # print(cmd.decode('utf-8'))
    res = subprocess.Popen(cmd.decode('utf-8'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    # print(res.stdout.read())            # bytes类型
    # print(res.stderr.read())            # bytes类型
    std_out = 'stdout:'+ res.stdout.read().decode('gbk')
    std_err = 'stderr:'+ res.stderr.read().decode('gbk')
    # print(std_out)
    # print(std_err)
    ss.send(bytes(std_out.encode('utf-8')))
    ss.send(bytes(std_err.encode('utf-8')))
ss.close()