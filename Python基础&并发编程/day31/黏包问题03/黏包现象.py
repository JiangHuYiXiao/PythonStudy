# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/13 14:43
# @Software       : PythonStudy
# @Python_verison : 3.7

# 1、通过os模块来使用系统命令
# import os
# os.system('dir')
# ret = os.popen('dir').read()     # 需要打印，有返回值，能对结果进行
# print(ret)

import subprocess
# 2、通过subprocess模块来使用系统命令
res = subprocess.Popen('dir',shell= True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
print('stdout:',res.stdout.read().decode('gbk'))
print('stderr:',res.stderr.read().decode('gbk'))

# 3、黏包现象：同时执行多条命令之后，得到的结果很可能只有一部分，在执行其他命令的时候又接收到之前执行的另外一部分结果，这种显现就是黏包。

# 4、黏包成因
# TCP协议中的数据传递：
# 当发送端缓冲区的长度大于网卡的MTU时，tcp会将这次发送的数据拆成几个数据包发送出去。
# MTU是Maximum Transmission Unit的缩写。意思是网络上传送的最大数据包。MTU的单位是字节。 大部分网络设备的MTU都是1500。
# 如果本机的MTU比网关的MTU大，大的数据包就会被拆开来传送，这样会产生很多数据包碎片，增加丢包率，降低网络速度。
# 面向流的通信特点和Nagle算法：
# TCP（transport control protocol，传输控制协议）是面向连接的，面向流的，提供高可靠性服务。
# 收发两端（客户端和服务器端）都要有一一成对的socket，因此，发送端为了将多个发往接收端的包，更有效的发到对方，使用了优化方法（Nagle算法），
# 将多次间隔较小且数据量小的数据，合并成一个大的数据块，然后进行封包。
# 这样，接收端，就难于分辨出来了，必须提供科学的拆包机制。 即面向流的通信是无消息保护边界的。
# 对于空消息：tcp是基于数据流的，于是收发的消息不能为空，这就需要在客户端和服务端都添加空消息的处理机制，防止程序卡住，而udp是基于数据报的，即便是你输入的是空内容（直接回车），
# 也可以被发送，udp协议会帮你封装上消息头发送过去。
# 可靠黏包的tcp协议：tcp的协议数据不会丢，没有收完包，下次接收，会继续上次继续接收，己端总是在收到ack时才会清除缓冲区内容。数据是可靠的，但是会粘包。

# 5、UDP不会发生黏包
# UDP（user datagram protocol，用户数据报协议）是无连接的，面向消息的，提供高效率服务。
# 不会使用块的合并优化算法，, 由于UDP支持的是一对多的模式，所以接收端的skbuff(套接字缓冲区）采用了链式结构来记录每一个到达的UDP包，
# 在每个UDP包中就有了消息头（消息来源地址，端口等信息），这样，对于接收端来说，就容易进行区分处理了。 即面向消息的通信是有消息保护边界的。
# 对于空消息：tcp是基于数据流的，于是收发的消息不能为空，这就需要在客户端和服务端都添加空消息的处理机制，防止程序卡住，而udp是基于数据报的，
# 即便是你输入的是空内容（直接回车），也可以被发送，udp协议会帮你封装上消息头发送过去。
# 不可靠不黏包的udp协议：udp的recvfrom是阻塞的，一个recvfrom(x)必须对唯一一个sendinto(y),收完了x个字节的数据就算完成,若是y;x数据就丢失，这意味着udp根本不会粘包，但是会丢数据，不可靠。
# 用UDP协议发送时，用sendto函数最大能发送数据的长度为：65535- IP头(20) – UDP头(8)＝65507字节。用sendto函数发送数据时，如果发送数据长度大于该值，则函数会返回错误。（丢弃这个包，不进行发送）
# 用TCP协议发送时，由于TCP是数据流协议，因此不存在包大小的限制（暂不考虑缓冲区的大小），这是指在用send函数时，数据长度参数不受限制。
# 而实际上，所指定的这段数据并不一定会一次性发送出去，如果这段数据比较长，
# 会被分段发送，如果比较短，可能会等待和下一次数据一起发送。

# 6、总结
# 黏包现象只发生在tcp协议中：
# 1.从表面上看，黏包问题主要是因为发送方和接收方的缓存机制、tcp协议面向流通信的特点。
# 2.实际上，主要还是因为接收方不知道消息之间的界限，不知道一次性提取多少字节的数据所造成的

