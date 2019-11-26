# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/5 9:22
# @Software       : Python_study
# @Python_verison : 3.7
# 锁是为了保证数据安全，使原来异步的程序转换为同步，牺牲效率保证安全
# acquire 需要锁
# release 释放锁
# 并发编程包含（多进程、多线程）
# import time
# from multiprocessing import Lock
# from multiprocessing import Process
# def func():
#     lock = Lock()
#     lock.acquire()
#     lock.acquire()          # 阻塞，因为要等到一个锁释放才能继续执行
#     lock.release()
#     print('func')          # 不执行
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.start()

# 锁的应用实例，抢票
from multiprocessing import Process
from multiprocessing import Lock
import json
import time
import random
# 查找余票方法
def search(i):
    with open(r'F:\Python_study\day36\ticket',mode = 'r',encoding='utf-8')as file:
        res = json.load(file)
        print(i,res['ticket'])

# # 买票的方法
def get(i):
    with open(r'F:\Python_study\day36\ticket', mode='r', encoding='utf-8')as file:
        ticket_num = json.load(file)['ticket']
    time.sleep(random.random())
    if ticket_num > 0:
        with open(r'F:\Python_study\day36\ticket', mode='w', encoding='utf-8')as file:
            json.dump({'ticket':ticket_num-1},file)
        print('%s已经抢到票了' % (i))
    else:
        print('%s没有票了'%(i))

def task(i,lock):
    search(i)
    lock.acquire()
    get(i)
    lock.release()
if __name__ == '__main__':
    lock = Lock()
    for i in range(20):
        p1 = Process(target=task,args=(i,lock))
        p1.start()