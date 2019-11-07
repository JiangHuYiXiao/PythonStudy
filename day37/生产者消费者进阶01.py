# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/6 20:39
# @Software       : Python_study
# @Python_verison : 3.7
# 存在一个矛盾的现象：数据的供需不平衡
# 刚开始：同步处理，生产数据，使用数据
# 而后：异步处理，主进程生产数据、子进程使用数据----多进程
# 后面：异步处理，子进程生产数据、子进程使用数据----生产模型

# 3个子进程生产泔水，2个子进程吃泔水
# 生产的快，吃的慢，泔水溢出
# 生产的慢，吃的慢，泔水不够     如果增加生产者----让生产变快
# 生产快，消费慢，首先应该是减少生产者（找一个容器放，约束容器的容量），这个容器就是队列，然后增加消费者


# 1、生产慢，消费快，增加生产者后，导致后面的吃不完
# from multiprocessing import Process
# from multiprocessing import Queue
# import time
# import random
#
# def producter(Q,food):
#     for i in range(10):
#         Q.put('%s-%s'%(food,i))
#         print('生产了%s-%s'%(food,i))
#         time.sleep(random.randint(1,2))         # 等待一下模拟生产慢
# def consumter(Q,name):
#     for i in range(10):
#         food = Q.get()
#         # time.sleep(1)
#         print('%s吃了-%s'%(name,food))
#
# if __name__ == '__main__':
#     Q = Queue()
#     p1 = Process(target=producter,args=(Q,'泔水'))
#     p1.start()
#     p2 = Process(target=producter,args=(Q,'骨头'))           # 生产慢，消费快则增加生产者
#     p2.start()
#     c1 = Process(target=consumter,args=(Q,'猪'))
#     # c1.daemon = True
#     c1.start()
#     # c2 = Process(target=consumter,args=(Q,'泔水','狗'))
#     # # c2.daemon = True
#     # c2.start()

# 2、生产慢，消费快，增加生产者后，消费者一直吃
# from multiprocessing import Process
# from multiprocessing import Queue
# import time
# import random
#
# def producter(Q,food):
#     for i in range(10):
#         Q.put('%s-%s'%(food,i))
#         print('生产了%s-%s'%(food,i))
#         time.sleep(random.randint(1,2))         # 等待一下模拟生产慢
# def consumter(Q,name):
#     while True:
#         food = Q.get()
#         # time.sleep(1)
#         print('%s吃了-%s'%(name,food))
#
# if __name__ == '__main__':
#     Q = Queue()
#     p1 = Process(target=producter,args=(Q,'泔水'))
#     p1.start()
#     p2 = Process(target=producter,args=(Q,'骨头'))           # 生产慢，消费快则增加生产者
#     p2.start()
#     c1 = Process(target=consumter,args=(Q,'猪'))
#     # c1.daemon = True
#     c1.start()
    # c2 = Process(target=consumter,args=(Q,'泔水','狗'))
    # # c2.daemon = True
    # c2.start()

# 3、生产慢，消费快，增加生产者后，消费者一直吃后，在生产者中发送一个信号None
# from multiprocessing import Process
# from multiprocessing import Queue
# import time
# import random
#
# def producter(Q,food):
#     for i in range(5):
#         Q.put('%s-%s'%(food,i))
#         print('生产了%s-%s'%(food,i))
#         time.sleep(random.randint(1,2))         # 等待一下模拟生产慢
#     Q.put(None)
# def consumter(Q,name):
#     while True:
#         food = Q.get()
#         if food == None:
#             break
#         # time.sleep(1)
#         print('%s吃了-%s'%(name,food))
#
# if __name__ == '__main__':
#     Q = Queue()
#     p1 = Process(target=producter,args=(Q,'泔水'))
#     p1.start()
#     p2 = Process(target=producter,args=(Q,'骨头'))           # 生产慢，消费快则增加生产者
#     p2.start()
#     c1 = Process(target=consumter,args=(Q,'猪'))
#     # c1.daemon = True
#     c1.start()
#     # c2 = Process(target=consumter,args=(Q,'泔水','狗'))
#     # # c2.daemon = True
#     # c2.start()

# 4、再增加几个消费者
# from multiprocessing import Process
# from multiprocessing import Queue
# import time
# import random
#
# def producter(Q,food):
#     for i in range(5):
#         Q.put('%s-%s'%(food,i))
#         print('生产了%s-%s'%(food,i))
#         time.sleep(random.randint(1,2))         # 等待一下模拟生产慢
#     Q.put(None)
# def consumter(Q,name):
#     while True:
#         food = Q.get()
#         if food == None:
#             break
#         # time.sleep(1)
#         print('%s吃了-%s'%(name,food))
#
# if __name__ == '__main__':
#     Q = Queue()
#     p1 = Process(target=producter,args=(Q,'泔水'))
#     p1.start()
#     p2 = Process(target=producter,args=(Q,'骨头'))           # 生产慢，消费快则增加生产者
#     p2.start()
#     c1 = Process(target=consumter,args=(Q,'猪'))
#     # c1.daemon = True
#     c1.start()
#     c2 = Process(target=consumter,args=(Q,'狗'))
#     # # c2.daemon = True
#     c2.start()
#     c3 = Process(target=consumter,args=(Q,'猫'))
#     # # c2.daemon = True
#     c3.start()
#
# # 结论：
# # 队列中内置了一把锁，所以多个消费者永远不会对一个数据进程操作
# # 因为只发了一个None所以程序又卡住了，只有一个consumer接收到了

# 5、增加几个None，程序正常运行和结束
from multiprocessing import Process
from multiprocessing import Queue
import time
import random

def producter(Q,food):
    for i in range(5):
        Q.put('%s-%s'%(food,i))
        print('生产了%s-%s'%(food,i))
        time.sleep(random.randint(1,2))         # 等待一下模拟生产慢
    Q.put(None)
    Q.put(None)
    Q.put(None)
def consumter(Q,name):
    while True:
        food = Q.get()
        if food == None:
            break
        # time.sleep(1)
        print('%s吃了-%s'%(name,food))

if __name__ == '__main__':
    Q = Queue()
    p1 = Process(target=producter,args=(Q,'泔水'))
    p1.start()
    p2 = Process(target=producter,args=(Q,'骨头'))           # 生产慢，消费快则增加生产者
    p2.start()
    c1 = Process(target=consumter,args=(Q,'猪'))
    # c1.daemon = True
    c1.start()
    c2 = Process(target=consumter,args=(Q,'狗'))
    # # c2.daemon = True
    c2.start()
    c3 = Process(target=consumter,args=(Q,'猫'))
    # # c2.daemon = True
    c3.start()




# 概述生产者消费者模型：
# 1、消费者不知道生产者能够生产多少数据
# 2、所以只能通过while True循环，进行循环消费
# 3、但是消费者不知道生产者什么时候生产完成，所以，需要生产者发送信号给消费者（进程之间的通信）
# 4、有多少消费者就要发送多少None
# 5、针对于队列Queue，目前只能写到这里，后面的处理生产者消费者模型，需要使用JoinableQueue队列

