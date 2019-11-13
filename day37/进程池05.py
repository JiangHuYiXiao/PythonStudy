# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/12 9:00
# @Software       : Python_study
# @Python_verison : 3.7
# 进程池：
# 定义一个池子，在里面放上固定数量的进程，有需求来了，就拿一个池中的进程来处理任务，等到处理完毕，进程并不关闭，而是将进程再放回进程池中继续等待任务。
# 如果有很多任务需要执行，池中的进程数量不够，任务就要等待之前的进程执行任务完毕归来，拿到空闲进程才能继续执行。
# 也就是说，池中进程的数量是固定的，那么同一时间最多有固定数量的进程在运行。这样不会增加操作系统的调度难度，还节省了开闭进程的时间，也一定程度上能够实现并发效果。


# 1、使用map方法，创建进程池执行代码，计算使用进程池创建所花的时间

# from multiprocessing import Pool
# from multiprocessing import Process
# import time
# def func(i):
#     print(i)
#     # time.sleep(1)
#
# if __name__ == '__main__':
#     po = Pool(5)                # 创建进程池对象，一般设置最大进程为电脑内核+1
#     start_time = time.time()
#     po.map(func,range(100))      # 创建进程,传参多个用元组
#     end_time = time.time() - start_time
#     print(end_time)         # 0.11222410202026367
#     po.close()              # 不允许再向进程池中添加任务
#     po.join()               # 使用join会使阻塞主进程，直到子进程结束后再去执行父进程后面的代码，添加close和join因为在mac上会出现后面的可能会在所有的子进程结束之前打印
#     print('+++++++')

# 2、多进程执行代码，计算所耗费的时间
# def func(i):
#     i+=1
#
# if __name__ == '__main__':
#     start_time = time.time()
#     l = []
#     for i in range(100):
#
#         p = Process(target=func,args=(i,))
#         p.start()
#
#         l.append(p)
#     [p.join() for p in l]
#     end_time = time.time() - start_time
#     print(end_time)         # 3.6670291423797607


# 结论：使用进程池创建进程执行代码所消耗的时间比使用多进程的快的多

# 3、apply方法，进程池同步
# from multiprocessing import Process
# from multiprocessing import Pool
# import time
# def func(i):
#     i +=1
#     print(i)
#     time.sleep(1)
#
# if __name__ == '__main__':
#     po = Pool(5)
#     for i in range(100):
#         po.apply(func,args=(i,))     # 创建进程

# 4、apply方法，进程池异步----常用
# from multiprocessing import Process
# from multiprocessing import Pool
# import time
# def func(i):
#     i +=1
#     print(i)
#     time.sleep(1)
#
# if __name__ == '__main__':
#     po = Pool(5)
#     for i in range(10):
#         po.apply_async(func,args=(i,))     # 创建进程
#     po.close()          # 必须在join之前先close，表示不允许再提交新的任务了
#     po.join()           # 等待子进程结束，不加就不会等待子进程结束，然后就子进程来不及输出结果


# 5、func函数有返回值，之前我们在多进程中，子进程是没有返回值的
from multiprocessing import Process
from multiprocessing import Pool
import time
def func(i):
    time.sleep(1)
    i +=1
    return i + 1

if __name__ == '__main__':
    po = Pool(5)
    res_l = []
    for i in range(10):
        res = po.apply_async(func,args=(i,))     # 创建进程
        res_l.append(res)
        # print(res.get())            # 阻塞，又变成同步,可以通过列表来保证异步

    po.close()          # 必须在join之前先close，表示不允许再提交新的任务了
    po.join()
    [print(i.get()) for i in res_l]             # 异步，一次性输出