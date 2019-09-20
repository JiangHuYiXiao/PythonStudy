# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/18 8:21
# @Software       : PythonStudy
# @Python_verison : 3.7
# 解决方式1：首先发送一下这个数据有多大，然后再按照数据的长度接收这个数据
import socket
ss = socket.socket()
ss.bind(('127.0.0.1',9966))
ss.listen()
conn,addr = ss.accept()
while True:
    cmd = input('>>>:')
    if cmd== 'q':
        conn.send(b'q')
        break

    conn.send(cmd.encode('utf-8'))
    num = conn.recv(1024).decode('utf-8')
    conn.send(bytes('ok'.encode('utf-8')))
    res = conn.recv(int(num)).decode('gbk')
    print(res)
conn.close()
ss.close()


# 该解决方法的好处：
# 1、确定了我们要接收多大的数据
# 2、要在文件中配置一个配置项，就是每一次recv的大小，一般配置项叫做 buffer = 4096
# 3、在传输大数据的时候，要明确告诉接收方要发送多大的数据，以便接收方能够准确接收到所有的数据
# 4、多用在文件传输的过程中
    # 大文件的传输一定是按照字节读，每一次读固定的字节
    # 传输的过程中客户端一边读一边传，接收端一边收一边写
    # send这个大文件之前，35672，每次send是35672-4096，直到小于4096直接读
    # recv每次可以接受任意大小字节，不会丢失，直到小于接收设置的值

# 不好处 ：多了一次交互