# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/6 8:32
# @Software       : Python_study
# @Python_verison : 3.7

# 1、事件---实际就是阻塞，是异步阻塞，同时阻塞多个进程，标志，同时使所有的进程都陷入阻塞，可以同时恢复
# 锁、信号量也是同时阻塞多个进程，也是异步的。
#
# from multiprocessing import Event
# e = Event()         # 创建一个事件对象
# e.set()             # 非阻塞信号
# e.clear()           # 阻塞信号
# print(e.is_set())           # False表示阻塞，True表示非阻塞
# e.wait()            # 默认为阻塞信号

# 2、事件应用实例：红绿灯
'''
from multiprocessing import Event
from multiprocessing import Process
import random
import time

def traffic_light(e):
    while True:
        if e.is_set() == True:           # 非阻塞，绿灯
            print('绿灯亮')
            time.sleep(3)
            e.clear()           # 绿灯变成红灯
        else:
            print('红灯亮')
            time.sleep(3)
            e.set()             # 红灯变成绿灯

def car(i,e):
    e.wait()
    print('%s通过'%(i))

if __name__ == '__main__':
    e = Event()
    # for i in range(100):
    tra_process = Process(target=traffic_light,args=(e,))
    tra_process.start()
    for i in range(100):
        if i%6 == 0:
            time.sleep(random.randint(1,3))
        car_process = Process(target=car,args=(i,e))
        car_process.start()
'''

# 3、队列：可以实现主进程和子进程的通信以及进程之前的通信，

# from multiprocessing import Queue
# q = Queue()           # 不限制队列的长度
# q = Queue(3)           # 限制队列的长度为3

# q.put(1)           # 添加数
# q.put('群雄逐鹿')           # 添加数
# print(q.get())          # 取数
# print(q.get())          # 取数
# print(q.qsize())            # qsize()     # 查询队列大小



# 4、主进程和子进程的通信通过队列
# from multiprocessing import Process
# from multiprocessing import Queue
# def func(q):
#     # print(q.get())
#     q.put('子进程传过来的数据')
# if __name__ == '__main__':
#     q = Queue()
#     # q.put('主进程传过来的数据')
#     p1 = Process(target=func,args=(q,))
#     p1.start()
#     print(q.get())


# 5、子进程和子进程通信通过队列
# from multiprocessing import Process
# from multiprocessing import Queue
# def func(q):
#     q.put('func子进程传过来的数据')
#
# def func1(q):
#     print(q.get())
#
# if __name__ == '__main__':
#     q = Queue()
#     p1 = Process(target=func,args=(q,))
#     p1.start()
#     p2 = Process(target=func1,args=(q,))
#     p2.start()

# 6、生产者消费者模型
'''
在并发编程中使用生产者和消费者模式能够解决绝大多数并发问题。
该模式通过平衡生产线程和消费线程的工作能力来提高程序的整体处理数据的速度。

为什么要使用生产者和消费者模式:
在线程世界里，生产者就是生产数据的线程，消费者就是消费数据的线程。
在多线程开发当中，如果生产者处理速度很快，而消费者处理速度很慢，那么生产者就必须等待消费者处理完，才能继续生产数据。
同样的道理，如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。
为了解决这个问题于是引入了生产者和消费者模式。

什么是生产者消费者模式:
生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。
生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列，
消费者不找生产者要数据，而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力。

'''
# 做包子的实例：
from multiprocessing import Process
from multiprocessing import Queue
import time
def producter(Q):
    for i in range(100):
        Q.put(i)
        # print('包子%s'%i)

def consumer(Q):
    for i in range(100):
        time.sleep(1)
        print('吃了包子%s'%(Q.get()))

if __name__ == '__main__':
    Q = Queue(10)
    p1 = Process(target=producter,args=(Q,))
    p1.start()
    p2 = Process(target=consumer,args=(Q,))
    p3 = Process(target=consumer,args=(Q,))     # 增加消费者
    p2.start()
    p3.start()
