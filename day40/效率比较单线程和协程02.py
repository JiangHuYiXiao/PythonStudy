# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/22 16:30
# @Software       : Python_study
# @Python_verison : 3.7
from gevent import monkey;monkey.patch_all()        # 为了让gevent可以识别time模块的IO
import time
import os

import gevent           # 不仅可以切换任务，还可以规避IO
# 单线程
def task(args):
    time.sleep(1)
    print(args,os.getpid())

def sync_func():            # 同步
    for i in range(10):
        task(i)

def async_func():           # 异步
    g_l = []
    for i in range(10):
        t = gevent.spawn(task,i)            # 给协程任务传参数
        g_l.append(t)
    gevent.joinall(g_l)         # 批量等待

start_time = time.time()
sync_func()
print(time.time()-start_time)           # 10.005990982055664


start_time = time.time()
async_func()
print(time.time()-start_time)           # 0.9992973804473877  协程快的多


