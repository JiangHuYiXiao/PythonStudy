# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/7 10:49
# @Software       : Python_study
# @Python_verison : 3.7
# ipc机制---队列（进程间通信），队列也是双向通信，有锁的，安全的
# ipc机制---管道（进程间通信）,管道是双向通信，无锁的，不安全的
'''
# from multiprocessing import Pipe
# p1,p2 = Pipe()          # 两个端口
#
# # send()往管道中发数据
# p1.send('hello')

# recv()从管道中取数据
# print(p2.recv())
# # print(p2.recv())            # 阻塞
# p2.send('python')
# print(p1.recv())
# print(p1.recv())            # 阻塞

# close(),关闭端口，关闭后只可以取一次，再取的话报EOFError
# p1.close()
# print(p2.recv())
# print(p2.recv())            # EOFError，程序通过try 代码 except EOFError break来结束代码
# 没有关闭两次取则阻塞
# 关闭了，第一次取则可以取到数据，第二次报EOFError
'''

# 1、使用Pipe实现主进程和子进程的通信
# from multiprocessing import Process
# from multiprocessing import Pipe
# import os
# def func(son):
#     print(son.recv())
#     print('子进程pid为：%s'%(os.getpid()))
#     print('子进程的父进程pid为：%s'%(os.getppid()))
#     son.send('好的')
#     son.close()
#
# if __name__ == '__main__':
#     foo,son = Pipe()
#     main_process = Process(target=func,args=(son,))
#     main_process.start()
#     foo.send('孩子好好学习，将来有出息')
#     print('主进程的pid为：%s'%(os.getpid()))
#     print(foo.recv())


# 2、关闭管道触发EOFError
from multiprocessing import Process
from multiprocessing import Pipe
import os
def func(sp):
    foo,son = sp
    foo.close()                     # 在子进程中一来就先关闭父进程的端口，不会影响主进程中使用foo
    # print(son.recv())
    while True:
        try:
            print(son.recv())
        except EOFError:
            break
    print('子进程pid为：%s'%(os.getpid()))
    print('子进程的父进程pid为：%s'%(os.getppid()))


if __name__ == '__main__':
    foo,son = Pipe()
    main_process = Process(target=func,args=((foo,son),))
    main_process.start()
    son.close()                     # 在父进程中一来就先关闭子进程的端口，不会影响子进程中使用son
    foo.send('孩子好好学习，将来有出息')
    foo.send('孩子好好学习，将来有出息')
    foo.send('孩子好好学习，将来有出息')
    foo.send('孩子好好学习，将来有出息')
    foo.close()
    print('主进程的pid为：%s'%(os.getpid()))


# 3、用管道也能实现生产者消费者模型
# 因为管道的不安全，所以不使用管道来实现生产者消费者模型，
# socket做的三件事：等待数据、将数据发送到操作系统、操作系统再把数据拷贝到进程中
# 进程的通信，我们现在最好用队列在同一台机器上进行进程的通信，其实以后我们用的一般是rabbitmq、kafaka、redis消息中间件，基于网络来使不同机器的进程通信