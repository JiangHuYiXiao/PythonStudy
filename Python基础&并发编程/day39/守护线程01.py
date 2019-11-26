# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/19 8:23
# @Software       : Python_study
# @Python_verison : 3.7

# 1、正常主线程会等待子线程的结束，如果没有设置守护线程
from threading import Thread
import time
import os
def func():
    print('子线程开始执行',os.getpid())
    time.sleep(1)
    print('子线程结束执行',os.getpid())

print('主线程执行开始',os.getpid())
t1 = Thread(target=func)
t1.start()
print('主线程执行结束',os.getpid())            # 执行完成这个会等待子线程输出，


# 2、主线程不会等待子线程的结束，如果有设置守护线程
from threading import Thread
import time
import os
def func():
    print('子线程开始执行',os.getpid())
    time.sleep(1)
    print('子线程结束执行',os.getpid())            # 不会执行

print('主线程执行开始',os.getpid())

t1 = Thread(target=func)
t1.setDaemon(True)          # 设置守护线程
t1.start()

print('主线程执行结束',os.getpid())            # 执行完成这个不会等待子线程输出，


# 3、主线程会等待子线程的结束，如果有设置守护线程且设置了join
from threading import Thread
import time
import os
def func():
    print('子线程开始执行',os.getpid())
    time.sleep(1)
    print('子线程结束执行',os.getpid())            # 会执行

print('主线程执行开始',os.getpid())

t1 = Thread(target=func)
t1.setDaemon(True)          # 设置守护线程
t1.start()
t1.join()
print('主线程执行结束',os.getpid())            # 执行完成这个不会等待子线程输出，