# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/10/31 9:22
# @Software       : Python_study
# @Python_verison : 3.7

# Process([group [, target [, name [, args [, kwargs]]]]])，由该类实例化得到的对象，表示一个子进程中的任务（尚未启动）

# 强调：
# 1. 需要使用关键字的方式来指定参数
# 2. args指定的为传给target函数的位置参数，是一个元组形式，必须有逗号

# 参数介绍：
# 1 group参数未使用，值始终为None
# 2 target表示调用对象，即子进程要执行的任务
# 3 args表示调用对象的位置参数元组，args=(1,2,'egon',)
# 4 kwargs表示调用对象的字典,kwargs={'name':'egon','age':18}
# 5 name为子进程的名称

# 1 p.start()：启动进程，并调用该子进程中的p.run()
# 2 p.run():进程启动时运行的方法，正是它去调用target指定的函数，我们自定义类的类中一定要实现该方法
# 3 p.terminate():强制终止进程p，不会进行任何清理操作，如果p创建了子进程，该子进程就成了僵尸进程，使用该方法需要特别小心这种情况。如果p还保存了一个锁那么也将不会被释放，进而导致死锁
# 4 p.is_alive():如果p仍然运行，返回True
# 5 p.join([timeout]):主线程等待p终止（强调：是主线程处于等的状态，而p是处于运行的状态）。timeout是可选的超时时间，需要强调的是，p.join只能join住start开启的进程，而不能join住run开启的进程
# 异步
# import os
# from multiprocessing import Process
# def func():
#     print('inner process:'+ str(os.getpid()))
# if __name__ == '__main__':
#     p1 = Process(target=func)           # 创建一个进程对象
#     p1.start()                          # 运行进程
#     print('main process:'+ str(os.getpid()))

# 同步
# def func():
#     print('inner process:'+ str(os.getpid()))
# if __name__ == '__main__':
#     print('我要去银行取钱')
#     func()
#     print('我取完了钱')

# 异步阻塞
# import time
# def func(money):
#     print('取%s元钱'%(money))
#     print('字进程PID:'+ str(os.getpid()))
#
# if __name__ == '__main__':
#     p1 = Process(target=func,args=(100,))
#     print('我去取钱了')
#     p1.start()
#     time.sleep(10)
#     print('我取了钱回来了')
#     print('主进程PID:'+ str(os.getpid()))
#
#     import time

# 同步阻塞
# def func(money):
#     print('取%s元钱' % (money))
#     print('字进程PID:' + str(os.getpid()))
#
#
# if __name__ == '__main__':
#     func(100)
#     print('我去取钱了')
#     time.sleep(10)
#     print('我取了钱回来了')
#     print('主进程PID:' + str(os.getpid()))

# 父进程，父进程和子进程是异步的
# import os
# from multiprocessing import Process
# import time
# def func(money):
#     print('取%s元钱' % (money))
#     print('子进程PID:'+ str(os.getpid()))
#     print('子进程的父进程PID:'+str(os.getppid()))
#
# if __name__ == '__main__':
#     p1 = Process(target=func,args=(100,))       # 创建进程
#     print('我去取钱了')
#     print('主进程PID:' + str(os.getpid()))
#     p1.start()                  # 启动进程
#     time.sleep(10)
#     print('主进程PID:'+ str(os.getpid()))
#     print('我取钱回来了')
'''
我去取钱了
取100元钱
子进程PID:13292
子进程的父进程PID:14544
主进程PID:14544
我取钱回来了
'''
# 主进程会等待子进程结束，不会先退出
# import os
# from multiprocessing import Process
# import time
# def func(money):
#     time.sleep(10)
#     print('取%s元钱' % (money))
#     print('子进程PID:'+ str(os.getpid()))
#     print('子进程的父进程PID:'+str(os.getppid()))
#
# if __name__ == '__main__':
#     p1 = Process(target=func,args=(100,))       # 创建进程
#     print('我去取钱了')
#     print('主进程PID:' + str(os.getpid()))
#     p1.start()                  # 启动进程
#     print('主进程PID:'+ str(os.getpid()))
#     print('我取钱回来了')

# 使用join会使阻塞主进程，直到子进程结束后再去执行父进程
# import os
# from multiprocessing import Process
# import time
# def func(money):
#     time.sleep(2)
#     print('取%s元钱' % (money))
#     print('子进程PID:'+ str(os.getpid()))
#     print('子进程的父进程PID:'+str(os.getppid()))
#
# if __name__ == '__main__':
#     p1 = Process(target=func,args=(100,))       # 创建进程
#     p1.start()                  # 启动进程
#     print('我去取钱了')
#     p1.join()
#     print('主进程PID:'+ str(os.getpid()))
#     print('我取钱回来了')

# 注意：在windows做创建进程时，必须放到if __name__ == '__main__':作用域内，否则的话会一直创建进程，直到内存满了。

# 开启多个子进程：
