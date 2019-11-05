# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/4 9:12
# @Software       : Python_study
# @Python_verison : 3.7

# 守护进程：
# 会随着主进程的代码执行结束而结束，正常的子进程没有执行完的时候主进程要一直等着。
# 守护进程下不能再创建子进程
# 必须在start之前设置P.daemon = True

# 1、创建守护进程
# import os
# from multiprocessing import Process
# def func():
#     print('子进程pid：',os.getpid())            # 不会执行
#     print('子进程的父进程pid：',os.getppid())            # 不会执行
# if __name__ == '__main__':
#     P =Process(target=func)
#     P.daemon = True
#     P.start()
#     print('主进程pid：',os.getpid())

# import time
# import os
# from multiprocessing import Process
# def func():
#     print('子进程pid：',os.getpid())
#     print('子进程的父进程pid：',os.getppid())
#     while True:
#         time.sleep(1)
#         print('时间已经过去了1s')
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.daemon = True               # 像这种情况如果不加守护进程则子进程会一直运行着
#     p.start()
#     for i in range(100):
#         # time.sleep(0.1)
#         print('*'* i)
#     print('主进程pid：',os.getpid())




# 2、守护进程中再开启子进程
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

# 3、守护进程随着主进程的代码执行结束而结束不会等待其他子进程
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
#     p1.daemon = True
#     p1.start()
#     print('主进程pid：', os.getpid())
#     p2 = Process(target=func1)
#     p2.start()
    # p1.join()           #添加join会等待所有的子进程

# 4、进程的其他方法和属性
# p.is_alive() 判断进程是否还活着
# p.terminate() 结束进程
# p.name  进程的名字
# p.pid  进程id
import os
import time
from multiprocessing import Process
def func():
    print('func')
    print('子进程1pid：', os.getpid())
    print('子进程1的父进程pid：', os.getppid())

if __name__ == '__main__':
    p = Process(target=func)
    p.start()
    print('主进程：',os.getpid())
    print(p.is_alive())
    print(p.name,p.pid)         # Process-1 9804
    p.terminate()
    time.sleep(0.2)
    print(p.is_alive())