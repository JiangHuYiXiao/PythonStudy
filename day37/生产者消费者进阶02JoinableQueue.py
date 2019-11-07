# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/7 10:24
# @Software       : Python_study
# @Python_verison : 3.7
from multiprocessing import Process
from multiprocessing import JoinableQueue
import time
import random

def producter(Q,food):
    for i in range(5):
        Q.put('%s-%s'%(food,i))
        print('生产了%s-%s'%(food,i))
        time.sleep(random.randint(1,2))         # 等待一下模拟生产慢
        Q.join()                            # 等待消费者把所有的数据处理完，等生产者放进去的数据都执行了taskdone后结束，PUT了多少数据，就有多少taskdone

def consumter(Q,name):
    while True:
        food = Q.get()
        print('%s吃了-%s'%(name,food))
        Q.task_done()

if __name__ == '__main__':
    Q = JoinableQueue()

    p1 = Process(target=producter,args=(Q,'泔水'))
    p1.start()
    p2 = Process(target=producter,args=(Q,'骨头'))           # 生产慢，消费快则增加生产者
    p2.start()
    c1 = Process(target=consumter,args=(Q,'猪'))
    c1.daemon = True
    c1.start()
    c2 = Process(target=consumter,args=(Q,'狗'))
    c2.daemon = True
    c2.start()
    c3 = Process(target=consumter,args=(Q,'猫'))
    c3.daemon = True
    c3.start()
    p1.join()           # 等待p1执行完毕
    p2.join()           # 等待p2执行完毕