# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/17 9:36
# @Software       : PythonStudy
# @Python_verison : 3.7

# 客户端：执行命令
import socket
import subprocess
ss = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1',9987)
while True:
    ss.sendto('你好'.encode('utf-8'),ip_port)
    cmd,addr = ss.recvfrom(1024)
    res = subprocess.Popen(cmd.decode('gbk'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    std_out = 'stdout:'+ res.stdout.read().decode('gbk')
    std_err = 'stderr:'+ res.stderr.read().decode('gbk')
    ss.sendto(std_out.encode('utf-8'),addr)
    ss.sendto(std_err.encode('utf-8'),addr)
ss.close()
