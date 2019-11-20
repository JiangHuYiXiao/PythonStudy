# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/19 8:47
# @Software       : Python_study
# @Python_verison : 3.7

# 1、线程锁只是对线程上锁了，没有对数据进行加锁，特殊情况当时间片轮转时候会存在一个数据被两个线程操作，是不安全的
# 2、针对这样的情况，我们需要在给数据进行加锁处理，保证安全
# 3、join是所有的线程等待，lock是部分线程等待，也就是你加锁的那段代码中的数据等待

# 1、不加锁
from threading import Thread
import time
n = 100
def func():
    global n
    temp = n
    time.sleep(0.01)            # 不设置等待，结果一定为0，设置等待，如果刚好时间片轮转到这，那么结果可能就是其他的100,99等，这样就需要对数据进行加锁
    n = temp - 1

for i in range(100):
    t = Thread(target=func)
    t.start()
print(n)



# 2、加锁处理

from threading import Thread
import time
from threading import Lock
n = 100
lock = Lock()
t_lst = []
def func():
    global n
    lock.acquire()
    temp = n
    time.sleep(0.01)            # 不设置等待，结果一定为0，设置等待，如果刚好时间片轮转到这，那么结果可能就是其他的100,99等，这样就需要对数据进行加锁
    n = temp - 1
    lock.release()

for i in range(100):

    t = Thread(target=func)
    t_lst.append(t)
    t.start()
[t.join() for t in t_lst]
print(n)                # 结果为0，一定