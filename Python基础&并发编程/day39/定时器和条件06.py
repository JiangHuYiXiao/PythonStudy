# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/20 16:27
# @Software       : Python_study
# @Python_verison : 3.7

# 1、定时器，定时开启一个线程，执行任务
from threading import Timer
def func():
    print('func函数')

tim = Timer(2,func)         # 第一个参数为等待的时间,单位为秒，第二个参数为函数名
tim.start()


# 2、只开启一个线程，线程一直在，每隔一段时间执行函数func,都是同一个线程，sleep短时间在线程内while True
from threading import Thread
import time
import os
def func():
    while True:
        time.sleep(1)
        print('hello world',os.getpid())            # 线程id一样
th = Thread(target=func)
th.start()


# 3、开启一个线程，每隔一段时间开启一个线程，sleep长时间在线程外while True
from threading import Timer
import time
import os
def func():
    print('hello world',os.getpid())            # 线程id一样

while True:
    ti = Timer(10,func)
    ti.start()


# 4、条件
import threading

def run(i):

    con.acquire()
    con.wait()  # 等钥匙
    print('run the thread %s' % i)
    con.release()

if __name__ == '__main__':
    con = threading.Condition()         # 条件 = 锁 + wait的功能
    for i in range(10):
        threading.Thread(target=run, args=(i,)).start()
    while True:
        num = int(input('>>>'))
        if num == 'q':
            break
        con.acquire()           # condition中的锁是递归锁
        con.notify(num)  # 传递信号，num等于多少就可以放行多少个线程，只能传int
        con.release()
        print('***')