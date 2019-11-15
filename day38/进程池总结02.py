# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/15 8:20
# @Software       : Python_study
# @Python_verison : 3.7
# 1、概念：
    # 进程是操作系统资源分配和调度的最小单元，是操作系统中运行程序的抽象。
# 2、进程的调度：
    # 2.1由操作系统来完成
    # 2.2进程调度的法则：
        # 1.先来先服务法
        # 2.时间片轮转法
        # 3.短作业优先法
        # 4.多级反馈法
# 3、进程的同步和异步:
    # 同步：调度之后还一定要等到结果
    # 异步：只管调度，不管结果

# 4、进程的状态：（就绪、运行、阻塞）
    # 首先是进程的【创建】--‘提交’->【就绪】---进程的调度，时间片到了就【运行】---如果遇到阻塞的事件---【阻塞】---阻塞完成后继续是【就绪】状态
    # 或者运行时没有阻塞就完成【退出】
    # 阻塞的情况有recv、sleep、input、accept

# 5、多进程
# def func():
#     pass
# from multiprocessing import Process
# p1 = Process(target=func,args=(args1,))       # 创建进程,args,必须传元组
# p1.start()              # 启动进程
# p1.join()               # 会阻塞主进程，等待子进程结束后再去执行主进程剩下的代码

# 6、守护进程：在p.start()之前设置p.daemon = True
# 会随着主进程的结束而结束，不会像正常的主进程一样等待子进程
# import os
# from multiprocessing import Process
# def func1():
#     print('func1')
#     print('子进程2pid：',os.getpid())
#     print('子进程2的父进程pid：',os.getppid())
# def func():
#     p1 = Process(target=func1)
#     p1.start()
#     print('func')
#     print('子进程1pid：',os.getpid())
#     print('子进程1的父进程pid：',os.getppid())
# if __name__ == '__main__':
#     P =Process(target=func)
#     P.daemon = True     # 不设置守护进程可以正常全部执行，设置守护进程则不会执行子进程的代码
#     P.start()
#     print('主进程pid：',os.getpid())


# import os
# from multiprocessing import Process
# import time
# def func1():
#     print('func1')
#     print('子进程2pid：', os.getpid())
#     print('子进程2的父进程pid：', os.getppid())
#     time.sleep(5)
#     print('*****')
#
# def func():
#     print('func')
#     print('子进程1pid：', os.getpid())
#     print('子进程1的父进程pid：', os.getppid())
#
# if __name__ == '__main__':
#     p1 = Process(target=func)
#     p1.daemon = True                # 因为p1设置为了主进程，所以不会等待func函数的代码执行，而是直接往后执行主进程的代码，进而执行p2
#     p1.start()
#     print('主进程pid：', os.getpid())
#     p2 = Process(target=func1)
#     p2.start()
#     # p1.join()           #如果，添加join就会等待所有的子进程


# 7、进程锁，是为了保证数据安全，使原来异步的变成同步，牺牲效率保证数据安全
# from multiprocessing import Lock
# from multiprocessing import Process
# def func():
#     lock = Lock()
#     lock.acquire()
#     print('解锁')
#     lock.release()        # 释放锁，不释放的话就阻塞了
#
#     lock.acquire()      # 上锁
#     print('没锁住')
#
#
# if __name__ == '__main__':
#     p1 = Process(target=func)
#     p1.start()

# 8、信号量，本质就是锁，只是这个锁可以多个进程使用
# from multiprocessing import Semaphore
# from multiprocessing import Process
# from multiprocessing import Lock
# se = Semaphore(3)           # 设置信号数量，表示最多只有三把锁
# se.acquire()
# print('1')
# se.acquire()
# print('2')
# se.acquire()
# print('3')
# se.acquire()
# print('4')              # 阻塞，打印不出来，因为只有三把锁，

# 9、进程事件
from multiprocessing import Event
# 1、事件---实际就是阻塞，是异步阻塞，同时阻塞多个进程，标志，同时使所有的进程都陷入阻塞，可以同时恢复
# 锁、信号量也是同时阻塞多个进程，也是异步的。
# from multiprocessing import Event
# e = Event()         # 创建一个事件对象
# e.set()             # 非阻塞信号
# e.clear()           # 阻塞信号
# print(e.is_set())           # False表示阻塞，True表示非阻塞
# e.wait()            # 默认为阻塞信号


# 10、队列：可以实现主进程和子进程的通信以及进程之前的通信，是目前我们学到的最安全常用的ipc通信机制
# 队列本身是有锁的，不会存在多个进程同时操作一个数据

# from multiprocessing import Queue
# q = Queue()           # 不限制队列的长度
# q = Queue(3)           # 限制队列的长度为3

# q.put(1)           # 添加数
# q.put('群雄逐鹿')           # 添加数
# print(q.get())          # 取数
# print(q.get())          # 取数
# print(q.qsize())            # qsize()     # 查询队列大小


# 11、生产者消费者模型
# 生产慢，则先增加生产者，减少消费者
# 消费慢，则先增加消费者，减少生产者
# 概述生产者消费者模型：
# 1、消费者不知道生产者能够生产多少数据
# 2、所以只能通过while True循环，进行循环消费
# 3、但是消费者不知道生产者什么时候生产完成，所以，需要生产者发送信号给消费者（进程之间的通信）
# 4、有多少消费者就要发送多少None
# 5、针对于队列Queue，目前只能写到这里，后面的处理生产者消费者模型，需要使用JoinableQueue队列
# from multiprocessing import Process
# from multiprocessing import Queue
# import time
# import random
# def producter(q,name,product):
#     for i in range(10):
#         q.put('%s-%s'%(product,i))
#         print('%s生产了%s-%s'%(name,product,i))
#         time.sleep(random.random())         # 模拟生产慢
#     q.put(None)
#     q.put(None)
#
# def consumer(q,consume):
#     while True:
#         food = q.get()
#         if food == None:
#             break
#         else:
#             print('%s吃了-%s'%(consume,food))
#
# if __name__ == '__main__':
#     q = Queue()
#     pr1 = Process(target=producter,args=(q,'大厨','红烧肉'))
#     pr1.start()
#     pr2 = Process(target=producter,args=(q,'大妈','包子'))          # 增加生产者
#     pr2.start()
#
#     co2 = Process(target=consumer,args=(q,'吃货2'))
#     co2.start()
#     co1 = Process(target=consumer,args=(q,'吃货1'))
#     co1.start()

# 12、生产者消费者模型，使用JoinableQueue来解决
# 需要设置消费者为守护进程，每次消费后发送task_done，在生产者里面设置join等待消费者把生产者生产的数据都处理完成执行了task_done