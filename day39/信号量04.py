# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/20 9:12
# @Software       : Python_study
# @Python_verison : 3.7
# 信号量的本质就是锁，只是这个锁需要多把钥匙开

'''
from threading import Semaphore
se = Semaphore(5)
se.acquire()
se.acquire()
se.acquire()
se.acquire()
se.acquire()
print('jieshu')
se.acquire()            # 阻塞，因为最多可以支持5次acquire
'''


from threading import Semaphore
from threading import Thread
import time
def func(i,se):
    se.acquire()
    print('thread -%s start'%(i))
    time.sleep(1)
    print('thread -%s end' % (i))
    se.release()

se = Semaphore(5)
for i in range(10):
    t = Thread(target=func,args=(i,se,))
    t.start()


# 信号量和线程池（进程池）的区别：
    # 相同点：信号量在进行多次acquire后和线程池一样最毒只能执行你，信号量的n，和线程池的n

    # 不同点：开的线程数不一样：信号量是开启range后面的线程数，比如上面的10，而线程池最多只能开n个线程