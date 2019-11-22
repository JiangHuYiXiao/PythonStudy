# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/20 21:48
# @Software       : Python_study
# @Python_verison : 3.7

# 之前我们学习了线程、进程的概念，了解了在操作系统中进程是资源分配的最小单位,线程是CPU调度的最小单位。按道理来说我们已经算是把cpu的利用率提高很多了。
# 但是我们知道无论是创建多进程还是创建多线程来解决问题，都要消耗一定的时间来创建进程、创建线程、以及管理他们之间的切换。
# 随着我们对于效率的追求不断提高，基于单线程来实现并发又成为一个新的课题，即只用一个主线程（很明显可利用的cpu只有一个）情况下实现并发
# 对于单线程下，我们不可避免程序中出现io操作，但如果我们能在自己的程序中（即用户程序级别，而非操作系统级别）控制单线程下的多个任务能在一个任务遇到io阻塞时就切换到另外一个任务去计算，
# 这样就保证了该线程能够最大限度地处于就绪态，即随时都可以被cpu执行的状态，相当于我们在用户程序级别将自己的io操作最大限度地隐藏起来，从而可以迷惑操作系统，让其看到：
# 该线程好像是一直在计算，io比较少，从而更多的将cpu的执行权限分配给我们的线程。

# 定义：# 协程的本质就是在单线程下，由用户自己控制一个任务遇到io阻塞了就切换另外一个任务去执行，以此来提升效率。
# 协程：是单线程下的并发，又称微线程，纤程。英文名Coroutine。一句话说明什么是协程：协程是一种用户态的轻量级线程，即协程是由用户程序自己控制调度的。、

# 为了实现它，我们需要找寻一种可以同时满足以下条件的解决方案：
#1. 可以控制多个任务之间的切换，切换之前将任务的状态保存下来，以便重新运行时，可以基于暂停的位置继续执行。
#2. 作为1的补充：可以检测io操作，在遇到io操作的情况下才发生切换


# 需要强调的是：

# #1. python的线程属于内核级别的，即由操作系统控制调度（如单线程遇到io或执行时间过长就会被迫交出cpu执行权限，切换其他线程运行）
# #2. 单线程内开启协程，一旦遇到io，就会从应用程序级别（而非操作系统）控制切换，以此来提升效率（！！！非io操作的切换与效率无关）

# 对比操作系统控制线程的切换，用户在单线程内控制协程的切换
# 优点如下：
# #1. 协程的切换开销更小，属于程序级别的切换，操作系统完全感知不到，因而更加轻量级
# #2. 单线程内就可以实现并发的效果，最大限度地利用cpu

# 缺点如下：
# #1. 协程的本质是单线程下，无法利用多核，可以是一个程序开启多个进程，每个进程内开启多个线程，每个线程内开启协程
# #2. 协程指的是单个线程，因而一旦协程出现阻塞，将会阻塞整个线程

# 总结协程特点：
# 必须在只有一个单线程里实现并发
# 修改共享数据不需加锁
# 用户程序里自己保存多个控制流的上下文栈
# 附加：一个协程遇到IO操作自动切换到其它协程（如何实现检测IO，yield、greenlet都无法实现，就用到了gevent模块（select机制））

# 我们之前学的生成器的yield就有这个效果，保存状态，切换任务，但是没法规避IO时间
'''
# 1、通过yield实现交换执行
def func1():
    print(1)
    yield
    print(3)
    yield

def func2():
    g = func1()
    next(g)
    print(2)
    next(g)
    print(4)

func2()


# 2、通过yield实现生产者消费者模型
def consumer():
    while True:
        n = yield
        print('消费了包子%s'%(n))
        print(n)


def producter():
    g = consumer()
    g.__next__()
    for i in range(10):
        print('生产了包子%s'%(i))
        g.send(i)

producter()

# 3、使用greenlet模块实现任务切换
from greenlet import greenlet           # 在单线程中切换状态的模块

def eat1():
    print('吃馒头')
    g2.switch()         # # 表示切换到eat2
    print('平时不努力')
    g2.switch()

def eat2():
    print('吃包子')
    g1.switch()
    print('战时必哭泣')

g1 = greenlet(eat1)
g2 = greenlet(eat2)
g1.switch()         # 表示切换到eat1
'''

# 4、使用gevent模块实现协程间的切换，gevent内部就封装了greenlet模块
# 正常的在代码间（yield，greenlet）切换会降低效率
# 如果在有IO的情况下进行切换，反而会更快
# 不管是yield还是greenlet都不能规避IO等待，只有gevent可以规避IO

# g1=gevent.spawn(func,1,,2,3,x=4,y=5)创建一个协程对象g1，spawn括号内第一个参数是函数名，如eat，后面可以有多个参数，可以是位置实参或关键字实参，都是传给函数eat的
# g2=gevent.spawn(func2)
# g1.join() #等待g1结束
# g2.join() #等待g2结束
# #或者上述两步合作一步：gevent.joinall([g1,g2])
# g1.value#拿到func1的返回值

import gevent

def func1():
    print(123)
    gevent.sleep(3)
    # 使用gevent自己的time才能够被识别，遇到这个就会切换，识别不了我们通用的time模块，
    # 如果想要识别time模块那么可以在执行文件收行加上from gevent import  monkey;monkey.patch_all()就可以识别time模块的IO
    print(456)

def func2():
    print('hhhh')
    gevent.sleep(4)             # 使用gevent自己的time才能够被识别
    print('end')

g1 = gevent.spawn(func1)            # 创建一个协程对象g1
g2 = gevent.spawn(func2)            # 创建一个协程对象g2
# g1.join()
# g2.join()
gevent.joinall([g1,g2])             # 等价于g1.join()和g2.join()两个



