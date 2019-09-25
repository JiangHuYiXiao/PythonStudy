# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/24 19:33
# @Software       : Python_study
# @Python_verison : 3.7

# 1、为什么会有黏包问题：
    # 首先，只有TCP协议才有黏包现象，因为TCP是面向流的协议。
    # 其次，在数据传输的过程中存在缓存机制来避免数据丢失，因此在连续多次发送小数据以及接收大小不符的情况下容易出现黏包现象。
    # 本质还是因为，接收端不知道发送过来的数据的大小。

# 2、如何解决黏包问题：
# 在传输数据时候先告诉接收端，需要先发送数据大小。
# 使用struct模块解决

# 3、struct模块
import struct
# struct.pack('i',num)  返回4个字节的长度，
# struct.unpack('i',num)     返回一个元组，元组第一个元素就是文件的大小
