# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/5 15:19
# @Software       : Python_study
# @Python_verison : 3.7
# 信号量的本质是锁，只是这个锁可以多个进程使用

# 如果不释放则后面的进程永远无法执行
# from multiprocessing import Semaphore
# from multiprocessing import Lock
# from multiprocessing import Process
# se = Semaphore(3)
# se.acquire()
# print('进来一个')
# se.acquire()
# print('进来一个')
# se.acquire()
# print('进来一个')
# se.acquire()
# print('进来一个')

# 信号量的应用实例：迷你唱吧，每个小唱吧最多支持4个人同时进入
from multiprocessing import Process
from multiprocessing import Semaphore
import time
import random
def sing(i,se):
    se.acquire()
    print('%s 进入ktv'%i)
    time.sleep(random.randint(1,10))
    print('%s 离开ktv'%i)
    se.release()

if __name__ == '__main__':
    se = Semaphore(4)
    for i in range(20):
        p = Process(target=sing,args=(i,se))
        p.start()


