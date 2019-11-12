# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/7 17:01
# @Software       : Python_study
# @Python_verison : 3.7
from multiprocessing import Manager
# 管道通信目前学习到了可以使用：
# Pipe   管道 双向通信 数据不安全
# Queue     队列 双向通信 数据安全
# JoinableQueue     put 和get的一个计数机制，每次get数据之后task_done，put端接收的计数-1，直到计数为0
# 进程间数据是独立的，可以借助于队列或管道实现通信，二者都是基于消息传递的
# 虽然进程间数据独立，但可以通过Manager实现数据共享，事实上Manager的功能远不止于此
# Manager()提供了各种数据类型的共享
# 展望未来，基于消息传递的并发编程是大势所趋
# 即便是使用线程，推荐做法也是将程序设计为大量独立的线程集合，通过消息队列交换数据。
# 这样极大地减少了对使用锁定和其他同步手段的需求，还可以扩展到分布式系统中。
# 但进程间应该尽量避免通信，即便需要通信，也应该选择进程安全的工具来避免加锁带来的问题。
# 以后我们会尝试使用数据库来解决现在进程之间的数据共享问题。
from multiprocessing import Manager
from multiprocessing import Process
from multiprocessing import Lock
import time

# 1、使用Manager创建字典、列表等
# if __name__ == '__main__':
#     m = Manager()           # 创建Manager对象
#     d = m.list()            # 使用对象.数据类型创建列表
#     d1 = m.dict()           # 使用对象.数据类型创建字典
#     print(d,d1)             # [] {}
#     d1['count'] = 0        # 添加键值对
#     print(d1)               # {'count': 0}

# 2、进程之间数据没有共享
# def func(d):
#     # time.sleep(3)
#     # d['count'] -= 1
#     print(d)
#
# if __name__ == '__main__':
#     # m =Manager()
#     # d = m.dict()
#     # d['count'] = 100
#     d = {}
#     for i in range(100):
#         p1 = Process(target=func, args=(d,))
#         p1.start()
#         d['count'] = 0
#         # p1.join()

# 3、进程之间数据共享
# def func(d):
#     d['count'] -= 1
#     print(d)
#
# if __name__ == '__main__':
#     m =Manager()
#     d = m.dict()
#     d['count'] = 100
#     for i in range(100):
#         p1 = Process(target=func, args=(d,))
#         p1.start()
#         p1.join()


# 4、等待所有的进程结束，应该结果为0，现在结果为不确定，使用Lock，所以我们一般不用Manager、Pipe因为他们不安全，我们以后使用Queue，JoinableQueue
# def func(d):
#     d['count'] -= 1
#     # print(d)
#
# if __name__ == '__main__':
#     m =Manager()
#     d = m.dict()
#     d['count'] = 100
#     l = []          # 建立一个空列表，为了后面统一join
#     for i in range(100):
#         p1 = Process(target=func, args=(d,))
#         p1.start()
#         l.append(p1)        #把所有的进程都添加到空列表中
#     [p1.join() for p1 in l]     # 等待所有的进程结束
#     print(d)            # 最终输出的结果不确定，{'count': 1}或者{'count': 0}


# 5、使用加锁，这样保证最终结果为0
def func(d,lock):
    lock.acquire()
    d['count'] -= 1
    lock.release()
    # print(d)

if __name__ == '__main__':
    m =Manager()
    lock = Lock()
    d = m.dict()
    d['count'] = 100
    l = []          # 建立一个空列表，为了后面统一join
    for i in range(100):
        p1 = Process(target=func, args=(d,lock))
        p1.start()
        l.append(p1)        #把所有的进程都添加到空列表中
    [p1.join() for p1 in l]     # 等待所有的进程结束
    print(d)            # 最终输出的结果{'count': 0}