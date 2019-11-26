# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/20 8:40
# @Software       : Python_study
# @Python_verison : 3.7

# 1、经典的死锁问题：科学家吃面问题
# 吃面要筷子和面，有两个人去吃，筷子和面分别只有一个，
from threading import Thread
from threading import Lock
import time

def eat1(name):
    kz.acquire()
    print('%s拿筷子'%(name))
    m.acquire()
    print('%s拿面了'%(name))
    print('%s吃面'%(name))
    m.release()
    kz.release()

def eat2(name):
    m.acquire()
    print('%s拿面了'%(name))
    time.sleep(1)           # 等面，设置后才会有死锁的问题
    kz.acquire()
    print('%s拿筷子'%(name))
    print('%s吃面'%(name))
    kz.release()
    m.release()

kz = Lock()
m = Lock()
t1 = Thread(target=eat1,args=('江湖',))
t1.start()
t2 = Thread(target=eat2,args=('一休',))
t2.start()
t3 = Thread(target=eat1,args=('大头',))
t3.start()
t4 = Thread(target=eat2,args=('小妖',))
t4.start()
# 出现了这样的情况：一个人拿到了筷子一个人拿到了面，两个人都不释放，这样就程序永远都运行不下去了。
# 江湖拿筷子
# 江湖拿面了
# 江湖吃面
# 一休拿面了
# 大头拿筷子



# 2、解决这个死锁问题，我们就需要学习递归锁RLock
# 递归锁是允许多次acquire，但是它的本质只有一把锁，你拿了筷子的锁，那么就别人拿走不了面的锁
# 只有等你把锁释放后才可以,且释放锁的时候必须从里面开始释放，意思就是你后面拿的要先释放
from threading import Thread
from threading import RLock
import time

def eat1(name):
    kz.acquire()
    print('%s拿筷子'%(name))
    m.acquire()
    print('%s拿面了'%(name))
    print('%s吃面'%(name))
    m.release()
    kz.release()

def eat2(name):
    m.acquire()
    print('%s拿面了'%(name))
    time.sleep(1)           # 等面，设置后才会有死锁的问题
    kz.acquire()
    print('%s拿筷子'%(name))
    print('%s吃面'%(name))
    kz.release()
    m.release()

kz = m =  RLock()           # 同一把锁，之前互斥锁是两把，为了不死锁，因为一个互斥锁不能同时多次acquire，多次acquire就会死锁

t1 = Thread(target=eat1,args=('江湖',))
t1.start()
t2 = Thread(target=eat2,args=('一休',))
t2.start()
t3 = Thread(target=eat1,args=('大头',))
t3.start()
t4 = Thread(target=eat2,args=('小妖',))
t4.start()
'''
江湖拿筷子
江湖拿面了
江湖吃面
一休拿面了
一休拿筷子
一休吃面
大头拿筷子
大头拿面了
大头吃面
小妖拿面了
小妖拿筷子
小妖吃面
'''