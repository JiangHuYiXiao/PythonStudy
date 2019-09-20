# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/18 15:05
# @Software       : PythonStudy
# @Python_verison : 3.7
import socket
import struct
ss = socket.socket()
ss.bind(('127.0.0.1',9678))
ss.listen()
conn,addr = ss.accept()
while True:
    cmd = input('>>>:')
    if cmd =='q':
        conn.send(b'q')
        break
    else:
        conn.send(bytes(cmd.encode('gbk')))
        num = conn.recv(4)
        num = struct.unpack('i',num)[0]
        result = conn.recv(int(num)).decode('gbk')
        print(result)
conn.close()
ss.close()

# struct模块，该模块可以把一个类型，如数字，转成固定长度的bytes

# 借助struct模块，我们知道长度数字可以被转换成一个标准大小的4字节数字。因此可以利用这个特点来预先发送数据长度。
# 发送时	：
# 先发送struct转换好的数据长度4字节
# 再发送数据

# 接收时：
# 先接受4个字节使用struct转换成数字来获取要接收的数据长度
# 再按照长度接收数据
