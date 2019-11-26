# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/18 9:01
# @Software       : Python_study
# @Python_verison : 3.7
# 1、模块选择
    # 多线程提供了两个模块，Thread和threading模块，但是threading更加高级，所以我们以后使用threading模块
'''

# 2、开启进程是快的，而且是异步的
from threading import Thread
import os
import time
def func():
    time.sleep(1)
    print('hello world!',os.getpid())


t = Thread(target=func)
t.start()                       # 开进程很快,执行到后要等待1s，所以先输出后面的额，然后一秒后输出func函数内的内容，所以很明显是异步的。如果是同步那么肯定先执行func，后执行外面的print
print(os.getpid())



# 3、多线程---异步，先执行主线程
from threading import Thread
import time
import os
def func(i):
    time.sleep(1)
    print('%s %s hello world'%(i,os.getpid()))
for i in  range(10):
    t  = Thread(target=func,args=(i,))
    t.start()

print(os.getpid())

# 4、多线程同步，先执行子线程,使用join()方法
from threading import Thread
import time
import os
def func(i):
    time.sleep(1)
    print('%s %s hello world'%(i,os.getpid()))
for i in  range(10):
    t  = Thread(target=func,args=(i,))
    t.start()
    t.join()
print(os.getpid())


# 5、多线程是异步，先执行子线程（使用列表批量join），但是和后面的主线程是同步的一起输出
from threading import Thread
import time
import os
thread_list =[]
def func(i):
    time.sleep(1)
    print('%s %s hello world'%(i,os.getpid()))
for i in  range(10):
    t  = Thread(target=func,args=(i,))
    t.start()
    thread_list.append(t)
[t.join() for t in thread_list]         # 循环外，统一等待所有的线程结束，然后执行下面的print
print(os.getpid())


# 6、使用类开启多线程   ---同步
    # 必须实现run方法，必须继承Thread
import threading
class MyThread(threading.Thread):
    def __init__(self,args1,args2):
        super().__init__()
        self.args1 = args1
        self.args2 = args2

    def run(self):
        for i in range(10):
            print('%s-%s-%s hello world'%(i,self.args1,self.args2))

my_thread = MyThread('你','好')
my_thread.start()
print('hhhhhh')


# 7、计算线程的数量，在子线程中
import threading
import time
import os
class MyThread(threading.Thread):
    count = 0               # 静态属性 、线程的静态属性共享
    def __init__(self,args1,args2):
        super().__init__()
        self.args1 = args1
        self.args2 = args2

    def run(self):
        MyThread.count += 1             # 一开始就加上1
        time.sleep(1)
        print('%s-%s-%s hello world'%(self.args1,self.args2,os.getpid()))

for i in range(10):
    my_thread = MyThread(i,i*'*')
    my_thread.start()           # 全部开启所有的线程
print('end')
print(MyThread.count)


# 8、类继承的属性,name线程名称
import threading
import time
import os
class MyThread(threading.Thread):
    count = 0               # 静态属性 、线程的静态属性共享
    def __init__(self,args1,args2):
        super().__init__()
        self.args1 = args1
        self.args2 = args2

    def run(self):
        MyThread.count += 1             # 一开始就加上1
        time.sleep(1)
        print('%s-%s-%s-%s'%(self.args1,self.args2,self.name,os.getpid()))

for i in range(10):
    my_thread = MyThread(i,i*'*')
    my_thread.start()           # 全部开启所有的线程
print('end')
print(MyThread.count)
'''

# 9、使用threading模块中的方法
# currentThread()  返回线程对象
# getName()        返回线程的name
# ident            线程的id
import threading
import time
def func(i):
    time.sleep(1)
    print(i,threading.currentThread().getName())
    print(i,threading.currentThread().ident)
    # print(threading.activeCount())        返回正在运行的线程数
for i in range(10):
    t = threading.Thread(target=func,args=(i,))
    t.start()

print(threading.enumerate())          # 返回现在正在运行的线程列表           # [<_MainThread(MainThread, started 79764)>, <Thread(Thread-10, started 80332)>]
# [<_MainThread(MainThread, started 80880)>, <Thread(Thread-1, started 78500)>, <Thread(Thread-2, started 73412)>, <Thread(Thread-3, started 79788)>, <Thread(Thread-4, started 79456)>, <Thread(Thread-5, started 76888)>, <Thread(Thread-6, started 73436)>, <Thread(Thread-7, started 75948)>, <Thread(Thread-8, started 80844)>, <Thread(Thread-9, started 76936)>, <Thread(Thread-10, started 79396)>]
# <_MainThread(MainThread, started 80880)>  主线程
print(threading.activeCount())          # 返回正在运行的线程数