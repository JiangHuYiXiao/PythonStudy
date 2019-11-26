# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/20 19:04
# @Software       : Python_study
# @Python_verison : 3.7

# 线程池和进程池是用来操作池的，最近新的模块，之前没有
# 开启线程需要成本，但是成本比开启进程低，
# 高IO的情况下开多线程，
'''
# 1、submit(函数名，参数)   合并了创建线程和start线程
from concurrent import futures
def func(args):
    print(args)


# futures.ProcessPoolExecutor         # 进程池  开的个数默认开cpu的核数+1
thread_pool = futures.ThreadPoolExecutor(5)          # 线程池，开的个数默认开cpu的核数*5
thread_pool.submit(func,200)   # 合并了创建线程和start线程

# 2、submit+for循环
from concurrent import futures
import time
import random
def func(args):
    print(args)
    time.sleep(random.randint(1,3))

thread_pool = futures.ThreadPoolExecutor(5)          # 线程池，开的个数默认开cpu的核数*5
for i in  range(10):
    thread_pool.submit(func,i)   # 合并了创建线程和start线程


# 3、result()拿结果
from concurrent import futures
import time
import random
def func(args):
    print(args)
    time.sleep(random.randint(1,3))
    return '*'*args
f_lst = []
thread_pool = futures.ThreadPoolExecutor(5)          # 线程池，开的个数默认开cpu的核数*5
for i in  range(10):
    f =thread_pool.submit(func,i)   # 合并了创建线程和start线程
    # print(f.result())               # 同步的
    f_lst.append(f)
[print(i.result()) for i in f_lst]              # 异步的

# 4、shutdown  合并了close和join
from concurrent import futures
import time
import random
def func(args):
    print(args)
    time.sleep(random.randint(1,3))
    return '*'*args
f_lst = []
thread_pool = futures.ThreadPoolExecutor(5)          # 线程池，开的个数默认开cpu的核数*5
for i in  range(10):
    f =thread_pool.submit(func,i)   # 合并了创建线程和start线程
    # print(f.result())               # 同步的
    f_lst.append(f)
thread_pool.shutdown()
for f in f_lst:
    print(f.result())

# 5、map
from concurrent import futures
def func(args):
    print(args)


# futures.ProcessPoolExecutor         # 进程池  开的个数默认开cpu的核数+1
thread_pool = futures.ThreadPoolExecutor(5)          # 线程池，开的个数默认开cpu的核数*5
thread_pool.map(func,range(10))   # 线程的map不支持返回值，天生异步 接收可迭代的对象
'''
# 6、回调函数add_done_callback(函数名)
from concurrent import futures
def func(n):
    print(n)
    return '*'*n

def call(args):
    print(args.result())

# futures.ProcessPoolExecutor         # 进程池  开的个数默认开cpu的核数+1
thread_pool = futures.ThreadPoolExecutor(5)          # 线程池，开的个数默认开cpu的核数*5
thread_pool.submit(func,1).add_done_callback(call)   # 写函数名