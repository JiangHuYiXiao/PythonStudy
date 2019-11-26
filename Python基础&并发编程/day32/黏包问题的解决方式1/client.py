# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/18 8:21
# @Software       : PythonStudy
# @Python_verison : 3.7
import socket
import subprocess
ss = socket.socket()
ss.connect(('127.0.0.1',9966))
while True:
    cmd = ss.recv(1024)
    if cmd =='q':
        break
    res = subprocess.Popen(cmd.decode('utf-8'),shell=True,stdout = subprocess.PIPE,stderr=subprocess.PIPE)
    # std_out = 'stdout:'+ res.stdout.read().decode('gbk')
    # std_err = 'stdout:'+ res.stderr.read().decode('gbk')
    std_out = res.stdout.read()         # 改成变量是因为通过管道执行时的数据不能调用两次
    std_err = res.stderr.read()         # 改成变量是因为通过管道执行时的数据不能调用两次
    ss.send((str(len(std_out))+str(len(std_err))).encode('gbk'))
    ss.recv(1024)
    ss.send(std_out)        # 这里使用std_out就没有使用两次
    ss.send(std_err)        # 这里使用std_out就没有使用两次
ss.close()

