# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/13 10:41
# @Software       : PythonStudy
# @Python_verison : 3.7
# UDP（User Datagram Protocol）不可靠的、无连接的服务，传输效率高（发送前时延小），
# 一对一、一对多、多对一、多对多、面向报文，尽最大努力服务，无拥塞控制。
# 使用UDP的应用：域名系统 (DNS)；视频流；IP语音(VoIP)。
'''
需求：
提供服务、接收客户端的时间格式，然后将服务器的时间按照客户端传的格式返回给客户端
'''
import socket
import time
ss = socket.socket(type=socket.SOCK_DGRAM)
ss.bind(('127.0.0.1',9977))

# 接收
time_format,addr = ss.recvfrom(1024)

# 时间转换
timestamp = time.time()
struct_time = time.localtime(timestamp)
result = time.strftime(time_format.decode('utf-8'),struct_time)

# 返回
ss.sendto(result.encode('utf-8'),addr)
ss.close()