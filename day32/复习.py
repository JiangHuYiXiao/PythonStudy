# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/17 14:21
# @Software       : PythonStudy
# @Python_verison : 3.7
# 网络层协议：IP
# 传输层：TCP、UDP协议
# 数据链路层协议：ARP协议
# 应用层协议：HTTP（https）协议，FTP协议，SMTP协议


#黏包现象：
# 只有tcp才有，udp是没有黏包现象的。
# 多个send 小的数据连在一起，会产生黏包现象，是tcp协议内部的优化算法和接收端的缓存机制引起。

# 引起黏包的情况有：
# 1、连续send两个小数据
# 2、两个recv，第一个recv接收的比较小
# 本质都是因为你不知道到底要接收多大的数据长度、