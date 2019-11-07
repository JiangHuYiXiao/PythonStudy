# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/7 17:01
# @Software       : Python_study
# @Python_verison : 3.7
from multiprocessing import Manager
# 管道通信目前学习到了可以使用：
# Pipe   管道 双向通信 数据不安全
# Queue     队列 双向通信 数据安全
# JoinableQueue     put 和get的一个计数机制，每次get数据之后task_done，put端接收的计数-1，直到计数为0